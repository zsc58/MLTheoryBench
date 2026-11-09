# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omissions.
- **10:** Fully correct.

# Core Steps

- **4 points:** Starting from the architectural inequality, correctly squares it and applies both \((r+s)^2\le 2r^2+2s^2\) and Cauchy-Schwarz across the \(L\) layers to obtain the pointwise bound with constants \(2C^2L\) and \(2\eta^2\).
- **2 points:** Takes expectation under the stipulated joint law, correctly identifies the layerwise squared-discrepancy expectation as \(J(a_\star)\), and uses \(J(a_\star)\le\gamma\) to establish both asserted normal-energy bounds.
- **3 points:** Uses the almost-sure lower bound on \(\|D_{a_\star}\|^2\), together with \(\delta>0\), to bound the normalized fraction and then its expectation by \((2C^2L\gamma+2\eta^2)/c_{\min}\).
- **1 point:** Identifies the last quantity as \(\rho^2\) and, using \(\rho\in[0,1)\), invokes the stated definition to conclude that \(a_\star\) is \(\rho\)-proximal.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Merely naming Cauchy-Schwarz or asserting that the loss controls normal energy does not earn the corresponding points unless the constants and expectation are derived. If the normal-energy bound is independently established despite an error in its proposed derivation, score subsequent valid normalization reasoning on its own merits.
