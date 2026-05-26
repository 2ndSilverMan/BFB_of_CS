# CS 핵심 로드맵 (CS Core Roadmap)

> 컴퓨터공학 전공 핵심을 체계적으로 공부하려는 사람을 위한 순서.

---

## 대상

- 컴퓨터공학 전공 핵심을 선수지식 순서대로 정리하려는 학습자

## 현재 가용성

현재 이 로드맵은 전공 전체 순서와 완료 기준을 제공한다. 시스템, 계산 이론, 보안 본문은 대부분 `Planned` 상태이므로, 지금은 전체 범위를 파악하고 각 섹션 README에서 `Draft` 이상 문서가 열린 항목부터 읽는다.

## 시작 전 확인

- [입문자 로드맵](Beginner.md)의 프로그래밍, 자료구조, 알고리즘 기초를 대략 설명할 수 있다.
- 수학은 이산수학부터 시작해도 된다. 미적분, 선형대수, 확률과 통계는 AI 경로를 병행할 때 더 깊게 보강한다.
- 시스템 파트가 처음이라면 컴퓨터 구조를 건너뛰지 않는다.

## 순서

### 기초

1. [프로그래밍 기초](../Programming/)
2. [이산수학](../Math/Discrete/)
3. [미적분](../Math/Calculus/)
4. [선형대수](../Math/Linear-Algebra/)
5. [확률과 통계](../Math/Probability-Statistics/)

### 자료구조 & 알고리즘

6. [자료구조](../Data-Structures/)
7. [알고리즘](../Algorithms/)

### 시스템

8. [컴퓨터 구조](../Systems/Computer-Architecture/)
9. [운영체제](../Systems/Operating-Systems/)
10. [컴퓨터 네트워크](../Systems/Networks/)
11. [데이터베이스](../Systems/Databases/)
12. [분산 시스템](../Systems/Distributed-Systems/)

### 이론

13. [계산 이론](../CS-Theory/Computation-Theory/)
14. [프로그래밍 언어론](../CS-Theory/Programming-Languages/)
15. [컴파일러](../CS-Theory/Compilers/)

### 보안

16. [보안과 암호학](../Engineering/Security/) — CS 전공 핵심으로는 이 섹션 안의 **암호학(대칭/비대칭, 해시, 디지털 서명)**과 **인증/인가, 웹 보안 기본 위협 모델**까지를 본다. 실무 운영(TLS 설정, OWASP 대응 도구 등)은 [시스템 엔지니어 로드맵](Systems-Engineer.md)에서 다룬다.
    - 암호학의 계산 이론적 기반은 [CS-Theory/Computation-Theory/](../CS-Theory/Computation-Theory/)의 복잡도 클래스와 환원 개념과 함께 본다.

---

## 완료 기준

- 자료구조와 알고리즘 선택을 복잡도와 데이터 특성으로 설명할 수 있다.
- 운영체제, 네트워크, 데이터베이스, 분산 시스템의 핵심 추상화를 연결해서 설명할 수 있다.
- 오토마타, 튜링 머신, P/NP, NP-완전성의 의미를 예시와 함께 설명할 수 있다.
- 간단한 언어의 파서/인터프리터 또는 컴파일러 파이프라인을 설계할 수 있다.
- 대칭/비대칭 암호, 해시, 디지털 서명의 수학적 근거와 위협 모델을 구분할 수 있다.
- 인증, 인가, TLS, 웹 보안의 기본 위협 모델을 OWASP Top 10 수준에서 설명할 수 있다.

---

## 다음 단계

- [시스템 엔지니어 로드맵](Systems-Engineer.md)
- [AI 핵심 로드맵](AI-Core.md)

## 관련 로드맵

- [입문자 로드맵](Beginner.md) — 선수지식 경로
