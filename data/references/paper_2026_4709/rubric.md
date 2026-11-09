# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives support exclusion on $O$ from the actual zero-loss equation. The argument must justify that $Z_\nabla>0$ before inferring zero forward probability from a zero numerator; positivity may be established elsewhere in the proof using nonempty $U$. It then obtains zero terminal probability on $O$.
- **3 points:** For each $x\in U$, derives $Z_\nabla p_F^\nabla(\tau)=R(x)^\beta p_B^\nabla(\tau\mid x)$ from zero loss, sums over all paths to $x$, and justifies normalization of the backward path law to obtain $Z_\nabla p_{\mathrm{top}}^\nabla(x)=R(x)^\beta$.
- **3 points:** Justifies normalization of the forward terminal marginal and uses it with support exclusion to derive $Z_\nabla=\sum_{y\in U}R(y)^\beta$. Recognizes that this sum is finite and strictly positive.
- **2 points:** States the complete normalized distribution, including both the $R(x)^\beta$ law on $U$ and zero mass on $O$.

# Evaluator Notes

Accept a complete valid alternative proof and any valid ordering of the steps. Do not require the reference proof's incidental presentation choices. A concise explanation that locally normalized policies terminate on the finite acyclic graph suffices to justify the path-law normalizations; explicit recurrence formulas are not mandatory.

The allocation indicator is inside the logarithm. Replacing the loss by the square of a logarithm plus an indicator outside that logarithm changes the problem. The balance and support-exclusion equations are consequences to be derived, not additional assumptions supplied by the task.

Treat failure to establish either support exclusion on $O$ or the path-summed balance on $U$ as a theorem-critical gap. Backward probabilities are products starting at the specified terminal $x$ and exclude any transition from the auxiliary sink. The proof must cover $O=\varnothing$ without conditioning on that empty event. No separate optimizer-existence, optimization-convergence, full-forward-support, or converse theorem is required.
