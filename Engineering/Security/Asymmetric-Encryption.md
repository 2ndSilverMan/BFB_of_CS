# 비대칭 암호화와 키 교환 (Asymmetric Encryption & Key Exchange)

- Level: Intermediate
- Prerequisites: [Engineering/Security/Symmetric-Encryption.md](Symmetric-Encryption.md), [Math/Discrete/](../../Math/Discrete/)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

비대칭 암호는 서로 다른 공개키와 개인키를 사용한다. 공개키는 배포해도 되지만 개인키는 소유자만 지킨다. 공개키 암호화, 키 합의, 디지털 서명은 모두 비대칭 기술을 쓰지만 목적과 안전한 키 사용법은 서로 다르다.

## 직관 (Intuition)

누구나 편지를 넣을 수 있지만 개인키 소유자만 열 수 있는 우편함을 생각할 수 있다. 다만 공개키 연산은 느리고 메시지 크기에도 제약이 있으므로, 실제 시스템은 비대칭 방식으로 임시 대칭키를 합의하거나 캡슐화하고 본문은 AEAD로 암호화한다. 이를 하이브리드 암호화라 한다.

## 이론 (Theory)

RSA는 큰 정수의 소인수분해 어려움에, 타원곡선 방식은 타원곡선 이산 로그 문제에 기반한다. 현대 프로토콜에서 ECDH/X25519 같은 키 합의는 양쪽이 공개값을 교환해 같은 공유 비밀을 얻도록 한다.

$$
K_A=\operatorname{KDF}(sk_A,pk_B,context), \qquad
K_B=\operatorname{KDF}(sk_B,pk_A,context), \qquad K_A=K_B
$$

공유 비밀은 그대로 암호 키로 쓰기보다 HKDF 같은 KDF로 프로토콜 문맥과 결합한다. RSA 암호화가 필요한 기존 시스템에서는 결정적인 textbook RSA가 아니라 무작위 패딩을 포함한 RSA-OAEP 같은 승인된 구성을 사용한다.

비대칭 암호만으로 상대의 신원을 확인할 수는 없다. 받은 공개키가 정말 상대의 것인지 인증서, 신뢰된 키 교환 경로, 키 고정(pinning) 같은 별도 신뢰 메커니즘이 필요하다. 또한 장기적으로는 양자 컴퓨터 위협에 대비한 후양자 알고리즘 전환과 crypto agility가 중요하다.

## 구현 (Implementation)

직접 정수 연산을 구현하지 않고 검증된 X25519와 HKDF API로 세션 키를 유도한다.

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

alice = X25519PrivateKey.generate()
bob = X25519PrivateKey.generate()
shared = alice.exchange(bob.public_key())

session_key = HKDF(
    algorithm=hashes.SHA256(), length=32, salt=None,
    info=b"example-protocol-v1",
).derive(shared)
```

실제 프로토콜은 공개키 직렬화, 상대 인증, 키 확인, 재전송 방지까지 함께 정의해야 한다. 가능하면 TLS나 검토된 메시징 프로토콜을 사용한다.

## 복잡도 (Complexity)

공개키 연산은 키 크기에 따른 큰 정수·곡선 연산이 필요해 대칭 암호보다 비싸다. 하지만 짧은 세션 키를 설정하는 데만 사용하면 전체 데이터 처리 비용은 대부분 `O(L)`인 대칭 AEAD가 담당한다.

## 응용 (Applications)

- TLS 핸드셰이크의 세션 키 합의
- 수신자 공개키를 이용한 하이브리드 파일·메시지 암호화
- 인증서와 소프트웨어 서명의 공개키 기반
- 여러 시스템 사이의 안전한 키 배포

## 흔한 오해 (Common Misunderstandings)

- 공개키로 암호화할 수 있다는 사실만으로 그 공개키의 주인이 인증되지는 않는다.
- 같은 RSA 키를 아무 구분 없이 암호화와 서명에 재사용하면 안 된다.
- 공개키 암호로 대용량 파일 전체를 직접 암호화하는 방식은 비효율적이고 입력 크기 제약도 있다.
- ECC가 무조건 안전한 것은 아니다. 검증된 곡선, 구현, 키 검증과 난수 생성이 필요하다.

## TMI

- Diffie–Hellman은 두 당사자가 사전에 공유한 비밀 없이 공개 채널에서 공유 비밀을 만드는 방법을 제시했다.
- 순방향 비밀성은 장기 개인키가 나중에 유출돼도 과거의 임시 세션 키가 복구되지 않도록 임시 키 합의를 사용하는 성질이다.
- 공개키 알고리즘 교체를 쉽게 만드는 crypto agility는 후양자 전환에서 특히 중요하다.

## 연습 / 확인 문제 (Exercises)

- 하이브리드 암호화에서 공개키 방식과 대칭 방식이 각각 맡는 역할을 설명하라.
- 인증되지 않은 Diffie–Hellman이 중간자 공격에 취약한 이유를 그려 보라.
- HKDF의 `info`에 프로토콜 문맥을 넣는 이유를 조사하라.

## 이어서 읽기 (Reading Path)

- 이전: [대칭 암호화](Symmetric-Encryption.md)
- 다음: [디지털 서명](Digital-Signatures.md)
- 관련: [PKI와 TLS](PKI-and-TLS.md)

## 참조 (References)

- [RFC 7748: Elliptic Curves for Security](https://www.rfc-editor.org/rfc/rfc7748.html)
- [RFC 8017: PKCS #1 RSA Cryptography Specifications](https://www.rfc-editor.org/rfc/rfc8017.html)
- [NIST Post-Quantum Cryptography Standards](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [Reference/Papers.md](../../Reference/Papers.md)
