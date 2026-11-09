# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the required path-law absolute continuity and finiteness from the endpoint and rate-support assumptions, using a valid finite-state CTMC likelihood or equivalent argument. A derivation of the local `Phi` expression earns full credit; merely naming a change-of-measure theorem without checking its hypotheses does not.
- **4 points:** Correctly inserts `mu_0` into the averaged negative path ELBO and proves `N-H(mu_0)=KL(J||M)` for the corresponding noising and comparison joint laws. Sign errors in the entropy term are material.
- **4 points:** Uses the Markov property to factor the noising joint law through `P` and `mu_(0|t1)`, factors the comparison law through `R` and `d`, and applies the KL chain rule to obtain exactly the decoder mismatch plus `KL(P||R)`.

# Evaluator Notes

Accept any complete proof under the stated assumptions, including a direct joint-density calculation or another rigorous path-space argument. The central achievement is the joint-law reinterpretation followed by the correct Markov factorization and KL decomposition, not the naming of those operations.

Do not automatically withhold the final four points because an earlier absolute-continuity derivation is flawed if the solver independently establishes the needed domination and then gives a valid factorization and decomposition. Conversely, an asserted final identity without the joint-law or equivalent derivation has a theorem-critical gap.
