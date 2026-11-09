# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly localizes crossing edges for the window matrix, bounds their total weight by \(w\), and uses the two query-side volume lower bounds to derive \(\phi_G(T_t)\le w/\min\{t,n-t\}\).
- **3 points:** For the uniform matrix, correctly identifies the crossing edges and derives both \(w_G(T_t,T_t^c)=t(H_n-H_t)\) and \(\operatorname{vol}(T_t)=t(2+H_n-H_t)\), including the required harmonic-sum calculation.
- **4 points:** Proves the \(1/5\) uniform lower bound by handling both possible volume orderings. In particular, the proof must justify the harmonic lower bounds and establish the complement-side inequality when \(T_t\) has the larger volume; merely asserting a uniform conductance result is insufficient.
- **1 point:** Correctly combines the two estimates into the stated temporal-cut contrast, including the balanced-cut consequence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
