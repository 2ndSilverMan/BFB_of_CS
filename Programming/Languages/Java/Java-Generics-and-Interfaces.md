# Java 인터페이스와 제네릭

- Level: Intermediate
- Prerequisites: [Java 클래스와 객체](Java-Classes-and-Objects.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인터페이스는 객체가 제공해야 할 행동의 계약이고, 제네릭은 타입을 매개변수로 받아 재사용 가능한 타입 안전 코드를 작성하는 기능이다.

## 직관 (Intuition)

인터페이스는 "이 물건은 이런 버튼을 제공해야 한다"는 약속이고, 제네릭은 "상자 안에 무엇이 들어갈지는 나중에 정하되, 한 번 정하면 그 타입을 지키자"는 장치다.

## 핵심 문법 (Core Syntax)

```java
interface Repository<T> {
    T findById(String id);
    void save(T value);
}

class UserRepository implements Repository<User> {
    public User findById(String id) {
        return new User(id);
    }
    public void save(User value) {
        // 저장
    }
}
```

## 이론 (Theory)

인터페이스는 다형성을 제공한다. 코드는 구체 클래스보다 인터페이스에 의존할 때 교체와 테스트가 쉬워진다. 제네릭은 컴파일 시점 타입 검사를 강화하지만, Java의 type erasure 때문에 런타임에는 일부 타입 정보가 사라진다.

## 구현 (Implementation)

API는 가능한 interface 타입으로 받고, 구현체는 사용 지점에서 선택한다. Generics는 `List<T>`, bounded type parameter, wildcard를 작은 예제로 나눠 확인하고 unchecked warning을 남기지 않도록 한다.

```java
import java.util.List;

public class Main {
    // bounded type parameter: Comparable을 만족하는 T만 허용
    static <T extends Comparable<T>> T max(List<T> items) {
        T best = items.get(0);
        for (T x : items) {
            if (x.compareTo(best) > 0) best = x;
        }
        return best;
    }

    public static void main(String[] args) {
        System.out.println(max(List.of(3, 9, 2)));  // 9
    }
}
```

## 복잡도 (Complexity)

Java generics는 주로 type erasure로 구현되어 primitive specialization을 자동 제공하지 않는다. Boxing된 값은 객체 allocation과 indirection 비용을 만들 수 있고, interface dispatch는 JIT 최적화 여부에 따라 비용이 달라진다.

## 응용 (Applications)

- 컬렉션 타입 안전성
- 의존성 역전
- 테스트 더블 작성
- 재사용 가능한 라이브러리 설계

## 흔한 오해 (Common Misunderstandings)

- 인터페이스는 구현이 전혀 없다는 뜻만은 아니다. default method가 있을 수 있다.
- Raw type을 쓰면 제네릭의 타입 안전성을 잃는다.
- `List<Object>`는 `List<String>`의 상위 타입이 아니다.
- 제네릭은 런타임 타입 검사 도구가 아니라 컴파일 타임 안전장치에 가깝다.

## TMI

- Wildcard `? extends T`, `? super T`는 생산자/소비자 위치에 따라 사용한다.
- "Program to an interface"는 Java 설계에서 자주 나오는 원칙이다.
- 함수형 인터페이스는 lambda expression과 연결된다.

## 연습 / 확인 문제 (Exercises)

- `Formatter<T>` 인터페이스를 만들고 구현체를 작성하라.
- Raw `List`를 썼을 때 생기는 위험을 예제로 보여라.
- `extends` wildcard와 `super` wildcard를 언제 쓰는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Java 클래스와 객체](Java-Classes-and-Objects.md)
- 다음: [Java 컬렉션](Java-Collections.md)

## 참조 (References)

- [Engineering/Software-Design/SOLID.md](../../../Engineering/Software-Design/SOLID.md)
- [Reference/Books.md](../../../Reference/Books.md)
