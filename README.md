# PaperProof

PaperProof 用于评测 AI 系统能否重建机器学习理论结果的证明。项目以 2026 年公开论文作为私有 ground truth，solver 只接收去身份化的闭卷证明任务，再由独立 reviewer 和 evaluator 检查并按参考证明与 rubric 评分。

## 仓库结构

| 目录 | 作用 |
|---|---|
| `workflow/` | 完整可复现链路：paper triage、flagship chain 选择、formalization、闭卷 solver、reviewer、evaluator、schemas、调度代码与测试。 |
| `reports/` | 面向汇报和论文写作的项目设计报告与图示。 |

## 数据说明

本仓库当前不发布原始数据包。原始包含论文来源、私有 ground truth 和 evaluator 所需参考材料，仅在本地保存，不得暴露给闭卷 solver 或推送到远程 Git。去身份化的公开任务与数据索引将在完成 anti-leakage 审查后单独发布。

## 当前工作流

1. Thread A 完成理论贡献 triage、flagship chain 选择和原文恢复/审计。
2. Thread B 构建并审查自洽的公开证明任务，再评估 proof-reconstruction complexity。
3. 闭卷 solver 只看到 public task，不能使用工具、网络或检索。
4. Validity reviewer 在不读参考证明的情况下检查 solver proof。
5. Reference evaluator 根据私有 ground truth 和 rubric 对可评分答案给出分数。

可运行实现见 [`workflow/README.md`](workflow/README.md)，对外报告见 [`reports/README.md`](reports/README.md)。
