# Jenkins와 GitLab CI (Jenkins / GitLab CI)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/CICD-Principles.md](CICD-Principles.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Jenkins와 GitLab CI는 commit·merge request·schedule 같은 event에 따라 build, test, deploy job을 실행하는 CI/CD 플랫폼이다.

## 직관 (Intuition)

둘 다 자동화 작업장을 제공한다. Jenkins는 조립식 공장에 가깝고, GitLab CI는 GitLab repository workflow에 붙은 일체형 라인에 가깝다.

## 이론 (Theory)

Jenkins는 controller와 agent 구조, plugin ecosystem, Jenkinsfile 기반 pipeline을 사용한다. GitLab CI는 `.gitlab-ci.yml`, stage, job, runner, artifact, environment를 중심으로 동작한다. 공통 관심사는 runner 격리, credential 관리, cache, artifact 보존 기간, manual approval, pipeline reuse다.

### Runner와 secret 경계

CI 도구의 핵심 위험은 runner 권한과 secret 노출이다. PR from fork, untrusted branch, protected environment, deployment token을 구분한다. Build log와 artifact에 secret이 남지 않도록 masking과 least privilege를 적용한다.

Pipeline 정의는 코드와 함께 리뷰하고, 재사용 template에는 버전 pinning을 둔다. CI 변경은 배포 경로를 바꾸는 일이므로 애플리케이션 코드만큼 중요하다.

## 구현 (Implementation)

```groovy
pipeline {
  agent any
  stages {
    stage('test') {
      steps { sh 'npm test' }
    }
  }
}
```

```yaml
test:
  stage: test
  script:
    - npm test
```

## 복잡도 (Complexity)

플러그인과 공용 template이 많아질수록 재사용성은 올라가지만 장애 원인 추적이 어려워진다. Runner queue와 cache miss가 pipeline 시간을 지배할 수 있다.

## 응용 (Applications)

- enterprise CI 운영
- 사내 runner와 폐쇄망 build
- multi-stage release pipeline
- manual approval이 필요한 배포

## 흔한 오해 (Common Misunderstandings)

- CI 서버가 있으면 CI 문화가 자동으로 생기지는 않는다.
- 공용 runner에 secret을 무분별하게 노출하면 위험하다.
- 성공한 pipeline도 배포 후 관찰 없이는 충분하지 않다.
- Plugin 추가는 유지보수 책임도 함께 추가한다.

## TMI

- Jenkins shared library는 pipeline 중복을 줄이지만 version 관리가 필요하다.
- GitLab CI의 artifact와 cache는 목적이 다르다. Artifact는 결과물, cache는 재사용 중간물이다.
- Runner는 build 환경의 일부이므로 image와 toolchain version을 고정하는 편이 좋다.

## 연습 / 확인 문제 (Exercises)

- Jenkinsfile과 GitLab CI job을 같은 단계로 표현하라.
- artifact와 cache의 차이를 예시로 설명하라.
- secret이 필요한 deploy job의 권한 경계를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [CI/CD 원칙](CICD-Principles.md)
- 다음: [배포 전략](Deployment-Strategies.md)

## 참조 (References)

- [Engineering/DevOps/CICD-Principles.md](CICD-Principles.md)
- [Engineering/DevOps/GitHub/GitHub-Actions.md](GitHub/GitHub-Actions.md)
