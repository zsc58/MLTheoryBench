# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Regret transport.** Establishes
  \[
  \operatorname{Reg}_T(\pi)-\operatorname{Reg}_T(\pi_0)
  \le L\sqrt{T\,\mathrm{KL}(\mathbb P\|\mathbb Q)/2}.
  \]
  A complete argument must address the fact that \(r_t\) depends on hidden \(P\) and need not be adapted to the observed-history filtration. One valid route proves policy-independence of the latent posterior at a fixed history, replaces instantaneous regret by its posterior expectation given history and action, verifies preservation of expected regret under both policies, and iterates conditional Hoeffding for this adapted replacement. Then apply change of measure and optimize. Direct iteration on the unobserved \(r_t\), or enlargement of the filtration without verifying the drift condition for that filtration, does not establish this step.

- **2 points: Interaction-to-completion comparison.** Justifies absolute continuity and factors interaction KL into deployed-history conditional action-kernel KL. Applies data processing through the common oracle and the bounded-likelihood-ratio divergence comparison in the correct direction to obtain the factor \(2+\log V\) multiplying forward completion KL. Hellinger-based proofs must use a normalization consistent with the stated constant.

- **3 points: Observable mismatch bridge.** Uses the current-first conditional KL chain rule and harmonic self-contraction to obtain the factor \(1+a\log T\). Proves that censoring at action \(B\) preserves current-demand KL and uses conditional coverage \(\rho\) to obtain the factor \(1/\rho\). Justifies any absolute-continuity hypotheses used for the chain rule, for example by first treating infinite observed mismatch as trivial and then using finite first-coordinate and conditional KL terms. Naming these mechanisms without establishing their inequalities is insufficient.

- **2 points: Final synthesis and predictive-loss identity.** Combines the bounds with the correct constants and square-root scaling. Proves the observed KL equals the difference of the defined population log-losses. The identity must not subtract two infinite quantities: with the specified common dominating kernel the true population log-loss is finite. Handles zero divergence and the empty sum at \(T=1\); the \(a=0\) endpoint requires no later-coordinate contribution.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular posterior notation. Treat an incorrect KL direction, unjustified interaction factorization, failure to recover latent KL from coverage, or concentration applied to nonadapted hidden-task regret as a theorem-critical gap. Do not infer that the drift condition survives conditioning on the latent task. If an intermediate conclusion is independently proved by another valid argument, award downstream credit according to what is actually established. The task does not ask for a separate rate bound on the ideal policy and does not identify the empirical-completion policy with population-risk Thompson sampling.
