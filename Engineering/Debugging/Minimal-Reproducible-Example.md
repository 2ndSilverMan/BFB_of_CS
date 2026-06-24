# 최소 재현 케이스 (Minimal Reproducible Example)

- Level: Beginner
- Prerequisites: [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

최소 재현 케이스(MRE)는 버그를 일으키는 데 필요한 코드, 입력, 환경만 남긴 작은 예제다. 버그를 설명 가능한 실험 대상으로 바꾸는 첫 단계다.

## 직관 (Intuition)

큰 방에서 잃어버린 바늘을 찾기 어렵다면 가구를 하나씩 치워야 한다. MRE는 버그가 계속 재현되는 가장 작은 방을 만든다.

## 이론 (Theory)

좋은 MRE는 minimal, complete, reproducible해야 한다. 입력, 기대 결과, 실제 결과, 환경, 실행 방법을 포함한다. 줄이는 과정에서 버그가 사라지면 직전에 제거한 요소가 단서다.

## 구현 (Implementation)

```text
환경: Python 3.12, Windows
실행: python repro.py
기대: 총합 6
실제: 총합 5
```

## 복잡도 (Complexity)

최소 재현을 만드는 비용은 dependency 수, 입력 크기, 환경 변수 수에 좌우된다. 줄이는 과정은 반복 실험이지만, 한 번 줄여 두면 원인 분석·리뷰·회귀 테스트 비용을 크게 낮춘다.

## 응용 (Applications)

- 버그 리포트 작성
- 외부 라이브러리 issue 제출
- 레거시 코드 원인 축소
- 회귀 테스트 시작점

## 흔한 오해 (Common Misunderstandings)

- 전체 프로젝트를 zip으로 보내는 것은 MRE가 아니다.
- 최소화 중 버그가 사라지면 실패가 아니라 단서다.
- 환경 정보가 없으면 재현이 안 될 수 있다.
- 민감정보를 그대로 포함하면 안 된다.

## TMI

- Delta debugging은 입력을 체계적으로 줄이는 방법이다.
- MRE를 만들다가 원인을 발견하는 경우가 매우 많다.
- 좋은 MRE는 질문 답변 시간을 크게 줄인다.

## 연습 / 확인 문제 (Exercises)

- 실패하는 테스트를 독립 파일 하나로 줄여라.
- 환경 정보를 포함한 버그 리포트를 작성하라.
- 큰 입력 파일을 절반씩 줄이며 재현 여부를 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [과학적 디버깅](Scientific-Debugging.md)
- 다음: [이분 탐색 디버깅](Bisect-Debugging.md)

## 참조 (References)

- [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- [Reference/Books.md](../../Reference/Books.md)
