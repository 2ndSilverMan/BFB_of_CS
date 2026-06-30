# 뮤테이션 테스트 (Mutation Testing)

- Level: Advanced
- Prerequisites: [Engineering/Testing/Code-Coverage.md](Code-Coverage.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

뮤테이션 테스트는 코드에 작은 변형(mutant)을 넣고 테스트가 그 변형을 잡아내는지 확인해 테스트 suite의 결함 탐지력을 측정한다.

## 직관 (Intuition)

테스트가 코드를 지나가기만 하는지, 실제로 틀린 행동을 잡는지 보려면 일부러 작은 버그를 심어 보면 된다. 좋은 테스트는 그 버그를 실패로 만든다.

## 이론 (Theory)

Mutation operator는 `>`를 `>=`로 바꾸거나, 조건을 뒤집거나, 반환값을 바꾸는 식이다. 테스트가 mutant를 실패시키면 killed, 통과하면 survived다. Mutation score는 killed mutant 비율이다.

### Mutation score가 말하는 것

Mutation testing은 코드에 작은 결함을 주입했을 때 테스트가 실패하는지 본다. 살아남은 mutant는 테스트가 실행은 했지만 의미 있는 assertion을 하지 않았거나, 해당 동작이 실제 contract가 아니라는 신호일 수 있다.

모든 mutant를 죽이는 것이 목표는 아니다. Equivalent mutant나 의미 없는 변형은 제외해야 한다. 비용이 크므로 core domain logic, security-sensitive code, 돈/권한/상태 전환 로직에 우선 적용한다.

## 구현 (Implementation)

```text
original: if age >= 18
mutant:   if age > 18
```

이 mutant를 죽이려면 age=18 경계값 테스트가 필요하다.

## 복잡도 (Complexity)

Mutant마다 테스트를 실행하므로 비용이 크다. Incremental mutation, selective mutation, 병렬화가 필요할 수 있다.

## 응용 (Applications)

- 테스트 assertion 품질 평가
- 핵심 도메인 로직 검증 강화
- 커버리지 숫자의 한계 보완
- 레거시 테스트 suite 개선

## 흔한 오해 (Common Misunderstandings)

- Mutation score 100%가 완벽한 테스트를 의미하지 않는다.
- Equivalent mutant는 실제로 행동 차이가 없어 죽일 수 없다.
- 모든 프로젝트에 전체 mutation testing을 매번 돌릴 필요는 없다.
- 느린 테스트 suite에서는 비용이 매우 커질 수 있다.

## TMI

- Mutation testing은 경계값 테스트의 중요성을 잘 드러낸다.
- Survived mutant는 테스트 추가 후보를 알려 준다.
- CI에서는 변경된 파일에만 제한적으로 적용하기도 한다.

## 연습 / 확인 문제 (Exercises)

- 나이 조건식에 mutation을 만들고 죽일 테스트를 작성하라.
- Equivalent mutant 예시를 설명하라.
- Mutation testing을 CI에 넣는 전략을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [코드 커버리지](Code-Coverage.md)
- 다음: [정적 분석과 린터](Static-Analysis-Linting.md)

## 참조 (References)

- [Engineering/Testing/Code-Coverage.md](Code-Coverage.md)
- [Reference/Books.md](../../Reference/Books.md)
