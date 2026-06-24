# 인증과 인가 (Authentication and Authorization)

- Level: Intermediate
- Prerequisites: [Engineering/Security/PKI-and-TLS.md](PKI-and-TLS.md), [Engineering/Security/Hash-Functions.md](Hash-Functions.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인증(authentication)은 사용자가 누구인지 확인하고, 인가(authorization)는 그 사용자가 어떤 자원에 어떤 동작을 할 수 있는지 결정한다. 세션 쿠키, OAuth 2.0, OpenID Connect(OIDC), JWT는 이 문제의 서로 다른 일부를 해결하는 도구다.

## 직관 (Intuition)

건물 입구에서 신분증을 확인하는 것이 인증이고, 확인된 사람의 출입증이 어느 방을 열 수 있는지 결정하는 것이 인가다. 한 번 로그인했다고 모든 데이터에 접근할 수 있어서는 안 되며, 서버는 요청마다 대상 자원에 대한 권한을 검사해야 한다.

## 이론 (Theory)

OAuth 2.0은 사용자의 비밀번호를 클라이언트에 주지 않고 제한된 권한을 위임하는 **인가 프레임워크**다. 로그인 신원 정보가 필요하면 OAuth 위에 OIDC를 사용한다. 브라우저·모바일 공개 클라이언트에는 Authorization Code와 PKCE를 사용하고, redirect URI를 정확히 비교하며 `state`와 OIDC `nonce`로 요청을 결합한다.

| 구성 요소 | 역할 |
|---|---|
| 세션 ID | 서버 측 로그인 상태를 가리키는 불투명 식별자 |
| 액세스 토큰 | 특정 자원·범위·기간에 대한 접근 권한 |
| 리프레시 토큰 | 새 액세스 토큰을 얻는 장기 자격 증명 |
| ID 토큰 | OIDC에서 인증 결과와 사용자 클레임 전달 |
| JWT | 서명 가능 클레임 표현 형식이며 그 자체가 인증 방식은 아님 |

토큰 검증은 서명만 보는 작업이 아니다. 허용 알고리즘을 고정하고 발급자 `iss`, 대상 `aud`, 만료 `exp`, 사용 시점과 토큰 용도를 검증한다. 인가는 최소 권한, 기본 거부, 객체 단위 검사 원칙을 따른다.

## 구현 (Implementation)

서버 세션 쿠키의 안전한 속성과 객체 단위 인가를 나타낸 프레임워크 독립 예시다.

```python
def handle_update(request, document_id):
    user = require_authenticated_session(request)
    document = repository.get(document_id)
    if document is None or not policy.can_edit(user, document):
        return forbidden()  # 클라이언트가 보낸 owner_id를 신뢰하지 않는다
    repository.update(document, validated_input(request))
    return no_content()


SESSION_COOKIE = {
    "secure": True,
    "httponly": True,
    "samesite": "Lax",
}
```

세션 ID와 토큰은 로그·URL에 넣지 않고, 로그인·권한 상승 때 세션을 회전하며 로그아웃과 사고 대응을 위한 폐기 전략을 둔다.

## 복잡도 (Complexity)

토큰의 암호학적 검증은 크기가 작아 보통 일정한 공개키 연산 비용으로 볼 수 있다. 실제 병목은 사용자·정책·자원 조회다. 역할 기반 검사는 단순하지만 세밀한 객체·속성 기반 정책은 캐시 무효화와 일관성 비용이 커질 수 있다.

## 응용 (Applications)

- 웹 로그인과 세션 관리
- 외부 애플리케이션에 제한된 API 권한 위임
- 조직의 SSO와 연합 신원
- RBAC·ABAC·관계 기반 접근 제어
- 서비스 계정과 워크로드 신원

## 흔한 오해 (Common Misunderstandings)

- OAuth는 로그인 프로토콜이 아니다. 인증에는 OIDC 같은 명시적 계층이 필요하다.
- JWT는 기본적으로 암호화되지 않는다. payload는 쉽게 디코딩할 수 있으므로 비밀을 넣지 않는다.
- 프런트엔드에서 버튼을 숨기는 것은 인가가 아니다. 서버가 매 요청을 검사해야 한다.
- 긴 만료 시간의 bearer token은 소유한 누구나 사용할 수 있으므로 비밀번호처럼 보호한다.

## TMI

- PKCE는 authorization code를 가로챈 공격자가 토큰으로 교환하지 못하게 일회성 verifier와 challenge를 결합한다.
- 사용자 역할이 `admin`인지 확인하는 것만으로는 다른 사용자의 개별 객체 접근을 막지 못한다. BOLA/IDOR가 이 틈에서 생긴다.
- 패스키는 공개키 자격 증명으로 피싱 저항성과 비밀번호 없는 인증을 제공하는 방향으로 널리 쓰이고 있다.

## 연습 / 확인 문제 (Exercises)

- 온라인 강의 서비스에서 학생·강사·관리자의 인증과 인가 결정을 구분하라.
- JWT 검증에서 서명 외에 검사해야 할 클레임을 정리하라.
- 다른 사용자의 `document_id`를 넣었을 때도 안전한 객체 단위 인가 테스트를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [PKI와 TLS](PKI-and-TLS.md)
- 다음: [웹 보안](Web-Security.md)
- 관련: [네트워크 보안](Network-Security.md)

## 참조 (References)

- [RFC 9700: Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700.html)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)
- [RFC 7519: JSON Web Token](https://www.rfc-editor.org/rfc/rfc7519.html)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
