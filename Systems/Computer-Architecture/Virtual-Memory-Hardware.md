# 가상 메모리 (하드웨어 관점) (Virtual Memory Hardware)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/Memory-Hierarchy.md](Memory-Hierarchy.md), [Systems/Operating-Systems/Memory-Management.md](../Operating-Systems/Memory-Management.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

가상 메모리는 각 프로세스에 연속된 가상 주소 공간을 제공하고, 하드웨어(MMU)와 OS가 이를 물리 메모리로 변환한다. 페이지 테이블과 TLB가 변환을 담당하며, 물리 메모리보다 큰 주소 공간을 가능케 한다.

## 직관 (Intuition)

각 프로그램이 "내가 메모리를 통째로 다 가졌다"고 믿게 만든다. 실제로는 OS가 조각(페이지)으로 나눠 물리 메모리 곳곳에, 부족하면 디스크에 둔다. 이 환상 덕에 프로그램은 다른 프로그램과 충돌하지 않고, 보호받으며, 물리 한계를 넘는 주소를 쓸 수 있다.

## 이론 (Theory)

가상 주소 = 페이지 번호 + 오프셋. **페이지 테이블**이 가상 페이지를 물리 프레임으로 매핑한다. 큰 주소 공간을 위해 다단계(계층) 페이지 테이블을 쓴다.

**MMU**가 변환을 수행하고, **TLB**(translation lookaside buffer)가 최근 변환을 캐싱해 매 접근의 페이지 테이블 조회를 피한다. 매핑이 없으면(또는 디스크에 있으면) **페이지 폴트**가 발생해 OS가 처리한다. 보호 비트(읽기/쓰기/실행)로 접근을 제어한다.

## 구현 (Implementation)

```python
PAGE_SIZE = 4096
def translate(vaddr, page_table, tlb):
    vpn = vaddr // PAGE_SIZE
    offset = vaddr % PAGE_SIZE
    if vpn in tlb:                       # TLB 히트: 빠른 경로
        frame = tlb[vpn]
    else:                                # TLB 미스: 페이지 테이블 조회
        if vpn not in page_table:
            raise PageFault(vpn)         # OS가 처리(디스크 로드 등)
        frame = page_table[vpn]
        tlb[vpn] = frame
    return frame * PAGE_SIZE + offset
```

## 복잡도 (Complexity)

TLB 히트면 변환은 사실상 0 사이클(병렬). TLB 미스는 페이지 테이블 워크(다단계면 여러 메모리 접근), 페이지 폴트는 디스크 I/O로 수 ms가 들어 수만 배 느리다. 따라서 TLB 적중률과 페이지 폴트율이 성능을 좌우한다.

## 응용 (Applications)

- 프로세스 격리·메모리 보호
- 물리 메모리 초과 사용(스와핑)
- 메모리 공유(공유 라이브러리, COW)
- 메모리 맵 파일(mmap)

## 흔한 오해 (Common Misunderstandings)

- 가상 메모리는 "디스크를 RAM처럼" 쓰는 것만이 아니다 — 격리·보호·공유가 핵심 이득이다.
- 페이지 폴트가 항상 오류는 아니다(요구 페이징의 정상 동작).
- TLB는 데이터 캐시와 별개다(주소 변환 전용).
- 큰 페이지(huge page)는 TLB 압박을 줄이지만 내부 단편화를 늘린다.

## TMI

- copy-on-write(COW)는 `fork` 시 페이지를 공유하다가 쓰기가 일어날 때만 복사해 효율을 높인다.
- TLB 미스 처리는 아키텍처에 따라 하드웨어(x86)나 소프트웨어(일부 RISC)가 한다.
- Meltdown 취약점은 가상 메모리 보호 경계를 추측 실행으로 우회했다.

## 연습 / 확인 문제 (Exercises)

- 4KB 페이지에서 가상 주소 0x3F50을 페이지 번호·오프셋으로 분해하라.
- TLB 히트·미스·페이지 폴트의 비용 차이를 설명하라.
- 다단계 페이지 테이블이 왜 필요한지 주소 공간 크기로 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [메모리 계층](Memory-Hierarchy.md)
- 다음: [입출력 (I/O) 시스템](IO-Systems.md), [Systems/Operating-Systems/Virtual-Memory.md](../Operating-Systems/Virtual-Memory.md)

## 참조 (References)

- [Systems/Operating-Systems/Virtual-Memory.md](../Operating-Systems/Virtual-Memory.md)
- [Systems/Computer-Architecture/Memory-Hierarchy.md](Memory-Hierarchy.md)
- [Reference/Books.md](../../Reference/Books.md)
