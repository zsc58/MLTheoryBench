# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly distinguishes the first-derivative playing distribution p from the second-derivative distribution q defining V_T; uses the pre-round projected cumulative regrets and the loss-range assumption; proves existence, uniqueness, and nonnegativity of the actual time equalizer, allowing zero increments.
2. **2 points:** Establishes the constant-potential invariant and the logarithmic bound on projected coordinates; provides a valid comparison between the actual projected update and a smooth unprojected update; verifies the initialization and burn-in conditions. The identity [x+r]_+=[ [x]_+ +r ]_+ must not be assumed in general.
3. **4 points:** Establishes the characteristic second-moment bottleneck, with enough detail to verify the final constant 2. For the reference route this includes the smooth log-potential's local Hessian control, the discretization estimate, the mixed space-time term, a noncircular crude estimate, and the refined bound Δt_j≤2∑_i q_{j,i}(Δx_{j,i})². The exact base-point expression is m−sU/S+s²D, not m+s²D. A valid bound on the mixed term is |U/S|≤3 sqrt(K/t)sqrt(m). Check the constants and hypotheses rather than accepting an unsupported appeal to self-concordance or to the paper's lemma.
4. **2 points:** Sums the actual time increments to obtain t_T≤t_0+2V_T and converts the potential invariant to the ceiling-ranked quantile bound with log((t_0+2V_T)/t_0). Handles nonpositive quantile regret, the endpoints of the epsilon range, and zero-increment cases.

# Evaluator Notes

Accept any complete valid alternative proof; the particular auxiliary increment, weighted norm, and intermediate constants in the reference proof are not mandatory. Award the bottleneck points for an alternative argument only if it actually proves the required q-weighted second-moment estimate or otherwise establishes the full target.

Do not accept replacing q by p, applying smooth third-derivative arguments to the clipped potential at zero without justification, bounding squared negative raw regrets by the positive-part potential, differentiating the pointwise gradient cancellation as if it held with the increment fixed in a neighborhood, or citing the source's uncorrected mixed-Hessian formula. These are mathematical defects, not presentation differences.

The public rank is ceil(Nε). There are at least ceil(Nε)≥Nε experts with regret at least that rank's value. An argument based on at most εN strict exceedances is not automatically the same order statistic at integer Nε. No specialized proof obligation is delegated to an unavailable reference, and there is no private GT quality warning.
