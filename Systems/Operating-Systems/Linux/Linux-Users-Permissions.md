# Linux 사용자와 권한 (Users and Permissions)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Linux/Linux-File-System.md](Linux-File-System.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Linux 권한은 파일마다 **소유자(user)·그룹(group)·기타(other)** 에 대해 **읽기(r)·쓰기(w)·실행(x)** 을 정한다. 소유자·권한 비트가 파일 접근의 1차 보안 경계이며, inode에 저장된다.

## 직관 (Intuition)

파일마다 "주인 / 주인의 팀 / 그 밖의 사람"에게 각각 무엇을 허용할지 붙어 있다. 서버 운영에선 **최소 권한**(필요한 만큼만)이 사고를 줄이는 핵심 원칙이다.

## 이론 (Theory)

### 1. rwx와 8진수

각 권한은 비트: **r=4, w=2, x=1**. 세 묶음(user/group/other)이 3자리 8진수가 된다.

$$\texttt{755} = \underbrace{7}_{rwx}\,\underbrace{5}_{r-x}\,\underbrace{5}_{r-x},\qquad \texttt{644}=rw\text{-}\,r\text{--}\,r\text{--}$$

### 2. 파일 vs 디렉터리의 x

- 파일 `x`: 실행 가능.
- **디렉터리 `x`: 그 안으로 "통과(traverse)"** 가능 — `x` 없으면 `r`이 있어도 안의 파일에 접근 못 한다(이름만 나열 가능/불가).

### 3. 특수 비트와 umask

- **setuid/setgid**: 실행 시 파일 소유자/그룹 권한으로 동작(`passwd` 가 대표).
- **sticky bit**: `/tmp` 처럼 공유 디렉터리에서 **자기 파일만 삭제** 가능하게.
- **umask**: 새 파일 기본 권한을 *제한*. `umask 022` → 새 파일 `666 & ~022 = 644`, 새 디렉터리 `777 & ~022 = 755`.

## 구현 (Implementation)

```bash
ls -l script.sh            # -rwxr-xr-x  → 755
chmod u+x script.sh        # 소유자에 실행 추가(심볼릭)
chmod 640 secret.txt       # rw-r----- (소유자 rw, 그룹 r, 기타 없음)
chown alice:devs file      # 소유자/그룹 변경
sudo systemctl status ssh  # 허가된 사용자만 상승 권한
```

**워크드 예제(umask).** `umask 027` 하에서 새 파일 생성 → `666 & ~027 = 666 & 750 = 640`(rw-r-----), 새 디렉터리 → `777 & ~027 = 750`(rwxr-x---). 그래서 기본적으로 "기타"는 접근 불가.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 권한 계산 | 단순(비트 AND) |
| 실제 접근 추적 | user·group·서비스 계정·ACL·컨테이너·mount 옵션이 겹치면 복잡 |

## 응용 (Applications)

- 실행 스크립트 권한, 로그·설정 파일 접근 제어.
- 서비스 계정 분리(root와 격리), sudo 권한 관리([인증](../../../Engineering/Security/Auth.md)).

## 흔한 오해 (Common Misunderstandings)

- **`chmod 777` 은 빠른 해결처럼 보이나 매우 위험** — 누구나 쓰기/실행.
- **디렉터리 `x` 없으면** 안의 파일에 경로로 접근 불가(r만으로 부족).
- **root는 강력하지만 실수도 강력** — 일상은 일반 계정 + sudo.
- **권한 오류를 무조건 sudo로 덮으면** 원인을 숨긴다.

## TMI

- 8진수 모드 `4755`(맨 앞 4)는 setuid + 755 — 잘못 쓰면 권한 상승 취약점.
- **capability** 는 root 권한을 잘게 쪼개 부여한다(예: `CAP_NET_BIND_SERVICE` 만으로 80포트 바인딩).
- POSIX ACL(`setfacl`)은 기본 rwx보다 세밀한 사용자별 권한을 준다.

## 연습 / 확인 문제 (Exercises)

- `rw-r--r--` 를 8진수로, `750` 을 rwx로 변환하라.
- 디렉터리 `x` 권한이 없을 때 안의 파일 접근이 왜 막히는지 설명하라.
- `umask 022` 와 `umask 077` 에서 새 파일 권한을 각각 계산하라.
- sticky bit가 `/tmp` 공유에서 무엇을 막는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Linux 파일 시스템](Linux-File-System.md)
- 다음: [프로세스와 서비스](Linux-Processes-and-Services.md)
- 관련: [인증](../../../Engineering/Security/Auth.md)

## 참조 (References)

- [Engineering/Security/Auth.md](../../../Engineering/Security/Auth.md)
- [Reference/Books.md](../../../Reference/Books.md)
