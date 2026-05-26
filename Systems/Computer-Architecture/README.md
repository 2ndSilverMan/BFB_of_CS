# 컴퓨터 구조 (Computer Architecture)

> 트랜지스터에서 CPU까지 — 컴퓨터의 물리적 작동 원리.

**선수지식**: 이진수, 기본 논리 회로

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 디지털 논리 (게이트, 회로) | Digital-Logic.md | Planned |
| 데이터 표현 (이진수, 부동소수점) | Data-Representation.md | Planned |
| CPU 구조와 명령어 집합 (ISA) | CPU-and-ISA.md | Planned |
| 파이프라이닝 | Pipelining.md | Planned |
| 메모리 계층 (레지스터, 캐시, RAM) | Memory-Hierarchy.md | Planned |
| 가상 메모리 | Virtual-Memory-Hardware.md | Planned |
| 입출력 (I/O) 시스템 | IO-Systems.md | Planned |
| 병렬 아키텍처 (멀티코어, GPU) | Parallel-Architecture.md | Planned |

---

## 학습 순서

```text
Digital-Logic → Data-Representation → CPU-and-ISA → Pipelining
        ↓
Memory-Hierarchy → Virtual-Memory-Hardware
        ↓
IO-Systems → Parallel-Architecture
```

---

## 연관 섹션

- [Systems/Operating-Systems/](../Operating-Systems/) — 하드웨어 자원을 운영체제가 추상화하고 관리
- [Systems/Parallel-Computing/](../Parallel-Computing/) — 멀티코어, SIMD, GPU 구조의 활용
- [Engineering/Performance/](../../Engineering/Performance/) — 캐시, 메모리 계층, CPU 병목 분석
