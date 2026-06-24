# Python 학습 트랙 (Python)

> 빠르게 실행해 보며 프로그래밍 기본기, 자동화, 데이터/AI 실습으로 이어지는 언어 트랙.

**선수지식**: [Programming/](../../)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 실행 환경과 기본 문법 | [Python-Setup-and-Syntax.md](Python-Setup-and-Syntax.md) | 인터프리터, 스크립트 실행, 들여쓰기, 기본 입출력 | Draft |
| 2 | 컬렉션 | [Python-Collections.md](Python-Collections.md) | list, tuple, dict, set과 순회 패턴 | Draft |
| 3 | 함수와 모듈 | [Python-Functions-and-Modules.md](Python-Functions-and-Modules.md) | 함수 정의, 스코프, import, 패키지 기본 | Draft |
| 4 | 파일과 예외 | [Python-Files-and-Errors.md](Python-Files-and-Errors.md) | 파일 입출력, 예외 처리, with 문 | Draft |
| 5 | 클래스와 객체 | [Python-OOP.md](Python-OOP.md) | class, 인스턴스, 메서드, 간단한 데이터 모델 | Draft |

---

## 학습 순서

```text
Python-Setup-and-Syntax -> Python-Collections -> Python-Functions-and-Modules
        ↓
Python-Files-and-Errors -> Python-OOP
```

---

## TMI

- Guido van Rossum은 1989년 12월 크리스마스 무렵의 취미 프로젝트로 Python 인터프리터를 쓰기 시작했다.
- Python이라는 이름은 뱀이 아니라 [Monty Python's Flying Circus](https://docs.python.org/3/faq/general.html#why-is-it-called-python)에서 왔다.
- Python의 `import this`를 실행하면 "The Zen of Python"이라는 짧은 철학 목록을 볼 수 있다.
- `import antigravity`를 실행하면 웹 브라우저로 관련 만화를 열려고 한다. 표준 라이브러리에 들어 있는 유명한 이스터에그다.
- Python은 들여쓰기가 문법이라 탭과 스페이스를 섞으면 `TabError` 같은 오류를 볼 수 있다.
- `-5`부터 `256`까지의 작은 정수는 CPython에서 재사용되는 경우가 많다. 그래서 `is`로 숫자를 비교하는 코드는 우연히 맞아 보일 수 있지만, 값 비교에는 `==`를 써야 한다.

---

## 연관 섹션

- [Programming/](../../) - 공통 프로그래밍 개념
- [Data-Structures/](../../../Data-Structures/) - 컬렉션 뒤에 이어지는 자료구조
- [AI/](../../../AI/) - Python 실습 이후 이어지는 AI/ML 경로
