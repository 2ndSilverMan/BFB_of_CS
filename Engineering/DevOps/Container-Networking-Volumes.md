# 컨테이너 네트워킹과 볼륨 (Container Networking and Volumes)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Docker-Basics.md](Docker-Basics.md), [Systems/Networks/Network-Models.md](../../Systems/Networks/Network-Models.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

컨테이너 네트워킹과 볼륨은 container가 서로 통신하고 데이터를 container lifecycle 밖에 보존하도록 해 주는 핵심 구성 요소다.

## 직관 (Intuition)

컨테이너는 금방 새로 만들 수 있는 방이고, volume은 방을 바꿔도 남는 창고다. Network는 방들이 서로 찾는 복도와 주소 체계다.

## 이론 (Theory)

Bridge network는 host 안의 container들을 가상 network로 묶고, port publishing은 host port를 container port에 연결한다. Container끼리는 같은 network에서 service name으로 통신할 수 있다. Volume은 Docker가 관리하는 저장 공간이고, bind mount는 host path를 직접 연결한다. 영구 데이터, backup, permission, SELinux/AppArmor 같은 보안 맥락을 고려한다.

### 네트워크와 저장소의 수명주기

컨테이너 네트워크는 service discovery, port publishing, bridge/overlay boundary를 분리해 이해해야 한다. `localhost`가 host인지 container 자신인지 헷갈리면 연결 오류가 자주 난다.

Volume은 container보다 오래 산다. 백업, migration, 권한, fsync, 데이터 손상 복구를 고려하지 않고 임시 저장소처럼 쓰면 장애 시 복구가 어렵다.

## 구현 (Implementation)

```bash
docker network create app-net
docker volume create db-data
docker run --network app-net --name redis redis:7
docker run -v db-data:/var/lib/postgresql/data postgres:16
```

## 복잡도 (Complexity)

Network hop, NAT, DNS lookup, filesystem driver, mount 방식이 성능과 디버깅 난도에 영향을 준다.

## 응용 (Applications)

- app과 database 연결
- persistent database container
- local integration test
- sidecar pattern 실험

## 흔한 오해 (Common Misunderstandings)

- Container 내부 `localhost`는 host가 아니라 그 container 자신이다.
- Container filesystem에 쓴 데이터는 삭제 시 사라질 수 있다.
- Bind mount는 host 경로와 권한 문제를 그대로 노출한다.
- Port publish 없이도 같은 network의 container끼리는 통신할 수 있다.

## TMI

- Docker Desktop의 host network 동작은 Linux native Docker와 차이가 있을 수 있다.
- Volume backup은 container image backup과 별개로 설계해야 한다.
- Network alias를 쓰면 service discovery 실험이 쉬워진다.

## 연습 / 확인 문제 (Exercises)

- 두 container를 같은 bridge network에 넣고 이름으로 ping하라.
- container 삭제 후 named volume 데이터가 남는지 확인하라.
- bind mount와 named volume의 운영 위험을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Docker Compose](Docker-Compose.md)
- 다음: [Kubernetes 기초](Kubernetes-Basics.md)

## 참조 (References)

- [Systems/Networks/Network-Models.md](../../Systems/Networks/Network-Models.md)
- [Systems/Operating-Systems/File-Systems.md](../../Systems/Operating-Systems/File-Systems.md)
