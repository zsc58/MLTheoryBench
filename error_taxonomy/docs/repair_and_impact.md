# 修复难度与结果、论文影响评级

> 本文保留原 07 的正式评级规则，补充 [错误分类](error_taxonomy.md)。A、B、reviewer 使用完全相同的标准；一条 finding 仍只对应一个定理内根错误。

## 0. 三个评价对象，而不是一个“严重性”

错误机制、修复难度与影响程度回答不同问题：

| 对象 | 字段 | 问题 |
|---|---|---|
| 单条 finding | `repair_difficulty_level` | 修正这一处根错误，需要多大的数学改动？ |
| 单个 result node | `result_impact_level` | 诚实修订后，这个结果相对原合同损失多少？ |
| 整篇 paper | `paper_impact_level` | 诚实修订全部受影响结果后，论文主要贡献损失多少？ |

三者都取 $1$--$4$，但含义不同，不得相加、求平均或机械传递。特别地：

- 容易修不等于影响小；
- 技术上难修不等于论文影响大；
- finding 层不再另评所谓“finding severity”；
- 所有层级都不记录 `confidence`。

例如，作者把同一路线实际支持的 $O(n^2)$ 复杂度误写成 $O(n)$。把 statement 改为 $O(n^2)$ 可能是修复难度 1；但如果 $O(n)$ 正是论文相对已有 $O(n\log n)$ 的核心改进，那么 result 影响可为 3，paper 影响可为 4。

## 1. 两种必需 turn 与一种可选传播 turn

### 1.1 Result turn

每个 `theory_candidate` 或 `internal_support` 只用一个 turn，依次完成：

1. 恢复完整原文合同；
2. 裁决已有 issue leads；
3. 审计反例、statement object、proof obligation、inference、calculation 与 dependency；
4. 确认互不重复的根错误 findings；
5. 对每条 finding 评价修复难度；
6. 综合本地 findings 和 inherited blockers，评价唯一的 result 影响。

“先识别错误，再评价修复和影响”只是同一 turn 内的推理顺序，不是第二次模型调用。

### 1.2 Optional propagation turn

全部显式 issue-node result turn 完成后，可以在同一个持久 session 中增加一次传播 turn。它读取已验证 finding 的 honest repair，并沿 `depends_on` 路径检查未标记下游 `theory_candidate` 的原合同是否仍获支持。

该 turn 只输出传播方式、修订后的下游 result summary 与 result impact；不寻找反例、不判断下游 theorem 真假、不发现新错误，也不创建或复制 finding。路径外 proof branches 视为 oracle-correct。没有已验证 finding 或没有 eligible downstream 时不调用模型，paper-level `propagation_audit` 为 `null`。

### 1.3 Paper-summary turn

全部 result turn 完成后，在同一个持久 paper session 中增加一个 summary turn：

1. 读取所有已验证 result audits 和可选 propagation assessment；
2. 回看 abstract、introduction、贡献列表、flagship chain 和已有工作比较；
3. 检查独立结果与替代支撑；
4. 输出唯一的 paper 影响。

该 turn 不得新建、删除、合并、拆分或改类 finding，也不得重评修复难度或 result 影响。如果发现前序结果可疑，只能写入 `paper_open_questions`，交给人工回查。

## 2. 共同参照：选定的诚实修订

### 2.1 为什么需要选修订路线

一处错误常有多种修法。例如，一个 theorem 声称对所有 $m\geq1$ 成立，而 proof 只覆盖 $m\geq m_0$：

- 直接把 statement 改成 $m\geq m_0$，改动容易但损失一段合同；
- 补证有限个 $m<m_0$，工作略多却可能完整保留合同。

如果无规则地总选“最省力”的方案，会高估 result 影响；如果总假设存在最强修法，又会把未经证明的希望当作事实。因此每条 finding 必须记录一条 `selected_honest_repair`。

### 2.2 选择规则

候选修订按以下顺序筛选：

