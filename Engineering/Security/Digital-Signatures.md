# 디지털 서명 (Digital Signatures)

- Level: Intermediate
- Prerequisites: [Engineering/Security/Hash-Functions.md](Hash-Functions.md), [Engineering/Security/Asymmetric-Encryption.md](Asymmetric-Encryption.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

디지털 서명은 개인키로 메시지에 서명하고 대응하는 공개키로 서명을 검증하는 기술이다. 메시지가 바뀌지 않았고 해당 개인키 소유자가 서명했음을 확인하는 데 쓰인다. 암호화처럼 내용을 숨기는 기능은 제공하지 않는다.

## 직관 (Intuition)

봉투를 잠그는 것이 암호화라면, 디지털 서명은 내용에 위조하기 어려운 도장을 찍는 일에 가깝다. 누구나 공개키로 도장을 검사할 수 있지만 유효한 도장은 개인키를 가진 사람만 만들 수 있다. 단, 공개키가 누구의 것인지 확인하는 절차가 별도로 필요하다.

## 이론 (Theory)

서명 체계는 키 생성, 서명, 검증 알고리즘으로 구성된다.

$$
(pk,sk)\leftarrow\operatorname{KeyGen},\quad
\sigma\leftarrow\operatorname{Sign}_{sk}(m),\quad
\operatorname{Verify}_{pk}(m,\sigma)\in\{true,false\}
$$

안전성 목표는 공격자가 선택한 메시지의 서명을 받아 볼 수 있어도 새 메시지에 대한 유효한 서명을 만들기 어렵게 하는 EUF-CMA로 모델링한다. RSA-PSS, ECDSA, EdDSA 등이 대표적이다. 알고리즘마다 해시 선택, 인코딩, 난수 또는 결정적 nonce 규칙이 다르므로 원시 연산을 섞지 않는다.

서명은 개인키 통제와 검증 정책이 온전할 때 출처 인증과 무결성을 제공한다. 법적 의미의 부인 방지는 키 공유, 키 탈취, 인증서 정책과 감사 기록까지 고려해야 하므로 수학적 검증 하나로 자동 보장되지 않는다.

## 구현 (Implementation)

고수준 Ed25519 API로 바이트 메시지에 서명하고 검증한다.

```python
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()
message = b"release-manifest-v1"
signature = private_key.sign(message)

try:
    public_key.verify(signature, message)
    valid = True
except InvalidSignature:
    valid = False
```

실제 배포에서는 서명 대상의 직렬화가 항상 동일해야 하며, 프로토콜 이름·버전·용도를 메시지에 포함해 다른 문맥의 서명이 재사용되지 않게 한다.

## 복잡도 (Complexity)

메시지 해시는 길이 $L$에 대해 `O(L)`이고, 서명과 검증은 알고리즘·키 크기에 따른 고정 규모의 공개키 연산을 추가한다. 대량 검증에서는 키 파싱, 인증서 체인 검증, 실패 처리 비용도 중요하다.

## 응용 (Applications)

- 소프트웨어 릴리스, 패키지, 컨테이너 이미지 서명
- TLS 인증서와 핸드셰이크의 소유권 증명
- 문서·트랜잭션·감사 로그의 무결성 확인
- 인증 토큰의 발급자 검증

## 흔한 오해 (Common Misunderstandings)

- 서명은 메시지를 암호화하지 않는다. 서명된 데이터는 그대로 읽힐 수 있다.
- 공개키를 얻었다고 그 소유자를 아는 것은 아니다. 인증서나 신뢰된 배포 경로가 필요하다.
- 파일의 해시 문자열만 서명할 때는 사용한 해시와 인코딩, 문맥까지 명확해야 한다.
- 검증 실패를 무시하거나 예외 시 성공으로 처리하면 강한 알고리즘도 무용지물이다.

## TMI

- ECDSA에서 nonce가 재사용되거나 편향되면 여러 서명만으로 개인키가 드러날 수 있다.
- Ed25519는 결정적 서명 방식을 사용해 런타임 난수 오류에 대한 의존을 줄이지만 키 생성의 안전한 난수는 여전히 필요하다.
- 코드 서명은 "안전한 코드"가 아니라 "특정 키로 서명된 뒤 바뀌지 않은 코드"임을 말한다.

## 연습 / 확인 문제 (Exercises)

- 서명된 메시지 한 바이트를 바꾸고 검증 결과를 확인하라.
- 암호화와 디지털 서명이 각각 제공하는 보안 속성을 표로 비교하라.
- 소프트웨어 배포 서명에서 키 폐기와 교체 절차가 왜 필요한지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [비대칭 암호화와 키 교환](Asymmetric-Encryption.md)
- 다음: [PKI와 TLS](PKI-and-TLS.md)
- 관련: [암호학적 해시 함수](Hash-Functions.md)

## 참조 (References)

- [NIST FIPS 186-5: Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final)
- [RFC 8032: Edwards-Curve Digital Signature Algorithm](https://www.rfc-editor.org/rfc/rfc8032.html)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Books.md](../../Reference/Books.md)
