# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the foundational gap/contact facts needed by the proof, including the contact identity \(\Lambda_n\Delta_n=\alpha_n\log n\). In the reference approach this includes the normalized gap representation and the Laplace-transform formula for the partition function. A valid alternative approach may supply equivalent foundations without using that integral formula.
- **3 points:** Proves \(D_n(\beta_n)\to0\) whenever \(\beta_n/\Lambda_n\to0\), with estimates valid uniformly when \(\alpha_n\) tends to zero. In the reference approach this follows from the contact-count lower bound on \(Z_n\) and a uniform bound on \((\alpha_n\log n)e^{-\alpha_n\log n/2}\).
- **3 points:** Proves \(H_n(\beta_n)\to0\) whenever \(\beta_n/\Lambda_n\to\infty\). In the reference approach this requires both \(Z_n\to1\) and control of the derivative/mean-gap term; \(Z_n\to1\) alone is not a sufficient entropy argument when the number of coordinates grows. A valid alternative direct entropy estimate earns the same credit.
- **2 points:** Correctly derives the necessary exponent matching \(\xi_\beta=\xi_\Lambda\) for schedules avoiding both collapses and the contact-coordinate relation \(\xi_\Lambda=\xi_\alpha-\xi_\Delta+1\), including existence of the third exponent for each of the three choices of two known exponents. Uses bounded-ratio comparisons consistently.

# Evaluator Notes

Accept a complete valid alternative proof. Neither the Laplace-transform representation nor differentiation of a partition function is mandatory when another argument proves all the stated conclusions. A bare invocation of a named method without the needed estimates is insufficient.

All accumulation/contact definitions are imposed on the finite-scale tail. Finitely many arbitrary positive extensions do not affect any limiting claim. Finiteness excludes maximum ties on that tail, but the theorem does not assume that the contact count diverges, that \(\alpha_n\) has a positive lower bound independent of \(n\), or that the score rows admit a particular attention/Gram realization.

The exponent-selection conclusion is necessary only: do not demand proof that matching exponents is sufficient to avoid both collapses. A logarithmic growth exponent means \(\asymp\), not a ratio tending to one. The inverse-temperature exponent convention in that conclusion is \(\xi_\beta\ge0\); the contact-coordinate exponents may be negative.

The reference supercritical estimate is explicitly justified by
\[
0\le-\beta Z_n'(\beta)
\le\left(\frac{\beta}{\beta-\Lambda_n}\right)^2-1
\qquad(\beta>\Lambda_n).
\]
Equivalent valid estimates are acceptable. No unresolved reference-proof obligation remains.
