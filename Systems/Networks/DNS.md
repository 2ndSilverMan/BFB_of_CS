# DNS (Domain Name System)

- Level: Beginner
- Prerequisites: [Systems/Networks/IP-and-Routing.md](IP-and-Routing.md), [Systems/Networks/TCP-UDP.md](TCP-UDP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

DNS는 사람이 읽는 도메인 이름(example.com)을 기계가 쓰는 IP 주소로 변환하는 분산 계층형 디렉터리 시스템이다. 인터넷의 "전화번호부" 역할을 한다.

## 직관 (Intuition)

사람은 숫자 IP를 외우기 어렵다. DNS는 이름을 주소로 바꿔 준다. 전 세계 이름을 한 서버가 다 알 수는 없으므로, 도메인을 점(.)으로 나눠 계층적으로 분담하고, 각 단계의 서버에게 "다음은 누구에게 물어봐"를 안내받으며 답을 찾아간다.

## 이론 (Theory)

이름 공간은 트리다: 루트(.) → TLD(.com) → 권한(authoritative) 서버. **재귀 해석(recursive resolver)**이 사용자 대신 루트→TLD→권한 서버를 차례로 질의한다(반복적 질의).

주요 레코드: A(IPv4), AAAA(IPv6), CNAME(별칭), MX(메일), NS(네임서버), TXT. **캐싱**과 TTL로 반복 질의를 줄인다. 대부분 UDP 53번을 쓰고, 응답이 크거나 영역 전송은 TCP를 쓴다. DNSSEC은 응답에 서명해 위조를 막고, DoH/DoT는 질의를 암호화한다.

## 구현 (Implementation)

```python
import socket
print(socket.gethostbyname("example.com"))   # A 레코드 조회 -> IP

# 해석 흐름(개념):
# stub resolver -> recursive resolver -> root(.) -> TLD(.com) -> authoritative
# 각 단계는 "다음에 물어볼 서버"를 알려 주고, resolver가 반복 질의
```

## 복잡도 (Complexity)

이름 해석은 보통 캐시 히트면 수 밀리초, 미스면 여러 왕복으로 수십~수백 ms다. 트리 깊이가 얕아(보통 3~4단계) 질의 수가 작고, 캐싱이 전체 시스템 부하를 극적으로 줄인다. 성능 지표는 지연과 캐시 적중률이다.

## 응용 (Applications)

- 모든 웹·이메일·앱의 이름 해석
- 로드 밸런싱·장애 조치(여러 A 레코드, 짧은 TTL)
- CDN의 사용자 근접 서버 선택
- 서비스 디스커리(내부 DNS)

## 흔한 오해 (Common Misunderstandings)

- DNS는 데이터를 전송하지 않는다. 이름→주소 변환만 한다.
- CNAME은 또 다른 이름을 가리키지 IP를 직접 주지 않는다.
- TTL이 길면 변경 전파가 느리다(전환 전 미리 줄이는 이유).
- 기본 DNS는 암호화·인증이 없어 위조·도청에 취약하다(DNSSEC/DoH 필요).

## TMI

- DNS는 1983년 등장 전까지 단일 `HOSTS.TXT` 파일로 관리됐다 — 확장 불가능했다.
- "It's always DNS"는 장애 원인 추적에서 DNS가 자주 범인이라는 운영자들의 농담이다.
- 루트 네임서버는 논리적으로 13개(A~M)지만 애니캐스트로 전 세계 수백 대에 복제돼 있다.

## 연습 / 확인 문제 (Exercises)

- `nslookup`/`dig`로 도메인의 A·MX 레코드를 조회하라.
- 재귀 질의와 반복 질의의 차이를 그림으로 설명하라.
- TTL이 캐싱과 변경 전파에 주는 영향을 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [HTTP / HTTPS](HTTP.md)
- 다음: [소켓 프로그래밍](Socket-Programming.md), [CDN과 로드 밸런싱](CDN-and-Load-Balancing.md)

## 참조 (References)

- [Systems/Networks/IP-and-Routing.md](IP-and-Routing.md)
- [Systems/Networks/CDN-and-Load-Balancing.md](CDN-and-Load-Balancing.md)
- [Reference/Books.md](../../Reference/Books.md)
