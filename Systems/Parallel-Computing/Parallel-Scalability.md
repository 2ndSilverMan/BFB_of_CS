# Amdahl의 법칙과 병렬 확장성 (Parallel Scalability)

- Level: Advanced
- Prerequisites: [Parallel-Models.md](Parallel-Models.md), [Multithreading.md](Multithreading.md), [Engineering/Performance/Benchmarking-Basics.md](../../Engineering/Performance/Benchmarking-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

병렬 확장성은 processor, thread, node를 늘릴 때 성능이 얼마나 좋아지는지를 의미한다. Amdahl의 법칙은 직렬 부분이 남아 있으면 병렬 자원을 아무리 늘려도 speedup에 한계가 있음을 보여준다.

## 직관 (Intuition)

요리를 여러 사람이 도와도 오븐에 굽는 시간처럼 한 명만 처리할 수 있는 단계가 있으면 전체 시간이 그 단계에 묶인다. 병렬화의 핵심은 병렬 부분을 늘리는 것뿐 아니라 직렬 병목과 조정 비용을 줄이는 것이다.

## 이론 (Theory)

프로그램 중 병렬화 가능한 비율을 $p$, processor 수를 $N$이라 하면 Amdahl speedup은

$$
S(N)=\frac{1}{(1-p)+p/N}
$$

이다. $N\to\infty$여도 최대 speedup은 $1/(1-p)$이다.

Gustafson의 법칙은 문제 크기를 함께 키우면 병렬 자원 증가가 더 잘 활용될 수 있음을 강조한다. strong scaling은 같은 문제를 더 많은 자원으로 빨리 푸는 것이고, weak scaling은 자원과 문제 크기를 함께 늘려 시간 유지 여부를 본다.

## 구현 (Implementation)

Amdahl speedup을 계산하면 직렬 병목의 영향을 볼 수 있다.

```python
def amdahl(p, n):
    return 1 / ((1 - p) + p / n)


for n in [1, 2, 4, 8, 16, 64]:
    print(n, round(amdahl(0.9, n), 2))
```

실제 측정에서는 thread 수, 입력 크기, warmup, pinning, NUMA, I/O 영향을 통제해야 한다.

## 복잡도 (Complexity)

병렬화는 이론적 작업량을 줄이기보다 wall-clock 시간을 줄인다. 하지만 synchronization, communication, load imbalance, cache coherence overhead가 늘면 speedup이 sublinear가 되거나 성능이 악화될 수 있다.

## 응용 (Applications)

- 병렬 알고리즘 성능 예측
- thread/node 수 튜닝
- HPC benchmark 분석
- GPU/분산 학습 scalability 평가

## 흔한 오해 (Common Misunderstandings)

- 코어 수를 두 배로 늘리면 항상 두 배 빨라지는 것은 아니다.
- 평균 CPU 사용률이 높아도 load imbalance가 있으면 느릴 수 있다.
- strong scaling과 weak scaling을 혼동하면 benchmark 해석이 틀어진다.
- 병렬화보다 알고리즘 개선이 더 큰 효과를 낼 때가 많다.

## TMI

- superlinear speedup은 cache 효과나 작업량 변화 때문에 가끔 관찰될 수 있다.
- 병렬 효율은 speedup을 processor 수로 나눈 값이다.
- 분산 시스템에서는 네트워크 tail latency가 전체 job 완료 시간을 지배할 수 있다.

## 연습 / 확인 문제 (Exercises)

- 병렬화 가능 비율이 95%일 때 Amdahl 최대 speedup을 계산하라.
- strong scaling과 weak scaling의 차이를 예로 설명하라.
- 병렬 프로그램에서 load imbalance를 진단하는 방법을 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [OpenMP / MPI](OpenMP-MPI.md)
- 다음: [Engineering/Performance/](../../Engineering/Performance/)

## 참조 (References)

- [Parallel-Models.md](Parallel-Models.md)
- [Multithreading.md](Multithreading.md)
- [Engineering/Performance/Benchmarking-Basics.md](../../Engineering/Performance/Benchmarking-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