1. 排除空洞、把结论放入假设、为单个反例量身定制、改变成无关问题或纯猜测的伪修复；
2. 先列出由原文正确推导、实际核对过的被引结果或有限局部论证直接支持的修订；
3. 在这组直接／局部修订中，优先保留更多原数学对象和实质合同；保留内容相当时，再选择新增数学工作较少的路线；
4. 每条 finding 只选择一条路线。不能按路线 A 的工作量，却按路线 B 的 surviving contract 评级；改变 objective、oracle、算法输出或理论解释的路线，若改变了原对象或接口，不是普通局部修复；
5. 只有不存在能保留有意义同类结果的直接／局部路线时，才选择核心论证或接口重建；若原合同不能可信保留，则选择原文有效内容支持的最强非平凡弱化结果。

更强但尚未核验的修法可以写入说明，不能因此降低等级或影响。核心重建的预期成功也不等于当前已有支持。影响评级只计入有效原文论证以及明确、有限、与原对象一致的局部补证；未来另行重建关键论证的可能性不降低 result 或 paper impact。

### 2.3 允许与禁止

允许修改：

- proof 的公式、分支、局部 lemma 或推理；
- statement 的假设、定义域、参数范围、rate、概率模式或量词；
- statement 所需对象的定义；
- 必要时的算法接口或步骤。

不允许用来降低难度的伪修复包括：

- 删除 theorem 而不给任何可识别结果；
- 把所需结论本身当作新假设；
- 改成恒真命题或空域命题；
- 只排除已知反例而没有自然数学含义；
- 换成与原节点研究对象和作用无关的新 theorem。

Agent 不必完成一份完整替代证明，但必须把修订路线具体到足以判断数学工作量与剩余合同。

定理自己的局部定义优先决定它的精确合同。不能因为全文叙事通常讨论更窄的模型，就把该限制静默加到一个显式定义了更广对象或 objective 的局部命题上。如果局部命题按其定义正确，但论文叙事对其意义有过强解读，应记为 prose/contract 边界问题，不得为了符合全局语义而制造 theorem finding。

同样，修订必须保持原 theorem 的实际对象。把实际训练模型、自适应算法或实现中的 estimator 替换成 oracle、population construction 或理想 rule aggregator，属于核心接口/算法修改：通常至少是 finding repair Level 3，并往往带来 result impact Level 3。

### 2.4 同一 result turn 内的对象与修订一致性

在本轮内核对原合同、选定修订、`open_questions` 与 `revised_result_summary` 是否一致。原始向量与单位化方向、样本统计量与总体量、固定对象与自适应输出等，须按控制性定义区分。修订改变了哪个对象或定义，应明确说明；会影响结论成立的实质条件须保留到修订后的 result summary，不能让同一个符号静默改变含义，也不能倒过来把修复条件算作原文假设。

原文含义暂不确定，但提出条件性修订，本身允许；必须明确条件，不能随后写成无条件已确立的保证。若不确定性阻止可靠评级，使用现有的 `null` 等级和开放问题。这是同一 turn 内的输出一致性检查，不增加模型阶段、schema 字段，也不要求每个对象差别都单独成为 finding。

## 3. Finding 层：修复难度

### 3.1 局部反事实语义

评价当前 finding 时：

- 假定本 result 中更早发现的独立错误已被正确修复；
- 假定外部定理及上游 result 的原文精确合同为真；
- 只计算修正当前根错误需要的工作；
- 不把它在下游传播多远计入修复难度。

因此 finding 修复难度衡量的是局部数学干预，不是全文后果。

### 3.2 数据结构

```yaml
repair_assessment:
  repair_difficulty_level: 1 | 2 | 3 | 4 | null
  selected_honest_repair: string
  level_rationale: string
```

`selected_honest_repair` 写具体修法；`level_rationale` 解释它为什么消除该根错误，以及为何属于本级。若证据不足，level 为 `null`，两个说明字段仍要指出候选路线和缺失证据。

### 3.3 Level 1：直接修订

修订由原文已有有效内容或一次机械重算直接决定，不需要新的非平凡论证。

典型情形：

- 修正符号、索引、端点、常数或一行公式；
- 重算并把 statement 改成现有 proof 已支持的 rate；
- 增加一个精确 side condition，加入后原 proof 原样成立；
- 缩到 proof 已完整覆盖的明确范围；
- 补一个立即可核验的平凡分支。

Level 1 只说明修订动作直接，不说明结果损失小。

### 3.4 Level 2：有限局部补丁

