# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes the quantile-negation identity `Q_{-Z}(1-u)=-Q_Z(u)` almost everywhere (or an equivalent generalized-inverse argument), including the role of continuity points.
- **2 points:** Uses the quantile definitions and the substitution `v=1-u` to derive `L_p(Z)=-U_{1-p}(-Z)` with the correct normalization.
- **3 points:** Establishes or validly invokes the Rockafellar-Uryasev superquantile representation for `-Z` at level `1-p`, with coefficient `1/p`, and explicitly handles the extended-real cases permitted by the task, such as an infinite hinge expectation or tail integral; then correctly negates the minimization.
- **3 points:** Performs the change of variable `eta=-a`, identifies `(-Z-a)_+=(eta-Z)_+`, and concludes the stated maximum over all real `eta` without changing assumptions or quantifiers.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award downstream points when conclusions are independently established, even if an earlier justification differs; theorem-critical missing transformations, an unverified variational formula in a permitted nonintegrable case, or an incorrect variational coefficient are major gaps.
