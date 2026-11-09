# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly formulate the fixed-coordinate Gaussian-mixture truncations, annealing path, score decomposition, and ELP interpolation/recursion. Work under the stated summability premises without adding hypotheses, and justify the finite-dimensional regularity and well-definedness needed by the chosen proof. The summability assumptions are premises; they need not be deduced from the componentwise finite-energy assumptions.
2. **3 points:** Construct an auxiliary diffusion with the annealing transport velocity and verify its marginals. Establish the correctly oriented path-space entropy comparison and terminal data processing. Evaluate both adapted drift functionals along the auxiliary path, including its previous mesh value. With J_d=(1/4)E integral ||Gamma^(-1/2)u||^2, a valid separated bound is 2J_d+(1/2)E integral ||Delta||^2. Derive the transport bound that produces the public coefficient 1/(8T), and justify localization and passage to full paths.
3. **3 points:** Derive the needed dimension-uniform auxiliary marginal moments, drift/increment estimates, and spatial and temporal freezing estimates from (A1)–(A7), including both affine and responsibility variations. A sufficient pair is C_sp(1+T+T^(-1))(t-s) for the spatial squared defect and C_tm(t-s)^2/T^2 for the temporal squared defect. Integrate them using sum h_n^2<=T h_max and sum h_n^3<=T^2 h_max. Merely naming regularity or citing the paper-specific lemma package is insufficient. Uniform moments of the ELP interpolation are not required by this proof.
4. **2 points:** Combine the transport and freezing bounds with constants independent of d, T, and the mesh. Use a numerical inequality such as 1+T+T^2<=(3/2)(1+T^2), rather than absorbing T into a T-independent constant. Bound finite annealing sums by the infinite summability bound, take the supremum over dimensions with the same horizon and mesh, and obtain the positive-tolerance consequence.

# Evaluator Notes

Accept a complete valid alternative proof and different intermediate estimates that establish the same public contract. Do not require the reference proof's incidental presentation choices. Treat an incorrect KL direction, evaluation of the entropy integrand under the wrong path law, omission of the auxiliary comparison, or failure to derive uniform freezing estimates as theorem-critical gaps. Finite moments alone do not establish Novikov's condition or uniform integrability of an unstopped stochastic exponential; a valid localized entropy argument is sufficient. Do not require use of the imported nonstandard continuous-time annealing theorem. Finite and countable mixtures, arbitrarily small or large positive T, and arbitrary finite deterministic meshes are included; no stability or small-step hypothesis may be added.
