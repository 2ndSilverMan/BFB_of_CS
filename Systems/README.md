# 컴퓨터 시스템 (Systems)

> 컴퓨터가 실제로 어떻게 동작하는가 — 하드웨어부터 분산 시스템까지.

**선수지식**: [Programming/](../Programming/), [Math/Discrete/](../Math/Discrete/)

---

## 서브섹션

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [Computer-Architecture/](Computer-Architecture/) | CPU, 메모리 계층, 캐시, 파이프라이닝 | 이진수, 논리 회로 |
| [Operating-Systems/](Operating-Systems/) | 프로세스, 스레드, 메모리 관리, 파일 시스템 | 컴퓨터 구조 |
| [Networks/](Networks/) | TCP/IP, HTTP, DNS, 라우팅, 소켓 프로그래밍 | OS 기초 |
| [Databases/](Databases/) | 관계형 DB, SQL, 트랜잭션, 인덱스, NoSQL | 기본 자료구조 |
| [Distributed-Systems/](Distributed-Systems/) | 분산 합의, CAP 정리, 복제, 일관성 | OS, 네트워크, DB |
| [Parallel-Computing/](Parallel-Computing/) | 스레드, 동기화, SIMD, GPU 컴퓨팅 | OS, 컴퓨터 구조 |

---

## 학습 순서

```
Computer-Architecture
        ↓
  Operating-Systems
        ↓
     Networks  →  Databases
        ↓               ↓
  Distributed-Systems ←─┘
        ↑
  Parallel-Computing
```

---

## 연관 섹션

- [CS-Theory/](../CS-Theory/) — 계산 모델, 언어론 (이론적 기반)
- [Engineering/](../Engineering/) — 시스템 설계, DevOps (실무 적용)
- [AI/MLOps/](../AI/MLOps/) — 분산 학습, 모델 서빙 인프라
