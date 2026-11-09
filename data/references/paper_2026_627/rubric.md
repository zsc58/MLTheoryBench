# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the directional SPO-loss bound with L=Delta(S)rho(C)/(2eta). Establishes scale invariance under consistent tie breaking; proves the needed degeneracy-distance geometric estimate or gives a complete valid alternative; combines the reciprocal inequalities with the correct sign and applies normalization and Cauchy-Schwarz. An unexplained citation to the specialized geometric theorem does not close this obligation.
- **3 points:** Correctly analyzes adaptive importance weighting and concentration. Establishes conditional unbiasedness for active-pair excess loss, including omitted zero-probability designs; bounds the realized weighted excess loss by gamma L; constructs fixed-hypothesis martingales with predictable stopping, or an equivalent rigorous device avoiding circular reliance on retention; and obtains the required simultaneous deviation bound over hypotheses and all times with justified constants and a summable failure probability.
- **2 points:** Proves by induction that h* remains in the nested confidence sets on the deviation event, using nonnegative population excess risk and empirical minimization. The argument must not obtain concentration by conditioning on future survival.
- **2 points:** Uses retention and empirical optimality to bound every post-update retained hypothesis by 2r_T=4gamma L sqrt(log(2T|H|/delta)/T) on one event of probability at least 1-delta. Handles stopping, including stopping before the first query, and zero cases without dividing by zero.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the directional geometric bottleneck or the adaptive importance-weight concentration argument as theorem-critical.

Individual importance-weighted losses need not be unbiased when some designs have zero sampling probability; the relevant unbiasedness is for differences between active hypotheses. Do not require a false individual-risk unbiasedness claim.

The conditional-range form of Azuma-Hoeffding is sufficient: a realized excess loss in [-B,B] gives a centered increment in a predictable interval of length 2B. It does not generally give a centered absolute bound B. A proof using an absolute bound 2B must still independently justify the requested numerical constant.

A union bound must range over fixed hypotheses and include an explicit summable allocation across all positive integer times. Merely calling a data-selected surviving hypothesis a martingale index, or saying that a standard adaptive argument applies without resolving survival and support changes, leaves a critical gap.

The geometric inequality is used only when Delta(S)>0. Singleton S, gamma L=0, zero pool masses, and zero sampling probabilities require no additional positivity assumptions. Minor omitted deterministic edge cases may be readily repairable; a circular or unsupported concentration argument is not a complete proof.

The procedure uses the explicit r_t in the public task. Do not require a solver to recover a source initialization, source recursion, or source-local repair that is not part of the public problem.
