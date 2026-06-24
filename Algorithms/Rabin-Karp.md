# 라빈-카프 (Rabin-Karp)

- Level: Intermediate
- Prerequisites: [Algorithms/KMP.md](KMP.md), [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

라빈-카프는 해시를 이용한 문자열 매칭 알고리즘이다. 패턴과 텍스트 부분문자열의 해시를 비교해 후보를 빠르게 거르고, 해시가 같을 때만 실제 문자를 확인한다. 롤링 해시로 윈도우 이동을 상수 시간에 처리한다.

## 직관 (Intuition)

문자열을 매번 글자별로 비교하면 느리다. 대신 각 부분문자열을 숫자(해시)로 바꿔 비교하면 한 번에 같은지 다른지 알 수 있다. 윈도우가 한 칸 미끄러질 때 해시를 처음부터 다시 계산하지 않고, 나간 문자를 빼고 들어온 문자를 더하는 "롤링"으로 갱신하는 것이 핵심이다.

## 이론 (Theory)

문자열을 진법 $b$의 수로 본다. 길이 $m$ 윈도우의 해시:

$$h=\Big(\sum_{k=0}^{m-1} s_k\, b^{m-1-k}\Big)\bmod q$$

한 칸 이동 시 롤링 갱신:

$$h'=\big((h - s_{\text{out}}\,b^{m-1})\cdot b + s_{\text{in}}\big)\bmod q$$

해시가 일치하면 실제 문자열을 확인한다(해시 충돌 대비). 큰 소수 $q$와 무작위 $b$로 충돌 확률을 낮춘다. 두 개의 해시(double hashing)를 쓰면 충돌이 사실상 무시할 수준이 된다.

## 구현 (Implementation)

```python
def rabin_karp(text, pat, b=256, q=1_000_000_007):
    n, m = len(text), len(pat)
    if m > n: return []
    hp = ht = 0; h = pow(b, m-1, q); res = []
    for i in range(m):
        hp = (hp*b + ord(pat[i])) % q
        ht = (ht*b + ord(text[i])) % q
    for i in range(n - m + 1):
        if hp == ht and text[i:i+m] == pat:   # 해시 일치 → 실제 확인
            res.append(i)
        if i < n - m:
            ht = ((ht - ord(text[i])*h)*b + ord(text[i+m])) % q
            ht %= q                            # 롤링 갱신
    return res
```

## 복잡도 (Complexity)

| | 시간 |
|---|---|
| 평균 | `O(n + m)` |
| 최악(충돌 다발) | `O(n·m)` |

평균적으로 선형이지만, 해시 충돌이 잦으면 매번 확인 비용이 들어 최악 `O(nm)`이다. 좋은 소수·이중 해시로 최악을 사실상 피한다.

## 응용 (Applications)

- 다중 패턴/표절 탐지(여러 해시 비교)
- 2D 패턴 매칭(이미지 부분 일치)
- 중복 부분문자열·문서 핑거프린팅
- Rabin fingerprint 기반 청크 분할(rsync, dedup)

## 흔한 오해 (Common Misunderstandings)

- 해시 일치가 곧 문자열 일치는 아니다 — 반드시 실제 확인이 필요하다.
- 모듈러를 빼는 갱신에서 음수가 날 수 있어 `% q` 보정이 필요하다.
- 단일 해시는 적대적 입력에 취약하다(해시 충돌 공격) — 무작위화·이중 해시로 완화.
- KMP보다 항상 빠르지 않다. 최악 보장은 KMP가 낫다.

## TMI

- Rabin fingerprint는 rsync·백업 시스템의 콘텐츠 정의 청크 분할의 토대다.
- 이중 해시(서로 다른 소수 두 개)는 충돌 확률을 곱셈적으로 줄이는 표준 트릭이다.
- 같은 롤링 해시 아이디어가 표절 탐지(MOSS류)와 중복 제거에 폭넓게 쓰인다.

## 연습 / 확인 문제 (Exercises)

- 작은 알파벳에서 롤링 해시 갱신을 손으로 한 칸 수행하라.
- 해시 충돌이 발생하는 입력을 만들고 실제 확인의 필요성을 보여라.
- 이중 해시가 충돌 확률을 어떻게 줄이는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Z 알고리즘](Z-Algorithm.md)
- 다음: [Aho-Corasick](Aho-Corasick.md), [서픽스 배열](Suffix-Array.md)

## 참조 (References)

- [Algorithms/KMP.md](KMP.md)
- [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- [Reference/Books.md](../Reference/Books.md)
