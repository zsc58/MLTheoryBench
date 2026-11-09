# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Aggregates the Dirichlet coordinates on a green list to a Beta law and derives the logit-shift map, including the exact hypergeometric expression for \gamma'.
- **2 points:** Proves the O(m^{-1/2}) approximation for \gamma' using the Beta variance and a valid concentration/Lipschitz argument.
- **2 points:** Establishes the null i.i.d. Bernoulli(\gamma) law, its standardized CLT, and the asymptotic level-\alpha threshold.
- **3 points:** Executes the central alternative argument: information decay implies geometric alpha-mixing; a stationary mixing CLT with a finite 2+\eta moment, summable \alpha(k)^{\eta/(2+\eta)}, and positive long-run variance applies; and the normalization is \sigma^2=c\gamma'(1-\gamma').
- **1 point:** Combines the detector threshold and alternative normal limit to obtain the stated normal power surrogate and identifies it as an approximation. A rigorous fixed-parameter asymptotic justification may use \gamma'>\gamma and convergence of both actual power and the surrogate to one.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require incidental presentation choices. Merely naming a mixing CLT or Dirichlet identity without applying its hypotheses earns no credit for that step; omission of the mixing-to-CLT bottleneck or an incorrect power normalization is a major gap. Do not demand a uniform moving-threshold approximation, a finite-sample identity, or an error rate: none follows from the stated CLT.
