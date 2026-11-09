# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes normalization and the local mixture bounds, together with the required optimizer relations. Correctly handles V_n=0, the zero interior optimizer, and boundary optimizers. Arguments using the prior at the optimizer must not evaluate q(0).
- **3 points:** Derives all four stated finite-time regret regimes with their required conditions and constants. In the moderate regime, justifies the optimizer control and both possibilities in the local interval length, including equality at |S_n|=bV_n/5. Uses the actual prior normalization or a valid weaker lower bound. Merely asserting a generic mixture-regret estimate is insufficient.
- **2 points:** Establishes an appropriate hindsight-wealth lower bound and uses it with the finite-time bounds to derive deterministic constants uniform over n and all paths in E_alpha. Handles small and zero variance using the defined Lambda_2 and Lambda_3. Applies Ville's inequality to the process initialized at F_0=1, including the first supermartingale transition.
- **2 points:** Excludes infinitely many actual high-deviation branch indices on a bounded-wealth, diverging-variance path. Derives S_n/V_n->0 and the upper-LIL constant 1 without circularity, and then establishes eventual regret at most ln ln(V_n)(1+o(1)). Justifies the almost-sure conclusion under the stated supermartingale and variance assumptions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its particular intermediate inequalities.

The large-regime constant is ln4+ln ln(6.6e)+ln ln ln(6.6e)+2ln(2c+5/b). If L=ln ln(6.6e), its two middle terms are L+ln L, not ln L+ln ln L.

At a nonzero boundary optimizer, the exact value is |a|q(a)=L/[2ln(6.6e)L^2]. Replacing 2 by 4 is a valid lower bound but not an equality. Either the exact value or the weaker bound may be used.

Do not require iid data or conditional mean p: the probabilistic hypothesis is the initialized mixture-supermartingale property. A proof may use standard Ville's inequality after verifying this initialization and the applicable hypotheses.

All theorem-critical obligations are closed in the replacement reference proof; there is no outstanding private dependency or proof-completeness warning.
