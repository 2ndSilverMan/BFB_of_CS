# Python 클래스와 객체 (Python OOP)

- Level: Beginner
- Prerequisites: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Python 클래스는 데이터와 동작을 묶는 사용자 정의 타입이다. 핵심은 **모든 것이 객체**이고, 속성 접근이 **인스턴스 `__dict__` → 클래스 → MRO** 순으로 해소된다는 객체 모델이다 — 이 한 가지가 `self`·상속·dunder·디스크립터를 전부 설명한다.

## 직관 (Intuition)

딕셔너리로도 데이터를 묶지만, 클래스는 "이 데이터로 무엇을 할 수 있는가"까지 같은 곳에 둔다. Python은 정적 타입 강제 대신 **duck typing**("필요한 메서드만 있으면 된다")을 쓴다. 그래서 "타입이 무엇인가"보다 "어떤 프로토콜을 따르는가"가 설계의 중심이다.

## 핵심 문법 (Core Syntax)

```python
class User:
    def __init__(self, name):       # 생성자(초기화자)
        self.name = name            # 인스턴스 속성 → self.__dict__
    def greet(self):                # 메서드: 첫 인자가 인스턴스
        return f"Hello, {self.name}"

u = User("Ada")
print(u.greet())                    # User.greet(u) 와 동일
```

## 이론 (Theory)

### 1. 속성 해소와 `self`

`u.greet()` 는 `type(u).greet.__get__(u)(...)` 로 변환된다 — 함수가 **디스크립터**라 인스턴스에 바인딩되어 `self` 가 자동 전달된다. 속성 읽기 `u.x` 는 ① 데이터 디스크립터(클래스) ② `u.__dict__` ③ 클래스·MRO ④ `__getattr__` 순으로 찾는다.

### 2. MRO와 C3 선형화

다중 상속의 메서드 순서는 **C3 선형화**로 결정된다(`Class.__mro__`). 다이아몬드 상속에서 `super()` 는 "부모"가 아니라 **MRO상 다음 클래스**를 가리킨다 — 그래서 협력적 다중 상속이 가능하다.

### 3. dataclass와 `__slots__`

값 객체는 `@dataclass` 로 `__init__`·`__repr__`·`__eq__` 를 자동 생성. 인스턴스가 매우 많으면 `__slots__` 로 per-instance `__dict__` 를 없애 메모리를 크게 줄인다(속성 집합 고정).

## 구현 (Implementation)

```python
from dataclasses import dataclass

@dataclass(slots=True)              # __dict__ 없이 고정 슬롯
class Point:
    x: int
    y: int
    def moved(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

class Counter:
    count = 0                        # 클래스 변수(공유!) — 주의
    def __init__(self):
        self.n = 0                   # 인스턴스 변수(개별)
    @classmethod
    def make(cls): return cls()      # cls = 실제 호출 클래스(상속 친화)
    @property
    def doubled(self): return self.n * 2   # 계산된 속성
```

## 복잡도 (Complexity)

| 항목 | 비용 |
|---|---|
| 속성 접근(`__dict__`) | 평균 $O(1)$ 해시 조회 |
| 메서드 호출 | 디스크립터 바인딩 오버헤드 |
| `__slots__` 인스턴스 | `__dict__` 제거로 메모리 ↓(수십 %) |
| MRO 해소 | 클래스 정의 시 1회 계산, 조회는 캐시 |

## 응용 (Applications)

- 도메인 객체·상태/동작 캡슐화, 라이브러리 API 모델링.
- 테스트용 fake/stub([Test-Doubles](../../../Engineering/Testing/Test-Doubles.md)).
- 프로토콜 기반 다형성(duck typing), ABC/`Protocol` 타입 힌트.

## 흔한 오해 (Common Misunderstandings)

- **가변 기본 인자 함정**: `def f(x, acc=[])` 의 `[]` 는 **정의 시 한 번** 생성돼 호출 간 공유된다 → `None` 센티넬을 써라.
- **클래스 변수 vs 인스턴스 변수**: 클래스 변수에 가변 객체를 두면 모든 인스턴스가 공유한다.
- **`self` 는 예약어가 아니다** — 관례일 뿐이나 반드시 따른다.
- **상속 > composition 아니다** — 깊은 상속보다 합성이 단순한 설계인 경우가 많다.
- **`private` 은 강제 아님** — `_name` 은 관례, `__name` 은 name mangling일 뿐.

## TMI

- `__slots__` 는 메모리 절감뿐 아니라 오타로 새 속성을 만드는 버그도 막는다(정의 안 된 속성 대입 시 에러).
- `@dataclass(frozen=True)` 는 불변 값 객체를 만들어 `__hash__` 도 생성 → dict 키로 쓸 수 있다.
- Python의 `super()` 는 인자 없이 호출하면 `__class__` 셀과 첫 인자에서 현재 클래스·인스턴스를 자동 추론한다(컴파일러 마법).

## 연습 / 확인 문제 (Exercises)

- `BankAccount` 에 입금/출금을 만들고, 잔액 음수 방지를 `property` setter로 강제하라.
- 가변 기본 인자 함정을 재현하고 `None` 센티넬로 고쳐라.
- 다이아몬드 상속을 만들어 `__mro__` 와 `super()` 호출 순서를 출력하라.
- 같은 클래스를 `__slots__` 유무로 만들어 인스턴스 메모리를 `sys.getsizeof` 로 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- 다음: [Data-Structures](../../../Data-Structures/)
- 관련: [OOP](../../OOP.md)

## 참조 (References)

- [Programming/OOP.md](../../OOP.md)
- [Engineering/Software-Design/Clean-Code.md](../../../Engineering/Software-Design/Clean-Code.md)
