# IP 주소와 라우팅 (IP and Routing)

- Level: Intermediate
- Prerequisites: [Systems/Networks/Network-Models.md](Network-Models.md), [Systems/Networks/Physical-and-Link.md](Physical-and-Link.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

IP(인터넷 프로토콜)는 네트워크 계층에서 종단 간 패킷 전달을 담당한다. IP 주소로 호스트를 식별하고, 라우터들이 라우팅 테이블에 따라 패킷을 목적지로 한 홉씩 전달한다.

## 직관 (Intuition)

링크 계층이 "옆집 전달"이라면 IP는 "먼 도시까지 우편 배달"이다. 각 라우터는 전체 경로를 모른 채 "이 목적지는 저쪽 방향"이라는 부분 정보(라우팅 테이블)만으로 다음 홉에 넘긴다. 이 분산된 결정이 모여 전 세계 어디로든 패킷이 도달한다.

## 이론 (Theory)

**IP 주소**: IPv4는 32비트, IPv6는 128비트. CIDR 표기 $\text{prefix}/n$은 앞 $n$비트가 네트워크 부분이다. 서브넷 마스크로 네트워크/호스트를 가른다.

**라우팅**: 라우터는 **최장 접두사 매칭(longest prefix match)**으로 목적지에 가장 구체적인 경로를 고른다. 라우팅 테이블은 정적 설정 또는 동적 프로토콜로 채워진다.
- **내부(IGP)**: OSPF(링크 상태, 다익스트라), RIP(거리 벡터, 벨만-포드).
- **외부(EGP)**: BGP(자율 시스템 간 경로 정책).

NAT은 사설 IP를 공인 IP로 변환해 주소 부족을 완화한다. TTL은 무한 루프를 막는다.

## 구현 (Implementation)

```python
import ipaddress
def longest_prefix_match(dest, routes):
    best = None
    dest_ip = ipaddress.ip_address(dest)
    for net, nexthop in routes:            # routes: [(CIDR, nexthop)]
        network = ipaddress.ip_network(net)
        if dest_ip in network:
            if best is None or network.prefixlen > best[0].prefixlen:
                best = (network, nexthop)   # 더 긴 접두사 우선
    return best[1] if best else None
```

## 복잡도 (Complexity)

최장 접두사 매칭은 소박하게는 경로 수에 선형이지만, 라우터는 트라이(또는 TCAM 하드웨어)로 거의 상수 시간에 처리한다. OSPF의 다익스트라는 `O(E log V)`, 라우팅 테이블 크기와 수렴 시간이 실제 성능을 좌우한다.

## 응용 (Applications)

- 인터넷·기업 네트워크의 패킷 전달
- 서브네팅으로 네트워크 분할·관리
- VPN, NAT, 방화벽 정책
- 클라우드 가상 네트워크(VPC)

## 흔한 오해 (Common Misunderstandings)

- IP는 신뢰성을 보장하지 않는다(비신뢰·비순서). 그건 TCP의 몫이다.
- 라우터는 전체 경로가 아니라 다음 홉만 결정한다.
- 사설 IP(10.x, 192.168.x)는 인터넷에서 직접 라우팅되지 않는다(NAT 필요).
- 최장 접두사 매칭이지 "첫 번째 일치"가 아니다.

## TMI

- IPv4 주소 고갈은 1990년대부터 예견됐고, NAT과 CIDR이 수명을 크게 연장했다.
- BGP의 경로는 기술이 아니라 상업적 정책으로 결정되는 경우가 많다.
- 잘못된 BGP 광고 하나가 대형 인터넷 장애를 일으킨 사례가 여러 번 있었다.

## 연습 / 확인 문제 (Exercises)

- `192.168.1.0/24`의 네트워크/호스트 비트와 가능한 호스트 수를 구하라.
- 여러 CIDR 경로에서 특정 목적지의 최장 접두사 매칭을 찾아라.
- 거리 벡터와 링크 상태 라우팅의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [물리 계층과 데이터 링크 계층](Physical-and-Link.md)
- 다음: [TCP와 UDP](TCP-UDP.md), [HTTP / HTTPS](HTTP.md)

## 참조 (References)

- [Systems/Networks/TCP-UDP.md](TCP-UDP.md)
- [Algorithms/Dijkstra.md](../../Algorithms/Dijkstra.md)
- [Reference/Books.md](../../Reference/Books.md)
