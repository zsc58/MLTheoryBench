# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Private Proof Notation

For the reference route only, define

W := int_s^T P(t)^T K_SS(t)P(t) dt.

W is an auxiliary matrix constructed in the proof. It is not supplied by the public task, and solvers are not required to introduce it if they give a complete valid alternative proof.

# Core Steps

- **Step 1 (2 points):** Sets up the propagator and correctly derives both train and test displacement identities with the defined operators G and D. The identification g(t)=P(t)g(s) must be justified, for example by uniqueness for the continuous-coefficient linear ODE or by the direct B^{-1}-energy argument.
- **Step 2 (3 points):** For the reference route, introduces W, establishes its positive-semidefinite squared-norm representation, and proves ker(W) subset of ker(G) using K_QS=J_Q J_S^T. Merely naming reservoir invisibility earns no credit for this step. Credit an equivalent argument that directly establishes the needed annihilation of propagated directions without naming W.
- **Step 3 (3 points):** Derives D=B^{-1}(I-P(T)), establishes the B^{-1}-energy identity, and proves both inclusions needed for ker(D)=ker(W). Credit an equivalent direct energy argument proving ker(D) subset of ker(G) without constructing W. Do not require invertibility of D or W, or commutation of B with K_SS(t).
- **Step 4 (2 points):** Uses the established annihilation or kernel inclusion to justify G=GD^dagger D and concludes the exact finite-window train-test coupling, without a small-drift or asymptotic assumption.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's presentation, auxiliary notation, or division into steps; award full credit when an alternative proof closes the corresponding mathematical obligations.

Standard finite-dimensional Moore-Penrose identities may be invoked with their correct application. For example, after proving ker(D) subset of ker(G), the identity D(I-D^dagger D)=0 immediately yields G=GD^dagger D. A solver need not reprove the existence of the pseudoinverse or derive these standard identities from an SVD. In contrast, an unsupported assertion of the theorem-specific factorization, reservoir invisibility, or the needed energy relation is a proof gap.

All ranks, including zero rank, are allowed. Separate discussions of degenerate cases are unnecessary when the proof already covers them; imposing a nondegeneracy assumption absent from the public task leaves the proof incomplete.

The coefficient A_circ is the path-dependent operator defined in the task. Do not require or infer a predictor computable from training outputs alone, a coefficient shared across different trajectories, or uniqueness on the entire training-output space. The public task does not ask for dissipation-normalized channels, a normalized remainder, quantitative small-eigenvalue estimates, or statistical generalization bounds.
