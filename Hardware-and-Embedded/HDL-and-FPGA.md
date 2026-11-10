# HDL과 FPGA 설계 (HDL and FPGA)

- Level: Intermediate
- Prerequisites: [디지털 논리](../Systems/Computer-Architecture/Digital-Logic.md), 이진수와 상태 전이
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (핵심 원리와 제한된 검증 모형)

---

## 개념 (Concept)

HDL은 시간에 따른 하드웨어의 동작과 연결을 표현하는 언어다. FPGA는 구성 가능한 논리·레지스터·연결 자원을 이용해 회로를 구현한다. HDL 프로그램의 문장 수와 실제 회로 크기, 소프트웨어 실행 시간은 같은 척도가 아니다. 이 문서는 동기식 RTL과 작은 카운터의 검증을 다루고, 보드별 핀 배치·전원·고속 인터페이스는 다루지 않는다.

## 직관 (Intuition)

소프트웨어의 반복문은 대개 한 처리기가 같은 명령을 여러 번 실행한다. 합성 가능한 고정 반복은 여러 하드웨어 연결로 펼쳐질 수 있다. 순차회로에서는 클록 에지 전 상태에서 다음 상태를 계산하고 에지에서 저장한다. “값을 지금 읽는가, 다음 에지에 저장하는가”가 중요하다.

## 이론 (Theory)

조합회로는 현재 입력의 함수이고, 순차회로는 저장된 상태가 있다. 아래 카운터의 상태 $q$는 동기 리셋이 참이면 0, 아니고 enable이면 $(q+1)\bmod16$, 그 외에는 이전 값이다.

