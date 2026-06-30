# 물리 계층과 데이터 링크 계층 (Physical and Link Layer)

- Level: Intermediate
- Prerequisites: [Systems/Networks/Network-Models.md](Network-Models.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

물리 계층은 비트를 전기·광·전파 신호로 실제 매체에 전송하는 계층이고, 데이터 링크 계층은 같은 링크에 연결된 장치들 사이에서 프레임을 안정적으로 주고받는다. 이더넷, MAC 주소, 오류 검출이 핵심이다.

## 직관 (Intuition)

상위 계층이 "어디로 보낼까(IP)"를 다룬다면, 링크 계층은 "바로 옆 장치에게 어떻게 전달할까"를 다룬다. 한 케이블이나 무선 채널을 여러 장치가 공유하면 충돌이 생기는데, 누가 언제 말할지(매체 접근 제어)와 도착한 비트가 깨지지 않았는지(오류 검출)를 이 계층이 책임진다.

## 이론 (Theory)

**물리 계층**: 인코딩(NRZ, 맨체스터), 변조, 대역폭·전송률. 신호 감쇠·잡음이 한계를 만든다.

**데이터 링크 계층**: 비트를 **프레임**으로 묶고, MAC 주소로 링크 내 장치를 식별한다. 두 하위 기능:
- **오류 검출**: CRC(순환 중복 검사), 패리티. 검출만 하고 보통 재전송은 상위가 처리.
- **매체 접근 제어(MAC)**: CSMA/CD(유선 이더넷, 충돌 감지), CSMA/CA(무선, 충돌 회피).

스위치는 MAC 주소 테이블로 프레임을 해당 포트로만 전달한다(허브의 브로드캐스트와 대비). ARP는 IP를 MAC으로 변환한다.

## 구현 (Implementation)

```python
def crc_remainder(data_bits, poly):        # CRC 오류 검출(개념)
    msg = data_bits + [0] * (len(poly) - 1)
    for i in range(len(data_bits)):
        if msg[i] == 1:
            for j in range(len(poly)):
                msg[i + j] ^= poly[j]       # 다항식 나눗셈(XOR)
    return msg[-(len(poly) - 1):]          # 나머지 = CRC
```

## 복잡도 (Complexity)

CRC 계산은 데이터 길이에 선형(`O(n)`)이며 하드웨어로 빠르게 처리된다. 핵심 성능 지표는 알고리즘 복잡도가 아니라 대역폭(bps), 지연(latency), 충돌·재전송으로 인한 유효 처리량(throughput)이다.

## 응용 (Applications)

- 이더넷·Wi-Fi LAN 구성
- 스위치의 프레임 포워딩
- 산업용·자동차 버스(CAN 등)
- 오류 검출이 필요한 모든 링크 전송

## 흔한 오해 (Common Misunderstandings)

- MAC 주소는 IP와 다르다. MAC은 링크 지역(local), IP는 종단 간 라우팅용이다.
- CRC는 오류를 검출하지 정정하지는 않는다(정정엔 ECC 코드 필요).
- 스위치(링크 계층)와 라우터(네트워크 계층)는 동작 계층이 다르다.
- 무선은 충돌 감지(CD)가 어려워 회피(CA)를 쓴다.

## TMI

- 이더넷의 CSMA/CD는 오늘날 전이중(full-duplex) 스위치 환경에선 거의 작동하지 않는다(충돌 자체가 없음).
- MAC 주소 앞 24비트(OUI)는 제조사를 식별한다.
- "프레임"과 "패킷"을 혼용하기 쉽지만 계층이 다르다(프레임=링크, 패킷=네트워크).

## 연습 / 확인 문제 (Exercises)

- 주어진 데이터와 생성 다항식으로 CRC 나머지를 계산하라.
- 허브와 스위치의 프레임 전달 차이를 설명하라.
- CSMA/CD와 CSMA/CA가 갈리는 이유를 매체 특성으로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [네트워크 모델](Network-Models.md)
- 다음: [IP 주소와 라우팅](IP-and-Routing.md)

## 참조 (References)

- [Systems/Networks/Network-Models.md](Network-Models.md)
- [Systems/Networks/IP-and-Routing.md](IP-and-Routing.md)
- [Reference/Books.md](../../Reference/Books.md)
