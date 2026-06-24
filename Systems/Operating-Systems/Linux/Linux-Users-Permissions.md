# Linux 사용자와 권한 (Users and Permissions)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Linux/Linux-File-System.md](Linux-File-System.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Linux 권한 모델은 사용자(user), 그룹(group), 기타 사용자(other)에 대해 읽기(read), 쓰기(write), 실행(execute) 권한을 관리한다. 소유자와 권한은 파일 접근을 제어하는 기본 보안 경계다.

## 직관 (Intuition)

파일마다 "주인", "주인의 팀", "그 밖의 사람"에게 각각 무엇을 허용할지 붙어 있다. 서버 운영에서는 누가 어떤 파일을 읽고 실행할 수 있는지 명확해야 사고를 줄인다.

## 이론 (Theory)

권한은 `rwx`로 표현된다. 파일에서 `x`는 실행 가능함을, 디렉터리에서 `x`는 그 디렉터리 안으로 접근할 수 있음을 뜻한다. `chmod`는 권한을, `chown`은 소유자를 바꾼다. `sudo`는 허가된 사용자가 특정 명령을 높은 권한으로 실행하게 한다.

특수 권한으로 setuid, setgid, sticky bit가 있다. `/tmp`에 sticky bit가 설정되어 있으면 다른 사용자의 파일을 임의로 지우기 어렵다.

## 구현 (Implementation)

```bash
ls -l
chmod u+x script.sh
chmod go-r secret.txt
groups
sudo systemctl status ssh
```

권한을 넓히기보다 필요한 최소 권한만 부여하는 습관이 중요하다.

## 복잡도 (Complexity)

권한 계산 자체는 단순하지만, 사용자·그룹·서비스 계정·컨테이너·마운트 옵션이 섞이면 실제 접근 가능성을 추적하기 어려워진다.

## 응용 (Applications)

- 실행 스크립트 권한 설정
- 로그·설정 파일 접근 제어
- 서비스 계정 분리
- sudo 권한 관리

## 흔한 오해 (Common Misunderstandings)

- `chmod 777`은 빠른 해결책처럼 보이지만 보안상 매우 위험하다.
- 디렉터리의 write 권한은 그 안의 파일 생성·삭제에 영향을 준다.
- root는 강력하지만 실수도 강력하게 만든다.
- 권한 오류를 무조건 sudo로 해결하면 원인을 숨길 수 있다.

## TMI

- Numeric mode `755`는 owner `rwx`, group `rx`, other `rx`를 뜻한다.
- `umask`는 새 파일의 기본 권한을 제한한다.
- Capability는 root 권한을 더 잘게 나눠 부여하는 Linux 기능이다.

## 연습 / 확인 문제 (Exercises)

- `rw-r--r--` 권한을 user/group/other 기준으로 해석하라.
- 디렉터리 execute 권한이 없으면 어떤 일이 생기는지 설명하라.
- 서비스 계정을 root와 분리해야 하는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [파일 시스템](Linux-File-System.md)
- 다음: [프로세스와 서비스](Linux-Processes-and-Services.md)

## 참조 (References)

- [Engineering/Security/Auth.md](../../../Engineering/Security/Auth.md)
- [Reference/Books.md](../../../Reference/Books.md)
