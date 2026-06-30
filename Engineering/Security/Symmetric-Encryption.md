# 대칭 암호화 (Symmetric Encryption)

- Level: Intermediate
- Prerequisites: [Engineering/Security/Hash-Functions.md](Hash-Functions.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

대칭 암호화는 송신자와 수신자가 **같은 비밀키**로 데이터를 암호화하고 복호화하는 방식이다. 현대 애플리케이션은 기밀성만 제공하는 원시 블록 암호보다, 변조 탐지까지 함께 제공하는 AES-GCM이나 ChaCha20-Poly1305 같은 AEAD(Authenticated Encryption with Associated Data)를 사용한다.

## 직관 (Intuition)

둘만 가진 자물쇠 열쇠로 상자를 잠그고 여는 것과 비슷하다. 암호문은 내용을 숨기지만, 공격자가 상자를 바꿔치기하지 않았는지도 확인해야 한다. AEAD는 암호화와 인증 태그를 한 동작으로 묶고, 숨기지 않아도 되지만 변조되면 안 되는 헤더를 AAD로 함께 보호한다.

## 이론 (Theory)

키 $K$, nonce $N$, 평문 $P$, 부가 데이터 $A$에 대해 AEAD는 암호문과 태그를 만든다.

$$
(C,T)=\operatorname{Enc}_K(N,P,A), \qquad P\ \text{or error}=\operatorname{Dec}_K(N,C,A,T)
$$

AES는 128비트 블록과 128·192·256비트 키를 사용하는 표준 블록 암호다. GCM 모드는 AES를 인증 암호로 구성한다. ChaCha20은 스트림 암호이며 Poly1305 인증자와 결합한다.

가장 중요한 운용 규칙은 **같은 키에서 nonce를 재사용하지 않는 것**이다. GCM과 ChaCha20-Poly1305 모두 nonce 재사용 시 기밀성과 무결성이 심각하게 깨질 수 있다. nonce는 비밀일 필요는 없지만 키별로 유일해야 한다. 키 생성·저장·회전과 실패 시 평문을 반환하지 않는 인증 태그 검증도 알고리즘 선택만큼 중요하다.

### Nonce 설계

Nonce는 비밀이 아니라 유일성이 핵심이다. Random nonce를 쓰면 충분한 길이와 충돌 확률을 계산해야 하고, counter nonce를 쓰면 재시작·동시성·샤딩에서 중복이 나지 않게 해야 한다. 분산 시스템에서는 key scope를 좁히거나 prefix를 할당해 충돌 영역을 분리한다.

### Envelope encryption

대용량 데이터는 데이터 키(DEK)로 암호화하고, DEK는 KMS/HSM의 키 암호화 키(KEK)로 감싼다. 이렇게 하면 데이터 전체를 재암호화하지 않고도 KEK 회전과 접근 제어를 운영할 수 있다.

암호문 포맷에는 알고리즘, 키 ID, nonce, AAD 버전, ciphertext, tag를 명확히 담는다.

### 오류 처리

복호화 실패는 인증 실패로 취급하고 평문 일부도 반환하지 않는다. 실패 원인을 상세히 외부에 노출하면 oracle이 될 수 있으므로 로그에는 상관 ID와 내부 진단 정보를 남기되 클라이언트 응답은 단순화한다.

## 구현 (Implementation)

검증된 고수준 AEAD API를 사용한다. 아래 예시는 `cryptography` 패키지의 AES-GCM 인터페이스다.

```python
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)
aead = AESGCM(key)
nonce = os.urandom(12)                 # 같은 키에서 절대 재사용하지 않는다
aad = b"record-type:v1"
ciphertext = aead.encrypt(nonce, b"secret payload", aad)
plaintext = aead.decrypt(nonce, ciphertext, aad)  # 변조 시 예외
```

프로덕션에서는 키를 암호문과 같은 위치에 저장하지 않고 KMS/HSM 또는 운영체제 비밀 저장소를 사용한다. 프레임워크가 제공하는 envelope encryption을 우선한다.

## 복잡도 (Complexity)

평문 길이를 $L$이라 하면 암호화와 복호화 시간은 `O(L)`, 스트리밍 추가 공간은 구현에 따라 작게 유지할 수 있다. 대칭 암호는 공개키 암호보다 대용량 데이터 처리에 훨씬 적합하다.

## 응용 (Applications)

- TLS 연결에서 실제 애플리케이션 데이터 보호
- 디스크·데이터베이스·백업 암호화
- 공개키 방식으로 전달한 세션 키를 이용한 대용량 메시지 암호화
- 인증된 쿠키나 토큰의 기밀 데이터 보호

## 흔한 오해 (Common Misunderstandings)

- 암호화만 하면 변조도 막힌다는 보장은 없다. 인증되지 않은 모드는 별도 MAC과 안전한 조합이 필요하다.
- nonce는 비밀번호나 비밀키가 아니지만 재사용해도 되는 값은 아니다.
- AES-256이라는 이름만으로 시스템이 안전해지지 않는다. 모드, nonce, 키 저장, 오류 처리가 함께 맞아야 한다.
- 직접 암호 모드를 조립하거나 자체 암호 알고리즘을 만드는 것은 학습 실험과 실제 보안 설계를 구분해야 한다.

## TMI

- GCM의 `G`는 유한체 연산을 이용한 GHASH 인증 구조에서 온다.
- CPU의 AES 가속 명령이 없는 환경에서는 ChaCha20-Poly1305가 좋은 성능을 내는 경우가 많다.
- AAD는 암호화되지는 않지만 인증된다. 프로토콜 버전이나 레코드 종류를 안전하게 결합할 때 유용하다.

## 연습 / 확인 문제 (Exercises)

- AEAD에서 ciphertext, nonce, AAD 중 공개 저장해도 되는 것과 반드시 비밀이어야 하는 것을 구분하라.
- 같은 키와 nonce를 재사용하면 왜 위험한지 스트림 암호 관점에서 설명하라.
- 예제의 AAD를 바꾼 뒤 복호화가 실패하는지 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [암호학적 해시 함수](Hash-Functions.md)
- 다음: [비대칭 암호화](Asymmetric-Encryption.md)
- 관련: [PKI와 TLS](PKI-and-TLS.md)

## 참조 (References)

- [NIST FIPS 197: Advanced Encryption Standard](https://csrc.nist.gov/pubs/fips/197/final)
- [NIST SP 800-38D: GCM and GMAC](https://csrc.nist.gov/pubs/sp/800/38/d/final)
- [RFC 8439: ChaCha20 and Poly1305 for IETF Protocols](https://www.rfc-editor.org/rfc/rfc8439.html)
- [Reference/Books.md](../../Reference/Books.md)
