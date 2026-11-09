# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the continuity inequality by differentiating the log-exponential loss along an interpolation, correctly identifies the induced softmax weights, and proves the tunable $\beta$-power-mean estimate, or supplies an equivalent valid argument. Merely naming differentiation or a softmax argument without deriving the averaged negative-sample term does not earn full credit. Intermediate interpolants may lie in the unit ball rather than the sphere; the finite loss formula remains well defined there.
- **2 points:** Chooses an appropriate $\beta$, applies the parameter Lipschitz condition, and uses Minkowski/Jensen or equivalent mixed-norm reasoning to establish $\rho_n(f_\theta,f_{\theta'})\le(4e/\gamma)B_\gamma L_0\|\theta-\theta'\|_2$. Covers both $\gamma<1$ and $\gamma\ge1$, including the boundary.
- **1 point:** Correctly bounds the loss oscillation by $4/\gamma$ and consequently controls the empirical metric diameter.
- **4 points:** Transfers Euclidean covers to the loss class, applies a valid Dudley entropy bound with the correct parameter-ball diameter, evaluates both entropy-integral regimes, and obtains the stated minimum with constant $96/\gamma$. Accounts for the case $B_\gamma L_0=0$, when the empirical loss class is a singleton and its expected Rademacher supremum is zero. In the positive case, justifies applicability of the entropy bound to the compact empirical loss-vector class and uses an endpoint and constant consistent with the stated entropy inequality.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central obligation is to retain enough control of the averaged negative-sample power mean to establish the stated conclusions. A generic Lipschitz bound using only the largest negative norm does not establish the stated theorem. If the continuity proof is flawed but the required empirical metric estimate is independently proved, award the later steps according to what is actually established.

The radius-$r$ parameter ball has pairwise diameter $2r$. A claim that its pairwise diameter is $r$ is incorrect. The endpoint $rL$ is nevertheless justified by a valid half-diameter entropy inequality; equivalently, a full-diameter inequality with coefficient $12$ can be converted to a half-diameter inequality with coefficient $24$ by monotonicity of covering numbers. Other valid entropy arguments yielding the requested constant are acceptable.

The Rademacher supremum in this task has no absolute value. Subtracting a fixed empirical loss vector does not change its expectation. Consequently a singleton class has complexity zero even if its loss values are nonzero. Do not require that the original loss class contain zero.

Failure to mention the zero case while dividing by $L$ is a readily repairable omitted case, not evidence that the theorem is false. A fully correct proof must cover it. No sampling model or population moment assumption should be demanded: both claims concern arbitrary realized tuples.
