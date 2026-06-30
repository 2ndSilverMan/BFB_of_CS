# 네트워크 보안 기초 (Network Security Basics)

- Level: Intermediate
- Prerequisites: [Systems/Networks/TCP-UDP.md](TCP-UDP.md), [Systems/Networks/HTTP.md](HTTP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

네트워크 보안 기초는 통신의 기밀성·무결성·가용성을 위협하는 공격과 방어 수단을 다룬다. 방화벽, TLS, VPN, 인증, 일반적 공격(MITM, DDoS, 스푸핑)을 포함한다.

## 직관 (Intuition)

네트워크는 기본적으로 신뢰할 수 없는 매체다 — 누군가 엿보거나, 가로채거나, 가장할 수 있다. 보안은 "도청해도 못 읽게(암호화), 바꾸면 들키게(무결성), 상대가 진짜인지 확인(인증), 마비시켜도 버티게(가용성)" 만드는 일이다.

## 이론 (Theory)

핵심 목표(CIA): 기밀성, 무결성, 가용성. 주요 위협과 방어:

- **도청·MITM**: TLS로 암호화·인증. 인증서로 서버 신원 확인.
- **스푸핑**: IP/ARP/DNS 위조 → 인증·DNSSEC·필터링.
- **DDoS**: 다수 호스트로 자원 고갈 → 레이트 리밋, CDN, 스크러빙.
- **포트 스캔·침입**: 방화벽(패킷 필터/상태 기반), IDS/IPS.

**계층별 방어(defense in depth)**: 경계(방화벽) + 전송(TLS) + 응용(인증·검증)을 겹쳐 둔다. 최소 권한·제로 트러스트가 현대 원칙이다.

## 구현 (Implementation)

```text
# 방화벽 규칙(개념): 기본 거부 + 필요한 것만 허용
default policy: DROP
allow  in  tcp 443  (HTTPS)
allow  in  tcp 22  from 10.0.0.0/8  (관리 SSH, 사내만)
allow  out established
deny   all else
```

## 복잡도 (Complexity)

보안은 알고리즘 복잡도가 아니라 위협 모델과 트레이드오프의 문제다. 암호화·검사는 약간의 지연·CPU를 더하지만, 침해 비용에 비하면 작다. DDoS 방어는 정상/공격 트래픽 구분이라는 통계·용량 문제다.

## 응용 (Applications)

- 기업 경계 방화벽·세그멘테이션
- TLS로 보호되는 웹·API
- VPN을 통한 원격 접속
- 클라우드 보안 그룹·WAF

## 흔한 오해 (Common Misunderstandings)

- 방화벽만으로 안전하지 않다 — 다계층 방어가 필요하다.
- 암호화는 기밀성을 주지만 가용성(DDoS)이나 잘못된 로직은 못 막는다.
- 내부 네트워크가 "안전"하다는 가정은 위험하다(제로 트러스트의 출발점).
- 보안은 한 번 설정하고 끝이 아니라 지속적 패치·모니터링이다.

## TMI

- "제로 트러스트"는 "절대 신뢰하지 말고 항상 검증하라"는 원칙으로, 경계 기반 보안의 한계에서 나왔다.
- 가장 흔한 침해 경로는 정교한 해킹이 아니라 피싱·약한 비밀번호·미패치다.
- TLS의 인증서 검증 실패를 무시하는 코드는 MITM에 문을 열어 주는 흔한 실수다.

## 연습 / 확인 문제 (Exercises)

- 기본 거부 방화벽 정책에서 웹 서버에 필요한 규칙을 작성하라.
- MITM 공격을 TLS가 어떻게 막는지 설명하라.
- DDoS와 일반 고부하를 구분하기 어려운 이유를 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [소켓 프로그래밍](Socket-Programming.md)
- 다음: [Engineering/Security/PKI-and-TLS.md](../../Engineering/Security/PKI-and-TLS.md), [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md)

## 참조 (References)

- [Engineering/Security/PKI-and-TLS.md](../../Engineering/Security/PKI-and-TLS.md)
- [Engineering/Security/Auth.md](../../Engineering/Security/Auth.md)
- [Reference/Books.md](../../Reference/Books.md)
