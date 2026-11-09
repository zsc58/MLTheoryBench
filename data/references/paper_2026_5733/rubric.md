# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Uses the explicitly assumed local $m_A$-strong convexity and $L_A$-smoothness in the same Euclidean coordinates as the iteration to obtain the one-step objective-error bound with factor $1-m_A/L_A$. The comparison value is $g_*=g_A(\bar U)=\widetilde g(0)$: the local-minimum hypothesis and strong convexity make this the minimum on the coordinate domain. The argument must respect the local domain and iterate-containment assumption.
- **2 points:** Iterates the one-step inequality for arbitrary $T\ge0$ and substitutes $K_A=L_A/m_A$ to obtain the stated contraction. The reasoning must remain valid when $K_A=1$ and use, or be consistent with, the declared convention at $T=0$.
- **4 points:** From $a/h_i\le d_i\le b/h_i$, derives $a\le d_ih_i\le b$, then $m_A\ge a$, $L_A\le b$, and $K_A\le b/a$. It must also correctly compare the contraction factors when $b/a\le K_0$.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A solution may invoke the standard strongly-convex smooth gradient-descent contraction directly after verifying its hypotheses, including the comparison minimizer and the applicability of the local assumptions along the iteration. The convex coordinate domain supplies the segments needed for the usual descent inequality. A separate proof of nondegeneracy is not required.

The Gram identity and aligned differential calculation correctly explain the spectral interpretation but are not separate public conclusions and are not required for full credit. The specified chart and its tangent-frame compatibility are assumptions defining the local optimization problem, not additional constructions a solver must prove exist.

Do not accept an argument that infers pullback-Hessian eigenvalues $d_ih_i$ solely from the ambient Hessian and the first differential. A constrained local minimum need not be an ambient critical point. The local pullback conditioning constants are an explicit assumption, and a correct solution may bypass the ambient-to-pullback Hessian calculation entirely. A theorem-critical failure to use the local conditioning or to justify applying it along the contained iteration is a major gap.

Do not require a separate discussion of an impossible aligned-frame instance in the square case. Do not penalize a solution merely for using the supplied zeroth-power convention without further commentary. No stochastic convergence theorem, clipped-SPD update analysis, or proof that a learning algorithm achieves inverse alignment is required.
