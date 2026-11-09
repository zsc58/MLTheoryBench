# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs the graph couplings induced by the quantization maps, verifies their marginals, and correctly derives `W_p(mu_i,nu_i)<=e_i` for both endpoints, including `p=infinity`, hence `delta_p<=E_p` or an equivalent direct reduction.
- **3 points:** Establishes the entropic-value bound from the stated assumptions. A complete route observes that admissibility makes the cost integral identical for all couplings of fixed marginals, uses nonnegative relative entropy and the product coupling to identify the finite optimal value, and compares the two product couplings by admissibility. If normalization is used, correctly tracks `g=h/tau`, `A=lambda/tau`, and multiplication of the optimal value by `tau`. A direct proof in the original normalization receives equal credit.
- **4 points:** Establishes the exact final bound with the definition of `W'_r` in the task. A complete route identifies it with the aggregate of endpoint `W_r` distances, proves or correctly justifies `W_r<=W_p`, obtains `2^(1/r-1/p)` from the two-coordinate norm inequality, handles `p=infinity`, and substitutes the quantization bounds. The stronger first-term-only bound suffices because the second term in the required conclusion is nonnegative for every permitted `tau`, `lambda`, and `kappa`.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, normalization, identification of unique optimizers when unnecessary for a chosen argument, or a nontrivial use of a redundant assumption.

The public `W'_s` is the aggregate of the two marginal Wasserstein distances. It is not Wasserstein distance on the space of joint laws equipped with a product metric. In particular, it vanishes for couplings of the same endpoint pair. The transport inequality is consequently automatic under the task's entropy convention; recognizing this is correct and must not be penalized.

A proof that replaces `W'_s` with a different quantity must still justify the stated claim under the actual public hypotheses. A stronger conclusion is acceptable only when proved from those hypotheses.

Merely asserting a specialized value-stability or optimizer-stability theorem does not close the corresponding proof obligation. The two specialized source citations are not additional public assumptions or independently audited black boxes. Their relevant consequences can be derived directly as in the reference proof. Standard elementary facts about relative entropy, pushforwards, moments, and power means may be used with their hypotheses respected.

Check that all cost integrals and optimal values used in differences are finite, that the named optimizers are well-defined, and that zero constants and `E_p=0` introduce no undefined operations. Finiteness and optimizer existence follow from the existing assumptions; do not demand additional moment, continuity, compact-support, or transport assumptions. The source's bounded-support convention is required only when `p=infinity`.
