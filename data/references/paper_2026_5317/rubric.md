# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points: Energy identity and bounds.** Correctly differentiates the metric kinetic energy along the stated dynamics, including the metric-dependent terms, and obtains $\dot E=-2\lambda K^{3/2}$. Deduces $0\le K(t)\le E(t)\le E(t_0)$ and the corresponding integrated identity. Merely asserting dissipation without deriving or otherwise justifying this identity does not earn full credit.
- **3 points: Hitting-time estimate.** Before the first time $K\le\varepsilon$, lower-bounds the cubic dissipation integral by $\varepsilon^{3/2}(s-t_0)$, handles the case $K(t_0)\le\varepsilon$, rules out an infinite hitting time, and obtains the stated constant.
- **4 points: Arc-length estimate and limiting energy.** Uses $K\le E(t_0)$ to upper-bound the cubic integral by $E(t_0)\int\sqrt K$, identifies $\sqrt2\int\sqrt K$ with graph-manifold arc length, and uses state convergence to identify the limiting energy difference as $K(t_0)+c(F(x(t_0))-F(z_\infty))$. The division-free conclusion must cover $E(t_0)=0$.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Do not require the reference proof's incidental notation or ordering. A later step may receive credit if its needed conclusion is independently established, even when an earlier attempted derivation is flawed. Missing the energy identity, the conversion to arc length, or the limiting-energy identification is theorem-critical rather than a stylistic omission.
