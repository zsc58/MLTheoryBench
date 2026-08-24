# PaperProof 大规模实验最终统计报告

## 1. 报告范围

本文档汇总 PaperProof 首轮大规模实验的最终运行结果。统计对象为 2026 年 1 月 1 日至 7 月 27 日收集的 3,320 篇论文，实验在虚拟机上以 10 并发完成，默认模型为 Get-Codex 提供的 `gpt-5.6-sol`，reasoning effort 为 `high`。

统计来源为远端最终运行目录：

```text
/home/ubuntu/ml-theory-run/stage3-full-2026-final-20260820
```

主批处理已于 2026 年 8 月 24 日 07:16（香港时间）结束。初次运行发现的少量工程失败随后均已重跑；针对极少数 evaluator 输出契约特例做了局部工程微调，未改变 triage、formalization、solver 或数学评分标准。最终 3,320 篇论文全部形成合法终态，没有 `pending`、`running` 或 `failed` 样本。

## 2. 核心结论

1. 3,320 篇输入论文中，1,204 篇形成了完整且可评分的 paper-level proof task，占 36.3%；1,007 篇在理论贡献筛选阶段被排除，1,109 篇在后续 source audit 或验证环节停止。
2. 评分范围为 0–10 分。在 1,204 个已评分任务中，平均分为 7.74，中位数为 10；761 个任务得到 8–10 分，占 63.2%，其中 616 个得到满分，本轮没有 0 分任务。
3. Proof Reconstruction Complexity（PRC）与 solver 得分呈清晰的单调关系：PRC0 到 PRC4 的平均分依次为 9.94、9.60、8.58、6.72 和 4.18。将 PRC0–PRC4 编码为 0–4 后，与得分的描述性 Pearson 相关系数为 -0.690。
4. 按当前 benchmark suitability 映射，64 个 PRC0 任务属于 `reject`，385 个 PRC1 属于 `baseline`，490 个 PRC2–PRC3 属于 `primary`，265 个 PRC4 属于 `stress`。因此，排除 PRC0 后的候选任务数为 1,140，严格的 `primary + stress` 主评测候选数为 755。
5. Thread A 在 2,313 篇进入 source audit 的论文中，对 1,291 篇记录了至少一个 paper-level theory issue，占 55.8%。这是保守的自动化审计信号，不等同于“55.8%的论文存在经人工确认的错误”。
6. 整次运行共调用模型 25,148 次，消耗约 1.375B input/output tokens。按项目采用的官方等价价格估算为 8,610.24 美元；按中转价格约为官方十分之一估算，约为 861.02 美元。

## 3. 输入数据

### 3.1 数据来源

| 数据来源 | 论文数 | 占总输入 |
|---|---:|---:|
| primary `stat.ML` | 1,583 | 47.7% |
| ML-related primary `math.OC` | 289 | 8.7% |
| primary `cs.LG`, cross-listed `stat.ML` | 1,448 | 43.6% |
| **总计** | **3,320** | **100.0%** |

`math.OC` 论文在数据收集阶段根据标题和摘要进行 ML 相关性筛选。选择 2026 年论文的主要目的是降低精确论文证明进入 solver 训练数据的概率，但该做法不能完全排除训练污染。

### 3.2 正文来源格式

| Agent 可读正文 | 论文数 | 占比 |
|---|---:|---:|
| arXiv HTML | 2,066 | 62.2% |
| MinerU extract | 991 | 29.8% |
| TeX source | 263 | 7.9% |
| **总计** | **3,320** | **100.0%** |

PDF 并不是 agent 的必要输入。实验优先使用结构化的 HTML 或 TeX；没有合适结构化来源时使用 MinerU extract。

## 4. 最终流程状态

### 4.1 总体状态

| 最终状态 | 论文数 | 占比 |
|---|---:|---:|
| `completed` | 1,204 | 36.3% |
| `stopped` | 1,109 | 33.4% |
| `filtered_out` | 1,007 | 30.3% |
| **总计** | **3,320** | **100.0%** |

`completed` 表示论文已经生成 public task、private reference proof、rubric、PRC、solver proof、validity review 和 final evaluation。1,204 个 completed package 全部具备这些预期文件，没有发现结构缺失。

