# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the conditional posterior identity needed for the fantasy construction. Conditional on the causal available transcript, the pending locations are fixed; conditioning the current posterior draw on its noisy fantasy labels gives the GP posterior based on the completed-plus-fantasy dataset. Explains why the fixed-dataset base-rule assumption applies. Does not substitute an unsupported equality with the history distribution of a sequential run of the base algorithm.
- **3 points:** Derives the fantasy-path regret bound B_T. Uses the uniform fixed-dataset moment bounds, the equality of full-history and fantasy-history posterior variances at identical locations, and Cauchy-Schwarz. Justifies integration of signed auxiliary terms by using bounded fixed-dataset means, an equivalent normalization of the witnesses, or another valid argument. Establishes the pathwise variance-information inequality with C1=2/log(1+sigma_noise^{-2}), through the fixed-design Gaussian information/log-determinant identity and the elementary logarithmic inequality. A correctly stated standard Gaussian information identity may be invoked after checking its hypotheses.
- **3 points:** Proves the worker-partition bound sum_t sigma^2(x_t;D_{N_{t-1}})<=C1 Q gamma_bar(T/Q). Uses the available-worker rule to show that previous evaluations on a worker have completed before reassignment, applies posterior-variance monotonicity and the per-worker information bounds, then uses concavity on the worker counts. Covers empty worker subsequences and real arguments T/Q.
- **2 points:** Gives a valid expected-regret decomposition and controls its signed discrepancy by centering at the completed-data posterior mean. Proves or correctly applies the finite-set Gaussian maximum second-moment bound with C2=2+2 log(|X|/2), including the singleton case and zero-variance convention, and combines the bounds to obtain the exact target.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its explicit reconstruction of auxiliary results when an appropriate standard result is accurately stated and its hypotheses are checked.

The base-rule condition is uniform over all fixed datasets. A bound that holds only along the base algorithm's own sequential history does not justify applying its moment bounds to RKB fantasy histories. Auxiliary variables are not required to be nonnegative or dataset-measurable.

Integrability of V_t(D) separately for every fixed D does not imply integrability of a raw witness after substituting a random fantasy dataset. A uniform upper bound on its signed mean does not supply a uniform absolute-moment bound. A valid local argument sets vbar_t(D)=E_D[V_t(D)] and c_t(D)=E_D[U_t(D)sigma(A(D);D)]. Nonnegative regret and |c_t(D)|<=sqrt(zeta_t) imply -sqrt(zeta_t)<=vbar_t(D)<=xi_t, so the mean function is integrable under any dataset mixture. One may integrate these fixed-dataset functions directly or replace the witness by vbar_t(D). Do not require or silently add a stronger public moment assumption. An otherwise complete argument that omits only this readily repairable justification belongs in the 8-9 range rather than receiving full credit.

The posterior sample used by RKB is drawn conditional on completed observations. Standardizing it by the mean and variance based on unavailable full actual observations is incorrect. Likewise, the pathwise inequality `(g_t(x_t)-f(x_t))_+ <= W_t sigma(x_t;D_{N_{t-1}})`, with W_t formed from g_t alone, is false in general. The valid argument first takes conditional expectation of the signed discrepancy and replaces f(x_t) by its completed-data posterior mean.

For adaptive designs, the information argument is pathwise in the locations. Do not accept an unsupported identification of a random variance sum with unconditional mutual information of adaptively selected latent and response vectors.

For |X|=1 the relevant Gaussian positive-part second moment is at most 1/2, which is below C2. A tail integration that uses 2 log(|X|/2) as a nonnegative split point without treating this case is incomplete. Zero posterior variances do not require a strictly positive kernel; their residuals vanish.

The selected source upper-tail lemma has a locally repaired threshold max(0,2 log(|X'|/(2 delta))) for nonempty X'. Its empty-set event is vacuous. The solver need not discuss this source repair or prove the auxiliary confidence statement separately: a direct valid Gaussian-maximum argument is sufficient.

A named method without the conditional-law argument, quantitative bounds, and valid worker partition receives credit only for portions actually established. The final constants, parameter ranges, expectation mode, and target must be matched. There are no unresolved reference-proof obligations.
