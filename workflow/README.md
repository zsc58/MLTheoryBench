# PaperProof Workflow

本目录包含复现当前 PaperProof 实验链路所需的 prompts、schemas、templates、代码与测试。论文数据和运行结果单独存放。

目录按功能组织，不依赖旧项目中的 `data/`、`data_v2/` 或 `experiments/` 相对路径。为完成这次整理，Python 文件只修改了模块导入、路径常量和文件名映射；prompt、schema、template、状态机逻辑及回退机制均保持不变。

## 目录结构

```text
workflow/
  AGENTS.md
  README.md

  data_preparation/
    prompts/                 Thread A 与 Thread B prompts
    schemas/                 各 turn 的 JSON 输出契约
    templates/               task、proof GT、rubric 与 provenance 模板
    pipeline/                单篇/批量入口、状态机、契约和 agent runtime
    tests/                   数据准备及回退机制测试

  proof_experiment/
    llm_solver/              裸模型 solver：prompt、模板和 runner

  reviewer_and_evaluator/
    reviewer/                validity reviewer：prompt、schema 和 runner
    evaluator/               reference evaluator：prompt、schema 和 runner

  runtime_support/
    codex/                   Codex SDK 适配层
    formalization/           文件落盘、基础契约和 validation bridge
    experiment/              run 初始化、批处理和汇总工具
    tests/                   solver/reviewer/evaluator 测试
    requirements.txt
```

## 数据准备

### Thread A

1. **Contribution Triage**
   - [`thread_a_turn1_triage.md`](data_preparation/prompts/thread_a_turn1_triage.md)
   - [`thread_a_triage_audit.md`](data_preparation/prompts/thread_a_triage_audit.md)

   识别论文的理论材料与主要贡献，输出 `proceed` 或 `filtered_out`。筛除结果由独立 triage audit 检查。

2. **Flagship Target Selection**
   - [`thread_a_turn2_target_selection.md`](data_preparation/prompts/thread_a_turn2_target_selection.md)

   在不参考候选定理正误的前提下生成和排序 flagship chains。

3. **Source Recovery And Audit**
   - [`thread_a_turn3_source_audit.md`](data_preparation/prompts/thread_a_turn3_source_audit.md)

   从原文恢复 statement、proof、依赖与精确行区间，并分别记录 statement/proof 的错误状态。

### Thread B

1. **Formalization Compile**
   - [`thread_b_turn1_compile.md`](data_preparation/prompts/thread_b_turn1_compile.md)

   从冻结后的 source-audited material closure 生成公开 task、proof ground truth、rubric 与 provenance。

2. **Artifact Audit**
   - [`thread_b_turn2_artifact_audit.md`](data_preparation/prompts/thread_b_turn2_artifact_audit.md)
   - [`thread_b_local_source_check.md`](data_preparation/prompts/thread_b_local_source_check.md)
   - [`thread_b_revision.md`](data_preparation/prompts/thread_b_revision.md)

   检查自洽性、source fidelity、validity、scope、scorability 与 anti-leakage，并处理局部原文核查和下游反馈回退。

3. **Proof Reconstruction Complexity**
   - [`thread_b_turn3_prc_assessment.md`](data_preparation/prompts/thread_b_turn3_prc_assessment.md)

   在 solver 运行前评估 Proof Reconstruction Complexity 与 proof-route exposure。

## 证明与评测

### Bare-Model Solver

- [`run_llm_baseline.py`](proof_experiment/llm_solver/run_llm_baseline.py)
- [`proof_system_prompt.md`](proof_experiment/llm_solver/prompts/proof_system_prompt.md)
- [`proof_answer_template.md`](proof_experiment/llm_solver/prompts/proof_answer_template.md)

Solver 只进行一次裸模型请求，不使用工具、网络、续写或自我修订。未来 agent solver 可继续加入 `proof_experiment/`。

### Validity Reviewer

- [`run_reviewer.py`](reviewer_and_evaluator/reviewer/run_reviewer.py)
- [`system_prompt.md`](reviewer_and_evaluator/reviewer/system_prompt.md)
- [`output_schema.json`](reviewer_and_evaluator/reviewer/output_schema.json)

Reviewer 只读取 task 和去除自评分后的 solver proof，不读取 private GT，也不打分。

### Reference Evaluator

- [`run_evaluator.py`](reviewer_and_evaluator/evaluator/run_evaluator.py)
- [`system_prompt.md`](reviewer_and_evaluator/evaluator/system_prompt.md)
- [`output_schema.json`](reviewer_and_evaluator/evaluator/output_schema.json)

Evaluator 读取 validity report、reference proof 与 rubric，输出 0–10 整数分和错误归属。

## 输入

每篇论文最少需要：

```text
<papers_root>/<paper_id>/
  private_source/
    metadata.json
    source.html | source.tex | extracted_text.md | source.pdf
```

## 环境

```bash
python3 -m venv .venv
.venv/bin/pip install -r workflow/runtime_support/requirements.txt
```

私有运行配置统一放在 gitignored 的 `workflow/.runtime/`：

```text
workflow/.runtime/
  get-codex/
    config.toml
    openai_api_key
  llm.env
  runs/
```

## 运行入口

单篇：

```bash
.venv/bin/python workflow/data_preparation/pipeline/run_stage3_pipeline.py \
  --paper-dir /absolute/path/to/paper_2026_001 \
  --api-profile workflow/.runtime/get-codex \
  --model gpt-5.6-sol \
  --reasoning-effort high \
  --codex-bin "$(command -v codex)"
```

批量：

```bash
.venv/bin/python workflow/data_preparation/pipeline/run_stage3_batch.py \
  --source-papers-root /absolute/path/to/papers \
  --run-root /absolute/path/to/run \
  --paper-ids-file /absolute/path/to/paper_ids.txt \
  --workers 10 \
  --api-profile workflow/.runtime/get-codex \
  --model gpt-5.6-sol \
  --reasoning-effort high \
  --codex-bin "$(command -v codex)"
```

## 测试

```bash
cd workflow
../.venv/bin/python -m unittest discover \
  -s data_preparation/tests -p 'test_*.py'
../.venv/bin/python -m unittest discover \
  -s runtime_support/tests -p 'test_*.py'
```

两组测试共 74 项，不调用外部模型。密钥、论文数据、隔离会话和运行结果不得提交到远程 Git。
