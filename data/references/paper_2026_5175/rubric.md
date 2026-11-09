# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Defines the fixed loss-good set and correctly applies the zero-observation bound separately to the target-backward and forward samples, including the joint \(1-2\alpha\) confidence statement.
- **3 points:** Derives from the good-set log-ratio inequalities both a lower bound on the normalizer ratio and the resulting upper bound on \(p(\tau)/q(\tau)\) on the good set. Merely asserting a likelihood-ratio bound without this derivation earns at most partial credit.
- **3 points:** Uses a valid good/bad-set decomposition of trajectory total variation to obtain \(\operatorname{TV}(p,q)\le e^{2c}-1+\varepsilon+\eta\), and substitutes the two sampled mass bounds. A deterministic argument that divides by \(1-\varepsilon\) must justify \(\varepsilon<1\) or handle \(\varepsilon=1\) separately. Under the observed all-good event, \(m\ge1\) and positivity of \(q\) already imply that \(G\) is nonempty and \(\varepsilon<1\); a proof using this fact needs no separate impossible-case analysis.
- **2 points:** Correctly identifies the terminal marginal of \(q\) as \(\rho\) and proves contraction of total variation under terminal marginalization, completing the stated bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The confidence claim must be interpreted as an implication holding outside a probability-\(2\alpha\) exceptional event; it is not a conditional-probability assertion obtained by conditioning on the observed all-good event.

Zero losses and \(c=0\) are allowed. No equality between \(A\) and \(A_*\) may be assumed. A proof must not assume that \(\log(1/\alpha)/m\) or \(\log(1/\alpha)/n\) is below one without treating the complementary, possibly trivial regime. The confidence statement remains valid, although noninformative, when \(2\alpha\ge1\). A genuinely omitted elementary boundary justification is a minor omission only when the remaining proof is correct; do not penalize a proof for omitting a case it has already excluded.
