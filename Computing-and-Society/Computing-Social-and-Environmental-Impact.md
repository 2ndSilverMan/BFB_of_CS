# 컴퓨팅의 사회·환경적 영향 (Computing Social and Environmental Impact)

- Level: Beginner
- Prerequisites: [전문직 윤리](Computing-Professional-Ethics.md), 단위와 비율 계산
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (사례 분석과 판단 기준)

---

## 개념 (Concept)

컴퓨팅의 영향은 프로그램의 출력뿐 아니라 누가 접근하고 누가 비용을 지불하며 어떤 자원을 소비하는지까지 포함한다. 효율·편의·매출 같은 단일 지표가 사회적 이익 전체를 대표하지 않는다. 여기서는 분배·접근 격차·측정 경계와 탄소 집약도의 작은 계산을 다룬다. 컴퓨팅 역사·정치경제 전체를 대신하는 개론은 아니다.

## 직관 (Intuition)

한 번의 요청에 필요한 에너지를 절반으로 줄였어도 요청 수가 세 배가 되면 총 에너지는 늘 수 있다. 온라인 신청을 빠르게 만든 서비스도 오프라인 대안을 없애면 장치·네트워크·보조 기술에 접근하기 어려운 사람에게 비용을 넘길 수 있다. 평균 효율과 누구에게 미치는 결과를 나눠 봐야 한다.

## 이론 (Theory)

시스템 경계는 포함하는 기기·네트워크·데이터센터·제조·사용 기간을 정한다. 기능 단위는 요청 한 건, 학습 한 회, 유효한 결과 한 건처럼 비교의 분모다. 서로 다른 경계·품질·분모의 수치를 같은 성능 순위로 비교하지 않는다.

[Green Software Foundation SCI 명세 1.1.0](https://sci.greensoftware.foundation/)는 운영 에너지 E, 전력 탄소 집약도 I, 할당한 내재 배출 M과 기능 단위 R로 $SCI=(E\times I+M)/R$을 계산하는 방법을 설명한다. 여기서는 단위를 맞춘 가상 계산만 수행한다. 실제 전력 계측·제조 배출 할당·공식 평가를 한 것은 아니다.

사회적 영향 분석은 이익과 부담의 분포를 비교한다. 신청 시간이 줄어든 평균값 외에 저속 연결·낮은 문해력·언어 차이·보조 기술 사용 시 실패가 어떻게 달라지는지 검토한다. 관측하지 않은 집단의 결과를 추정값으로 사실처럼 쓰지 않는다.

## 구현 (Implementation)

가상 시스템 A의 하루 에너지 10kWh, I=400gCO2e/kWh, 하루에 할당한 M=1,000gCO2e, 요청 수 100,000이라 두면 총 5,000gCO2e, 요청당 0.05g이다. 같은 요청 수에서 에너지만 6kWh로 줄이면 0.034g이 된다.

```python
from math import isclose

def intensity(energy_kwh, grams_per_kwh, embodied_grams, units):
    if min(energy_kwh, grams_per_kwh, embodied_grams) < 0 or units <= 0:
        raise ValueError("nonnegative emissions and positive units required")
    return (energy_kwh * grams_per_kwh + embodied_grams) / units

assert isclose(intensity(10, 400, 1000, 100_000), 0.05)
assert isclose(intensity(6, 400, 1000, 100_000), 0.034)
old_total = 100_000 * 0.05
new_total = 300_000 * 0.034  # 단위 집약도가 유지된다는 추가 가정
assert new_total > old_total
assert isclose(new_total, 10_200)
```

사회적 영향을 함께 기록하는 교육용 설계표는 다음과 같다.

| 변경안 | 기대 이익 | 부담을 질 수 있는 대상 | 확인할 증거·대안 |
|---|---|---|---|
| 이미지 압축 | 트래픽·대기 감소 | 작은 글자를 읽는 사용자 | 확대 가독성과 대체 텍스트 |
| 온라인 전용 신청 | 운영 시간 감소 | 접속·기기 제약이 있는 사람 | 전화·방문 등 대체 경로 |
| 야간 일괄 계산 | 전력 조건에 따른 배출 변화 가능 | 결과를 즉시 필요로 하는 사람 | deadline·지역별 전력 자료·보관 비용 |

“야간이 항상 저탄소” 같은 일반화는 하지 않는다. 시간·지역의 자료와 서비스 제약을 확인해야 한다.

## 복잡도 (Complexity)

실측 에너지와 제조 배출의 할당에는 오차가 있고 전력 계수도 공간·시간·방법에 따라 달라진다. 요청 수가 늘면 캐시·서버 수·네트워크 비용이 바뀌어 같은 단위 집약도가 유지되지 않을 수 있다. 영향 점검에는 기술 지표뿐 아니라 접근 실패·업무 이전·장기 유지보수 같은 다른 단위의 근거가 필요하다.

## 응용 (Applications)

서비스 경량화, 장비 교체·수명 연장, 캐시·배치 설계, 공공 서비스 접근성 비교에 사용한다. 낡은 장비 유지가 항상 최선이거나 새 장비 교체가 항상 효율적이라고 단정하지 않고 제조·운영의 경계와 수명을 비교한다.

## 흔한 오해 (Common Misunderstandings)

- 클라우드면 배출이 없다: 물리 하드웨어와 전력 사용이 남는다.
- 요청당 개선이 총량 감소다: 수요와 서비스 범위를 함께 봐야 한다.
- 평균 사용자에게 편하면 모두에게 좋다: 접근 실패와 비용의 분포를 확인한다.

## TMI

- 측정 경계 밖으로 계산을 옮기는 것과 실제 배출을 줄이는 것은 다르다.
- 기능 단위를 “유효한 결과”로 잡으면 재시도·실패 요청 비용을 숨기기 어려워진다.

## 연습 / 확인 문제 (Exercises)

1. A에서 I가 200으로 줄고 다른 조건이 같다면? **답:** (10×200+1000)/100000=0.03g/요청.
2. 제조 배출을 빼고 두 기기를 비교하면 어떤 판단이 왜곡될 수 있나? **답:** 교체 비용·수명·할당 기간의 영향을 놓칠 수 있다.
3. 온라인 전용 전환을 평가할 지표를 제안하라. **판단 기준:** 평균 시간 외에 실패율의 집단/환경별 차이, 대체 경로, 관측 범위가 포함된다.

## 이어서 읽기 (Reading Path)

- 관련: [접근성](../Graphics-and-Interaction/HCI/Accessible-Interaction.md), [성능](../Engineering/Performance/).
- 다음: [연구 설계](../Research-Practice/Research-Design-and-Validity.md).

## 참조 (References)

- [Green Software Foundation — Software Carbon Intensity Specification 1.1.0](https://sci.greensoftware.foundation/) — 계산 경계·기능 단위·운영 및 내재 배출의 구분. 예제 숫자는 실측이 아니다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 단위 집약도와 총량 차이, 기능 단위·경계의 명시, 접근성 부담 비교.
- 보충할 내용: 실제 에너지 계측과 불확실성, 컴퓨팅 역사·노동·플랫폼 경제의 근거 있는 사례.
- 확인 상태: 2026-09-18 SCI 1.1.0 소개·계산 구조 확인. 에너지·탄소·집단별 사용자 영향을 실측하지 않았다. Python 3.12/Windows에서 본문의 Python 1개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
