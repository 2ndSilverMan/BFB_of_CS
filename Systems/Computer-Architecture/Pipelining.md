# 파이프라이닝 (Pipelining)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/CPU-and-ISA.md](CPU-and-ISA.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

파이프라이닝은 명령어 실행을 여러 단계로 나눠, 서로 다른 단계의 명령어들을 동시에 처리하는 기법이다. 처리량(throughput)을 높이지만, 의존성·분기로 인한 해저드를 관리해야 한다.

## 직관 (Intuition)

세탁을 생각하자. 세탁기→건조기→개기를 한 빨래가 끝나야 다음을 시작하면 느리다. 대신 첫 빨래가 건조기로 가면 두 번째 빨래를 세탁기에 넣는다. 파이프라이닝은 명령어 실행의 각 단계를 이렇게 겹쳐, 매 클록마다 한 명령어가 완료되게 한다.

## 이론 (Theory)

고전적 5단계: **IF**(인출), **ID**(해석), **EX**(실행), **MEM**(메모리), **WB**(쓰기). 각 단계가 한 클록을 차지하고, 동시에 5개 명령어가 다른 단계에 있다. 이상적으로 CPI(명령당 클록)가 1에 근접한다.

**해저드(hazard)**:
- **구조적**: 자원 충돌.
- **데이터**: 앞 명령 결과를 뒤가 필요로 함 → 포워딩(forwarding)·스톨로 해결.
- **제어**: 분기 결과를 모름 → 분기 예측·지연 슬롯.

해저드는 버블(스톨)을 만들어 실제 CPI를 1보다 키운다. 슈퍼스칼라·아웃오브오더는 더 많은 병렬성을 추출한다.

## 구현 (Implementation)

```text
        클록:  1    2    3    4    5    6    7
명령1:        IF   ID   EX   MEM  WB
명령2:             IF   ID   EX   MEM  WB
명령3:                  IF   ID   EX   MEM  WB
→ 정상 상태에서 매 클록 1명령 완료(throughput ↑)

# 데이터 해저드 예: ADD R1,..  뒤 SUB ..,R1
# 포워딩으로 EX 결과를 다음 EX로 직접 전달 → 스톨 없이 해결
```

## 복잡도 (Complexity)

$k$단계 파이프라인은 이상적으로 처리량을 약 $k$배 높이지만, 지연(한 명령어의 총 시간)은 줄지 않는다. 실제 속도 향상은 해저드로 인한 스톨, 분기 예측 실패 페널티, 파이프라인 채우기/비우기 오버헤드에 의해 깎인다.

## 응용 (Applications)

- 모든 현대 CPU의 명령어 처리
- GPU의 대규모 스레드 파이프라인
- 명령어 수준 병렬성(ILP) 추출
- 처리량 중심 하드웨어 설계

## 흔한 오해 (Common Misunderstandings)

- 파이프라이닝은 개별 명령어를 빠르게 하지 않는다 — 처리량을 높일 뿐 지연은 그대로다.
- 단계를 무한정 늘린다고 좋아지지 않는다(해저드·분기 페널티 증가).
- 분기 예측 실패는 파이프라인을 비워 큰 페널티를 준다.
- CPI 1은 이상값이며 실제로는 해저드로 더 크다.

## TMI

- 인텔 펜티엄 4의 초장 파이프라인(31단계)은 클록은 높였지만 분기 페널티로 효율이 나빠 교훈으로 남았다.
- 분기 예측기는 현대 CPU에서 95% 이상의 정확도를 보이는 정교한 하드웨어다.
- Spectre 같은 취약점은 추측 실행(speculative execution)의 부작용을 악용했다.

## 연습 / 확인 문제 (Exercises)

- 5단계 파이프라인에서 데이터 해저드가 생기는 명령어 쌍을 만들어라.
- 포워딩이 스톨을 어떻게 줄이는지 설명하라.
- 분기 예측 실패 페널티가 파이프라인 깊이와 어떤 관계인지 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [CPU와 ISA](CPU-and-ISA.md)
- 다음: [메모리 계층](Memory-Hierarchy.md)

## 참조 (References)

- [Systems/Computer-Architecture/CPU-and-ISA.md](CPU-and-ISA.md)
- [Reference/Books.md](../../Reference/Books.md)
