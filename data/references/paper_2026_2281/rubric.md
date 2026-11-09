# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly sets up the exact heat-kernel mechanism with generator \(\Delta_g\), uses stochastic completeness and the Ricci and sensitivity bounds, and applies the Renyi-divergence definition to every ordered adjacent pair.
- **4 points:** Derives the explicit Renyi bound using a valid argument. For the Harnack route, states the applicable inequality, verifies its hypotheses with \(V=0\), and performs the density conversion with the conjugate exponent \(q=\alpha/(\alpha-1)\). Justifies absolute continuity and the use of density-ratio test functions, for example by bounded truncation and monotone convergence. The integral estimate must have exponent \(K\alpha(\alpha-1)d(x,y)^2/[2(1-e^{-2Kt})]\), so that division by \(\alpha-1\) yields the required divergence constant. Merely naming Harnack or concentration is insufficient.
- **2 points:** Establishes nonincreasing dependence on diffusion time, strict decrease for positive sensitivity, the zero-sensitivity case, the \(K<0\) and \(K>0\) long-time limits, and the continuous flat limit \(\alpha\Delta^2/(4t)\). Treats the positive limiting value as a property of the upper-bound expression, not a universal lower bound on actual privacy loss.
- **2 points:** For \(\varepsilon>0\), correctly inverts the \(K<0\) bound and verifies positive logarithm arguments, positivity of time when \(\Delta>0\), and the privacy guarantee. Gives the \(K=0\) calibration and its agreement with the \(K\to0\) limit. Handles \(\Delta=0\), when the formulas give time zero, by verifying that adjacent time-zero laws coincide.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular truncation construction.

The supplied dimension-free Harnack theorem is a standard-independent external result and may be invoked with its relevant statement and hypotheses; reproving that external theorem is not required. Its conversion to the claimed Renyi bound is a core obligation and must not be replaced by an unsupported assertion of a specialized density consequence.

An argument with a missing \(\alpha-1\) in the integral exponent followed by an unjustified cancellation does not complete the main bound. Assess any independently correct steps, and distinguish an isolated transcription error from a missing or invalid density argument.

For \(K<0\), the assumed Ricci lower bound is positive; avoid reversing this sign convention. For \(K=0\), the conclusion applies under the stated nonnegative Ricci lower bound, not only in Euclidean space. No heat-kernel density at time zero is required: the task explicitly defines the time-zero law as a Dirac measure.
