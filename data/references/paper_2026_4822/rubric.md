# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines a valid coupling/replay-to-shared-stack construction and proves equality of the replay and shared-stack joint trajectory laws and the ordinary marginal laws. In a conditional-law proof, this includes the prescribed action kernels, deterministic reuse of the appropriate recorded reward, and the conditional fresh-reward law after recorded rewards are exhausted. An explicit valid deferred-revelation argument is also acceptable.
- **3 points:** Establishes the arm-wise stopping-time and martingale identities, or equivalent moment arguments, including zero means, second moments, and the cross-policy covariance at the minimum pull count. A stopping-time proof must use genuine time-indexed martingales and verify the relevant measurability and integrability hypotheses. The minimum/maximum identity for the product of two stopped sums is one valid way to justify the cross moment.
- **3 points:** Decomposes cumulative rewards and rigorously bounds all count-count, mixed, and suboptimal-arm centered-sum covariances as $o(T)$; derives $\mathbb E N_{i,a^*}=T-o(T)$ and the corresponding expected-minimum estimate in the coupled model. In a full covariance expansion, the count-count coefficient is $\mu_a\mu_b$. The estimates must use count variances, rather than incorrectly assuming count second moments are $o(T)$.
- **2 points:** Computes the limiting covariance matrix, or an equivalent sufficient variance calculation, and correctly obtains $\operatorname{Var}(\widehat\theta_{\mathrm{ind}})/T\to2\sigma_{a^*}^2$ and $\operatorname{Var}(\widehat\theta_{\mathrm{cpl}})/T\to0$.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions, allocating credit to mathematically equivalent obligations rather than requiring the reference proof's notation or exact route. Do not award credit merely for naming coupling, optional sampling, or covariance cancellation without justifying the needed identities and bounds. In particular, independence of deterministic stack coordinates alone does not justify a conditional fresh-reward claim at an adaptive random index without a stopping-time or deferred-revelation argument.

A gap in the replay/shared-stack law or in the optimal-arm cross-covariance is theorem-critical. Minor algebraic or presentation errors are readily repairable when the limiting conclusions remain justified. Do not penalize a solver for using the correct count-count coefficient instead of the source's missing-factor expression. Do not require bounded or subgaussian rewards, positive optimal-arm variance, or a particular bandit algorithm. The proof must remain valid when $K=1$, when some arms are never pulled, and when $\sigma_{a^*}^2=0$; a uniform argument covering these cases needs no separate case discussion.
