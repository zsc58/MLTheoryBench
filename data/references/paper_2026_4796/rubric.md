# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly partitions the selected calibration scores into $m$ safe exchangeable scores and $n-m$ arbitrary contaminated scores, and sets up the relevant order-statistic index.
2. **3 points:** Proves the deterministic order-statistic comparison showing that contaminated scores can reduce the threshold by at most $n-m$ ranks. Handles the nonpositive shifted index and the appended-infinity case; the reasoning also covers $m=0$.
3. **3 points:** Applies or proves the tie-safe exchangeable rank inequality for the unsorted safe scores and the test score, and derives $1-\alpha-g(\delta,n)$ with $g(\delta,n)=\delta n/((1-\delta)n+1)$. If using the intermediate bound $1-(n+1)\alpha/(m+1)$, the correct additional loss is $\alpha(n-m)/(m+1)$, not $(1-\alpha)(n-m)/(m+1)$. Identifies the residual event with interval coverage.
4. **2 points:** Establishes corrected-level coverage for a valid upper bound in $[\delta,1]$, using monotonicity of $g$ and the whole-line interval for a nonpositive corrected level. Covers a possibly random upper bound by a valid argument, such as containment of the fixed-level interval based on $\delta$ itself.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The standard rank inequality may be invoked with its exchangeability hypothesis and tie-safe formulation; reproducing the counting proof is not mandatory. Do not require independent safe scores, continuous score distributions, or independence of contaminated scores from safe scores or the test score.

Do not infer selected-score exchangeability merely from exchangeability of a larger unselected safe pool. It is an explicit assumption of this task. The result is marginal coverage under that assumption, not a new conditional-coverage or arbitrary post-selection theorem.

A random upper bound must dominate contamination almost surely. An expectation bound or an unspecified high-confidence estimate does not satisfy that requirement. Merely substituting a random level into a fixed-level coverage inequality leaves a gap unless justified by an additional valid argument. No independence assumption on the valid upper bound is needed.

A negative numerical coverage lower bound is harmless. The cases $m=0$, $m=n$, and an infinite conformal threshold belong to the task and must be covered, either explicitly or by an argument that clearly includes them.
