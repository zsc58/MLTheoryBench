# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points: Covariance estimation.** Uses the specified coordinate and pair estimators and the explicit radius. Derives the centered-product decomposition, a valid product-mgf bound, and scalar mean-error bounds under predictable adaptive sampling. Obtains the entrywise failure probability and accounts for the union over pairs. Conditioning on terminal counts must not be treated as making adaptively sampled data independent.
2. **3 points: Optimism confidence.** Establishes a summable failure bound sufficient for optimism at a fixed optimal action. The reference route uses the one-sided vector mu* vee overline mu, nonnegative covariance-axis realignment, geometric count peeling, a conditional exponential supermartingale, and a fully justified conversion of rectangular tails to a sum tail. An appropriate covering proof or valid alternative earns full credit. Merely citing a specialized covering lemma without its relevant statement and verified hypotheses does not close this step. Do not require the unverified sharper per-bin formula printed in the source.
3. **2 points: Regret decomposition and failure accounting.** Uses optimism and the confidence constraint to obtain true-covariance, pair-counter covariance-estimation, and inverse-coordinate-count contributions. Separately handles selected-action mean overestimation, for example by charging selected coordinates at distinct sample counts. Shows all remaining failure contributions are o(log T); finite constants may depend on the fixed instance. Does not assume unsupported simultaneous two-sided confidence for every action.
4. **2 points: Cumulative exploration.** Derives and applies a valid gap-weighted counter integral and l2 charging bound. Correctly handles exponents 1/2, 3/4, and 1; uses maximum active size m for coordinates and m^2 for ordered pairs; and obtains a bound of order delta(T)[log^2(m+1)S/Delta+log(m+1)n^2(Delta^-1/3+1+log(Delta_max/Delta))]. Equivalent bounds sufficient for the target receive full credit.
5. **1 point: Final asymptotics and domains.** Explicitly transforms the small-gap hypothesis to absorb the remaining terms, uses delta(T)/log T tending to 2, and obtains universal leading constants. Handles the all-zero-gap case separately and avoids undefined extrema for counters absent from all positive-gap actions. Empty actions and zero covariance must not create undefined expressions in the proof.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require incidental presentation choices, exact auxiliary constants, or the particular bin ratio of the reference proof. The public m is maximum action size, not the number of actions; the model and algorithm are in normalized units. The covariance radius is the displayed count-dependent formula, not an abstract least confidence radius. The reference proof contains complete derivations of its theorem-critical obligations and has no outstanding private-GT warning. Its local source corrections concern proof validity and do not authorize altering the public assumptions, algorithm, or target.
