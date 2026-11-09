# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly sets up the canonical conditional density relative to the base prior, including its partition function and the relevant measurability, positivity, and normalization conditions.
- **3 points:** Performs the hierarchical integration and factors out \(\pi\), obtaining a nonnegative measurable function of \(F(x)\) alone. Correctly handles the possible extended-valued integral by noting that normalization makes it finite \(F_\#P\)-almost everywhere.
- **3 points:** Gives a valid maximum-relative-entropy argument for the complete pushforward-law constraint. This may use conditional Jensen/data processing for KL divergence, or an equivalent rigorous argument, and must show that the factor multiplying \(\pi\) is the Radon--Nikodym derivative of the prescribed pushforward law relative to \(F_\#P\).
- **2 points:** Identifies \(F_\#p_q\) as the effective constraint and concludes that the normalized mixture minimizes \(D_{\mathrm{KL}}(\cdot\|\pi)\) among normalized densities with that law, including the conventional extended-value interpretation of KL divergence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award the maximum-entropy step only when the answer justifies the variational claim for the complete marginal-law constraint; merely naming exponential families, hierarchical mixtures, or indicator constraints is insufficient.
