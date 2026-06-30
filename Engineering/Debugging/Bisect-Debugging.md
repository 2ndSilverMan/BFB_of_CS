# 이분 탐색 디버깅 (Bisect Debugging)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Minimal-Reproducible-Example.md](Minimal-Reproducible-Example.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

이분 탐색 디버깅은 버그가 있는 범위를 절반씩 줄여 원인 commit, 입력, 설정, 파이프라인 단계를 찾는 방법이다. `git bisect`가 대표 도구다.

## 직관 (Intuition)

100개의 변경 중 어느 하나가 문제라면 하나씩 보는 대신 중간을 검사해 앞쪽인지 뒤쪽인지 나눈다. 잘 나누면 훨씬 적은 실험으로 원인을 찾는다.

## 이론 (Theory)

후보가 정렬되어 있고 good/bad 판정이 가능하면 `O(log n)` 실험으로 원인을 찾을 수 있다. 판정이 flaky하면 잘못된 방향으로 갈 수 있어 재현 안정성이 중요하다.

### 좋은 판정 함수

Bisect의 품질은 각 지점을 good/bad로 안정적으로 분류하는 판정 함수에 달려 있다. Flaky test나 환경 의존 결과가 있으면 잘못된 반쪽을 버릴 수 있다. 판정 스크립트는 deterministic해야 하고, 필요하면 같은 지점을 여러 번 실행해 신뢰도를 높인다.

Commit bisect뿐 아니라 config, dependency version, feature flag, input size, pipeline stage에도 같은 이분 탐색 사고를 적용할 수 있다.

## 구현 (Implementation)

```bash
git bisect start
git bisect bad
git bisect good v1.2.0
# 각 단계에서 테스트 실행 후 good/bad 표시
```

## 복잡도 (Complexity)

후보가 $n$개이고 good/bad 판정이 안정적이면 원인 위치를 `O(log n)`번의 실험으로 좁힐 수 있다. 한 번의 판정 비용은 build·test·재현 시간에 좌우되며, flaky test가 있으면 반복 검증 비용이 추가된다.

## 응용 (Applications)

- 회귀 commit 찾기
- 설정 옵션 원인 축소
- 입력 데이터 최소화
- 배포 단계별 장애 지점 찾기

## 흔한 오해 (Common Misunderstandings)

- 테스트 판정이 불안정하면 bisect 결과도 불안정하다.
- 여러 버그가 섞이면 단일 경계가 아닐 수 있다.
- 중간 commit이 빌드되지 않으면 skip이 필요하다.
- Bisect는 원인 위치를 좁힐 뿐 수정 방법을 자동으로 주지 않는다.

## TMI

- `git bisect run`은 판정 스크립트를 자동 실행한다.
- 입력 파일도 절반씩 줄이는 delta debugging을 적용할 수 있다.
- 로그 양을 절반씩 줄이는 것도 유용한 전략이다.

## 연습 / 확인 문제 (Exercises)

- 간단한 repo에서 의도적 버그 commit을 만들고 bisect로 찾아라.
- Flaky test가 bisect에 주는 영향을 설명하라.
- 입력 데이터 bisect 절차를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [최소 재현 케이스](Minimal-Reproducible-Example.md)
- 다음: [중단점과 스텝 실행](Breakpoints-and-Stepping.md)

## 참조 (References)

- [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- [Reference/Books.md](../../Reference/Books.md)
