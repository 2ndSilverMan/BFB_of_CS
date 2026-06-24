# 텍스트 전처리 (Text Preprocessing)

- Level: Beginner
- Prerequisites: [Programming/Arrays-and-Strings.md](../../Programming/Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

text preprocessing은 raw 텍스트를 모델이 다룰 수 있는 토큰(token)과 숫자 표현으로 바꾸는 단계다. 정규화(normalization), 토크나이제이션(tokenization), 어휘(vocabulary) 구성, 정수 인코딩으로 이어진다.

## 직관 (Intuition)

모델은 글자 그대로의 문자열이 아니라 정수 ID 열을 입력으로 받는다. 그런데 "Apple", "apple", "apples"를 전혀 다른 것으로 취급하면 데이터가 쪼개지고, 반대로 너무 뭉뚱그리면 의미가 사라진다. 전처리는 이 "쪼개기 단위"와 "같게 볼 것"을 정해, 어휘 크기와 의미 보존 사이의 균형을 잡는 일이다.

## 이론 (Theory)

대표적 토크나이제이션 방식:

- **word 단위**: 공백·구두점 기준. 단순하지만 OOV(out-of-vocabulary)와 어휘 폭증 문제가 크다.
- **character 단위**: 어휘는 작지만 sequence가 길고 의미 단위가 약하다.
- **subword 단위**: BPE, WordPiece, Unigram LM. 자주 쓰는 조각은 통째로, 드문 단어는 조각으로 쪼개 OOV를 없애고 어휘를 적정 크기로 유지한다.

BPE(byte pair encoding)는 가장 빈번한 인접 토큰 쌍을 반복적으로 병합해 어휘를 키운다. 빈도 $f$가 높은 쌍부터 합치므로, 자주 등장하는 형태소·접사가 자연스럽게 하나의 토큰이 된다. 이후 각 토큰을 정수 ID로 매핑하고, 배치 처리를 위해 길이를 padding/truncation으로 맞춘다.

## 구현 (Implementation)

```python
def bpe_merges(corpus_tokens, num_merges):
    vocab = list_initial_symbols(corpus_tokens)   # 문자 단위 시작
    for _ in range(num_merges):
        pair = most_frequent_adjacent_pair(corpus_tokens)
        if pair is None:
            break
        corpus_tokens = merge_pair(corpus_tokens, pair)  # 가장 빈번한 쌍 병합
        vocab.append("".join(pair))
    return vocab
```

## 복잡도 (Complexity)

토크나이제이션 자체는 입력 길이에 선형(`O(n)`)에 가깝다. BPE 어휘 학습은 병합 횟수와 코퍼스 크기에 따라 비용이 늘지만 보통 한 번만 수행해 캐싱한다. 어휘 크기는 임베딩 행렬과 softmax 비용에 직접 영향을 준다.

## 응용 (Applications)

- 모든 NLP·LLM 파이프라인의 입력 단계
- 다국어 모델의 공통 subword 어휘 구성
- 코드·DNA 등 비자연어 sequence 토크나이제이션
- 검색 인덱싱에서의 정규화·표제어 추출

## 흔한 오해 (Common Misunderstandings)

- 토큰 = 단어가 아니다. subword 모델에서는 한 단어가 여러 토큰일 수 있다.
- 무조건적인 소문자화·불용어 제거가 항상 좋은 것은 아니다. 과제에 따라 정보를 잃는다.
- subword가 OOV를 "제거"하지만, 희귀어가 많은 토큰으로 쪼개져 sequence가 길어지는 비용이 있다.
- 토큰 수와 글자 수는 다르며, LLM 과금·context 한도는 보통 토큰 기준이다.

## TMI

- 영어에서 토큰 1개는 평균적으로 약 4글자 정도에 대응한다는 경험칙이 자주 인용된다.
- BPE는 원래 1994년 데이터 압축 알고리즘이었는데, 2016년 NMT에서 subword 토크나이제이션으로 재발견됐다.
- byte-level BPE는 유니코드 대신 바이트를 단위로 삼아 어떤 문자열도 OOV 없이 처리한다(GPT-2 계열).

## 연습 / 확인 문제 (Exercises)

- 작은 코퍼스에서 BPE 병합을 3회 손으로 수행해 어휘를 구하라.
- word 토크나이저와 subword 토크나이저의 OOV 처리 차이를 예시로 설명하라.
- 같은 문장에서 character/word/subword 토큰 수를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI/NLP/](README.md)
- 다음: [언어 모델 기초](Language-Model-Basics.md), [단어 임베딩](Word-Embeddings.md)

## 참조 (References)

- [AI/NLP/Language-Model-Basics.md](Language-Model-Basics.md)
- [AI/NLP/Word-Embeddings.md](Word-Embeddings.md)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Books.md](../../Reference/Books.md)
