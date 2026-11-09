# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Correctly derives, from the null conditional independence and auxiliary-uniform assumptions, that $Y_t\mid\mathcal G_{t-1}$ is Uniform$(0,1)$ and $Z_t\mid\mathcal G_{t-1}$ is Exp$(1)$.
- **3 points:** Computes the Exp$(1)$ conditional moment generating function for $\lambda\in(0,1)$ and proves that $(1-\lambda)e^{\lambda Z_t}$ has conditional mean at most one.
- **2 points:** Correctly multiplies the one-step factors, verifies adaptedness/nonnegativity and the e-process (supermartingale) property, and obtains the displayed formula for $M_t(\lambda)$.
- **1 point:** Applies Ville's inequality to establish the level-$\alpha$ crossing guarantee for the stated optional-stopping rule.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
