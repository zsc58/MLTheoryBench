# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly identifies the constituent successor kernels and switching-suffix laws, respecting the prescribed initial action, initial phase, and post-transition switch timing. Establishes the geometric-series representation or an equivalent valid probabilistic representation, with sufficient justification of convergence and kernel domains.
2. **3 points:** Derives the phase-wise switching Bellman equation and resolves the current phase correctly, obtaining the current-phase coefficient \((1-\gamma)/(1-\beta_k)\) and continuation coefficient \((\gamma-\beta_k)/(1-\beta_k)\). The continuation must explicitly or unambiguously include action averaging under the next policy. Operators must act on the correct state or state-action domains; a state-indexed operator cannot be applied directly to a state-action-indexed kernel without the requisite conversion.
3. **3 points:** Carries out backward induction over the suffixes, evaluating each suffix at the actual intermediate state-action pair. Correctly composes the constituent kernels, propagates continuation factors, and derives the exact product weights \(w_k\) for every phase.
4. **2 points:** Concludes equality of successor measures for arbitrary prescribed initial \((s,a)\), including the absorbing final phase, \(n=1\), and switching probabilities 0 or 1. All denominators and compositions are well-defined, and no theorem-critical gaps remain.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its use of a resolvent; for an alternative method, award the corresponding points for establishing the same mathematical obligations.

Compact kernel notation is acceptable when its domains and next-policy action averaging are clear. Treat a genuine domain mismatch or omission of that averaging as a mathematical error, rather than accepting an asserted continuation identity without justification. Endpoint cases need not be discussed separately when the proof visibly includes them without division by a switching probability or conditioning on an unreachable phase. Do not require any external policy-composition or flow-model convergence theorem.
