# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1–2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3–7:** Some correct core steps or conclusions, but important steps are missing.
- **8–9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points — Output law and clipping:** Derives the Poisson acceptance/output-law identity for the specified sampler, establishes termination, and gives a valid clipping comparison strong enough for the later change of measure. A symmetric chi-squared estimate is one suitable route. Merely naming a rejection sampler is insufficient.
- **4 points — Characteristic one-step estimate:** Proves the intrinsic-dimension posterior/increment moment bound or an equally strong substitute; analyzes the actual path and proposal; controls exact-score clipping error at the stated step-size scale; and proves robustness using the two score MSEs. The correct non-unit-alpha next-score coefficient is of order alpha_k² eta_k(1+eta_k/sigma_k²). The score error must ultimately be integrated under the true marginals, not an uncontrolled proposal law. Naming the source's specialized propositions without establishing their relevant content does not close this step.
- **2 points — Accumulation:** Applies reverse-chain KL factorization and data processing with expectations under p_{k+1}; uses adjacent-weight domination correctly; retains the terminal s_K error and the initialization term. There are K-1 transitions but K score-error weights.
- **2 points — Schedule and consequences:** Constructs a variance-preserving schedule with the stated explicit logarithmic bound; allocates per-step error so its total is O(delta²); proves the Gaussian initialization estimate; counts all score evaluations with the stated high probability; and proves the early-stopping and bounded-Lipschitz consequences. Handle M_2=0 and the admissible early-noise domain without undefined logarithms.

# Evaluator Notes

Accept any complete valid alternative proof under the public assumptions. The reference proof supplies one fully reconstructed route, not additional public assumptions.

Do not require Hölder regularity, bounded support, score smoothness, a proximal oracle, or non-uniform Lipschitz hypotheses: none belong to this theorem. The covering-number definition permits infinite covering numbers and then uses its ambient-dimension cap.

Do not accept the former proposal N(alpha_k^{-1}x'+eta_k s_k(D_k(x')),eta_k I); it is not the specified algorithm. The actual proposal uses s_{k+1} at the reverse input and variance v_k. Auxiliary Gaussian variances are v_k/2.

A proof that drops s_K's error, silently assumes sigma_{k+1}²/sigma_k² is universally bounded for arbitrary alpha_k, or turns Kdelta into delta² without retuning the per-step tolerance has a substantive gap.

O and the displayed comparison constants hide universal constants only, not additional logarithmic factors. Do not impose the source's erroneous numerical one-call query constant; the target is the fixed-clipping-level O(K) total bound.

All theorem-critical reference obligations are closed; there is no GT completeness exception.
