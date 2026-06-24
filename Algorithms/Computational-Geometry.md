# 계산 기하학 (Computational Geometry)

- Level: Advanced
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md), [Algorithms/Sorting.md](Sorting.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

계산 기하학은 점·선·다각형 같은 기하 객체에 대한 알고리즘을 다룬다. 볼록 껍질, 선분 교차, 가장 가까운 점 쌍, 다각형 포함 판정 등이 핵심 문제다.

## 직관 (Intuition)

"점들을 감싸는 가장 작은 볼록 다각형은?", "두 선분이 만나는가?" 같은 기하 질문은 그림으로는 쉬워도 좌표로 정확·빠르게 풀려면 영리한 알고리즘과 수치 안정성이 필요하다. 핵심 도구는 외적(cross product)으로 "왼쪽/오른쪽/일직선"을 판별하는 것이다.

## 이론 (Theory)

**방향 판정(orientation)**: 세 점 $O,A,B$의 외적 부호로 좌회전/우회전/일직선을 구분한다.

$$(A-O)\times(B-O)=(A_x-O_x)(B_y-O_y)-(A_y-O_y)(B_x-O_x)$$

핵심 알고리즘:
- **볼록 껍질**: Graham scan·Andrew monotone chain, 정렬 후 `O(n log n)`.
- **선분 교차**: 방향 판정 4번으로 두 선분 교차 여부. 여러 선분은 스위프 라인으로 `O(n log n)`.
- **가장 가까운 점 쌍**: 분할 정복으로 `O(n log n)`.
- **점-다각형 포함**: ray casting(홀짝) 또는 winding number.

수치 정밀도(부동소수점)와 퇴화 케이스(공선, 중복점) 처리가 실무의 난점이다.

## 구현 (Implementation)

```python
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):                   # Andrew monotone chain
    pts = sorted(set(points))
    if len(pts) <= 2: return pts
    def half(pts):
        h = []
        for p in pts:
            while len(h) >= 2 and cross(h[-2], h[-1], p) <= 0:
                h.pop()                     # 우회전이면 제거 → 볼록 유지
            h.append(p)
        return h[:-1]
    return half(pts) + half(pts[::-1])      # 하단 + 상단
```

## 복잡도 (Complexity)

| 문제 | 시간 |
|---|---|
| 볼록 껍질 | `O(n log n)` |
| 선분 교차(스위프) | `O(n log n)` |
| 가장 가까운 점 쌍 | `O(n log n)` |
| 점-다각형 포함 | `O(n)` |

대부분 정렬·스위프가 병목이라 `O(n log n)`이다. 공간은 보통 `O(n)`.

## 응용 (Applications)

- 컴퓨터 그래픽스·게임(충돌, 가시성)
- GIS·지도(영역 포함, 경로)
- 로보틱스 경로 계획·모션
- VLSI 설계, 패턴 인식

## 흔한 오해 (Common Misunderstandings)

- 부동소수점 오차가 방향 판정을 뒤집을 수 있어, 정수 좌표나 정밀 비교가 필요하다.
- 퇴화 케이스(공선점, 중복점)를 무시하면 볼록 껍질이 깨진다.
- 외적 부호는 좌표계(좌수/우수) 규약에 의존한다.
- ray casting의 점이 경계·꼭짓점에 닿는 경우는 별도 처리가 필요하다.

## TMI

- Graham scan(1972)은 정렬 + 스택이라는 단순 구조로 볼록 껍질을 푸는 고전이다.
- "회전하는 캘리퍼스(rotating calipers)"는 볼록 다각형의 지름·너비를 선형에 구하는 우아한 기법이다.
- 계산 기하의 정밀도 문제는 "robust geometry"라는 별도 연구 분야를 낳았다.

## 연습 / 확인 문제 (Exercises)

- 외적 부호로 세 점의 방향(좌/우/일직선)을 판정하라.
- 작은 점 집합의 볼록 껍질을 monotone chain으로 구하라.
- ray casting으로 점의 다각형 내부 여부를 판정하는 절차를 기술하라.

## 이어서 읽기 (Reading Path)

- 이전: [랜덤 알고리즘](Randomized-Algorithms.md)
- 다음: [병렬 알고리즘](Parallel-Algorithms.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md)
- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Reference/Books.md](../Reference/Books.md)
