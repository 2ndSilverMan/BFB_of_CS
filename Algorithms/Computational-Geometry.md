# 계산 기하학 (Computational Geometry)

- Level: Advanced
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md), [Algorithms/Sorting.md](Sorting.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

계산 기하학은 점·선·다각형 같은 기하 객체의 알고리즘을 다룬다. 볼록 껍질, 선분 교차, 가장 가까운 점 쌍, 다각형 포함 판정이 핵심이며, **외적(cross product) 기반 방향 판정**이 거의 모든 것의 토대다.

## 직관 (Intuition)

"점들을 감싸는 최소 볼록 다각형은?", "두 선분이 만나는가?"는 그림으론 쉬워도 좌표로 정확·빠르게 풀려면 영리한 알고리즘과 **수치 안정성**이 필요하다. 핵심 도구는 외적으로 "왼쪽/오른쪽/일직선"을 판별하는 것.

## 이론 (Theory)

### 1. 방향 판정 (orientation predicate)

세 점 $O,A,B$ 의 외적 부호:

$$(A-O)\times(B-O)=(A_x-O_x)(B_y-O_y)-(A_y-O_y)(B_x-O_x)$$

양수=좌회전(반시계), 음수=우회전, 0=공선. 이 한 술어로 볼록성·교차·포함이 모두 결정된다.

### 2. 핵심 알고리즘

- **볼록 껍질**: Andrew monotone chain / Graham scan — 정렬 후 우회전 점을 스택에서 제거, $O(n\log n)$.
- **선분 교차**: 두 선분의 끝점에 대한 방향 판정 4번. 여러 선분은 **스위프 라인**(Bentley-Ottmann) $O((n+k)\log n)$.
- **가장 가까운 점 쌍**: 분할 정복 + 경계 띠(strip) 검사 $O(n\log n)$.
- **점-다각형 포함**: ray casting(교차 홀짝) 또는 winding number.

### 3. 강건성(robustness)

부동소수점 오차가 방향 판정 부호를 뒤집으면 알고리즘이 깨진다 → **정수 좌표·정확 산술(exact arithmetic)**, 퇴화 케이스(공선·중복) 별도 처리가 실무 난점("robust geometry" 분야).

## 구현 (Implementation)

```python
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):                      # Andrew monotone chain, O(n log n)
    pts = sorted(set(points))
    if len(pts) <= 2: return pts
    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and cross(h[-2], h[-1], p) <= 0:
                h.pop()                        # 우회전/공선 제거 → 볼록 유지
            h.append(p)
        return h[:-1]                          # 마지막(다음 반쪽 시작점) 제외
    return half(pts) + half(pts[::-1])         # 하단 + 상단
```

## 복잡도 (Complexity)

| 문제 | 시간 | 공간 |
|---|---|---|
| 볼록 껍질 | $O(n\log n)$ | $O(n)$ |
| 선분 교차(스위프) | $O((n+k)\log n)$ | $O(n)$ |
| 가장 가까운 점 쌍 | $O(n\log n)$ | $O(n)$ |
| 점-다각형 포함 | $O(n)$ | $O(1)$ |

대부분 정렬·스위프가 병목이라 $O(n\log n)$. **워크드 예제.** 점 `(0,0),(1,1),(2,0),(1,-1),(1,0)`: monotone chain이 내부점 `(1,0)` 을 우회전 판정으로 제거 → 껍질 `(0,0),(1,-1),(2,0),(1,1)`.

## 응용 (Applications)

- 그래픽스·게임(충돌·가시성), GIS·지도(영역 포함·경로).
- 로보틱스 경로 계획, VLSI 설계, 패턴 인식·군집(볼록 껍질 특징).

## 흔한 오해 (Common Misunderstandings)

- **부동소수점 오차가 방향 판정을 뒤집는다** — 정수 좌표/정밀 비교 필요.
- **퇴화 케이스(공선·중복점)를 무시하면** 볼록 껍질이 깨진다.
- **외적 부호는 좌표계(좌수/우수) 규약에 의존**.
- **ray casting이 경계·꼭짓점에 닿는 경우**는 별도 처리.

## TMI

- Graham scan(1972)은 정렬 + 스택이라는 단순 구조의 고전이다.
- "회전하는 캘리퍼스(rotating calipers)"는 볼록 다각형의 지름·너비를 $O(n)$ 에 구하는 우아한 기법이다.
- CGAL은 정확 산술로 강건성을 보장하는 대표 계산 기하 라이브러리다.

## 연습 / 확인 문제 (Exercises)

- 외적 부호로 세 점의 방향(좌/우/공선)을 판정하라.
- 작은 점 집합의 볼록 껍질을 monotone chain으로 구하라.
- ray casting으로 점의 다각형 내부 여부를 판정하는 절차를 기술하라.
- 부동소수점 방향 판정이 틀리는 좌표 예를 만들고 정수 산술로 고쳐라.

## 이어서 읽기 (Reading Path)

- 이전: [랜덤 알고리즘](Randomized-Algorithms.md)
- 다음: [병렬 알고리즘](Parallel-Algorithms.md)
- 관련: [벡터](../Math/Linear-Algebra/Vectors.md), [분할 정복](Divide-and-Conquer.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md)
- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Reference/Books.md](../Reference/Books.md)
