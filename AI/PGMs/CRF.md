# 조건부 랜덤 필드 (Conditional Random Field, CRF)

- Level: Advanced
- Prerequisites: [MRF.md](MRF.md), [HMM.md](HMM.md), [Cliques.md](Cliques.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

CRF는 관측 $X$가 주어졌을 때 라벨 $Y$의 조건부분포 $P(Y\mid X)$를 무방향 그래프로 모델링하는 판별적 시퀀스/구조 예측 모델이다. HMM이 관측까지 함께 생성하는 모델이라면, CRF는 라벨 조건부분포에 직접 집중한다.

## 직관 (Intuition)

문장의 품사를 예측할 때 현재 단어뿐 아니라 주변 단어, 대문자 여부, 접미사, 이전/다음 라벨 관계를 함께 보고 싶다. CRF는 이런 다양한 feature를 라벨 시퀀스 전체의 일관성과 함께 점수화한다.

## 이론 (Theory)

선형 체인 CRF는 다음 형태로 쓸 수 있다.

$$
P(y\mid x)=\frac{1}{Z(x)}
\exp\left(\sum_t \sum_k w_k f_k(y_{t-1},y_t,x,t)\right)
$$

$f_k$는 feature function이고, $Z(x)$는 입력 $x$에 대한 정규화 상수다. HMM과 달리 관측 feature의 독립 가정을 강하게 둘 필요가 없고, 임의의 overlapping feature를 사용할 수 있다.

추론은 forward-backward와 Viterbi의 변형으로 수행한다. 학습은 조건부 로그우도를 최대화하며, gradient는 관측 feature count와 모델 기대 feature count의 차이로 나타난다.

## 구현 (Implementation)

선형 체인 CRF의 local score는 transition score와 emission feature score를 더한 값으로 생각할 수 있다.

```python
def local_score(prev_y, y, x_t, weights):
    score = weights.get(("transition", prev_y, y), 0.0)
    score += weights.get(("word", y, x_t), 0.0)
    return score


weights = {
    ("transition", "NOUN", "VERB"): 0.4,
    ("word", "NOUN", "dog"): 1.2,
    ("word", "VERB", "runs"): 1.5,
}

print(local_score("NOUN", "VERB", "runs", weights))
```

실제 CRF는 dynamic programming으로 모든 라벨 시퀀스의 점수를 합산하거나 최적 시퀀스를 찾는다.

## 복잡도 (Complexity)

라벨 수가 $K$, 시퀀스 길이가 $T$이면 선형 체인 CRF의 forward/Viterbi는 보통 $O(TK^2)$이다. 일반 그래프 구조 CRF는 treewidth에 따라 비용이 지수적으로 커질 수 있다.

## 응용 (Applications)

- 품사 태깅
- 개체명 인식
- 형태소 분석과 시퀀스 라벨링
- 이미지 segmentation의 구조 예측 모델

## 흔한 오해 (Common Misunderstandings)

- CRF는 HMM보다 항상 좋은 것이 아니라 feature와 데이터, 비용에 따라 다르다.
- CRF도 정규화 상수 계산이 필요하다. 다만 입력 조건부 정규화다.
- 독립 feature를 요구하지 않는다고 아무 feature나 넣어도 되는 것은 아니다.
- 딥러닝 sequence tagger 이후에도 CRF layer는 라벨 전이 제약을 넣는 데 쓰인다.

## TMI

- BiLSTM-CRF는 신경망 emission score와 CRF transition 구조를 결합한 고전적인 NER 구조다.
- label bias problem은 locally normalized sequence model의 한계로 CRF 도입 동기 중 하나다.
- CRF는 log-linear model과 graphical model의 교차점에 있다.

## 연습 / 확인 문제 (Exercises)

- HMM과 CRF의 생성/판별 차이를 설명하라.
- 선형 체인 CRF에서 transition feature가 왜 필요한지 예를 들어라.
- 라벨 수가 20, 길이가 100이면 기본 Viterbi 비용의 차수를 계산하라.

## 이어서 읽기 (Reading Path)

- 이전: [클리크와 포텐셜](Cliques.md)
- 다음: [변수 소거](Variable-Elimination.md)

## 참조 (References)

- [MRF.md](MRF.md)
- [HMM.md](HMM.md)
- [Cliques.md](Cliques.md)
- [Reference/Books.md](../../Reference/Books.md)
