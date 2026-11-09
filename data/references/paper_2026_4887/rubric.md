# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly handles the hierarchical posterior and the expected reduction in marginal parameter entropy. Establishes the one-step logarithmic characterization with a finite candidate-independent additive term. A derivation through joint predictive entropy, expected posterior entropy, or an equivalent valid argument is acceptable. Merely computing entropy conditional on a known variance does not complete this step.
- **3 points:** Establishes the exact maximizing sets using the common additive term and logarithmic monotonicity. Handles zero-weight steps as no observations, including mixed pools where all quadratic scores vanish, and the case with no positive-weight candidates. The proof must justify why a positive-weight candidate has strictly positive marginal information even when its vector is zero.
- **3 points:** Derives the rank-one precision/determinant recursion, telescopes it for any admissible sequence, and converts cumulative quadratic scores using 0<=x_s<=1 and log(1+x)>=x/2, or a valid equivalent estimate.
- **2 points:** Bounds the terminal determinant using trace(V_t^{-1})<=d+t and eigenvalue AM-GM, obtains 2d log(1+t/d), covers the empty sum, and concludes the stated fixed-d asymptotic bound.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its explicit digamma expression for the additive constant, or its particular proof of strict positivity. A proof using entropy scaling and a rigorously established shared-scale dependence argument can receive full credit without evaluating the scalar constant in closed form.

The source and the task concern marginal parameter entropy after integrating out the latent variance. The covariance factor update is response-independent, but the marginal posterior scale is not. Assigning the exact value (1/2)log(1+pi(z)z^T Vz) to marginal information, or replacing the variance hierarchy by a known variance, leaves a theorem-critical error.

A positive-weight zero-vector observation may inform the parameter through their shared latent variance. It is not equivalent to a zero-weight step, which reveals nothing. Do not accept the unrestricted quadratic-score maximizing set over the entire pool in the mixed zero-score case.

The cumulative score bound is deterministic and holds for every admissible sequence. A proof may discuss greedy selection, but its argument must establish the universal-sequence statement; restricting the proof to a special greedy sequence without justification is insufficient. The displayed quadratic score is not the sum of exact marginal information gains.

Treat omission of the determinant/trace bottleneck or a justified conversion from logarithmic increments to quadratic scores as theorem-critical. Do not require inversion of S_t or any positive lower bound on its eigenvalues. No minimum degrees of freedom beyond positivity, finite-variance assumption, estimation-error theorem, sample-complexity theorem, or batch-information theorem is needed.
