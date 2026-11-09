# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly handles the audit model and quantifiers: the same labeling-independent randomized history rule may inspect either pool and repeat inspections, terminates almost surely, and reports using observed information. The cost counts distinct excluded items only. Validity and zero-miss success hold for every applicable complete labeling, while the lower bound and infimum are evaluated under an arbitrary fixed complete zero-miss labeling.
2. **4 points:** Establishes the planted-subset coupling for an arbitrary allowed adaptive randomized audit, keeping included-pool labels unchanged. Shows identical trajectories when the planted subset avoids the zero-miss run's distinct excluded inspected set; bounds intersection probability by $mT/N_0$; averages over planted subsets and uses validity to derive $\mathbb E_0[T]\ge(1-\beta-\delta)N_0/m$.
3. **2 points:** Constructs the uniform without-replacement zero-count audit with $n_0=\lceil N_0(1-\delta^{1/m})\rceil$, specifies a non-certifying report on a nonzero count, and proves validity and certain zero-miss success. Justifies the zero-count probability bound, including cases where avoiding all relevant items is impossible, and verifies that the sample size is feasible.
4. **2 points:** Accounts for the ceiling and proves the requested explicit upper bound $n_0\le(1+\log(1/\delta))N_0/m$. Combines it with the converse to bound the infimum and conclude the $\Theta(N_0/m)$ rate, with positive constants depending only on $\beta,\delta$ and not on the fixed zero-miss labeling.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A missing coupling or unjustified validity bound is theorem-critical. A lower-bound argument restricted to excluded-only audits does not establish the full claim unless it also justifies reduction from the allowed two-pool model. Do not replace the pointwise zero-miss expectation by an unstated average or supremum over labelings. Repeated inspections must not be charged as new distinct excluded items. The theorem requires the explicit displayed finite-sample inequalities, not merely an unspecified asymptotic upper constant.
