# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes that the initial sample is independent of the latent variable and query label, and correctly derives \(\mathsf E_n=\log 2\), \(\mathsf A_n=0\), and \(H(Y^\dagger\mid S_n)=\log 2\).
- **3 points:** Proves that arbitrary finite deployment-distribution acquisitions preserve this independence and hence give \(\mathsf E^{\mathcal C_\rho}_\infty=\log 2\), while the single input-\(1\) acquisition reveals the latent variable and gives \(\mathsf E^{\mathcal C_1}_\infty=0\).
- **2 points:** Correctly draws the acquisition-relative trichotomy conclusion: the exhibited uncertainty is neither aleatoric nor deployment-sample-reducible, but is reducible by another mechanism.
- **2 points:** Uses the same numerical facts to prove the incompatibility between the mutual-information convention and the binary deployment-reducibility convention, including why the latter's forced aleatoric assignment contradicts \(\mathsf A_n=0\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
