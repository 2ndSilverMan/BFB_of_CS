# 렌더링 기초 (Rendering Fundamentals)

- Level: Intermediate
- Prerequisites: [기하 변환과 카메라](Geometry-and-Cameras.md), 이차방정식, 내적
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (핵심 원리와 제한된 예제)

---

## 개념 (Concept)

렌더링은 장면·카메라·재질·광원을 이용해 영상의 샘플을 계산하는 과정이다. geometry가 어디에 있는지, 어느 표면이 보이는지, 그 표면에서 어떤 빛이 오는지는 다른 문제다. 여기서는 가시성을 중심으로 래스터화와 광선 교차를 비교하고, 하나의 구에 대한 작은 교차 검사를 구현한다. 완전한 물리 기반 렌더러는 아니다.

## 직관 (Intuition)

래스터화는 “이 삼각형이 덮는 픽셀은 무엇인가”를 묻고, ray casting은 “이 픽셀 방향의 광선이 처음 만나는 표면은 무엇인가”를 묻는다. 두 방법 모두 가려진 뒤쪽 표면을 그대로 그리면 잘못된 결과가 된다. 그림자·반사·간접광은 첫 교차만 찾는 문제를 넘어선다.

## 이론 (Theory)

래스터화의 기본 흐름은 정점 변환 → clipping → 화면상의 샘플 포함 검사 → 속성 보간 → 깊이 검사 → shading이다. 삼각형 내부의 점은 세 꼭짓점에 대한 barycentric 좌표로 표현할 수 있다. 원근 투영 뒤 texture 좌표 등을 단순 선형 보간하면 왜곡될 수 있어 perspective-correct interpolation이 필요하다.

광선은 $p(t)=o+td$, $t>0$로 나타낸다. 중심 c, 반지름 r인 구는 $\|p-c\|^2=r^2$이므로 다음 이차식이 된다.

$$a=d\cdot d,\quad b=2d\cdot(o-c),\quad k=(o-c)\cdot(o-c)-r^2$$
$$at^2+bt+k=0$$

판별식이 음수면 교차가 없고, 근 중 양수인 가장 작은 t를 택한다. d가 단위벡터가 아니면 t는 거리 자체가 아니다. [PBRT 구 절](https://pbr-book.org/4ed/Shapes/Spheres)은 이 관계뿐 아니라 부동소수 오차를 고려한 구현을 다룬다. 아래 예제는 교육용 보통 정밀도 계산이므로 접선·매우 큰 좌표의 강건성을 보장하지 않는다.

## 구현 (Implementation)

원점에서 +z로 쏜 광선과 중심 (0,0,5), 반지름 1인 구의 첫 교차는 t=4다. 구 내부에서 출발하면 음수인 진입근을 버리고 양수인 출구근을 택한다.

```python
from math import sqrt, isclose

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def first_hit(origin, direction, center, radius):
    if radius <= 0:
        raise ValueError("positive radius required")
    oc = tuple(x-y for x, y in zip(origin, center))
    a = dot(direction, direction)
    if a == 0:
        raise ValueError("nonzero direction required")
    b = 2 * dot(direction, oc)
    k = dot(oc, oc) - radius*radius
    disc = b*b - 4*a*k
    if disc < 0:
        return None
    roots = ((-b-sqrt(disc))/(2*a), (-b+sqrt(disc))/(2*a))
    positive = [t for t in roots if t > 0]
    return min(positive) if positive else None

sphere = ((0, 0, 5), 1)
assert isclose(first_hit((0, 0, 0), (0, 0, 1), *sphere), 4)
assert isclose(first_hit((0, 0, 0), (0, 0, 2), *sphere), 2)
assert first_hit((0, 0, 0), (0, 1, 0), *sphere) is None
assert first_hit((0, 0, 0), (0, 0, -1), *sphere) is None
assert isclose(first_hit((0, 0, 5), (0, 0, 1), *sphere), 1)
```

첫 교차점은 (0,0,4), 바깥쪽 법선은 (0,0,-1)이다. 표면에서 광원으로 향하는 단위 방향 l=(0,0,-1)이면 $\max(0,n\cdot l)=1$이고 반대면 0이다. 이는 cosine 기하 인자만 계산한 것이다. 실제 출력 radiance에는 광원·BRDF·가림·단위·색 공간 처리가 추가된다.

## 복잡도 (Complexity)

N개 물체를 P개 광선과 모두 비교하면 단순 구현은 O(PN)이다. BVH 같은 가속 구조는 많은 장면에서 검사를 줄이지만 모든 장면에서 O(log N)이라고 단정할 수 없다. 래스터화도 삼각형 수만이 아니라 덮는 샘플 수, overdraw, shading 비용에 영향을 받는다.

## 응용 (Applications)

3D 미리보기, picking, 충돌 후보 확인, 시뮬레이션 영상 생성에 활용한다. ray casting은 광선의 첫 교차이고 path tracing은 빛의 여러 경로를 표본화하는 계산이므로 같은 이름으로 섞지 않는다.

## 흔한 오해 (Common Misunderstandings)

- 교차 t가 가장 작으면 항상 앞에 있다: 양수인지와 광선 규약을 먼저 확인한다.
- 더 많은 폴리곤이면 물리적으로 정확하다: 조명·재질·샘플링 모델도 중요하다.
- z-buffer가 투명도를 모두 해결한다: 여러 층의 혼합은 추가 처리와 순서 문제가 있다.

## TMI

- 수치 오차로 반사·그림자 광선이 출발 표면을 다시 맞는 self-intersection이 생길 수 있다.
- 선형 광량 공간에서의 연산과 화면 인코딩 값의 연산을 구분해야 밝기 혼합을 해석할 수 있다.

## 연습 / 확인 문제 (Exercises)

1. 중심 (0,0,10), 반지름 2라면 단위 +z 광선의 첫 교차는? **답:** t=8.
2. 구 내부 출발에서 작은 근만 고르면 어떤 오류가 생기는가? **답:** 음수 근을 선택해 뒤쪽 교차를 보고한다.
3. 렌더 결과가 검다고 교차 실패라고 할 수 있는가? **판단 기준:** 기하·가시성·법선·광원·색 변환을 분리하여 진단한다.

## 이어서 읽기 (Reading Path)

- 관련: [자료구조](../../Data-Structures/), [수치계산](../../Math/Numerical-Methods/).
- 다음: [데이터 시각화](Data-Visualization.md) — 영상 생성과 정보 전달의 다른 목적.

## 참조 (References)

- [PBRT 4판 — Spheres](https://pbr-book.org/4ed/Shapes/Spheres) — 광선-구 이차식, 근 선택, 수치 강건성. 본문의 짧은 코드는 원문 코드를 복사하지 않은 교육용 구현이다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 래스터화/광선 질문의 비교, 구의 근 선택과 실패 입력, 가시성과 shading 구분.
- 보충할 내용: 삼각형 래스터화 실습, BVH, texture·BRDF·샘플링, 실제 영상 렌더 결과 검증.
- 확인 상태: 2026-09-18 PBRT 구 교차 절 확인. Python 교차 모델 외 GPU·영상 품질·강건한 수치 구현은 검증하지 않았다. Python 3.12/Windows에서 본문의 Python 1개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
