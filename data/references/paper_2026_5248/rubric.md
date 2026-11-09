# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the needed positivity and spectral properties of B and Q and derives the deterministic residual bound for the stated step-size range. Positive semidefiniteness together with a justified nonzero denominator suffices for this inequality; proving strict positive definiteness is also valid but is not separately required for full credit.
- **3 points:** Establishes a probability-at-least-1-delta initialization event and a noncircular finite-horizon induction on it. Chooses control and regularization-threshold constants independently of N and delta, verifies unique solvability of the Newton updates, justifies the push-through representation, and bounds output weights, residuals, and neuron-wise directions at the required scale. It is not necessary to prove successful training on every initialization.
- **3 points:** Derives the effective-kernel comparison, including the residual-dependent preconditioner, movement from initialization, and initialization concentration. Retains the regularization factors until they can legitimately be absorbed into constants depending on the fixed gamma. If using a named concentration theorem, states its relevant hypotheses and verifies them. Concentration is established before conditioning; conditional expectations may be bounded using P(Omega_R)>=1/2. Merely asserting kernel concentration without controlling these terms earns at most 1 of these points.
- **1 point:** Bounds the Taylor remainder using the output-Hessian norm on the entire update segment and compares the finite and deterministic recursions. Obtains the finite-horizon trajectory bound, with correct conditional expectations, maximum-over-time control if used, and probability accounting.
- **1 point:** Combines the trajectory estimate with the deterministic residual estimate by the triangle inequality, obtaining exactly the target inequality on a successful-training event of probability at least 1-2delta.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular deterministic control constants. Constants may depend on the fixed alpha, gamma, data, initialization law, residual threshold, and horizon; they must not depend on N or delta.

The M=1 case must not rely on a vanishing log M sampling error. A log(2M) or max(1,log M) concentration bound is valid, with its M=1 contribution absorbed into N^{-(1-beta)}. Stronger valid concentration estimates are also acceptable.

At K=0 the problem reduces to initialization control. Do not require kernel evolution or a Taylor remainder for that case, and do not accept a bound that incorrectly multiplies the nonzero initialization error by K.

The public assumptions require every input to be nonzero and no two inputs to be collinear. They do not impose moments on w or eta, nonzero labels, or positive variance of c. Do not introduce these as necessary assumptions.

A proof may use only positive semidefiniteness for the final spectral inequality. If it additionally relies on specialized feature linear independence or strict positive definiteness, a bare paper-specific citation is not a completed proof obligation. The reference proof supplies a direct derivation.
