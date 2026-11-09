# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives a one-step composite objective-gap inequality from proximal optimality and convexity. In the reference route, the linearization remainder is bounded by $\langle s^{n+1}-s^n,x^{n+1}-x^n\rangle$, and weighted Young's inequality gives the squared-difference term with denominator $W_n$. An unsupported comparator-dependent inner product does not earn full credit for this step.
- **3 points:** Derives the adaptive cumulative estimate. In the reference route this includes telescoping the changing metric, proving or correctly applying the scalar cumulative-square-root estimate, and handling the lagged denominators by splitting $a_i^k/w_i^{k-1}$ into $a_i^k/w_i^k$ and the inverse-weight correction. The accumulation must include $s^1-s^0$, and the metric and Young terms must both be retained. Equivalent valid estimates receive full credit.
- **2 points:** Uses bounded subgradients, bounded iterates, and positive weights to obtain a cumulative bound $A+B\sqrt{N-1}$ with finite nonnegative constants independent of $N$. If the inverse-weight correction is bounded by telescoping, the factor arising from $\|s_i^k-s_i^{k-1}\|^2\le4G^2$ must be included. The displacement bound may depend on a fixed minimizer and the bounded trajectory.
- **2 points:** Applies convexity/Jensen averaging over $x^2,\ldots,x^N$, uses minimality for the lower bound, and proves both the displayed finite-horizon inequality and its $O(N^{-1/2})$ consequence.
- **1 point:** Maintains correct quantifiers, indices, domains, and parameter dependence. The argument must cover $N=2$ and zero gradient-difference accumulations and must not assume $x^1\in\operatorname{dom}g$, smoothness, finite-dimensional blocks, or a restriction on $\eta$ absent from the task.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its exact constants, or its particular inverse-weight decomposition when another argument closes the same obligations. Merely naming an adaptive-gradient argument or an internal summation proposition without establishing the applicable difference-adaptive bound is insufficient.

The proximal updates are well-defined under the stated assumptions and produce points in $\operatorname{dom}g$ from $x^2$ onward. A solver may invoke the standard proximal existence and optimality facts with their hypotheses checked; reproducing the reference proof's existence argument is not required. Standard convexity, Cauchy-Schwarz, Young's inequality, and finite Jensen averaging may also be used without separate proofs. The scalar summation estimate may be invoked as a standard result if its relevant statement and applicability are clear; otherwise it must be derived.

No proof obligation is being deferred to an unresolved paper-specific dependency. The reference proof explicitly closes the changing-metric and lagged-denominator estimates.
