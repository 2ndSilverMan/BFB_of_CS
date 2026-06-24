# 이분 매칭 (Bipartite Matching)

- Level: Advanced
- Prerequisites: [Algorithms/Max-Flow.md](Max-Flow.md), [Algorithms/BFS-DFS.md](BFS-DFS.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

이분 매칭은 두 그룹으로 나뉜 정점들 사이에서 서로 겹치지 않는 최대 짝짓기를 찾는 문제다. 작업-사람 배정처럼 "한 사람은 한 작업, 한 작업은 한 사람"인 상황을 모형화한다.

## 직관 (Intuition)

지원자와 일자리가 있고, 각 지원자가 할 수 있는 일이 정해져 있다. 최대한 많은 짝을 맺으려면, 이미 짝지어진 것을 살짝 재배치(증가 경로)해 빈자리를 만든다. "내가 들어가면 밀려난 사람이 다른 자리로 갈 수 있는가"를 따라가는 것이 핵심이다.

## 이론 (Theory)

이분 그래프 $G=(L\cup R, E)$에서 매칭은 끝점을 공유하지 않는 간선 집합이다. **증가 경로(augmenting path)**는 매칭/비매칭 간선이 번갈아 나오며 양 끝이 미매칭인 경로다. 이런 경로를 찾아 뒤집으면 매칭 크기가 1 늘어난다(쾨니그-베르주 정리).

최대 유량으로 환원: source→$L$, $R$→sink에 용량 1을 주면 최대 유량 = 최대 매칭. **쾨니그 정리**: 이분 그래프에서 최대 매칭 = 최소 정점 덮개. **홀의 결혼 정리**는 완전 매칭 존재 조건을 준다.

## 구현 (Implementation)

```python
def hungarian(adj, n_left, n_right):       # 헝가리안(증가 경로) 매칭
    match_r = [-1] * n_right
    def try_kuhn(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_r[v] == -1 or try_kuhn(match_r[v], visited):
                    match_r[v] = u          # 증가 경로 발견 → 재배치
                    return True
        return False
    result = 0
    for u in range(n_left):
        if try_kuhn(u, [False]*n_right):
            result += 1
    return result
```

## 복잡도 (Complexity)

| 알고리즘 | 시간 |
|---|---|
| 쿤(증가 경로) | `O(V·E)` |
| Hopcroft-Karp | `O(E√V)` |

쿤 알고리즘은 단순하고 작은 그래프에 충분하다. Hopcroft-Karp는 여러 증가 경로를 동시에 찾아 더 빠르며, 디닉을 단위 용량에 적용한 것과 같은 경계다.

## 응용 (Applications)

- 작업·자원 배정, 시간표 작성
- 네트워크 스위치 스케줄링
- 이미지의 특징점 대응
- 최소 정점 덮개·최대 독립 집합(이분)

## 흔한 오해 (Common Misunderstandings)

- 탐욕적 매칭은 최적이 아니다. 증가 경로로 재배치해야 한다.
- 이분이 아닌 일반 그래프 매칭은 훨씬 어렵다(Blossom 알고리즘 필요).
- 최대 매칭은 유일하지 않을 수 있다.
- 가중치가 있으면 단순 매칭이 아니라 할당 문제(헝가리안/MCMF)가 된다.

## TMI

- "헝가리안 알고리즘"이라는 이름은 König·Egerváry 두 헝가리 수학자의 결과에서 비롯됐다.
- 일반 그래프의 매칭은 Edmonds의 Blossom 알고리즘(1965)이 다항 시간임을 처음 보였다.
- 쾨니그 정리는 이분 그래프에서 NP-난해 문제(정점 덮개)가 다항 시간이 되는 드문 사례다.

## 연습 / 확인 문제 (Exercises)

- 작은 이분 그래프에서 증가 경로로 최대 매칭을 구하라.
- 최대 매칭과 최소 정점 덮개가 같음을 한 예로 확인하라(쾨니그).
- 매칭을 최대 유량으로 환원하는 그래프를 그려라.

## 이어서 읽기 (Reading Path)

- 이전: [Dinic's Algorithm](Dinic.md)
- 다음: [최소 비용 최대 유량 (MCMF)](MCMF.md)

## 참조 (References)

- [Algorithms/Max-Flow.md](Max-Flow.md)
- [Algorithms/Dinic.md](Dinic.md)
- [Reference/Books.md](../Reference/Books.md)
