# Python 실행 환경과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Python은 인터프리터로 코드를 실행하는 동적 타입 언어다. 스크립트 파일을 실행하거나 REPL에서 한 줄씩 실험할 수 있으며, 들여쓰기가 블록을 나타내는 문법이다.

## 직관 (Intuition)

Python은 "읽기 쉬운 의사코드에 가까운 실행 가능한 문장"을 지향한다. 중괄호 대신 들여쓰기로 구조를 표현하므로, 코드 모양이 곧 코드 의미가 된다.

## 이론 (Theory)

Python은 동적 타입 객체 모델과 interpreter 실행 모델을 가진 언어다. 들여쓰기, namespace, module import, 예외 처리 규칙을 이해하면 작은 script에서 큰 application으로 넘어가기 쉽다.

## 핵심 문법 (Core Syntax)

```python
name = "Ada"
age = 20

if age >= 18:
    print(f"{name} is an adult")
else:
    print(f"{name} is a minor")

for i in range(3):
    print(i)
```

파일은 보통 `python script.py`로 실행한다. 실행 환경은 프로젝트별 가상 환경으로 분리하는 습관이 좋다.

## 구현 (Implementation)

가상 환경을 만들고 작은 script와 REPL을 번갈아 사용해 문법을 확인한다. 실행 파일에는 `if __name__ == "__main__":` guard를 두고, package 설치와 interpreter version을 프로젝트별로 고정한다.

```python
import sys


def main():
    print(f"Python {sys.version_info.major}.{sys.version_info.minor}")
    print("Hello, BFB")


if __name__ == "__main__":   # 실행 진입점
    main()
```

## 복잡도 (Complexity)

Python은 interpreter overhead가 있어 작은 연산을 매우 많이 반복하면 느려질 수 있다. 대신 built-in 자료구조와 C로 구현된 library를 활용하면 같은 알고리즘도 훨씬 작은 상수 비용으로 실행된다.

## 응용 (Applications)

- 자동화 스크립트
- 데이터 처리와 AI/ML 실습
- 웹 서버와 CLI 도구
- 알고리즘 문제 풀이

## 흔한 오해 (Common Misunderstandings)

- 들여쓰기는 스타일이 아니라 문법이다.
- Python이 동적 타입이라고 타입이 없다는 뜻은 아니다.
- `is`는 값 비교가 아니라 객체 동일성 비교다. 값 비교에는 `==`를 쓴다.
- 전역 환경에 패키지를 마구 설치하면 프로젝트 재현성이 나빠진다.

## TMI

- `python -m module`은 모듈을 스크립트처럼 실행한다.
- `__name__ == "__main__"` 패턴은 파일을 직접 실행할 때만 동작할 코드를 구분한다.
- 가상 환경은 `venv` 같은 도구로 만들 수 있다.

## 연습 / 확인 문제 (Exercises)

- 이름과 나이를 입력받아 조건문으로 문장을 출력하라.
- `for`와 `while`로 각각 1부터 5까지 출력하라.
- 같은 코드를 들여쓰기 하나만 바꿔 실행 결과가 어떻게 달라지는지 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [Python 컬렉션](Python-Collections.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