需要一段有真实数学内容、但边界清晰的局部补证或有限修改；研究对象和主 proof strategy 不变。仅把一个未经证明的条件写进 statement 属于 Level 1，前提是明确选择缩小 statement 且现有 proof 随即原样成立；若要证明原始域本身推出该条件，则是额外工作。

典型情形：

- 补有限个小参数或边界 case；
- 加入一个标准、局部、用途明确的 lemma；
- 完成有限的 comparison、Lipschitz 转换或误差分支；
- 加一个自然条件，作用只限于当前局部接口；
- 用有限局部证明保住原合同，比直接弱化 statement 多做一些工作。

### 3.5 Level 3：核心论证或接口修订

保留一个有意义且可识别的结果，需要新的 theorem-critical 论证、重建关键 lemma，或实质修改核心接口、定义或算法。

典型情形：

- 新的 uniform concentration、coupling、selection 或 identification argument；
- 关键概率接口从 pointwise 改造成 adaptive/simultaneous；
- 重建 proof 的核心 lemma；
- 修改关键算法步骤；
- 原文有效内容不足以直接确定修订后 theorem，但存在具体可信的挽救路线。

### 3.6 Level 4：结构性重建或撤回

有积极的结构证据表明，不存在可信的有限修订可以保留一个同族、可识别的结果；需要重建主要机制、重新设计算法/定义，或撤回节点。

Level 4 不能仅由“agent 没想到修法”推出。若只是证据不足，应记 `null`；若仍有可信但未经完成的核心路线，通常是 Level 3。

## 4. Result 层：合同影响

### 4.1 评价对象

Result 影响综合：

- 当前节点的全部本地 findings；
- `inherited_blocker` 或 `mixed` dependency；
- 各 finding 的选定诚实修订；
- 上游 result 的修订后合同；
- 多个修订合并后的内部一致性。

它回答：

> 完成这些诚实修订后，该节点相对原 statement 损失了多少数学内容与用途？

它不评价客观世界中是否存在一份未知的替代证明。若 proof 把复杂度从 $O(n^2)$ 算成 $O(n)$，我们评价原文可支持的 $O(n^2)$ 版本；找不到否定 $O(n)$ 的全局反例，不会消除这项合同降级。

### 4.2 数据结构与 null 语义

```yaml
result_impact_assessment:
  result_impact_level: 1 | 2 | 3 | 4 | null
  revised_result_summary: string
  impact_explanation: string
  primary_driver_finding_id: string | null
```

- 首先检查资源准入：`audit_status=rejected_missing_proof_source` 的节点不评级，整个 assessment 为 `null`，但不能计作 unaffected；资源标签与具体 typo 允许清单见 [错误分类第 10 节](error_taxonomy.md)。
- 通过资源准入的节点没有本地 finding，也没有 inherited blocker：整个 `result_impact_assessment` 为 `null`；
- 节点已受影响，但证据不足以评级：保留对象，`result_impact_level: null`；
- 非空等级必须选一个本地或上游 finding 作为主要驱动。

含资源 reject 的 paper 在 `paper_open_questions` 说明覆盖限制；只评价其余节点已确认的影响，不因缺失材料提高或降低等级。完整 paper-impact 统计排除这类 paper，但其余通过资源准入节点的 findings 和 result 等级仍可统计。

### 4.3 Level 1：无实质合同损失

修订后原有实质保证和适用制度保留，数学用途不变；至多补上不会删去有意义制度或保证的平凡限定、调整。例如修正 proof 而完整保留合同，或不影响实质用途的平凡边界限定。单纯 typo 和自然记号约定按审计准入规则忽略，不因此新建 finding 或评级。

### 4.4 Level 2：有限但实质的降级

节点仍是同一种结果，主要用途保留，但确实失去了一个非平凡的适用范围、次要分支或保证，或者使用时需要额外的实质条件。非核心常数、log factor 或阈值变化，也要说明它造成了什么实际合同损失，不能仅因公式变了就定级。

判别 Level 1/2 时，在 `impact_explanation` 回答：**原结论以前承诺支持的哪一种数学用途，现在不再获支持？** 若没有实质损失，说明为何变化仅为平凡限定。

