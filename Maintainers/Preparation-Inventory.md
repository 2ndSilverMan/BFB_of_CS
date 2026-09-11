# 재작성 준비 인벤토리 (Preparation Inventory)

새 문서 프로젝트로 옮길 재료와 추가 조사 대상을 찾기 위한 자동 생성 목록입니다.
출처 수·구현 후보 수·메모 유무는 관측값이며, 정확성·실행 성공·사람 검토·문서 완성도를 뜻하지 않습니다.

## 집계 기준

- 범위: 학습 영역의 실제 주제 Markdown 파일. README와 아직 파일이 없는 Planned 항목은 제외합니다.
- 직접 출처: `## 참조`, `## 참조 (References)`, `## References` 아래에서 사용하는 명시적 HTTP(S) Markdown 링크의 서로 다른 URL 수입니다. 하위 섹션도 포함합니다.
- 인라인·참조형·각괄호 자동링크를 인식합니다. 코드·HTML 주석·이미지·단독 URL·예약 예시 도메인·로컬 주소는 제외합니다. 같은 URL의 반복은 한 번만 세며, URL의 fragment/query가 다르면 별도로 셉니다.
- 링크가 살아 있는지, 원문이 주장을 뒷받침하는지는 확인하지 않습니다. 본문에만 있는 외부 링크와 중앙 참고목록을 가리키는 상대링크는 직접 출처 수에 포함하지 않습니다.
- 구현 후보: 언어가 지정된 코드 fence 수에서 텍스트(text/txt/plaintext/plain/none), Mermaid, 수식(math/latex/tex)을 제외합니다. 셸 명령·설정·의사코드도 포함될 수 있으며 실행하지 않습니다.
- 메모: `## 재작성 메모 (Rewrite Notes)` 제목의 존재 여부입니다. 내용의 충실도는 판단하지 않습니다.
- `missing-source`·`missing-notes`는 집계 대상 링크·제목이 없다는 뜻입니다. `unclosed-code-fence`는 닫히지 않은 코드 fence가 있다는 뜻입니다. 모두 작업 대상을 찾기 위한 표시입니다.
- 파서는 이 저장소의 ATX 제목과 최대 3칸 들여쓴 backtick/tilde fence를 대상으로 합니다. 모든 CommonMark 문법을 지원하지는 않습니다.

## 영역별 요약

전체 주제 524개 중 직접 출처가 있는 문서는 20개, 재작성 메모가 있는 문서는 7개입니다.

| 영역 | 주제 수 | 출처 있음 | 출처 없음 | 구현 후보 블록 | 메모 있음 | 메모 없음 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| AI | 191 | 2 | 189 | 355 | 1 | 190 |
| Algorithms | 34 | 1 | 33 | 35 | 1 | 33 |
| CS-Theory | 30 | 1 | 29 | 30 | 1 | 29 |
| Data-Structures | 17 | 0 | 17 | 26 | 0 | 17 |
| Engineering | 113 | 12 | 101 | 83 | 2 | 111 |
| Math | 52 | 2 | 50 | 100 | 1 | 51 |
| Programming | 33 | 2 | 31 | 84 | 1 | 32 |
| Systems | 54 | 0 | 54 | 55 | 0 | 54 |

## 주제별 재료

