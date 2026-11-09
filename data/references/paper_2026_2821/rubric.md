# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Correctly uses the Gaussian kernel's characteristic/universal property to infer equality of the transported independent coupling and the Bayesian joint coupling from zero MMD.
- **Step 2 (3 points):** Derives the product-test identity for bounded continuous state and observation functions, correctly using the triangular form of $T$ and the two coupling disintegrations.
- **Step 3 (3 points):** Shows that equality against all observation test functions implies equality, for each state test in a determining class, of the corresponding conditional expectations almost surely; handles the common full-measure set (or an equivalent measure-theoretic argument).
- **Step 4 (2 points):** Uses a countable measure-determining class, or an equivalent valid conditional-measure uniqueness argument, to conclude $T_x(\cdot,y)\#\pi_x=\pi_{x\mid y}(\cdot\mid y)$ for $\pi_y$-almost every $y$, stating the exact conditional transport conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award no credit for merely naming MMD, universality, or disintegration without carrying out the corresponding identification argument. Minor null-set or regularity presentation differences are readily repairable when the conditional measure conclusion is otherwise established.

The explicitly assumed characteristic property is sufficient for Step 1; a separate proof of Gaussian characteristicness is not required. Do not require or endorse uniform density of the Gaussian RKHS in all bounded continuous functions on the noncompact Euclidean domain. A valid universality argument must use an appropriate determining function space or otherwise correctly establish measure identification.

In the transported conditional expectation, the observation is held fixed: the relevant expression is $\int f(T_x(x,y))\,\pi_x(dx)$. Independence does not justify replacing it by an unconditional expectation averaging over the observation. An alternative proof using rectangle tests and uniqueness of disintegration may receive full credit without reproducing the continuous-test construction. The reference proof's explicit rational-rectangle approximations are one way, not a required way, to obtain a common full-measure set.
