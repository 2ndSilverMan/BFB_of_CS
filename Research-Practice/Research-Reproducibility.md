# 재현성과 연구 산출물 (Research Reproducibility)

- Level: Intermediate
- Prerequisites: [연구 설계](Research-Design-and-Validity.md), 파일·버전·명령의 기본 개념
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (연구 절차와 제한된 사례)

---

## 개념 (Concept)

재현 가능한 연구 산출물은 다른 사람이 주장과 연결된 입력·방법·환경·결과를 추적하고 다시 확인할 수 있게 만드는 자료다. 코드 공개, 같은 환경에서 재실행, 독립 구현으로 결과 확인은 서로 다른 수준이다. 분야마다 reproduction/replication 용어가 다를 수 있으므로 사용한 정의를 문서에 적는다.

## 직관 (Intuition)

“실행되었다”와 “논문의 결론이 재현되었다”는 다르다. 작은 데이터에서 오류 없이 끝났어도 논문의 입력·지표·통계·하드웨어가 다르면 같은 주장을 시험한 것이 아닐 수 있다. 실행 기록은 무엇을 확인했는지 좁고 정확하게 연결해야 한다.

## 이론 (Theory)

산출물에는 코드뿐 아니라 데이터·설정·환경·분석·원시 결과·시각화 생성 절차가 포함될 수 있다. [ACM artifact 안내](https://www.acm.org/publications/policies/artifact-review-and-badging-current)는 산출물의 가용성·평가와 결과 검증을 구분하는 참고 기준이다. 저장소에 파일을 올렸다는 이유만으로 공식 배지를 붙이지 않는다.

버전/커밋과 해시는 무엇을 실행했는지 식별하는 데 도움을 준다. 해시 일치는 바이트 동일성의 근거이지 데이터가 올바르거나 합법적으로 공개되었다는 근거가 아니다. 난수 seed를 고정해도 라이브러리·병렬 연산·장치에 따라 결과가 달라질 수 있어 bitwise equality와 허용 오차 내 의미적 일치를 구분한다.

## 구현 (Implementation)

가상 실험의 manifest에 다음을 남긴다.

| 항목 | 기록할 내용 |
|---|---|
| 주장 | “제공된 정수 입력에 대해 정렬·중복 제거 결과가 기대와 같다” |
| 입력 | 데이터 파일 또는 본문 값, 인코딩·해시 |
| 코드 | 버전/커밋과 실행 진입점 |
| 환경 | Python·OS·아키텍처, 외부 패키지 유무 |
| 실행 | 정확한 명령, 옵션, 종료 코드 |
| 결과 | 기대 출력, 실제 출력, 비교 기준 |
| 제외 | 대규모 성능·병렬 비결정성·다른 데이터는 미검증 |

외부 파일·네트워크가 필요 없는 최소 예제다.

```python
import hashlib
import json
import platform

raw = [3, 1, 3, 2]
encoded = json.dumps(raw, separators=(",", ":")).encode("utf-8")
fingerprint = hashlib.sha256(encoded).hexdigest()
result = sorted(set(raw))
assert result == [1, 2, 3]
assert len(fingerprint) == 64
assert hashlib.sha256(encoded).hexdigest() == fingerprint
assert hashlib.sha256(b"[3,1,3,2,0]").hexdigest() != fingerprint
print({"python": platform.python_version(),
       "input_sha256": fingerprint, "result": result})
```

이 예제의 재실행은 정렬·중복 제거와 입력 식별 절차를 확인한다. 실제 연구의 성능·일반화·독립 재현을 입증하지 않는다. 실패했다면 기대값을 결과에 맞춰 조용히 바꾸지 않고 환경·입력·실행 차이를 기록한다.

민감하거나 재배포할 수 없는 데이터는 공개를 강행하지 않는다. 접근 절차, 스키마, 합성 예제, 검증 가능한 요약과 제한을 남기되 합성 데이터가 원 결과의 재현을 대신했다고 주장하지 않는다.

## 복잡도 (Complexity)

환경 고정·보관·문서화에는 지속 비용이 든다. 컨테이너도 하드웨어·커널·외부 서비스의 모든 조건을 고정하지 않는다. 전체 데이터를 못 보관하면 어떤 주장까지 확인 가능한지 범위를 낮춰 보고한다. 저장 용량과 실행 비용이 크면 smoke test와 full experiment를 구분하고 각각의 예상 시간·자원을 적는다.

## 응용 (Applications)

논문 부록, benchmark, 알고리즘 구현, 교육 실습, 문서의 계산 예제를 관리할 때 사용한다. 수학적 결과도 정리 가정·증명 보조 파일·검산 코드를 함께 보관할 수 있다.

## 흔한 오해 (Common Misunderstandings)

- Git 링크 하나면 재현된다: 브랜치 내용과 외부 의존성이 바뀔 수 있다.
- seed를 고정하면 모든 환경에서 같다: 비결정적 연산과 버전 차이를 확인해야 한다.
- 해시가 맞으면 주장이 맞다: 해시는 내용 식별이지 타당성 검증이 아니다.

## TMI

- 실험 명령뿐 아니라 결과 표를 만드는 분석 명령도 연구의 일부다.
- 실패 기록과 부정적 결과가 있어야 나중에 성공한 설정만 선택된 경위를 추적할 수 있다.

## 연습 / 확인 문제 (Exercises)

1. 같은 출력이 나왔는데 입력 해시가 다르면? **답:** 두 실행의 입력이 같은지 확인되지 않았다. 출력이 우연히 같을 수 있다.
2. 소규모 예제만 통과했다면 논문 성능표에 어떤 상태를 표시해야 하나? **답:** 실행 가능성의 제한된 확인이며 성능 결과는 미검증이다.
3. 공개 금지 데이터가 있는 산출물을 설계하라. **판단 기준:** 권한·접근 절차·대체 예제·확인 가능한 주장·한계가 구분된다.

## 이어서 읽기 (Reading Path)

- 다음: [논문 작성과 비평](Scientific-Writing-and-Critique.md).
- 관련: [지식재산](../Computing-and-Society/Intellectual-Property-and-Collaboration.md), [프라이버시](../Computing-and-Society/Privacy-and-Data-Governance.md).

## 참조 (References)

- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current) — 산출물 가용성·평가·결과 검증의 구분. 공식 배지는 해당 심사 절차와 별개로 주장하지 않는다.
- [ACM 공식 검색 색인에 잡힌 동일 정책](https://prod-www.acm.bloomreach.cloud/publications/policies/artifact-review-and-badging-current) — 이번 환경에서는 검색 요약만 접근 가능했다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 주장별 manifest, 입력 해시와 의미 검사의 분리, smoke/full 실험 구분.
- 보충할 내용: 실제 논문 산출물 재실행, 환경 잠금 파일, GPU 비결정성·오차 허용 기준.
- 확인 상태: 2026-09-18 ACM 정책 검색 요약 확인, 원문 직접 열기는 실패. 예제는 제한된 로컬 확인용이며 외부 연구 결과를 재현한 것은 아니다. Python 3.12/Windows에서 본문의 Python 1개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
