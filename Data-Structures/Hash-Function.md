# 해시 함수 (Hash Function)

- Level: Intermediate
- Prerequisites: [Data-Structures/Hash-Table.md](Hash-Table.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

해시 함수는 **임의 크기 입력(키)을 고정 크기 정수(해시값)로** 대응시킨다. [해시 테이블](Hash-Table.md)은 이 정수를 버킷 인덱스로 줄여 위치를 정한다. 좋은 해시는 입력을 출력 공간 전체에 **고르고 예측 불가능하게** 흩뿌려 충돌을 최소화하고 평균 $O(1)$ 접근을 가능케 한다.

## 직관 (Intuition)

키를 잘게 섞어 "지문" 하나로 압축하는 믹서. 비슷한 키(`key1`, `key2`)도 결과가 완전히 달라야 고루 퍼지고, 같은 키는 언제나 같은 값이어야(결정적) 다시 찾는다. **"고르게 + 결정적 + 빠르게"** 가 핵심 긴장이고, 여기에 **"적대자가 충돌을 못 만들게"** 가 더해진다.

## 이론 (Theory)

### 1. 좋은 해시의 성질

| 성질 | 의미 |
|---|---|
| 결정성 | 같은 입력 → 항상 같은 출력 |
| 균등 분포 | 출력이 범위에 고르게 |
| 효율성 | 빠른 계산 |
| 눈사태(avalanche) | 입력 1비트가 출력의 ~절반 비트를 뒤집음 |

### 2. 범위 축소: division vs multiplication vs Fibonacci

해시값 $h$ 를 버킷 수 $m$ 으로 줄이기:

- **나눗셈법** $h \bmod m$: $m$ 을 소수로 두면 패턴 키의 편향을 줄임.
- **곱셈법** $\lfloor m\,(hA \bmod 1)\rfloor$ ($0<A<1$): $m$ 이 2의 거듭제곱이어도 잘 동작.
- **Fibonacci 해싱**: $A=1/\varphi$ ($\varphi$ 황금비)로 두면 분포가 특히 좋다.

### 3. universal hashing — 적대자를 이기는 보장

고정된 해시는 **그 함수에 맞춰 일부러 충돌시키는 입력**(anti-hash test, HashDoS)에 무력하다. **universal hashing**(Carter–Wegman)은 해시를 **함수족에서 무작위로** 골라, *어떤 입력이든* 두 키가 충돌할 확률을 $\le 1/m$ 로 보장한다 → 적대적 입력에서도 기대 $O(1)$. 실무는 실행마다 시드를 섞는 **해시 무작위화**나 키 기반 **SipHash**로 이를 구현한다.

### 4. 다항식 롤링 해시

문자열 $s$ 를 $h=\sum s_i\,b^{\,|s|-1-i} \bmod p$ 로 보는 다항식 해시는 **부분 문자열 해시를 $O(1)$ 에 갱신**(슬라이딩)할 수 있어 [라빈-카프](../Algorithms/Rabin-Karp.md) 문자열 매칭의 핵심이다. 단일 모듈러는 충돌 공격에 약해 **이중 해싱**(서로 다른 $b, p$ 두 벌)을 흔히 쓴다.

> **해시 테이블용 해시 ≠ 암호학적 해시(SHA-256).** 후자는 충돌 저항·역상 저항 같은 보안 성질을 추가로 요구하고 훨씬 느리다 → [암호학적 해시 함수](../Engineering/Security/Hash-Functions.md).

## 구현 (Implementation)

```python
def poly_hash(s, base=131, mod=(1 << 61) - 1):   # Mersenne 소수 mod
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod            # 자리값을 base로 가중
    return h

print(poly_hash("apple") == poly_hash("apple"))   # True (결정적)
print(poly_hash("ab") != poly_hash("ba"))         # True (순서 구분)

def fib_index(key, bits):                          # Fibonacci 해싱 (m = 2**bits)
    A = 0x9E3779B97F4A7C15                          # 2^64 / φ
    return ((hash(key) * A) & ((1 << 64) - 1)) >> (64 - bits)
```

## 복잡도 (Complexity)

`L`=키 길이.

| 항목 | 비용 |
|---|---|
| 길이 `L` 키 해시 계산 | $O(L)$ |
| 해시값 → 버킷 변환 | $O(1)$ |
| 다항식 해시 슬라이딩 갱신 | $O(1)$/스텝 |

해시 테이블의 "평균 $O(1)$" 은 보통 키 길이를 상수로 보고 해시를 한 번 계산한다는 가정 위에 있다.

## 응용 (Applications)

- 해시 테이블(`dict`/`set`)의 인덱스 계산.
- [라빈-카프](../Algorithms/Rabin-Karp.md) 문자열 매칭, 중복 문서·표절 탐지.
- **일관 해싱(consistent hashing)**: 가상 노드를 둔 해시 링으로 서버 추가/제거 시 재배치를 최소화 → 분산 캐시·샤딩.
- LSH(MinHash/SimHash): 유사도 보존 해시로 근접 중복 검색.

## 흔한 오해 (Common Misunderstandings)

- **해시는 압축 저장 도구가 아니다** — 비가역이고 충돌 때문에 일대일도 아니다.
- **테이블용 해시와 암호학적 해시 혼동 금지** — 빠른 일반 해시를 비밀번호 저장에 쓰면 취약(전용 KDF 필요).
- **"충돌 없는 해시"는 입력 공간이 더 크면 불가능** — 목표는 충돌 제거가 아니라 균등 분포.
- **`hash()` 결과를 그대로 인덱스로 쓰면 안 된다** — 음수일 수 있고 범위도 안 맞아 `% m` 등 사상 필요.

## TMI

- Python은 3.3부터 문자열/바이트 해시에 무작위 시드를 기본 적용(`PYTHONHASHSEED`) — 실행마다 `hash("x")` 가 달라지는 HashDoS 방어책이다.
- **완전 해시(perfect hashing)** 는 미리 아는 고정 키 집합에 충돌이 0이도록 설계한 해시 — 컴파일러 예약어 인식 등에 쓰인다.
- 일관 해싱은 2007년 Amazon Dynamo 논문으로 분산 시스템의 표준 기법이 됐다(memcached, Cassandra).
- `0x9E3779B9`(32비트 황금비 상수)는 해시·PRNG·xxHash 등 곳곳에 등장하는 "마법수"다.

## 연습 / 확인 문제 (Exercises)

- `poly_hash`의 `base=1`이면 어떤 키들이 충돌하는지 설명하라(힌트: 애너그램).
- 한 글자만 바꾼 두 문자열의 해시값 차이를 측정해 눈사태 효과를 확인하라.
- 다항식 해시로 길이 k 슬라이딩 윈도우 해시를 $O(1)$ 갱신으로 구현하라(라빈-카프).
- universal hashing이 왜 적대적 입력에서도 기대 $O(1)$ 을 보장하는지 충돌 확률 $\le 1/m$ 로 논증하라.

## 이어서 읽기 (Reading Path)

- 이전: [해시 테이블](Hash-Table.md)
- 다음: [암호학적 해시 함수](../Engineering/Security/Hash-Functions.md)
- 관련: [라빈-카프](../Algorithms/Rabin-Karp.md), [배열](Array.md)

## 참조 (References)

- [Data-Structures/Hash-Table.md](Hash-Table.md)
- [Engineering/Security/Hash-Functions.md](../Engineering/Security/Hash-Functions.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
