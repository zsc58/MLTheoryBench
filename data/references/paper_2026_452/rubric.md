# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Mean-field maximizers.** Correctly enumerate magnetization masses (or give an equivalent derivation) and establish the unique negative class-0 maximizer and the two class-1 zero-field maximizers \(\pm m_*\). Merely citing a phase-transition slogan without checking these conclusions earns no credit for this step.
- **3 points: Concentration and phase weights.** Prove concentration at \(m_0\) for class 0 and near \(\{\pm m_*\}\) for class 1, and derive the tilted limiting weights \(p=\sigma(2cm_*)\) and \(1-p\). This is the central bottleneck; both the two-phase limit and its weights must be justified.
- **2 points: Marginals and dependence-aware rule.** Derive the limiting one-coordinate marginals, show they are on the informative sides of \(1/2\), use the separation assumption to obtain \(|m_0|<t<m_*\), and prove the absolute-magnetization risk and hence Bayes risk tend to zero.
- **3 points: Product-marginal classifier and excess risk.** Reduce the oracle product-marginal posterior to its vote-fraction threshold, establish the ordering placing the negative class-1 phase below the threshold and the positive phase above it, and conclude risk \(\pi(1-p)\) and the same limiting excess over Bayes risk.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof may use another rigorous large-deviation or Laplace argument in place of the displayed free-energy calculation. Do not award the phase-weight points merely for asserting a generic two-phase phenomenon. If an intermediate derivation is flawed but its needed conclusion is independently proved, score downstream achievements based on what is actually established.
