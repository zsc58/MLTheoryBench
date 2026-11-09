# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes the residual-demand invariant for each item type, including integrality and nonnegativity of the residual, and uses it to prove demand balance with the final unmet-demand variable. Handles zero demand and an empty eligible set.
- **3 points:** Proves per-location inventory feasibility and carrier eligibility, accounts for zero coordinates at unvisited locations, and correctly invokes product separability to obtain feasibility of the full multi-item decision.
- **2 points:** Derives the decoder-only runtime by accounting for logical initialization and sparse output recording, eligibility and score computation, sorting, the allocation scan, and all carrier maximization scans. Includes the universal-eligibility specialization and respects the constant-size convention.
- **2 points:** Uses feasibility of the fixed decoded decision in the stated stochastic feasible set to prove that its conditional objective under the same evaluation law is no smaller than the program optimum. Respects the distinction between simulated decoder inputs and actual evaluation uncertainty.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A runtime claim that includes an unaccounted score-generation or neural-forward-pass cost does not establish the decoder-only bound. A proof that literally initializes or writes every entry of a dense location-carrier array must account for that additional cost; the task instead specifies a zero-default sparse output. Unit-cost arithmetic is stipulated, so bit complexity need not be analyzed.

A feasibility argument that omits either demand balance or per-location capacity constraints is incomplete. Constraint separability does not imply objective separability, and no such assertion is needed. Carrier maximization is only over nonempty eligible sets; empty networks are handled without an empty-set softmax or maximization.

The policy-value expectation holds the realized decoder inputs fixed and integrates the actual uncertainty law given the context. Do not accept a proof that treats the evaluated future realization as information available to the decoder or replaces the objective by its training-scenario average. The inequality is a feasible-point comparison, not a claim that the decoder is optimal.

The recourse formulation uses nonnegative real variables and does not require a total-unimodularity argument. Its existence follows from the feasible choice v=0,w=D and compactness. The first-stage feasible set is finite and nonempty. These well-definedness observations may be brief or implicit in an otherwise correct argument; do not turn them into unrelated additional theorem requirements. Nonnegative extended conditional expectations are permitted.
