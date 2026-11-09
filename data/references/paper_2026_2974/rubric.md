# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Uses coordinate smoothness and the AdaGrad update to derive a valid descent inequality, introduces a predictable accumulator proxy with deterministic proof offsets, and exploits conditional unbiasedness. For the reference route, justifies the denominator-error estimate using conditional Holder and Young inequalities, without assuming finite second noise moments.
2. **3 points:** Correctly controls the normalized-gradient sums by logarithmic telescoping and bounds accumulator growth using the coordinate-wise p-moment assumption, norm comparison, smoothness, and the resulting \(\log K_T\) estimate. The proof must justify the expectations used; finite-horizon normalized updates provide the necessary gradient and objective bounds.
3. **3 points:** Performs the proof-specific coordinatewise offset balancing and closes the self-bounding inequalities, obtaining all four stated T-dependent terms with their correct p-dependent exponents. For the reference route, supplies an explicit offset choice, handles both the large- and small-coordinate-log cases, and treats zero-noise coordinates without undefined division. The auxiliary offsets may depend on unconditional expected energies but must not become random future-dependent proxy parameters or algorithm changes.
4. **2 points:** Converts accumulated coordinate energies to the average \(\ell_1\) gradient norm with the correct \(1/\sqrt T\) normalization and states the complete expected-rate bound, including parameter ranges and the \(p>4/3\) regime.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its auxiliary objects when a different rigorous argument establishes the same bound. In a proof following the reference route, an unproved offset/self-bounding closure is a theorem-critical gap, not a completed step. Omitting any of the four rate terms without proving an equivalent or stronger bound is also theorem-critical.

The source coefficient replacement \(2^{1/\bar p+3/2}\le4\) is an inequality; equality is not valid for general \(p<2\). A harmless equality typo is readily repairable when the argument only needs this valid upper bound. At \(p=2\), the positive-noise offset is simply \(c_i=s_i\). At \(s_i=0\), conditional noise moment zero implies exact gradients in that coordinate, so a zero offset is admissible by direct argument. Do not require a positive noise level, a positive initial gap, a bounded objective above, independent successive oracle draws, or a finite second noise moment.
