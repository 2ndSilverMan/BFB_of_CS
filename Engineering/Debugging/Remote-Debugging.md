# 원격 디버깅 (Remote Debugging)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Breakpoints-and-Stepping.md](Breakpoints-and-Stepping.md), [Engineering/DevOps/Docker-Basics.md](../DevOps/Docker-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

원격 디버깅은 로컬 IDE나 디버거가 다른 머신, 컨테이너, 서버 프로세스에 연결해 중단점과 상태 관찰을 수행하는 방식이다.

## 직관 (Intuition)

버그가 내 노트북에서는 안 나고 서버에서만 난다면, 서버 위 프로그램을 멀리서 현미경으로 보는 것이 원격 디버깅이다.

## 이론 (Theory)

원격 디버깅은 debug agent, port forwarding, symbol/source mapping, 권한 설정이 필요하다. 보안상 디버그 포트는 외부에 열면 안 되며, 운영 환경에서는 중단점이 서비스 영향을 줄 수 있다.

### 안전한 원격 관찰

원격 디버깅은 production state를 직접 관찰할 수 있어 강력하지만, 권한·성능·개인정보 위험이 크다. 접속은 시간 제한, 감사 로그, read-only 우선, break 금지 정책을 둔다. Production에서 프로세스를 멈추는 breakpoint는 장애를 확대할 수 있다.

가능하면 live debugger보다 metrics, trace, structured log, feature flag, shadow traffic 같은 비침습적 관찰을 먼저 사용한다.

## 구현 (Implementation)

```text
container app starts with debug port
local IDE forwards port
IDE attaches to remote process
```

## 복잡도 (Complexity)

Remote debugging 비용은 네트워크 지연, symbol/source version 일치, target 환경 접근 권한에 좌우된다. Production에 직접 붙는 경우 breakpoint가 사용자 traffic을 멈출 수 있어 read-only 관찰과 sandbox 재현을 우선한다.

## 응용 (Applications)

- 컨테이너 내부 문제 추적
- staging 환경 디버깅
- 서버 전용 환경 변수 문제
- 원격 프로세스 상태 관찰

## 흔한 오해 (Common Misunderstandings)

- 운영 서비스에 중단점을 걸면 실제 요청이 멈출 수 있다.
- 디버그 포트를 공개하면 보안 위험이 크다.
- 소스 코드와 배포 artifact 버전이 다르면 breakpoint가 어긋난다.
- 원격 디버깅은 로그와 metrics를 대체하지 않는다.

## TMI

- Production에서는 snapshot/debug probe처럼 멈추지 않는 관찰 도구가 더 안전할 수 있다.
- Source map은 minified JavaScript 디버깅에 중요하다.
- Kubernetes 환경에서는 port-forward로 임시 연결하는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- 원격 디버깅이 위험한 운영 상황을 설명하라.
- Source mapping이 필요한 이유를 말하라.
- Staging에서만 나는 버그의 원격 디버깅 절차를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [중단점과 스텝 실행](Breakpoints-and-Stepping.md)
- 다음: [코어 덤프 분석](Core-Dump-Analysis.md), [로그 수준](Logging-Levels.md)

## 참조 (References)

- [Engineering/DevOps/Docker-Basics.md](../DevOps/Docker-Basics.md)
- [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md)
