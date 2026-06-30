# Java 인터페이스와 제네릭

- Level: Intermediate
- Prerequisites: [Java 클래스와 객체](Java-Classes-and-Objects.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

인터페이스는 객체가 제공할 **행동의 계약**, 제네릭은 **타입을 매개변수로** 받아 재사용 가능한 타입 안전 코드를 만드는 기능이다. Java 제네릭의 핵심 특이점은 **type erasure**(런타임에 타입 인자가 지워짐)다.

## 직관 (Intuition)

인터페이스는 "이 물건은 이런 버튼을 제공해야 한다"는 약속, 제네릭은 "상자 안에 뭐가 들어갈진 나중에 정하되 한 번 정하면 지킨다"는 장치. "구체 클래스가 아니라 인터페이스에 의존하라"가 테스트·교체 용이성의 토대다.

## 핵심 문법 (Core Syntax)

```java
interface Repository<T> {
    T findById(String id);
    void save(T value);
}
class UserRepository implements Repository<User> {
    public User findById(String id) { return new User(id); }
    public void save(User v) { /* ... */ }
}
```

## 이론 (Theory)

### 1. type erasure

제네릭은 **컴파일 타임 검사용**이고, 컴파일 후 타입 인자는 지워져 런타임엔 raw(보통 `Object`)다. 그래서 `new T()`·`T[]`·`instanceof List<String>` 이 불가, primitive는 **boxing**(`List<int>` 불가, `List<Integer>`)된다.

### 2. PECS 와일드카드

**Producer Extends, Consumer Super**:

- `? extends T` — 읽기(생산자): `List<? extends Number>` 에서 꺼내 `Number` 로 읽기 가능, 넣기 불가.
- `? super T` — 쓰기(소비자): `List<? super Integer>` 에 `Integer` 넣기 가능.

### 3. 불변성(invariance)과 default method

제네릭은 **불변** — `List<String>` 은 `List<Object>` 의 하위 타입이 **아니다**(배열의 공변성과 다름, 그래서 더 안전). 인터페이스는 **default method**(구현 포함)와 함수형 인터페이스(단일 추상 메서드 → 람다)를 가질 수 있다.

## 구현 (Implementation)

```java
import java.util.List;
public class Main {
    static <T extends Comparable<T>> T max(List<T> items) {   // bounded type param
        T best = items.get(0);
        for (T x : items) if (x.compareTo(best) > 0) best = x;
        return best;
    }
    // PECS: src에서 읽고(extends) dst에 쓴다(super)
    static <T> void copy(List<? extends T> src, List<? super T> dst) {
        for (T x : src) dst.add(x);
    }
    public static void main(String[] args) {
        System.out.println(max(List.of(3, 9, 2)));            // 9
    }
}
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 제네릭 | 런타임 오버헤드 없음(erasure), primitive specialization 없음 |
| boxing | 객체 할당 + indirection 비용(`Integer` 등) |
| 인터페이스 디스패치 | JIT inlining 여부에 따라 비용 변동 |

## 응용 (Applications)

- 컬렉션 타입 안전성, 의존성 역전(인터페이스 의존), 테스트 더블.
- 재사용 라이브러리(제네릭 + bounded type), 함수형 인터페이스 + 람다.

## 흔한 오해 (Common Misunderstandings)

- **인터페이스에 구현이 있을 수 있다** — default method.
- **raw type(`List`)은 타입 안전성을 잃는다** — 항상 제네릭으로.
- **`List<Object>` 는 `List<String>` 의 상위가 아니다** — 불변성.
- **제네릭은 런타임 타입 검사 도구가 아니다** — erasure, 컴파일 타임 안전장치.

## TMI

- 배열은 공변(`String[]` is `Object[]`)이라 `ArrayStoreException` 런타임 오류가 가능 — 제네릭의 불변성이 이를 컴파일 타임에 막는다.
- `? extends`/`? super` 혼동 시 "꺼낼 거면 extends, 넣을 거면 super"(PECS)를 떠올린다.
- `@FunctionalInterface` 애너테이션은 단일 추상 메서드 계약을 컴파일러가 강제하게 한다.

## 연습 / 확인 문제 (Exercises)

- `Formatter<T>` 인터페이스 + 구현체를 작성하라(default method 포함).
- raw `List` 사용 시의 unchecked 경고·위험을 재현하라.
- `copy(src, dst)` 를 PECS 와일드카드로 작성하고 왜 안전한지 설명하라.
- 배열 공변성으로 `ArrayStoreException` 을 만들고 제네릭이 이를 어떻게 막는지 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [Java 클래스와 객체](Java-Classes-and-Objects.md)
- 다음: [Java 컬렉션](Java-Collections.md)
- 관련: [SOLID](../../../Engineering/Software-Design/SOLID.md)

## 참조 (References)

- [Engineering/Software-Design/SOLID.md](../../../Engineering/Software-Design/SOLID.md)
- [Reference/Books.md](../../../Reference/Books.md)
