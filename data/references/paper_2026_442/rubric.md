# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the two conditional score representations and concludes that every \(G_x^A\) has conditional mean \(\nabla\log m(x)\). Merely asserting unbiasedness without justification does not earn full credit.
- **4 points:** Reduces the integrated conditional variance to an \(A\)-dependent second moment and correctly computes the endpoint score moments, including the vanishing cross terms and
  \(M=(1-a)^{-1}F_q+a^{-1}F_p\). This is the central proof step.
- **2 points:** Derives and solves the matrix normal equation \(AM=a^{-1}F_p\), preserving matrix order and obtaining the stated formula for \(A^*\).
- **2 points:** Establishes global, unique minimality, for example by proving \(M\succ0\) from the Gaussian term and showing the objective difference is \(\operatorname{tr}((A-A^*)M(A-A^*)^\top)\).

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A direct computation from the independent generative variables is equivalent to a nested integration-by-parts computation. Do not award the moment-reduction points for merely naming integration by parts or a control-variate principle. If a claimed unbiasedness derivation is flawed but the common conditional mean is independently established, score subsequent valid optimization steps on their merits.

The explicit target-score second-moment assumption, positivity, and C¹ regularity suffice for the necessary analytic operations. For full rigor, a proof should account for square integrability and justify its differentiation and integration by parts. A concise justification using integrability of \(\nabla p\), bounded Gaussian kernel derivatives, and cutoff integration by parts is sufficient; the reference proof's detailed cutoff construction is not mandatory. Conditional Jensen justifies finiteness of the marginal score second moment, so the variance reduction does not subtract infinite quantities. These checks belong to the first two core steps, not a separate point category. Do not require a finite second moment of \(Y\), Lipschitz continuity of its score, strong convexity, or nonsingularity of \(F_p\); none is a hypothesis of the task. A merely omitted routine analytic justification is assessed under the existing 8–9 guidance, rather than treated as failure of the entire optimization argument.
