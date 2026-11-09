# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly defines and analyzes the separated surrogate's row profiling, including existence and uniqueness of query minimizers and strict increase of \(F\) in its second cost.
- **3 points:** Proves the bounded cost-table counterexample: continuity supplies \(\delta\), Bayes selects row 1, while the profiled separated surrogate uniquely decodes row 2, establishing non-consistency.
- **2 points:** Recasts executed pairs as multiclass actions and derives the exact decomposition \(c_{i_\pi}=D+\sum_i(M-c_i)\mathbf1\{i_\pi\ne i\}\), then constructs the augmented weighted comp-sum surrogate.
- **2 points:** Establishes the weighted multiclass reduction for conditional and population risks, best-in-class risks, and minimizability gaps, explicitly handling \(W(x)=0\) and \(\alpha=0\).
- **1 point:** Applies the standard comp-sum H-consistency theorem under the required hypothesis-class conditions and obtains \(\widetilde\Gamma_\tau(u)=\alpha\Gamma_\tau(u/\alpha)\), including \(\Gamma_1(u)=\sqrt{2u}\).
