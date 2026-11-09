# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the supplied finite pairwise rates, hard minimum, positive allocation-independent weights, and weighted surrogate. Justifies, or correctly invokes, continuity on the compact simplex and existence of surrogate maximizers. No computation of the constrained projections is required.
- **3 points:** Derives the minimum-rate factorization and proves the two-sided bound on the normalized weighted sum, including challenger-dependent weights, or establishes an equivalent uniform estimate by another valid method.
- **2 points:** Uses the subexponential condition to conclude uniform convergence. The reference estimate is \(\sup_p|F_t(p)-m(p)|\le (L_t+\log(K-1))/t\); another valid bound tending to zero is equally acceptable.
- **3 points:** Shows that every choice of surrogate maximizers converges to the unique hard-minimum maximizer, using uniform approximation, compactness, continuity, and uniqueness, or a complete equivalent argument. The argument must apply as real \(t\to\infty\), for example by considering arbitrary sequences \(t_n\to\infty\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Naming log-sum-exp or argmax-consistency without deriving the required bounds and convergence earns credit only for the parts actually established.

The rates and their continuity are supplied by the task. Do not require a derivation of projection existence, projection uniqueness, an envelope identity, saddlepoint asymptotics, or the statistical large-deviation characterization. In particular, a solver can prove the result directly for the given continuous rate functions without expanding their divergence formula. If the divergence is expanded, its orientation is \(D_i(v;\theta_i)=A_i(\theta_i)-A_i(v)-A_i'(v)(\theta_i-v)\).

No positivity of allocation coordinates or pairwise rates is assumed. A proof must remain valid on the closed simplex and for \(K=2\); separate discussion of these cases is unnecessary if the displayed argument already covers them. Uniqueness of a surrogate maximizer is not required. Merely restating the setup is not a substitute for the proof steps, and omitting an unnecessary restatement must not reduce the score.
