# 메모리 관리 (Memory Management)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md), [Systems/Computer-Architecture/Data-Representation.md](../Computer-Architecture/Data-Representation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

메모리 관리는 운영체제가 한정된 물리 메모리를 여러 프로세스에 **할당·보호·추상화**하는 일이다. 핵심 아이디어는 각 프로세스에 "나 혼자 연속된 메모리를 통째로 쓰는 것 같은" 가상 주소 공간이라는 환상을 주는 것이다.

## 직관 (Intuition)

프로그램은 `0번지부터 내 메모리`라고 믿고 짜이지만, 실제 물리 메모리에는 여러 프로그램이 섞여 올라가 있다. 운영체제와 하드웨어(MMU)가 "가상 주소 → 물리 주소" 번역을 대신 해 주므로, 각 프로세스는 서로를 모른 채 안전하게 격리된다. 아파트 호수(가상)와 실제 동·층(물리)을 우편 시스템이 매핑해 주는 것과 같다.

## 이론 (Theory)

CPU가 내는 주소는 **가상 주소(논리 주소)** 이고, 메모리에 실제로 닿는 것은 **물리 주소**다. 변환은 MMU가 한다.

**페이징(paging).** 가상 주소 공간을 고정 크기 페이지, 물리 메모리를 같은 크기 프레임으로 나눈다. 가상 주소는 (페이지 번호 $p$, 오프셋 $d$)로 쪼개지고, 페이지 테이블이 $p \to$ 프레임 $f$를 알려 준다.

$$\text{물리 주소} = f \times \text{PAGE\_SIZE} + d$$

페이징은 외부 단편화를 없애지만, 페이지를 다 못 채운 만큼의 **내부 단편화**가 생긴다. **세그멘테이션**은 코드·데이터·스택처럼 의미 단위로 나누는 방식이며, 둘을 섞어 쓰기도 한다.

## 구현 (Implementation)

페이지 테이블을 이용한 주소 변환을 단순화한 예시다.

```python
PAGE_SIZE = 256
page_table = {0: 5, 1: 2, 2: 7}   # 가상 페이지 -> 물리 프레임

def translate(virtual_addr):
    page, offset = divmod(virtual_addr, PAGE_SIZE)
    if page not in page_table:
        raise ValueError("page fault")     # 매핑 없음 -> 페이지 폴트
    frame = page_table[page]
    return frame * PAGE_SIZE + offset

print(translate(300))   # page 1, offset 44 -> frame 2 -> 2*256 + 44 = 556
```

## 복잡도 (Complexity)

| 항목 | 비용 |
|---|---|
| 단일 단계 페이지 테이블 조회 | `O(1)` (TLB 적중 시 매우 빠름) |
| 다단계 페이지 테이블 | 단계 수만큼 메모리 접근 |
| 페이지 테이블 공간 | 가상 주소 공간 크기에 비례 |

자주 쓰는 변환은 TLB(Translation Lookaside Buffer)라는 캐시에 담아 거의 `O(1)`로 처리한다.

## 응용 (Applications)

- 프로세스 간 메모리 격리와 보호
- 가상 메모리(물리 메모리보다 큰 주소 공간, 스왑)
- 메모리 매핑 파일(`mmap`), 공유 메모리
- 복사-시-쓰기(copy-on-write)로 효율적인 `fork`

## 흔한 오해 (Common Misunderstandings)

- 가상 메모리가 곧 "스왑(디스크 사용)"만을 뜻하지는 않는다. 핵심은 주소 추상화와 격리이며, 스왑은 그 응용 중 하나다.
- 페이징이 항상 느린 것은 아니다. TLB 덕분에 대부분의 변환은 사실상 공짜에 가깝다.
- 단편화는 한 종류가 아니다. 페이징은 내부 단편화, 가변 분할·세그멘테이션은 외부 단편화 경향이 있다.
- 프로세스가 보는 주소가 실제 물리 주소라고 가정하면 안 된다. 거의 항상 가상 주소다.

## TMI

- 매핑이 없는 페이지에 접근하면 **페이지 폴트**가 발생하고, OS가 디스크에서 페이지를 올리거나(정상) 잘못된 접근이면 프로그램을 중단시킨다(세그폴트).
- "메모리가 부족하다"며 디스크 스왑이 과해져 시스템이 거의 멈추는 현상을 **스래싱(thrashing)** 이라 한다.
- 64비트 주소 공간은 이론상 16엑사바이트지만, 실제 CPU는 그중 일부 비트만 사용한다(예: 48비트).

## 연습 / 확인 문제 (Exercises)

- `PAGE_SIZE`가 1024일 때 가상 주소 5000의 페이지 번호와 오프셋을 구하라.
- 내부 단편화와 외부 단편화의 차이를 그림이나 예시로 설명하라.
- TLB가 없을 때와 있을 때 주소 변환 비용이 어떻게 달라지는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](Processes-and-Threads.md)
- 다음: [가상 메모리와 페이지 교체](Virtual-Memory.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md)
- [Systems/Computer-Architecture/Data-Representation.md](../Computer-Architecture/Data-Representation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
