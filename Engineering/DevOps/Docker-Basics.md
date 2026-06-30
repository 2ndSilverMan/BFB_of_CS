# Docker 기초 (Docker Basics)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../../Systems/Operating-Systems/Processes-and-Threads.md), [Systems/Operating-Systems/File-Systems.md](../../Systems/Operating-Systems/File-Systems.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Docker는 application과 dependency를 image로 묶고 격리된 container process로 실행하는 도구다. Image는 immutable layer 집합, container는 image의 실행 instance다.

## 직관 (Intuition)

실행 환경을 설명서 대신 versioned package로 전달한다. Container는 VM보다 가볍지만 host kernel을 공유하며 process·network·filesystem isolation을 조합한다.

## 이론 (Theory)

Linux container는 namespace로 resource view를 격리하고 cgroup으로 CPU·memory를 제한한다. Dockerfile instruction은 layer와 build cache를 만들며 registry가 image를 배포한다. Volume은 container lifecycle과 독립적인 data를, bind mount는 host path를 연결한다.

Image digest로 immutable artifact를 식별하고, minimal base·non-root user·secret 미포함·multi-stage build를 기본으로 삼는다.

### 이미지 보안과 재현성

좋은 컨테이너 이미지는 작고 재현 가능하며 실행 권한이 제한되어 있다. Base image digest pinning, multi-stage build, non-root user, read-only filesystem, dependency scan, SBOM을 함께 고려한다. Build context에는 secret과 불필요한 파일이 들어가지 않게 `.dockerignore`를 관리한다.

Runtime에서는 CPU/memory limit, health check, signal handling, log stdout/stderr 원칙을 지킨다.

## 구현 (Implementation)

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER 10001
CMD ["python", "app.py"]
```

build context와 `.dockerignore`에 secret·불필요한 파일이 포함되지 않게 한다.

## 복잡도 (Complexity)

Build 시간은 context·layer·dependency에, image pull은 compressed size와 network에 좌우된다. Container 시작은 보통 VM boot보다 빠르지만 storage driver와 initialization 비용이 있다.

## 응용 (Applications)

- reproducible development·CI
- service packaging·deployment
- isolated integration test
- Kubernetes workload image

## 흔한 오해 (Common Misunderstandings)

- container는 완전한 security boundary나 VM과 동일하지 않다.
- image 안에 넣은 secret은 layer history에 남을 수 있다.
- container filesystem은 영구 data 저장소가 아니다.
- `latest` tag는 immutable version 보장이 아니다.

## TMI

- PID 1 process는 signal 전달과 zombie reaping을 고려해야 한다.
- layer 순서는 cache hit와 build 시간에 영향을 준다.
- rootless mode는 host privilege 위험을 줄인다.

## 연습 / 확인 문제 (Exercises)

- 작은 application의 multi-stage Dockerfile을 작성하라.
- image와 container, volume의 lifecycle을 비교하라.
- non-root 실행과 read-only filesystem을 적용하라.

## 이어서 읽기 (Reading Path)

- 이전: [CI/CD 원칙](CICD-Principles.md)
- 다음: [Kubernetes 기초](Kubernetes-Basics.md)
- 관련: [Docker Compose](Docker-Compose.md)

## 참조 (References)

- [Docker Get Started](https://docs.docker.com/get-started/)
- [Systems/Operating-Systems/Processes-and-Threads.md](../../Systems/Operating-Systems/Processes-and-Threads.md)
- [Reference/Books.md](../../Reference/Books.md)
