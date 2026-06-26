# 해시 함수 (Hash Function)

- Level: Intermediate
- Prerequisites: [Data-Structures/Hash-Table.md](Hash-Table.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

해시 함수는 **임의 크기의 입력(키)을 고정 크기의 정수(해시값)로 대응**시키는 함수다. 해시 테이블에서는 이 정수를 버킷 인덱스로 변환해 데이터를 어디에 둘지 정한다. 좋은 해시 함수는 입력을 출력 공간 전체에 **고르고 예측 불가능하게** 흩뿌려, 충돌을 최소화하고 평균 `O(1)` 접근을 가능하게 한다.

## 직관 (Intuition)

해시 함수는 키를 잘게 섞어 "지문" 하나로 압축하는 믹서다. 비슷한 키(`"key1"`, `"key2"`)라도 결과가 완전히 달라야 버킷에 골고루 퍼진다. 반대로 같은 키는 언제나 같은 값을 내야(결정적, deterministic) 나중에 다시 찾을 수 있다. "고르게 + 결정적으로 + 빠르게"가 설계의 핵심 긴장 관계다.

## 이론 (Theory)

좋은 해시 함수가 갖춰야 할 성질은 다음과 같다.

| 성질 | 의미 |
|---|---|
| 결정성(deterministic) | 같은 입력은 항상 같은 출력 |
| 균등 분포(uniformity) | 출력이 가능한 범위에 고르게 퍼짐 |
| 효율성(efficiency) | 빠르게 계산됨 |
| 눈사태 효과(avalanche) | 입력 1비트만 바뀌어도 출력의 약 절반 비트가 바뀜 |

해시값 $h$를 버킷 수 $m$ 범위로 줄이는 두 대표 기법이다.

- **나눗셈법(division)**: $h \bmod m$. $m$을 소수로 두면 패턴이 있는 키의 편향을 줄인다.
- **곱셈법(multiplication)**: $\lfloor m \cdot (h \cdot A \bmod 1) \rfloor$ ($0 < A < 1$). $m$이 2의 거듭제곱이어도 잘 동작한다.

충돌은 비둘기집 원리상 피할 수 없다(키 공간 > 버킷 수). 충돌 처리 전략은 [해시 테이블](Hash-Table.md)에서 다룬 체이닝과 개방 주소법으로 나뉜다. 또한 적대적 입력이 일부러 충돌을 유발하는 것(HashDoS)을 막기 위해, 실무 라이브러리는 실행마다 무작위 시드를 섞는 **해시 무작위화**나 SipHash 같은 키 기반 해시를 쓴다.

> 주의: 해시 테이블용 해시와 **암호학적 해시(SHA-256 등)** 는 목표가 다르다. 후자는 충돌·역상 저항성 같은 보안 성질을 추가로 요구한다.

## 구현 (Implementation)

문자열용 다항식 롤링 해시(polynomial hash)의 최소 형태다.

```python
def poly_hash(s, base=131, mod=(1 << 61) - 1):
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod   # 자리값을 base로 가중
    return h


print(poly_hash("apple"))
print(poly_hash("apple") == poly_hash("apple"))   # True (결정적)
print(poly_hash("ab") != poly_hash("ba"))         # True (순서 구분)
```

버킷 인덱스로 줄일 때는 나눗셈법을 쓴다.

```python
def bucket_index(key, num_buckets):
    return poly_hash(key) % num_buckets
```

## 복잡도 (Complexity)

`L`은 키의 길이(바이트/문자 수)다.

| 항목 | 비용 |
|---|---|
| 길이 `L` 키의 해시 계산 | `O(L)` |
| 해시값 → 버킷 변환 | `O(1)` |

해시 테이블 연산이 "평균 `O(1)`"이라 할 때, 이는 보통 키 길이를 상수로 보고 해시 계산을 한 번 한다는 가정 위에 있다.

## 응용 (Applications)

- 해시 테이블(`dict`, `set`)의 인덱스 계산
- 문자열 매칭(라빈-카프), 중복 문서 탐지
- 부하 분산: 일관 해싱(consistent hashing)으로 키를 서버에 분배
- 무결성 확인·식별자 생성(암호학적 해시 영역)

## 흔한 오해 (Common Misunderstandings)

- 해시 함수는 데이터를 **압축 저장**하는 도구가 아니다. 원본을 복원할 수 없으며(일반적으로 비가역), 충돌 때문에 일대일도 아니다.
- 해시 테이블용 해시와 암호학적 해시를 혼동하면 안 된다. 빠른 일반 해시를 비밀번호 저장에 쓰면 보안에 취약하다.
- "충돌이 없는 해시 함수"는 입력 공간이 출력보다 크면 불가능하다. 목표는 충돌 제거가 아니라 균등 분포다.
- `hash()` 결과를 그대로 버킷 인덱스로 쓰면 안 된다. 음수일 수 있고 범위도 맞지 않으므로 `% m` 등으로 사상해야 한다.

## TMI

- Python은 3.3부터 문자열·바이트 해시에 무작위 시드를 기본 적용한다(`PYTHONHASHSEED`). 그래서 실행을 새로 할 때마다 `hash("x")` 값이 달라진다. 이는 HashDoS 방어책이다.
- 완전 해시(perfect hashing)는 미리 알려진 고정 키 집합에 대해 충돌이 전혀 없도록 설계한 해시로, 컴파일러의 예약어 인식 등에 쓰인다.
- 일관 해싱은 서버 추가·제거 시 재배치되는 키를 최소화해, 분산 캐시(memcached)·데이터베이스 샤딩의 표준 기법이 됐다.

## 연습 / 확인 문제 (Exercises)

- 위 `poly_hash`에서 `base`를 1로 두면 어떤 키들이 충돌하는지 설명하라.
- 같은 길이의 두 문자열에 대해 한 글자만 바꿨을 때 해시값이 얼마나 달라지는지 측정해 눈사태 효과를 확인하라.
- 정수 키에 대한 곱셈법 해시를 구현하고, 나눗셈법과 분포를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [해시 테이블](Hash-Table.md)
- 다음: [암호학적 해시 함수](../Engineering/Security/Hash-Functions.md)
- 관련: [배열](Array.md)

## 참조 (References)

- [Data-Structures/Hash-Table.md](Hash-Table.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
