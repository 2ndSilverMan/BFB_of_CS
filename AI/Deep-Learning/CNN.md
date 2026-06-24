# 합성곱 신경망 (Convolutional Neural Networks)

- Level: Intermediate
- Prerequisites: [AI/Deep-Learning/Backpropagation.md](Backpropagation.md), [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

CNN은 작은 kernel을 공간 위치마다 공유해 local pattern을 추출하는 신경망이다. locality와 weight sharing으로 이미지 같은 grid 데이터에서 MLP보다 적은 파라미터로 translation-aware feature를 학습한다.

## 직관 (Intuition)

같은 edge detector를 이미지 모든 위치에 밀어 보며 어디에 경계가 있는지 찾는다. 앞 층은 선·모서리, 뒤 층은 질감·부분·객체처럼 더 넓은 receptive field의 표현을 조합한다.

## 이론 (Theory)

2차원 cross-correlation 형태는

$$Y_{i,j,o}=\sum_{u,v,c}K_{u,v,c,o}X_{i+u,j+v,c}$$

다. kernel $K$, stride, padding, dilation이 출력 크기와 receptive field를 정한다. 입력 크기 $H$, kernel $K$, padding $P$, stride $S$이면 한 축 출력은

$$\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1$$

이다. pooling이나 strided convolution은 해상도를 줄인다.

## 구현 (Implementation)

```python
def conv1d(signal, kernel):
    width = len(signal) - len(kernel) + 1
    return [sum(signal[i + j] * kernel[j] for j in range(len(kernel)))
            for i in range(width)]


print(conv1d([1, 2, 3, 4], [1, -1]))
```

실전에서는 tensor library의 검증·최적화된 convolution을 사용한다.

## 복잡도 (Complexity)

출력 $H_oW_o$, kernel $K_hK_w$, 입출력 channel $C_i,C_o$에 대해 직접 convolution은 `O(H_oW_oK_hK_wC_iC_o)`다. 파라미터는 `O(K_hK_wC_iC_o)`다.

## 응용 (Applications)

- 이미지 분류·검출·분할
- 음성 spectrogram과 시계열
- 의료영상·위성영상
- 다른 모델의 visual backbone

## 흔한 오해 (Common Misunderstandings)

- CNN이 완전한 translation invariance를 자동 보장하지 않는다.
- padding 방식은 경계 feature에 영향을 준다.
- channel 수와 공간 크기를 혼동하면 tensor shape 오류가 난다.
- convolution이라는 이름이지만 라이브러리는 kernel을 뒤집지 않는 cross-correlation을 자주 구현한다.

## TMI

- 1x1 convolution은 공간 이웃 대신 channel을 섞는다.
- depthwise separable convolution은 공간·channel 혼합을 분리해 계산을 줄인다.
- dilated convolution은 파라미터를 크게 늘리지 않고 receptive field를 넓힌다.

## 연습 / 확인 문제 (Exercises)

- 주어진 입력·kernel·stride의 출력 크기를 계산하라.
- edge kernel로 작은 행렬을 직접 convolution하라.
- standard와 depthwise separable convolution의 파라미터 수를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [드롭아웃](Dropout.md)
- 다음: [어텐션](Attention.md)

## 참조 (References)

- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
