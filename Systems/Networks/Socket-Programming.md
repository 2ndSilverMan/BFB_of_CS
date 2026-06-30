# 소켓 프로그래밍 (Socket Programming)

- Level: Intermediate
- Prerequisites: [Systems/Networks/TCP-UDP.md](TCP-UDP.md), [Systems/Operating-Systems/Processes-and-Threads.md](../Operating-Systems/Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

소켓은 네트워크 통신의 종단점을 추상화한 OS 인터페이스다. 소켓 API(socket, bind, listen, accept, connect, send, recv)로 TCP·UDP 통신을 프로그래밍한다.

## 직관 (Intuition)

소켓은 "네트워크로 연결된 파일"처럼 다룰 수 있는 손잡이다. 서버는 특정 포트에서 연결을 기다리고(listen/accept), 클라이언트는 그 주소로 연결한다(connect). 연결되면 양쪽이 파일을 읽고 쓰듯 데이터를 주고받는다. OS가 TCP/IP의 복잡함을 이 단순한 API 뒤로 숨긴다.

## 이론 (Theory)

소켓은 (IP, 포트, 프로토콜)로 식별된다. **TCP(스트림)**:
1. 서버: `socket → bind → listen → accept`
2. 클라이언트: `socket → connect`
3. 양방향 `send`/`recv`, 종료 `close`.

**UDP(데이터그램)**는 연결 없이 `sendto`/`recvfrom`. TCP는 바이트 스트림이라 메시지 경계가 없어 애플리케이션이 프레이밍(길이 접두사·구분자)을 정해야 한다. 동시 다중 연결은 스레드/프로세스, 또는 I/O 멀티플렉싱(`select`/`epoll`)·비동기로 처리한다.

## 구현 (Implementation)

```python
import socket
# TCP 에코 서버
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("0.0.0.0", 9000))
srv.listen()
conn, addr = srv.accept()          # 연결 수락(블로킹)
while (data := conn.recv(4096)):
    conn.sendall(data)             # 받은 것을 그대로 반송
conn.close()
```

## 복잡도 (Complexity)

소켓 호출 자체는 상수 시간이지만, 동시성 모델이 확장성을 좌우한다. 연결당 스레드는 수천 연결에서 비용이 크고, `epoll`/`kqueue` 같은 이벤트 기반 멀티플렉싱은 `O(활성 이벤트 수)`로 수만~수십만 연결(C10K 문제)을 처리한다.

## 응용 (Applications)

- 웹 서버·프록시·데이터베이스 드라이버
- 실시간 게임·채팅·스트리밍
- RPC·메시지 큐의 전송 계층
- IoT 장치 통신

## 흔한 오해 (Common Misunderstandings)

- TCP는 메시지가 아니라 바이트 스트림이다 — `recv` 한 번이 한 메시지를 보장하지 않는다(프레이밍 필요).
- `send`가 요청한 바이트를 모두 보냈다고 보장하지 않는다(반환값 확인, `sendall`).
- 블로킹 소켓은 한 연결에서 멈추면 다른 연결을 못 본다(멀티플렉싱·스레드 필요).
- `SO_REUSEADDR` 없이 재시작하면 "address already in use"가 날 수 있다.

## TMI

- "C10K 문제"는 한 서버가 동시 1만 연결을 다루는 도전으로, `epoll`/`kqueue` 등 이벤트 기반 I/O를 대중화했다.
- 버클리 소켓 API(1983, BSD)는 40년 넘게 사실상 표준으로 남아 있다.
- Nagle 알고리즘(작은 패킷 합치기)은 지연에 민감한 앱에서 `TCP_NODELAY`로 끄곤 한다.

## 연습 / 확인 문제 (Exercises)

- TCP 에코 서버/클라이언트를 작성하고 메시지 경계 문제를 관찰하라.
- 길이 접두사 프레이밍으로 메시지 경계를 복원하라.
- 블로킹과 `select` 기반 다중 연결 처리를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [DNS](DNS.md)
- 다음: [네트워크 보안 기초](Network-Security-Basics.md)

## 참조 (References)

- [Systems/Networks/TCP-UDP.md](TCP-UDP.md)
- [Systems/Operating-Systems/Processes-and-Threads.md](../Operating-Systems/Processes-and-Threads.md)
- [Reference/Books.md](../../Reference/Books.md)
