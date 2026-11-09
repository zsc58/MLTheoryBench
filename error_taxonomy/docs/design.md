# 设计总览：论文理论错误分类与影响审计

## 1. 研究对象与三个层级

本模块读取已经标记了 source-level issue 的论文材料，独立核查原文错误，再分类和评级。它不评价 solver 答案，不重新做 Thread A 的贡献发现或旗舰链选择，也不将原 issue 标签当作真值。

三个评价尺度彼此独立，均为 1–4 级：

| 评价尺度 | 评价单位 | 核心问题 |
|---|---|---|
| Repair difficulty | 一条 finding | 修正这处根错误需要多少新的数学工作？ |
| Result impact | 一个定理／结果节点 | 原文有效论证及明确局部补证，还能保留多少原合同？ |
| Paper impact | 一篇论文 | 已确认的损坏影响了多少主要理论贡献？ |

容易修不等于影响小；影响大不等于命题已被证明为假。具体四档定义见 [评级规则](repair_and_impact.md)。

分类和计数的单位是 finding，不是文章或节点。一篇论文包含多个节点，一个节点可以有多个独立错误；同一错误的重复表述、上下游传播和两次审计重复发现均不能重复计数。

## 2. 数据入口与范围

正式批量运行接收显式论文清单。每篇使用完整文本表示，以及包含 `material_records` 的最新原文审计。若输入最终 `paper_analysis.json`，取其中 `/source_audit`，而非优先采用可能过时的首次 Turn-3 文件。后来 chain 检查回写到节点的状态随之生效；尚未回写但精确定位的线索可通过 `later_chain_leads_file` 提供。

只选择以下角色中有明确标记的节点：

- `theory_candidate` 或 `internal_support`；
- statement 状态为 `minor_issue`、`major_issue`，或 proof 状态为 `minor_error`、`major_gap`，或有对应的 later-chain lead。

未标记节点、definition 和 external result 留在 inventory 中供上下文与依赖核查，不自动加入完整审计队列。`stopped`、`max_validation_feedback`、`evaluator_unscorable` 和目录名本身不能生成错误 finding。正式样本名单应另外保留选样口径，不能把已标记样本中的比例称为全部 ML 论文错误率。

文本必须覆盖声明的论文版本及相关附录。软件能核对文件、字段、哈希和引用，但不能仅靠字节数证明全文完整。模型须先执行 proof-resource gate；完全因材料缺失而没有证明的节点单独 reject，不算 clean，也不算 theorem failure。

## 3. 双独立审计加 reviewer

```text
同一份全文＋最新原始线索＋inventory
    ├── 会话 A：逐 result 审计 → A 的 paper impact
    └── 会话 B：逐 result 审计 → B 的 paper impact
                     ↓
新 reviewer 会话：每轮审定一个 result 的 A/B 候选并集
                     ↓
最终 paper-summary turn → reviewer 版 paper_audit.json
```

独立性指会话和输入信息隔离：B 不看到 A；不意味着同模型判断在统计上独立。每个会话首轮注入全文和共同标准，随后在同一会话内逐节点处理。节点依据输入中声明的 `depends_on` 按依赖优先排序；这不是另一个模型生成的完备证明图谱。

一个普通 result turn 同时完成：完整合同核查、原 lead 裁决、错误定位与分类、反例核验、每条 finding 的 repair、依赖记录和总体 result impact。不另开“补证明／评修复”的第二阶段。

Reviewer 首轮取得与独立审计完全相同的数学标准，再加一份流程补充。每个节点按顺序：

1. 依据全文核查原合同与每个候选是否实质存在，先排除 typo、审计过严与 artifact；
2. 将 A/B 对同一根错误的描述去重，必要时拆开原来混在一起的独立错误；
3. 每条保留的根错误只选一个大类、一个小类；
4. 选择一条符合共同规则的诚实修复，重评 repair；
5. 独立核验反例，而不从 proof 有错推出 theorem 假；
6. 根据先前 reviewer 的 canonical findings 重建依赖，再评整个 result；
7. 所有节点完成后，才输入 A/B 的 paper-impact 意见，依据最终 reviewer ledger 评论文影响。

