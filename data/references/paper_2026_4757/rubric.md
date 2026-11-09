# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the compatible noiseless mixture, the nonempty active set, and the standardized coefficients. Establishes or correctly invokes the given variance normalization and sum_j alpha_j^2=1.
- **4 points:** Establishes K(y)=sum_j alpha_j^4 K(s_j), obtains the absolute-value bound, and applies balance to prove |K(y)|<=beta K_max/q. Accept either a direct fourth-moment expansion or a precise statement and correct application of fourth-cumulant additivity and homogeneity, with centering, independence, moments, and normalization accounted for. Merely naming a method without the identity and subsequent estimates does not complete this step.
- **1 point:** Establishes K(y)=K_0/q for equal squared weights and common source kurtosis, identifying the nonzero-K_0 case as the witness to order sharpness. An explicit source distribution witnessing nonzero kurtosis is welcome but not required.
- **3 points:** Derives both necessary screening inequalities with the correct strict and non-strict endpoints. Treats the standard-deviation bound as an explicit hypothesis, not a finite-sample theorem to be proved from finite eighth moments. Does not claim sufficiency or turn the standard-deviation upper bound into a lower bound on actual estimation error.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its explicit sharpness example. A proof may use the normalization already supplied in the task rather than rederive it.

No proof of an estimator variance theorem is required. The finite-eighth-moment and estimator assumptions apply only to the sampling comparison; the population bound, equality case, and fixed-contrast ceiling use finite fourth moments.

The argument must remain valid when K_max=0: then the positive-contrast antecedents are false. Do not require a separate discussion if the proof handles this case without dividing by K_max. Likewise, no separate discussion of q=1 or beta<1 is required when the reasoning already covers them. Balance and normalization automatically imply beta>=1 for any actual balanced projection.
