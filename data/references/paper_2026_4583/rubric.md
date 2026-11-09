# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Inexact-oracle descent (3 points):** Handles eta=0 separately or otherwise avoids dividing by zero. For eta>0, correctly uses oracle feasibility, strong convexity, smoothness, and the stepsize restriction to derive a quantified one-step inequality controlling ||f_{t+1}-f_t||^2 by objective decrease plus eta epsilon_t. The coefficient m/(4 eta), or a valid stronger coefficient, suffices.
2. **Telescoping sublinear guarantee (2 points):** Sums the descent inequality, uses V>=0, and derives the explicit average and minimum successive-gap bounds. Under summable oracle errors, establishes their O(T^{-1/2}) rates and proves individual gaps tend to zero by square-summability or another valid argument. A vanishing average alone does not prove individual-gap convergence.
3. **Prediction-dependent projector contraction (4 points):** In the separate exact squared-loss regime with 0<eta<=1, derives residual monotonicity and a correct consecutive-update identity, or an equivalent quantitative argument. With r_t=y-f_t, A_t=A(f_t), and delta_t=f_{t+1}-f_t, a valid identity is delta_{t+1}=(1-eta)delta_t+eta(A_{t+1}-A_t)r_{t+1}. Equivalently, the perturbation term can be written eta(A_{t+1}-A_t)(I-eta A_t)r_t. Combines these facts with the assumed Lipschitz bound to obtain the stated kappa and recurrence.
4. **Geometric conclusion (1 point):** Correctly iterates the recurrence when kappa<1, establishes geometric decay of the gaps, and obtains geometric convergence of f_t by summing the gap bounds. Includes kappa=0, where the sequence is constant from f_1 onward.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Award downstream points only to the extent that the claimed bounds are actually established; a named method without its quantitative derivation does not earn the corresponding step.

The identity delta_{t+1}=(1-eta)delta_t+eta(A_{t+1}-A_t)r_t is generally false. Do not accept it as an exact projector identity merely because it leads to the desired numerical bound; the residual index or the omitted factor must be corrected, or a valid alternative derivation supplied.

The O(T^{-1/2}) assertion concerns the average and minimum over the first T gaps. Do not require an individual-gap O(t^{-1/2}) rate. The individual-gap conclusion in the general regime is convergence to zero.

Do not impose eta<=m/(2L) on the independent exact squared-loss contraction argument. Its stipulated range is 0<eta<=1. No full-rank assumption, spectral lower bound on B, or continuity of A away from the trajectory is required.
