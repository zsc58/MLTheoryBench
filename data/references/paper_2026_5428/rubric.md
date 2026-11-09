# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points: Interval inequality and large-update control.** Correctly derives an interval regret upper bound for an arbitrary layer active throughout the interval. Establishes the comparator's intervalwise feasibility, accounts for normalized active predictions and comparator smoothing, and justifies the potential estimate for the actual initialization. In particular, the initial center need not exceed the coordinate floor; a valid logarithmic bound or equivalent treatment is required. Handles both 32γ_j|e_t(i)|≤1 and its complement, shows how the correction cancels the quadratic stability terms, and charges the large-update residual to the signed recorded penalty. The common quadratic coefficient after combining the cases must be sufficient for the large-update case. Merely invoking mirror descent or 'standard stability' without establishing this paper-specific mechanism earns no credit for the missing portion.
- **2 points: Global bookkeeping.** Correctly telescopes the layer-mass boundary terms over consecutive intervals and proves that initialization contributes O(1/T). Uses the last active round to bound each terminal signed penalty from above, including all K inactive coordinates, giving a total upper bound O(log T). Tracks the aggregate floor remainder, for example O(Slog(KMT)/T²+1/T), rather than asserting a K-uniform O(1) remainder without justification. Shows its absorption in the relevant conclusions, here or in the rate-selection steps.
- **2 points: Worst-case guarantee and horizon boundaries.** For T≥4, selects an always-active geometric-grid rate within a constant factor of min{1/32,sqrt(log(KMT)/Q_s)} and correctly optimizes the interval expression to obtain O(log(KT)+sqrt(log(KT)Q_s)). Handles Q_s=0. Covers T=2,3 without assuming a nonexistent grid rate below 1/32, for example by proving the learner remains defined and applying the bounded-loss upper bound. Establishes feasibility throughout the horizon, here or elsewhere, and sums to the first claimed bound.
- **2 points: Benign guarantee.** Uses the assumed active rate with fixed uniform comparison constants to remove the per-interval logarithmic cost while retaining the shared O(log T) penalty. Recognizes that the finite-rate premise cannot hold when Q_s=0 under the stated convention. Justifies absorption of any logarithmic floor remainder uniformly in K; for the reference remainder, the premise and maximum grid rate imply sqrt(log(KMT)Q_s) is at least a fixed constant times log(KMT)/T. Correctly obtains the second claimed upper bound, including short horizons.

# Evaluator Notes

Accept any complete valid alternative proof under exactly the stated assumptions. Do not require the reference proof's notation, constants, or incidental presentation choices. A correctly stated standard three-point mirror inequality may be invoked when its hypotheses, including use of a positive center outside the current feasible set, are verified. The paper-specific stability and safeguard arguments must still be established.

Both targets are one-sided regret upper bounds. Regret against an arbitrary comparator may be negative; neither the task nor the proof requires an absolute-value regret bound. Likewise, terminal penalties need only be bounded from above, and negative increments or reactivation before a layer's last active round are allowed.

Do not accept modifications of the prescribed initialization, rate grid, or algorithm, a restriction to T≥4, a growth restriction on K, or stronger activity hypotheses as substitutes for proving the stated task. A readily repairable omitted finite-horizon case can qualify for the 8-9 range when the rest of the proof is complete; it does not justify marking the target false.

A failed interval inequality generally leaves both final bounds unsupported. If that inequality is independently established despite an error in its attempted derivation, award the later bookkeeping and rate-optimization achievements according to what is actually proved. Award each achievement only once even when its argument is placed in a different section. No unresolved reference-proof obligation is being treated as a completed scoring step.
