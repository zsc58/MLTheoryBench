# 错误分类与审计规则

> 分类对象是原论文中的**错误 finding**，不是论文主题，也不是给整篇论文或整个定理强选一个标签。本文保留原 05 的四大类、17 小类与判定规则。正式运行使用独立 A/B 审计加 reviewer；以下单次审计结构在每个会话内分别执行，整体见 [设计说明](design.md)。

## 0. 三层基本单位

### 0.1 Paper：运行与存储的顶层单位

每篇论文的每次独立审计建立一个持久 session；A、B 与 reviewer 彼此不共用 session。独立审计首轮输入：

- 当前英文 taxonomy prompt；
- 论文完整 TeX、HTML 或抽取表示；
- 完整 Thread-A Turn-3 source audit；
- 全篇 later-chain issue leads；
- paper-level result inventory；
- 待审 result-node 队列；
- 精简的 result-node output schema。

随后在同一 thread 中每轮只审一个 `theory_candidate` 或 `internal_support`。Runner 对被选节点按已声明依赖做 dependency-first 拓扑排序；每轮同时输出本节点 findings、每条 finding 的修复难度以及本节点总体影响。结果通过 schema 和语义校验后加入该 paper 的上游 ledger，供后续节点判断 blocker、接口误用和修订后合同。全部 result turn 完成后，再进行唯一一次 paper-summary turn；runner 最终组装 paper-level JSON。

Paper 层只保存一次：

- `paper_id` 与理论主题；
- source registry：真实路径、来源种类与表示 fidelity；
- 完整 result inventory，包括 Turn-3 状态与声明的 `depends_on`；
- 原始 issue-lead registry；
- 目标 result IDs；
- 各 result-node audits。

模型、thread ID、token、prompt/schema hash、私有文件暴露清单等工程信息另存在 run manifest，不混入数学 taxonomy 数据。

### 0.2 Result node：每轮审计容器

一个被审计的定理、引理、命题、推论或未编号理论 claim 称为一个 result node。独立审计节点只取 Thread A 中的 `theory_candidate` 与 `internal_support`；definition 和 external result 可以进入 paper inventory 和依赖图，但不作为本流程的独立 target。

每个 result node 恢复完整合同：

$$
\mathcal A \Longrightarrow \mathcal C,
$$

其中 $\mathcal A$ 包含正式 statement、paper/section standing assumptions、量词、参数范围、定义域和上游结果的精确接口，$\mathcal C$ 是原文实际声称的结论。

必须先核查局部 statement 和控制性定义，再纳入确实支配该节点的共同假设。每项从上下文引入的限制都须找到它支配本结果的声明；共享符号、研究动机或叙述性解释不能替代这个依据。局部显式定义了更广对象时，不得默默换成全文中更窄的模型。反例也必须在同一份完整合同下核验。

### 0.3 Finding：分类与计数的原子单位

Finding 是一处可定位、可给出数学理由的原论文根错误。它至少回答：

- 根错误是什么；
- 为什么原步骤无效或为什么证明义务未完成；
- 属于四类机制中的哪一类及哪个小类；
- 精确原文位置；
- 它与哪些输入 issue leads 对应；
- 在反事实修复哪些前序错误后仍然独立存在；
- 该根错误的最小诚实修订及修复难度。

`finding_id` 就是该定理内根错误的稳定标识。`error_statement` 用一句话陈述根错误，`mathematical_reason` 展开数学论证。不再另设重复的 `root_cause`、`summary` 或跨 finding 的 root-cause group。

两个缺陷若需要不同修复，且修复前一条后后一条仍然存在，就拆成两条 findings。若多个表面异常只需同一个数学修复，则它们是同一根错误的 manifestations，只建一条 finding。

## 1. 四类根错误与唯一归属

每个节点都检查四个方面：

1. `theorem_failure.statement_object_findings`：陈述对象失效；
2. `findings.proof_obligation`：证明义务缺口；
3. `findings.inference`：推理步骤失效；
4. `findings.calculation`：计算步骤失效。

这不是对整个 result node 四选一。一个节点可以有多条独立根错误，分布在多个数组；但同一根错误只能进入一个数组。

唯一归属优先级为：

