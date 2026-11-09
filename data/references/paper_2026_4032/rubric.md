# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Neural-law recovery (2 points).** Establishes the existence of centered potentials in the specified class whose embedded Gibbs laws converge in total variation to the entropic optimizer. The reference route obtains a continuous optimal potential on the compact target support, approximates it using the injective feature map and density of the function class, and controls the resulting Gibbs densities. A complete equivalent argument is accepted. Recovery is a conclusion, not an available assumption.
2. **Heat smoothing and joint limit (3 points).** Establishes that smoothing preserves the needed approximation control and tends to the identity as heat time vanishes, yielding a valid choice of indices tending to infinity and positive heat times decreasing to zero. The reference uses total-variation contraction and the Euclidean/torus heat-kernel approximate-identity property. Taking the indices to be successive integers and heat times to be their reciprocals is sufficient; a nontrivial diagonal argument is not required.
3. **Projection-pullback convergence (3 points).** Justifies passage through the measurable recovery map. The reference proves continuity at points of the embedded graph using nearest-point optimality and the triangle inequality, then applies the almost-sure continuous mapping theorem. An equivalent direct convergence or coupling argument is accepted; the literal factor-two estimate is not mandatory.
4. **Coupling identification (2 points).** Shows that the limiting law is the specified inverse-embedding pullback and has both marginals \(P_\Gamma\) and \(Q_\Gamma\), hence is a valid coupling on \(\Gamma\times\Gamma\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular construction of a continuous optimal potential. Standard results may be used when their relevant statements and hypotheses justify the application. Merely naming the specialized neural recovery theorem, or treating total-variation recovery as a hypothesis, does not close the recovery obligation.

The reference proof's compact-support existence argument uses soft-transform coordinate maximization, Arzelà–Ascoli, and marginal identification by differentiation of the semidual. Its approximation argument uses continuous extension from the compact feature image and uniform approximation. These are private proof details, not additional public assumptions.

Treat failure to establish neural recovery, failure to justify convergence through projection by any valid method, or failure to identify both limiting marginals as theorem-critical gaps. Do not demand that intermediate Gibbs laws or positive-time graph laws have the exact target marginal. No finite-sample, training, or optimization rate is requested.
