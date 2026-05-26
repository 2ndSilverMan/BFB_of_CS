# 참조 자료 커버리지 (Reference Coverage)

> 책, 강의, 논문, 용어 사전의 분야별 보강 상태를 관리하는 작성자용 문서.

---

## Coverage

각 셀은 `커버된 하위 분야 수 / 전체 하위 분야 수 (총 항목 수)` 형식이다. `*` 표시는 특정 하위 분야에 항목이 몰려 있다는 뜻이다.
하위 디렉토리가 있는 섹션은 구체적인 하위 섹션 링크만 커버리지로 계산한다. 예를 들어 `[Systems](../Systems/)`는 총 항목 수에는 들어가지만, 특정 하위 분야 커버리지에는 들어가지 않는다.

| 섹션 | 하위 분야 | Books | Courses | Papers |
|---|---|---|---|---|
| Programming | 1 | 1/1 (3) | 1/1 (2) | 1/1 (2) |
| Math | 7 | 4/7 (4) | 3/7 (3) | 1/7 (1) |
| Data-Structures | 1 | 1/1 (1) | 1/1 (1) | 1/1 (3) |
| Algorithms | 1 | 1/1 (2) | 1/1 (2) | 1/1 (4) |
| Systems | 6 | 5/6 (5) | 3/6 (4) | 1/6 (7)* |
| CS-Theory | 4 | 3/4 (3) | 1/4 (1) | 1/4 (3)* |
| AI | 12 | 5/12 (5) | 5/12 (6) | 7/12 (14) |
| Engineering | 7 | 6/7 (9) | 3/7 (4) | 4/7 (6) |

## 보강 우선순위

2026-05-26 기준 우선순위다.

- **AI 심화 분야**: Theoretical-ML, PGMs, Causal-Inference, AI-Safety, MLOps, LLMs, Computer-Vision, Generative-Models 각각 책 0권.
- **Systems Papers**: 7편 전부 Distributed-Systems. Computer-Architecture, Operating-Systems, Databases 논문 필요.
- **CS-Theory Courses**: Programming-Languages, Compilers, Quantum-Computing 강의 0개.
- **Math Papers**: 1편 (Shannon). Calculus, Linear-Algebra, Optimization의 역사적 논문 누락.

## Glossary

알파벳별 정리. 약 90개 용어. AI(Transformer, RAG, RLHF 등), Systems(Mutex, Process, Paging 등), Algorithms(Big-O, DP 등) 위주. 섹션별 균형은 [Glossary.md](../Reference/Glossary.md) 빠른 진입점 표 참고.

## 갱신 규칙

- [Books.md](../Reference/Books.md), [Courses.md](../Reference/Courses.md), [Papers.md](../Reference/Papers.md)를 수정하면 이 문서의 Coverage 표를 함께 갱신한다.
- 항목 수뿐 아니라 하위 분야 쏠림도 같이 확인한다.
- 특정 분야에 항목이 몰려 있으면 `*` 표시를 유지하고 보강 우선순위에 이유를 적는다.
