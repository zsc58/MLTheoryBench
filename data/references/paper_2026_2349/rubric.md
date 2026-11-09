# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Establishes the main identities needed for the representation. In the reference route, this means constructing the harmonic lift, proving harmonicity of its homogeneous components, deriving the Gaussian harmonic eigenvalue, and applying the Taylor/symmetry ReLU argument. A valid direct Gaussian/Hermite or other alternative derivation receives equivalent credit; harmonic lifting is not mandatory.
- **2 points:** Obtains exactly the stated sharpened coefficients and the complete pointwise representation, including its constant and linear terms. In the reference route, this is restriction to the original variables and averaging the extra Gaussian coordinate. An alternative route deriving the same formula receives equivalent credit.
- **3 points:** Establishes the sub-Gaussian neuron-norm estimates and the polynomial Gaussian norm and moment calculations needed to obtain every stated K_{d,k}. The reference route uses the Hermite/Fischer identity, Gaussian radial moments, and Cauchy--Schwarz. Equivalent valid estimates proving the same constants are acceptable.
- **1 point:** Proves finite-width existence with the stated negative norm-squared term by a valid sampling/variance or equivalent argument, and handles a zero integrated neuron norm. Zero output weights may pad a network to n neurons.

# Evaluator Notes

Accept any complete valid alternative proof. The point allocations concern mathematical obligations, not a required sequence of named methods. Merely restating the representation earns no derivation credit, but a proof must not lose credit for avoiding harmonic lifting or projection.

A generic n^{-1/2} assertion does not establish the precise error bound. The proof must justify the displayed constants and the subtraction of ||p-p_0||_2^2. It should also make clear why the square-root argument is nonnegative.

Check the positive scale convention, constant and zero polynomials, d=1, and the zero-neuron case. An exponential bound involving division by ||v|| must either be restricted to v!=0 or accompanied by the separate zero-vector case. Routine omitted boundary justifications may warrant the 8-9 range, rather than invalidating an otherwise correct argument.

The source's unrestricted claim of invertibility for every spherical probability is false at the point mass at zero. The task uses a nondegenerate Gaussian, and a proof needs only the valid Gaussian identity. Do not require or accept unsupported general invertibility as a substitute for this identity.

Norm-biased sampling can discard parameters whose neurons vanish in L2(D). It need not dominate the original measure on those parameters, and its mean need only equal p-p_0 in L2(D) for the existence argument. Do not penalize a correct effective-support construction for lacking pointwise unbiasedness outside a D-full set. Conversely, do not accept a claim that this optimizer necessarily dominates the entire original measure.

The reference proof explicitly closes the Gaussian eigenvalue, projection, Hermite/Fischer identity, neuron estimates, and variance calculation. There is no unresolved private proof obligation.