`filtered_out` 表示论文没有进入正式 formalization。`stopped` 表示论文原本进入了后续流程，但出现确认的 source issue 或无法稳定解决的验证异议。最终数据中没有工程失败终态。

### 4.2 各数据来源的状态

| 数据来源 | 总数 | Completed | Stopped | Filtered |
|---|---:|---:|---:|---:|
| `stat.ML` | 1,583 | 600（37.9%） | 573（36.2%） | 410（25.9%） |
| ML-related `math.OC` | 289 | 123（42.6%） | 103（35.6%） | 63（21.8%） |
| `cs.LG` cross `stat.ML` | 1,448 | 481（33.2%） | 433（29.9%） | 534（36.9%） |

`cs.LG` cross `stat.ML` 的筛除比例最高，达到36.9%；ML-related `math.OC` 的 completed 比例最高，达到42.6%。这些差异同时受到前置来源选择、论文理论结构和样本组成影响，不能直接解释为某一类别“质量更高”。

### 4.3 Filtered-out 原因

| 原因 | 论文数 | 占全部输入 | 占 Filtered |
|---|---:|---:|---:|
| `paper_not_theory_core` | 686 | 20.7% | 68.1% |
| `paper_too_weak` | 320 | 9.6% | 31.8% |
| `no_suitable_flagship_chain` | 1 | <0.1% | 0.1% |
| **总计** | **1,007** | **30.3%** | **100.0%** |

在 3,320 篇论文中，模型将 686 篇归为 `empirical_or_method_only`、598 篇归为 `theory_auxiliary`、2,036 篇归为 `theory_core`。

所有初次返回 `filtered_out` 的论文都经过独立 triage audit。936 篇被直接确认；71 篇的 contribution summary、inventory 或分类字段得到修正，其中70篇修正后仍然筛除，1篇被纠正为 `proceed`。独立复核确实提供了回退通道，但在本轮中实际救回率较低。

### 4.4 Stopped 原因

| 原因 | 论文数 | 占 Stopped |
|---|---:|---:|
| `paper_issue` | 743 | 67.0% |
| `max_validation_feedback` | 320 | 28.9% |
| `evaluator_unscorable` | 46 | 4.1% |
| **总计** | **1,109** | **100.0%** |

`paper_issue` 表示所有合格旗舰 chain 均被 source audit 中的阻断性 statement/proof 问题覆盖。`max_validation_feedback` 表示 solver 与 reviewer 的两轮总回退预算耗尽后仍无法形成稳定可评分任务。`evaluator_unscorable` 表示此前步骤未能发现的问题最终由 evaluator 判定为不可评分。

后两类合计366篇，在最终互斥质量映射中记为 `suspect`，而不是确认的论文错误。

## 5. Contribution Triage、Chain Selection 与 Source Audit

### 5.1 理论材料恢复

Turn A1 在 3,320 篇有效 triage 中共记录 46,394 个浅层理论材料条目，平均每篇 13.97 个，中位数 13 个。材料包括 13,827 个 `theory_candidate`、11,555 个 `internal_support`、14,255 个 `definition` 和 6,757 个 `external`。

这些条目用于恢复论文整体理论结构。它们不是最终公开任务的小题列表，也不是独立 benchmark 样本。

### 5.2 Flagship chain 选择

2,314 篇论文进入 target selection，其中2,313篇至少生成一条可选 chain，仅1篇因没有合适的旗舰 chain 被筛除。

| Chain 指标 | 平均数 | 中位数 | 范围 |
|---|---:|---:|---:|
| 每篇评估的 plausible chains | 3.03 | 3 | 1–4 |
| 每篇 CF ≥ 8 的 eligible chains | 2.32 | 2 | 0–4 |
| 最终 chain 中的 theory candidates | 1.84 | 2 | 1–7 |

295 篇论文使用了 lower-ranked fallback chain，占进入 source audit 论文的12.8%。这说明“对全部CF达标chain做 source audit，再选择最高排名且无阻断问题的chain”确实减少了因单一首选结果有错而整篇停止的数量。

### 5.3 Source audit 覆盖范围

2,313 篇论文完成了完整 source audit，共恢复 40,277 个材料记录：

| 材料角色 | 记录数 |
|---|---:|
| `theory_candidate` | 12,882 |
| `internal_support` | 10,523 |
| `definition` | 10,543 |
| `external` | 6,329 |

