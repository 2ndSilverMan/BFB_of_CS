# Linux 파일 시스템 (Linux File System)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/File-Systems.md](../File-Systems.md), [Systems/Operating-Systems/Linux/Linux-Shell-Basics.md](Linux-Shell-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Linux 파일 시스템은 디렉터리 트리 하나 아래에 파일, 디렉터리, 장치, 마운트 지점을 배치한다. 루트 디렉터리 `/`에서 시작해 `/home`, `/etc`, `/var`, `/usr`, `/tmp` 같은 표준 위치가 있다.

## 직관 (Intuition)

Windows의 드라이브 문자 여러 개보다, Linux는 하나의 큰 나무에 다른 디스크나 네트워크 저장소를 가지처럼 붙이는 방식에 가깝다. 이 붙이는 작업이 mount다.

## 이론 (Theory)

파일은 이름과 데이터뿐 아니라 inode, 권한, 소유자, timestamp 같은 metadata를 가진다. Directory는 이름을 inode에 매핑하는 특별한 파일이다. Mount는 다른 파일 시스템을 기존 디렉터리 경로에 연결한다.

일반적 경로 의미는 다음과 같다.

- `/etc`: 시스템 설정
- `/var`: 변하는 데이터, 로그, spool
- `/home`: 사용자 홈
- `/tmp`: 임시 파일
- `/proc`: 커널이 제공하는 프로세스·시스템 정보

## 구현 (Implementation)

```bash
pwd
ls -la
du -sh .
df -h
find . -name "*.log"
```

`du`는 디렉터리 사용량, `df`는 파일 시스템 여유 공간을 보는 데 자주 쓴다.

## 복잡도 (Complexity)

큰 디렉터리에서 recursive scan은 파일 수에 비례해 느려진다. 네트워크 파일 시스템이나 느린 디스크에서는 metadata 조회도 병목이 될 수 있다.

## 응용 (Applications)

- 디스크 사용량 조사
- 설정 파일 위치 찾기
- 로그와 임시 파일 정리
- 마운트 문제 진단

## 흔한 오해 (Common Misunderstandings)

- `/root`는 루트 디렉터리가 아니라 root 사용자의 홈 디렉터리다.
- 파일 확장자가 실행 가능 여부를 결정하지 않는다. 권한과 shebang이 중요하다.
- 삭제한 파일도 프로세스가 열고 있으면 공간이 바로 회수되지 않을 수 있다.
- `/proc`의 파일들은 실제 디스크 파일이 아니라 kernel interface다.

## TMI

- Hard link는 같은 inode를 여러 이름으로 가리키게 한다.
- Symbolic link는 다른 경로를 가리키는 별도 파일이다.
- `lsof`는 어떤 프로세스가 파일을 열고 있는지 볼 때 유용하다.

## 연습 / 확인 문제 (Exercises)

- `/etc`, `/var/log`, `/tmp`, `/home`의 역할을 설명하라.
- `du`와 `df`의 차이를 말하라.
- symbolic link와 hard link의 차이를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [셸과 기본 명령](Linux-Shell-Basics.md), [파일 시스템 이론](../File-Systems.md)
- 다음: [사용자와 권한](Linux-Users-Permissions.md)

## 참조 (References)

- [Systems/Operating-Systems/File-Systems.md](../File-Systems.md)
- [Reference/Books.md](../../../Reference/Books.md)
