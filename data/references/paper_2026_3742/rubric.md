# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Expresses posterior odds through weighted empirical profile losses and correctly compares them with population constrained losses; controls empirical errors almost surely using finite-variance iterated-logarithm bounds, including unpulled and zero-variance arms.
- **3 points:** Proves sufficient optimal-arm posterior mass and pull growth, obtains the two-coordinate quadratic separation, and rigorously converts summable posterior bounds above a logarithmic threshold into the universal pathwise upper counts and regret bound.
- **3 points:** For each feasible raised-mean alternative, establishes a non-summable posterior lower bound below threshold and rigorously converts it into a matching pathwise lower count; applies this to every arm in the unconstrained case.
- **2 points:** Uses the immediate neighbor of the optimum on the same side as each distant arm to establish the unimodal quadratic bound, proves distant-arm counts are sublogarithmic, and obtains the neighbor-only regret constant.

# Evaluator Notes

Accept any complete valid alternative proof. No sub-Gaussian assumption is available or needed. The initial uniform draw can sample an arm with an empty optimizer hypothesis once; it cannot sample that arm again. The one-arm case has zero regret. A lower-count argument must justify its pathwise probability conversion rather than apply a conditional bound on an event not known at the conditioning time.