시뮬레이션은 주어진 입력 파형에서 모델 동작을 확인한다. 합성은 RTL을 논리 네트워크로 변환하고, 배치·배선은 실제 자원과 연결에 대응한다. [Yosys 합성 안내](https://yosyshq.readthedocs.io/projects/yosys/en/latest/getting_started/example_synth.html)는 이 중 합성 변환의 흐름을 설명한다. 시뮬레이션 통과만으로 핀·타이밍·전원 조건이 충족되지는 않는다.

동일 클록의 단순 레지스터 경로에서 setup 제약은 대략 $T_{clk}\ge t_{cq}+t_{comb}+t_{setup}$로 볼 수 있다. 실제 분석에는 클록 skew·jitter와 불확실성을 추가한다. hold는 가장 빠른 경로의 별도 제약이므로 클록을 느리게 한다고 항상 해결되지 않는다. 비동기 입력은 메타안정성을 만들 수 있어 동기화·CDC 설계가 필요하다.

## 구현 (Implementation)

독립적으로 작성한 Verilog 예제다. 동기식 active-high 리셋이며 초기 상태는 리셋을 거치기 전 보장하지 않는다.

```verilog
module counter4 (
    input wire clk, input wire reset, input wire enable,
    output reg [3:0] count
);
    always @(posedge clk) begin
        if (reset)
            count <= 4'd0;
        else if (enable)
            count <= count + 4'd1;
    end
endmodule
```

테스트벤치에서는 클록 하강 에지에 입력을 바꾸고 다음 상승 에지의 갱신 후 값을 검사한다. 다음은 SystemVerilog 파일로 두 모듈을 함께 저장할 때의 예다.

```systemverilog
module tb;
    reg clk = 0, reset = 1, enable = 0;
    wire [3:0] count;
    counter4 dut(clk, reset, enable, count);
    always #5 clk = ~clk;
    initial begin
        @(posedge clk); #1;
        if (count !== 0) $fatal(1, "reset");
        @(negedge clk); reset = 0; enable = 1;
        repeat (16) @(posedge clk);
        #1;
        if (count !== 0) $fatal(1, "wrap");
        @(negedge clk); enable = 0;
        @(posedge clk); #1;
        if (count !== 0) $fatal(1, "hold");
        $display("PASS");
        $finish;
    end
endmodule
```

Icarus Verilog가 설치된 환경에서 예상 실행 방법은 아래와 같다. 현재 환경에서는 실행하지 않았다.

```sh
iverilog -g2012 -s tb -o counter-test counter.sv
vvp counter-test
```

같은 상태 전이의 Python 참조 모델은 시뮬레이터 없이 검산할 수 있다.

```python
def step(count, reset, enable):
    return 0 if reset else ((count + 1) & 15 if enable else count)

q = step(7, True, True)
assert q == 0
for expected in list(range(1, 16)) + [0]:
    q = step(q, False, True)
    assert q == expected
assert step(q, False, False) == q
assert step(9, True, False) == 0
```

## 복잡도 (Complexity)

4비트 상태와 증가·선택 논리가 필요하지만 LUT 개수는 대상 소자와 합성 최적화에 따라 다르다. 클록당 한 번 상태가 바뀌며, 최대 주파수는 실제 배치·배선과 타이밍 분석으로 정한다. Python 모델은 기능 명세를 확인할 뿐 RTL 문법·이벤트 의미·물리 타이밍을 검증하지 않는다.

## 응용 (Applications)

카운터는 타이머·주소 생성·패킷 길이 추적의 구성 요소다. 같은 방법으로 상태 전이표를 만든 뒤 FIFO의 empty/full, FSM의 불법 상태 복귀를 검사할 수 있다.

## 흔한 오해 (Common Misunderstandings)

- HDL의 모든 문법이 합성된다: 지연문과 테스트벤치의 제어는 시뮬레이션용일 수 있다.
- 레지스터에 초기값이 자동으로 정해진다: 목표 소자와 초기화·리셋 명세를 확인해야 한다.
- 비동기 버스의 각 비트에 동기화기를 붙이면 충분하다: 각 비트가 다른 시점에 관측되어 일관되지 않은 값이 될 수 있다.

## TMI

- 조합 블록에서 모든 분기에 출력을 대입하지 않으면 의도하지 않은 래치가 추론될 수 있다.
- 테스트벤치도 이벤트 순서가 중요하다. 에지와 동시에 입력 변경·출력 검사를 하면 race가 생길 수 있다.

## 연습 / 확인 문제 (Exercises)

1. reset과 enable이 함께 1이면? **답:** reset 우선이므로 0이다.
2. $t_{cq}=0.4$, $t_{comb}=3.0$, $t_{setup}=0.6$ns이면 불확실성을 제외한 최소 주기는? **답:** 4ns, 이상화된 상한 250MHz. 보드 동작 보장값은 아니다.
3. 테스트벤치에 무엇을 더 넣겠는가? **판단 기준:** enable 중간 중단, 동작 중 reset, 모든 상태 전이, CDC 또는 타이밍 검사가 기능 검사와 다르다는 점을 제시한다.

## 이어서 읽기 (Reading Path)

- 이전: [회로 기초](Circuits-and-Electronics.md).
- 다음: [실시간 설계](Embedded-Real-Time-Design.md).
- 관련: [파이프라이닝](../Systems/Computer-Architecture/Pipelining.md).

## 참조 (References)

- [Yosys Synthesis starter](https://yosyshq.readthedocs.io/projects/yosys/en/latest/getting_started/example_synth.html) — 합성 과정과 타깃 종속 변환. 본문의 카운터·테스트벤치는 별도 작성했다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 상태 전이 명세, 카운터 RTL·테스트벤치·Python 참조 모델, 기능/물리 검증 구분.
- 보충할 내용: HDL 시뮬레이션 실행 기록, 보드별 제약 파일, CDC·FIFO 예제, 정적 타이밍 보고서 해석.
- 확인 상태: 2026-09-18 Yosys 합성 안내 확인. HDL 시뮬레이터·합성 도구·보드가 없어 HDL 실행과 합성·타이밍 검증은 미실시. Python 모델 검산은 별도로 기록한다. Python 3.12/Windows에서 본문의 Python 1개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
