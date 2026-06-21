# CPU 구조와 명령어 집합 (CPU and ISA)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/Data-Representation.md](Data-Representation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

CPU는 메모리에 있는 명령어를 하나씩 가져와 실행하는 장치다. **명령어 집합 구조(ISA, Instruction Set Architecture)** 는 "CPU가 이해하는 명령어의 목록과 규칙"으로, 하드웨어와 소프트웨어 사이의 계약이다. 컴파일러는 고수준 코드를 이 ISA의 명령어로 번역한다.

## 직관 (Intuition)

CPU는 단순한 동작을 엄청나게 빠르게 반복한다. "명령어를 가져오고(fetch) → 해석하고(decode) → 실행하고(execute) → 결과를 쓴다(writeback)"는 사이클을 초당 수십억 번 돈다. ISA는 이때 쓸 수 있는 "단어 목록"이고, 프로그램은 그 단어들을 늘어놓은 문장이다.

```mermaid
flowchart LR
    Fetch["가져오기 (Fetch)"] --> Decode["해석 (Decode)"]
    Decode --> Execute["실행 (Execute)"]
    Execute --> Writeback["기록 (Writeback)"]
    Writeback --> Fetch
```

## 이론 (Theory)

CPU의 핵심 부품:

| 부품 | 역할 |
|---|---|
| 레지스터(register) | CPU 내부의 초고속 임시 저장소 |
| ALU | 산술·논리 연산 수행 |
| 제어 장치(CU) | 명령어를 해석하고 신호를 보냄 |
| 프로그램 카운터(PC) | 다음에 실행할 명령어 주소 |

명령어는 보통 연산 코드(opcode)와 피연산자(operand)로 구성된다. ISA 설계 철학은 크게 둘로 나뉜다.

- **RISC**: 단순하고 고정 길이인 적은 수의 명령어(ARM, RISC-V).
- **CISC**: 복잡하고 가변 길이인 많은 명령어(x86).

성능의 대략적 관계는 다음과 같다.

$$\text{실행 시간} = \text{명령어 수} \times \text{CPI} \times \text{클럭 주기}$$

여기서 CPI는 명령어당 평균 사이클 수다. 셋 중 하나만 줄여서는 전체가 빨라지지 않는다.

## 구현 (Implementation)

ISA의 fetch-decode-execute를 흉내 낸 아주 작은 가상 머신이다.

```python
def run(program):
    regs = {"A": 0, "B": 0}
    pc = 0
    while pc < len(program):
        op, *args = program[pc]        # fetch + decode
        if op == "SET":
            regs[args[0]] = args[1]    # execute + writeback
        elif op == "ADD":
            regs[args[0]] += regs[args[1]]
        elif op == "PRINT":
            print(regs[args[0]])
        pc += 1                        # 다음 명령어로

run([
    ("SET", "A", 2),
    ("SET", "B", 3),
    ("ADD", "A", "B"),   # A = A + B
    ("PRINT", "A"),      # 5
])
```

## 복잡도 (Complexity)

알고리즘 빅오가 아니라 **명령어 수·CPI·클럭**의 곱으로 성능을 본다.

| 지표 | 의미 |
|---|---|
| 클럭 주파수 | 초당 사이클 수(Hz) |
| CPI | 명령어당 평균 사이클 |
| IPC | 사이클당 실행 명령어 수(CPI의 역수 관점) |

같은 일을 더 적은 명령어로, 더 낮은 CPI로, 더 높은 클럭으로 하면 빨라진다.

## 응용 (Applications)

- 컴파일러의 코드 생성과 최적화 대상
- 임베디드·모바일에서 ISA 선택(전력 대 성능)
- 성능 분석(명령어 수·분기 예측 실패·캐시 미스)
- 에뮬레이터, 가상 머신, 바이트코드 설계

## 흔한 오해 (Common Misunderstandings)

- 클럭이 높으면 무조건 빠르다고 오해한다. 명령어 수와 CPI가 더 나쁘면 느릴 수 있다.
- RISC가 CISC보다 항상 우월한 것은 아니다. 설계 트레이드오프이며, 현대 x86은 내부적으로 RISC식 마이크로옵으로 분해해 실행한다.
- ISA와 마이크로아키텍처는 다르다. ISA는 "무엇을(계약)", 마이크로아키텍처는 "어떻게(구현)"다.
- 어셈블리가 곧 기계어는 아니다. 어셈블리는 사람이 읽을 수 있는 표기이고, 기계어는 그 비트 인코딩이다.

## TMI

- x86은 대표적 CISC, ARM·RISC-V는 RISC다. 스마트폰 대부분은 ARM, 최근 노트북에도 ARM(Apple Silicon)이 늘었다.
- 무어의 법칙(트랜지스터 수가 약 2년마다 2배)은 오랫동안 성능 향상을 이끌었지만, 클럭 한계로 이제는 멀티코어·전용 가속기 쪽으로 방향이 옮겨졌다.
- 복잡한 명령어를 내부에서 더 작은 단위(마이크로코드)로 풀어 실행하는 기법은 1950~60년대부터 쓰였다.

## 연습 / 확인 문제 (Exercises)

- 위 가상 머신에 `SUB`와 조건 분기 `JMP_IF_ZERO` 명령어를 추가해 보라.
- 명령어 수가 같을 때 CPI가 절반이 되면 실행 시간은 어떻게 변하는지 식으로 설명하라.
- RISC와 CISC의 트레이드오프를 명령어 길이·디코딩 복잡도 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [데이터 표현](Data-Representation.md)
- 다음: 파이프라이닝 (예정 `Pipelining.md`), 메모리 계층 (예정 `Memory-Hierarchy.md`)

## 참조 (References)

- [Systems/Computer-Architecture/Data-Representation.md](Data-Representation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
