# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates the conditional population objective \(\mathcal R_x(q)=\sum_y P^*_{Y\mid X}(y\mid x)\operatorname{KL}(q\|\pi_y^\nu)\) and the outer expectation over \(P_X^*\), respecting the inherited Dirichlet predictor family and the possibility of infinite population risk for competing predictors.
- **3 points:** Correctly computes the expected log-density coefficients as \(\alpha_k-1+\nu P^*_{Y\mid X}(k\mid x)\), recognizes that label normalizers are constant in \(p\), and uses valid conditional integral manipulations. Positive Dirichlet parameters justify the required logarithmic integrability, including when some conditional class probabilities vanish.
- **3 points:** Uses the Gibbs variational principle or an equivalent KL argument to obtain the normalized conditional optimizer \(\operatorname{Dir}(\alpha+\nu P^*_{Y\mid X}(\cdot\mid x))\), establishes its uniqueness as a probability law, and transfers the result to every population minimizer almost everywhere. The transfer must justify or validly imply a finite attainable oracle population risk; a uniform comparison with \(\operatorname{Dir}(\alpha)\), a bound on the normalizers, or another correct argument is acceptable. Simultaneous representability by one model parameter, rather than separate parameter choices for each \(x\), must be used.
- **2 points:** Derives total evidence \(\alpha_0+\nu\) and vacuity \(K/(\alpha_0+\nu)\), with the same almost-everywhere qualification, and explains independence from \(n\) when the prior, temperature, and DGP are fixed.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental notation, its explicit normalizer formula, or its particular prior-comparison bound. A valid proof over a larger class of densities also proves the stated result, but any additional integral manipulations must be justified.

Treat omission of the conditional variational minimization, an incorrect Dirichlet parameter calculation, or an invalid transfer from separately chosen pointwise parameters to one population predictor as theorem-critical gaps. Distinguish a routine omitted integrability estimate from an actual undefined infinity-minus-infinity argument. The reference proof supplies all needed estimates without imposing finite population risk on every predictor.

Do not require uniqueness of network parameters, strictly positive conditional class probabilities, bounded network outputs uniformly over \(x\), or an empirical-estimator convergence theorem. Do not award the uncertainty consequence for a claim that every uncertainty functional is determined solely by total concentration; the statistic specified in the task is vacuity. No upper bound of one on vacuity is assumed for the unrestricted positive prior concentrations. Statements about all covariates, including arbitrary \(P_X^*\)-null locations, are not justified by population-risk minimization.
