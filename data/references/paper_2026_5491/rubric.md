# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Proves both $P_{\rm esc}\le nq$ and $P_{\rm esc}=nq(1+O(nq))$ for the stated positive integer attempt count, with a remainder uniform as $nq\to0$. Give partial credit for either estimate alone; both are required for full credit in this category.
- **3 points:** Correctly handles the signed Bernoulli bit contributions conditional on the stored weight and derives the factorized conditional characteristic function for every real $t$.
- **3 points:** Uses the offset-binary identities to obtain the exact conditional mean $-2pw-p\delta$ and computes the exact conditional variance $p(1-p)\delta^2(4^b-1)/3$.
- **2 points:** Establishes the MSB variance fraction's limit $3/4$, proves that the specified third-absolute-moment Lyapunov ratio has a finite strictly positive limit for every fixed $p\in(0,1)$, and validly excludes convergence of the standardized conditional laws to $\mathcal N(0,1)$ for arbitrary sequences of stored grid values. Assess these three conclusions separately for partial credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The WKB formula and the displayed escape and threshold-binomial formulas are supplied in the public setup. Their probabilistic interpretation may be justified briefly, but deriving the WKB law from quantum mechanics or independently rederiving every supplied probability formula is not a scoring requirement. The two escape estimates are explicit targets and must both be proved.

The attempt count $n=f\tau$ is a positive integer, not a continuously varying exponent or the mean of a Poisson attempt count. A Taylor proof of the small-escape estimate is acceptable if its remainder gives the required uniform relative $O(nq)$ control.

All bit calculations are conditional on the stored value. In the precision limit, the stored bit pattern may change arbitrarily with $b$; no distribution over stored weights, consistency of bit patterns across precisions, or independence across precisions is required. Do not impose a restriction $p<1/2$ or exclude $p=1/2$.

A positive limiting Lyapunov ratio shows failure of that sufficient central-limit condition, but does not alone establish failure of Gaussian convergence. Full credit requires a separate valid justification of the latter conclusion. The reference proof uses bounded support of the standardized sums; another valid argument is equally acceptable. A solution that treats failure of the Lyapunov condition as a necessary-and-sufficient obstruction has not completed this part of the proof.

The public target requires existence and strict positivity of the Lyapunov limit, not a particular simplification of its numerical constant. Exact computation is one acceptable way to prove the target. No higher-moment theorem, layer-output central-limit result, compensation guarantee, bit-allocation result, or saturation analysis is required.
