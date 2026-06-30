# 공개키 기반 구조와 TLS (PKI and TLS)

- Level: Intermediate
- Prerequisites: [Engineering/Security/Digital-Signatures.md](Digital-Signatures.md), [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

공개키 기반 구조(PKI)는 공개키를 이름·조직·도메인 같은 신원과 연결하는 인증서, 인증 기관(CA), 정책과 폐기 절차의 체계다. TLS는 PKI와 키 합의, 인증 암호를 결합해 네트워크 연결의 기밀성·무결성과 상대 인증을 제공한다.

## 직관 (Intuition)

서버가 공개키를 내미는 것만으로는 그것이 진짜 서버의 키인지 알 수 없다. 인증서는 신뢰된 기관이 "이 도메인과 이 공개키가 연결된다"고 서명한 전자 신분증이다. 클라이언트는 루트 인증서까지 서명 사슬과 도메인 이름을 검사한 뒤 임시 세션 키를 합의한다.

```mermaid
flowchart LR
    R[신뢰 저장소의 Root CA] --> I[Intermediate CA]
    I --> S[서버 인증서]
    S --> H[호스트 이름·기간·용도 검증]
    H --> K[임시 키 합의]
    K --> A[AEAD로 애플리케이션 데이터 보호]
```

## 이론 (Theory)

X.509 인증서에는 주체, 공개키, 발급자, 유효 기간, 확장 필드와 발급자의 서명이 들어간다. 검증자는 대략 다음을 함께 확인한다.

- 서명 체인이 신뢰 저장소의 루트로 이어지는가
- 현재 시각이 유효 기간 안에 있는가
- 요청한 호스트 이름이 Subject Alternative Name과 맞는가
- 키 용도와 기본 제약이 인증서 역할에 맞는가
- 정책상 필요한 폐기 상태와 알고리즘 요구사항을 만족하는가

TLS 1.3 핸드셰이크는 지원 버전과 암호 스위트를 협상하고, 일반적으로 임시 (EC)DH 키 합의로 트래픽 키를 만든 뒤 서버가 인증서 개인키 소유를 증명한다. 이후 레코드는 AEAD로 보호한다. 0-RTT 데이터는 재전송 가능성이 있으므로 멱등성이 없는 요청에 신중해야 한다.

### 인증서 검증 파이프라인

TLS 검증은 체인 서명, hostname, 유효 기간, key usage, basic constraints, 정책, 폐기 상태를 함께 본다. 중간 인증서 누락, wildcard 범위 오해, 내부 도메인 이름 불일치가 운영에서 자주 발생한다.

검증을 끄는 플래그는 테스트 편의 기능이 아니라 보안 경계 제거다. 개발 환경에서도 자체 CA를 명시적으로 신뢰하도록 구성한다.

### mTLS와 서비스 신원

mTLS는 클라이언트도 인증서를 제시해 서비스 간 신원을 확인한다. 이때 인증서 subject를 권한으로 직접 쓰기보다 SPIFFE ID나 service identity를 정책 엔진에 연결한다. 인증서 발급·회전 자동화가 없으면 mTLS는 운영 부채가 된다.

### 갱신과 사고 대응

인증서는 만료 전 자동 갱신, 배포 확인, 실패 알림이 필요하다. 키 유출이나 오발급 사고가 나면 폐기, 교체, pinning 업데이트, 영향 범위 확인 절차가 있어야 한다. Certificate Transparency 모니터링은 공개 인증서 오발급 탐지에 도움을 준다.

## 구현 (Implementation)

파이썬의 기본 신뢰 저장소와 호스트 이름 검증을 유지한 TLS 클라이언트 예시다.

```python
import socket
import ssl

context = ssl.create_default_context()
with socket.create_connection(("example.com", 443), timeout=5) as raw:
    with context.wrap_socket(raw, server_hostname="example.com") as tls:
        print(tls.version())
        print(tls.getpeercert()["subjectAltName"])
```

인증서 오류를 피하려고 검증을 끄거나 모든 인증서를 허용하지 않는다. 개발 환경에서는 자체 CA를 신뢰 저장소에 명시적으로 추가한다.

## 복잡도 (Complexity)

핸드셰이크는 인증서 체인 길이와 공개키 연산에 비례하는 초기 비용이 있고 네트워크 왕복 지연도 필요하다. 연결 뒤 데이터 처리는 길이 $L$에 대해 대칭 AEAD의 `O(L)` 비용이 중심이다. 연결 재사용은 지연과 연산을 크게 줄인다.

## 응용 (Applications)

- HTTPS와 API 통신
- 데이터베이스·메시지 브로커의 전송 구간 암호화
- mTLS를 통한 클라이언트와 서버의 상호 인증
- 내부 서비스의 인증서 기반 신원과 키 회전

## 흔한 오해 (Common Misunderstandings)

- HTTPS는 서버 애플리케이션이 정직하거나 취약점이 없다는 보장이 아니다.
- 인증서 체인 서명만 확인해서는 부족하다. 호스트 이름과 유효 기간, 용도도 검사해야 한다.
- 자체 서명 인증서가 수학적으로 약하다는 뜻은 아니다. 안전한 신뢰 배포 경로가 없다는 점이 문제다.
- TLS 종료 지점 이후의 프록시·로그·저장소 데이터는 별도로 보호해야 한다.

## TMI

- 루트 CA 인증서는 보통 자기 서명되어 있지만, 신뢰의 근거는 그 서명이 아니라 운영체제나 브라우저의 신뢰 저장소 배포 정책이다.
- Certificate Transparency 로그는 공개적으로 발급된 인증서를 감시해 오발급 탐지를 돕는다.
- TLS 1.3은 오래된 키 교환과 암호 구성을 대폭 제거해 협상 공간을 단순화했다.

## 연습 / 확인 문제 (Exercises)

- 브라우저에서 한 사이트의 인증서 체인과 Subject Alternative Name을 확인하라.
- 인증서 서명은 유효하지만 호스트 이름이 다른 경우 클라이언트가 거부해야 하는 이유를 설명하라.
- TLS 종료 프록시를 사용하는 시스템에서 평문이 존재하는 구간을 그려 보라.

## 이어서 읽기 (Reading Path)

- 이전: [디지털 서명](Digital-Signatures.md)
- 다음: [인증과 인가](Auth.md)
- 관련: [TCP와 UDP](../../Systems/Networks/TCP-UDP.md)

## 참조 (References)

- [RFC 8446: The Transport Layer Security Protocol Version 1.3](https://www.rfc-editor.org/rfc/rfc8446.html)
- [RFC 5280: Internet X.509 PKI Certificate Profile](https://www.rfc-editor.org/rfc/rfc5280.html)
- [OWASP Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
- [Reference/Books.md](../../Reference/Books.md)
