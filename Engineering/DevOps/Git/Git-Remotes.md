# 원격 저장소 (Git Remotes)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md](Git-Branches-Merging-Rebasing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

원격 저장소는 네트워크에 있는 Git 저장소다. `fetch`, `pull`, `push`, upstream 설정으로 로컬 이력과 원격 이력을 동기화한다.

## 직관 (Intuition)

로컬 저장소는 내 노트, 원격 저장소는 팀이 함께 보는 게시판이다. 게시판을 먼저 읽고(fetch), 내 변경을 올리고(push), 필요하면 합친다.

## 이론 (Theory)

`origin/main` 같은 remote-tracking branch는 마지막 fetch 시점의 원격 상태를 로컬에 기록한 이름이다. `git fetch`는 원격 정보를 가져오지만 working tree를 바꾸지 않는다. `git pull`은 fetch 후 merge 또는 rebase를 수행한다. Upstream은 현재 branch가 기본으로 추적할 원격 branch를 뜻한다.

## 구현 (Implementation)

```bash
git remote -v
git fetch origin
git switch main
git pull --ff-only
git push -u origin feature/login
```

`--ff-only`는 예기치 않은 merge commit을 만들지 않게 해 초보자에게 안전한 기본값이 될 수 있다.

## 복잡도 (Complexity)

네트워크 비용은 변경 object 수와 repository 크기에 좌우된다. 큰 history와 binary artifact는 clone·fetch 시간을 늘린다.

## 응용 (Applications)

- 팀 작업 공유
- CI/CD trigger
- fork 기반 오픈소스 기여
- backup성 remote mirror 구성

## 흔한 오해 (Common Misunderstandings)

- `fetch`는 작업 파일을 덮어쓰지 않는다.
- `pull`은 단순 다운로드가 아니라 이력 통합 작업이다.
- `origin`은 특별한 서버가 아니라 기본 remote 이름일 뿐이다.
- Force push는 원격 이력을 바꾸므로 범위와 의도를 분명히 해야 한다.

## TMI

- `git push --force-with-lease`는 원격이 내가 아는 상태일 때만 강제 push해 사고를 줄인다.
- Fork와 upstream remote를 함께 쓰면 원본 프로젝트와 내 사본을 분리해 관리할 수 있다.
- Shallow clone은 CI에서 checkout 시간을 줄이는 데 유용하지만 일부 history 작업을 제한한다.

## 연습 / 확인 문제 (Exercises)

- 원격 branch를 fetch한 뒤 local branch를 만들어 추적하라.
- `pull --merge`와 `pull --rebase`의 이력 차이를 비교하라.
- force push가 필요한 상황과 위험한 상황을 구분하라.

## 이어서 읽기 (Reading Path)

- 이전: [브랜치, 머지, 리베이스](Git-Branches-Merging-Rebasing.md)
- 다음: [충돌 해결](Git-Conflict-Resolution.md)

## 참조 (References)

- [GitHub 저장소와 권한](../GitHub/GitHub-Repositories.md)
- [Engineering/DevOps/](../)

