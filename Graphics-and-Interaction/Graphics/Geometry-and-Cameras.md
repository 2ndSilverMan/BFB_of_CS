# 기하 변환과 카메라 (Geometry and Cameras)

- Level: Intermediate
- Prerequisites: [벡터](../../Math/Linear-Algebra/Vectors.md), [행렬](../../Math/Linear-Algebra/Matrices.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (핵심 원리와 제한된 예제)

---

## 개념 (Concept)

기하 변환은 같은 물체를 다른 좌표계로 표현하거나 위치·방향·크기를 바꾸는 연산이다. 카메라는 공간의 점을 영상의 위치에 대응시키는 모델이다. 여기서는 열벡터, 오른쪽부터 적용하는 행렬 곱, 카메라 전방 +z라는 규약을 사용한다. 특정 그래픽 API의 축·깊이 규약과 같다고 가정하지 않는다.

## 직관 (Intuition)

카메라를 오른쪽으로 옮기면 화면 속 정지 물체는 왼쪽으로 이동한다. 물체를 옮긴 것이 아니라 관측 기준이 바뀐 것이다. 같은 좌표 숫자라도 world인지 camera인지 표시하지 않으면 회전·이동의 부호가 뒤섞인다.

## 이론 (Theory)

3차원 점은 동차좌표 $(x,y,z,1)$, 방향은 $(d_x,d_y,d_z,0)$로 나타낸다. 마지막 성분 덕분에 평행이동 행렬이 점에는 작용하지만 방향에는 작용하지 않는다. 아핀 변환 $M$은 모델 좌표를 world로, view 변환 $V$는 world를 camera로 바꾼다. 카메라 pose가 camera-to-world 변환 $C$라면 $V=C^{-1}$다.

$VMp$에서 M이 먼저 적용된다. 일반적으로 $TRp\ne RTp$다. 원점을 기준으로 회전한 뒤 이동하는 것과 이동한 점을 원점 주위로 회전하는 것은 다르기 때문이다.

핀홀 모델에서 $z>0$인 camera 점을 가상 영상 평면에 투영하면 $u=f_xx/z+c_x$, $v=f_yy/z+c_y$다. 여기서는 영상 y도 위쪽 증가로 두었다. 배열 행 번호가 아래로 증가하는 영상에는 별도 y 반전이 필요하다. [PBRT의 투영 카메라](https://pbr-book.org/4ed/Cameras_and_Film/Projective_Camera_Models)는 직교·원근 카메라의 구분과 좌표 변환을 설명한다.

직교 투영은 깊이에 따른 크기 변화가 없고, 원근 투영은 깊이로 나눈다. 원근 변환은 정보를 잃으므로 화면 점 하나만으로 원래 3차원 점을 복원하지 못한다. 카메라에서 나가는 광선 위 후보가 남는다.

## 구현 (Implementation)

카메라는 world의 (1,0,0)에 있고 축은 world와 평행하다고 가정한다. world 점 (3,2,4)는 camera에서 (2,2,4)다. $f_x=f_y=100$, 주점 (320,240)이면 화면 좌표는 (370,290)이다. 렌즈 왜곡·센서 크기·clipping은 생략한다.

```python
from math import isclose

def matvec(m, v):
    return tuple(sum(a*b for a, b in zip(row, v)) for row in m)

view = ((1, 0, 0, -1), (0, 1, 0, 0),
        (0, 0, 1, 0), (0, 0, 0, 1))
point = matvec(view, (3, 2, 4, 1))
direction = matvec(view, (1, 0, 0, 0))
assert point == (2, 2, 4, 1)
assert direction == (1, 0, 0, 0)

def project(p, fx=100, fy=100, cx=320, cy=240):
    x, y, z = p
    if z <= 0:
        raise ValueError("requires a point in front of the camera")
    return fx*x/z + cx, fy*y/z + cy

assert project(point[:3]) == (370, 290)
assert project((4, 4, 8)) == (370, 290)
try:
    project((1, 1, 0))
except ValueError:
    pass
else:
    raise AssertionError("z=0 must be rejected")
```

## 복잡도 (Complexity)

고정 크기 행렬의 점당 계산은 상수 비용이며 N개 점에는 O(N)이다. 실제 비용에는 clipping·가시성·래스터화가 추가된다. z가 0에 가까우면 작은 오차가 큰 화면 이동으로 확대된다. nonuniform scale 아래 표면 법선은 일반 방향처럼 M으로만 변환하면 표면에 수직이라는 성질을 잃을 수 있다. 역전치 변환과 정규화가 필요한 이유를 내적 보존으로 유도할 수 있다.

## 응용 (Applications)

3D 렌더링, 로봇 좌표 변환, 카메라 보정의 기초다. 컴퓨터 비전은 관측 영상으로 공간·카메라를 추정하는 역문제를, 그래픽스는 주어진 공간에서 영상을 생성하는 순방향 문제를 자주 다룬다.

## 흔한 오해 (Common Misunderstandings)

- 행렬 저장 순서와 벡터 곱 규약은 같다: row-major 메모리 배치만으로 변환 적용 순서를 알 수 없다.
- 3D 점과 방향은 같은 변환을 받는다: 평행이동 적용 여부가 다르다.
- 카메라 위치를 그대로 view의 translation에 넣으면 된다: pose의 역변환이 필요하다.

## TMI

- near/far clipping은 화면 밖 점을 자르는 것뿐 아니라 깊이 표현과 수치 정밀도에도 영향을 준다.
- 화면 좌표의 원점과 픽셀 중심 규약을 명시해야 반 픽셀 차이의 원인을 추적할 수 있다.

## 연습 / 확인 문제 (Exercises)

1. 같은 카메라에서 world 점 (5,4,8)을 투영하면? **답:** camera (4,4,8), 화면 (370,290).
2. 방향 (0,1,0,0)에 view를 곱하면? **답:** 변화 없음. 카메라가 회전하면 방향도 회전한다.
3. 화면 좌표가 같다는 것이 world 점이 같다는 뜻인가? **답:** 아니다. 위 두 점이 반례다.

## 이어서 읽기 (Reading Path)

- 다음: [렌더링 기초](Rendering-Fundamentals.md).
- 관련: [컴퓨터 비전](../../AI/Computer-Vision/), [선형시스템](../../Math/Linear-Algebra/Linear-Systems.md).

## 참조 (References)

- [Pharr, Jakob, Humphreys, PBRT 4판 — Projective Camera Models](https://pbr-book.org/4ed/Cameras_and_Film/Projective_Camera_Models) — 직교·원근 카메라와 좌표 변환. 본문의 규약과 수치는 별도로 명시했다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: pose/view 역관계, 점·방향 비교, 투영의 비가역성 수치 예제.
- 보충할 내용: 회전 포함 카메라, homogeneous clipping, normal 역전치 증명, 렌즈 왜곡.
- 확인 상태: 2026-09-18 PBRT 카메라 모델 절 확인. Python 대수 계산 외 실제 GPU 영상·카메라 보정 실험은 하지 않았다. Python 3.12/Windows에서 본문의 Python 1개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
