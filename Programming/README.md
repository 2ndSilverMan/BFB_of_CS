# 프로그래밍 기초 (Programming)

> 컴퓨터에게 일을 시키는 법 - 변수, 흐름 제어, 함수, 추상화, 언어별 입문.

**선수지식**: 없음

---

## 읽는 법

- 링크가 걸린 `Draft` 문서는 지금 읽을 수 있는 초안이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| 변수와 타입 | [Variables-and-Types.md](Variables-and-Types.md) | 데이터를 어떻게 표현하고 저장하는가 | Review |
| 조건문과 반복문 | [Control-Flow.md](Control-Flow.md) | 프로그램의 흐름을 제어하는 구조 | Draft |
| 함수와 재귀 | [Functions-and-Recursion.md](Functions-and-Recursion.md) | 코드 재사용과 재귀적 사고 | Draft |
| 배열과 문자열 | [Arrays-and-Strings.md](Arrays-and-Strings.md) | 가장 기본적인 데이터 묶음 | Draft |
| 언어 선택 가이드 | [Language-Selection.md](Language-Selection.md) | Python, JavaScript, C, Java, C++ 중 시작 언어를 고르는 기준 | Review |
| 포인터와 메모리 | [Pointers-and-Memory.md](Pointers-and-Memory.md) | C 계열 언어에서 메모리를 직접 다루는 법 | Draft |
| 객체지향 프로그래밍 | [OOP.md](OOP.md) | 클래스, 상속, 다형성, 캡슐화 | Draft |
| 함수형 프로그래밍 입문 | [Functional-Intro.md](Functional-Intro.md) | 순수 함수, 불변성, 고차 함수 | Draft |

---

## 언어별 트랙

| 트랙 | 내용 |
|---|---|
| [Languages/Python/](Languages/Python/) | 빠른 실습, 자동화, 데이터/AI 입문 |
| [Languages/JavaScript/](Languages/JavaScript/) | 웹 브라우저, Node.js, DOM, 비동기 프로그래밍 |
| [Languages/C/](Languages/C/) | 컴파일, 포인터, 메모리, 시스템 기초 |
| [Languages/Java/](Languages/Java/) | 객체지향, 정적 타입, 컬렉션, 예외 |
| [Languages/Cpp/](Languages/Cpp/) | RAII, STL, 템플릿, 성능 중심 추상화 |

전체 언어 경로는 [Languages/](Languages/)에서 관리한다.

---

## 학습 순서

현재 바로 읽을 수 있는 최소 경로:

```text
변수와 타입 → 조건문/반복문 → 함수와 재귀 → 배열과 문자열
                                                     ↓
                                             언어 선택 가이드
                                                     ↓
                                             Data-Structures/
```

언어별 트랙은 방향을 고르기 위한 목차이며, 아직 대부분 `Planned` 상태다. `포인터와 메모리`, `OOP`, `함수형 입문`은 후속 확장 주제다. 입문자 로드맵을 먼저 따라갈 때는 `배열과 문자열`까지 읽고, 특정 언어를 고르고 싶으면 [언어 선택 가이드](Language-Selection.md)를 거친 뒤 [Data-Structures/](../Data-Structures/)로 넘어가면 된다.

---

## 연관 섹션

- [Math/Discrete/](../Math/Discrete/) — 논리와 집합론은 프로그래밍 사고의 기반
- [Data-Structures/](../Data-Structures/) — 프로그래밍 기초 이후 자연스러운 다음 단계
