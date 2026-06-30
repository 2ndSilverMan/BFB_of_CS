# 네트워크 보안 (Network Security)

- Level: Intermediate
- Prerequisites: [Systems/Networks/Network-Models.md](../../Systems/Networks/Network-Models.md), [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md), [PKI-and-TLS.md](PKI-and-TLS.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

네트워크 보안은 통신 경로에서 기밀성, 무결성, 인증, 가용성을 지키기 위한 기술과 운영 원칙이다. TLS, 방화벽, 네트워크 분리, VPN, IDS/IPS, rate limiting, DDoS 대응 등이 포함된다.

## 직관 (Intuition)

네트워크는 여러 문과 복도, 우편함이 있는 건물과 비슷하다. 누구를 들일지, 어떤 방까지 갈 수 있는지, 오가는 편지가 바뀌지 않았는지, 복도가 막히지 않는지 계속 관리해야 한다.

## 이론 (Theory)

네트워크 보안은 계층별로 나누어 생각하면 좋다.

- Link/network layer: VLAN, routing policy, IP filtering, VPN
- Transport layer: TLS, mTLS, TCP hardening, rate limit
- Application layer: 인증, 권한, input validation, API gateway
- 운영 계층: logging, monitoring, incident response, patching

주요 위협은 eavesdropping, spoofing, tampering, replay, lateral movement, DDoS, misconfiguration이다. 방어는 단일 장치보다 defense in depth로 설계한다.

### Segmentation과 blast radius

네트워크 분리는 침입을 완전히 막는 장치가 아니라 침해 범위를 줄이는 장치다. Public subnet, application subnet, data subnet, management plane을 나누고, east-west traffic도 필요한 경로만 허용한다.

정책은 "열어야 하는 포트" 목록보다 "허용된 source identity, destination, protocol, purpose"로 문서화하는 편이 안전하다.

### Zero Trust 운영

Zero Trust는 내부망을 무조건 신뢰하지 않는다는 원칙이다. 요청마다 신원, 장치 상태, 서비스 권한, 정책을 확인하고, 네트워크 위치는 신뢰의 보조 신호로만 사용한다. mTLS, service identity, short-lived credentials, continuous monitoring이 핵심 도구다.

### 관찰 가능성과 대응

방화벽이나 IDS 경고는 대응 절차가 없으면 가치가 작다. Flow log, DNS log, auth log, application log를 상관 분석할 수 있어야 하고, 의심스러운 lateral movement를 발견했을 때 격리·차단·증거 보존 절차가 있어야 한다.

## 구현 (Implementation)

네트워크 보안 점검은 서비스 경계별로 표로 관리할 수 있다.

```text
service     exposed?   auth      tls     inbound policy
api         public     OAuth     yes     only 443
db          private    mTLS      yes     app subnet only
metrics     private    token     yes     ops subnet only
```

실제 설정은 조직의 클라우드, 온프레미스, 서비스 메시, 방화벽 정책에 맞춰 관리한다.

## 복잡도 (Complexity)

보안 장치를 늘리면 보호는 강해질 수 있지만 운영 복잡도와 장애 지점도 늘어난다. 암호화는 CPU 비용과 인증서 운영을 요구하고, 세밀한 네트워크 정책은 변경 관리와 관찰 가능성이 필요하다.

## 응용 (Applications)

- 서비스 간 mTLS
- 내부망 segmentation
- API gateway와 WAF 운영
- DDoS 완화와 rate limiting
- 침해 탐지와 로그 상관 분석

## 흔한 오해 (Common Misunderstandings)

- 내부망이라고 안전하다고 가정하면 안 된다.
- TLS만 켜면 네트워크 보안이 끝나는 것이 아니다.
- 방화벽 규칙은 시간이 지나며 예외가 쌓이므로 주기적 검토가 필요하다.
- 보안 로그를 수집만 하고 경보·대응이 없으면 효과가 제한적이다.

## TMI

- Zero Trust는 네트워크 위치만으로 신뢰하지 않고 지속적으로 인증·인가하자는 운영 철학이다.
- 서비스 메시지는 mTLS와 traffic policy를 애플리케이션 밖에서 관리할 수 있게 해준다.
- 네트워크 보안 사고는 기술 취약점보다 잘못 열린 포트나 과한 권한에서 시작되는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- 기밀성, 무결성, 인증, 가용성을 네트워크 예시로 설명하라.
- public API와 private database의 inbound policy를 설계해 보라.
- 내부망 신뢰 모델과 Zero Trust 모델의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Web Security](Web-Security.md)
- 다음: [Engineering/DevOps/](../DevOps/)

## 참조 (References)

- [Systems/Networks/Network-Models.md](../../Systems/Networks/Network-Models.md)
- [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)
- [PKI-and-TLS.md](PKI-and-TLS.md)
- [Reference/Books.md](../../Reference/Books.md)
