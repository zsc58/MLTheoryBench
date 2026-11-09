# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the normalized Boltzmann densities and their positivity and differentiability, with the stated absolute-continuity and gradient-error integrability conditions. Recognizes that the logarithms and log-density ratio are well-defined. These checks may be integrated into the argument rather than presented separately.
- **4 points:** Derives the score-difference identity and computes the relative-score integral as beta^2 times the p_eta-expectation of the squared PMF-gradient error. Establishes its finiteness from the precise moment assumption. Introducing the symbol J is optional.
- **3 points:** Applies the stated logarithmic Sobolev inequality to q=p_eta with its hypotheses satisfied, the correct direction, and the constant 1/(2 rho). Does not presume finite KL as an extra assumption needed to invoke the stated inequality.
- **1 point:** Combines the calculation and LSI to obtain the exact beta^2/(2 rho) bound for the required distributions, including zero gradient error without an invalid division.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or a separately named relative Fisher divergence. A direct computation of the integral appearing in the assumed LSI is sufficient.

Do not require a proof of the assumed LSI, a conditional projected-force identity, a training-loss decomposition, a sampling argument, or an optimization guarantee. The requested expectation is under p_eta, not under p*. Replacing that measure or reversing the KL arguments changes the claim and is not justified by the force-matching context.

Only the squared gradient difference is assumed integrable under p_eta. Do not require separate second moments of the two forces, integrability of the two energies separately, or a separately assumed finite KL. KL finiteness follows after applying LSI. An explicit negative-part bound for the KL integral is a permissible detail, not a required presentation step.
