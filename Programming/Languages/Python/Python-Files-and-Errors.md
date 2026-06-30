# Python 파일과 예외 (Files and Errors)

- Level: Beginner
- Prerequisites: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

파일 입출력은 프로그램 밖 데이터를 읽고 쓰는 것, 예외 처리는 실행 중 오류 흐름을 다루는 것이다. Python은 **컨텍스트 매니저(`with`)** 로 자원을 안전하게 닫고, **`try/except`** 로 오류를 호출 스택 위로 전파·포착한다.

## 직관 (Intuition)

파일은 프로그램이 끝나도 남는 메모장, 예외는 "문제가 생겼다"는 신호다. Python 문화는 **EAFP**("허락보다 용서가 쉽다" — 일단 해 보고 예외를 잡는다)를 선호한다(LBYL "하기 전에 확인"보다). 좋은 코드는 오류를 숨기지 않고 *필요한 곳에서 구체적으로* 잡는다.

## 핵심 문법 (Core Syntax)

```python
with open("input.txt", "r", encoding="utf-8") as f:   # 자동 close
    text = f.read()

try:
    n = int(text.strip())
except ValueError:
    print("숫자로 바꿀 수 없습니다.")
```

## 이론 (Theory)

### 1. 컨텍스트 매니저 프로토콜

`with obj as x:` 은 `obj.__enter__()` 를 호출해 `x` 를 얻고, 블록을 벗어날 때 **예외 발생 여부와 무관하게** `obj.__exit__()` 를 부른다. 파일은 `__exit__` 에서 `close()` 하므로 자원 누수·디스크립터 고갈을 막는다.

### 2. 예외 전파와 구체성

예외는 잡힐 때까지 **호출 스택을 거슬러 전파**되고, 안 잡히면 트레이스백을 출력하며 종료. **너무 넓은 `except Exception`** 은 진짜 버그(타이포·논리 오류)까지 삼켜 "조용히 망가지는" 프로그램을 만든다 → 구체 예외(`FileNotFoundError`, `ValueError`)를.

### 3. else/finally와 인코딩·경로

`try/except/else/finally`: `else` 는 예외 없을 때, `finally` 는 항상(정리). 텍스트 파일은 **인코딩 명시**가 안전(기본값은 OS별로 다름). **상대 경로는 소스 위치가 아니라 현재 작업 디렉터리(cwd)** 기준이라 실행 위치에 따라 깨진다.

## 구현 (Implementation)

```python
from pathlib import Path

def read_count(path):
    try:
        with open(path, encoding="utf-8") as f:    # 컨텍스트 매니저
            return int(f.read().strip())
    except FileNotFoundError:                       # 구체 예외
        return 0
    except ValueError:                              # 내용이 숫자가 아님
        return -1

def stream_lines(path):                             # 큰 파일: 줄 단위(메모리 O(1))
    with open(path, encoding="utf-8") as f:
        for line in f:                              # 전체 read() 대신 스트리밍
            yield line.rstrip("\n")

print(Path("data") / "a.txt")                       # OS 독립 경로 결합
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 파일 I/O | 바이트 수·버퍼링·스토리지 지연에 좌우 |
| `f.read()` 전체 | 메모리 $O(\text{파일 크기})$ |
| 줄/청크 스트리밍 | 메모리 $O(1)$ — 큰 파일 권장 |
| 예외 발생 | 정상 흐름보다 비쌈(예외를 흐름 제어로 남용 금지) |

## 응용 (Applications)

- 설정 파일·CSV/JSON 로그 처리, 사용자 입력 검증.
- 실패 가능한 외부 작업(네트워크·DB) 감싸기, 재시도.

## 흔한 오해 (Common Misunderstandings)

- **예외를 다 무시(`except: pass`)하면** 안정이 아니라 조용한 붕괴.
- **파일을 안 닫으면 디스크립터 누수** — `with` 를 써라.
- **상대 경로는 cwd 기준** — 소스 기준이 아니다(`Path(__file__).parent` 활용).
- **인코딩 미지정은 이식성 문제** — `encoding="utf-8"` 명시.
- **큰 파일을 `read()` 로 통째로** 읽으면 메모리 폭발 — 스트리밍.

## TMI

- `pathlib.Path` 는 경로를 객체로 다뤄 `/` 연산자로 결합하고 OS 차이를 흡수한다.
- `with A() as a, B() as b:` 로 여러 자원을 한 번에 관리한다.
- `contextlib.contextmanager` 데코레이터로 제너레이터를 컨텍스트 매니저로 만든다(`yield` 앞=enter, 뒤=exit).

## 연습 / 확인 문제 (Exercises)

- 텍스트 파일의 줄 수를 스트리밍(메모리 $O(1)$)으로 세라.
- 존재하지 않는 파일을 열 때의 예외를 구체적으로 처리하라.
- `try/except/else/finally` 각 블록이 언제 실행되는지 출력으로 확인하라.
- 상대 경로가 실행 디렉터리에 따라 깨지는 예를 만들고 `Path(__file__)` 로 고쳐라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- 다음: [Python 클래스와 객체](Python-OOP.md)
- 관련: [스택 트레이스](../../../Engineering/Debugging/Stack-Traces.md)

## 참조 (References)

- [Engineering/Debugging/Stack-Traces.md](../../../Engineering/Debugging/Stack-Traces.md)
- [Reference/Books.md](../../../Reference/Books.md)
