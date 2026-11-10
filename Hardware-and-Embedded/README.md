# 하드웨어와 임베디드

> 회로·디지털 설계·장치 인터페이스·실시간 제약을 소프트웨어와 연결한다. CPU 구조 설명은 Systems의 기존 문서를 재사용한다.

**선수지식**: [디지털 논리](../Systems/Computer-Architecture/Digital-Logic.md), [C 언어](../Programming/Languages/C/)

## 현재 가용성

아래 등록 주제에 `Draft` 본문이 있다. 개념·원리·구체 사례·확인 문제와 판단 기준·직접 출처·재작성 메모를 포함한다. `Planned`는 아직 본문이 없는 예정 항목에만 사용한다. 초안이 있다는 것은 분야 전체의 내용·실습·연구 깊이가 확보됐다는 뜻이 아니다. 각 문서의 확인 상태에서 실제 실행한 계산과 미실시한 실험을 구분한다.

## 주제 목록

표는 초기 선수지식 순서다. 전 영역의 전체 세부 목차를 확정한 것이 아니며 후속 조사에서 확장한다.

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| 회로와 전자소자 기초 | [Circuits-and-Electronics.md](Circuits-and-Electronics.md) | 전압·전류·논리 레벨과 측정 가정 | Draft |
| HDL과 FPGA 설계 | [HDL-and-FPGA.md](HDL-and-FPGA.md) | 조합·순차회로, 시뮬레이션, 타이밍 제약 | Draft |
| 마이크로컨트롤러와 인터페이스 | [Microcontrollers-and-Interfaces.md](Microcontrollers-and-Interfaces.md) | 인터럽트, 타이머, GPIO, 장치 통신 | Draft |
| 임베디드 실시간 설계 | [Embedded-Real-Time-Design.md](Embedded-Real-Time-Design.md) | 마감시간, WCET 가정, 스케줄링, 안전한 실패 | Draft |

## 학습 확인 목표

타이밍 다이어그램과 테스트벤치로 설계를 설명하고, 센서 입력부터 출력까지 지연 예산을 계산한다. 실제 장비가 없으면 시뮬레이션 범위와 미검증 전기적 조건을 구분한다.

## 연관 섹션

[운영체제](../Systems/Operating-Systems/), [프로그래밍](../Programming/)