每篇论文平均恢复17.41个材料记录，中位数17个，四分位区间为13–21个。

### 5.4 Result-level source labels

| 结果类型 | 维度 | Clean | Minor | Major | 总数 |
|---|---|---:|---:|---:|---:|
| Theory candidate | Statement | 8,717（67.7%） | 2,157（16.7%） | 2,008（15.6%） | 12,882 |
| Theory candidate | Proof | 8,390（65.1%） | 1,243（9.6%） | 3,249（25.2%） | 12,882 |
| Internal support | Statement | 8,842（84.0%） | 1,072（10.2%） | 609（5.8%） | 10,523 |
| Internal support | Proof | 8,488（80.7%） | 939（8.9%） | 1,096（10.4%） | 10,523 |

这里的 `minor` 表示可以通过局部、source-grounded 且不改变实质结论的修复解决；`major` 表示 statement 需要实质修改，或 theorem-critical proof gap 在认真补全后仍无法闭合。

这些记录不是彼此独立的“错误个数”。一个上游结果的 major issue 会沿依赖关系传播到下游证明，因此多个 major-gap 标签可能来自同一根源。同时，这些判断来自自动化 source audit，尚不能当作论文错误率发布。

## 6. 最终任务与 PRC

### 6.1 PRC 分布

| PRC | Benchmark suitability | 任务数 | 占 Completed |
|---|---|---:|---:|
| PRC0 | `reject` | 64 | 5.3% |
| PRC1 | `baseline` | 385 | 32.0% |
| PRC2 | `primary` | 314 | 26.1% |
| PRC3 | `primary` | 176 | 14.6% |
| PRC4 | `stress` | 265 | 22.0% |
| **总计** |  | **1,204** | **100.0%** |

按当前规则，正式可保留任务数为：

- `baseline + primary + stress`：1,140篇，占全部输入的34.3%；
- `primary + stress`：755篇，占全部输入的22.7%；
- `stress`：265篇，占全部输入的8.0%。

### 6.2 PRC 各维度

PRC在 solver 运行前完成，四个 intrinsic dimensions 均按0–3评分；Proof-Route Exposure（E）单独评估。

| Intrinsic dimension | 平均分 | 中位数 |
|---|---:|---:|
| Strategy Discovery（S） | 1.96 | 2 |
| Subgoal Structure and Dependency（D） | 1.75 | 2 |
| Technical Reasoning and Execution（T） | 1.83 | 2 |
| Capability Integration（C） | 2.13 | 2 |

最终任务中，1,084篇为E0，120篇为E1；没有E2或E3进入最终 solver 阶段。E2/E3意味着公开题面暴露了过多证明路线，必须回退修改后重新评估，因此最终分布中不应出现E2/E3。

每个任务平均包含4.60个 solver obligations 和4.24种 materially different capabilities。Evaluator 最终用于评分的 core steps 平均为4.04个，中位数4个。

## 7. Solver 得分

### 7.1 总体得分分布

| 得分 | 任务数 | 占比 |
|---:|---:|---:|
| 0 | 0 | 0.0% |
| 1 | 44 | 3.7% |
| 2 | 66 | 5.5% |
| 3 | 79 | 6.6% |
| 4 | 55 | 4.6% |
| 5 | 53 | 4.4% |
| 6 | 51 | 4.2% |
| 7 | 95 | 7.9% |
| 8 | 16 | 1.3% |
| 9 | 129 | 10.7% |
| 10 | 616 | 51.2% |
| **总计** | **1,204** | **100.0%** |

评分范围为0–10分。总体平均分为7.74，中位数为10，四分位数为6和10。761个任务得到8–10分，占63.2%；297个任务得到1–5分，占24.7%。本轮没有最终得分为0的 completed task，但0分仍是评分标准中的有效档位。

### 7.2 得分与 PRC

