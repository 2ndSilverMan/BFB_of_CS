# 리팩토링 (Refactoring)

- Level: Intermediate
- Prerequisites: [Engineering/Software-Design/Clean-Code.md](Clean-Code.md), [Engineering/Testing/Unit-Test-Principles.md](../Testing/Unit-Test-Principles.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

리팩토링은 observable behavior를 유지하면서 내부 구조를 작은 단계로 개선하는 작업이다. 기능 추가·bug fix와 구분해 안전망과 되돌릴 수 있는 commit으로 진행한다.

## 직관 (Intuition)

운행 중인 도로를 한 번에 갈아엎지 않고 우회로와 검사를 두며 작은 구간씩 정비한다. 매 단계가 동작하므로 문제 지점을 좁힐 수 있다.

## 이론 (Theory)

Code smell은 긴 함수, 중복, divergent change, shotgun surgery, primitive obsession 같은 개선 신호이지 자동 판결이 아니다. Characterization test로 기존 behavior를 고정하고 extract, rename, move, introduce parameter object 등을 적용한다.

Refactoring 전후 public behavior가 같다는 범위에는 output뿐 아니라 exception, side effect, protocol compatibility와 필요한 성능 contract가 포함될 수 있다.

## 구현 (Implementation)

```python
def overdue_fee(days_late, daily_rate):
    billable_days = max(days_late - 3, 0)
    return billable_days * daily_rate
```

중복 계산을 이름 있는 함수로 추출하면 test와 변경 지점이 명확해진다.

## 복잡도 (Complexity)

Runtime complexity를 유지하는 경우가 많지만 구조 변경이 성능을 바꿀 수 있어 benchmark contract도 필요하다. 작은 단계는 review·rollback 비용을 줄인다.

## 응용 (Applications)

- legacy code 개선
- 새 기능 전 variation point 준비
- 중복 제거·module 경계 정리
- architecture migration

## 흔한 오해 (Common Misunderstandings)

- test 없이 큰 rewrite를 리팩토링이라 부르기 어렵다.
- behavior 유지가 bug까지 영원히 보존하라는 뜻은 아니다. 별도 변경으로 고친다.
- 모든 smell을 즉시 제거할 필요는 없다.
- refactor와 feature change를 한 commit에 섞으면 검토가 어려워진다.

## TMI

- strangler pattern은 legacy system을 경계별로 점진 교체한다.
- IDE rename도 symbol 해석이 정확할 때 안전하다.
- branch by abstraction은 장기 migration 중 두 구현을 전환한다.

## 연습 / 확인 문제 (Exercises)

- 긴 함수를 characterization test 뒤 분해하라.
- shotgun surgery 사례에서 변경 지점을 모아라.
- refactor와 behavior change commit을 분리하라.

## 이어서 읽기 (Reading Path)

- 이전: [클린 코드](Clean-Code.md)
- 다음: [단위 테스트 원칙](../Testing/Unit-Test-Principles.md)

## 참조 (References)

- [Engineering/Testing/Unit-Test-Principles.md](../Testing/Unit-Test-Principles.md)
- [Reference/Books.md](../../Reference/Books.md)
