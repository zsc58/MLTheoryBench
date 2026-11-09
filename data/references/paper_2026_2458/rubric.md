# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly derives the integrated-data representation from \(\bar X=A\tilde X+B\tilde U\) and the rank condition, including \(\bar XG=A-BK\) and the stabilizing equivalence.
- **2 points:** Establishes that the data Lyapunov equation is exactly the model Lyapunov equation for the induced gain and that evaluation is well-defined.
- **3 points:** Solves the constrained Hamiltonian minimization, proves that its induced gain is uniquely \(R^{-1}B^TP\), and handles the nonunique \(G\) representations (including the specified minimum-norm choice).
- **3 points:** Correctly identifies the iterates with Kleinman policy iteration and derives invariance of stability, monotonicity/value convergence, convergence of gains to the CARE-optimal feedback, and convergence of the selected representation matrices.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A named standard Kleinman result receives credit only when its hypotheses are verified and its consequences are correctly applied; merely naming a method without the data-to-model equivalence earns no credit for the central steps.
