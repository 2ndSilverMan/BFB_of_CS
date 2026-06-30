# Git 내부 구조 (Git Internals)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Git/Git-Basics.md](Git/Git-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Git 내부 구조는 blob, tree, commit, tag object와 ref, index, packfile로 이루어진 content-addressed object database다.

## 직관 (Intuition)

Git 저장소는 파일별 변경분 상자라기보다 스냅샷 조각들을 해시 주소로 보관하는 창고다. branch는 그 창고 안 특정 commit을 가리키는 이름표다.

## 이론 (Theory)

Blob은 파일 내용, tree는 directory 구조, commit은 tree와 parent·author·message를 가리킨다. Ref는 branch와 tag 이름을 commit hash에 매핑한다. Loose object가 많아지면 packfile로 압축해 저장한다. Index는 다음 commit에 들어갈 tree를 준비하는 staging structure다.

### 객체 모델로 사고하기

Git의 commit은 snapshot을 가리키는 객체이고, branch는 commit을 가리키는 이동 가능한 ref다. 이 모델을 이해하면 reset, rebase, merge, reflog가 훨씬 덜 무섭다. 대부분의 "사라진 변경"은 객체가 즉시 지워진 것이 아니라 ref에서 도달하지 못하게 된 상태다.

위험한 작업 전에는 현재 ref와 작업 트리 상태를 기록한다. Reflog는 로컬 안전망이지만 영구 백업은 아니다.

## 구현 (Implementation)

```bash
git cat-file -t HEAD
git cat-file -p HEAD
git ls-tree HEAD
git rev-parse HEAD
```

위 명령은 porcelain 명령 뒤에 있는 object model을 직접 보여 준다.

## 복잡도 (Complexity)

Object 조회는 hash 기반이라 빠르지만, history traversal은 commit graph 크기와 path filtering에 좌우된다. Packfile 최적화는 저장 공간과 network transfer를 줄인다.

## 응용 (Applications)

- 이력 복구와 reflog 이해
- shallow clone·partial clone 판단
- repository size 최적화
- merge/rebase 동작 이해

## 흔한 오해 (Common Misunderstandings)

- Git은 단순 diff 목록만 저장하지 않는다.
- branch는 복사본이 아니라 commit을 가리키는 ref다.
- commit hash는 파일 내용만으로 결정되지 않는다.
- packfile은 사용자가 직접 자주 만질 대상이 아니다.

## TMI

- `.git/HEAD`는 현재 branch ref 또는 detached commit을 가리킨다.
- Reflog는 ref 이동 기록이라 “잃어버린 commit”을 찾는 데 유용하다.
- Git의 내부 명령을 plumbing command, 사용자 친화 명령을 porcelain command라고 부른다.

## 연습 / 확인 문제 (Exercises)

- `git cat-file`로 commit, tree, blob을 각각 확인하라.
- branch 이름 파일이 어떤 hash를 담는지 찾아라.
- `git gc`가 왜 필요한지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Git 학습 트랙](Git/)
- 다음: [CI/CD 원칙](CICD-Principles.md)

## 참조 (References)

- [Engineering/DevOps/Git/Git-Basics.md](Git/Git-Basics.md)
- [Engineering/DevOps/Git/Git-Undoing-Changes.md](Git/Git-Undoing-Changes.md)
