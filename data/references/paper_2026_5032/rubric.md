# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Confidence control and certification validity (2 points).** Establish simultaneous confidence control with failure probability at most \(2KdT^{-3}\), justifying concentration at adaptive pull counts through latent prefixes or another valid argument. Derive that strict separation implies \(\mu_{a,j}\le U_{a,j}\le U_{c,j}<L_{b,j}\le\mu_{b,j}\) for every \(a\ne b\), or give an equivalent valid derivation. Conclude that the certified arm is Pareto-optimal and that regret is zero from the certification round onward on the confidence event.

2. **Uncertainty-scale charging (3 points).** Derive \(\Delta_a^P\le m_j-\mu_{a,j}\) from the gap definition and prove \(\Delta_{A_t}^P\le4\beta_{A_t}(t)\) for every non-certifying pull. Cover both possible sampled endpoints. For the runner-up, accept either the source's split according to whether the UCB leader is a true maximizer or the direct argument using \(m_j\le U_b=L_b+2\beta_b\le U_c+2\beta_b\). No particular case presentation is required.

3. **Width floor and finite-time upper bound (3 points).** Prove that the positive-gap objective has pair width at least \(g^\dagger/2\), both when its UCB leader is its true winner and when it is not. Transfer this floor through widest-pair scheduling to obtain sampled radius at least \(g^\dagger/4\). Infer the post-warm-start count bound \(m_a\le32\log T/(g^\dagger)^2\), with correct pre-pull indexing, and sum radius charges to obtain \(64K\log T/g^\dagger\). Add the warm-start and confidence-failure terms to establish the exact displayed expectation bound. The argument must accommodate zero exploration counts and no certification before the horizon. Interpret the stated asymptotic consequence for a fixed instance.

4. **Matching lower bound (2 points).** Verify the duplicated-coordinate geometry, including \(g^\dagger=\Delta_{\rm sc}\), each inferior arm's gap \(\Delta_{\rm sc}\), and \(R_T^P=\Delta_{\rm sc}\sum_{a=2}^K N_a(T)\). Explain why a duplicated vector provides exactly one scalar Bernoulli observation. Verify that full-model uniform goodness implies the induced scalar policy's subpolynomial expected regret for every Bernoulli mean vector, so that a correctly stated standard sampling lower bound applies. Evaluate the alternative-mean KL infimum, combine the per-arm liminf bounds, and derive the explicit \(3(K-1)/(8\Delta_{\rm sc})\) constant and its full-model order interpretation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The two standard-independent results used by the reference proof are Hoeffding concentration and the Bernoulli Lai–Robbins sampling lower bound; a correct statement or specialization and a justified application suffice without reproving those results.

Treat omission of the width-floor argument, certification implication, or information-preserving scalar reduction as theorem-critical gaps. A lower-bound invocation must have the required goodness across alternative mean vectors; goodness merely on the fixed instance with arm 1 best is insufficient. Do not interpret the d identical coordinates as d independent observations.

Do not require proof that the first certifying objective actually maximizes the true marginal gap. The width floor uses a maximizing objective, but the policy may commit to any certifying objective. Do not require a characterization of all Pareto geometries, a positive gap for every objective, or uniform goodness of the upper-bound policy outside its stated regime.

Do not substitute zero Pareto gap for Pareto optimality: the source definitions allow dominated arms with zero Pareto gap. The public full-model goodness condition refers explicitly to arms outside the Pareto set. On every duplicated-coordinate scalar instance, these are exactly the arms with strictly suboptimal scalar means.

There are no unresolved GT obligations and no additional hidden assumptions or scoring requirements.
