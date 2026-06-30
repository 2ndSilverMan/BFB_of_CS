# C++ STL

- Level: Intermediate
- Prerequisites: [C++ 클래스와 템플릿](Cpp-Classes-and-Templates.md), [Data-Structures/](../../../Data-Structures/)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

STL은 **컨테이너 · 반복자(iterator) · 알고리즘 · 함수 객체**를 템플릿으로 조합하는 C++ 표준 라이브러리다. 설계 철학은 "**알고리즘이 컨테이너가 아니라 iterator 범위에 동작**"해, 자료구조와 알고리즘을 직교적으로 결합하는 것이다.

## 직관 (Intuition)

`vector` 에 담고, iterator로 범위를 가리키고, `sort` 같은 알고리즘을 적용한다. 직접 루프를 쓰기보다 **검증된 표준 도구를 조합**한다. 컨테이너마다 내부 표현·복잡도·iterator 무효화 규칙이 다르다는 것만 알면 예측 가능해진다.

## 핵심 문법 (Core Syntax)

```cpp
#include <algorithm>
#include <vector>
std::vector<int> xs = {3, 1, 4, 2};
std::sort(xs.begin(), xs.end());           // 알고리즘은 iterator 범위에
for (int x : xs) std::cout << x << " ";    // range-based for
```

## 이론 (Theory)

### 1. 컨테이너 = 자료구조

| 컨테이너 | 내부 | 접근/검색 |
|---|---|---|
| `vector` | [동적 배열](../../../Data-Structures/Array.md) | 인덱스 $O(1)$, 검색 $O(n)$ |
| `deque` | 블록 배열 | 양 끝 $O(1)$ |
| `list` | [이중 연결 리스트](../../../Data-Structures/Linked-List.md) | 핸들 삽입 $O(1)$, 접근 $O(n)$ |
| `map`/`set` | [레드-블랙 트리](../../../Data-Structures/Red-Black-Tree.md) | $O(\log n)$, 정렬 순회 |
| `unordered_map` | [해시 테이블](../../../Data-Structures/Hash-Table.md) | 평균 $O(1)$, 최악 $O(n)$ |

### 2. iterator 카테고리와 무효화

iterator는 input/forward/bidirectional/random-access 카테고리가 있고, 알고리즘은 요구 카테고리가 다르다(`sort` 는 random-access). **iterator 무효화**: `vector` 재할당은 모든 iterator를, `map`/`list` 삭제는 그 원소만 무효화 — 모르면 미묘한 UB.

### 3. 알고리즘 + 함수 객체

`<algorithm>` 함수는 범위 + 술어(람다)를 받는다. C++20 **ranges** 는 `xs | views::filter(...) | views::transform(...)` 처럼 합성을 표현력 있게 만든다.

## 구현 (Implementation)

```cpp
#include <algorithm>
#include <map>
#include <vector>
std::vector<std::string> words = {"a","b","a","c","b","a"};
std::map<std::string,int> freq;
for (const auto& w : words) freq[w]++;                 // 빈도 집계
auto top = std::max_element(freq.begin(), freq.end(),  // 람다 비교자
    [](const auto& l, const auto& r){ return l.second < r.second; });
// top->first == "a", top->second == 3

std::vector<int> v = {3,1,4,1,5};
std::sort(v.begin(), v.end());
v.erase(std::unique(v.begin(), v.end()), v.end());     // 정렬 후 중복 제거 관용구
```

## 복잡도 (Complexity)

| 연산 | vector | map | unordered_map |
|---|---|---|---|
| 검색 | $O(n)$ | $O(\log n)$ | 평균 $O(1)$ |
| 삽입 | 끝 amortized $O(1)$ | $O(\log n)$ | 평균 $O(1)$ |
| 정렬 순회 | 정렬 필요 | 자동 정렬 | 불가 |

**워크드 예제.** `sort + unique + erase` 가 중복 제거의 표준 관용구: `unique` 는 인접 중복을 끝으로 밀고 새 끝 iterator를 반환 → `erase` 로 잘라낸다(정렬이 선행돼야 인접해짐).

## 응용 (Applications)

- 알고리즘 문제 풀이(컨테이너+`<algorithm>`), 고성능 데이터 처리.
- 정렬·탐색·변환·집계, 컨테이너 기반 도메인 모델.

## 흔한 오해 (Common Misunderstandings)

- **`vector` 가 항상 느린 고수준 도구가 아니다** — 연속 메모리라 캐시 친화·매우 빠름.
- **`std::list` 는 삽입은 빠르나 캐시 locality가 나빠 실측이 느리다** — 기본은 `vector`.
- **iterator 무효화를 무시하면 UB** — 컨테이너별 규칙 확인.
- **`unordered_map` 평균 $O(1)$ 이지만 최악·해시 품질**을 고려해야 한다.

## TMI

- `<algorithm>` 함수가 컨테이너가 아니라 iterator 범위를 받는 설계가 STL의 직교성(컨테이너 × 알고리즘)의 핵심이다.
- `reserve()` 로 `vector` 용량을 미리 잡으면 재할당·iterator 무효화를 줄인다.
- C++20 ranges는 lazy view 합성으로 중간 컨테이너 없이 파이프라인을 만든다.

## 연습 / 확인 문제 (Exercises)

- `vector<int>` 를 정렬하고 `sort+unique+erase` 로 중복을 제거하라.
- `map` 과 `unordered_map` 의 순회 순서·복잡도 차이를 보여라.
- `vector` 에 push_back 하며 iterator를 들고 있다가 무효화되는 버그를 재현하라.
- 람다 비교자로 구조체 벡터를 특정 필드 기준 정렬하라.

## 이어서 읽기 (Reading Path)

- 이전: [클래스와 템플릿](Cpp-Classes-and-Templates.md)
- 다음: [스마트 포인터와 메모리](Cpp-Memory-and-Smart-Pointers.md)
- 관련: [배열](../../../Data-Structures/Array.md), [해시 테이블](../../../Data-Structures/Hash-Table.md)

## 참조 (References)

- [Data-Structures/Array.md](../../../Data-Structures/Array.md)
- [Data-Structures/Hash-Table.md](../../../Data-Structures/Hash-Table.md)
