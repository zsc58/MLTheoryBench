# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly use the reward normalization and the common condition-independent forward kernel to transfer the target law to the source law. A direct marginal calculation using \(Q(z\mid c)=w(z,c)P(z\mid c)\), with \(w=\exp(R/\tau)/A(c)\), earns full credit. A valid denoising-objective argument is also acceptable when its hypotheses are justified; it is not required.
- **4 points:** Derive the posterior density-ratio decomposition and its score consequence. One complete route establishes \(Q_t(x\mid c)=P_t(x\mid c)\mathbb E_{P(z\mid x,c,t)}[w(z,c)]\) and differentiates its logarithm. Another valid route derives the weighted posterior kernel-score average and justifies the Bayes/posterior differentiation steps used to obtain the same decomposition. Merely naming importance weighting or a score identity is insufficient.
- **2 points:** Substitute \(w(z,c)=\exp(R(z,c)/\tau)/A(c)\) and correctly show that the condition-only normalizer disappears under \(\nabla_x\), yielding the exponentiated-reward posterior expectation.
- **2 points:** Identify the resulting target score with every optimizer of the original population score objective and state the conclusion \(\mu(dt)Q_t(dx,dc)\)-almost everywhere. A complete justification uses admissibility of the measurable target score, its zero loss, nonnegativity of the loss, and strict positivity of \(\lambda\). Arbitrary optimizer versions may differ on objective-null sets.

# Evaluator Notes

Accept a complete valid alternative proof and award points for the equivalent mathematical obligations it resolves. Do not require the reference proof's incidental ordering, the auxiliary denoising construction, a forward-kernel score, or differentiation under an integral. A direct proof using the noised marginal densities and the normalized posterior is fully sufficient.

The public regularity assumptions concern the specified marginal and posterior-expectation functions. They do not assume a differentiable kernel score, valid differentiation under its integral, a finite denoising second moment, or a finite global denoising residual. Do not accept an invocation of global denoising/score-matching argmin equivalence without justification when it is essential to the submitted proof. In particular, an infinite score-independent additive term does not justify equality of argmin sets. Conversely, do not penalize a proof for avoiding that equivalence.

Treat an unproved score decomposition or an incorrect reward-ratio substitution as a theorem-critical gap. Direct differentiation of an established marginal product identity satisfies the decomposition obligation; posterior differentiation under an integral is not separately required.

The optimization is over all jointly measurable fields depending on \((x,c,t)\), not over an unspecified restricted network class. No separate integrability of the score's squared norm is needed when the chosen field has zero error. No pointwise conclusion at null conditions, exceptional times, or off-support locations is required. The time law, positive finite weight, posterior time dependence, and fixed condition marginal must remain consistent with the public task.
