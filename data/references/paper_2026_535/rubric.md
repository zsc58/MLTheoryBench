# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establish normalization on the stated population domain, derive concavity and KL-relative smoothness with constant L_f r_max, and justify existence and uniqueness of the regularized minimizer. The optimizer-existence argument must not rely on strict convexity alone. Handle a zero smoothness bound by retaining a positive algorithmic L.
- **3 points:** Derive the population functional derivative from the CDF variation, compare it to the defined empirical plug-in estimator, and use the Lipschitz property and conditional DKW tail integration to prove E[||e_t||_sp,x^2|pi_t]<=L_f^2 r_max^2/M. Use the half-range seminorm and justify averaging over contexts without claiming a uniform empirical-CDF bound over all contexts.
- **3 points:** Derive the inexact KL three-point relation using the full separated residual ghat_t+L log(p_{t+1}/p_t)+beta log p_{t+1}. Retain the estimation-error pairing when replacing the population gradient. Obtain the explicit one-step bound with coefficient L+beta/2 and additive 2(A_t+B_t)/beta using Holder, Pinsker, and Young, where A_t and B_t are the context averages of squared span seminorms.
- **2 points:** Telescope with weights q^k, correctly evaluate their geometric sum, and use the independent output-index draw to obtain the exact initial-KL coefficient, denominator q^T-1, and floor 2(epsilon+delta)/beta. Substitute the empirical error bound and distinguish the O(1/M) sampling term from the 2 delta/beta optimization term.

# Evaluator Notes

Accept any complete valid alternative proof; the displayed architecture is not mandatory. All seven obligations listed in the reference proof must be supported for full credit. Do not award completion credit for merely naming DKW, mirror descent, or a three-point theorem without stating and applying the needed inequality.

The population reward-density condition and empirical plug-in definition are different: empirical measures are allowed to be atomic. Do not require them to have densities. Conversely, differentiating the literal right-CDF-weighted atomic reward is not a substitute for analyzing the estimator defined in the task.

The span seminorm is half the essential range with respect to the reference kernel at each context. Equivalent rescalings are acceptable only if the assumptions and constants are translated consistently. There is no supremum over contexts in the empirical-concentration target.

The empirical surrogate in the source already includes the reference KL. Its derivative plus the proximal logarithm is equivalent to the separated residual in the task; adding a second reference-KL derivative is incorrect. The source's isolated omission of the estimation-error pairing is not a valid proof step and has been repaired in the reference proof.

A fixed positive delta does not yield a total O(1/M) floor. The O(1/M) statement for the entire floor requires delta=0 or delta=O(1/M).

Propagate a failed dependency only when the final contraction, empirical estimate, or optimizer claim is unsupported. A small constant or indexing slip can be readily repairable; an undefined estimator, an invalid atomic integration-by-parts argument, or omission of an uncontrolled error pairing is theorem-critical.