| PRC | N | 平均分 | 中位数 | 10分 | 8–10分 | 1–5分 |
|---|---:|---:|---:|---:|---:|---:|
| PRC0 | 64 | 9.94 | 10 | 60（93.8%） | 64（100.0%） | 0（0.0%） |
| PRC1 | 385 | 9.60 | 10 | 312（81.0%） | 355（92.2%） | 4（1.0%） |
| PRC2 | 314 | 8.58 | 10 | 180（57.3%） | 236（75.2%） | 39（12.4%） |
| PRC3 | 176 | 6.72 | 7 | 44（25.0%） | 73（41.5%） | 61（34.7%） |
| PRC4 | 265 | 4.18 | 3 | 20（7.5%） | 33（12.5%） | 193（72.8%） |

PRC 与实际表现之间不仅有均值差异，也表现为分布整体迁移：PRC0全部达到8分以上，而72.8%的PRC4任务只得到1–5分。按0–4编码的PRC与得分的描述性Pearson相关系数为 -0.690。

这个结果是当前最强的校准信号，但仍需谨慎解释：PRC是序数标签；PRC与得分由同一主要模型家族参与产生；相关性目前只在一个 solver 配置上观察到。后续应使用其他裸模型和组内 agent 复测。

### 7.3 各论文来源的得分

| 数据来源 | Completed | 平均分 | 中位数 |
|---|---:|---:|---:|
| `stat.ML` | 600 | 7.58 | 9 |
| ML-related `math.OC` | 123 | 7.15 | 9 |
| `cs.LG` cross `stat.ML` | 481 | 8.09 | 10 |

`cs.LG` cross `stat.ML` 的已完成任务平均分最高，`math.OC` 最低。不过各来源的PRC组成不同，例如 `math.OC` 的123个任务中有39个PRC4，而 `cs.LG` 的481个任务中有86个PRC4。因此，未经分层建模的来源均分不能直接归因于领域本身。

## 8. Reviewer 与 Evaluator

### 8.1 Validity reviewer

Reviewer 在看不到 private proof 和 rubric 的情况下得到：

| Reviewer verdict | 数量 | 占比 |
|---|---:|---:|
| `valid_complete` | 654 | 54.3% |
| `valid_with_minor_issue` | 114 | 9.5% |
| `incomplete_major_gap` | 436 | 36.2% |

Evaluator 结合 private reference 后的最终 validity resolution 为616个 `valid_complete`、145个 `valid_with_minor_issue` 和443个 `incomplete_major_gap`。相较独立 reviewer，最终评分阶段将一部分表面完整的证明调整为 minor 或 major，整体略微更严格。

### 8.2 Final evaluator verdict

| Evaluator verdict | 数量 | 对应分数 |
|---|---:|---|
| `fully_correct` | 616 | 10 |
| `minor_repair` | 145 | 8–9 |
| `substantial_partial_progress` | 333 | 3–7 |
| `minimal_progress` | 110 | 1–2 |
| `incorrect` | 0 | 0 |

231个答案被识别为采用了与 reference 不同的 alternative proof route，占19.2%。这说明 evaluator 并非只接受原论文路线，但该标签本身仍由模型判断，需要在后续人工审计中抽查。

### 8.3 Artifact 与 reference 问题

| Reference issue | 数量 | 占比 |
|---|---:|---:|
| `none` | 1,128 | 93.7% |
| `repairable_ground_truth_error` | 58 | 4.8% |
| `repairable_task_formalization_error` | 16 | 1.3% |
| `repairable_core_step_omission` | 2 | 0.2% |

Public task 状态为1,179个 `clean`、7个 `minor_typo`、17个 `repairable_formalization_error` 和1个 `material_target_error`。Ground truth 状态为1,112个 `clean`、39个 `minor_issue`、44个 `repairable_error` 和9个 `material_error`。

所有 1,204 个 completed task 的 `needs_human_review` 均为 false，这是当前窄化 human-review policy 的结果，不表示所有 artifact 已经得到人工确认。特别是 1 个 `material_target_error` 和 9 个 `material_error` 应在发布前作为优先审计对象。

## 9. 论文问题这一 Side Product

### 9.1 最终互斥质量映射

在进入 source audit 或后续 formalization 的2,313篇论文中：

| Paper-quality mapping | Completed | Stopped | 总数 | 占比 |
|---|---:|---:|---:|---:|
| `clean` | 791 | 0 | 791 | 34.2% |
| `issue` | 413 | 743 | 1,156 | 50.0% |
| `suspect` | 0 | 366 | 366 | 15.8% |
| **总计** | **1,204** | **1,109** | **2,313** | **100.0%** |

