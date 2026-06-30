# 로지스틱 회귀 (Logistic Regression)

- Level: Intermediate
- Prerequisites: [AI/Machine-Learning/Linear-Regression.md](Linear-Regression.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

로지스틱 회귀는 이름에 "회귀"가 들어가지만 **이진 분류** 모델이다. 입력의 가중합을 시그모이드 함수에 통과시켜, 결과를 0과 1 사이의 **확률**로 낸다.

## 직관 (Intuition)

선형 회귀는 $-\infty$부터 $+\infty$까지의 값을 낸다. 하지만 "스팸일 확률"은 0~1이어야 한다. 시그모이드는 어떤 실수든 부드럽게 0~1로 눌러 주는 S자 곡선이라, 가중합을 확률로 바꾸는 다리 역할을 한다.

```mermaid
flowchart LR
    X["특징 x"] --> LOGIT["logit z = theta^T x"]
    LOGIT --> SIG["sigmoid(z)"]
    SIG --> P["P(y=1|x)"]
    P --> THR["threshold 선택"]
    THR --> CLASS["class label"]
```

## 이론 (Theory)

시그모이드 함수와 모델:

$$\sigma(z) = \frac{1}{1 + e^{-z}}, \qquad P(y = 1 \mid x) = \sigma(\theta^\top x)$$

손실은 MSE가 아니라 **로그 손실(binary cross-entropy)** 을 쓴다. 선형 로지스틱 회귀의 로그 손실은 볼록이라 지역 최솟값에 갇히는 문제는 작다. 다만 정규화가 없고 데이터가 완전히 선형 분리되면 유한한 최적해가 없을 수 있으므로, 실무에서는 정규화와 수치 안정화가 중요하다.

$$J(\theta) = -\frac{1}{m}\sum_{i=1}^{m}\Big[\,y_i \log \hat{p}_i + (1 - y_i)\log(1 - \hat{p}_i)\,\Big]$$

여기서 $\hat{p}_i = \sigma(\theta^\top x_i)$다. 보통 $\hat{p} \ge 0.5$이면 클래스 1로 분류하며, 이 경계 $\theta^\top x = 0$이 **결정 경계**다.

### odds와 logit 해석

로지스틱 회귀는 확률 자체보다 log-odds를 선형 모델링한다.

$$
\log\frac{p}{1-p}=\theta^\top x
$$

따라서 계수 $\theta_j$가 1 증가하면, 다른 특징이 고정되어 있을 때 odds가 $e^{\theta_j}$배 곱해진다. 이 해석은 의료·리스크 모델에서 유용하지만, 상관된 특징과 표준화 여부를 함께 봐야 한다.

### threshold와 비용

0.5 임계값은 클래스 비용이 대칭이고 calibration이 괜찮을 때의 기본값이다. 사기 탐지나 의료 스크리닝처럼 false negative와 false positive 비용이 다르면 validation set에서 precision-recall, ROC, expected cost를 보고 threshold를 따로 정한다.

### 완전 분리와 규제

데이터가 어떤 직선으로 완전히 분리되면 로그손실은 파라미터 크기를 무한히 키워 계속 줄어들 수 있다. 이 경우 유한한 MLE가 없으므로 L2 같은 규제가 사실상 필수다. 수렴하지 않는 큰 계수는 모델이 "확신"을 배운 것이 아니라 최적화 문제가 ill-posed해진 신호일 수 있다.

## 구현 (Implementation)

```python
import numpy as np

def sigmoid(z):
    z = np.asarray(z)
    return np.where(z >= 0,
                    1 / (1 + np.exp(-z)),
                    np.exp(z) / (1 + np.exp(z)))

def train(X, y, lr=0.1, steps=2000):
    theta = np.zeros(X.shape[1])
    m = len(y)
    for _ in range(steps):
        p = sigmoid(X @ theta)
        grad = X.T @ (p - y) / m       # 로그 손실의 기울기
        theta -= lr * grad
    return theta

X = np.array([[1, 0.5], [1, 1.5], [1, 2.5], [1, 3.5]])
y = np.array([0, 0, 1, 1])
theta = train(X, y)
print((sigmoid(X @ theta) >= 0.5).astype(int))   # [0 0 1 1]
```

평가에서는 확률 품질과 threshold 품질을 분리해서 본다.

```python
proba = sigmoid(X @ theta)
threshold = 0.7
labels = (proba >= threshold).astype(int)
print(proba, labels)
```

## 복잡도 (Complexity)

`m`은 표본 수, `d`는 특징 수, `T`는 반복 횟수다.

| 항목 | 시간 |
|---|---|
| 경사 하강 학습 | `O(T·m·d)` |
| 예측(샘플 1개) | `O(d)` |

닫힌 해가 없어 반복 최적화로 학습한다.

다중 클래스 softmax 회귀는 클래스 수 `k`가 추가되어 한 스텝이 보통 `O(mdk)`가 된다. 이진 문제는 `k=1` logit으로 충분하다.

## 응용 (Applications)

- 스팸 분류, 이탈 예측, 클릭 예측
- 의료 진단(질병 유무 확률)
- 신경망 출력층(소프트맥스는 다중 클래스 일반화)
- 해석 가능한 분류 기준선

## 흔한 오해 (Common Misunderstandings)

- "회귀"라는 이름과 달리 분류 모델이다. 출력은 확률이고, 임계값으로 클래스를 정한다.
- 로지스틱 회귀에 MSE를 쓰면 비볼록이 되어 학습이 불안정하다. 그래서 로그 손실을 쓴다.
- 결정 경계는 입력 공간에서 선형이다. 비선형 경계가 필요하면 특징 변환이나 다른 모델이 필요하다.
- 출력 확률을 잘 보정된 확률로 곧장 믿으면 안 될 때가 있다(보정 별도 필요).
- 정확도만 보면 불균형 데이터에서 성능을 크게 오해할 수 있다. PR-AUC, recall, calibration을 함께 본다.
- 계수가 크다고 feature가 인과적으로 중요하다는 뜻은 아니다. feature scaling과 confounding을 확인해야 한다.

## TMI

- 시그모이드는 통계학의 로지스틱 함수에서 왔고, 인구 성장 모델 등에서 19세기부터 쓰였다.
- 다중 클래스로 확장한 것이 소프트맥스 회귀이며, 거의 모든 분류 신경망의 마지막 층이 사실상 이 구조다.
- $\sigma'(z) = \sigma(z)(1 - \sigma(z))$라는 깔끔한 도함수 덕분에 역전파 계산이 간단하다.

## 연습 / 확인 문제 (Exercises)

- 시그모이드의 도함수가 $\sigma(z)(1-\sigma(z))$임을 유도하라.
- 위 코드의 학습된 `theta`로 결정 경계 $x$ 값을 구하라($\theta^\top x = 0$).
- 로그 손실이 왜 오답에 큰 벌점을 주는지 $\hat{p} \to 0$일 때의 $-\log \hat{p}$로 설명하라.
- 비용이 비대칭인 분류 문제에서 threshold를 0.5가 아닌 값으로 선택하는 절차를 설계하라.
- 완전 선형 분리 데이터에서 규제 없는 로지스틱 회귀 계수가 계속 커지는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [선형 회귀](Linear-Regression.md)
- 다음: [결정 트리](Decision-Trees.md), [규제](Regularization.md)
- 관련: [퍼셉트론과 다층 신경망](../Deep-Learning/MLP.md), [k-최근접 이웃](KNN.md), [SVM](SVM.md)

## 참조 (References)

- [AI/Machine-Learning/Linear-Regression.md](Linear-Regression.md)
- [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
