# Java 컬렉션

- Level: Intermediate
- Prerequisites: [Java 인터페이스와 제네릭](Java-Generics-and-Interfaces.md), [Data-Structures/](../../../Data-Structures/)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Java Collections Framework(JCF)는 `List`·`Set`·`Map`·`Queue` **인터페이스와 구현체를 분리**해 제공한다. 변수는 인터페이스 타입으로, 구현체는 access pattern으로 고르는 것이 핵심 사용법이다.

## 직관 (Intuition)

컬렉션은 데이터를 담는 표준 상자. 순서가 필요하면 `List`, 중복 제거면 `Set`, key-value면 `Map`. 같은 인터페이스라도 **구현체마다 내부 자료구조·복잡도·순서 보장이 다르다** — `ArrayList` vs `LinkedList`, `HashMap` vs `TreeMap`.

## 핵심 문법 (Core Syntax)

```java
List<String> names = new ArrayList<>();    names.add("Ada");
Set<String> tags  = new HashSet<>();       tags.add("java");
Map<String,Integer> scores = new HashMap<>(); scores.put("Ada", 100);
```

## 이론 (Theory)

### 1. 구현체 내부

| 인터페이스 | 구현체 | 내부 | 특성 |
|---|---|---|---|
| List | ArrayList / LinkedList | [동적 배열](../../../Data-Structures/Array.md) / [이중 연결](../../../Data-Structures/Linked-List.md) | 인덱스 $O(1)$ / 핸들 삽입 $O(1)$ |
| Map | HashMap / TreeMap | [해시 테이블](../../../Data-Structures/Hash-Table.md) / [레드-블랙](../../../Data-Structures/Red-Black-Tree.md) | 평균 $O(1)$ / 정렬 $O(\log n)$ |
| Set | HashSet / TreeSet | HashMap / TreeMap 위 | 위와 동일 |

### 2. HashMap 내부 (Java 8+)

버킷 배열 + 체이닝. **부하율 0.75** 초과 시 2배 resize. 한 버킷 체인이 **8을 넘고 테이블 ≥ 64면 레드-블랙 트리로 treeify** → 최악을 $O(n)$ 에서 $O(\log n)$ 으로. 키는 **`equals`/`hashCode` 계약**(같으면 같은 해시)을 지켜야 한다.

### 3. fail-fast 반복자

대부분 컬렉션은 순회 중 구조 변경을 감지해 **`ConcurrentModificationException`** 을 던진다(fail-fast). 순회 중 제거는 `Iterator.remove` 또는 `removeIf`.

## 구현 (Implementation)

```java
import java.util.*;
public class Main {
    public static void main(String[] args) {
        String[] words = {"a","b","a","c","a"};
        Map<String,Integer> freq = new HashMap<>();    // 변수는 인터페이스 타입
        for (String w : words) freq.merge(w, 1, Integer::sum);   // 집계 관용구
        System.out.println(freq.get("a"));             // 3

        List<Integer> xs = new ArrayList<>(List.of(3,1,2,3));
        xs.removeIf(x -> x == 3);                       // 순회 중 안전 제거
        Collections.sort(xs);                          // [1, 2]
    }
}
```

## 복잡도 (Complexity)

| 연산 | ArrayList | LinkedList | HashMap | TreeMap |
|---|---|---|---|---|
| 인덱스 접근 | $O(1)$ | $O(n)$ | — | — |
| 검색 | $O(n)$ | $O(n)$ | 평균 $O(1)$ | $O(\log n)$ |
| 끝 삽입 | amortized $O(1)$ | $O(1)$ | 평균 $O(1)$ | $O(\log n)$ |

## 응용 (Applications)

- 목록·테이블 데이터, 중복 제거, 빈도 집계.
- BFS/DFS(`ArrayDeque`), 캐시(`LinkedHashMap`의 LRU).

## 흔한 오해 (Common Misunderstandings)

- **인터페이스 타입 선언이 구현체 교체를 쉽게** 한다(`List<String> = new ArrayList<>()`).
- **`HashMap` 순서에 의존 금지** — 순서는 `LinkedHashMap`/`TreeMap`.
- **객체를 키로 쓰려면 `equals`/`hashCode` 일관성** — 하나만 오버라이드하면 버그.
- **순회 중 수정은 `ConcurrentModificationException`** — `Iterator.remove`/`removeIf`.

## TMI

- `Collections`(유틸리티 클래스)와 `Collection`(인터페이스)은 다른 것.
- `List.of`/`Map.of` 는 **불변** 컬렉션 — `add` 하면 `UnsupportedOperationException`.
- Stream API(`words.stream().collect(...)`)는 컬렉션 처리를 선언적 파이프라인으로 표현한다.

## 연습 / 확인 문제 (Exercises)

- 문자열 목록 중복을 `Set` 으로 제거하라.
- `merge`/`getOrDefault` 로 단어 빈도를 집계하라.
- `ArrayList` vs `LinkedList` 의 인덱스 접근·삽입 비용을 비교하라.
- 순회 중 `remove` 로 `ConcurrentModificationException` 을 재현하고 `removeIf` 로 고쳐라.

## 이어서 읽기 (Reading Path)

- 이전: [인터페이스와 제네릭](Java-Generics-and-Interfaces.md)
- 다음: [Java 예외와 파일](Java-Exceptions-and-Files.md)
- 관련: [해시 테이블](../../../Data-Structures/Hash-Table.md)

## 참조 (References)

- [Data-Structures/Array.md](../../../Data-Structures/Array.md)
- [Data-Structures/Hash-Table.md](../../../Data-Structures/Hash-Table.md)
