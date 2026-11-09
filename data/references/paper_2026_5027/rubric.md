# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the suffix-sum definitions to establish exact marginal factorization on positive prefixes and zero marginal weight on zero prefixes. Handles the empty-prefix and empty-suffix conventions, including `L_0=Z`. Does not assume that `L_t` is finite on every zero prefix. No quotient recursion is required.
- **3 points:** Under the proposal law, derives `E_R[W_T|F_t]=W_t^look` by cancellation on supported suffixes and uses the full-path support assumption to account for all positive target contributions. Establishes square-integrability of the conditional mean, the squared-error decomposition for square-integrable `F_t`-measurable approximations, and the minimum-MSE conclusion. Does not require normalization of `m_t`.
- **2 points:** Obtains the prefix-only identity and exact excess term `E_R[(W_t^prf)^2(L_t-1)^2]`, with the zero-prefix convention. Justifies the result even when `W_t^prf` is not square-integrable, for example by conditioning on individual prefixes, localization, or an equivalent valid argument with nonnegative extended expectations.
- **3 points:** Uses conditional independence of the auxiliary estimate and the evaluated future, not conditional unbiasedness alone, to justify the approximate-lookahead cross-term cancellation. Derives the exact approximate-weight MSE identity, including potentially infinite unconditional error, and applies the conditional `C_t/J` bound to obtain the stated inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central conditional-expectation projection and the quantified Monte Carlo inequality are theorem-critical; merely naming them earns no credit for the corresponding step.

The transition factors `m_t` are finite and nonnegative but need not be probability kernels. A proof that relies on their normalization does not establish the complete public claim.

Square-integrability of `W_T` guarantees square-integrability of `W_t^look`, but not of `W_t^prf` or `W_t^prf hat L_t`. Do not accept an unsupported assertion of those additional moments. A proof using finite conditional second moments and then integrating nonnegative conditional errors resolves this issue without strengthening the assumptions. Do not require an added prefix-moment assumption.

All conditional and random-variable identities are almost sure. Proposal-null prefixes need not carry uniquely specified conditional expectations. Prefixes with zero target weight and prefixes with zero future value must be compatible with the stated conventions.

The approximate estimate need not be `F_t`-measurable. A proof must correctly account for its auxiliary randomness. Conditional unbiasedness by itself does not imply that its error is orthogonal to the full-weight residual; the stated conditional independence supplies that justification.

The public target is the displayed inequality with coefficient `E_R[(W_t^prf)^2 C_t]`, which can be infinite. A finite O(1/J) or vanishing-error conclusion follows only when this coefficient is finite and fixed as `J` varies. Do not demand such an unconditional convergence claim, and do not credit it if asserted without justification.

Do not require the source's incremental-weight quotient recursion, a particular rollout construction, SMC resampling arguments, or MH arguments. These are not additional public targets.
