# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the simultaneous tabular confidence and count event under the stated conditional subgaussian observation model, including both tails and a valid total failure-probability budget. Obtains pessimism \(\widehat r\leq r\) and correctly bounds \(\mathbb E_{\rho\times\pi_0}b^2\) by logarithmic factors times \(SA/n\). Handles zero-mass cells by restriction to the support of \(\rho\) or an equivalent division-free argument.
- **3 points:** Derives the central forward-KL performance inequality from the objective: identifies and justifies the Bregman/divergence representation, uses optimality for the pessimistic reward, and applies Fenchel-Young to obtain the \(\pi^{*2}/\pi_0\)-weighted squared-error bound. The derivation must apply to finite real-valued pessimistic estimates, which need not lie in \([0,1]\). Merely naming convex duality, a paper-specific lemma, or a divergence is insufficient.
- **2 points:** Combines pessimism, the coverage factor, and the count bound to prove the stated high-probability \(\varepsilon^{-1}\) upper rate with the required \(\eta C_*^2SA\) dependence. Uses \(r-\widehat r\leq2b\), or another valid bound on the pessimistic estimation error, rather than incorrectly replacing it by the empirical-mean error. Correctly identifies arbitrary global maximizers with local optimizers only where \(\rho(s)>0\).
- **3 points:** Proves the minimax lower rate in the task's observation experiment by constructing a valid paired-arm hypercube, deriving its optimal policies and additive loss decomposition, showing both a per-coordinate forward-KL loss separation of order \(\eta/n\) and bounded neighboring full-data-law KL, and correctly aggregating with Assouad's lemma to \(\Omega(\eta SA/n)\). A precise standard Assouad inequality may be invoked without proof once its hypotheses are verified. The KL calculation must include the sampled context and action and the \(n\)-sample product law.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A lower-bound proof may use different universal constants or an equivalent hard family. A solution that establishes only one direction cannot receive full credit.

Do not require full support of the context distribution, independence of a residual from its sampled cell, bounded observed rewards in the upper-bound model, or clipping of the reward estimator. None is an assumption of the task. Conditional Bernoulli rewards are admissible for the lower construction. Merely citing a bounded-increment concentration theorem does not justify the upper confidence event for general subgaussian observations; a valid subgaussian concentration statement or moment-generating-function calculation does.

The lower bound is a supremum over admissible instances, including context distributions and full-support logging policies. It is not asserted separately for every fixed logging policy or fixed context distribution. An estimator may use the known logging policy and independent randomization, but not the unknown reward or an instance-dependent oracle. A constant bound such as 32 on neighboring KL is sufficient when using the exponential-KL form of Assouad; Pinsker's inequality alone would not yield a useful testing bound at that constant.

An omitted elementary boundary qualification may be readily repairable, but an argument that substantively adds a full-support assumption on \(\rho\), changes the observation experiment, or changes the estimator does not establish the full stated task.
