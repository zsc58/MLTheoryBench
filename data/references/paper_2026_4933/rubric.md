# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formalizes the exact CI-only oracle setting, essential-graph parameter, and adaptive worst-case objective. Recognizes that correctness is required over all DAGs on V and that s is not a promised input restriction.
- **3 points:** Correctly counts the 2^s-s-1 conditioning subsets, selects an unqueried W, and constructs a valid representative DAG and deleted-edge alternative. The replacement reference uses a complete clique of size s and isolated remaining vertices, for which it explicitly verifies arbitrary orderings remain in the same MEC. A proof using a general input instead must justify extension of its clique order to the whole MEC.
- **3 points:** Establishes query-answer agreement for all allowed set-valued queries. In the reference family, the only nonadjacent clique pair is u,v; direct active-path analysis shows that it is separated exactly when C∩S=W, and analysis of the endpoint sets extends this to arbitrary queries. A complete general disagreement argument or another valid indistinguishability argument is equally acceptable.
- **2 points:** Verifies admissible Markov and faithful realizations, completes the adaptive indistinguishability argument, and obtains the exact numerical and asymptotic bounds. Handles the zero-bound cases and exact randomized procedures consistently with the public contract.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or the source's stronger assertion for every fixed ground-truth DAG. The public target is a worst-case lower bound, so a hard family with a distinguished input of each required parameter value suffices.

The alternative MEC is not required to have the same clique parameter as the distinguished input. A proof must not rely on a promise that the unknown graph has a supplied value of s.

Queries may have set-valued endpoints. A proof restricted to singleton endpoints must additionally establish that its indistinguishability argument covers all allowed queries.

The three findings against the previous reference were valid proof-completeness concerns. The replacement closes all obligations needed for the public target: its special-case clique extension is explicit, its query-disagreement argument is derived directly, and Section 8 supplies faithful realizations. Do not require a solver using this hard family to prove the unnecessary general clique-extension or general edge-deletion statements.

Conversely, merely naming the specialized external edge-deletion lemma does not establish it. A proof that relies on the general statement must supply a derivation or a legitimately audited justification. The replacement's special-case proof must not be treated as certification of that general statement.

The faithful-realization construction uses finite Gaussian coefficient families. It verifies positive definiteness and factorization, gives explicit nonzero conditional-covariance witnesses for every graphical dependence, and avoids finitely many polynomial zero sets. Auxiliary witnesses may have zero edge coefficients: they serve to prove that a polynomial is not identically zero, whereas the final chosen distribution must have all required dependencies. Equivalent valid realization arguments are acceptable.

A standard-independent result may close an obligation when its relevant statement is supplied or unambiguously identified and its hypotheses are verified. No particular realization construction is mandatory.

For exact randomized algorithms, a sound proof can intersect the probability-one correctness events for the fixed finite hard family and then fix a seed. It must not infer simultaneous correctness over alternative inputs merely from correctness on one input.

The exact expression is zero for s=0 and s=1. The notation 2^{Omega(s)} is asymptotic in growing s, rather than a positive lower bound at those endpoints. The task does not request a bounded-error randomized lower bound.
