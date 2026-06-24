# Python 함수와 모듈 (Functions and Modules)

- Level: Beginner
- Prerequisites: [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md), [Python 컬렉션](Python-Collections.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

함수는 재사용 가능한 코드 조각이고, 모듈은 Python 파일 단위로 코드를 묶는 방법이다. 함수를 작게 나누고 모듈로 정리하면 프로그램을 읽고 테스트하기 쉬워진다.

## 직관 (Intuition)

함수는 이름 붙은 조리법이고, 모듈은 관련 조리법을 모아 둔 공책이다. 같은 일을 여러 번 복붙하지 않고 이름으로 호출한다.

## 핵심 문법 (Core Syntax)

```python
def greet(name, excited=False):
    suffix = "!" if excited else "."
    return f"Hello, {name}{suffix}"


print(greet("Ada"))
print(greet("Linus", excited=True))
```

다른 파일의 함수는 `import`로 가져온다.

```python
import math

print(math.sqrt(9))
```

## 이론 (Theory)

Python 이름 탐색은 지역(local), 둘러싼 함수(enclosing), 전역(global), 내장(builtins) 순서로 일어난다. 기본 인자는 함수 정의 시점에 한 번 만들어지므로 mutable default는 피한다.

## 구현 (Implementation)

함수는 하나의 책임과 명확한 인자·반환값을 갖게 작성하고, module은 import side effect가 없도록 구성한다. 실행용 코드는 `main()`과 module guard 아래에 두어 import와 실행을 분리한다.

## 복잡도 (Complexity)

함수 호출은 Python에서 작지 않은 상수 비용이 있으므로 아주 작은 연산을 과도하게 쪼개면 hot path에서 부담이 될 수 있다. Module import는 한 번 cache되지만 초기 import 시점의 I/O와 top-level 실행 비용은 남는다.

## 응용 (Applications)

- 반복 코드 제거
- 테스트 가능한 단위 구성
- 표준 라이브러리와 외부 패키지 사용
- 프로젝트 구조화

## 흔한 오해 (Common Misunderstandings)

- `return`이 없으면 함수는 `None`을 반환한다.
- Mutable default argument는 호출 사이에 상태를 공유할 수 있다.
- `from module import *`는 이름 충돌을 만들기 쉬워 피하는 편이 좋다.
- 모듈 import는 파일 실행이기도 하므로 top-level side effect를 조심한다.

## TMI

- 함수도 객체라 변수에 담거나 인자로 넘길 수 있다.
- `*args`, `**kwargs`는 가변 인자를 받을 때 쓴다.
- 패키지는 여러 모듈을 디렉터리로 묶은 구조다.

## 연습 / 확인 문제 (Exercises)

- 리스트 평균을 계산하는 함수를 작성하라.
- Mutable default argument 문제를 재현하고 고쳐라.
- 직접 만든 모듈을 다른 파일에서 import해 보라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 컬렉션](Python-Collections.md)
- 다음: [Python 파일과 예외](Python-Files-and-Errors.md), [Python OOP](Python-OOP.md)

## 참조 (References)

- [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md)
- [Reference/Books.md](../../../Reference/Books.md)
