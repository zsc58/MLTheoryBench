# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Verifies that the reweighted law and normalized push-forward are well-defined and proves the decision-risk identity. A loss-homogeneity argument is sufficient; any valid alternative is accepted.
- **3 points:** Proves the squared-loss change-of-variables identity with exactly the factor $1/C$. The argument must apply to every measurable predictor, allowing infinite squared and weighted-spherical risks through nonnegative integration.
- **3 points:** Establishes existence and the almost-sure characterization of every weighted-spherical Bayes minimizer. The reference route proves positivity of the conditional expected norm, completes the conditional square, verifies a measurable finite-risk minimizer, and uses the nonnegative integrated gap to obtain almost-sure uniqueness. The unit-ball bound is a convenient finiteness justification, not a mandatory intermediate result for an alternative proof.
- **2 points:** Proves that every surrogate Bayes minimizer induces a conditionally optimal decision and hence minimizes global decision risk. The argument must remain valid when the conditional mean is zero and must justify the stated conditional/global equivalence, either explicitly or through a nonnegative conditional-gap argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its ordering, or its particular intermediate formulas.

A separate zero-conditional-mean case split is not required. If $a(x)=\mathbb E[\|Y\|\mid X=x]>0$, then $m(x)/a(x)$ is a strictly positive scalar multiple of $m(x)$ even when $m(x)=0$. The scale-invariance identity $w^*(\alpha c)=w^*(c)$ for $\alpha>0$ applies to $c=0$ as well. An argument using this identity for all cost vectors covers the zero case completely. Conversely, a proof that divides by $\|m(x)\|$ without covering zero conditional means has a genuine gap.

Both requested risk identities and the conclusion for every surrogate Bayes minimizer are substantive obligations. Producing only one optimal surrogate predictor does not by itself establish the universal conclusion unless all minimizers are characterized or an equivalent argument is supplied. The unrestricted Bayes domain must not be replaced by a bounded nonzero-output hypothesis class.

The public task supplies oracle measurability. Do not require a measurable-selection construction. Standard conditional-expectation facts and nonnegative push-forward integration may be used without reproving their general measure-theoretic foundations. Do not impose an additional positive lower bound on the cost norm or on the conditional mean.
