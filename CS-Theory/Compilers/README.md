# 컴파일러 (Compilers)

> 소스 코드를 기계어로 번역하는 과정.

**선수지식**: [CS-Theory/Programming-Languages/](../Programming-Languages/), [CS-Theory/Computation-Theory/](../Computation-Theory/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 어휘 분석 (Lexer) | Lexer.md | Planned |
| 구문 분석 (Parser) | Parser.md | Planned |
| 추상 구문 트리 (AST) | AST.md | Planned |
| 의미 분석과 타입 검사 | Semantic-Analysis.md | Planned |
| 중간 표현 (IR) | Intermediate-Representation.md | Planned |
| 코드 최적화 | Optimization.md | Planned |
| 코드 생성 | Code-Generation.md | Planned |
| 인터프리터 vs 컴파일러 | Interpreter-vs-Compiler.md | Planned |

---

## 학습 순서

```text
Lexer → Parser → AST
  ↓
Semantic-Analysis → Intermediate-Representation → Optimization → Code-Generation
  ↓
Interpreter-vs-Compiler
```

---

## 연관 섹션

- [CS-Theory/Programming-Languages/](../Programming-Languages/) — 선수지식
- [Engineering/Performance/](../../Engineering/Performance/) — 컴파일러 최적화와 런타임 성능
- [Systems/Computer-Architecture/](../../Systems/Computer-Architecture/) — 코드 생성 대상 아키텍처
