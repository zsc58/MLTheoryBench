# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly proves unbiasedness and derives the exact variance identity, including the subtraction of $I_S(v)^2$, and obtains the upper bound in terms of $\Gamma_S$.
- **4 points:** Reorganizes $\Gamma_S$ by $r=|S\cap T|$ and $q=|T\setminus S|$, obtains the correct binomial-ratio or equivalent representation, and performs the substantive boundary/interior analysis. Merely asserting that a combinatorial estimate is standard does not earn this step.
- **2 points:** Establishes $\Gamma_S=\Theta(\log n)$ for $s=1$ and $\Gamma_S=\Theta_s(n^{s-1})$ for every fixed $s\geq2$, with both upper and lower estimates and the allowed dependence on $s$ handled correctly.
- **2 points:** Applies the combinatorial estimate to prove the variance upper bounds and constructs a bounded value function, such as a nonzero constant function, whose interaction vanishes and whose exact variance attains the matching rates.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that derives only upper bounds cannot receive the final 2 points for worst-case tightness. If the exact variance formula or the combinatorial factor is independently established despite an earlier flawed derivation, score valid downstream uses of that established conclusion normally. Treat an unsupported assertion of the order-dependent estimate for $\Gamma_S$ as a theorem-critical gap.
