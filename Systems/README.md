# 컴퓨터 시스템 (Systems)

> 컴퓨터가 실제로 어떻게 동작하는가 — 하드웨어부터 분산 시스템까지.

**선수지식**: [Programming/](../Programming/), [Math/Discrete/](../Math/Discrete/)

---

## 현재 가용성

현재 이 섹션은 시스템 학습 범위와 순서를 보여주는 주제 지도다. 개별 본문은 대부분 `Planned` 상태이므로, 각 하위 README에서 `Draft` 이상으로 열린 항목부터 읽는다.

---

## 서브섹션

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [Computer-Architecture/](Computer-Architecture/) | CPU, 메모리 계층, 캐시, 파이프라이닝 | [Math/Discrete/](../Math/Discrete/) (기초) |
| [Operating-Systems/](Operating-Systems/) | 프로세스, 스레드, 메모리 관리, 파일 시스템 | [Systems/Computer-Architecture/](Computer-Architecture/) |
| [Parallel-Computing/](Parallel-Computing/) | 스레드, 동기화, SIMD, GPU 컴퓨팅 | [Systems/Operating-Systems/](Operating-Systems/), [Systems/Computer-Architecture/](Computer-Architecture/) |
| [Networks/](Networks/) | TCP/IP, HTTP, DNS, 라우팅, 소켓 프로그래밍 | [Systems/Operating-Systems/](Operating-Systems/) (기초) |
| [Databases/](Databases/) | 관계형 DB, SQL, 트랜잭션, 인덱스, NoSQL | [Data-Structures/](../Data-Structures/) |
| [Distributed-Systems/](Distributed-Systems/) | 분산 합의, CAP 정리, 복제, 일관성 | [Systems/Operating-Systems/](Operating-Systems/), [Systems/Networks/](Networks/), [Systems/Databases/](Databases/) |

---

## 학습 순서

```text
Computer-Architecture
        ↓
  Operating-Systems
     ↙     ↘
Parallel  Networks  →  Databases
                          ↓
                  Distributed-Systems
```

---

## 연관 섹션

- [CS-Theory/](../CS-Theory/) — 계산 모델, 언어론 (이론적 기반)
- [Engineering/Performance/](../Engineering/Performance/) — 시스템 지식을 바탕으로 한 성능 분석
- [Engineering/](../Engineering/) — 시스템 설계, DevOps (실무 적용)
- [AI/MLOps/](../AI/MLOps/) — 분산 학습, 모델 서빙 인프라
