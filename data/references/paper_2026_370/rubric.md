# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the operator/nuclear descent lemma, conditional mini-batch variance estimates, polar identity and scale invariance, norm inequalities, and the squared Frobenius gradient-gap bound under the stated assumptions. Cross-time noise terms must be justified by conditional centering or another valid argument, not an unsupported assertion that adaptive stochastic gradient errors are independent.
- **3 points:** Analyzes vector-style momentum with the prescribed unscaled update and tuning, obtains the required Frobenius-gradient rate, and converts it to the nuclear-gradient rate with the necessary square-root-of-dimension factor. A valid EMA proof must explicitly control both the squared signal lag and stochastic noise and close the movement-dependent term. Retaining the negative momentum-norm term is one valid approach. Handle the cap-active case and the prescribed zero-noise and zero-gap conventions. Merely asserting the desired EMA estimate earns little credit for this step.
- **3 points:** Uses scale invariance and nuclear/operator duality to obtain direct nuclear-norm descent for the polar update, explicitly controls its signal lag, noise, and initial boundary term, and supplies admissible parameter choices proving all three terms of the polar rate. A valid argument must handle capped tuning and provide a positive polar stepsize in zero-gap cases, rather than substituting zero into a formula requiring a positive stepsize. Merely naming momentum averaging or polar duality without establishing the estimates earns little credit for this step.
- **2 points:** Correctly converts both rates to the displayed sufficient iteration complexities with integer rounding and a minimum of one iteration. Identifies the precise rank improvement: the deterministic rate coefficient changes from d^(1/2) to 1 and the T^(-1/4) coefficient from d^(1/2) to d^(1/4), corresponding to iteration coefficients d to 1 and d^2 to d. Accounts for the additional, faster-decaying polar term d sigma/sqrt(BT) and does not claim uniform finite-horizon dominance or a lower-bound separation from upper bounds alone.

# Evaluator Notes

Accept a complete valid alternative proof and any universal numerical constants. Do not require the reference proof's incidental presentation choices, auxiliary notation, or particular admissible tuning for the polar method. A later step may receive credit if its needed conclusion is established independently. Missing control of the momentum-gradient mismatch is theorem-critical, as is treating nuclear-norm descent as though it followed from a Frobenius argument without duality.

For the vector update, alpha=q^2/(4L) is exactly the prescribed minimum for 0<q<=1. Do not accept an argument that silently replaces this stepsize by a smaller one. In particular, a proof using a parameter theta must verify strict positivity and uniform control of any denominator 1-4 theta; the source's equality tuning does not automatically provide this. A direct analysis of the zero-momentum case or retaining the negative momentum-norm descent term avoids that issue.

The signal-lag and noise components need not be independent. The norm-sum inequalities in the reference proof do not require such independence. The single-sample variance assumption holds uniformly at every point, and the fresh iid batches therefore give the conditional variance bound at adaptive iterates.

The zero-gap vector convention freezes the iterates even with noisy gradients. For the polar method, positive stepsizes remain required; a sufficiently small positive stepsize can handle a noisy zero-gap start, while a noiseless zero-gap start remains fixed. Boundary cases that are omitted but immediately repairable should be assessed according to the scoring guide; a false claim that an inadmissible zero polar stepsize closes these cases is not a complete proof.
