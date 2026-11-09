# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Express marginal coverage as \(\mathbb E[D_{n,k}]\) by conditioning and establish the beta reference mean \(k/(n+1)\).
- **3 points:** Derive \(|\operatorname{Cov}(k)-k/(n+1)|\le W_1(\nu_{n,k},\beta_{n,k})\le W_p(\nu_{n,k},\beta_{n,k})\le\rho\) using the Lipschitz mean bound and Wasserstein monotonicity.
- **3 points:** Construct or use the monotone beta-to-\(\nu_{n,k}\) transport, identify its pth displacement moment with \(W_p^p\), split the tail event, and obtain \(\Pr(D_{n,k}\le t)\le F_{\beta_{n,k}}(t+\varepsilon)+(\rho/\varepsilon)^p\).
- **2 points:** Prove the almost-sure-displacement sharpening and the nominal-level consequence \(|\operatorname{Cov}(k_\gamma)-\gamma|\le\rho+1/(n+1)\).

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Naming a coupling or transport without deriving the event inclusion and penalty is insufficient; omission of either the tail argument or the coverage conclusion is theorem-critical.
