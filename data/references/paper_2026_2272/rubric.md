# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly identifies both flows with the geometric family, deriving the tempered parameter equation \(\alpha_T'=\lambda-\alpha_T\), \(\alpha_T(0)=0\), and the standard parameter \(\alpha_S(t)=1-e^{-t}\). Establishes the representation from the normalized equation or gives an equivalent valid identification. Does not rely on cancelling a centered log-ratio when it can vanish identically.
- **4 points:** Derives \(\frac{d}{d\alpha}D(\rho_\alpha\|\pi)=-(1-\alpha)\operatorname{Var}_{\rho_\alpha}(\log(\mu_0/\pi))\) for \(0<\alpha<1\), with normalization, finite KL, differentiation, and centering justified. The source assumptions give finite first log-ratio moments; interior exponential tilting supplies the second moments needed for differentiation. Equivalent domination or convex-analysis arguments are acceptable.
- **2 points:** Establishes \(0\le\alpha_T(t)\le\alpha_S(t)<1\) for finite \(t>0\) from the schedule range and parameter formulas.
- **2 points:** Integrates to obtain the exact KL difference and the no-speedup conclusion. Handles a zero lower endpoint by a justified limiting argument or an equivalent absolutely-continuous formulation, and covers equal endpoints and \(t=0\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A missing or incorrect variance-derivative calculation is a theorem-critical gap.

Do not require finite variances at \(\alpha=0\) or \(\alpha=1\), a fourth-moment assumption, or finite endpoint KL derivatives. These do not follow from the assumptions and are not needed. In particular, finite second moments of the densities and a quadratic bound on the log-ratio do not establish its finite variance at an endpoint. A proof that relies on that inference needs correction; assess the remaining correct work under the scoring guide rather than treating endpoint variance finiteness as an additional task assumption.

For full credit, a proof must justify integration from zero when necessary. Continuity of KL at zero together with monotone convergence of the nonnegative variance integral suffices. No issue arises from an infinite integrand at a single endpoint or an empty integration interval.

Allow \(\mu_0=\pi\), zero schedules, and the constant schedule one. Strict inequality is not required. The source's schedule monotonicity is retained, although the comparison itself only uses the range \([0,1]\).

When deriving log-density equalities, include target normalization constants or explicitly work modulo spatially constant terms before normalizing. Omitting such terms in an asserted exact equality is incorrect; omitting them in a proportional-density formula is legitimate.
