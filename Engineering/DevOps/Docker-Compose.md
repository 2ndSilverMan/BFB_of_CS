# Docker Compose (Docker Compose)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Docker-Basics.md](Docker-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Docker Compose는 여러 container service, network, volume, environment를 하나의 YAML 파일로 정의하고 함께 실행하는 도구다.

## 직관 (Intuition)

앱, 데이터베이스, 캐시를 명령 하나로 같은 실험실에 띄운다. 개발 환경을 말로 설명하는 대신 실행 가능한 조립도로 남긴다.

## 이론 (Theory)

Compose file은 service별 image/build, port, environment, volume, depends_on, network를 정의한다. 기본 network 안에서 service 이름이 DNS 이름처럼 동작한다. Compose는 local development와 integration test에 특히 유용하지만, production orchestration은 Kubernetes 같은 별도 플랫폼이 담당하는 경우가 많다.

## 구현 (Implementation)

```yaml
services:
  app:
    build: .
    ports: ["8080:8080"]
    depends_on: [db]
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

## 복잡도 (Complexity)

서비스 수가 늘수록 startup order, health check, volume state, port 충돌 관리가 중요해진다.

## 응용 (Applications)

- local development stack
- integration test environment
- demo 환경 구성
- dependency service 임시 실행

## 흔한 오해 (Common Misunderstandings)

- `depends_on`은 application readiness를 완전히 보장하지 않는다.
- Compose volume은 container 삭제와 별개로 남을 수 있다.
- 환경 변수를 파일에 넣을 때 secret 관리에 주의해야 한다.
- Local Compose가 production network와 resource 조건을 그대로 대표하지 않는다.

## TMI

- `docker compose down -v`는 volume까지 삭제하므로 데이터 손실에 주의한다.
- Healthcheck를 넣으면 dependency readiness를 더 명확히 표현할 수 있다.
- Compose profile은 선택적 service를 켜고 끄는 데 유용하다.

## 연습 / 확인 문제 (Exercises)

- 앱과 데이터베이스를 Compose로 묶어 실행하라.
- named volume과 bind mount의 차이를 실습하라.
- healthcheck 없는 `depends_on`의 한계를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Docker 기초](Docker-Basics.md)
- 다음: [컨테이너 네트워킹과 볼륨](Container-Networking-Volumes.md)

## 참조 (References)

- [Engineering/DevOps/Docker-Basics.md](Docker-Basics.md)
- [Systems/Networks/DNS.md](../../Systems/Networks/DNS.md)

