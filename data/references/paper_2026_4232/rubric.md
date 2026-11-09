# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates the objective over probability densities, expands the KL term, and establishes that the normalizing integral \(Z=\int_M e^{-G/\tau}p_0\,d\mu\) is finite and strictly positive.
- **2 points:** Proves existence/optimality by constructing the normalized candidate and establishing the objective-versus-relative-entropy identity (or an equally valid complete existence argument under the stated assumptions).
- **4 points:** Carries out the normalization-constrained variational calculation (or a fully equivalent derivation) to obtain \(p(m)=C e^{-G(m)/\tau}p_0(m)\), and determines \(C=Z^{-1}\); merely naming a Gibbs principle earns no credit for this step.
- **2 points:** Establishes uniqueness by the equality condition for relative entropy or strict convexity, including the relevant almost-everywhere qualification.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
