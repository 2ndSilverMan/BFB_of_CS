# 입문자 로드맵 (Beginner Roadmap)

> 프로그래밍과 CS를 처음 시작하는 사람을 위한 순서.

---

## 대상

- 프로그래밍과 CS를 처음 시작하는 학습자

## 현재 가용성

현재 바로 읽을 수 있는 본문은 프로그래밍 기초, 논리, 기본 자료구조, 기본 알고리즘까지의 최소 경로다. 이 경로만으로도 간단한 프로그램 작성, 기본 자료구조 읽기, Big-O와 BFS/DFS의 입문 수준 이해는 가능하다.

아래 전체 로드맵은 최종 목표다. 트리, 해시, 기본 DP, 시스템 맛보기까지 포함한 완료 기준은 아직 `Planned` 문서가 채워져야 닫힌다.

## 순서

현재 바로 읽을 수 있는 본문 경로는 다음 순서다.

1. 프로그래밍 기초
   - [변수와 타입](../Programming/Variables-and-Types.md)
   - [조건문과 반복문](../Programming/Control-Flow.md)
   - [함수와 재귀](../Programming/Functions-and-Recursion.md)
   - [배열과 문자열](../Programming/Arrays-and-Strings.md)
   - [언어 선택 가이드](../Programming/Language-Selection.md)
2. 수학 기초
   - [명제 논리와 술어 논리](../Math/Discrete/Logic.md)
3. 자료구조
   - [배열](../Data-Structures/Array.md)
   - [연결 리스트](../Data-Structures/Linked-List.md)
   - [스택](../Data-Structures/Stack.md)
   - [큐](../Data-Structures/Queue.md)
   - [그래프 표현](../Data-Structures/Graph-Representation.md)
4. 알고리즘
   - [복잡도 분석](../Algorithms/Complexity.md)
   - [정렬](../Algorithms/Sorting.md)
   - [이진 탐색](../Algorithms/Binary-Search.md)
   - [BFS / DFS](../Algorithms/BFS-DFS.md)

방향을 고르기 위한 선택 트랙 목차는 다음과 같다. 아직 대부분 `Planned` 상태이므로, 본문 경로를 보조하는 지도처럼 사용한다.

- [언어별 학습 트랙](../Programming/Languages/)
- [Linux 학습 트랙](../Systems/Operating-Systems/Linux/)
- [Git 학습 트랙](../Engineering/DevOps/Git/)
- [GitHub 학습 트랙](../Engineering/DevOps/GitHub/)

현재 경로를 다 읽은 뒤 최종 완료 기준을 채우려면 다음 예정 주제가 추가로 필요하다.

| 영역 | 예정 보강 주제 |
|---|---|
| 이산수학 | `Induction.md`, `Graph-Theory.md` |
| 자료구조 | `Binary-Tree.md`, `Hash-Table.md` |
| 알고리즘 | `DP-Basics.md` |
| 시스템 맛보기 | `Data-Representation.md`, `Processes-and-Threads.md`, `Network-Models.md`, `Relational-Model-and-SQL.md` |

아래 전체 로드맵은 입문자 과정의 최종 목표다.

### 기초

1. [프로그래밍 기초 (Programming)](../Programming/)
   - 변수, 조건문, 반복문, 함수, 재귀, 언어 선택
2. [이산수학 (Discrete Mathematics)](../Math/Discrete/)
   - 논리, 집합, 귀납법, 그래프 이론 기초

### 자료구조 & 알고리즘

3. [자료구조 (Data Structures)](../Data-Structures/)
   - 배열, 연결 리스트, 스택, 큐, 트리, 해시
4. [알고리즘 (Algorithms)](../Algorithms/)
   - 정렬, 탐색, DP, 그래프 알고리즘

### 시스템

5. [컴퓨터 구조 (Computer Architecture)](../Systems/Computer-Architecture/)
6. [운영체제 (Operating Systems)](../Systems/Operating-Systems/)
7. [컴퓨터 네트워크 (Networks)](../Systems/Networks/)
8. [데이터베이스 (Databases)](../Systems/Databases/)

---

## 현재 경로 완료 기준

현재 링크가 걸린 `Draft` 문서만 읽었을 때의 기준이다.

- 변수, 조건문, 반복문, 함수, 배열/문자열로 간단한 콘솔 프로그램을 작성할 수 있다.
- 학습 목표에 맞는 시작 언어를 고르고, 다음 언어별 트랙이 무엇인지 찾을 수 있다.
- 기본 논리식, 드모르간 법칙, 조건문의 참/거짓 흐름을 코드와 연결해 설명할 수 있다.
- 배열, 연결 리스트, 스택, 큐, 그래프 표현의 기본 차이를 설명할 수 있다.
- Big-O로 단일 순회, 중첩 반복문, 이진 탐색의 시간 복잡도를 설명할 수 있다.
- 정렬된 배열에서 이진 탐색을 구현하고, 그래프를 BFS/DFS로 순회할 수 있다.
- 다음에 채워야 할 주제가 트리, 해시, DP, 시스템 기본 용어라는 점을 알고 있다.

## 최종 완료 기준

입문자 로드맵 전체를 끝냈을 때의 기준이다. 현재 `Draft` 문서만으로는 일부 항목이 아직 충족되지 않는다.

- 간단한 콘솔 프로그램을 함수와 자료구조로 나누어 작성할 수 있다.
- Big-O로 기본 연산의 시간/공간 복잡도를 설명할 수 있다.
- 배열, 연결 리스트, 스택, 큐, 트리, 해시 테이블의 차이를 설명하고 기본 구현을 읽을 수 있다.
- BFS/DFS, 이진 탐색, 정렬, 기본 DP 문제를 풀이할 수 있다.
- 프로세스, 메모리, TCP/IP, SQL 트랜잭션 같은 시스템 기본 용어를 설명할 수 있다.

---

## 다음 단계

- [CS 핵심 로드맵](CS-Core.md)
- [AI 핵심 로드맵](AI-Core.md)
