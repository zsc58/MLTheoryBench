# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Specifies the hard distribution and Walsh binary prediction-independent family, including the constant group. Establishes the threshold-sign Walsh expansion, the O(log m) sum of coefficient maxima, and a uniformly accurate subsampled representation with O(log^3 T) indices. The chosen set must work simultaneously for all thresholds and grid points and must be fixed independently of the forecaster.
- **3 points:** Uses predictable threshold weights and the half-group difference/triangle argument to derive E[A]<=O(log m) E[MCerr], where A=sum_t|p_t-x^t|. Conditional expectation must be applied before the current outcome is revealed, not after conditioning on a final random bucket. Handles predictions equal to grid points and the constant coefficient.
- **2 points:** Proves that l1 honesty forces prediction diversity, obtaining E[N]>=T/[4 sqrt(E[A]+T/m+1)] or a quantitatively equivalent universal-constant bound. Also derives the predictable adaptive Rademacher-bucketing bound E sum_v|U_v|>=Omega(E[N]/log(T+1)). For the latter, justifies the potential increase at zero, the excursion decomposition, conditional independence of predictably selected increments, and the truncated return-time estimate. A citation to the paper-specific adaptive-bucketing theorem alone does not close this step.
- **3 points:** Transfers bucketed noise through the constant group's pathwise reverse-triangle inequality, combines the inequalities without changing the placement of expectation or maximum, performs a valid two-case comparison, and concludes E[MCerr_T(G_S)]>=Omega(T^(2/3)/log^C(T+1)) with universal constants and the correct quantifier order. The same S must work for every possibly randomized forecaster.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its approximation tolerance, or its particular universal constants. A direct grid-spacing argument and the source's uniformly spaced proxy argument are both acceptable ways to prove diversity.

Treat omission of the Walsh-to-l1 mechanism, the diversity estimate, or the adaptive-bucketing lower bound as theorem-critical gaps. In particular, do not award full proof credit for replacing the adaptive-bucketing argument with an unsupported claim that a bucket conditioned on its final size is an ordinary independent random walk.

A standard simple-symmetric-random-walk first-return law or tail estimate may be used with its relevant statement and hypotheses supplied. The tail summation uses k>floor(a/2), not k>ceil(a/2), because the first return takes even values. An isolated indexing typo that does not invalidate the resulting estimate is a readily repairable error.

Prediction labels need not belong to a fixed finite or countable set. Excursion starts may be indexed chronologically, or a proof may condition on the learner's independent full random seed and justify any resulting finite-support argument. Either approach must avoid unjustified interchange of expectation with a sum over random real-valued labels.

The repaired reference proof has no unresolved theorem-critical obligations; no incomplete private step should be treated as an established fact for scoring purposes.