$$
\text{statement-object}
\;>\;
\text{proof obligation}
\;>\;
\{\text{inference},\text{calculation}\}.
$$

### 1.1 Statement-object 优先于 proof obligation

若全合同见证已经证明 statement 所需对象不存在、非有限、类型不合法或不取到，而 proof 又恰好漏证该性质，只建 statement-object finding。Proof omission 是同一根错误的低层表现，写入 `mathematical_reason` 和 `locations`，不再建立 obligation 副本。

### 1.2 Proof obligation 优先于同根的局部表现

若同一块未覆盖的 domain、branch、component 或 terminal bridge 同时表现为某个引理误用、范围越界或局部公式失败，根错误归 proof obligation；use site 是证据，不再建立 inference/calculation 副本。

但如果作者已经明确尝试处理完整参数域，只是尝试中的计算或推断本身错了，那么该部分已经被“处理”，应归 inference 或 calculation，不能因为正确修正后到不了原结论，又复制一条 obligation finding。

### 1.3 Inference 与 calculation 互斥

保持证明策略、数学对象和所用结果不变：

- 仅通过重新计算同一个局部表达式即可确认错误：calculation；
- 需要指出定理条件、逻辑关系、量词、概率对象或结构转移无效：inference。

两者没有高低优先级，但同一根错误不能双标。证据不足时写入 `open_questions`，不为了展示两种视角而建两条 findings。

## 2. 定理失效证据与 proof 错误正交

我们不要求先解决 theorem 真假，才允许审计 proof。定理失效模块为：

```text
theorem_failure
├── status
├── statement_object_findings
└── other_global_counterexamples
```

`status` 只有：

- `proven_erroneous`：两个正面数组至少一个非空；
- `undetermined`：两个数组都为空。

`undetermined` 绝不表示 theorem 正确，只表示本次审计没有找到已经核验的全局失效见证。某一步推不出来、solver 未补出证明、evaluator 不可评分、或无误差控制的数值失败，都不是全局反例。

普通反例必须逐项核验：

- 满足原文全部 standing assumptions、量词和参数范围；
- 使用原文对象，而非 formalizer 的删减或误写版本；
- 精确指出合同的哪个结论成分失败；
- 关键计算已解析核验，或属于有严格控制的 exact computer-assisted argument。

未核完的候选构造只写进 `open_questions`。

反例不决定 proof finding 的类别。例如作者声称复杂度 $O(n)$，而 proof 明确写出 $n$ 轮、每轮 $O(n)$，却合并成 $O(n)$。沿同一路线正确结果是 $O(n^2)$，所以这是 calculation finding。即使我们尚不能证明不存在另一个 $O(n)$ 实现，这条 source error 仍然成立。

Statement-object 是唯一例外：对象失效既提供定理反例，又是一种无法由后三个 proof 机制表达的 statement error，因此对象失效见证直接内嵌在对应 finding 中。

## 3. 陈述对象失效（statement-object invalidity）

### 3.1 定义

只检查 theorem 为表达结论而必须使用的对象是否存在、有限、类型正确、可行或取到。它不是“一切缺假设”的收纳箱，也不包括“对象有意义但性质说错”的普通假命题。

例如，定理称 $d(P,Q)$ 为取值于 $[0,\infty)$ 的 metric，但允许的 $P,Q$ 上可能有 $d(P,Q)=+\infty$，属于对象非有限。若 $d(P,Q)$ 始终有限，但三角不等式不成立，则只是一条普通反例；仍需根据原文实际证明错误进入后三类之一。

### 3.2 小类

所有大类中的小类都按实际失效的数学操作或对象要求选择，不按定理主题或证明中出现的词汇分类；下述排除说明不新增类别或改变一条根错误只归一类的规则。

#### `undefined_or_nonfinite_statement_object`

Statement 所需的量、逆、积分、期望、距离或其他对象在允许输入上可能未定义或非有限。

#### `type_structure_or_representation_invalidity`

对象被当作属于不兼容的 codomain、函数空间、代数结构、可测类或表示，导致 statement 中的构造或运算不合法。

#### `feasible_object_solution_or_witness_nonexistence`

Statement 需要的可行点、解、certificate、selector、coupling、estimator 或其他见证在原假设下未必存在。

#### `extremum_optimizer_or_selection_nonattainment`

