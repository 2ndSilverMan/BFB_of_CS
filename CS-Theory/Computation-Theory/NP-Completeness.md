# NP-완전성과 환원 (NP-Completeness & Reductions)

- Level: Advanced
- Prerequisites: [CS-Theory/Computation-Theory/Complexity-Classes.md](Complexity-Classes.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

NP-완전(NP-complete) 문제는 **NP 안에서 가장 어려운 문제들**이다. NP에 속하면서, NP의 모든 문제가 그것으로 다항 시간에 **환원(reduction)** 될 수 있다. 따라서 NP-완전 문제 하나라도 다항 시간에 풀린다면 NP 전체가 다항 시간에 풀려 $\text{P}=\text{NP}$가 된다.

## 직관 (Intuition)

수천 개의 어려운 문제가 알고 보면 "같은 난이도의 한 문제"의 변장이라면? NP-완전 문제들이 그렇다 — 외판원 문제, 그래프 색칠, 스도쿠가 서로 변환 가능해, 하나를 빠르게 풀면 전부 빠르게 풀린다. 그래서 어떤 새 문제가 NP-완전임을 보이면, "이건 (아마도) 빠른 정확해가 없다"는 강력한 신호가 된다.

## 이론 (Theory)

핵심 도구는 **다항 시간 환원** $A \le_p B$ — 문제 $A$의 임의 입력을 다항 시간에 문제 $B$의 입력으로 변환해, $B$의 답이 $A$의 답을 그대로 알려 주는 것이다. "$A \le_p B$이면 $B$는 $A$만큼 어렵다."

두 정의를 구분한다.

| 용어 | 조건 |
|---|---|
| NP-난해(NP-hard) | NP의 모든 문제가 이것으로 환원됨 (NP 소속은 불필요) |
| NP-완전(NP-complete) | NP-난해 **이면서** 자신도 NP에 속함 |

**쿡-레빈 정리(Cook-Levin theorem, 1971)** 는 **SAT**(부울 만족 가능성 문제)가 최초의 NP-완전 문제임을 증명했다. 이후 새 문제 $X$가 NP-완전임을 보이려면 두 가지만 하면 된다.

1. $X \in \text{NP}$ (답을 다항 시간에 검증 가능)
2. 이미 알려진 NP-완전 문제 $Y$에 대해 $Y \le_p X$ (환원)

카프(Karp)가 1972년 21개 문제를 이렇게 줄줄이 NP-완전으로 증명한 뒤, 현재 수천 개가 알려져 있다(3-SAT, 정점 덮개, 해밀턴 경로, 부분집합 합, 배낭 등).

## 구현 (Implementation)

3-SAT → 정점 덮개(Vertex Cover)류 환원의 아이디어 대신, 검증 가능성(NP 소속)을 SAT로 보인다.

```python
# SAT 검증: 변수 할당이 주어지면 절(clause)들이 모두 참인지 O(절 수)에 확인
def verify_sat(clauses, assignment):
    # clauses: [[1, -2, 3], ...]  (양수=변수, 음수=부정)
    for clause in clauses:
        if not any(
            (lit > 0 and assignment[abs(lit)]) or
            (lit < 0 and not assignment[abs(lit)])
            for lit in clause
        ):
            return False        # 한 절이라도 거짓이면 불만족
    return True

clauses = [[1, -2], [2, 3]]
print(verify_sat(clauses, {1: True, 2: False, 3: True}))   # True
```

푸는 것은 어렵지만(변수 `n`개에 최악 `O(2^n)`), 검증은 다항 시간임이 NP-완전성의 출발점이다.

## 복잡도 (Complexity)

| 항목 | 의미 |
|---|---|
| 환원 비용 | 다항 시간이어야 의미가 있음 |
| NP-완전 문제 풀이 | 알려진 최선이 지수/준지수 시간 |
| 함의 | 하나라도 다항 시간 해 → P=NP |

NP-완전임이 P≠NP를 증명하는 것은 아니다. 다만 "다항 시간 해가 있을 가망이 매우 낮다"는 실용적 결론을 준다.

## 응용 (Applications)

- 새 문제의 난이도 진단(NP-완전이면 정확·빠른 해 단념)
- 대신 근사 알고리즘·휴리스틱·정수계획법·SAT 솔버로 우회
- 스케줄링, 경로 최적화, 자원 배분의 현실적 접근 결정
- 암호학적 가정의 근거(일부)

## 흔한 오해 (Common Misunderstandings)

- NP-완전과 NP-난해는 다르다. NP-난해는 NP에 속하지 않아도 되며(정지 문제는 NP-난해지만 NP-완전 아님), NP-완전은 NP 소속이 필수다.
- NP-완전이 "풀 수 없다"는 뜻은 아니다. 작은 입력이나 특수 구조에서는 충분히 풀린다. 어려운 것은 최악의 일반 경우다.
- 환원 방향을 헷갈리기 쉽다. $X$가 어렵다고 보이려면 **알려진 어려운 문제를 $X$로** 환원해야 한다(반대가 아니다).
- NP-완전 문제를 만났다고 포기할 필요는 없다. 근사·휴리스틱·솔버가 실무에선 충분히 잘 동작하는 경우가 많다.

## TMI

- 카프의 1972년 논문 "Reducibility Among Combinatorial Problems"의 21개 NP-완전 문제 목록은 복잡도 이론의 출발점으로 꼽힌다.
- 현대 SAT 솔버는 이론적으로 NP-완전인 SAT를 수백만 변수 규모에서도 종종 빠르게 푼다. "최악은 지수, 실전은 놀랍게 빠름"의 대표 사례다.
- 테트리스, 슈퍼마리오, 캔디 크러시의 일반화 버전이 NP-난해 또는 그 이상임이 증명돼 있다. 게임의 난이도가 이론적으로 뒷받침된 셈이다.

## 연습 / 확인 문제 (Exercises)

- $A \le_p B$일 때 "$B$가 쉬우면 $A$도 쉽다"가 성립하는 이유를 설명하라.
- 어떤 문제가 NP-완전임을 보이는 2단계 절차를 직접 서술하라.
- NP-난해이지만 NP-완전이 아닌 문제의 예를 하나 들고 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [복잡도 클래스](Complexity-Classes.md)
- 다음: [근사 알고리즘](../../Algorithms/Approximation-Algorithms.md)
- 관련: [결정 불가능성](Undecidability.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Complexity-Classes.md](Complexity-Classes.md)
- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
