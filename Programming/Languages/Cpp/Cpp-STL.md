# C++ STL

- Level: Intermediate
- Prerequisites: [C++ 클래스와 템플릿](Cpp-Classes-and-Templates.md), [Data-Structures/](../../../Data-Structures/)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

STL(Standard Template Library)은 컨테이너, 반복자, 알고리즘, 함수 객체를 제공하는 C++ 표준 라이브러리의 핵심 부분이다. 자료구조와 알고리즘을 템플릿 기반으로 조합한다.

## 직관 (Intuition)

`vector`에 데이터를 담고, iterator로 범위를 가리키고, `sort` 같은 알고리즘을 적용한다. 직접 루프를 다 쓰기보다 검증된 표준 도구를 조합한다.

## 핵심 문법 (Core Syntax)

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> xs = {3, 1, 4, 2};
    std::sort(xs.begin(), xs.end());
    for (int x : xs) {
        std::cout << x << "\n";
    }
}
```

## 이론 (Theory)

STL은 컨테이너가 데이터를 보관하고, iterator가 범위를 표현하며, algorithm이 범위에 동작하는 구조다. 컨테이너의 iterator invalidation, 정렬 조건, allocator, value category를 이해하면 표준 라이브러리 사용이 훨씬 예측 가능해진다.

## 구현 (Implementation)

구현할 때는 직접 자료구조를 만들기 전에 표준 컨테이너와 알고리즘 조합으로 표현할 수 있는지 먼저 본다. 성능이 중요하면 컨테이너별 복잡도와 메모리 locality를 측정한다.

```cpp
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> words = {"a", "b", "a", "c", "b", "a"};
    std::map<std::string, int> freq;
    for (const auto& w : words) freq[w]++;     // 표준 컨테이너 활용
    auto top = std::max_element(freq.begin(), freq.end(),
        [](const auto& l, const auto& r) { return l.second < r.second; });
    std::cout << top->first << ":" << top->second << "\n";  // a:3
}
```

## 복잡도 (Complexity)

`std::vector`는 연속 배열, `std::map`은 보통 balanced tree, `std::unordered_map`은 hash table 기반이다. 컨테이너마다 iterator invalidation 규칙이 다르다.

## 응용 (Applications)

- 알고리즘 문제 풀이
- 고성능 데이터 처리
- 정렬, 탐색, 변환
- 컨테이너 기반 도메인 모델

## 흔한 오해 (Common Misunderstandings)

- `vector`는 항상 느린 고수준 도구가 아니다. 연속 메모리라 매우 빠른 경우가 많다.
- `std::list`는 삽입이 빠르지만 캐시 locality가 나빠 실제로 느릴 수 있다.
- Iterator invalidation을 무시하면 미묘한 버그가 생긴다.
- `unordered_map`은 평균 O(1)이지만 최악과 해시 품질을 고려해야 한다.

## TMI

- Range-based for는 iterator 문법을 간결하게 만든다.
- `<algorithm>`의 함수들은 컨테이너가 아니라 iterator range를 받는다.
- C++20 ranges는 알고리즘 조합을 더 표현력 있게 만든다.

## 연습 / 확인 문제 (Exercises)

- `vector<int>`를 정렬하고 중복을 제거하라.
- `map`과 `unordered_map`의 차이를 설명하라.
- Iterator invalidation이 발생하는 예를 찾아라.

## 이어서 읽기 (Reading Path)

- 이전: [클래스와 템플릿](Cpp-Classes-and-Templates.md)
- 다음: [스마트 포인터와 메모리](Cpp-Memory-and-Smart-Pointers.md)

## 참조 (References)

- [Data-Structures/Array.md](../../../Data-Structures/Array.md)
- [Data-Structures/Hash-Table.md](../../../Data-Structures/Hash-Table.md)
