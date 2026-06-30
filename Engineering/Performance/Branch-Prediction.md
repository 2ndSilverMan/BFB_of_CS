# 분기 예측과 파이프라인 (Branch Prediction)

- Level: Advanced
- Prerequisites: [Systems/Computer-Architecture/Pipelining.md](../../Systems/Computer-Architecture/Pipelining.md), [Engineering/Performance/Cache-Friendly-Code.md](Cache-Friendly-Code.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

분기 예측은 CPU가 조건문의 결과를 미리 추측해 pipeline을 계속 채우는 기술이다. 예측 실패는 pipeline flush와 stall을 만든다.

## 직관 (Intuition)

CPU는 길을 걷기 전에 갈림길을 맞힌다. 갈림길이 규칙적이면 빠르고, 무작위면 되돌아오는 비용이 커진다.

## 이론 (Theory)

Modern CPU는 branch history와 pattern table로 taken/not-taken을 예측한다. Data-dependent branch가 random하면 miss rate가 올라간다. 조건문을 없애는 branchless programming, data sorting, lookup table, vectorization이 도움이 될 수 있지만, 불필요한 branchless 코드는 readability와 compiler optimization을 해칠 수 있다.

### 예측 가능성과 데이터 분포

분기 예측 실패는 pipeline flush를 만들 수 있다. 정렬된 데이터나 편향된 조건은 예측이 쉽고, 랜덤한 조건은 어렵다. 따라서 같은 코드도 입력 분포에 따라 성능이 달라진다.

Branchless code는 항상 빠른 것이 아니다. 불필요한 연산이 늘거나 readability가 떨어질 수 있다. 예측 실패가 실제 병목인지 profile counter로 확인한 뒤 적용한다.

## 구현 (Implementation)

```python
def count_positive(values):
    count = 0
    for x in values:
        if x > 0:
            count += 1
    return count
```

입력이 정렬되어 있으면 branch pattern이 단순해지고, 무작위로 섞이면 예측 실패가 늘 수 있다. 실제 영향은 profiler와 hardware counter로 확인한다.

## 복잡도 (Complexity)

Big-O는 그대로여도 branch miss penalty 때문에 상수 비용이 크게 달라진다. 특히 tight loop에서 차이가 두드러진다.

## 응용 (Applications)

- parser·filter loop 최적화
- packet processing
- compression·encoding
- high-frequency trading·game loop

## 흔한 오해 (Common Misunderstandings)

- 모든 `if`가 느린 것은 아니다.
- compiler가 이미 branch를 없애거나 재배치할 수 있다.
- branchless code가 항상 빠른 것은 아니다.
- 예측 실패 비용은 CPU 세대와 workload에 따라 다르다.

## TMI

- Spectre류 취약점은 speculative execution과 branch prediction을 악용했다.
- `perf stat` 같은 도구로 branch misses를 볼 수 있다.
- Data layout을 바꾸는 것이 조건문을 손대는 것보다 큰 효과를 낼 때가 있다.

## 연습 / 확인 문제 (Exercises)

- 정렬된 입력과 무작위 입력에서 같은 loop를 benchmark하라.
- branch miss와 cache miss를 구분해 해석하라.
- branchless 버전이 더 느려지는 사례를 찾아라.

## 이어서 읽기 (Reading Path)

- 이전: [캐시 친화적 코드](Cache-Friendly-Code.md)
- 다음: [SIMD / 벡터화](SIMD-Vectorization.md)

## 참조 (References)

- [Systems/Computer-Architecture/Pipelining.md](../../Systems/Computer-Architecture/Pipelining.md)
- [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
