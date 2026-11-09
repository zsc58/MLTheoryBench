# 实际采用的参考文献

本清单只保留对现行规则有具体作用的文献，不是领域综述。以下文献提供思想、边界或案例；本项目的四大类、17 小类、同根唯一归属和三级四档评级并非原样摘自其中任何一篇。链接与书目信息核查于 2026-09-15。

## 1. 可观察的数学错误，而非作者心理归因

Annie Selden and John Selden. *Errors and Misconceptions in College Level Theorem Proving*. 1987 年会议论文；ERIC 收录的技术报告版本为 2003 年，No. 2003-3。[ERIC 记录及全文入口](https://eric.ed.gov/?id=ED518588)

论文区分与特定 misconception 相关的错误和其他推理错误。对本项目的实际启发是：可以从对象良定义、证明另一条命题、误用定理和无效推广等可观察现象寻找分类角度。但不能从论文文字反推作者的认知缺陷。我们不保留其两大认知分组，也不照搬 M/E 编号；具体机制按理论 ML 数据重新组合。

对应规则：[错误分类](error_taxonomy.md)的四方面检查和义务／推理边界。迁移关系是方法与部分机制的适配，不是类别表的一一继承。

## 2. 证明没有展开，不自动等于实质错误

Line Edslev Andersen. *Acceptable gaps in mathematical proofs*. **Synthese**, 197, 233–247, 2020. DOI: 10.1007/s11229-018-1778-8。[大学正式记录](https://pure.au.dk/portal/en/publications/acceptable-gaps-in-mathematical-proofs/)，[期刊 DOI](https://doi.org/10.1007/s11229-018-1778-8)

该研究基于数学家审稿实践，讨论已发表证明中有意留下的 gap。我们据此保留“常规背景知识和适用引用可以承担证明内容”的边界，避免把省略展开直接记为错误；但是否已经提供具体义务的依据，仍须回到原文核验，不能凭“专家大概会补”放过关键缺口。

对应规则：短引用／直接推论核查、末尾空泛声称不自动完成义务、修复评级中的桥梁回查。具体准入清单是项目适配，不是作者提出的机器审计协议。

## 3. 修复需要的数学工作与当前损坏程度分开

William D'Alessandro. *Transferable and Fixable Proofs*. **Episteme**, 22(1), 271–282, 2025；2023-11-22 首次在线发表. DOI: 10.1017/epi.2023.54。[期刊全文](https://www.cambridge.org/core/journals/episteme/article/transferable-and-fixable-proofs/196B2A0EB367A15F85967DD5EB7528ED)

文中讨论 transferable、fixable 与 corrigible 的区别；特别说明有实质错误、使当前证明失效的论证仍可能可修复，使用已有技术修补也可能需要非平凡工作。我们借鉴“新增数学工作”作为修复轴，而不把“改动字数少”或“当前 proof 断了”直接当作修复难度。

对应规则：[repair 与 impact 分轴](repair_and_impact.md)、直接修订／局部补丁／核心修订的区别。四档阈值及 result/paper 的独立评级是项目自己的设计；没有采用“共同体可接受就不算错误”的判准。

## 4. 理论 ML 勘误中的定理失效与有限论文影响

Louis-Philippe Vignault, Audrey Durand, and Pascal Germain. *Erratum: Risk Bounds for the Majority Vote: From a PAC-Bayesian Analysis to a Learning Algorithm*. **Journal of Machine Learning Research**, 24(294), 1–13, 2023。[JMLR 正式页面及全文入口](https://jmlr.org/papers/v24/22-0747.html)

勘误定位多数投票风险分析中的错误证明，说明原命题在一般情形下为假，给出修订结论，同时指出原论文其余结果受到的影响有限。这直接示范了：proof 错误、命题的反例、修订后的适用范围与全文贡献影响，不能合成同一个标签。

对应规则：定理失效证据独立于 proof 机制；下游依赖须核查；paper impact 不等于最高 result impact。本例用于方法依据，不纳入本项目 2026 年待审论文数据，也不能用来估计错误发生频率。

## 5. 审计结论不是数学正确性证书

Christian Greiffenhagen. *Checking correctness in mathematical peer review*. **Social Studies of Science**, 2024. DOI: 10.1177/03063127231200274。[期刊全文](https://journals.sagepub.com/doi/10.1177/03063127231200274)

该研究讨论数学同行评审实际怎样检查正确性，提醒读者审稿实践与穷尽式形式验证并非同一回事。我们借鉴的是证据边界：模型两次一致、reviewer 保留一个指控、或者没有找到反例，均不能自行变成定理真假的证书。

对应规则：保留 `undetermined` 与开放问题；不输出模型自报 confidence；双评一致不能代替原文论证。这篇文献没有验证本项目 LLM reviewer 的准确率，也不直接提供我们的错误类别。

## 不再列入的内容

实证 ML 数据泄漏、一般实验复现清单、出版撤稿规范，以及仅与自然语言到 Lean 翻译有关的细分类别，不是现行 source-error 分类或三级评级的直接依据，因此不在本运行模块保留长篇 literature map。形式化忠实性作为来源排除原则仍保留，但不据此声称本项目在进行 Lean 验证。
