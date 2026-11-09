# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Symmetric full-conformal construction and coverage (3 points).** Defines the augmented candidate-labeled sample and full scores excluding each target's own indexed occurrence, proves permutation equivariance, and correctly invokes or proves finite-sample full-conformal coverage at the true candidate. The relevant rank is $r=\lceil(n+1)(1-\alpha)\rceil$. A correct argument allows ties and uses an infinite threshold when $r=n+1$. A direct rank proof may count at most $n+1-r$ coordinates having at least $r$ strictly smaller coordinates and then apply exchangeability.
2. **Score monotonicity and comparison (3 points).** Proves that adding reference occurrences cannot increase the sum of the k smallest scores, then derives equality between full and practical test scores and the required inequality for every calibration score. Checks that the reference collections have at least k elements and retains multiplicities.
3. **Quantile comparison and set inclusion (2 points).** Uses coordinatewise monotonicity of the stated empirical quantile to show the full threshold is no larger than the leave-one-out threshold and establishes samplewise inclusion of the full prediction set in the practical set. The comparison also holds when both thresholds are infinite.
4. **Final marginal guarantee (2 points).** Transfers full-conformal coverage through set inclusion to conclude probability at least $1-\alpha$ under exchangeability, with the stated finite-sample and marginal interpretation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solver must derive the substantive comparison and coverage arguments used by their proof; merely naming conformal prediction or monotonicity is insufficient. A precise invocation of the standard full-conformal theorem is acceptable when its hypotheses and the applicable quantile convention are verified. Propagate a missing full-conformal justification only to the extent that the final coverage is unsupported.

Do not require independence, absence of ties, distinct observations, nonnegative scores, or conditional coverage. A proof that assumes these without justification has not proved the full statement unless it separately removes the restriction. Do not treat ranks as uniformly distributed without addressing ties. The case $\alpha<1/(n+1)$ has $q=+\infty$ and coverage one; a proof must handle that case explicitly or through a theorem that includes it. The constraints $1\le k<n$ already imply $n\ge2$.

The public quantile definition is authoritative. Do not replace its infinite endpoint by the maximum calibration score or impose an additional lower bound on alpha. The original source's capped endpoint is a documented local source error, repaired in the task and provenance; it is not an unresolved solver obligation.
