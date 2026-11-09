# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Derives the weighted OLS normal-equation expression and identifies the conditional mean using centered training noise and fixed weights, including the auxiliary-weighted parameter and its bias relative to the main task. Justifies the almost-sure invertibility needed for the estimator.
- **3 points:** Correctly computes the conditional covariance from independent centered task noises and evaluates the expected prediction-variance contribution using the inverse-Wishart identity or an equivalent exact calculation, obtaining the factor \(d/(N-d-1)\) under \(N>d+1\).
- **3 points:** Completes the bias-variance decomposition for a fresh independent main-task example and obtains the exact \(E_K\) formula, including irreducible noise and the \(\Lambda^2/(1+\Lambda)^2\) mismatch term, together with the zero-weight baseline \(E_0\), without requiring normalized auxiliary weights to be defined at \(\Lambda=0\).
- **2 points:** Reparameterizes by \(\lambda'_k\), compares the exact expressions, and proves both directions of the stated necessary-and-sufficient inequality for positive transfer. The algebra must remain valid when noise variances vanish or the bracketed coefficient is zero or negative.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or the name of a particular probability distribution if the exact design-moment calculation is otherwise justified. Treat an unjustified exact random-design variance factor or an incorrect squared \(\Lambda\) bias factor as a theorem-critical gap.

The weights in the task are deterministic, and the training noises are centered. The test feature and test noise are mutually independent and independent of training. A proof must not replace these with adaptive weights or correlated noises.

Zero variances and zero individual auxiliary weights are permitted. A proof whose calculations already cover these cases need not discuss them separately. Do not require division by the bracketed comparison coefficient, a positive main-task noise variance, or strict positivity of every auxiliary weight. The baseline may be established directly from main-task OLS or an equivalent argument that does not use an undefined normalized auxiliary parameter.
