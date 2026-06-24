# C++ 학습 트랙 (C++)

> 성능 제어, RAII, 표준 라이브러리, 템플릿을 함께 다루는 언어 트랙.

**선수지식**: [Programming/Languages/C/](../C/), [배열과 문자열](../../Arrays-and-Strings.md)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 실행 환경과 기본 문법 | [Cpp-Setup-and-Syntax.md](Cpp-Setup-and-Syntax.md) | 컴파일, namespace, iostream, 값과 참조 | Draft |
| 2 | 참조와 RAII | [Cpp-References-and-RAII.md](Cpp-References-and-RAII.md) | reference, lifetime, destructor, resource ownership | Draft |
| 3 | 클래스와 템플릿 | [Cpp-Classes-and-Templates.md](Cpp-Classes-and-Templates.md) | class, operator, template의 기본 사용 | Draft |
| 4 | STL | [Cpp-STL.md](Cpp-STL.md) | vector, string, map, algorithm 사용 패턴 | Draft |
| 5 | 스마트 포인터와 메모리 | [Cpp-Memory-and-Smart-Pointers.md](Cpp-Memory-and-Smart-Pointers.md) | unique_ptr, shared_ptr, move semantics 기본 | Draft |

---

## 학습 순서

```text
Cpp-Setup-and-Syntax -> Cpp-References-and-RAII
        ↓
Cpp-Classes-and-Templates -> Cpp-STL -> Cpp-Memory-and-Smart-Pointers
```

---

## TMI

- Bjarne Stroustrup은 1979년에 훗날 C++이 되는 언어 작업을 시작했고, 처음 이름은 "C with Classes"였다.
- `C++`라는 이름은 C의 증가 연산자 `++`에서 왔다. Stroustrup의 FAQ에 따르면 Rick Mascitti가 이 이름을 제안했다.
- C++은 "C/C++" 하나의 언어가 아니다. C와 호환성을 강하게 의식하지만, 별도의 표준과 철학을 가진 언어다.
- C++에는 "most vexing parse"라는 유명한 함정이 있다. 객체를 만든 줄 알았는데 컴파일러가 함수 선언으로 해석하는 식의 문제다.
- `std::vector<bool>`은 일반적인 `vector<T>`처럼 bool을 하나씩 저장하지 않고 비트 단위 특수화를 사용한다. 그래서 참조처럼 보이는 값도 진짜 `bool&`가 아닐 수 있다.
- RAII는 보통 "R-A-I-I"로 한 글자씩 읽는다. 이름은 딱딱하지만 C++에서 파일, 락, 메모리를 안전하게 다루는 핵심 습관이다.

---

## 연관 섹션

- [Programming/Languages/C/](../C/) - C 기반 메모리와 컴파일 모델
- [Data-Structures/](../../../Data-Structures/) - STL 사용 뒤에 이어지는 자료구조 원리
- [Engineering/Performance/](../../../Engineering/Performance/) - 성능 중심 C++ 코드로 확장

## 참조

- [Bjarne Stroustrup - C++ FAQ](https://www.stroustrup.com/bs_faq.html)
