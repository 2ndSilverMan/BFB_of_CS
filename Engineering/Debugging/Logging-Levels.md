# 로깅 수준 설계 (Logging Levels)

- Level: Beginner
- Prerequisites: [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

로깅 수준은 로그의 중요도와 용도를 구분하는 체계다. 흔히 DEBUG, INFO, WARN, ERROR, FATAL 같은 수준을 사용한다.

## 직관 (Intuition)

모든 말을 확성기로 외치면 중요한 경고를 놓친다. 로그 수준은 일상 기록, 이상 징후, 즉시 대응할 오류를 구분하는 볼륨 조절기다.

## 이론 (Theory)

DEBUG는 개발·상세 진단, INFO는 정상 주요 이벤트, WARN은 자동 복구 가능하지만 주의할 상태, ERROR는 요청 실패나 개입이 필요한 오류에 쓴다. 로그 수준은 alert와 직접 연결하기보다 metric과 error budget과 함께 본다.

## 구현 (Implementation)

```json
{"level":"INFO","event":"order_created","order_id":"123"}
{"level":"ERROR","event":"payment_failed","error_code":"timeout"}
```

## 복잡도 (Complexity)

로그 비용은 traffic, log level, field 크기, index 정책에 거의 선형으로 증가한다. 낮은 level을 오래 켜면 저장 비용과 노이즈가 커지고, 높은 level만 남기면 원인 분석에 필요한 맥락을 잃을 수 있다.

## 응용 (Applications)

- 운영 로그 필터링
- 장애 조사
- alert 후보 선별
- 감사 이벤트 기록

## 흔한 오해 (Common Misunderstandings)

- ERROR 로그가 하나라도 있으면 항상 장애라는 뜻은 아니다.
- DEBUG를 production에서 무제한 켜면 비용과 개인정보 위험이 커진다.
- 로그 수준만으로 사용자 영향도를 알 수 없다.
- 민감정보는 어떤 수준에도 남기면 안 된다.

## TMI

- Sampling은 고빈도 로그 비용을 줄인다.
- Audit log는 일반 application log와 보존·무결성 요구가 다를 수 있다.
- 로그 message보다 structured field가 검색과 집계에 유리하다.

## 연습 / 확인 문제 (Exercises)

- 로그인 성공/실패/비밀번호 오류의 로그 수준을 정하라.
- DEBUG 로그를 안전하게 켜는 조건을 설계하라.
- ERROR 로그와 alert의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [구조화 로깅](Structured-Logging.md)
- 다음: [분산 로그 상관](Distributed-Log-Correlation.md)

## 참조 (References)

- [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md)
- [Engineering/DevOps/Metrics-Alerts.md](../DevOps/Metrics-Alerts.md)
