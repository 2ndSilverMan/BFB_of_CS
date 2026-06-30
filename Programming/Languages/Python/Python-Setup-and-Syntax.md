# Python 실행 환경과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Python은 소스를 **바이트코드로 컴파일해 CPython 가상머신이 실행**하는 동적 타입 언어다. "변수에 타입이 있다"가 아니라 **이름이 객체를 가리킨다**(name binding)는 모델이 동작의 거의 전부를 설명한다. 들여쓰기는 스타일이 아니라 **문법**이다.

## 직관 (Intuition)

Python은 "읽기 쉬운 의사코드에 가까운 실행 가능한 문장"을 지향한다. 중괄호 대신 들여쓰기로 구조를 표현해 코드 모양이 곧 의미다. 내부적으론 `source → .pyc 바이트코드 → CPython VM 루프` 로 실행되며, 인터프리터 오버헤드 때문에 작은 연산의 대량 반복은 느리다(그래서 C로 구현된 내장 구조를 쓴다).

## 핵심 문법 (Core Syntax)

```python
name, age = "Ada", 20                  # 다중 대입 = 이름 바인딩
if age >= 18:
    print(f"{name} is an adult")        # f-string
for i in range(3):
    print(i)

import sys
def main():
    print(f"Python {sys.version_info.major}.{sys.version_info.minor}")
if __name__ == "__main__":              # 직접 실행 시에만
    main()
```

## 이론 (Theory)

### 1. 이름 바인딩과 동일성

`a = [1]` 은 리스트 객체를 만들고 이름 `a` 를 거기에 **바인딩**한다. `b = a` 는 같은 객체를 가리킨다(복사 아님). 그래서 **`is`(객체 동일성, 같은 메모리)와 `==`(값 동등성)는 다르다**. CPython은 작은 정수 `-5..256` 과 일부 문자열을 **인터닝(캐시)** 해 재사용한다.

### 2. 실행 모델과 GIL

CPython은 한 번에 한 스레드만 바이트코드를 실행하게 하는 **GIL(전역 인터프리터 락)** 이 있어, CPU 바운드 멀티스레딩은 진짜 병렬이 아니다(I/O 바운드는 이득). 진짜 병렬은 `multiprocessing` 이나 C 확장.

### 3. 재현성

전역에 패키지를 마구 설치하면 프로젝트 간 충돌·재현 불가가 생긴다 → **가상 환경**(`venv`)으로 인터프리터·의존성을 프로젝트별 격리.

## 구현 (Implementation)

```python
a = 256; b = 256
print(a is b)        # True  (작은 정수 캐시)
c = 257; d = 257
print(c is d)        # False (캐시 범위 밖, 별도 객체) — 값은 == True

x = [1, 2]; y = x
y.append(3)
print(x)             # [1, 2, 3]  ← 같은 객체(aliasing)
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 바이트코드 실행 | 인터프리터 루프 오버헤드(C/Rust보다 수십 배) |
| 내장 구조·C 라이브러리 | 같은 알고리즘도 훨씬 작은 상수 |
| CPU 바운드 스레딩 | GIL로 직렬화 → 멀티프로세싱 필요 |

## 응용 (Applications)

- 자동화 스크립트, 데이터 처리·AI/ML 실습.
- 웹 서버·CLI 도구, 알고리즘 문제 풀이(빠른 작성).

## 흔한 오해 (Common Misunderstandings)

- **들여쓰기는 스타일이 아니라 문법** — 섞인 탭/스페이스는 에러.
- **동적 타입 ≠ 타입 없음** — 객체에는 타입이 있고, 이름에 없을 뿐.
- **`is` 는 값 비교가 아니다** — 동일성. 값 비교는 `==`. (`x is None` 만 `is` 관례.)
- **작은 정수 캐시에 의존하지 말 것** — 구현 세부라 범위 밖에선 `is` 가 False.
- **전역 설치는 재현성을 해친다** — venv 사용.

## TMI

- `python -m module` 은 모듈을 스크립트처럼 실행한다(`-m venv`, `-m http.server` 등).
- `import dis; dis.dis(f)` 로 함수의 바이트코드를 직접 볼 수 있다.
- f-string(3.6+)은 컴파일 시점에 포맷 코드로 풀려 `%`/`.format` 보다 빠르다.

## 연습 / 확인 문제 (Exercises)

- `a=256;b=256` 과 `c=257;d=257` 의 `is`/`==` 결과를 예측하고 확인하라.
- aliasing으로 리스트가 의도치 않게 바뀌는 예를 만들고 복사로 고쳐라.
- `dis` 로 간단한 함수의 바이트코드를 출력하라.
- venv를 만들어 같은 패키지의 두 버전을 격리하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [Python 컬렉션](Python-Collections.md)
- 관련: [값과 참조 / 메모리](../../Pointers-and-Memory.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