| 문서 | Status | 직접 출처 수 | 구현 후보 블록 | 재작성 메모 | 확인할 표시 |
| --- | --- | ---: | ---: | --- | --- |
| [AI/AI-Safety/Activation-Patching.md](../AI/AI-Safety/Activation-Patching.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Adversarial-Examples.md](../AI/AI-Safety/Adversarial-Examples.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/AI-Regulation.md](../AI/AI-Safety/AI-Regulation.md) | Draft | 3 | 2 | 없음 | missing-notes |
| [AI/AI-Safety/AI-Risk-Classification.md](../AI/AI-Safety/AI-Risk-Classification.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Alignment-Overview.md](../AI/AI-Safety/Alignment-Overview.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Attention-Visualization.md](../AI/AI-Safety/Attention-Visualization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Capability-Evaluation.md](../AI/AI-Safety/Capability-Evaluation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Certified-Robustness.md](../AI/AI-Safety/Certified-Robustness.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Dangerous-Capability-Evaluation.md](../AI/AI-Safety/Dangerous-Capability-Evaluation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Fairness-Bias.md](../AI/AI-Safety/Fairness-Bias.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Feedback-Limitations.md](../AI/AI-Safety/Feedback-Limitations.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Mechanistic-Interpretability.md](../AI/AI-Safety/Mechanistic-Interpretability.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/OOD-Generalization.md](../AI/AI-Safety/OOD-Generalization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Poisoning-Attacks.md](../AI/AI-Safety/Poisoning-Attacks.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Probing-Classifiers.md](../AI/AI-Safety/Probing-Classifiers.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Red-Teaming.md](../AI/AI-Safety/Red-Teaming.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Reward-Hacking.md](../AI/AI-Safety/Reward-Hacking.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/RLHF-Constitutional-AI.md](../AI/AI-Safety/RLHF-Constitutional-AI.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Scalable-Oversight.md](../AI/AI-Safety/Scalable-Oversight.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Sparse-Autoencoder.md](../AI/AI-Safety/Sparse-Autoencoder.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/AI-Safety/Superalignment.md](../AI/AI-Safety/Superalignment.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Causal-DAG.md](../AI/Causal-Inference/Causal-DAG.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Causal-ML.md](../AI/Causal-Inference/Causal-ML.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Causal-Representation.md](../AI/Causal-Inference/Causal-Representation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Confounding.md](../AI/Causal-Inference/Confounding.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Correlation-vs-Causation.md](../AI/Causal-Inference/Correlation-vs-Causation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Counterfactual.md](../AI/Causal-Inference/Counterfactual.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/DiD.md](../AI/Causal-Inference/DiD.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Do-Calculus.md](../AI/Causal-Inference/Do-Calculus.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Identifiability.md](../AI/Causal-Inference/Identifiability.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Instrumental-Variables.md](../AI/Causal-Inference/Instrumental-Variables.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Intervention.md](../AI/Causal-Inference/Intervention.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Mediation.md](../AI/Causal-Inference/Mediation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/Potential-Outcomes.md](../AI/Causal-Inference/Potential-Outcomes.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/RCT.md](../AI/Causal-Inference/RCT.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/RDD.md](../AI/Causal-Inference/RDD.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Causal-Inference/SCM.md](../AI/Causal-Inference/SCM.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/3D-Vision.md](../AI/Computer-Vision/3D-Vision.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Classical-Vision.md](../AI/Computer-Vision/Classical-Vision.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/CNN-Deep-Dive.md](../AI/Computer-Vision/CNN-Deep-Dive.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Image-Basics.md](../AI/Computer-Vision/Image-Basics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Image-Classification.md](../AI/Computer-Vision/Image-Classification.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Image-Generation.md](../AI/Computer-Vision/Image-Generation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Instance-Segmentation.md](../AI/Computer-Vision/Instance-Segmentation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Object-Detection.md](../AI/Computer-Vision/Object-Detection.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Optical-Flow.md](../AI/Computer-Vision/Optical-Flow.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Pose-Estimation.md](../AI/Computer-Vision/Pose-Estimation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Semantic-Segmentation.md](../AI/Computer-Vision/Semantic-Segmentation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Video-Understanding.md](../AI/Computer-Vision/Video-Understanding.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Computer-Vision/Vision-Language.md](../AI/Computer-Vision/Vision-Language.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Activation-Functions.md](../AI/Deep-Learning/Activation-Functions.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Attention.md](../AI/Deep-Learning/Attention.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Backpropagation.md](../AI/Deep-Learning/Backpropagation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/CNN.md](../AI/Deep-Learning/CNN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Dropout.md](../AI/Deep-Learning/Dropout.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Fine-Tuning.md](../AI/Deep-Learning/Fine-Tuning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/GNN.md](../AI/Deep-Learning/GNN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Loss-Functions.md](../AI/Deep-Learning/Loss-Functions.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/MLP.md](../AI/Deep-Learning/MLP.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Normalization-Layers.md](../AI/Deep-Learning/Normalization-Layers.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/RNN-LSTM-GRU.md](../AI/Deep-Learning/RNN-LSTM-GRU.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Self-Supervised.md](../AI/Deep-Learning/Self-Supervised.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Transfer-Learning.md](../AI/Deep-Learning/Transfer-Learning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Deep-Learning/Transformer.md](../AI/Deep-Learning/Transformer.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Autoencoders.md](../AI/Generative-Models/Autoencoders.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Beta-VAE.md](../AI/Generative-Models/Beta-VAE.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Conditional-GAN.md](../AI/Generative-Models/Conditional-GAN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/CycleGAN.md](../AI/Generative-Models/CycleGAN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/DCGAN.md](../AI/Generative-Models/DCGAN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/DDIM.md](../AI/Generative-Models/DDIM.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/DDPM.md](../AI/Generative-Models/DDPM.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/EBM.md](../AI/Generative-Models/EBM.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/GAN-Basics.md](../AI/Generative-Models/GAN-Basics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Latent-Diffusion.md](../AI/Generative-Models/Latent-Diffusion.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Normalizing-Flows.md](../AI/Generative-Models/Normalizing-Flows.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Real-NVP.md](../AI/Generative-Models/Real-NVP.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/Score-Based.md](../AI/Generative-Models/Score-Based.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/StyleGAN.md](../AI/Generative-Models/StyleGAN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Generative-Models/VAE.md](../AI/Generative-Models/VAE.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/BERT-Family.md](../AI/LLMs/BERT-Family.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Chain-of-Thought.md](../AI/LLMs/Chain-of-Thought.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Distillation.md](../AI/LLMs/Distillation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/DPO.md](../AI/LLMs/DPO.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Efficient-Attention.md](../AI/LLMs/Efficient-Attention.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Encoder-Decoder.md](../AI/LLMs/Encoder-Decoder.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/GPT-Family.md](../AI/LLMs/GPT-Family.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/In-Context-Learning.md](../AI/LLMs/In-Context-Learning.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Inference-Optimization.md](../AI/LLMs/Inference-Optimization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Instruction-Tuning.md](../AI/LLMs/Instruction-Tuning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/LLM-Agents.md](../AI/LLMs/LLM-Agents.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/PEFT.md](../AI/LLMs/PEFT.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Pretraining.md](../AI/LLMs/Pretraining.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Prompt-Engineering.md](../AI/LLMs/Prompt-Engineering.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Quantization.md](../AI/LLMs/Quantization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/RAG.md](../AI/LLMs/RAG.md) | Draft | 3 | 2 | 있음 | - |
| [AI/LLMs/RLHF.md](../AI/LLMs/RLHF.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/LLMs/Transformer-Advanced.md](../AI/LLMs/Transformer-Advanced.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Bias-Variance.md](../AI/Machine-Learning/Bias-Variance.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Cross-Validation.md](../AI/Machine-Learning/Cross-Validation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Decision-Trees.md](../AI/Machine-Learning/Decision-Trees.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Dimensionality-Reduction.md](../AI/Machine-Learning/Dimensionality-Reduction.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Ensemble.md](../AI/Machine-Learning/Ensemble.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Hierarchical-Clustering.md](../AI/Machine-Learning/Hierarchical-Clustering.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/K-Means.md](../AI/Machine-Learning/K-Means.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/KNN.md](../AI/Machine-Learning/KNN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Linear-Regression.md](../AI/Machine-Learning/Linear-Regression.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Logistic-Regression.md](../AI/Machine-Learning/Logistic-Regression.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Overfitting.md](../AI/Machine-Learning/Overfitting.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/Regularization.md](../AI/Machine-Learning/Regularization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Machine-Learning/SVM.md](../AI/Machine-Learning/SVM.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/AB-Testing.md](../AI/MLOps/AB-Testing.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Data-Drift.md](../AI/MLOps/Data-Drift.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Data-Labeling.md](../AI/MLOps/Data-Labeling.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Data-Validation.md](../AI/MLOps/Data-Validation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Data-Versioning.md](../AI/MLOps/Data-Versioning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Distributed-Training.md](../AI/MLOps/Distributed-Training.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Experiment-Tracking.md](../AI/MLOps/Experiment-Tracking.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Feature-Store.md](../AI/MLOps/Feature-Store.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Feedback-Loop.md](../AI/MLOps/Feedback-Loop.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/GPU-Cluster.md](../AI/MLOps/GPU-Cluster.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/gRPC-Serving.md](../AI/MLOps/gRPC-Serving.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Hyperparameter-Tuning.md](../AI/MLOps/Hyperparameter-Tuning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/ML-Pipeline.md](../AI/MLOps/ML-Pipeline.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Model-Monitoring.md](../AI/MLOps/Model-Monitoring.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Model-Optimization.md](../AI/MLOps/Model-Optimization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Model-Registry.md](../AI/MLOps/Model-Registry.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Online-vs-Batch-Serving.md](../AI/MLOps/Online-vs-Batch-Serving.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Reproducibility.md](../AI/MLOps/Reproducibility.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/REST-Serving.md](../AI/MLOps/REST-Serving.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/MLOps/Streaming-vs-Batch.md](../AI/MLOps/Streaming-vs-Batch.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Attention-in-NLP.md](../AI/NLP/Attention-in-NLP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/NLP/BERT.md](../AI/NLP/BERT.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/GPT.md](../AI/NLP/GPT.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Language-Model-Basics.md](../AI/NLP/Language-Model-Basics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Machine-Translation.md](../AI/NLP/Machine-Translation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/NER.md](../AI/NLP/NER.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Question-Answering.md](../AI/NLP/Question-Answering.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Relation-Extraction.md](../AI/NLP/Relation-Extraction.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/RNN-for-NLP.md](../AI/NLP/RNN-for-NLP.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Summarization.md](../AI/NLP/Summarization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Text-Classification.md](../AI/NLP/Text-Classification.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Text-Preprocessing.md](../AI/NLP/Text-Preprocessing.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/NLP/Transformer-NLP.md](../AI/NLP/Transformer-NLP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/NLP/Word-Embeddings.md](../AI/NLP/Word-Embeddings.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Bayesian-Networks.md](../AI/PGMs/Bayesian-Networks.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Belief-Propagation.md](../AI/PGMs/Belief-Propagation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Cliques.md](../AI/PGMs/Cliques.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/CRF.md](../AI/PGMs/CRF.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/d-Separation.md](../AI/PGMs/d-Separation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/EM-Algorithm.md](../AI/PGMs/EM-Algorithm.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Factorization.md](../AI/PGMs/Factorization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Graph-Review.md](../AI/PGMs/Graph-Review.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/HMM.md](../AI/PGMs/HMM.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/MCMC.md](../AI/PGMs/MCMC.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/MRF.md](../AI/PGMs/MRF.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Naive-Bayes.md](../AI/PGMs/Naive-Bayes.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Variable-Elimination.md](../AI/PGMs/Variable-Elimination.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/PGMs/Variational-Inference.md](../AI/PGMs/Variational-Inference.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Actor-Critic.md](../AI/Reinforcement-Learning/Actor-Critic.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/DQN.md](../AI/Reinforcement-Learning/DQN.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Dynamic-Programming.md](../AI/Reinforcement-Learning/Dynamic-Programming.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Function-Approximation.md](../AI/Reinforcement-Learning/Function-Approximation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Hierarchical-RL.md](../AI/Reinforcement-Learning/Hierarchical-RL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/MDP.md](../AI/Reinforcement-Learning/MDP.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Model-Based-DRL.md](../AI/Reinforcement-Learning/Model-Based-DRL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Monte-Carlo.md](../AI/Reinforcement-Learning/Monte-Carlo.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Multi-Agent-RL.md](../AI/Reinforcement-Learning/Multi-Agent-RL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Offline-RL.md](../AI/Reinforcement-Learning/Offline-RL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Policy-Gradient.md](../AI/Reinforcement-Learning/Policy-Gradient.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Policy.md](../AI/Reinforcement-Learning/Policy.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/PPO.md](../AI/Reinforcement-Learning/PPO.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/SAC.md](../AI/Reinforcement-Learning/SAC.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/TD-Learning.md](../AI/Reinforcement-Learning/TD-Learning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Reinforcement-Learning/Value-Functions.md](../AI/Reinforcement-Learning/Value-Functions.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Bias-Variance-Theory.md](../AI/Theoretical-ML/Bias-Variance-Theory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Convex-Learning.md](../AI/Theoretical-ML/Convex-Learning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Double-Descent.md](../AI/Theoretical-ML/Double-Descent.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Expert-Algorithms.md](../AI/Theoretical-ML/Expert-Algorithms.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/GD-Convergence.md](../AI/Theoretical-ML/GD-Convergence.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Generalization-Bounds.md](../AI/Theoretical-ML/Generalization-Bounds.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Implicit-Regularization.md](../AI/Theoretical-ML/Implicit-Regularization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/MDL.md](../AI/Theoretical-ML/MDL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Multi-Armed-Bandit.md](../AI/Theoretical-ML/Multi-Armed-Bandit.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Mutual-Information.md](../AI/Theoretical-ML/Mutual-Information.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/No-Free-Lunch.md](../AI/Theoretical-ML/No-Free-Lunch.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Non-Convex-Convergence.md](../AI/Theoretical-ML/Non-Convex-Convergence.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/PAC-Learning.md](../AI/Theoretical-ML/PAC-Learning.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Rademacher-Complexity.md](../AI/Theoretical-ML/Rademacher-Complexity.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Regret-Minimization.md](../AI/Theoretical-ML/Regret-Minimization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/Shattering.md](../AI/Theoretical-ML/Shattering.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [AI/Theoretical-ML/VC-Dimension.md](../AI/Theoretical-ML/VC-Dimension.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Algorithms/Aho-Corasick.md](../Algorithms/Aho-Corasick.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Amortized-Analysis.md](../Algorithms/Amortized-Analysis.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Approximation-Algorithms.md](../Algorithms/Approximation-Algorithms.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Backtracking.md](../Algorithms/Backtracking.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Bellman-Ford.md](../Algorithms/Bellman-Ford.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/BFS-DFS.md](../Algorithms/BFS-DFS.md) | Review | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Binary-Search.md](../Algorithms/Binary-Search.md) | Draft | 3 | 2 | 있음 | - |
| [Algorithms/Bipartite-Matching.md](../Algorithms/Bipartite-Matching.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Bitmask-DP.md](../Algorithms/Bitmask-DP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Complexity.md](../Algorithms/Complexity.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Computational-Geometry.md](../Algorithms/Computational-Geometry.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Dijkstra.md](../Algorithms/Dijkstra.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Dinic.md](../Algorithms/Dinic.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Divide-and-Conquer.md](../Algorithms/Divide-and-Conquer.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/DP-Basics.md](../Algorithms/DP-Basics.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/DP-Optimization.md](../Algorithms/DP-Optimization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Fast-Exponentiation.md](../Algorithms/Fast-Exponentiation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/FFT.md](../Algorithms/FFT.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Floyd-Warshall.md](../Algorithms/Floyd-Warshall.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Greedy.md](../Algorithms/Greedy.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/KMP.md](../Algorithms/KMP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Max-Flow.md](../Algorithms/Max-Flow.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/MCMF.md](../Algorithms/MCMF.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/MST.md](../Algorithms/MST.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Number-Theory.md](../Algorithms/Number-Theory.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Parallel-Algorithms.md](../Algorithms/Parallel-Algorithms.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Rabin-Karp.md](../Algorithms/Rabin-Karp.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Randomized-Algorithms.md](../Algorithms/Randomized-Algorithms.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/SCC.md](../Algorithms/SCC.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Sorting.md](../Algorithms/Sorting.md) | Review | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Suffix-Array.md](../Algorithms/Suffix-Array.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Topological-Sort.md](../Algorithms/Topological-Sort.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Tree-DP.md](../Algorithms/Tree-DP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Algorithms/Z-Algorithm.md](../Algorithms/Z-Algorithm.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/AST.md](../CS-Theory/Compilers/AST.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Code-Generation.md](../CS-Theory/Compilers/Code-Generation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Intermediate-Representation.md](../CS-Theory/Compilers/Intermediate-Representation.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Interpreter-vs-Compiler.md](../CS-Theory/Compilers/Interpreter-vs-Compiler.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Lexer.md](../CS-Theory/Compilers/Lexer.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Optimization.md](../CS-Theory/Compilers/Optimization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Parser.md](../CS-Theory/Compilers/Parser.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Compilers/Semantic-Analysis.md](../CS-Theory/Compilers/Semantic-Analysis.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/Complexity-Classes.md](../CS-Theory/Computation-Theory/Complexity-Classes.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/Context-Free.md](../CS-Theory/Computation-Theory/Context-Free.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/Regular-Expressions.md](../CS-Theory/Computation-Theory/Regular-Expressions.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/Regular-Languages.md](../CS-Theory/Computation-Theory/Regular-Languages.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/Turing-Machine.md](../CS-Theory/Computation-Theory/Turing-Machine.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Computation-Theory/Undecidability.md](../CS-Theory/Computation-Theory/Undecidability.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Concurrency-Models.md](../CS-Theory/Programming-Languages/Concurrency-Models.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Lambda-Calculus.md](../CS-Theory/Programming-Languages/Lambda-Calculus.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Memory-Models.md](../CS-Theory/Programming-Languages/Memory-Models.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Paradigms.md](../CS-Theory/Programming-Languages/Paradigms.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Syntax-and-Semantics.md](../CS-Theory/Programming-Languages/Syntax-and-Semantics.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Type-Inference.md](../CS-Theory/Programming-Languages/Type-Inference.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Programming-Languages/Type-Systems.md](../CS-Theory/Programming-Languages/Type-Systems.md) | Draft | 2 | 3 | 있음 | - |
| [CS-Theory/Quantum-Computing/Entanglement.md](../CS-Theory/Quantum-Computing/Entanglement.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Grover.md](../CS-Theory/Quantum-Computing/Grover.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Quantum-Circuits.md](../CS-Theory/Quantum-Computing/Quantum-Circuits.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Quantum-Complexity.md](../CS-Theory/Quantum-Computing/Quantum-Complexity.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Quantum-Error-Correction.md](../CS-Theory/Quantum-Computing/Quantum-Error-Correction.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Quantum-Gates.md](../CS-Theory/Quantum-Computing/Quantum-Gates.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Qubits.md](../CS-Theory/Quantum-Computing/Qubits.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [CS-Theory/Quantum-Computing/Shor.md](../CS-Theory/Quantum-Computing/Shor.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Array.md](../Data-Structures/Array.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Data-Structures/AVL-Tree.md](../Data-Structures/AVL-Tree.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Binary-Tree.md](../Data-Structures/Binary-Tree.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/BST.md](../Data-Structures/BST.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Data-Structures/Deque.md](../Data-Structures/Deque.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Fenwick-Tree.md](../Data-Structures/Fenwick-Tree.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Graph-Representation.md](../Data-Structures/Graph-Representation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Hash-Function.md](../Data-Structures/Hash-Function.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Hash-Table.md](../Data-Structures/Hash-Table.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Heap.md](../Data-Structures/Heap.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Data-Structures/Linked-List.md](../Data-Structures/Linked-List.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Data-Structures/Queue.md](../Data-Structures/Queue.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Data-Structures/Red-Black-Tree.md](../Data-Structures/Red-Black-Tree.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Segment-Tree.md](../Data-Structures/Segment-Tree.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Stack.md](../Data-Structures/Stack.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Data-Structures/Trie.md](../Data-Structures/Trie.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Data-Structures/Union-Find.md](../Data-Structures/Union-Find.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Bisect-Debugging.md](../Engineering/Debugging/Bisect-Debugging.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Breakpoints-and-Stepping.md](../Engineering/Debugging/Breakpoints-and-Stepping.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Canary-Feature-Flags.md](../Engineering/Debugging/Canary-Feature-Flags.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Conditional-Breakpoints.md](../Engineering/Debugging/Conditional-Breakpoints.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Core-Dump-Analysis.md](../Engineering/Debugging/Core-Dump-Analysis.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Deadlock-Detection.md](../Engineering/Debugging/Deadlock-Detection.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Distributed-Log-Correlation.md](../Engineering/Debugging/Distributed-Log-Correlation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Error-Tracking.md](../Engineering/Debugging/Error-Tracking.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Logging-Levels.md](../Engineering/Debugging/Logging-Levels.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Memory-Errors.md](../Engineering/Debugging/Memory-Errors.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Minimal-Reproducible-Example.md](../Engineering/Debugging/Minimal-Reproducible-Example.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Postmortem.md](../Engineering/Debugging/Postmortem.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Race-Condition-Debugging.md](../Engineering/Debugging/Race-Condition-Debugging.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Remote-Debugging.md](../Engineering/Debugging/Remote-Debugging.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Rubber-Duck-Debugging.md](../Engineering/Debugging/Rubber-Duck-Debugging.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Scientific-Debugging.md](../Engineering/Debugging/Scientific-Debugging.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Stack-Traces.md](../Engineering/Debugging/Stack-Traces.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Structured-Logging.md](../Engineering/Debugging/Structured-Logging.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Debugging/Valgrind-AddressSanitizer.md](../Engineering/Debugging/Valgrind-AddressSanitizer.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Ansible.md](../Engineering/DevOps/Ansible.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/AWS-Core-Services.md](../Engineering/DevOps/AWS-Core-Services.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/CICD-Principles.md](../Engineering/DevOps/CICD-Principles.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Cloud-Computing.md](../Engineering/DevOps/Cloud-Computing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Container-Networking-Volumes.md](../Engineering/DevOps/Container-Networking-Volumes.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Deployment-Strategies.md](../Engineering/DevOps/Deployment-Strategies.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Distributed-Tracing.md](../Engineering/DevOps/Distributed-Tracing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Docker-Basics.md](../Engineering/DevOps/Docker-Basics.md) | Draft | 1 | 1 | 없음 | missing-notes |
| [Engineering/DevOps/Docker-Compose.md](../Engineering/DevOps/Docker-Compose.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/GCP-Azure-Overview.md](../Engineering/DevOps/GCP-Azure-Overview.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Git/Git-Basics.md](../Engineering/DevOps/Git/Git-Basics.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md](../Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Git/Git-Conflict-Resolution.md](../Engineering/DevOps/Git/Git-Conflict-Resolution.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Git/Git-Remotes.md](../Engineering/DevOps/Git/Git-Remotes.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Git/Git-Undoing-Changes.md](../Engineering/DevOps/Git/Git-Undoing-Changes.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Git-Internals.md](../Engineering/DevOps/Git-Internals.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/GitHub/GitHub-Actions.md](../Engineering/DevOps/GitHub/GitHub-Actions.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/GitHub/GitHub-Code-Review.md](../Engineering/DevOps/GitHub/GitHub-Code-Review.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/GitHub/GitHub-Flow.md](../Engineering/DevOps/GitHub/GitHub-Flow.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/GitHub/GitHub-Issues-and-Pull-Requests.md](../Engineering/DevOps/GitHub/GitHub-Issues-and-Pull-Requests.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/GitHub/GitHub-Repositories.md](../Engineering/DevOps/GitHub/GitHub-Repositories.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Helm.md](../Engineering/DevOps/Helm.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Jenkins-GitLab-CI.md](../Engineering/DevOps/Jenkins-GitLab-CI.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Kubernetes-Advanced.md](../Engineering/DevOps/Kubernetes-Advanced.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Kubernetes-Basics.md](../Engineering/DevOps/Kubernetes-Basics.md) | Draft | 1 | 2 | 없음 | missing-notes |
| [Engineering/DevOps/Logging-Systems.md](../Engineering/DevOps/Logging-Systems.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Metrics-Alerts.md](../Engineering/DevOps/Metrics-Alerts.md) | Draft | 1 | 1 | 없음 | missing-notes |
| [Engineering/DevOps/Server-Images-and-Snapshots.md](../Engineering/DevOps/Server-Images-and-Snapshots.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Serverless.md](../Engineering/DevOps/Serverless.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/SLI-SLO-SLA.md](../Engineering/DevOps/SLI-SLO-SLA.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/DevOps/Terraform-Basics.md](../Engineering/DevOps/Terraform-Basics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Async-IO.md](../Engineering/Performance/Async-IO.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Benchmarking-Basics.md](../Engineering/Performance/Benchmarking-Basics.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Branch-Prediction.md](../Engineering/Performance/Branch-Prediction.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Cache-Friendly-Code.md](../Engineering/Performance/Cache-Friendly-Code.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/CDN-Caching.md](../Engineering/Performance/CDN-Caching.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/CPU-Profiling.md](../Engineering/Performance/CPU-Profiling.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Database-Query-Optimization.md](../Engineering/Performance/Database-Query-Optimization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/False-Sharing.md](../Engineering/Performance/False-Sharing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Flame-Graphs.md](../Engineering/Performance/Flame-Graphs.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/IO-Profiling.md](../Engineering/Performance/IO-Profiling.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/JIT-Optimization.md](../Engineering/Performance/JIT-Optimization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Lazy-Evaluation.md](../Engineering/Performance/Lazy-Evaluation.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Lock-Contention.md](../Engineering/Performance/Lock-Contention.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Memoization-Caching.md](../Engineering/Performance/Memoization-Caching.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Memory-Layout.md](../Engineering/Performance/Memory-Layout.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Memory-Profiling.md](../Engineering/Performance/Memory-Profiling.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Network-Performance.md](../Engineering/Performance/Network-Performance.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Practical-Complexity.md](../Engineering/Performance/Practical-Complexity.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/SIMD-Vectorization.md](../Engineering/Performance/SIMD-Vectorization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Performance/Thread-Pool-Tuning.md](../Engineering/Performance/Thread-Pool-Tuning.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Security/Asymmetric-Encryption.md](../Engineering/Security/Asymmetric-Encryption.md) | Draft | 3 | 1 | 없음 | missing-notes |
| [Engineering/Security/Auth.md](../Engineering/Security/Auth.md) | Draft | 4 | 1 | 없음 | missing-notes |
| [Engineering/Security/Digital-Signatures.md](../Engineering/Security/Digital-Signatures.md) | Draft | 2 | 1 | 없음 | missing-notes |
| [Engineering/Security/Hash-Functions.md](../Engineering/Security/Hash-Functions.md) | Draft | 3 | 1 | 없음 | missing-notes |
| [Engineering/Security/Network-Security.md](../Engineering/Security/Network-Security.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Security/PKI-and-TLS.md](../Engineering/Security/PKI-and-TLS.md) | Draft | 3 | 1 | 없음 | missing-notes |
| [Engineering/Security/Symmetric-Encryption.md](../Engineering/Security/Symmetric-Encryption.md) | Draft | 3 | 1 | 없음 | missing-notes |
| [Engineering/Security/Web-Security.md](../Engineering/Security/Web-Security.md) | Draft | 4 | 1 | 없음 | missing-notes |
| [Engineering/Security/Zero-Knowledge-Proofs.md](../Engineering/Security/Zero-Knowledge-Proofs.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/Behavioral-Patterns.md](../Engineering/Software-Design/Behavioral-Patterns.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/Clean-Code.md](../Engineering/Software-Design/Clean-Code.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/Creational-Patterns.md](../Engineering/Software-Design/Creational-Patterns.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/Design-Principles.md](../Engineering/Software-Design/Design-Principles.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/Refactoring.md](../Engineering/Software-Design/Refactoring.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/SOLID.md](../Engineering/Software-Design/SOLID.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Software-Design/Structural-Patterns.md](../Engineering/Software-Design/Structural-Patterns.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/Approach.md](../Engineering/System-Design/Approach.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/Caching.md](../Engineering/System-Design/Caching.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/CDN.md](../Engineering/System-Design/CDN.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/Database-Design.md](../Engineering/System-Design/Database-Design.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/Load-Balancing.md](../Engineering/System-Design/Load-Balancing.md) | Draft | 3 | 1 | 있음 | - |
| [Engineering/System-Design/Message-Queues.md](../Engineering/System-Design/Message-Queues.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/Microservices.md](../Engineering/System-Design/Microservices.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/System-Design/Scalability.md](../Engineering/System-Design/Scalability.md) | Draft | 2 | 1 | 있음 | - |
| [Engineering/System-Design/System-Design-Case-Studies.md](../Engineering/System-Design/System-Design-Case-Studies.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/BDD.md](../Engineering/Testing/BDD.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Boundary-Value-Analysis.md](../Engineering/Testing/Boundary-Value-Analysis.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Code-Coverage.md](../Engineering/Testing/Code-Coverage.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Contract-Testing.md](../Engineering/Testing/Contract-Testing.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Database-Testing.md](../Engineering/Testing/Database-Testing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/E2E-Testing.md](../Engineering/Testing/E2E-Testing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Integration-Test-Strategy.md](../Engineering/Testing/Integration-Test-Strategy.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/K6-JMeter.md](../Engineering/Testing/K6-JMeter.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Load-Stress-Soak-Testing.md](../Engineering/Testing/Load-Stress-Soak-Testing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Mutation-Testing.md](../Engineering/Testing/Mutation-Testing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Static-Analysis-Linting.md](../Engineering/Testing/Static-Analysis-Linting.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/TDD.md](../Engineering/Testing/TDD.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Test-Doubles.md](../Engineering/Testing/Test-Doubles.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Testable-Design.md](../Engineering/Testing/Testable-Design.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Testing-Pyramid.md](../Engineering/Testing/Testing-Pyramid.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/UI-Test-Tools.md](../Engineering/Testing/UI-Test-Tools.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Unit-Test-Principles.md](../Engineering/Testing/Unit-Test-Principles.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Engineering/Testing/Visual-Regression-Testing.md](../Engineering/Testing/Visual-Regression-Testing.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Chain-Rule.md](../Math/Calculus/Chain-Rule.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Differentiation.md](../Math/Calculus/Differentiation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Integration.md](../Math/Calculus/Integration.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Limits.md](../Math/Calculus/Limits.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Multivariable-Integration.md](../Math/Calculus/Multivariable-Integration.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Partial-Derivatives.md](../Math/Calculus/Partial-Derivatives.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Calculus/Taylor-Series.md](../Math/Calculus/Taylor-Series.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Combinatorics.md](../Math/Discrete/Combinatorics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Graph-Theory.md](../Math/Discrete/Graph-Theory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Induction.md](../Math/Discrete/Induction.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Logic.md](../Math/Discrete/Logic.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Recurrences.md](../Math/Discrete/Recurrences.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Relations-and-Functions.md](../Math/Discrete/Relations-and-Functions.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Discrete/Set-Theory.md](../Math/Discrete/Set-Theory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/Determinant.md](../Math/Linear-Algebra/Determinant.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/Eigenvalues.md](../Math/Linear-Algebra/Eigenvalues.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/Linear-Systems.md](../Math/Linear-Algebra/Linear-Systems.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/Matrices.md](../Math/Linear-Algebra/Matrices.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/Orthogonality.md](../Math/Linear-Algebra/Orthogonality.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/PCA.md](../Math/Linear-Algebra/PCA.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Math/Linear-Algebra/SVD.md](../Math/Linear-Algebra/SVD.md) | Draft | 3 | 3 | 있음 | - |
| [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Numerical-Methods/Differentiation-Integration.md](../Math/Numerical-Methods/Differentiation-Integration.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Numerical-Methods/Floating-Point.md](../Math/Numerical-Methods/Floating-Point.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Numerical-Methods/Interpolation.md](../Math/Numerical-Methods/Interpolation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Numerical-Methods/Numerical-Linear-Systems.md](../Math/Numerical-Methods/Numerical-Linear-Systems.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Numerical-Methods/ODE-Solvers.md](../Math/Numerical-Methods/ODE-Solvers.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Numerical-Methods/Root-Finding.md](../Math/Numerical-Methods/Root-Finding.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Optimization/Adaptive-Methods.md](../Math/Optimization/Adaptive-Methods.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Optimization/Convex-Optimization.md](../Math/Optimization/Convex-Optimization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Optimization/Gradient-Descent.md](../Math/Optimization/Gradient-Descent.md) | Draft | 2 | 3 | 없음 | missing-notes |
| [Math/Optimization/Lagrangian.md](../Math/Optimization/Lagrangian.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Optimization/Linear-Programming.md](../Math/Optimization/Linear-Programming.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Optimization/Quadratic-Programming.md](../Math/Optimization/Quadratic-Programming.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Optimization/SGD.md](../Math/Optimization/SGD.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Bayes-Theorem.md](../Math/Probability-Statistics/Bayes-Theorem.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/CLT.md](../Math/Probability-Statistics/CLT.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Distributions.md](../Math/Probability-Statistics/Distributions.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Expectation.md](../Math/Probability-Statistics/Expectation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Hypothesis-Testing.md](../Math/Probability-Statistics/Hypothesis-Testing.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Information-Theory.md](../Math/Probability-Statistics/Information-Theory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Markov-Chains.md](../Math/Probability-Statistics/Markov-Chains.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/MLE.md](../Math/Probability-Statistics/MLE.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Probability-Statistics/Probability-Basics.md](../Math/Probability-Statistics/Probability-Basics.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Continuity.md](../Math/Real-Analysis/Continuity.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Function-Spaces.md](../Math/Real-Analysis/Function-Spaces.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Measure-Theory.md](../Math/Real-Analysis/Measure-Theory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Real-Numbers.md](../Math/Real-Analysis/Real-Numbers.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Riemann-Integration.md](../Math/Real-Analysis/Riemann-Integration.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Sequences-Series.md](../Math/Real-Analysis/Sequences-Series.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Math/Real-Analysis/Uniform-Continuity.md](../Math/Real-Analysis/Uniform-Continuity.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md) | Draft | 0 | 5 | 없음 | missing-source, missing-notes |
| [Programming/Control-Flow.md](../Programming/Control-Flow.md) | Draft | 0 | 4 | 없음 | missing-source, missing-notes |
| [Programming/Functional-Intro.md](../Programming/Functional-Intro.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Functions-and-Recursion.md](../Programming/Functions-and-Recursion.md) | Draft | 0 | 4 | 없음 | missing-source, missing-notes |
| [Programming/Language-Selection.md](../Programming/Language-Selection.md) | Review | 4 | 5 | 없음 | missing-notes |
| [Programming/Languages/C/C-Arrays-Strings-Structs.md](../Programming/Languages/C/C-Arrays-Strings-Structs.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/C/C-Files-and-Builds.md](../Programming/Languages/C/C-Files-and-Builds.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Programming/Languages/C/C-Pointers-and-Memory.md](../Programming/Languages/C/C-Pointers-and-Memory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/C/C-Setup-and-Compilation.md](../Programming/Languages/C/C-Setup-and-Compilation.md) | Draft | 0 | 4 | 없음 | missing-source, missing-notes |
| [Programming/Languages/C/C-Types-and-Control-Flow.md](../Programming/Languages/C/C-Types-and-Control-Flow.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Cpp/Cpp-Classes-and-Templates.md](../Programming/Languages/Cpp/Cpp-Classes-and-Templates.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Cpp/Cpp-Memory-and-Smart-Pointers.md](../Programming/Languages/Cpp/Cpp-Memory-and-Smart-Pointers.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Cpp/Cpp-References-and-RAII.md](../Programming/Languages/Cpp/Cpp-References-and-RAII.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Cpp/Cpp-Setup-and-Syntax.md](../Programming/Languages/Cpp/Cpp-Setup-and-Syntax.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Cpp/Cpp-STL.md](../Programming/Languages/Cpp/Cpp-STL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Java/Java-Classes-and-Objects.md](../Programming/Languages/Java/Java-Classes-and-Objects.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Java/Java-Collections.md](../Programming/Languages/Java/Java-Collections.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Java/Java-Exceptions-and-Files.md](../Programming/Languages/Java/Java-Exceptions-and-Files.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Java/Java-Generics-and-Interfaces.md](../Programming/Languages/Java/Java-Generics-and-Interfaces.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Java/Java-Setup-and-Syntax.md](../Programming/Languages/Java/Java-Setup-and-Syntax.md) | Draft | 0 | 3 | 없음 | missing-source, missing-notes |
| [Programming/Languages/JavaScript/JavaScript-Async.md](../Programming/Languages/JavaScript/JavaScript-Async.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/JavaScript/JavaScript-DOM-and-Events.md](../Programming/Languages/JavaScript/JavaScript-DOM-and-Events.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/JavaScript/JavaScript-Functions-and-Scope.md](../Programming/Languages/JavaScript/JavaScript-Functions-and-Scope.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/JavaScript/JavaScript-Setup-and-Syntax.md](../Programming/Languages/JavaScript/JavaScript-Setup-and-Syntax.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/JavaScript/JavaScript-Values-and-Coercion.md](../Programming/Languages/JavaScript/JavaScript-Values-and-Coercion.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Python/Python-Collections.md](../Programming/Languages/Python/Python-Collections.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Python/Python-Files-and-Errors.md](../Programming/Languages/Python/Python-Files-and-Errors.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Python/Python-Functions-and-Modules.md](../Programming/Languages/Python/Python-Functions-and-Modules.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Python/Python-OOP.md](../Programming/Languages/Python/Python-OOP.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Languages/Python/Python-Setup-and-Syntax.md](../Programming/Languages/Python/Python-Setup-and-Syntax.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/OOP.md](../Programming/OOP.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Pointers-and-Memory.md](../Programming/Pointers-and-Memory.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Programming/Variables-and-Types.md](../Programming/Variables-and-Types.md) | Review | 3 | 5 | 있음 | - |
| [Systems/Computer-Architecture/CPU-and-ISA.md](../Systems/Computer-Architecture/CPU-and-ISA.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/Data-Representation.md](../Systems/Computer-Architecture/Data-Representation.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/Digital-Logic.md](../Systems/Computer-Architecture/Digital-Logic.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/IO-Systems.md](../Systems/Computer-Architecture/IO-Systems.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/Memory-Hierarchy.md](../Systems/Computer-Architecture/Memory-Hierarchy.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/Parallel-Architecture.md](../Systems/Computer-Architecture/Parallel-Architecture.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/Pipelining.md](../Systems/Computer-Architecture/Pipelining.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Systems/Computer-Architecture/Virtual-Memory-Hardware.md](../Systems/Computer-Architecture/Virtual-Memory-Hardware.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Concurrency-Control.md](../Systems/Databases/Concurrency-Control.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Database-Normalization.md](../Systems/Databases/Database-Normalization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Distributed-DB.md](../Systems/Databases/Distributed-DB.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Systems/Databases/NoSQL.md](../Systems/Databases/NoSQL.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Query-Optimization.md](../Systems/Databases/Query-Optimization.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Recovery.md](../Systems/Databases/Recovery.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Relational-Model-and-SQL.md](../Systems/Databases/Relational-Model-and-SQL.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Systems/Databases/Transactions-and-ACID.md](../Systems/Databases/Transactions-and-ACID.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/CAP-Theorem.md](../Systems/Distributed-Systems/CAP-Theorem.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Consensus.md](../Systems/Distributed-Systems/Consensus.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Distributed-System-Case-Studies.md](../Systems/Distributed-Systems/Distributed-System-Case-Studies.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Distributed-Transactions.md](../Systems/Distributed-Systems/Distributed-Transactions.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Message-Queues-Event-Streaming.md](../Systems/Distributed-Systems/Message-Queues-Event-Streaming.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Partitioning.md](../Systems/Distributed-Systems/Partitioning.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Replication.md](../Systems/Distributed-Systems/Replication.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/System-Models.md](../Systems/Distributed-Systems/System-Models.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Distributed-Systems/Time-and-Ordering.md](../Systems/Distributed-Systems/Time-and-Ordering.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/CDN-and-Load-Balancing.md](../Systems/Networks/CDN-and-Load-Balancing.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/DNS.md](../Systems/Networks/DNS.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/HTTP.md](../Systems/Networks/HTTP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/IP-and-Routing.md](../Systems/Networks/IP-and-Routing.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/Network-Models.md](../Systems/Networks/Network-Models.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/Network-Security-Basics.md](../Systems/Networks/Network-Security-Basics.md) | Draft | 0 | 0 | 없음 | missing-source, missing-notes |
| [Systems/Networks/Physical-and-Link.md](../Systems/Networks/Physical-and-Link.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/Socket-Programming.md](../Systems/Networks/Socket-Programming.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Networks/TCP-UDP.md](../Systems/Networks/TCP-UDP.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Deadlock.md](../Systems/Operating-Systems/Deadlock.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/File-Systems.md](../Systems/Operating-Systems/File-Systems.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/IO-and-Drivers.md](../Systems/Operating-Systems/IO-and-Drivers.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Linux/Linux-File-System.md](../Systems/Operating-Systems/Linux/Linux-File-System.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Linux/Linux-Packages-and-Logs.md](../Systems/Operating-Systems/Linux/Linux-Packages-and-Logs.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Linux/Linux-Processes-and-Services.md](../Systems/Operating-Systems/Linux/Linux-Processes-and-Services.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Linux/Linux-Shell-Basics.md](../Systems/Operating-Systems/Linux/Linux-Shell-Basics.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Linux/Linux-Users-Permissions.md](../Systems/Operating-Systems/Linux/Linux-Users-Permissions.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Memory-Management.md](../Systems/Operating-Systems/Memory-Management.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Processes-and-Threads.md](../Systems/Operating-Systems/Processes-and-Threads.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Scheduling.md](../Systems/Operating-Systems/Scheduling.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Synchronization.md](../Systems/Operating-Systems/Synchronization.md) | Draft | 0 | 2 | 없음 | missing-source, missing-notes |
| [Systems/Operating-Systems/Virtual-Memory.md](../Systems/Operating-Systems/Virtual-Memory.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Parallel-Computing/GPU-and-CUDA.md](../Systems/Parallel-Computing/GPU-and-CUDA.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Parallel-Computing/Multithreading.md](../Systems/Parallel-Computing/Multithreading.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Parallel-Computing/OpenMP-MPI.md](../Systems/Parallel-Computing/OpenMP-MPI.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Parallel-Computing/Parallel-Models.md](../Systems/Parallel-Computing/Parallel-Models.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Parallel-Computing/Parallel-Scalability.md](../Systems/Parallel-Computing/Parallel-Scalability.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |
| [Systems/Parallel-Computing/SIMD.md](../Systems/Parallel-Computing/SIMD.md) | Draft | 0 | 1 | 없음 | missing-source, missing-notes |

## 다시 생성하기

저장소 루트에서 실행합니다. 생성 시각을 넣지 않아 같은 입력은 같은 결과를 만듭니다.

```powershell
python Maintainers/Scripts/build_preparation_inventory.py --write
python Maintainers/Scripts/build_preparation_inventory.py --check
python Maintainers/Scripts/build_preparation_inventory.py --format json
```

JSON은 원문 경로·내용 해시·출처 URL과 줄 번호·코드 언어와 범위·메모 위치를 포함합니다. Markdown 보고서의 `--check`는 집계/표시가 바뀌었는지만 비교하며, 일반 본문 변경 전체를 감지하는 검사는 아닙니다.
