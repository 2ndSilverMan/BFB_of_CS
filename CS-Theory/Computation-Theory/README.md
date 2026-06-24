# 계산 이론 (Theory of Computation)

> 컴퓨터가 할 수 있는 것과 할 수 없는 것의 경계.

**선수지식**: [Math/Discrete/](../../Math/Discrete/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 정규 언어와 유한 오토마타 (DFA/NFA) | [Regular-Languages.md](Regular-Languages.md) | Draft |
| 정규 표현식 | [Regular-Expressions.md](Regular-Expressions.md) | Draft |
| 문맥 자유 문법 (CFG)과 푸시다운 오토마타 | [Context-Free.md](Context-Free.md) | Draft |
| 튜링 머신 | [Turing-Machine.md](Turing-Machine.md) | Draft |
| 결정 불가능성 (정지 문제) | [Undecidability.md](Undecidability.md) | Draft |
| 복잡도 클래스 (P, NP, PSPACE) | [Complexity-Classes.md](Complexity-Classes.md) | Draft |
| NP-완전성과 환원 | [NP-Completeness.md](NP-Completeness.md) | Draft |

---

## 학습 순서

```text
Regular-Languages → Regular-Expressions → Context-Free
        ↓
Turing-Machine → Undecidability
        ↓
Complexity-Classes → NP-Completeness
```

---

## 연관 섹션

- [Math/Discrete/](../../Math/Discrete/) — 형식 언어와 논리의 수학적 기반
- [Algorithms/](../../Algorithms/) — P vs NP, 복잡도 클래스의 실용적 의미
- [CS-Theory/Programming-Languages/](../Programming-Languages/) — 튜링 완전성과 언어 설계
