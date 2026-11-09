# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct proof of the stated conditional claims, with only readily repairable errors or omitted cases.
- **10:** Fully correct proof of the stated conditional claims. Do not require a proof of the separately unresolved constructive architecture-existence claim.

# Core Steps

1. **Geometric converse (3 points).** Derives the normalized score decomposition, projection residual, principal-angle signal term, and ambient-noise term with the correct integral.
2. **Comparator bounds (3 points).** Proves both rank cases, including the output-side term \(d_2-\sum_{j=1}^{d_1}\cos^2\theta_j\) when \(d_1<d_2\), the information-loss term, the pseudoinverse noise term, and the ambient-noise coefficient.
3. **ReLU transfer (2 points).** Applies the quadratic comparison and the explicit architecture-capacity premise to obtain the constrained-risk rate. A claimed construction of an architecture from the specialized external approximation result is not an established step merely because that result is named.
4. **Finite-sample closure (2 points).** Uses the integrated conditional denoising loss and derives both the truncation-event probability and discarded-loss second-moment bound from the latent density tail, Gaussian components, independence, and tail integration. Applies bounded-loss covering concentration and the denoising identity. Retains \((1+a)^2\), \(1+1/a\), \((2+a)\iota\), and \((2a+a^2)E_2\), and states both requested substituted inequalities.

# Evaluator Notes

Accept any complete valid alternative proof. The empirical loss is an integral conditional on each initial observation, not a single sampled-time/noisy-pair loss. Do not award the comparator step for replacing the \(d_1<d_2\) output-side term by a sum of only \(d_1\) squared sines. Naming Gaussian concentration without establishing the probability and weighted-tail estimates does not complete finite-sample closure. The architecture-capacity premise is a condition of the public theorem; its advertised constructive realization remains the private GT gap disclosed in the audit.
