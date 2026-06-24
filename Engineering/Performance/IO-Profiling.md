# I/O 프로파일링 (I/O Profiling)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/IO-and-Drivers.md](../../Systems/Operating-Systems/IO-and-Drivers.md), [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

I/O 프로파일링은 disk, network, filesystem, database 같은 외부 자원 대기 시간이 latency와 throughput에 미치는 영향을 측정한다.

## 직관 (Intuition)

프로그램이 “느린” 것이 아니라 기다리는 시간이 긴 경우가 많다. CPU가 놀고 있다면 다음 질문은 무엇을 기다리는가다.

## 이론 (Theory)

I/O 병목은 queue depth, service time, wait time, bandwidth, syscall 수, retry, timeout으로 드러난다. Disk는 sequential/random access와 fsync가 중요하고, network는 RTT, packet loss, connection reuse, serialization cost가 중요하다. Off-CPU profiling은 thread가 sleep·block된 stack을 보여 준다.

## 구현 (Implementation)

```python
import time
from pathlib import Path

path = Path("sample.bin")
payload = b"x" * 1024 * 1024

start = time.perf_counter()
path.write_bytes(payload)
elapsed = time.perf_counter() - start

print(f"{len(payload) / elapsed / 1024 / 1024:.1f} MiB/s")
```

## 복잡도 (Complexity)

I/O 시간은 데이터 크기뿐 아니라 요청 수, seek, RTT, queueing에 좌우된다. 작은 요청을 많이 보내면 총 bytes가 작아도 overhead가 커진다.

## 응용 (Applications)

- slow request root cause 분석
- batch size·buffer size 결정
- database round trip 감소
- object storage·CDN 성능 비교

## 흔한 오해 (Common Misunderstandings)

- CPU 사용률이 낮다고 여유 있는 시스템은 아니다.
- local benchmark가 network storage 성능을 대표하지 않는다.
- cache hit 상태의 결과를 cold start 성능으로 일반화하면 안 된다.
- retry storm은 평균 latency보다 tail latency를 먼저 망가뜨린다.

## TMI

- `fsync`는 데이터 durability를 높이지만 tail latency를 크게 만들 수 있다.
- TLS handshake와 DNS lookup도 I/O 경로에 포함된다.
- I/O profile은 로그 timestamp만으로도 초기 단서를 얻을 수 있다.

## 연습 / 확인 문제 (Exercises)

- 작은 파일 1만 개와 큰 파일 1개의 읽기 시간을 비교하라.
- connection pooling 전후의 요청 latency를 측정하라.
- cold cache와 warm cache benchmark를 분리하라.

## 이어서 읽기 (Reading Path)

- 이전: [메모리 프로파일링](Memory-Profiling.md)
- 다음: [플레임 그래프](Flame-Graphs.md)

## 참조 (References)

- [Systems/Operating-Systems/IO-and-Drivers.md](../../Systems/Operating-Systems/IO-and-Drivers.md)
- [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)