Infimum/supremum 作为数值可以存在，但 statement 要求的 optimizer、argmin/argmax、measurable selection 或 attained extremum 未必存在。

排除：顺序统计量的索引超出样本范围，属于对象未定义；不能因为定义涉及排序或最小值就归为最优值未取到。

每条对象失效 finding 必须包含 `invalidity_witness`，记录构造、逐项假设核对、失效的合同成分、核验方式和原文位置。

## 4. 证明义务缺口（proof-obligation gap）

### 4.1 定义

假定 proof 中每个可识别的尝试步骤都由 oracle 正确完成，证明骨架仍没有覆盖 theorem 要求的一部分。实际 proof 只支持：

$$
\mathcal A\cap\mathcal R \Longrightarrow \mathcal C',
$$

而 theorem 要求：

$$
\mathcal A\Longrightarrow\mathcal C.
$$

Finding 保存：

- `extra_conditions`：proof 实际增加的 $\mathcal R$；
- `supported_conclusion`：proof 实际支持的 $\mathcal C'$；
- `missing_obligation`：相对原合同具体缺什么。

### 4.2 小类

#### `omitted_component_term_or_branch`

整个 proof 没有处理一个必要成分、事件、case branch、算法分支或分解部分。

- 纳入：风险分解有 bias 与 variance，只分析 bias；
- 排除：已经写出应含全部项的展开式，但局部代数漏了一项；后者归 calculation。

#### `endpoint_boundary_or_degenerate_case_uncovered`

Theorem 覆盖端点、边界、零噪声、奇异或其他退化输入，但 proof 没有任何分支或论证处理它。

- Statement 为 $\lambda\in[0,2]$，proof 只处理 $(0,2)$ 且没有端点论证：obligation；
- Proof 明确把只在 $(0,2)$ 成立的中间公式用于端点：该端点已被尝试，通常归 inference。

#### `parameter_dimension_or_asymptotic_regime_uncovered`

Proof 只覆盖 sample size、dimension、parameter、horizon、regularity 或 asymptotic regime 的真子集，且没有其余制度的有效 reduction。

例如只证 $m\geq m_0$ 却声明所有 $m\geq1$；或 expansion 只在 $d^2/n\to0$ 下成立，却声明任意 $d,n\to\infty$。

#### `terminal_conclusion_or_critical_bridge_gap`

完成所有已尝试步骤后，仍只得到不同的结论或缺少一个非平凡终点桥梁。例如：

- expectation 与 high probability；
- pointwise 与 uniform；
- proxy quantity 与 theorem target；
- 缺失 identification、existence、comparison 或 algorithmic guarantee。

如果 proof 根本没有 concentration/tail bridge，从期望界跳到高概率界，是 obligation。若 proof 明确尝试 Bernstein/Markov，但条件误用，且修正该尝试即可闭合，则是 inference。

末句仅写“显然”“因此”或“由引理可得”，不自动构成对缺失义务的尝试。反过来，短引用也可以是真正有效的证明：先核查被引结果的接口、代入和原文已经具备的条件；不能仅因没有展开常规核验就记为 gap。判断依据是有没有实际覆盖该义务，而不是证明字数。

## 5. 推理步骤失效（inference-step invalidity）

### 5.1 定义

作者明确尝试从 premises 推到某个 conclusion，但因为定理条件、逻辑关系、量词、概率对象、结构转移或适用域而无效。Finding 保存 `premises`、`claimed_inference` 和详细 `mathematical_reason`。

### 5.2 小类

#### `theorem_lemma_or_rule_misapplication`

调用 theorem、lemma、identity、inequality rule、optimization condition 或标准结论时缺少 side condition、对象不兼容，或使用了比原结论更强的接口。

#### `invalid_logical_geometric_or_structural_inference`

一般逻辑、几何、functional-analytic、convex、spectral、variational 或其他结构关系推断错误，且不更适合下列具体类别。

#### `invalid_generalization_or_quantifier_shift`

从特殊到一般、有限到无限、局部到整体、pointwise 到 uniform、existential 到 universal，或无依据交换 quantifier、limit、extremum、expectation 和 probability。

#### `probability_conditioning_coupling_or_object_transfer`