- 不能用“改动局部”“一行即可修好”推出 Result 1；这些描述的是修复动作，不是合同损失。
- 排除整个非平凡样本量／维数制度可能只需一行，但仍有实质影响。
- 不能仅凭“增加了条件”推出 Result 2；新增条件也可能只是把无害边界约定写明。
- 条件自然、熟悉或常见，不等于删去的适用范围没有数学内容。
- 衡量的是当前 result 的合同，而非它在整篇论文中的重要性；后者属于 paper impact。

若损失的是本结果的主要保证、核心制度或身份，则继续按 Level 3/4 判断，不因修改有限就停留在 Level 2。

### 4.5 Level 3：主要合同降级

节点仍可识别，却失去主要强度、适用性或算法意义。例如：

- advertised rate 或 complexity order 明显变差；
- adaptive/uniform 退化成 fixed/pointwise；
- high probability 退化成 expectation；
- exact recovery 退化成 approximate recovery；
- global guarantee 退化成 local guarantee；
- polynomial-time 或有限步保证消失；
- 核心参数制度、目标 quantity 或主要适用域被删。

常数、log factor 或范围变化不是自动的 Level 2。如果它本身是论文宣传的核心改进，可以是 Level 3。

### 4.6 Level 4：结果失去原身份

修订后没有与原节点实质相同的非空洞结果，节点必须撤回，或上游诚实修订使它不能再推出。替换成研究对象、算法或结论类型实质不同的新 theorem 也属于本级。

### 4.7 主要驱动 finding

`primary_driver_finding_id` 选择：若消除这条 finding，最能恢复原 result contract 的那一条。

若并列：

1. 选迫使合同变化最大者；
2. 再选 dependency/proof chain 中更有决定作用者；
3. 其他共同原因写入 `impact_explanation`。

上游错误可作为 driver，但不会在当前节点复制成新 finding。

## 5. Paper 层：贡献影响

### 5.1 评价对象

Paper 影响在全部 result 审计后判断：

> 将受影响节点按已选诚实路线修订后，论文当前声称的主要理论贡献还剩多少？

必须结合全文：

- abstract、introduction 和 contribution list；
- flagship theorem 与支撑链；
- 与已有工作的比较优势；
- 是否有独立结果或替代路线保留贡献；
- 受影响节点是中心结果还是可替换的技术支撑。

Paper impact 不是 result impact 的最大值。一个 Level 4 附录结果可能只带来 Paper Level 1；核心复杂度结果 Level 3 可能使 advertised novelty 消失而带来 Paper Level 4。

### 5.2 数据结构与 null 语义

```yaml
paper_impact_assessment:
  paper_impact_level: 1 | 2 | 3 | 4 | null
  impact_summary: string
  remaining_contribution_summary: string
  primary_driver_result_id: string | null
  evidence_locations:
    - source_id: string
      locator: string
```

- 没有任何受影响 result：整个 assessment 为 `null`；
- 论文已受影响但证据不足：保留对象，level 为 `null`；
- 非空等级必须选择一个已审 result，并用原文位置说明论文如何宣传该贡献。

### 5.3 Level 1：主要贡献基本不受影响

错误仅影响局部技术、平凡端点、次要附录结果或可替换支撑；主要 theorem、方法优势和核心 novelty 保持。

### 5.4 Level 2：有实质影响，核心能力仍保留

论文失去非平凡范围、次要保证或限定，但主要数学能力及其定义性的比较优势仍有支持。

### 5.5 Level 3：主要能力显著受损

一个或多个中心结果失去主要数学能力或定义性的比较优势，原整体主张不能维持；论文仍保留同类或独立的有价值贡献。仅因为原句不能原样维持、结果被称为 flagship，或没有找到独立新证明，不足以给 Level 3。

### 5.6 Level 4：核心理论身份不再得到支持

标题／摘要级理论定位、flagship chain 或主要方法保证不再得到支持，且 surviving material 已不能保留该主要数学能力。不能只因为一个摘要句子需要改写就给 Level 4。

### 5.7 主要驱动 result

`primary_driver_result_id` 选择对论文主要贡献的修订影响最大的 affected result，可以来自正式 result audit，也可以来自已验证的 propagation assessment。它描述 contribution-impact driver，不一定是保存 causal root finding 的最上游节点。优先考虑 abstract/introduction 直接依赖且合同确实被改变的 flagship result；其他共同原因写入 `impact_summary`。

## 6. Inherited blocker 的评级

