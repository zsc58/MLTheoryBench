# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Geometric simultaneous steering (3 points).** Constructs, or otherwise rigorously derives, smooth localized contraction and transport fields and proves that the reference flow sends each cell within a strictly smaller internal tolerance of its assigned target. Convexity must justify the contraction formula on the whole cell. The paths and moving supports need only be separated at equal times; do not require disjoint spatial path images. The argument must allow targets to coincide with other starting anchors. A finite-obstacle routing construction, including sequential motions through temporary positions, is valid.
2. **Quantitative field and trajectory control (2 points).** Establishes bounds sufficient for the stated width threshold, such as Lip_x(v_eta)<=L(1-log eta) and B(v_eta)<=B(1-log eta), with L and B fixed independently of eta. Defines the Fourier-Barron quantity if it is used and verifies its finiteness and tolerance dependence. The decomposition v_eta=lambda_eta U+W with fixed smooth compactly supported U,W and lambda_eta=O(1-log eta), together with the Fourier derivative estimate, is sufficient; exact geometric constants are not required. Proves a uniform bound for all reference trajectories starting in D_R, not just those starting in the cells, with no dependence on the cells in the final trajectory-bound constant.
3. **Finite-width semi-autonomous approximation (3 points).** States and correctly applies a valid uniform ReLU ridge approximation result on a fixed space-time cube, checks its hypotheses, and accounts for total vector-valued width and any affine overhead. Componentwise application with p>=3d and floor(p/d) units per component is one valid implementation. Derives the quantitative network error and the explicit width implication; merely naming a Barron method earns no credit for this step. In particular, the proof must explain how a bound A(1-log eta)eta^{-TL}/sqrt(p) becomes at most eta/2 under the advertised threshold with one fixed C.
4. **Flow transfer and final constants (2 points).** Uses a valid ODE stability estimate and, when approximation is only local, a first-exit or equivalent containment argument. The stability exponent may use the reference-field Lipschitz constant; no uniform bound on the approximating network's Lipschitz constant is necessary. Preserves strict inclusion in the open target balls and proves the uniform terminal-flow bound with M independent of the cells. Handles zero diameter and empty cells, including the all-empty and single-nonempty cases, without adding assumptions to the task.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Do not require the particular path scheduling, cutoff profiles, source theorem labels, or incidental constants of the reference proof. The public task imposes no nonempty-interior condition, no exclusion of input-target coincidences, and no parameter-norm restrictions.

A claim that arbitrary assigned endpoints admit disjoint spatial arc images is not a valid general justification: interchanged singleton targets already violate it. Equal-time noncollision is sufficient. Also, a non-strict distance estimate only gives a closed intermediate ball; strict final inclusion must follow from slack or a separate strict estimate.

A missing quantitative width derivation, an unsupported geometric routing assertion, circular trajectory containment, or a final M that depends on the cells is theorem-critical when it leaves a requested conclusion unsupported. Routine width padding, fixed dimension-dependent neuron overhead, and elementary degenerate cases are locally repairable when the rest of the proof supplies all required bounds. Propagate a failed dependency only when the final inclusions or bounded-flow conclusion are consequently unsupported.

The reference proof uses one stated standard independent scalar approximation theorem. All paper-specific steering, norm-growth, containment, and width-transfer obligations are derived; there is no unresolved private-reference obligation to treat as an established scoring step.
