# 참조 자료 커버리지 (Reference Coverage)

> 책, 강의, 논문, 용어 사전의 분야별 보강 상태를 관리하는 작성자용 문서.

---

## Coverage

각 셀은 `커버된 하위 분야 수 / 전체 하위 분야 수 (총 항목 수)` 형식이다. `*` 표시는 특정 하위 분야에 항목이 몰려 있다는 뜻이다.
하위 디렉토리가 있는 섹션은 구체적인 하위 섹션 링크만 커버리지로 계산한다. 예를 들어 `[Systems](../Systems/)`는 총 항목 수에는 들어가지만, 특정 하위 분야 커버리지에는 들어가지 않는다.

| 섹션 | 하위 분야 | Books | Courses | Papers |
|---|---|---|---|---|
| Programming | 1 | 1/1 (3) | 1/1 (2) | 1/1 (2) |
| Math | 7 | 7/7 (7) | 7/7 (7) | 3/7 (3) |
| Data-Structures | 1 | 1/1 (1) | 1/1 (1) | 1/1 (3) |
| Algorithms | 1 | 1/1 (2) | 1/1 (2) | 1/1 (4) |
| Systems | 6 | 6/6 (6) | 6/6 (7) | 4/6 (10)* |
| CS-Theory | 4 | 4/4 (4) | 3/4 (3) | 3/4 (5) |
| AI | 12 | 10/12 (10) | 9/12 (10) | 7/12 (14) |
| Engineering | 7 | 7/7 (10) | 3/7 (4) | 4/7 (6) |

## 보강 우선순위

2026-06-08 기준이다. 핵심 공백을 1차로 채웠고 남은 항목은 다음과 같다.

- **AI 책**: Theoretical-ML, Computer-Vision, MLOps, Causal-Inference, AI-Safety를 1차로 채웠다. **Generative-Models와 LLMs는 표준 교재가 아직 부족**해 책 0권으로 남아 있다(강의는 보강함).
- **AI 강의**: MLOps, PGMs, Generative-Models, LLMs를 채웠다. Theoretical-ML, Causal-Inference, AI-Safety 강의는 미보강.
- **Systems Papers**: Computer-Architecture(Amdahl), Operating-Systems(UNIX), Databases(Codd)를 추가해 4/6. 여전히 Distributed-Systems 편중(10편 중 7편)이라 `*` 유지. Networks, Parallel-Computing 논문 미보강.
- **CS-Theory**: Compilers, Programming-Languages 강의·논문을 채웠다. **Quantum-Computing 강의 0개**(책은 Nielsen & Chuang 보강).
- **Math Papers**: Optimization(Robbins-Monro), Numerical-Methods(Hestenes-Stiefel)를 추가해 3/7. Linear-Algebra, Calculus의 역사적 논문은 미보강.

## Glossary

알파벳별 정리. 약 90개 용어. AI(Transformer, RAG, RLHF 등), Systems(Mutex, Process, Paging 등), Algorithms(Big-O, DP 등) 위주. 섹션별 균형은 [Glossary.md](../Reference/Glossary.md) 빠른 진입점 표 참고.

## 갱신 규칙

- [Books.md](../Reference/Books.md), [Courses.md](../Reference/Courses.md), [Papers.md](../Reference/Papers.md)를 수정하면 이 문서의 Coverage 표를 함께 갱신한다.
- 항목 수뿐 아니라 하위 분야 쏠림도 같이 확인한다.
- 특정 분야에 항목이 몰려 있으면 `*` 표시를 유지하고 보강 우선순위에 이유를 적는다.