在 data-dependent choice、conditioning、dependence、filtration、coupling、distribution、sample 或 random object 之间转移事件/界时，没有 simultaneous 或 conditional argument。

例如 concentration lemma 只对每个固定 $\lambda$ 成立，却直接代入同一数据选出的 $\widehat\lambda$。

#### `intermediate_domain_boundary_or_regime_overreach`

某个已经写出的中间步骤只在更窄的内部、非退化、有限或渐近制度成立，却被用于 theorem 的完整范围。它与 obligation 的区别是：这里作者已经明确尝试了该范围，只是尝试无效。

## 6. 计算步骤失效（calculation-step invalidity）

### 6.1 定义

保持策略、对象和所用定理不变，通过正确重算同一 algebra、derivative、integral、normalization、inequality combination、scaling 或 asymptotic balance 即可确认错误。

Finding 保存原文 `displayed_expression` 和 `correct_recalculation`。

### 6.2 小类

#### `local_algebra_symbol_normalization_or_explicit_formula_omission`

局部代数、符号、正负号、归一化、代入、导数、积分、矩阵式或明确公式错误，包括一个声称完整的展开式漏项。

#### `inequality_constant_or_probability_budget_error`

不等式方向、常数、数值因子、probability allocation、union-bound budget 或 confidence parameter 计算/合并错误。

#### `scaling_dimension_or_sample_complexity_error`

维数因子、operator scale、norm conversion、iteration count、computational complexity 或 sample complexity 依赖算错。

#### `rate_exponent_remainder_or_asymptotic_balance_error`

Convergence exponent、truncation balance、remainder order、tail rate、little-o/big-O 或 asymptotic tradeoff 算错。

排除：局部正负号或代入错误不会因为出现在渐近证明中就变成速率错误；应按失效的局部运算分类，除非根错误本身就是速率或阶数的计算。

## 7. 同一证明内的顺序审计

按 proof DAG 或自然顺序：

1. 定位一条 atomic root error；
2. 只授予修复该错误所需的最小 oracle repair；
3. 在反事实修复后继续检查所有后续步骤；
4. 后一处缺陷只有在前一错误修复后仍然存在，才成为新 finding。

Finding 的 `assessed_after_repairing` 保存本节点中在审计它之前被反事实修复的 finding IDs。它记录审计顺序，不表示后一错误由前一错误引起。

若修改前一错误的 radius、parameter、assumption 或 interface 后才产生新的 proof work，这只是修复后果，不是原文中的第二条错误；目前写入 `open_questions`，以后由 impact/fix taxonomy 统一处理。

不再使用 `independence_status`：进入正式数组的 finding 按定义就是一条独立根错误；无法确认独立性时不强行建 finding。

## 8. Result 之间的依赖

若 $T_2$ 使用 $T_1$，审计 $T_2$ 时先把 $T_1$ 的原文精确合同视为接口：

$$
T_1:\quad \mathcal A_1\Longrightarrow\mathcal C_1.
$$

`dependencies[].use_status` 为：

- `valid_use`：$T_2$ 满足 $\mathcal A_1$，且没有强化 $\mathcal C_1$；
- `invalid_use`：$T_2$ 误用接口，并由本节点 finding 拥有该根错误；
- `inherited_blocker`：本地使用正确，但已确认的上游 finding 阻断该接口；
- `mixed`：既有上游 blocker，又有独立本地误用；
- `indeterminate`：现有 ledger 或 source 不能判断。

只允许已审定上游 finding ID 进入 `upstream_finding_ids`；当前节点自己拥有的根错误进入 `local_finding_ids`。如果上游结果有错误而下游准确使用原文合同，则下游只记 `inherited_blocker`，`local_finding_ids=[]`，不复制 finding；审计下游其余 proof 时仍把上游精确合同作为 oracle。

这里还要区分“接口误用”和“正确引用后另作错误推理”。只有遗漏上游 side condition、强化上游结论等以接口适配本身为根错误的 finding，才进入 `local_finding_ids` 并使依赖成为 `invalid_use` 或 `mixed`。若上游接口被准确引用，错误发生在之后的独立推理中，则该 finding 只存在于本节点的机制数组，dependency 仍是 `valid_use` 且两个 finding-ID 数组均为空。

