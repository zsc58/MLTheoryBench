# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derive (or otherwise establish) that, under no-cancellation, the off-diagonal precision support is exactly the moralized skeleton, and correctly transport this statement under permutations.
- **3 points:** Prove the exact-factorization bridge: combine the two masked feasibility equations, the support mask identity, and IC(0)-admissibility to obtain \(\Omega_\pi=L_\pi L_\pi^T\) for every candidate ordering, with the Cholesky uniqueness conclusion.
- **3 points:** Establish MEC soundness by showing feasibility of the reverse-topological reference ordering, applying ReSP optimality, and using the strict SMR inequality to rule out every minimizer whose induced DAG lies outside the true MEC.
- **2 points:** Establish robustness for arbitrary candidate orderings by using the factor support constraint and the precision-support/moralized-skeleton identification to prove induced-edge containment.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that invokes the precision-support characterization must state its hypotheses and verify that no-cancellation supplies them; merely naming a specialized result without connecting it to the mask is insufficient. Propagate an error in the support characterization to the robustness step, but score an independently valid exact-factorization and SMR argument on its own merits.
