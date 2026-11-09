# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly uses or verifies the population measurement identity \(p_A=\theta_AJ_A+1-q_{0,A}\) and identifies the own-calibration population correction as \(\theta_A\).
- **2 points:** Justifies the probability limits of both plug-in corrections from the stated consistency assumptions and nonzero population denominators. The argument respects the defined values on exceptional samples; such values do not change the limits because the exceptional-event probabilities tend to zero.
- **4 points:** Correctly subtracts the target from the shared-calibration population correction and derives \((\theta_A\Delta J-\Delta q_0)/J_B\), without conflating the calibration parameters of A and B.
- **1 point:** Correctly rewrites the bias as \([\theta_A\Delta q_1-(1-\theta_A)\Delta q_0]/J_B\) and recognizes the signed \(1/J_B\) scaling, or its magnitude \(1/|J_B|\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution that merely asserts the estimator limits or the displayed bias formula without justifying the plug-in step and distinct-calibration algebra cannot receive full credit.

The sample-proportion consistencies are assumptions, not conclusions the solver must derive from an unstated sampling model. A correct continuous-mapping or ratio-limit argument with nonzero population denominators suffices; the solver need not reproduce the reference proof's precise exceptional-event bounds or union bound. Do not require independence of the estimated components. Do not accept an argument claiming that population nonzero denominators make empirical denominators nonzero on every sample.

The conditional-law convention permits boundary accuracies whenever the stated calibration assumptions are satisfied. Do not require division by a class probability or introduce an additional restriction \(\theta_A>1/2\). The correction is the stated, untruncated ratio, not its projection onto \([0,1]\).

The amplification statement concerns the exact mismatch term's denominator. It does not require an unsupported comparison of the magnitudes of the \(\Delta q_0\) and \(\Delta q_1\) contributions, nonzero bias for every mismatch, positivity of \(J_B\), or uniform convergence as \(J_B\) approaches zero. The target is convergence in probability, not convergence of expectations; failure to prove expectation convergence is not a defect.
