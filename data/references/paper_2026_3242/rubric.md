# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Hamiltonian dynamics and KL control (2 points).** Establish global well-posedness from smoothness, conservation of the Hamiltonian and phase volume, invariance of nu tensor gamma, and exact joint-KL conservation. Use the KL chain rule after Gaussian momentum initialization to show that every deterministic-time position marginal has KL at most the segment's initial KL. Establish the moment and density properties needed to restart the algorithm. In particular, exponential-time admissibility must not rely solely on an exponential-in-time Lipschitz bound that need not be integrable for arbitrary T; the energy-based quadratic position-moment bound or another valid argument suffices.

2. **Average-KL/Wasserstein estimate (4 points).** Derive, rather than merely cite, the weighted inequality for the deterministic-segment position marginals p_t:
\[
\frac12W_2^2(p_T,\nu)+3\int_0^T(T-t)\mathrm{KL}(p_t\|\nu)\,dt-\frac M2\int_0^T(T-t)W_2^2(p_t,\nu)\,dt
\le\frac12W_2^2(p_0,\nu)+T^2\mathrm{KL}(p_0\|\nu).
\]
The source-route obligations are: temporary regular initialization and its propagated regularity; continuity and momentum equations and the acceleration identity; the upper second-difference estimate using transport couplings; justified cutoff integration by parts with the favorable singular-Hessian sign; the conditional Gaussian entropy estimate, matrix trace/log-determinant estimate, Monge-Ampere identity, and semi-convexity; and the concavity/integration argument with zero initial right derivative. Finally remove temporary regularity by constructing approximations converging in both W_2 and KL, proving finite-time flow stability, and passing to the limit. The negative integrated Wasserstein term requires actual convergence, not an unsupported application of lower semicontinuity. Standard independent Brenier/Monge-Ampere facts and Gaussian maximum entropy may be used with their hypotheses verified. The paper-specific average-KL or differential inequality cannot be assumed as an axiom.

3. **Randomized-time contraction (2 points).** Apply the alpha-Talagrand inequality with the correct sign to the average estimate, and use convexity of KL for the triangular mixture to obtain
\[
C_T=\frac{2}{3-M/\alpha}\left(1+\frac1{\alpha T^2}\right).
\]
Prove the exponential-time case, for example by deriving the Gamma(3, rate 1/T) mixture of triangular laws and computing E[S^{-2}]=1/(2T^2). This gives a slightly stronger exponential coefficient, which may then be weakened to C_T. Do not confuse KL of a mixture with the average KL; only the appropriate inequality is needed.

4. **Iteration and complexity (2 points).** Show admissibility and finite KL persist, iterate to the K-step bound for every T>0 and K>=0, and compute the contraction at T=2/sqrt(alpha-M). Verify the displayed ceiling in the nontrivial error regime, and take zero iterations when the initialization already meets the tolerance, including zero initial KL. Derive the almost-sure triangular bound and the exponential expectation for the sum of integration times. Interpret the asymptotic in the task with r=M/alpha fixed; the exact ceiling gives an additive one and the coefficient 1/log(1+(1-r)/(5-r)), which is not uniformly bounded as r approaches 1.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, an interior first-derivative formula when only the initial derivative is needed, or its particular approximation sequence. The public theorem concerns the unconditional output position law. Independent integration times are not adaptive stopping times. Marginal KL domination by its initial value does not assert monotonicity along a deterministic Hamiltonian trajectory. For small T the displayed C_T can exceed one, which does not invalidate the stated inequality.

A theorem-critical omission in Step 2 is major even if the final contraction formula is guessed correctly. The replacement reference derives that step and has no unresolved private proof obligation. Routine endpoint omissions or readily repairable notation errors should be distinguished from missing core arguments.
