# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Approximation and ERM baseline (2 points).** Uses the stipulated comparator in the bounded class, the distinction between the l1 uniform approximation norm and the Euclidean temporal L2 loss, and ERM minimality to derive the empirical bound T epsilon_app^2. Correctly identifies the individual bounded-loss scale T q B_loss^2. The specialized external approximation theorem need not be proved: comparator existence is an explicit premise.

2. **Temporal-output empirical-process reduction (3 points).** Derives the squared-loss Lipschitz constant 2 sqrt(Tq) B_loss in coefficient space and applies a correctly stated vector-contraction result with its hypotheses verified. Establishes the centered sub-Gaussian coefficient increments, their empirical temporal L2 metric, and the radius/diameter bounds, or supplies an equivalent valid empirical-process argument. Finite temporal projections followed by a justified uniform limit are fully acceptable. Merely naming contraction, Parseval, or sub-Gaussianity without checking their application is insufficient.

3. **ODE/readout parameter entropy control (3 points).** Establishes the vector-field and layer Lipschitz bounds, state bounds, and parameter-perturbation bounds through Gronwall and layer telescoping. Controls all readout parameters, including biases, with readout width factors. Constructs a cover whose centers satisfy the output restriction and whose count includes integer rounding or an additive one. Derives the entropy bound with sufficient numerical control to imply the requested constant. Retains the factor (w_max^h_Pi B_max^h_Pi+1) in Delta. Finite-sum arguments, or explicit case handling, must avoid excluding layer Lipschitz constants zero or one. A claim that a grid and Dudley 'give the constant' without the required estimates leaves a major gap.

4. **Final PAC substitution (2 points).** Applies the uniform empirical-Rademacher inequality to the fixed measurable bounded-loss class under iid sampling, invokes the ERM baseline on the resulting event, and verifies the numerical and dimensional comparisons leading to the displayed bound for every delta in (0,1). The argument should apply to every ERM on that event, or otherwise justify any estimator measurability it uses.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's basis, order of estimates, loose intermediate constants, or particular chaining presentation. A stronger bound that demonstrably implies the requested bound earns full credit. Standard independent theorems may be invoked when their relevant statements and hypotheses are clear; re-proving vector contraction or the generalization inequality is not required.

The central entropy/ODE perturbation argument is theorem-critical. The corrected reference proof supplies it explicitly and has no unresolved GT obligation. Do not accept the unrounded source grid count, arbitrary off-class grid centers, or a change from readout widths to vector-field widths. Do not require an unjustified assumption B_max>=1. The corrected task includes zero parameter bounds and the cases H=1 and layer Lipschitz constant one. Minor endpoint or measurability omissions should be judged according to whether they admit an immediate local repair, rather than automatically receiving a major-gap score.