两次一致不是数学证据，两次分歧也不要求取平均或较高等级。Reviewer 是候选并集的裁决，不是第三轮不限范围发现；无关的新疑点放入 `open_questions`。最终 paper-summary 不得回写 finding 或 result 等级。

## 4. 核心分类与证据

四大类分别是陈述对象失效、证明义务缺口、推理步骤失效、计算步骤失效，共 17 个小类。完整定义和边界见 [分类规则](error_taxonomy.md)。同根优先级为：

$$
\text{陈述对象失效}>\text{证明义务缺口}>\{\text{推理步骤失效},\text{计算步骤失效}\}.
$$

这不是给整条定理四选一。后一步即使授予前一步正确仍独立出错，应再建 finding；仅由前一步错误导致的后果不另计。

为什么把定理真假与 proof 错误分开？发现 proof 把同一路线的 $O(n^2)$ 算成 $O(n)$，已足以确认计算错误，但未必能排除另有 $O(n)$ 证明。找反例有能力与搜索范围限制，不能据此改变实际失效操作的类别。对象失效则特殊：对象本身不存在或无意义时，即使后续条件推演顺畅也无法表达原结论，所以它单独成类。

`theorem_failure` 的两个数组分别保存对象失效 findings（内嵌见证）和其他全局反例。两者都空为 `undetermined`，否则为 `proven_erroneous`。所有纳入的见证须符合全文控制性假设；未核完的候选只留开放问题。

## 5. 修复参照与传播

先在原文有效内容和明确有限局部补证支持的修订中，优先保留更多原合同，再比较工作量。不能以一条路线的工作量配另一条路线的剩余保证，也不能把结论塞入假设当作修复。

独立重建核心论证的可能性可以说明修复方向，却不能仅凭预期成功降低 result/paper impact。高等级也不能仅由“模型找不到修法”推出，须定位实际损坏和贡献损失。

审计下游 $T_2$ 的本地错误时，把上游 $T_1$ 的精确原合同当作 oracle：正确使用上游但继承其错误，只记 dependency，不复制 finding。评级时则代入已确认的上游修订，并检查下游究竟用了上游哪一部分；那部分若仍保留，不能机械传递高等级。

正式双评＋reviewer 批量路径保持已经测试的配置：有审计节点间 dependency 和最终 paper impact，不额外启用 propagation turn。原有独立审计 runner 的显式 `--enable-propagation-audit` 能力及配套 prompt/schema 保留：它只评上游修订对未标记下游合同的影响，不新建错误、不找反例。不能把 A/B 未经 reviewer 审定的 propagation 输出直接混入最终结论；若未来要在双评流程启用它，应单独明确 reviewer 传播规则。

## 6. 最终数据与复现

- `paper_audit.json`：数学记录，以 paper 为顶层；含 inventory、原 leads、各节点合同、findings、反例、依赖与 impact。
- `review_provenance.json`：每条 A/B 候选如何保留、合并、拆分或驳回；不把两次重复发现再计为两个错误。
- `manifest.json`：每个会话实际输入暴露、prompt/schema hash、session ID、各 turn 状态、输出 hash 和 usage。
- `attempt.json` 与 `batch_status.json`：阶段成功／失败与最终采用路径。失败保留；续跑不覆盖成功、不替换论文。

结构和语义校验能发现漏裁 lead、重复候选、非法 ID、越界依赖或不一致的空值，不是数学正确性证书。摘要统计以完整完成的配对论文为主；缺 proof 节点排除，含此类节点的 paper 单列覆盖不足。失败尝试的已观测 usage 单列，不能当作零。

所有 raw inputs、prompts 的实例化全文、运行记录和真实论文元数据都是私有数据。公开代码目录只保存通用程序、通用提示词、schema 和方法文档；独立 source auditor 的全文输入不得流入闭卷 solver。

## 7. 文献与项目自身设计

当前真正使用的五篇文献见 [引用清单](references.md)，分别支撑可观察错误分类、常规 gap 的排除、错误与可修复性的区别、论文级影响不等同定理级失效，以及同行审计的证据限制。

四大类／17 小类的最终组合、同根优先级、顺序反事实去重、三级四档评级、固定候选并集的双评＋reviewer，是本项目结合理论 ML 数据和讨论形成的操作设计；不是任何一篇文献原有的现成 taxonomy。
