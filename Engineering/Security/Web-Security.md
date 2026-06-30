# 웹 보안 (Web Security)

- Level: Intermediate
- Prerequisites: [Engineering/Security/Auth.md](Auth.md), [Systems/Networks/README.md](../../Systems/Networks/README.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

웹 보안은 신뢰할 수 없는 입력, 브라우저의 출처 모델, 인증 상태, 서버 권한과 공급망을 함께 다뤄 웹 애플리케이션을 보호하는 분야다. 하나의 필터로 해결되지 않으며 입력부터 출력, 데이터베이스, 세션, 배포와 모니터링까지 계층별 방어가 필요하다.

## 직관 (Intuition)

웹 요청의 URL, 헤더, 쿠키, JSON, 파일은 모두 공격자가 만들 수 있다. 애플리케이션은 데이터를 명령이나 코드와 섞지 않고, 인증된 사용자에게도 허용된 자원만 보여 주며, 실패를 감지하고 안전하게 복구해야 한다. 경계마다 "누가 통제하는 값인가"를 묻는 습관이 핵심이다.

## 이론 (Theory)

대표 위험과 우선 방어는 다음처럼 연결된다. OWASP Top 10은 위험 환경에 따라 주기적으로 개정되므로 목록을 체크박스로만 쓰지 않고 위협 모델과 함께 사용한다.

| 위험 | 원인 | 우선 방어 |
|---|---|---|
| 접근 제어 실패 | 서버의 객체·동작 권한 검사 누락 | 기본 거부, 매 요청·객체별 인가 |
| Injection | 데이터와 명령의 경계 붕괴 | 매개변수화 API, 구조화된 명령 |
| XSS | 신뢰하지 않는 값을 실행 문맥에 출력 | 문맥별 자동 이스케이프, CSP |
| CSRF | 브라우저가 인증 정보를 자동 첨부 | CSRF 토큰, SameSite, 출처 검사 |
| 보안 설정 오류 | 기본 계정·과도한 권한·상세 오류 | 안전한 기본값, 구성 검증 |
| 공급망 실패 | 취약·변조된 의존성과 빌드 | 잠금 파일, 출처·서명, 업데이트 정책 |

브라우저의 same-origin policy는 출처가 다른 문서의 읽기를 제한하지만 모든 요청 전송을 막지는 않는다. CORS는 서버가 브라우저에 교차 출처 읽기 권한을 선언하는 방식이지 인증이나 방화벽이 아니다.

### 신뢰 경계

웹 보안의 기본 질문은 "이 값은 누가 통제하는가"다. URL path, query, header, cookie, form body, uploaded file, webhook payload, queue message, cached HTML은 모두 다른 신뢰 경계를 가진다. 내부 서비스에서 온 요청도 앞단 프록시나 큐를 거쳤다면 원본 사용자 권한을 다시 확인해야 한다.

권한 검사는 라우트 진입, 객체 조회, mutation 직전, background job 실행 지점에 반복적으로 필요할 수 있다.

### 출력 문맥

XSS 방어는 입력을 "깨끗하게" 만드는 것보다 출력 문맥을 정확히 아는 일이 중요하다. HTML text, HTML attribute, URL, JavaScript string, CSS는 서로 다른 escaping 규칙을 가진다. Markdown이나 rich text를 허용하면 sanitizer 정책과 CSP를 함께 설계한다.

### 운영 방어

웹 보안은 코드만으로 끝나지 않는다. 보안 헤더, dependency update, secret scanning, rate limit, audit log, anomaly alert, incident runbook이 함께 필요하다. 실패가 발생했을 때 어떤 요청과 계정, 자원, 배포 버전이 관련됐는지 추적할 수 있어야 한다.

## 구현 (Implementation)

프레임워크의 매개변수화 쿼리와 자동 이스케이프를 유지한다.

```python
def find_user(connection, email):
    # 사용자 입력을 SQL 문자열에 이어 붙이지 않는다.
    return connection.execute(
        "SELECT id, display_name FROM users WHERE email = ?",
        (email,),
    ).fetchone()


def transfer(request):
    user = require_session(request)
    require_valid_csrf_token(request)
    amount = validate_positive_amount(request.form["amount"])
    account = load_account(request.form["account_id"])
    require_owner(user, account)
    return perform_transfer(account, amount)
```

HTML, URL, JavaScript, CSS는 서로 다른 출력 문맥이므로 직접 치환 함수 하나로 처리하지 않는다. 템플릿 자동 이스케이프를 유지하고 위험한 HTML이 꼭 필요할 때만 검토된 sanitizer를 사용한다.

## 복잡도 (Complexity)

대부분의 검증과 인코딩은 입력 길이 $L$에 대해 `O(L)`이다. 그러나 보안의 실제 비용은 정책 검사, 의존성 관리, 로깅, 패치와 사고 대응에 분산된다. 모든 입력을 무제한 처리하면 알고리즘 복잡도와 자원 고갈 공격도 가능하므로 크기·시간 제한을 둔다.

## 응용 (Applications)

- 웹·모바일 백엔드와 공개 API
- 관리자 콘솔과 사내 업무 시스템
- 파일 업로드, 결제, 사용자 생성 콘텐츠
- CI/CD, 의존성, 비밀 관리까지 포함한 소프트웨어 공급망

## 흔한 오해 (Common Misunderstandings)

- 입력 검증만으로 XSS가 해결되지는 않는다. 출력되는 문맥에 맞는 인코딩이 필요하다.
- CORS를 넓게 열거나 닫는 것은 서버 측 인가를 대체하지 않는다.
- HTTPS는 SQL injection, XSS, 권한 누락을 막지 않는다.
- WAF는 보조 방어선이며 안전한 쿼리·출력·권한 설계를 대신할 수 없다.

## TMI

- `HttpOnly` 쿠키는 JavaScript의 직접 읽기를 막지만 브라우저가 요청에 쿠키를 붙이는 것은 막지 않으므로 CSRF 방어와 역할이 다르다.
- CSP는 XSS의 피해를 줄이는 추가 계층이지 출력 인코딩을 생략할 면허가 아니다.
- 상세 오류를 사용자에게 숨기더라도 서버 측 상관 ID와 구조화 로그는 남겨야 탐지와 대응이 가능하다.

## 연습 / 확인 문제 (Exercises)

- 게시판의 글 작성·조회·수정 흐름에서 입력과 출력 문맥, 객체 단위 권한 검사를 표시하라.
- SQL 문자열 연결 코드를 매개변수화 쿼리로 바꾸고 같은 입력으로 테스트하라.
- 세션 쿠키, CSRF 토큰, CSP가 각각 막는 위협과 막지 못하는 위협을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [인증과 인가](Auth.md)
- 다음: [네트워크 보안](Network-Security.md)
- 관련: [PKI와 TLS](PKI-and-TLS.md)

## 참조 (References)

- [OWASP Top 10:2025](https://owasp.org/Top10/2025/)
- [OWASP Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
