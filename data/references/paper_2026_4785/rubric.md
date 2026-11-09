# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive the universal lower bound \(\mathbb E_B[n_\tau]\ge\sum_x (R(x)/Z)\operatorname{cl}(x)\) by identifying the terminal marginal as \(R(x)/Z\), conditioning on the terminal state, and using that every directed walk to \(x\) has length at least \(\operatorname{cl}(x)\). The terminal marginal is that of the first reversed transition, with almost-sure termination following from the finite-moment assumption.
- **3 points:** Construct or otherwise justify existence of a single reward-matching backward policy that follows predecessors decreasing \(\operatorname{cl}\) by one, stops at \(s_0\), has finite expected length, and attains the lower bound. The construction must not require a parent at \(s_0\), including when \(s_0\) is itself terminal.
- **3 points:** Prove necessity: any positive probability on a trajectory longer than the shortest distance for its terminal state yields a strictly larger expectation, so such a policy cannot minimize.
- **1 point:** Prove sufficiency: support exclusively on shortest trajectories makes every conditional mean equal to \(\operatorname{cl}(x)\), hence attains the lower bound and is minimizing; state the resulting if-and-only-if conclusion clearly.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The finite-moment assumption concerns the unconditioned reversed walk, with infinite length on nontermination; it is not a conditional moment given termination. A solver may use the immediate consequence of almost-sure termination without reproducing the full stopped-path normalization argument. The absorption time includes the initial reversed transition out of \(s_f\), whereas \(n_\tau\) excludes the final forward transition into \(s_f\).

Repeated states are permitted in trajectories. The initial state may itself be terminal, in which case the direct trajectory \(s_0\to s_f\) has length zero. Neither strict positivity on all graph edges nor any restriction on the policy at states never visited is required. All terminal rewards are strictly positive, so terminal conditioning is well-defined.

Treat omission of an explicit absorbing-boundary convention, an isolated indexing slip, or a readily repairable boundary-case omission as a minor issue when the main argument is otherwise correct. A missing strictness argument or unattained lower-bound construction is theorem-critical. Do not require forward-policy, flow, or training results.
