# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omissions.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly sets up the RU values, empirical threshold, population threshold, and simultaneous tail and hinge events at confidence delta/2. Uses the stated positive finite deviation bounds and the smallness condition. All objective differences must be well-defined.
- **4 points:** Derives the uniform threshold displacement bound |hat theta_n(h)-theta^star(h)|<=Delta_n(delta/2) from the two-sided margin and empirical-tail deviation. In particular, the empirical tail is below alpha at the upper bracket and above alpha at the lower bracket. Merely naming a quantile argument is insufficient.
- **2 points:** Gives an exact, correctly signed expansion of the empirical RU error into the population-threshold hinge empirical process, the stated population-tail correction, and a remainder. A hinge-integral derivation must use (x-a)_+-(x-b)_+=-integral_b^a 1{x>s} ds and valid telescoping algebra. An equivalent exact derivation is acceptable.
- **2 points:** Bounds the coupling and curvature remainders for both signs of the threshold displacement by alpha^(-1)[epsilon_n(delta/2)Delta_n(delta/2)+c_+Delta_n(delta/2)^(kappa+1)/(kappa+1)], intersects the events, and gives the uniform leading-term bound and equivalent C_1 rate.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular names for intermediate terms. A separate proof of the classical empirical RU minimizer characterization is not necessary when the argument works directly with the empirical value as defined in the task.

The empirical distribution may have atoms and ties; do not require its tail to equal alpha at the empirical threshold. Do not assume continuity of the empirical tail or that n alpha is an integer. The population correction is zero because P(X_h>theta^star(h))=alpha; a decomposition omitting this zero term is acceptable when its equivalence is clearly justified.

All estimates must hold on one event simultaneously over h. No independence between the two deviation events, or between the empirical threshold and the sample, is available or required. The endpoint Delta_n(delta/2)=u_0 is allowed. A displacement of zero is covered by vanishing integrals. The source specifies epsilon_n>0, so an additional epsilon_n=0 case is not required.

The source contains locally repaired sign and telescoping errors. Do not accept those erroneous identities merely because they appear in the paper. In particular, bounds for negatively oriented integrals must use absolute values or the unordered interval. No specialized quantile representation or heavy-tail concentration theorem is an unproved scoring prerequisite; the deviation bounds are assumptions and the needed deterministic argument must be supplied.
