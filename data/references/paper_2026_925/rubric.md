# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the path-space likelihood ratio from the specified dynamics, predictable integrand, true exponential martingale, and common initial law. Identifies the changed law with the learned law and derives the terminal conditional-expectation representation, hence the terminal chi-square expression.
- **3 points:** Establishes the required quadratic, fourth-order, and exponential-Taylor-remainder controls from the stated moment assumptions. In particular, derives rather than asserts the quartic remainder. Checks that gamma>2 permits the fourth bracket moment and that 2(1+delta)/(delta-1)<2+gamma permits the higher BDG moment. Keeps finite BDG factors in admissible constants.
- **3 points:** Uses the mean-zero martingale and the definition of rho_i to identify the conditional signal, controls the conditional bracket term, and derives (1/4)rho_i a_i^2-Ca_i^4, including the clean (1/8)rho_i a_i^2 consequence at the stated threshold.
- **2 points:** Derives the upper bound 4a_i^2+ca_i^4 and concludes uniform small-error equivalence when rho_i is bounded below, with the correct constant dependencies.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, exact auxiliary constants, or particular route through fourth moments if another valid argument proves the required remainder estimate.

The stochastic integrals are indexed by increasing sampling time; the physical coordinate Y_{t0} is the terminal coordinate X_L, not the initial sigma-field. Brownian sign conventions are interchangeable only when the SDE and stochastic exponential signs are changed consistently.

A proof invoking Girsanov must use the shared initialization and verify the drift change. A terminal exponential random variable is not by itself a martingale-process hypothesis. The density projection and quartic remainder remain proof obligations and may not simply be assumed.

The case a_i=0 is included: A_i=N_i=W_i=0 almost surely, the two path laws and their terminal marginals agree, and the asserted divergence is zero. A proof may cover this directly or through a valid division-free argument. Do not demand division by a_i in that case. If rho_i=0, the public perturbative threshold permits only a_i=0.

The constants c,C must depend only on delta,C_delta,gamma,K_gamma and be uniform in i. The final equivalence constants and its uniform smallness threshold may additionally depend on the positive lower bound underline rho. There is no obligation to establish a finite-sample score-estimation rate, a KL/chi-square equivalence, a learned/ideal energy equivalence, or a cross-generation recursion.

All core steps have complete derivations in the reference proof; there is no unresolved ground-truth obligation.