自动选择审计节点时，流程只取具有明确 source-issue 记录的 `theory_candidate` 或 `internal_support`，包括 Thread-A Turn-3 的 statement/proof issue 和 later-chain 明确定位到该节点的 issue lead。未被明确标记的下游节点不会仅因依赖一个错误上游而自动加入 target queue；否则会把“现有 issue 数据的分类审计”悄悄扩展成“整条下游证明链的再次发现式审计”，改变样本入选口径。

依赖传播仍然保留在 paper-level 分析中。若一个被审节点使用了已审上游，按上述 `dependencies[].use_status` 记录。对于未标记下游，可选的 paper-level propagation turn 只把已确认 finding 的 honest repair 代入依赖路径，恢复该下游仍受支持的合同并评级 result impact；它不会把下游加入 finding target queue，也不创建 `inherited_blocker` result audit。

传播 turn 不寻找反例、不判断下游 theorem 真假、不发现或记录新的独立错误。路径外 proof branches 一律视为 oracle-correct。它只回答 repaired upstream interface 是否未被使用、仍足够、导致假设范围收窄、导致结论削弱、使原文支持丧失，或现有材料不足。最终 paper impact 综合正式 result audits 和这份可选传播 assessment。显式 `--result-id` 仍只用于精确调试或人工追加的完整复核。

## 9. Issue leads 与独立审计

Paper 顶层的 `issue_leads` 保存 Turn 3 statement/proof leads 与 later-chain leads。每条 lead 有稳定 `lead_id`、所属 `result_id`、来源和原始 claim。

每个 result node 的 `lead_adjudications` 必须逐条裁决当前节点的全部 leads：

- `confirmed`；
- `partially_confirmed`；
- `rejected_by_controlling_context`；
- `rejected_as_artifact`；
- `rejected_other`；
- `indeterminate`。

不再复制整份输入 leads，也不保存可机械推出的 overall verdict。Finding 的 `related_lead_ids` 指向与它对应的原线索；空数组表示完整审计中新发现。

## 10. Source registry 与位置

Paper 顶层 `paper_context.sources` 给每个输入文件一个稳定 `source_id`，保存真实私有路径、来源种类及原文表示 fidelity。Result node 不再重复文件路径。

所有 statement、proof、lead、finding、counterexample 和 dependency 位置统一为：

```json
{
  "source_id": "paper_source",
  "locator": "Theorem 4, L117-L120"
}
```

对于 extracted text、OCR 或 unknown representation，单个畸形符号不能独立支撑 source finding。上下文明确消解时记为 artifact；否则保留未判定。若数学语义在相关段落稳定，且由精确重算、全合同反例或重复原文用法独立确认，仍可审定数学错误。

### 10.1 完全缺失证明资源的节点：单独 reject

Result 顶层增加一个资源准入标签 `audit_status`，取值为 `assessed` 或 `rejected_missing_proof_source`。它不属于错误分类或严重程度。只有核查全文、附录与证明指向后，确认因资源缺失而完全没有本节点的 proof 或可识别论证，才使用 reject。例如本版本明确把全部证明放在未提供的 full version，或抽取材料完全缺失指定的证明章节。

简短但可识别的引用／直接推论论证仍是证明材料；已有 proof 内的一处 gap、无效步骤或模型补不出证明，不按资源缺失 reject。部分材料歧义仍用原有 `open_questions`，不扩大此标签范围。

Reject 节点保留可读到的 `contract`、每条原始 lead 的裁决以及 `open_questions` 中的缺失资源名称／位置说明；不继续做实质分类或评级。四类 findings、其他反例与 dependencies 都为空，`theorem_failure.status=undetermined`，`result_impact_assessment=null`。这里的 null 不是 unaffected；统计先看资源标签。保留原记录以便过滤，不物理删除数据。

同篇其他材料齐全节点继续审计。Reject 不进入上游错误 ledger，也不能成为 inherited blocker 或主要影响原因。Paper-summary 在 `paper_open_questions` 写出覆盖限制，只讨论其余节点已确认的影响。统计上，reject 节点排除出 result/finding/反例分布；其余节点仍可计数。含 reject 的 paper 不进入完整 paper-impact 分布，避免把不完整审计当成全文结论。历史实验不自动回填新标签或重算。

