# 텍스트 분류 (Text Classification)

- Level: Intermediate
- Prerequisites: [Text-Preprocessing.md](Text-Preprocessing.md), [Word-Embeddings.md](Word-Embeddings.md), [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

텍스트 분류는 문서, 문장, 댓글 같은 텍스트에 하나 이상의 라벨을 부여하는 NLP 작업이다. 감성 분석, 스팸 탐지, 주제 분류, 의도 분류가 대표 예다.

## 직관 (Intuition)

문장을 읽고 “긍정/부정”, “배송 문의/환불 문의”, “스포츠/정치/기술” 같은 카테고리를 붙이는 작업이다. 모델은 단어, 구문, 문맥에서 라벨을 예측하는 단서를 찾는다.

## 이론 (Theory)

텍스트 분류 파이프라인은 보통 다음 단계로 구성된다.

1. 텍스트 정제와 토크나이징
2. 표현 생성: bag-of-words, TF-IDF, embedding, transformer representation
3. 분류기 학습: logistic regression, SVM, CNN/RNN, BERT fine-tuning
4. 평가: accuracy, precision, recall, F1, AUROC

다중 클래스와 다중 라벨 문제를 구분해야 한다. 클래스 불균형이 있으면 accuracy만으로 평가하면 위험하다.

## 구현 (Implementation)

간단한 bag-of-words feature는 단어 count로 만들 수 있다.

```python
from collections import Counter


def bow(text):
    return Counter(text.lower().split())


print(bow("great product great price"))
```

실무에서는 train/validation/test split, label leakage, 중복 문서 제거가 중요하다.

## 복잡도 (Complexity)

BoW+선형 모델은 빠르고 해석하기 쉽다. Transformer fine-tuning은 성능이 높을 수 있지만 토큰 길이와 모델 크기에 따라 학습/추론 비용이 크다.

## 응용 (Applications)

- 감성 분석
- 스팸/악성 댓글 탐지
- 고객 문의 의도 분류
- 문서 라우팅과 태깅

## 흔한 오해 (Common Misunderstandings)

- 정확도가 높아도 소수 클래스 recall이 낮을 수 있다.
- 전처리를 test set에 맞춰 조정하면 leakage가 생긴다.
- 긴 문서를 단순 truncation하면 중요한 근거를 잃을 수 있다.
- 라벨 정의가 모호하면 모델 성능보다 데이터 품질이 병목이 된다.

## TMI

- 전통적인 TF-IDF+linear SVM은 여전히 강한 baseline이다.
- Calibration이 필요한 의사결정 시스템에서는 확률 보정도 중요하다.
- Active learning은 라벨링 비용이 큰 텍스트 분류에서 유용할 수 있다.

## 연습 / 확인 문제 (Exercises)

- 다중 클래스와 다중 라벨 분류의 차이를 설명하라.
- 클래스 불균형에서 F1을 보는 이유를 말하라.
- 텍스트 분류에서 leakage가 생길 수 있는 사례를 하나 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [Transformer for NLP](Transformer-NLP.md)
- 다음: [개체명 인식](NER.md)

## 참조 (References)

- [Text-Preprocessing.md](Text-Preprocessing.md)
- [Word-Embeddings.md](Word-Embeddings.md)
- [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- [Reference/Books.md](../../Reference/Books.md)