`issue` 与 `stopped` 不是同义词。413篇 completed 论文仍带有issue标签，通常表示论文存在有问题的非选中 candidate，但 pipeline 找到了另一条无阻断问题的合格旗舰 chain，或存在允许的局部修复。

`suspect` 对应320篇耗尽验证反馈预算的任务和46篇 evaluator-unscorable 任务。它表示现有链路没有稳定解决异议，不等同于确认原论文有错。

### 9.2 非互斥 source-issue 信号

在2,313篇完成 source audit 的论文中，1,291篇的 `paper_level_theory_issue` 为true，占55.8%。这个字段记录全文 candidate 中是否至少存在一个 major source issue；它可以与最终 `suspect` 重叠，因此不能直接由上面的互斥表相加得到。

当前结果支持把 source issue 作为有价值的附加研究方向，但在正式报告“论文错误率”之前，至少还需要：

- 对 clean、minor 和 major 分层抽取人工样本；
- 区分独立根因与依赖传播产生的下游 major-gap 标签；
- 区分原论文错误、原文抽取错误和 source-audit agent 的误判；
- 报告人工一致率和置信区间，而不是直接发布自动标签比例。

此前50篇校准样本在调整语言后，超过95%的粗分类符合人工预期。这说明 major 的尺度已有较好校准，但不足以证明大规模运行中的每一个具体标签均正确。

## 10. 回退与修订行为

### 10.1 Source re-audit

814篇论文触发了一次 source re-audit，占全部输入的24.5%。每篇最多执行一次。该机制让 source-blind Thread B 在发现记录可能不完整时，只请求 Thread A 记录的局部 statement/proof 范围，而不重新读取整篇论文。

### 10.2 Solver 与 reviewer feedback

| Validation feedback 次数 | 全部论文 | Completed tasks | Completed 平均分 |
|---:|---:|---:|---:|
| 0 | 2,651 | 895 | 8.17 |
| 1 | 331 | 222 | 6.96 |
| 2 | 338 | 87 | 5.29 |

共有669篇论文触发至少一次 solver/reviewer 回传，338篇使用了两次反馈上限。需要更多反馈的 completed task 得分明显更低，这更可能说明复杂或不稳定任务同时更难 formalize 和求解，而不能解释为回退导致得分下降。

初次运行中的少量输出契约异常已通过重跑和局部一致性校验修正，未改变数学判断标准。

## 11. Token、成本与时间

### 11.1 总用量

| Usage | Tokens |
|---|---:|
| Non-cached input | 1,087,597,297 |
| Cached input | 184,591,080 |
| Total input | 1,272,188,377 |
| Output | 102,665,402 |
| **Input + output** | **1,374,853,779** |
| Reasoning output | 38,120,375 |

Reasoning output 是 output tokens 的子集，不能再次加到总量中。Cached input 占总 input 的 14.5%。全流程共记录 25,148 次模型调用，平均每篇论文 7.57 次调用、414,113 tokens。

### 11.2 按角色分解

| Role | Total tokens | Token占比 | 官方等价成本 | 成本占比 |
|---|---:|---:|---:|---:|
| Thread A paper/source agent | 786.47M | 57.2% | $4,492.72 | 52.2% |
| Thread B formalization agent | 427.15M | 31.1% | $2,503.71 | 29.1% |
| Independent triage auditor | 52.56M | 3.8% | $292.77 | 3.4% |
| Reference evaluator | 42.51M | 3.1% | $273.90 | 3.2% |
| Validity reviewer | 35.78M | 2.6% | $308.02 | 3.6% |
| Closed-book solver | 30.39M | 2.2% | $739.11 | 8.6% |
| **总计** | **1,374.85M** | **100.0%** | **$8,610.24** | **100.0%** |

Thread A 与 Thread B 合计消耗 88.3% 的 tokens 和 81.3% 的官方等价成本，是后续优化的主要位置。Solver 只占 2.2% 的 tokens，却因 output token 价格较高而占 8.6% 的成本。

官方等价成本采用以下项目计价假设：non-cached input 为每百万tokens 5美元，cached input 为0.5美元，output 为30美元。按中转价格约为官方十分之一估算，本轮实际成本约为861.02美元。该数字是价格模型估算，不是中转站最终账单。

