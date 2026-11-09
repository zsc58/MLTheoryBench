# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points: Effective-opportunity intensity.** Correctly uses the specified independent Bernoulli filter decisions conditional on the complete baseline configurations to obtain the product retention probability, applies marked-Poisson thinning and superposition/integration over latent types, and derives the stated finite positive rate \(\alpha_{rj}\). Merely naming thinning without deriving the rate does not earn full credit. An equivalent argument using Poisson counts on the preimages of time intervals is acceptable.
- **2 points: Exponential race and softmax.** Establishes independent exponential first-arrival times and computes the winning probability as \(\alpha_{rj}/\sum_k\alpha_{rk}\), then obtains the softmax representation from \(f_{rj}=\tau\log\alpha_{rj}\).
- **1 point: Aggregate mean decomposition.** Uses conditional expectation for the trip choices to prove \(\lambda_{rj}=\rho_rp_{rj}\) and correctly separates the row total from the allocation. The identity must remain valid when \(\rho_r=0\); normalizing the mean row is not required.
- **3 points: Exact identifiability characterization.** Proves both directions: equal allocations are equivalent precisely to row-wise positive rescaling of intensities and to common additive offsets of scores at the same fixed temperature. Then uses the kernel of \(H_r\) to show that \(H_rf_r\) is the unique zero-mean representative and is distinct from production scale.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that only shows invariance under rescaling, without proving that this is the entire ambiguity, has a material gap in the final step. Failure to derive the filtered intensity leaves the characteristic central mechanism unsupported even if the subsequent normalization algebra is correct.

The standard independent-thinning theorem may be used without reproving it. Its applicable randomization hypothesis is the prescribed independent Bernoulli law conditional on the entire baseline configuration, not merely mutual independence of decisions conditional on marks. A concise application that uses the explicit setup and derives the product rate is sufficient; no particular conditioning notation is required. Retention rules coupled to baseline arrival gaps do not satisfy the revised setup when their conditional success probabilities given the complete configurations differ from the displayed probabilities.

The setup permits \(\rho_r=0\). In that case the mean row is zero, and division by its row total is undefined. If a solution uses normalization of the mean row, that step must be restricted to \(\rho_r>0\). A correct conditional-expectation proof that never divides by \(\rho_r\) need not give a separate zero-production case to earn full credit. An otherwise correct proof with only an unqualified optional normalization sentence has a readily repairable local error; do not treat the theorem itself as false or require a stronger public assumption.

Identifiability concerns the destination-choice probability law at the given temperature. Do not require recovery of that law from a zero-production count row, statistical independence of production scale and exposure, or observation of the arrival times. The finite nonempty destination set may be a singleton; a general argument that already covers this case needs no separate case split.
