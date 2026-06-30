# 셸과 기본 명령 (Linux Shell Basics)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

셸은 사용자의 명령을 읽어 **프로그램을 실행하는 인터페이스**다. 내부적으로는 입력을 파싱·확장한 뒤 `fork`로 자식 프로세스를 만들고 `exec`로 프로그램을 올린다([프로세스와 스레드](../Processes-and-Threads.md)). **표준 스트림 + 파이프 + 리디렉션**으로 작은 도구를 조합하는 것이 유닉스 철학의 핵심.

## 직관 (Intuition)

GUI가 버튼·창으로 일한다면, 셸은 짧은 문장으로 시킨다. 기록·자동화가 쉬워 서버 운영의 기본 도구다. 진짜 힘은 **"작은 도구를 파이프로 잇기"** — `ls | grep | wc` 처럼 한 도구의 출력이 다음 도구의 입력이 된다.

## 이론 (Theory)

### 1. 표준 스트림과 파일 디스크립터

모든 프로세스는 **fd 0=stdin, 1=stdout, 2=stderr** 로 시작한다. **리디렉션**은 이 fd를 파일로 바꾼다: `> out`(stdout→파일), `2> err`(stderr), `< in`(stdin). **파이프** `A | B` 는 A의 fd1을 B의 fd0에 연결(커널 파이프 버퍼).

### 2. 셸의 확장 순서

셸은 명령 실행 전에 단계적으로 확장한다(대략): 중괄호 `{a,b}` → 틸드 `~` → 변수 `$VAR` → 명령치환 `$(...)` → **글로빙** `*.txt`(파일명 매칭) → 단어 분할. 그래서 `rm *.txt` 의 `*` 는 `rm`이 아니라 **셸**이 먼저 파일 목록으로 펼친다.

### 3. 내장 vs 외부, 종료 코드

`cd`·`export` 는 셸 상태를 바꿔 **내장 명령**(자식이면 부모 디렉터리가 안 바뀜), `ls`·`grep` 은 외부 프로그램. 각 명령은 **종료 코드**(0=성공, 비0=실패)를 `$?` 로 남기고, `&&`/`||` 가 이를 본다.

## 구현 (Implementation)

```bash
pwd; ls -la                       # 현재 위치, 상세 목록
mkdir -p practice && cd practice  # 성공 시에만 cd (&&)

# 파이프라인: 각 도구의 stdout → 다음 stdin
cat /etc/passwd | grep "/bin/bash" | wc -l    # bash 쓰는 계정 수

ls *.txt 2> /dev/null             # 글로빙(셸이 펼침), stderr 버림
echo "exit code: $?"              # 직전 명령 종료 코드
```

**워크드 예제(`ls | grep .md | wc -l`).** ① `ls` 가 파일명을 stdout으로 → ② 파이프 버퍼 → ③ `grep .md` 가 `.md` 줄만 통과 → ④ `wc -l` 이 줄 수를 셈. 세 프로세스가 **동시에** 돌며 스트리밍된다(전체를 다 모으고 넘기는 게 아님).

## 복잡도 (Complexity)

| 작업 | 좌우 요인 |
|---|---|
| 파일 목록 | 디렉터리 항목 수 |
| 복사 | 파일 크기·디스크 속도 |
| 검색(`grep -r`) | 탐색 범위·I/O |
| 파이프라인 | 가장 느린 단계(병목) |

## 응용 (Applications)

- 서버 접속 후 상태 확인, 파일 이동·복사·압축.
- 로그 검색·필터링(`grep`/`awk`/`sed`), 스크립트 자동화의 기반.

## 흔한 오해 (Common Misunderstandings)

- **`*` 는 명령이 아니라 셸이 확장**한다 — `rm *` 는 셸이 먼저 펼친 목록을 `rm`에 넘긴다(그래서 위험).
- **`cd` 가 내장인 이유** — 외부 프로그램이면 자식 프로세스의 디렉터리만 바뀌고 셸은 그대로.
- **조용히 끝났다고 성공이 아니다** — `$?`·stderr 확인.
- **`A | B` 는 순차가 아니라 동시 실행 + 스트리밍**.

## TMI

- `man command`(매뉴얼), `history`(이전 명령 — 비밀값을 명령에 직접 쓰면 기록됨 주의), Tab completion(오타 방지).
- `2>&1` 은 "stderr를 stdout이 가는 곳으로" — 순서가 중요해 `> f 2>&1` 와 `2>&1 > f` 가 다르다.
- 파이프의 한 단계가 실패해도 기본 종료 코드는 마지막 명령 것 — `set -o pipefail` 로 바꾼다.

## 연습 / 확인 문제 (Exercises)

- `ls | grep | wc -l` 파이프라인을 만들고 각 단계의 stdin/stdout을 설명하라.
- `rm *.txt` 에서 `*` 를 누가 펼치는지(셸 vs rm) 설명하고 위험성을 논하라.
- `cmd > out 2>&1` 와 `cmd 2>&1 > out` 의 차이를 fd 관점에서 설명하라.
- `A && B || C` 의 동작을 종료 코드 `$?` 로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](../Processes-and-Threads.md)
- 다음: [사용자와 권한](Linux-Users-Permissions.md)
- 관련: [Linux 파일 시스템](Linux-File-System.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md)
- [Reference/Books.md](../../../Reference/Books.md)
