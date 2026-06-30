# 클린 코드 (Clean Code)

- Level: Intermediate
- Prerequisites: [Engineering/Software-Design/SOLID.md](SOLID.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

클린 코드는 **독자가 의도와 불변식을 빠르게 이해하고 안전하게 바꿀 수 있는** 코드다. 명명, 작은 응집 단위, 명시적 오류 처리, 일관성, 자동 포매터·테스트가 수단이다. "짧음"이 아니라 **놀라움(surprise)이 적음**이 목표.

## 직관 (Intuition)

코드는 쓰는 시간보다 **읽히는 시간이 훨씬 길다**(보통 10:1). 그래서 도메인 언어와 제어 흐름이 분명하고, 단위가 드러나며, 숨은 부작용이 없는 코드가 비싼 가치를 갖는다.

## 이론 (Theory)

- **이름**: 역할·단위·범위를 드러낸다(`calc(x,r)` → `calculate_invoice_total(line_items, tax_rate)`).
- **함수**: 하나의 추상화 수준에서 응집된 일을. 숨은 부작용·불리언 플래그 매개변수를 줄인다.
- **주석**: "무엇"을 반복하지 말고 **"왜"와 제약**을 남긴다.
- **오류**: 삼키지 말고(`except: pass` 금지) 맥락·복구 책임을 명확히.
- **가드 절(guard clause)**: 깊은 중첩 대신 조기 반환으로 평탄화.

## 구현 (Implementation)

```python
# Before: 의미·단위 불명, 깊은 중첩
def proc(d, r):
    if d:
        if r > 0:
            s = 0
            for i in d: s += i[0] * i[1]
            return s + s * r

# After: 도메인 의미 + 가드 절 + 단위
def calculate_invoice_total(line_items, tax_rate):
    if not line_items:                                  # 가드 절
        return 0
    subtotal = sum(it.unit_price * it.quantity for it in line_items)
    return subtotal + subtotal * tax_rate               # tax 포함
```

**워크드 비교.** `proc(d, r)` 는 `d`·`r` 이 무엇인지, 반환이 무엇인지 읽어야 안다(`r<=0`이면 `None` 반환하는 숨은 함정도). `calculate_invoice_total` 은 이름만으로 입력·출력·단위가 드러나고 빈 입력을 명시 처리한다.

## 복잡도 (Complexity)

성능 Big-O와 별개로 **인지 복잡도(cognitive complexity)** 를 낮춘다. 단, **과도한 함수 분해·indirection은 탐색 비용을 오히려 늘린다**(점프가 많아짐).

## 응용 (Applications)

- 코드 리뷰·온보딩, 결함 예방·리팩토링.
- 공개 API·라이브러리, 오래 사는 비즈니스 코드.

## 흔한 오해 (Common Misunderstandings)

- **짧은 함수가 항상 읽기 좋지 않다** — 과분해는 흐름을 흩는다.
- **주석을 다 없애는 게 목표가 아니다** — "왜"는 남긴다.
- **clever one-liner가 명확한 loop보다 우월하지 않다**.
- **스타일 통일만으로 아키텍처 문제를 못 푼다**.

## TMI

- 포매터(black·prettier)는 미학 논쟁을 자동화해 리뷰를 *행위*에 집중시킨다.
- 단위가 포함된 이름(`timeout_ms`, `price_usd`)은 money·time 버그를 줄인다(화성 기후 궤도선은 단위 혼동으로 추락).
- "삭제 가능한 코드가 가장 유지보수하기 쉽다"는 관점 — 가장 좋은 코드는 안 쓴 코드.

## 연습 / 확인 문제 (Exercises)

- 위 `proc` 를 의미 있는 이름 + 가드 절로 리팩토링하라(숨은 `None` 반환도 처리).
- 유용한 "왜" 주석과 불필요한 "무엇" 주석을 구분하라.
- 과분해된 함수들을 응집된 하나로 다시 합쳐 보라.
- 불리언 플래그 매개변수를 두 함수로 분리하라.

## 이어서 읽기 (Reading Path)

- 이전: [SOLID](SOLID.md)
- 다음: [리팩토링](Refactoring.md)
- 관련: [생성 패턴](Creational-Patterns.md)

## 참조 (References)

- [Engineering/Software-Design/SOLID.md](SOLID.md)
- [Reference/Books.md](../../Reference/Books.md)