### 11.3 按终态分解

| 终态 | 平均调用数 | 平均tokens | 官方等价总成本 | 平均每篇成本 |
|---|---:|---:|---:|---:|
| Completed | 11.87 | 579,954 | $4,621.08 | $3.84 |
| Stopped | 7.97 | 516,102 | $3,411.90 | $3.08 |
| Filtered out | 2.01 | 103,508 | $577.26 | $0.57 |

按全部输入摊销，官方等价成本为每篇2.59美元，中转估算为0.259美元。按1,204个 completed task 摊销，分别为7.15美元和0.715美元；按排除PRC0后的1,140个可保留任务摊销，分别约为7.55美元和0.755美元。

Stopped 平均已经消耗 completed 的约89%的tokens，说明许多停止发生在较晚的 source audit 或 validation 阶段。

### 11.4 运行时间

- 创建运行：2026-08-20 23:30（香港时间）；
- 暂停：2026-08-21 11:28；
- 恢复：2026-08-21 21:51；
- 主批处理完成：2026-08-24 07:16；
- 少量失败重跑与终态对齐完成：2026-08-24 17:22；
- 主批处理总墙钟时间：79.77小时；
- 扣除约10.38小时暂停后，估计活跃运行时间为69.39小时；
- 10并发下活跃吞吐约47.9篇/小时，墙钟吞吐约41.6篇/小时。

## 12. 工程完整性

初次运行发现了少量工程失败。重跑后，针对极少数 evaluator 严重性字段一致性特例做了局部工程微调，未修改其他流程或数学评分标准。最终结果中 `failed=0`。

- 1,204个 completed package 全部具备八类预期核心文件；
- 3,320篇全部写入 `pipeline_manifest.json`；
- 最终运行目录占用约1.1GB，其中 paper packages 约1,021MB、logs约14MB、debug attempts约67MB。

## 13. 主要分析与后续建议

### 13.1 当前最可靠的结果

PRC 与 solver 得分之间的单调关系是目前最清晰、最适合对外汇报的结果。它同时体现在平均分、满分率和低分率上，并且跨越了足够大的样本量。下一步应以其他 solver 和组内 agent 复测该趋势，而不是继续调整 PRC 阈值来贴合当前模型。

### 13.2 不应直接得出的结论

- 不能根据50.0%的最终 `issue` 或55.8%的 `paper_level_theory_issue` 断言相同比例的论文存在真实错误；
- 不能根据51.2%的满分率断言模型已经普遍掌握研究级TML证明，因为任务选择、训练污染和 evaluator calibration 都可能抬高得分；
- 不能根据不同arXiv类别的均分直接比较领域难度，因为各类别的PRC和筛选组成不同；
- 不能把 completed 中 `issue` 论文的8.42平均分高于 clean 论文的7.38解释为issue使任务更容易，这很可能来自chain回退、PRC组成和选择偏差。

### 13.3 发布前的最低工作

1. 对1个 `material_target_error`、9个GT `material_error`、46个 evaluator-unscorable 和320个 max-validation 样本优先审计；
2. 对 clean、issue、suspect 与PRC0–4做分层人工抽样，报告人工一致率；
3. 使用至少一个不同裸模型和组内 agent 运行相同任务，检验 PRC 趋势和得分稳定性；
4. 最终发布时同时提供全部 1,204 个已评分 artifact、1,140 个非reject任务索引，以及 755 个 primary/stress 主评测索引，避免混淆不同使用范围。

## 14. 可直接用于汇报的数字

- 输入论文：3,320篇；
- Completed：1,204篇；
- 非PRC0候选任务：1,140篇；
- Primary + stress任务：755篇；
- 评分范围：0–10分，本轮0分任务为0个；
- 平均分：7.74；
- 8–10分比例：63.2%；
- PRC0到PRC4平均分：9.94、9.60、8.58、6.72、4.18；
- PRC与得分的描述性相关：-0.690；
- Source-audited论文：2,313篇；
- 自动记录至少一个paper-level theory issue：1,291篇；
- 模型调用：25,148次；
- 总input/output tokens：1.375B；
- 官方等价成本：8,610.24美元；
- 中转估算成本：861.02美元；
- 主批处理活跃运行时间：约69.4小时；
- 最终工程失败：0篇。
