# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** States the bounded-bias best-arm model, PAC guarantee, gap/parameter conditions, and identifies the relevant output events under the hard instance and alternatives.
- **3 points:** Constructs, for each suboptimal arm, an admissible paired environment changing its true mean and flipping bias by `2L`, and correctly shows the observed-mean separation is `Delta_m + epsilon - 2L` up to a positive perturbation.
- **2 points:** Applies a valid change-of-measure/testing inequality to derive the required trajectory-KL lower bound from the two PAC error probabilities.
- **2 points:** Derives the adaptive Gaussian KL as `E[N_m]` times squared mean separation over `2 sigma^2`, including the stopping/adaptive-sampling justification.
- **1 point:** Lets the perturbation vanish, sums over all suboptimal arms, and obtains the stated total expected-sample lower bound and order.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A theorem-critical failure to construct the opposite-bias alternatives, establish the KL/testing lower bound, or perform the per-arm summation is a major gap.
