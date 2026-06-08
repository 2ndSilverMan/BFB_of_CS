# C 학습 트랙 (C)

> 컴파일, 포인터, 메모리, 배열, 구조체를 통해 컴퓨터 내부 동작을 직접 다루는 언어 트랙.

**선수지식**: [Programming/](../../), [배열과 문자열](../../Arrays-and-Strings.md)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 컴파일과 기본 문법 | C-Setup-and-Compilation.md | 컴파일러, main 함수, 헤더, 기본 입출력 | Planned |
| 2 | 타입과 제어 흐름 | C-Types-and-Control-Flow.md | 정수/실수/문자 타입, 조건문, 반복문 | Planned |
| 3 | 포인터와 메모리 | C-Pointers-and-Memory.md | 주소, 역참조, 스택/힙, 동적 할당 | Planned |
| 4 | 배열, 문자열, 구조체 | C-Arrays-Strings-Structs.md | C 문자열, 구조체, 포인터와 배열 관계 | Planned |
| 5 | 파일과 빌드 | C-Files-and-Builds.md | 파일 입출력, 여러 소스 파일, 간단한 빌드 흐름 | Planned |

---

## 학습 순서

```text
C-Setup-and-Compilation -> C-Types-and-Control-Flow
        ↓
C-Pointers-and-Memory -> C-Arrays-Strings-Structs -> C-Files-and-Builds
```

---

## TMI

- C는 Dennis Ritchie가 Bell Labs에서 Unix를 구현하던 흐름 속에서 발전시킨 언어다. Ritchie의 회고에 따르면 C는 1969-1973년 사이에 형성되었고, 특히 1972년에 창의적인 변화가 집중되었다.
- C라는 이름은 선행 언어 B의 다음 단계라는 맥락을 가진다. B 역시 Bell Labs에서 시스템 프로그래밍을 위해 쓰였다.
- "Hello, world" 예제는 C의 상징처럼 알려졌지만, Dennis Ritchie는 Bell Labs의 B 언어 튜토리얼에도 그 초기 사례가 있었다고 적었다.
- C의 `sizeof(char)`는 표준상 항상 1이다. 하지만 이것이 "문자 하나는 항상 1바이트"라는 뜻은 아니다.
- 매크로는 함수처럼 보여도 전처리 단계에서 치환된다. 괄호를 빠뜨린 매크로는 연산자 우선순위 때문에 기묘한 버그를 만들 수 있다.
- C에서 배열 이름은 많은 상황에서 포인터처럼 변환되지만, 배열과 포인터가 같은 것은 아니다. `sizeof`에 넣어 보면 차이가 드러난다.

---

## 연관 섹션

- [Programming/](../../) - 언어 공통 개념
- [Systems/Computer-Architecture/](../../../Systems/Computer-Architecture/) - 데이터 표현과 CPU 실행 흐름
- [Systems/Operating-Systems/](../../../Systems/Operating-Systems/) - 프로세스와 메모리 관리

## 참조

- [Dennis Ritchie - The Development of the C Language](https://www.bell-labs.com/usr/dmr/www/chist.pdf)
- [Bell Labs - The Programming Language B](https://www.nokia.com/bell-labs/about/dennis-m-ritchie/bintro.html)
