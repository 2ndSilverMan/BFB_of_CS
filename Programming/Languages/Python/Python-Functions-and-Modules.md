# Python 함수와 모듈 (Functions and Modules)

- Level: Beginner
- Prerequisites: [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md), [Python 컬렉션](Python-Collections.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

함수는 재사용 가능한 코드 단위, 모듈은 파일 단위 코드 묶음이다. 핵심 메커니즘은 **LEGB 이름 탐색**과 **함수가 일급 객체**라는 점, 그리고 **모듈이 `sys.modules` 에 캐시되는 싱글턴**이라는 점이다.

## 직관 (Intuition)

함수는 이름 붙은 조리법, 모듈은 조리법 공책. 같은 일을 복붙하지 않고 이름으로 호출한다. Python에서 함수는 **값**이라 변수에 담고 인자로 넘기고 반환할 수 있어, 데코레이터·콜백·고차 함수가 자연스럽다.

## 핵심 문법 (Core Syntax)

```python
def greet(name, excited=False):
    return f"Hello, {name}{'!' if excited else '.'}"

print(greet("Ada"))
print(greet("Linus", excited=True))

import math
from math import sqrt as root            # 별칭
print(math.pi, root(9))
```

## 이론 (Theory)

### 1. LEGB 이름 탐색

이름은 **Local → Enclosing → Global → Builtins** 순으로 찾는다. 함수 안에서 전역을 *바꾸려면* `global`, 둘러싼 함수 변수를 바꾸려면 `nonlocal` 이 필요하다(읽기는 자동).

### 2. 클로저와 late binding 함정

중첩 함수는 둘러싼 변수를 **참조로 캡처**한다(값 복사 아님). 그래서 루프에서 만든 클로저들은 **루프가 끝난 뒤의 최종 값**을 공유한다 — 기본 인자(`x=i`)로 그 시점 값을 고정해야 한다.

### 3. 가변 기본 인자

기본값은 **함수 정의 시 한 번** 평가된다. `def f(acc=[])` 의 `[]` 는 호출 간 공유돼 누적된다 → `None` 센티넬 패턴.

### 4. 모듈 = 캐시된 싱글턴

`import m` 은 처음 한 번 `m.py` 를 실행해 모듈 객체를 만들고 `sys.modules` 에 캐시한다. 이후 import는 캐시를 돌려준다 — 그래서 **top-level 부작용(side effect)** 은 import 시점에 한 번 일어난다.

## 구현 (Implementation)

```python
# late binding 함정과 해결
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])              # [2, 2, 2]  ← 모두 최종 i 공유
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])              # [0, 1, 2]  ← 기본 인자로 고정

def append_to(x, acc=None):              # 가변 기본 인자 회피
    acc = [] if acc is None else acc
    acc.append(x); return acc
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 함수 호출 | 프레임 생성 등 작지 않은 상수 — hot path 과분할 주의 |
| 모듈 import | 첫 회만 실행·캐시, 이후 $O(1)$ 조회 |
| `*args`/`**kwargs` | 튜플·딕트 생성 비용 |

## 응용 (Applications)

- 반복 제거·테스트 가능한 단위, 고차 함수·데코레이터.
- 표준 라이브러리·외부 패키지 사용, 패키지로 프로젝트 구조화.

## 흔한 오해 (Common Misunderstandings)

- **`return` 없으면 `None` 반환**.
- **가변 기본 인자는 호출 간 상태를 공유** — `None` 센티넬.
- **루프 클로저는 late binding** — 변수를 참조로 캡처.
- **`from m import *` 는 이름 충돌** — 피한다.
- **모듈 import는 파일 실행** — top-level 부작용 주의.

## TMI

- 함수도 객체라 `f.__name__`, `f.__doc__`, 속성 부여가 가능하다(데코레이터가 이를 활용).
- `*args`/`**kwargs` 로 임의 인자를 받고 전달(forwarding)한다.
- 순환 import는 `sys.modules` 에 부분 완성 모듈이 들어가 `AttributeError` 를 낸다 — 구조로 푼다.

## 연습 / 확인 문제 (Exercises)

- 루프에서 클로저 리스트를 만들어 late binding을 재현하고 고쳐라.
- 가변 기본 인자 버그를 재현하고 센티넬로 고쳐라.
- `nonlocal` 로 카운터 클로저를 만들어라.
- 직접 만든 모듈을 import하고 top-level `print` 가 언제 실행되는지 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 컬렉션](Python-Collections.md)
- 다음: [Python 파일과 예외](Python-Files-and-Errors.md)
- 관련: [Python OOP](Python-OOP.md), [함수와 재귀](../../Functions-and-Recursion.md)

## 참조 (References)

- [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md)
- [Reference/Books.md](../../../Reference/Books.md)
