# HTTP / HTTPS

- Level: Intermediate
- Prerequisites: [Systems/Networks/TCP-UDP.md](TCP-UDP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

HTTP는 웹에서 클라이언트와 서버가 자원을 주고받는 응용 계층 요청-응답 프로토콜이다. HTTPS는 HTTP를 TLS로 암호화해 기밀성·무결성·인증을 더한 것이다.

## 직관 (Intuition)

브라우저가 "이 주소의 페이지를 줘"라고 요청하면 서버가 "여기 있어"라고 응답한다 — 이 단순한 대화가 HTTP다. 각 요청은 메서드(GET/POST 등), 경로, 헤더, 본문으로 구성된다. HTTPS는 그 대화를 도청·변조할 수 없게 봉투에 넣어 보낸다.

## 이론 (Theory)

**요청/응답 구조**: 요청 라인(메서드 + URL + 버전), 헤더, 본문. 응답은 상태 코드(2xx 성공, 3xx 리다이렉트, 4xx 클라이언트 오류, 5xx 서버 오류) + 헤더 + 본문.

**메서드 의미**: GET(조회, 안전·멱등), POST(생성), PUT(멱등 교체), DELETE, PATCH.

**상태 비저장(stateless)**: 각 요청은 독립적이다. 상태는 쿠키·토큰·세션으로 보완한다.

**버전**: HTTP/1.1(지속 연결), HTTP/2(멀티플렉싱, 헤더 압축), HTTP/3(QUIC, UDP 기반). **HTTPS**는 TLS 핸드셰이크로 세션 키를 교환한 뒤 대칭 암호로 통신한다.

## 구현 (Implementation)

```text
GET /index.html HTTP/1.1
Host: example.com
Accept: text/html

HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1234

<!DOCTYPE html>...
```

```python
import urllib.request
with urllib.request.urlopen("https://example.com") as r:
    print(r.status)                # 200
    print(r.headers["Content-Type"])
```

## 복잡도 (Complexity)

HTTP 성능은 알고리즘 복잡도보다 왕복 지연(RTT), 연결 수립 비용(TCP+TLS 핸드셰이크), 본문 크기에 좌우된다. HTTP/2 멀티플렉싱과 HTTP/3의 0-RTT는 이 지연을 줄이려는 진화다. 캐싱(`Cache-Control`, ETag)이 유효 성능을 크게 바꾼다.

## 응용 (Applications)

- 웹 페이지·API(REST) 통신
- 마이크로서비스 간 호출
- 모바일 앱 백엔드
- 파일 다운로드·스트리밍

## 흔한 오해 (Common Misunderstandings)

- GET은 본문을 가질 수 있으나 의미가 없고, 부수 효과를 주면 안 된다(안전성).
- HTTPS는 데이터를 암호화하지만 서버가 누구인지(인증)도 함께 보장한다.
- 상태 코드 200이 곧 "정상 처리"는 아니다(본문에 오류가 있을 수 있음, API 설계 의존).
- 쿠키 자체가 세션이 아니다 — 세션을 식별하는 수단일 뿐이다.

## TMI

- HTTP/2의 멀티플렉싱은 1.1의 "head-of-line blocking"을 줄였지만, TCP 수준 HOL은 HTTP/3(QUIC)에서야 해결됐다.
- 418 "I'm a teapot"은 만우절 농담(RFC 2324)에서 온 실제 상태 코드다.
- TLS 1.3은 핸드셰이크를 1-RTT로 줄이고 재방문 시 0-RTT를 지원한다.

## 연습 / 확인 문제 (Exercises)

- GET과 POST의 멱등성·안전성 차이를 설명하라.
- 301과 302 리다이렉트의 차이를 말하라.
- HTTPS 핸드셰이크에서 비대칭·대칭 암호가 각각 어디에 쓰이는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [TCP와 UDP](TCP-UDP.md)
- 다음: [DNS](DNS.md), [Engineering/Security/PKI-and-TLS.md](../../Engineering/Security/PKI-and-TLS.md)

## 참조 (References)

- [Systems/Networks/TCP-UDP.md](TCP-UDP.md)
- [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md)
- [Reference/Books.md](../../Reference/Books.md)
