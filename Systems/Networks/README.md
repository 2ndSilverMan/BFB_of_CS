# 컴퓨터 네트워크 (Networks)

> 컴퓨터들이 서로 통신하는 방법.

**선수지식**: [Systems/Operating-Systems/](../Operating-Systems/) (기초)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 네트워크 계층 모델 (OSI / TCP/IP) | [Network-Models.md](Network-Models.md) | Draft |
| 물리 계층과 데이터 링크 계층 | Physical-and-Link.md | Planned |
| IP 주소와 라우팅 | IP-and-Routing.md | Planned |
| TCP와 UDP | [TCP-UDP.md](TCP-UDP.md) | Draft |
| HTTP / HTTPS | HTTP.md | Planned |
| DNS | DNS.md | Planned |
| 소켓 프로그래밍 | Socket-Programming.md | Planned |
| 네트워크 보안 기초 | Network-Security-Basics.md | Planned |
| CDN과 로드 밸런싱 | CDN-and-Load-Balancing.md | Planned |

---

## 학습 순서

```text
Network-Models → Physical-and-Link → IP-and-Routing
       ↓
TCP-UDP → DNS → HTTP
       ↓
Socket-Programming → Network-Security-Basics → CDN-and-Load-Balancing
```

---

## 연관 섹션

- [Systems/Operating-Systems/](../Operating-Systems/) — 소켓, 프로세스, 커널 네트워크 스택
- [Systems/Distributed-Systems/](../Distributed-Systems/) — 네트워크 위에서 동작하는 분산 프로토콜
- [Engineering/Security/](../../Engineering/Security/) — TLS, 네트워크 보안, 인증
- [Engineering/DevOps/](../../Engineering/DevOps/) — 클라우드 네트워킹과 서비스 운영
