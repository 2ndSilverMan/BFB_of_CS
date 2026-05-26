# 보안과 암호학 (Security & Cryptography)

> 실무 보안과 실용 암호학을 함께 다루는 영역.

**선수지식**: [Math/Discrete/](../../Math/Discrete/) (정수론), [Systems/Networks/](../../Systems/Networks/)

암호학의 이론적 기반은 [CS-Theory/Computation-Theory/](../../CS-Theory/Computation-Theory/)와 연결하고, 이 섹션에서는 시스템을 보호하기 위한 적용 관점까지 함께 정리한다.

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 암호학

| 주제 | 파일 | Status |
|---|---|---|
| 대칭 암호화 (AES, ChaCha20) | Symmetric-Encryption.md | Planned |
| 비대칭 암호화 (RSA, ECC) | Asymmetric-Encryption.md | Planned |
| 해시 함수 (SHA, 무결성) | Hash-Functions.md | Planned |
| 디지털 서명 | Digital-Signatures.md | Planned |
| 공개키 인프라 (PKI, TLS) | PKI-and-TLS.md | Planned |
| 영지식 증명 | Zero-Knowledge-Proofs.md | Planned |

### 응용 보안

| 주제 | 파일 | Status |
|---|---|---|
| 인증과 인가 (OAuth, JWT) | Auth.md | Planned |
| 웹 보안 (OWASP Top 10) | Web-Security.md | Planned |
| 네트워크 보안 | Network-Security.md | Planned |

---

## 학습 순서

```text
Hash-Functions → Symmetric-Encryption
        ↓
Asymmetric-Encryption → Digital-Signatures → PKI-and-TLS
        ↓
Auth → Web-Security → Network-Security
        ↓
Zero-Knowledge-Proofs
```

---

## 연관 섹션

- [CS-Theory/Computation-Theory/](../../CS-Theory/Computation-Theory/) — 암호학의 복잡도 기반
- [CS-Theory/Quantum-Computing/](../../CS-Theory/Quantum-Computing/) — 양자 내성 암호
