# 셸과 기본 명령 (Linux Shell Basics)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

셸(shell)은 사용자의 명령을 읽고 프로그램을 실행하는 인터페이스다. Linux 명령줄에서는 경로를 이동하고, 파일을 보고, 명령을 조합해 운영체제와 상호작용한다.

## 직관 (Intuition)

그래픽 파일 탐색기가 버튼과 창으로 일을 한다면, 셸은 짧은 문장으로 일을 시킨다. 처음에는 낯설지만 기록 가능하고 자동화하기 쉬워 서버 운영의 기본 도구가 된다.

## 이론 (Theory)

명령은 보통 `command option argument` 구조를 갖는다. 현재 디렉터리는 working directory이고, 상대 경로는 그 위치를 기준으로 해석된다. 표준 입력(stdin), 표준 출력(stdout), 표준 오류(stderr)를 통해 프로그램을 연결할 수 있다.

명령은 셸 내장 명령과 외부 프로그램으로 나뉜다. `cd`는 현재 셸 상태를 바꾸므로 내장 명령이고, `ls` 같은 명령은 외부 프로그램일 수 있다.

## 구현 (Implementation)

```bash
pwd                 # 현재 위치 출력
ls                  # 파일 목록
cd /tmp             # 디렉터리 이동
mkdir practice      # 디렉터리 만들기
cp source.txt copy.txt
mv old.txt new.txt
```

삭제 명령은 되돌리기 어렵다. `rm`을 쓰기 전에는 항상 `pwd`와 `ls`로 경로를 확인한다.

## 복잡도 (Complexity)

명령 자체의 비용은 수행하는 프로그램에 따라 다르다. 파일 목록은 디렉터리 크기에, 복사는 파일 크기와 디스크 속도에, 검색은 탐색 범위에 영향을 받는다.

## 응용 (Applications)

- 서버 접속 후 상태 확인
- 파일 이동·복사·압축
- 로그 검색과 간단한 필터링
- 스크립트 자동화의 기반

## 흔한 오해 (Common Misunderstandings)

- `.`은 현재 디렉터리, `..`은 부모 디렉터리다.
- `~`는 보통 현재 사용자의 홈 디렉터리를 뜻한다.
- 명령이 조용히 끝났다고 실패하지 않았다는 뜻은 아니다. 종료 코드와 오류 출력을 확인해야 한다.
- 인터넷에서 본 명령을 의미 없이 붙여 넣으면 위험하다.

## TMI

- `man command`는 매뉴얼을 여는 전통적 방법이다.
- `history`는 이전 명령을 보여 주지만 비밀값을 명령에 직접 쓰면 기록될 수 있다.
- Tab completion은 경로 오타를 크게 줄여 준다.

## 연습 / 확인 문제 (Exercises)

- 홈 디렉터리 아래 실습 디렉터리를 만들고 그 안에서 `pwd`, `ls`를 실행해 보라.
- 상대 경로와 절대 경로 예시를 각각 작성하라.
- 위험해 보이는 명령을 실행하기 전 확인해야 할 질문 3가지를 적어라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](../Processes-and-Threads.md)
- 다음: [파일 시스템](Linux-File-System.md), [사용자와 권한](Linux-Users-Permissions.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md)
- [Reference/Books.md](../../../Reference/Books.md)
