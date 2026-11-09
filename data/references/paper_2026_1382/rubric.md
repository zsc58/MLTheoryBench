# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly characterizes the FSPA output after \(T\) doubling rounds as the normalized result of \(N_T=2^T-1\) applications of \(\rho\), accounting for intermediate normalizations.
- **3 points:** Decomposes the initial state into \(S_R\) and its orthogonal complement and proves the dominant-component and boundary-eigenvalue norm bounds using the degenerate spectrum.
- **3 points:** Derives the normalized subspace-fidelity lower bound \(\alpha/[\alpha+(1-\alpha)r^{2k}]\) and correctly solves it to obtain a sufficient iteration threshold for fidelity \(1-\varepsilon\).
- **2 points:** Converts the threshold to the doubling schedule and states the resulting oracle complexity with denominator \(\log(\lambda_1/\lambda_{R+1})\) and numerator logarithmic in \(1/\varepsilon\) and \(1/\alpha\).

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the reference proof's incidental presentation choices. The central requirement is the quantitative degenerate-subspace fidelity and boundary-gap complexity result; merely naming power iteration or spectral amplification without deriving the bounds is insufficient.
