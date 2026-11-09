# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly derives strict positivity of surprisal and uses the deterministic reward and baseline to prove \(\chi(y^*)>0>\chi(a)\) for every incorrect arm, uniformly over the allowed policy regimes.
- **3 points:** Correctly substitutes the symmetric probabilities into the additive priority and derives \(f_\alpha(y^*)-f_\alpha(a)=\alpha-(1-\alpha)L\), including cancellation of the baseline terms.
- **3 points:** Solves the ranking inequality with all sign cases: \(\alpha>L/(1+L)\) for \(L>0\), \(\alpha>0\) for \(L=0\), and every \(\alpha\in[0,1]\) for \(L<0\).
- **1 point:** Correctly translates the cases to \(p\gtrless 1/K\) and states the resulting contrast between regime-independent delight and regime-dependent additive tuning.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of either boundary case or an unjustified division by \(1+L\) as a substantive gap in the additive-ranking step.
