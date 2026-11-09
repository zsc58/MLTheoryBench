# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establish the exact stochastic-policy Bellman error representation. Justify the statewise max-difference convex combination, including coincident endpoints, and derive the deflated error update from the residual correction.
- **3 points:** Decompose into mean and transverse coordinates and rigorously derive the triangular switched system on the stated space, with $z_{k+1}=\bar A_{\mu_k}z_k$ and $a_{k+1}=\ell_{\mu_k}z_k$. Verify cancellation of the autonomous scalar term rather than assuming it.
- **3 points:** Prove the augmented-family JSR identity by a valid block upper-triangular argument or direct product computation; justify stochastic-policy convexification and its JSR invariance; and establish the projected bound, obtaining $\rho_{\rm def}=\bar\rho\le\gamma$. A quotient-norm argument or the source's projected-product argument is acceptable for the last inequality.
- **2 points:** Derive uniform projected product bounds, including the empty-product case needed at $k=1$, and use the scalar lifting estimate to prove the full-error bound with a constant independent of $Q_0$ and $k$. Deduce the limsup conclusion for every permitted $\beta$, including zero transverse error, $\bar\rho=0$, and the zero-dimensional transverse space.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. General standard linear-algebra or JSR results may be used when their relevant statements and applicable hypotheses are clear; merely naming the paper-specific representation or convergence theorem does not establish the corresponding core step. The enlarged switching family supplies uniform bounds and is not required to coincide with the set of switching sequences realized by the nonlinear iteration. Do not require mixing, irreducibility, a positive projected JSR, or strict improvement when $\bar\rho=\gamma$. A proof that handles $n=1$ and zero transverse error implicitly through valid formulas need not give separate case headings.
