# 조건문과 반복문 (Control Flow)

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](Variables-and-Types.md)
- Status: Draft

---

## 개념 (Concept)

제어 흐름은 프로그램의 실행 순서를 정하는 방법이다. 조건문은 어떤 조건이 참일 때만 특정 코드를 실행하고, 반복문은 같은 작업을 여러 번 실행한다.

## 직관 (Intuition)

프로그램이 항상 위에서 아래로 한 번만 실행된다면 할 수 있는 일이 매우 제한된다. 조건문은 갈림길이고, 반복문은 되풀이 작업을 자동화하는 장치다.

- 조건문: "비밀번호가 맞으면 로그인한다."
- 반복문: "목록에 있는 모든 점수를 더한다."
- 조기 종료: "원하는 값을 찾으면 더 찾지 않는다."

## 이론 (Theory)

조건문은 불리언 표현식을 기준으로 분기한다.

```text
if 조건:
    조건이 참일 때 실행
else:
    조건이 거짓일 때 실행
```

반복문은 보통 두 종류로 나뉜다.

| 종류 | 쓰임 |
|---|---|
| for 반복문 | 정해진 범위나 컬렉션을 순회 |
| while 반복문 | 조건이 참인 동안 계속 반복 |

반복문에는 종료 조건이 있어야 한다. 종료 조건이 없거나 갱신이 잘못되면 무한 루프가 된다.

## 구현 (Implementation)

조건문 예시:

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C or below"

print(grade)
```

반복문 예시:

```python
scores = [90, 85, 100]
total = 0

for score in scores:
    total += score

average = total / len(scores)
print(average)
```

`while`은 반복 횟수가 미리 정해지지 않았을 때 유용하다.

```python
n = 16
steps = 0

while n > 1:
    n //= 2
    steps += 1

print(steps)
```

## 복잡도 (Complexity)

| 구조 | 시간 | 공간 |
|---|---|---|
| 단일 조건문 | O(1) | O(1) |
| 길이 n 목록 한 번 순회 | O(n) | O(1) |
| 이중 반복문으로 n x n 순회 | O(n^2) | O(1) |

반복문 개수만 세는 것보다 각 반복문이 몇 번 실행되는지를 계산하는 것이 중요하다.

## 응용 (Applications)

- 입력값 검증
- 목록 검색과 필터링
- 누적합, 최댓값, 최솟값 계산
- 시뮬레이션과 게임 루프
- 알고리즘의 기본 골격 구성

## 흔한 오해 (Common Misunderstandings)

- `if`가 여러 개 있는 것과 `if / elif / else`는 다르다. 전자는 조건을 각각 검사하고, 후자는 한 분기만 선택한다.
- 반복문 안에서 제어 변수를 갱신하지 않으면 무한 루프가 될 수 있다.
- `break`는 반복문 전체를 끝내고, `continue`는 현재 반복만 건너뛴다.
- 중첩 반복문이 항상 O(n^2)은 아니다. 각 루프의 반복 횟수를 따로 봐야 한다.

## 연습 / 확인 문제 (Exercises)

- 1부터 100까지의 정수 중 짝수만 출력하라.
- 주어진 점수 목록에서 최댓값과 평균을 구하라.
- 숫자 목록에서 처음으로 음수가 나오는 위치를 찾고, 없으면 `-1`을 출력하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](Variables-and-Types.md)
- 다음: [함수와 재귀](Functions-and-Recursion.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](Variables-and-Types.md)
- [Algorithms/Complexity.md](../Algorithms/Complexity.md)
