# 라빈-카프 (Rabin-Karp)

- Level: Intermediate
- Prerequisites: [Algorithms/KMP.md](KMP.md), [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

라빈-카프는 **롤링 해시**로 문자열을 매칭한다. 패턴과 텍스트 윈도우의 해시를 비교해 후보를 빠르게 거르고, 해시가 같을 때만 실제 문자를 확인한다. 윈도우 이동을 상수 시간에 처리하는 것이 핵심.

## 직관 (Intuition)

매번 글자별 비교는 느리다. 부분문자열을 숫자(해시)로 바꾸면 같은지 한 번에 안다. 윈도우가 한 칸 미끄러질 때 해시를 처음부터 다시 계산하지 않고, **나간 문자를 빼고 들어온 문자를 더하는 "롤링"** 으로 $O(1)$ 갱신한다([해시 함수](../Data-Structures/Hash-Function.md)의 다항식 해시).

## 이론 (Theory)

### 1. 다항식 해시와 롤링

문자열을 진법 $b$ 의 수로: 길이 $m$ 윈도우 해시 $h=\big(\sum_{k=0}^{m-1} s_k\,b^{m-1-k}\big)\bmod q$. 한 칸 이동:

$$h'=\big((h - s_{\text{out}}\,b^{m-1})\cdot b + s_{\text{in}}\big)\bmod q$$

### 2. 충돌과 확률

해시 일치는 **후보일 뿐** — 반드시 실제 문자열을 확인한다(해시 충돌 대비). 무작위 소수 $q$ 에서 임의 두 문자열의 충돌 확률 $\approx 1/q$. **이중 해싱**(서로 다른 $q_1,q_2$)이면 충돌 확률 $\approx 1/(q_1q_2)$ 로 사실상 0 → 확인 생략도 가능.

### 3. 적대적 입력

단일 고정 해시는 일부러 충돌을 만드는 anti-hash test에 취약 → **무작위 base/소수**로 방어. 이는 [universal hashing](../Data-Structures/Hash-Function.md)의 응용.

## 구현 (Implementation)

```python
def rabin_karp(text, pat, b=256, q=1_000_000_007):
    n, m = len(text), len(pat)
    if m > n: return []
    hp = ht = 0
    bm = pow(b, m - 1, q)                    # b^(m-1) mod q
    for i in range(m):
        hp = (hp*b + ord(pat[i])) % q
        ht = (ht*b + ord(text[i])) % q
    res = []
    for i in range(n - m + 1):
        if hp == ht and text[i:i+m] == pat:  # 해시 일치 → 실제 확인
            res.append(i)
        if i < n - m:                         # 롤링 갱신
            ht = ((ht - ord(text[i])*bm)*b + ord(text[i+m])) % q
            ht %= q                           # 음수 보정
    return res
```

## 복잡도 (Complexity)

| | 시간 |
|---|---|
| 평균 | $O(n+m)$ |
| 최악(충돌 다발) | $O(nm)$ |

좋은 소수·이중 해시로 최악을 사실상 피한다. **워크드 예제.** `b=10`, `q=13`, 패턴 `35` → $h=(3\cdot10+5)\bmod13=35\bmod13=9$. 텍스트 `1235` 윈도우 `12→ (1\cdot10+2)=12`, 롤링 `23`, `35` → 마지막에 $9$ 일치, 실제 확인 통과.

## 응용 (Applications)

- 다중 패턴/표절 탐지(여러 해시 비교, MOSS류), 문서 핑거프린팅.
- 2D 패턴 매칭(이미지 부분 일치).
- **콘텐츠 정의 청크 분할(CDC)**: Rabin fingerprint로 rsync·백업·dedup의 경계 결정.

## 흔한 오해 (Common Misunderstandings)

- **해시 일치 ≠ 문자열 일치** — 반드시 실제 확인(또는 이중 해시로 확률 통제).
- **모듈러 뺄셈에서 음수** 가능 → `% q` 보정 필요.
- **단일 해시는 적대적 입력에 취약** — 무작위화·이중 해시로 완화.
- **KMP보다 항상 빠르지 않다** — 최악 보장은 KMP가 낫다.

## TMI

- Rabin fingerprint는 rsync·백업의 콘텐츠 정의 청크 분할의 토대 — "어디서 자를지"를 해시가 정한다.
- 이중 해시는 충돌 확률을 곱셈적으로 줄이는 표준 트릭.
- 같은 롤링 해시가 [Z](Z-Algorithm.md)·접미사 구조와 결합해 다양한 문자열 문제(최장 공통 부분문자열 등)를 푼다.

## 연습 / 확인 문제 (Exercises)

- 작은 알파벳에서 롤링 해시 갱신을 손으로 한 칸 수행하라.
- 해시 충돌이 나는 입력을 만들고 실제 확인의 필요성을 보여라.
- 이중 해시가 충돌 확률을 어떻게 줄이는지 계산하라.
- 길이 $k$ 슬라이딩 윈도우로 최장 공통 부분문자열을 이분 + 롤링 해시로 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [Z 알고리즘](Z-Algorithm.md)
- 다음: [Aho-Corasick](Aho-Corasick.md)
- 관련: [서픽스 배열](Suffix-Array.md), [해시 함수](../Data-Structures/Hash-Function.md)

## 참조 (References)

- [Algorithms/KMP.md](KMP.md)
- [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- [Data-Structures/Hash-Function.md](../Data-Structures/Hash-Function.md)
- [Reference/Books.md](../Reference/Books.md)
