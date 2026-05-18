# 운영체제 (Operating Systems)

> 선수 지식 → 난이도 순 정렬.

## 1. 프로세스 & 스레드 (선수 지식: 컴퓨터 구조)

| # | 주제 | 파일 |
|---|------|------|
| 1 | 프로세스와 스레드 (Process & Thread) | [Process-and-Thread.md](Process-and-Thread.md) |
| 2 | 프로세스 제어 블록 (PCB) | [PCB.md](PCB.md) |
| 3 | 컨텍스트 스위칭 (Context Switching) | [Context-Switching.md](Context-Switching.md) |
| 4 | 스레드 모델 (User-Level vs Kernel-Level) | [Thread-Models.md](Thread-Models.md) |
| 5 | 코루틴 & 그린 스레드 (Coroutines) | [Coroutines.md](Coroutines.md) |

## 2. CPU 스케줄링 (선수 지식: 프로세스)

| # | 주제 | 파일 |
|---|------|------|
| 6 | 스케줄링 알고리즘 (FCFS, SJF, RR, Priority) | [CPU-Scheduling.md](CPU-Scheduling.md) |
| 7 | 다중 레벨 큐 스케줄링 | [Multilevel-Queue.md](Multilevel-Queue.md) |
| 8 | 다중 프로세서 스케줄링 | [Multi-Processor-Scheduling.md](Multi-Processor-Scheduling.md) |
| 9 | 실시간 스케줄링 (EDF, RMS) | [Realtime-Scheduling.md](Realtime-Scheduling.md) |

## 3. 동기화 (선수 지식: 프로세스 & 스레드)

| # | 주제 | 파일 |
|---|------|------|
| 10 | 임계 구역 문제 (Critical Section) | [Critical-Section.md](Critical-Section.md) |
| 11 | 뮤텍스 & 세마포어 | [Mutex-Semaphore.md](Mutex-Semaphore.md) |
| 12 | 모니터 & 조건 변수 (Monitor & Condition Variables) | [Monitor.md](Monitor.md) |
| 13 | 교착 상태 (Deadlock) | [Deadlock.md](Deadlock.md) |
| 14 | 라이브락 & 기아 (Livelock & Starvation) | [Livelock-Starvation.md](Livelock-Starvation.md) |
| 15 | 락-프리 동기화 (Lock-Free / Wait-Free) | [Lock-Free-Sync.md](Lock-Free-Sync.md) |

## 4. 메모리 관리 (선수 지식: 컴퓨터 구조, 프로세스)

| # | 주제 | 파일 |
|---|------|------|
| 16 | 메모리 할당 (Contiguous Allocation) | [Memory-Allocation.md](Memory-Allocation.md) |
| 17 | 페이징 (Paging) | [Paging.md](Paging.md) |
| 18 | 세그멘테이션 (Segmentation) | [Segmentation.md](Segmentation.md) |
| 19 | 가상 메모리 (Virtual Memory) | [Virtual-Memory.md](Virtual-Memory.md) |
| 20 | TLB & 페이지 테이블 구조 | [TLB.md](TLB.md) |
| 21 | 페이지 교체 알고리즘 (Page Replacement) | [Page-Replacement.md](Page-Replacement.md) |
| 22 | 메모리 매핑 (mmap) | [Memory-Mapping.md](Memory-Mapping.md) |
| 23 | 가비지 컬렉션 (Garbage Collection) | [Garbage-Collection.md](Garbage-Collection.md) |

## 5. 파일 시스템 (선수 지식: 메모리 관리, 디스크 구조)

| # | 주제 | 파일 |
|---|------|------|
| 24 | 파일 시스템 구조 (File System Structures) | [File-System.md](File-System.md) |
| 25 | 디렉토리 구현 (Directory Implementation) | [Directory.md](Directory.md) |
| 26 | 저널링 파일 시스템 (Journaling) | [Journaling.md](Journaling.md) |
| 27 | 로그 구조 파일 시스템 (LFS) | [LFS.md](LFS.md) |
| 28 | 분산 파일 시스템 (NFS, AFS) | [Distributed-FS.md](Distributed-FS.md) |

## 6. I/O (선수 지식: CPU, 메모리, 프로세스)

| # | 주제 | 파일 |
|---|------|------|
| 29 | I/O 모델 (Blocking, Non-blocking, Async, io_uring) | [IO-Models.md](IO-Models.md) |

## 7. 고급 운영체제 (선수 지식: 1~6 전반)

| # | 주제 | 파일 |
|---|------|------|
| 30 | 보호 모델 & 접근 제어 (Protection Models) | [Protection-Models.md](Protection-Models.md) |
| 31 | 마이크로커널 & 엑소커널 | [Microkernel.md](Microkernel.md) |
| 32 | 가상화 & 하이퍼바이저 (Virtualization) | [Virtualization.md](Virtualization.md) |
| 33 | 컨테이너 기술 (Containers, cgroups, namespaces) | [Containers.md](Containers.md) |
| 34 | 실시간 운영체제 (RTOS) | [RTOS.md](RTOS.md) |
