# 컴파일러 (Compilers)

> 선수 지식 → 난이도 순 정렬.

## 1. 이론적 기반 (선수 지식: 계산이론, 타입 이론)

| # | 주제 | 파일 |
|---|------|------|
| 1 | 형식 문법 (Formal Grammars) | [Formal-Grammars.md](Formal-Grammars.md) |
| 2 | 람다 계산법 (Lambda Calculus) | [Lambda-Calculus.md](Lambda-Calculus.md) |
| 3 | 타입 이론 (Type Theory) | [Type-Theory.md](Type-Theory.md) |

## 2. 프론트엔드 (선수 지식: 형식 문법, 오토마타)

| # | 주제 | 파일 |
|---|------|------|
| 4 | 어휘 분석 & 렉서 (Lexical Analysis) | [Lexical-Analysis.md](Lexical-Analysis.md) |
| 5 | 구문 분석 — 하향식 (Top-Down Parsing) | [Top-Down-Parsing.md](Top-Down-Parsing.md) |
| 6 | 구문 분석 — 상향식 (Bottom-Up Parsing) | [Bottom-Up-Parsing.md](Bottom-Up-Parsing.md) |
| 7 | LL & LR 파서 | [LL-LR-Parser.md](LL-LR-Parser.md) |
| 8 | 심볼 테이블 (Symbol Table) | [Symbol-Table.md](Symbol-Table.md) |
| 9 | 의미 분석 (Semantic Analysis) | [Semantic-Analysis.md](Semantic-Analysis.md) |
| 10 | 타입 검사 (Type Checking) | [Type-Checking.md](Type-Checking.md) |

## 3. 중간 표현 & 분석 (선수 지식: 프론트엔드, 그래프)

| # | 주제 | 파일 |
|---|------|------|
| 11 | 중간 코드 표현 (IR: SSA, 3-주소 코드) | [IR.md](IR.md) |
| 12 | 기본 블록 & 제어 흐름 그래프 (CFG) | [CFG.md](CFG.md) |
| 13 | 데이터 흐름 분석 (Data Flow Analysis) | [Data-Flow-Analysis.md](Data-Flow-Analysis.md) |

## 4. 백엔드 (선수 지식: IR, 데이터 흐름 분석)

| # | 주제 | 파일 |
|---|------|------|
| 14 | 명령어 선택 & 스케줄링 (Instruction Selection) | [Instruction-Selection.md](Instruction-Selection.md) |
| 15 | 레지스터 할당 (Register Allocation) | [Register-Allocation.md](Register-Allocation.md) |
| 16 | 코드 생성 (Code Generation) | [Code-Generation.md](Code-Generation.md) |

## 5. 최적화 (선수 지식: IR, CFG, 데이터 흐름)

| # | 주제 | 파일 |
|---|------|------|
| 17 | 상수 전파 & 폴딩 (Constant Propagation) | [Constant-Propagation.md](Constant-Propagation.md) |
| 18 | 죽은 코드 제거 (Dead Code Elimination) | [Dead-Code-Elimination.md](Dead-Code-Elimination.md) |
| 19 | 루프 최적화 (Loop Optimization) | [Loop-Optimization.md](Loop-Optimization.md) |
| 20 | 인라인 확장 (Inlining) | [Inlining.md](Inlining.md) |
| 21 | 벡터화 (Vectorization / SIMD) | [Vectorization.md](Vectorization.md) |
| 22 | 링크 타임 최적화 (LTO) | [LTO.md](LTO.md) |

## 6. 고급 주제 (선수 지식: 컴파일러 전반, 타입 이론)

| # | 주제 | 파일 |
|---|------|------|
| 23 | JIT 컴파일 (Just-In-Time Compilation) | [JIT.md](JIT.md) |
| 24 | AOT vs JIT | [AOT-vs-JIT.md](AOT-vs-JIT.md) |
| 25 | 가비지 컬렉션 알고리즘 (GC Algorithms) | [GC-Algorithms.md](GC-Algorithms.md) |
| 26 | 정적 분석 & 추상 해석 (Abstract Interpretation) | [Abstract-Interpretation.md](Abstract-Interpretation.md) |
| 27 | 프로그램 검증 (Program Verification, Hoare Logic) | [Program-Verification.md](Program-Verification.md) |
| 28 | 의존 타입 (Dependent Types) | [Dependent-Types.md](Dependent-Types.md) |
| 29 | 효과 시스템 (Effect Systems) | [Effect-Systems.md](Effect-Systems.md) |