### 10.2 Typo / minor 约定的具体允许清单

以下三类先于错误分类排除；每项都有自己的边界，不用“容易修复”统包：

1. **原文已确定修正读法的转录或记号疏漏。** 缺失／错写的正负号、符号、哑指标、关系号、公式漏项等，必须由原文定义、已经正确的推导或一致的后续使用明确确定修正版本。修正是在恢复原文已有的式子；后面反复声称希望得到的结论，本身不足以支持修正读法。
2. **上下文明确的自然记号约定。** 例如非负 pairwise incoherence 指标中没有元素对时取零，用于表达“没有两两相关性”。须由该量的定义和用途支持；不是把所有空集最大值都设成零。
3. **不影响后续使用的常规平凡边界限定。** 例如 Bessel 修正样本方差的重复次数 $K\ge2$ 未重申，或只在高维坐标公式中使用时未重申维数不是一。须检查后续定理／算法：例外情形本就不在该常规用途内，或者有立即明确的平凡处理且后续用途完全不变。若算法可能到达零分母并实际需要此量，或排除边界改变算法行为／承诺的保证，就不落入这一允许项。写出一个比值本身不能证明分母非零。

属于允许项的错误不建 finding、反例、open question 或等级；若它本来就是输入 lead，只保留简短裁决。这不是删除全部 repair Level 1：仍有实质数学内容的局部易修错误继续统计。

## 11. 当前 result-node 结构

```text
result audit
├── result_id
├── audit_status: assessed | rejected_missing_proof_source
├── contract
│   ├── quantified_domain
│   ├── assumptions
│   ├── conclusion
│   └── statement_objects
├── lead_adjudications
├── theorem_failure
│   ├── status
│   ├── statement_object_findings
│   └── other_global_counterexamples
├── findings
│   ├── proof_obligation
│   ├── inference
│   └── calculation
├── dependencies
├── result_impact_assessment
└── open_questions
```

四类 finding 中的每一条都包含：

```text
repair_assessment
├── repair_difficulty_level: 1 | 2 | 3 | 4 | null
├── selected_honest_repair
└── level_rationale
```

同一 result turn 在完成全部 finding 与依赖审计后，还输出：

```text
result_impact_assessment
├── result_impact_level: 1 | 2 | 3 | 4 | null
├── revised_result_summary
├── impact_explanation
└── primary_driver_finding_id
```

当前体系分为 finding 修复难度、result 影响和 paper 影响三种序数量，不相加、不求平均，也不互相替代。没有重复的 root-cause 字段、次级多标签或 confidence。完整规则见 [修复与影响评级](repair_and_impact.md)。

## 12. 修复难度与两级影响

新增等级不改变 finding 的机制分类，也不构成单独的模型审计阶段：

$$
\text{同一 result turn}
=
\text{findings}
+
\text{finding repair difficulty}
+
\text{result impact}.
$$

所有 result 完成后的额外 paper-summary turn 只判断论文贡献影响，不得创建或改写 findings。

三个评价对象分别回答：

1. `repair_difficulty_level`：修正单条根错误需要多大数学改动；
2. `result_impact_level`：综合本节点本地错误和 inherited blockers 后，原合同损失多大；
3. `paper_impact_level`：综合修订后，论文现有主要理论贡献损失多大。

`confidence` 不进入任何层级。模型自报置信度不能可靠校准证据质量；不确定性通过 `null` 等级和说明所缺证据来表达。

## 13. 统计口径

最终报告至少区分：

1. paper 数；
2. 受影响 result-node 数；
3. finding/root-error 数；
4. 四类 mechanism 与 subtype 分布；
5. `proven_erroneous` 节点数及两类见证数；
6. 输入 leads 的确认、重分类、驳回与未判定数；
7. inherited blockers 和本地 invalid uses；
8. finding 修复难度、result 影响和 paper 影响的各自分布及交叉表。

同一上游错误在多个下游节点造成影响，不重复计作新的 root error。修复难度和两层影响与错误 mechanism 分开统计。

## 14. 配套文件

可运行入口、输入契约与输出清单见 [README](../README.md)。Reviewer 只复用本规则审定 A/B 候选并集，不另设分类或评级标准。文献借鉴与本项目设计的区别见 [引用清单](references.md)。
