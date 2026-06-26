# Python 파일과 예외 (Files and Errors)

- Level: Beginner
- Prerequisites: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

파일 입출력은 프로그램 밖의 데이터를 읽고 쓰는 방법이고, 예외 처리는 실행 중 발생한 오류를 다루는 방법이다. Python에서는 `with` 문으로 파일 자원을 안전하게 관리하고 `try/except`로 오류 흐름을 처리한다.

## 직관 (Intuition)

파일은 프로그램이 끝나도 남는 메모장이고, 예외는 실행 중 문제가 생겼다는 신호다. 좋은 프로그램은 문제를 숨기지 않고 필요한 곳에서 잡아 의미 있는 메시지로 바꾼다.

## 핵심 문법 (Core Syntax)

```python
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

try:
    number = int(text.strip())
except ValueError:
    print("숫자로 바꿀 수 없습니다.")
```

`with`는 파일을 자동으로 닫아 자원 누수를 줄인다.

## 이론 (Theory)

예외는 호출 스택을 따라 전파된다. 너무 넓은 `except Exception`은 버그를 숨길 수 있으므로 가능한 구체적 예외를 잡는다. 파일 경로는 실행 위치에 따라 달라질 수 있어 상대 경로 사용 시 주의한다.

## 구현 (Implementation)

파일은 `with open(..., encoding="utf-8")`처럼 context manager로 열고, 예외는 `FileNotFoundError`, `PermissionError`, `UnicodeDecodeError`처럼 구체적으로 처리한다. 사용자에게 보여 줄 메시지와 로그에 남길 세부 정보를 분리한다.

```python
def read_count(path):
    try:
        with open(path, encoding="utf-8") as f:   # context manager
            return int(f.read().strip())
    except FileNotFoundError:                      # 구체 예외 처리
        return 0
    except ValueError:
        return -1


print(read_count("missing.txt"))  # 0
```

## 복잡도 (Complexity)

파일 I/O 시간은 byte 수, buffering, storage latency에 좌우된다. 큰 파일을 한 번에 `read()`하면 memory 사용량이 파일 크기에 비례하므로 line streaming이나 chunk 처리로 제한한다.

## 응용 (Applications)

- 설정 파일 읽기
- CSV/JSON 로그 처리
- 사용자 입력 검증
- 실패 가능한 외부 작업 감싸기

## 흔한 오해 (Common Misunderstandings)

- 예외를 모두 무시하면 안정적인 프로그램이 아니라 조용히 망가지는 프로그램이 된다.
- 파일을 열기만 하고 닫지 않으면 자원이 낭비될 수 있다.
- 상대 경로는 소스 파일 위치가 아니라 현재 작업 디렉터리 기준으로 해석될 수 있다.
- 텍스트 파일은 인코딩을 명시하는 편이 안전하다.

## TMI

- `pathlib.Path`는 경로를 객체로 다루게 해 주는 표준 라이브러리다.
- `json` 모듈은 설정과 데이터 교환에 자주 쓰인다.
- `finally`는 예외 발생 여부와 관계없이 정리 코드를 실행한다.

## 연습 / 확인 문제 (Exercises)

- 텍스트 파일의 줄 수를 세는 스크립트를 작성하라.
- 존재하지 않는 파일을 열 때 발생하는 예외를 처리하라.
- JSON 파일을 읽어 특정 key를 출력하라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- 다음: [Python 클래스와 객체](Python-OOP.md)

## 참조 (References)

- [Engineering/Debugging/Stack-Traces.md](../../../Engineering/Debugging/Stack-Traces.md)
- [Reference/Books.md](../../../Reference/Books.md)
