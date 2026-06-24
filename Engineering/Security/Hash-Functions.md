# 암호학적 해시 함수 (Cryptographic Hash Functions)

- Level: Intermediate
- Prerequisites: [Algorithms/Complexity.md](../../Algorithms/Complexity.md), [Programming/Arrays-and-Strings.md](../../Programming/Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

암호학적 해시 함수는 길이가 제각각인 입력을 고정 길이 다이제스트로 바꾸는 결정적 함수다. 같은 입력은 같은 결과를 내지만, 결과에서 입력을 찾거나 같은 결과를 내는 두 입력을 찾기 어렵도록 설계한다. 무결성 확인, 디지털 서명, 메시지 인증의 재료로 쓰인다.

## 직관 (Intuition)

해시는 파일의 짧은 지문과 같다. 입력이 한 비트만 달라져도 결과가 크게 바뀌므로 전송 전후 지문을 비교할 수 있다. 그러나 누구나 새 지문을 계산할 수 있으므로 **해시만으로는 공격자가 파일과 지문을 함께 바꾸는 상황을 막지 못한다**. 비밀키가 필요한 HMAC이나 서명이 그 빈틈을 채운다.

## 이론 (Theory)

$n$비트 암호학적 해시 $H$가 목표로 하는 핵심 성질은 다음과 같다.

| 성질 | 공격자의 목표 | 이상적인 작업량 |
|---|---|---|
| 역상 저항성 | 주어진 $y$에 대해 $H(x)=y$인 $x$ 찾기 | 약 $2^n$ |
| 제2 역상 저항성 | 주어진 $x$와 같은 해시의 다른 입력 찾기 | 약 $2^n$ |
| 충돌 저항성 | $H(x)=H(x')$인 서로 다른 두 입력 찾기 | 생일 공격으로 약 $2^{n/2}$ |

현재 일반적인 무결성 용도에는 SHA-256, SHA-384, SHA-3 계열을 사용한다. MD5와 SHA-1은 충돌 저항성이 깨졌으므로 보안 목적의 새 설계에 쓰지 않는다.

비밀번호는 빠른 일반 해시로 저장하지 않는다. 사용자별 salt와 함께 Argon2id, scrypt, bcrypt, PBKDF2 같은 의도적으로 비싼 비밀번호 해시/KDF를 사용한다. 메시지 인증에는 $\operatorname{HMAC}(K,m)$처럼 비밀키를 포함한 구조를 사용한다.

## 구현 (Implementation)

파이썬 표준 라이브러리로 파일 무결성용 SHA-256과 메시지 인증용 HMAC을 구분한다.

```python
import hashlib
import hmac


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def authenticate(key: bytes, data: bytes) -> bytes:
    return hmac.digest(key, data, "sha256")


message = b"amount=100"
tag = authenticate(b"random-secret-key-from-a-key-store", message)
assert hmac.compare_digest(tag, authenticate(b"random-secret-key-from-a-key-store", message))
```

실제 키는 코드에 넣지 않고 키 관리 시스템이나 안전한 비밀 저장소에서 가져온다. 인증 태그 비교에는 타이밍 누출을 줄이는 전용 비교 함수를 쓴다.

## 복잡도 (Complexity)

입력 길이를 $L$이라 하면 해시 계산 시간은 `O(L)`, 스트리밍 구현의 추가 공간은 `O(1)`에 가깝다. 보안 강도는 실행 복잡도와 별개로 출력 길이와 알려진 공격에 좌우된다. 비밀번호 KDF는 공격 비용을 높이기 위해 의도적으로 시간과 메모리를 더 사용한다.

## 응용 (Applications)

- 다운로드 파일과 저장 데이터의 무결성 확인
- HMAC 기반 API 메시지 인증
- 디지털 서명 전 메시지 요약
- Git 같은 콘텐츠 주소화와 중복 탐지
- salt를 포함한 비밀번호 검증 자료 생성

## 흔한 오해 (Common Misunderstandings)

- 해시는 암호화가 아니므로 복호화 키가 없다.
- 단순 해시는 인증 수단이 아니다. 공격자가 데이터와 해시를 함께 바꿀 수 있다.
- salt는 비밀일 필요가 없으며 사용자마다 달라야 한다. 서버 공통 비밀인 pepper와 역할이 다르다.
- SHA-256이 안전하다는 말이 `SHA256(password)`가 안전하다는 뜻은 아니다.

## TMI

- 충돌 공격이 $2^n$보다 $2^{n/2}$에 가까운 이유는 생일 역설과 같다.
- Git의 객체 ID는 콘텐츠 주소 역할을 하지만, 저장소 신뢰성을 위해 서명과 접근 제어가 별도로 필요하다.
- 해시의 avalanche effect는 작은 입력 변화가 출력 비트 전반에 퍼지는 현상이다.

## 연습 / 확인 문제 (Exercises)

- 같은 비밀번호에 서로 다른 salt를 적용했을 때 결과가 달라지는 이유를 설명하라.
- 파일 해시 비교와 HMAC 검증이 각각 어떤 공격자를 가정하는지 비교하라.
- 큰 파일을 한 번에 메모리에 올리지 않고 SHA-256을 계산하라.

## 이어서 읽기 (Reading Path)

- 이전: [복잡도 분석](../../Algorithms/Complexity.md)
- 다음: [대칭 암호화](Symmetric-Encryption.md)
- 관련: [디지털 서명](Digital-Signatures.md)

## 참조 (References)

- [NIST FIPS 180-4: Secure Hash Standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)
- [NIST FIPS 202: SHA-3 Standard](https://csrc.nist.gov/pubs/fips/202/final)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Reference/Books.md](../../Reference/Books.md)
