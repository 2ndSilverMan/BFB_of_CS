# 영지식 증명 (Zero-Knowledge Proofs)

- Level: Advanced
- Prerequisites: [Hash-Functions.md](Hash-Functions.md), [Digital-Signatures.md](Digital-Signatures.md), [Math/Discrete/Number-Theory-Basics.md](../../Math/Discrete/Number-Theory-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

영지식 증명은 어떤 명제가 참이라는 사실을, 그 명제를 증명하는 비밀 정보 자체는 드러내지 않고 증명하는 암호 프로토콜이다. 증명자는 지식을 가지고 있음을 보이고, 검증자는 그 지식의 내용을 배우지 않는다.

## 직관 (Intuition)

비밀번호를 말하지 않고도 “내가 비밀번호를 안다”는 사실만 보여주고 싶다고 하자. 영지식 증명은 이런 요구를 수학적으로 만든다. 검증자는 속았을 가능성이 충분히 낮다고 믿지만, 비밀 자체는 얻지 못한다.

## 이론 (Theory)

영지식 증명에는 세 성질이 중요하다.

- Completeness: 참인 명제라면 정직한 증명자가 검증자를 납득시킬 수 있다.
- Soundness: 거짓 명제라면 부정직한 증명자가 속이기 어렵다.
- Zero-knowledge: 검증자는 명제의 참/거짓 외에 추가 지식을 얻지 못한다.

상호작용형 ZKP는 여러 라운드의 challenge-response로 구성될 수 있고, 비상호작용형 NIZK는 공통 참조 문자열이나 Fiat-Shamir transform 같은 도구로 한 번의 증명으로 만든다. zk-SNARK, zk-STARK는 간결한 증명과 검증을 목표로 하는 현대적 계열이다.

## 구현 (Implementation)

아주 단순화한 challenge-response 구조는 다음 흐름으로 볼 수 있다.

```text
prover commits to hidden witness-derived value
verifier sends random challenge
prover responds using witness
verifier checks response without learning witness
```

실제 프로토콜은 수학적 군, commitment, polynomial, hash, randomness 요구사항이 엄격하므로 직접 구현보다 검증된 라이브러리와 프로토콜을 사용해야 한다.

## 복잡도 (Complexity)

프로토콜마다 proving time, verification time, proof size, trusted setup 필요성이 다르다. SNARK는 검증과 증명이 짧을 수 있지만 trusted setup이 필요한 계열이 있고, STARK는 proof가 더 클 수 있지만 투명성과 post-quantum 성질을 강조한다.

## 응용 (Applications)

- 프라이버시 보존 인증
- 블록체인 확장성과 private transaction
- 신원/자격 증명에서 선택적 공개
- 계산 무결성 증명

## 흔한 오해 (Common Misunderstandings)

- 영지식은 “아무것도 증명하지 않는다”가 아니라 “필요한 사실만 증명한다”는 뜻이다.
- 모든 ZKP가 작고 빠른 것은 아니다.
- trusted setup이 필요한 프로토콜에서는 setup 절차가 보안 가정의 일부다.
- ZKP를 쓴다고 전체 시스템 프라이버시가 자동 보장되지는 않는다. 메타데이터와 구현이 중요하다.

## TMI

- Sudoku 해법을 공개하지 않고 해법을 안다는 것을 증명하는 예시는 교육용으로 자주 쓰인다.
- Fiat-Shamir transform은 random oracle model 아래 상호작용을 줄이는 방법으로 설명된다.
- 영지식 시스템은 암호학, 컴파일러, 분산 시스템이 만나는 복합 기술이다.

## 연습 / 확인 문제 (Exercises)

- completeness, soundness, zero-knowledge를 각각 한 문장으로 설명하라.
- 비밀번호를 공개하지 않는 인증에서 ZKP가 어떤 문제를 줄이는지 설명하라.
- proof size와 proving time의 trade-off가 중요한 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [Digital Signatures](Digital-Signatures.md)
- 다음: [Network Security](Network-Security.md)

## 참조 (References)

- [Hash-Functions.md](Hash-Functions.md)
- [Digital-Signatures.md](Digital-Signatures.md)
- [Math/Discrete/Number-Theory-Basics.md](../../Math/Discrete/Number-Theory-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
