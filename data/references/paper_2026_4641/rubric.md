# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Forward duplication invariant (3 points).** Defines the replication of scalars, vectors, and matrices and proves preservation through Avg, both scaled matrix multiplications, and OuterNonlin. The OuterNonlin argument must account for the k^r copies of each averaged r-tuple and its normalization, including r=0. Concludes equality of the scalar averaged readout whenever raw parameters are replicated.

2. **Backpropagation and gradient relations (3 points).** Derives the appropriate reverse or equivalent derivative invariant rather than merely citing automatic backpropagation. A normalized vector sensitivity d_v times its ordinary derivative replicates; the ordinary derivative scales inversely with its widening factor. Handles scalar dependencies, all OuterNonlin argument slots, and both matrix orientations. Obtains raw loss-gradient relations H_W^up=(k_out k_in)^(-1) Rep(H_W), H_u^up=k_u^(-1) Rep(H_u), and H_c^up=H_c. Includes the loss-chain coefficients and sums all occurrences of shared parameters. Correctly distinguishes G_A=n_in H_W for the single optimizer variable A=W/n_in, so G_A^up=k_out^(-1) Rep(G_A).

3. **Optimizer and decay scaling (3 points).** Uses joint degree-m homogeneity in the gradient history and auxiliary vector, together with the stated matrix/vector/scalar hyperparameters. Demonstrates both decay conventions explicitly or by an equally complete unified calculation. For matrices, applies coupled decay to A=W/n_in and converts the update back to W. The resulting raw coupled filter uses n_in n_out H_W,j+bar_lambda W_j; the decoupled raw update has factor 1-bar_gamma bar_lambda and filter history n_in n_out H_W,j. Gives the corresponding n_u H_u,j vector calculation and the unchanged scalar calculation. Shows that corresponding widened histories yield identical entrywise raw updates. Does not apply an additional optimizer independently to transpose occurrences or multiply the gradient step by the decoupled decay factor.

4. **Training-time conclusion (1 point).** Starts from the duplicated initialization and uses induction on the complete history through step t, not just the current gradient. Concludes raw-parameter replication after every update and hence equality of the functions for every input and training time.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental notation or presentation choices. A direct coordinate, symmetry, or differentiation argument may replace reverse-mode induction if it rigorously establishes the necessary individual-entry gradient relations, including shared matrices and scalar loss derivatives. Differentiating equality only on the replicated parameter subspace gives sums over replicated entries and does not, without an additional argument, establish equality of the individual gradient entries.

A proof omitting either decay mode, a parameter class that is present, or the necessary gradient normalization has a theorem-critical gap. A proof treating ordinary vector adjoints as unscaled replicated quantities is incorrect unless it explicitly uses normalized adjoints instead. A proof that adds coupled decay to a raw matrix while claiming to optimize W/n_in uses the wrong update rule.

Naming homogeneity or a tensor-program argument without deriving the corresponding invariant earns no credit for the relevant step. Joint scaling of epsilon must be included when auxiliary parameters are present. A complete calculation must remain meaningful when gradients or base hyperparameters vanish; division by such quantities requires separate treatment.

The supplied reference proof fully derives its obligations. No paper-specific external theorem or unproved automatic-backpropagation claim is an accepted substitute for a missing derivation.