上游 $T_1$ 有 finding，而下游 $T_2$ 正确使用 $T_1$ 原文合同且没有本地错误时：

- $T_2$ 不生成 finding；
- dependency 记 `inherited_blocker`；
- $T_2$ 仍可能需要非空 result impact；
- driver 可以引用 $T_1$ 的 finding ID。

若 $T_1$ 的诚实修订保持 $T_2$ 所需接口，$T_2$ 可为 Level 1；若修订后接口不足以推出 $T_2$，则 $T_2$ 可为 Level 3 或 4。未被完整审计的下游也可通过独立 propagation turn 得到同一口径的 result impact，但该 turn 只检查 repaired interface 对合同的影响，不寻找反例、不判断 theorem 真假、不发现新错误。传播只影响 result/paper 层，不增加根错误计数。

## 7. 不确定性如何表达

本体系不使用任何 `confidence` 字段。原因是模型自报置信度通常不能作为校准后的证据强度，且容易与数学证据本身混淆。

不确定性只通过以下可核查方式表达：

- 候选反例未核完：不纳入 witness 数组，在 `open_questions` 写缺哪项假设核对；
- finding 尚不能成立：不强行建 finding，在 `open_questions` 写所需材料；
- finding 已成立但修复工作量不明：`repair_difficulty_level: null`；
- result 已受影响但剩余合同不明：assessment 对象存在，level 为 `null`；
- paper 已受影响但贡献定位不足：assessment 对象存在，level 为 `null`。

`null` 不是 Level 4，也不是“影响为零”。

## 8. 统计口径

分别报告三个分母：

1. 所有确认 findings 中修复难度 1--4 与 null 的分布；
2. 所有含本地 finding 或 inherited blocker 的 result nodes 中影响 1--4 与 null 的分布；
3. 所有含受影响 result 的 papers 中影响 1--4 与 null 的分布。

Clean result 和 clean paper 不强行记 Level 1。建议报告：

- repair difficulty 按 mechanism/subtype 的分布；
- repair difficulty $\times$ result impact 交叉表；
- result impact $\times$ paper impact 交叉表；
- 哪些 mechanism 常成为 result primary driver；
- 哪些 result 角色常成为 paper primary driver。

这些是 ordinal categories，第一版不计算加权总分或均值。

## 9. 校准案例

下表仅说明通过实质错误准入后的评级关系；如果某个具体端点／符号问题符合 typo 允许清单，应先排除，而非为它生成 Level 1 finding。各例不是对真实论文的审定数据。

| 情形 | Finding repair | Result impact | Paper impact |
|---|---:|---:|---:|
| $n=1$ 时误用未定义的 $\delta_0$，改为 $n\geq2$ 或平移索引 | 1 | 1 | 通常 1 |
| 同一路线正确复杂度为 $O(n^2)$，statement 写成 $O(n)$ | 1 | 通常 3 | 若 $O(n)$ 是核心 novelty，可为 4 |
| proof 漏有限个小 $m$，直接改为 sufficiently large $m$ | 1 | 1--2 | 通常 1--2 |
| 为保留 all-$m$ 合同，需补有限个非平凡构造 | 2 | 1 | 通常 1 |
| fixed-parameter concentration 被用于 data-adaptive choice，需要新 uniform argument | 3 | 通常 3 | 若 adaptivity 是中心主张，可为 3--4 |
| 核心对象/算法在允许输入上失效，局部限制无法保留同类结果 | 4 | 4 | 若是旗舰方法，可为 4 |

## 10. 最终原则

1. 错误机制、修复难度、result 影响和 paper 影响分开。
2. Repairability 只在 finding 层；severity 只在 result 与 paper 两层。
3. 每个 result 用一个 turn 同时完成 finding 和前两种评级。
4. 全部 result 后只加一个 paper-summary turn。
5. 一条 finding 对应一个根错误；传播不生成新 finding。
6. 先尽量保留可信的核心合同，再在同等保留度下最小化修订工作。
7. 容易修不等于影响小，高影响也不等于技术上难修。
8. 未找到全局反例不降低已确认 proof error 的修复或影响等级。
9. 不使用模型 `confidence`；证据不足时使用有明确语义的 `null` 与开放问题。
10. 三级 ordinal 结果分别统计，不制造单一总分。
