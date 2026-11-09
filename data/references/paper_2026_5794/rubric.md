# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Conditional Gaussian reduction (2 points):** Correctly conditions on the clock and endpoint, uses the affine interpolation and covariance 2 A(T) I_d, and derives the Gaussian law with mean t x_1 and covariance 2(1-t)^2 A(T) I_d.
2. **Deterministic-clock case (1 point):** Computes A=1/2 for T_s=s and obtains the Gaussian marginal N(t x_1,(1-t)^2 I_d).
3. **Stable-clock bottleneck (4 points):** Represents A as the weighted Stieltjes integral, derives its Laplace transform exp(-lambda^(alpha/2)/2) from the specified stable-subordinator increments, substitutes it into the characteristic function, and correctly identifies the shifted isotropic alpha-stable law and its Theta(r^-alpha) radial tail. Naming stability without the Laplace-transform derivation earns only partial credit.
4. **Student-t mixture (3 points):** Computes A=V_nu/2 for the inverse-gamma clock, performs the Gaussian/inverse-gamma integral with correct constants to obtain the multivariate Student-t density with nu degrees of freedom, and establishes the Theta(r^-nu) radial tail.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Standard independent facts about stable and Student-t tail asymptotics may be invoked after their hypotheses are verified. The score should reflect the mathematical achievements actually established; omissions of a theorem-critical transform or mixture calculation are major gaps.
