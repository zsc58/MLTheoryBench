# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs the balanced hidden-good-arm prior and threshold profile; verifies the exploration parameters under the actual `C>=1` premise and horizon condition; proves constant threshold-crossing probability for every good arm by perturbation, prefix measurability, and a valid localized change of measure; and controls false positives from regret. With the reference constants, `E[FP]<=beta K/4`, not `beta K/8`.
- **2 points:** Converts false-positive and false-negative control into the quantitative information lower bound using the uniform-subset entropy and binary coordinate-error inequalities. Justifies the conditional-entropy chain, concavity, and use of binary entropy on `[0,1/2]`, retaining the finite subtraction `(1/2)log_2(2K)`.
- **2 points:** Reconstructs all batch boundaries and committed actions from the seed and boundary-memory transcript under the stated current-time/state/seed model. Uses seed independence and conditional data processing to prove `I(S*;Y)<=(B-1)W<=BW`, and derives the displayed converse, including its parameter domain and vacuous or nonpositive-bound cases.
- **2 points:** Supplies a complete executable static-grid construction and proves both its per-round `O(S log T)` retained-memory bound and its `O((K/S)(log log T)^2)` batch bound. Accounts for integer sample lengths, the deterministic round budget and final batch, and data-independent block cardinalities. The finite-bit implementation must work for arbitrary `[0,1]` rewards; storing unrestricted real empirical means as exact words is insufficient without an implementation argument.
- **2 points:** Establishes simultaneous accuracy with valid conditioning for adaptively selected fresh samples, including any finite-precision error. Proves best-arm survival, incumbent monotonicity, the end-of-iteration incumbent gap, and the later-slot challenger gap, or valid substitutes. Bounds refresh, actual-challenger, filler, and final-exploitation regret, handling initial slots separately. Includes the failure event in expectation: probability at most `T^-2` and regret at most `T` give contribution at most `T^-1`. The guarantee must be uniform over all bounded reward distributions.

# Evaluator Notes

Accept any complete valid alternative proof under the repaired public assumptions. Do not require the reference construction, its constants, its quantization rule, or its incidental presentation choices. A different finite-precision implementation or a different complete algorithm is acceptable if its information access, memory, batch count, and regret are proved.

The source's construction, schedule identities, concentration-event invariants, and regret decomposition are not admissible unproved black boxes merely because they are named. Likewise, phrases such as 'the source parameter conditions hold', 'use the prescribed threshold', or 'the schedule identities give the result' do not discharge their corresponding obligations without sufficient definitions and derivations.

Distinguish a harmless constant-factor arithmetic error from a missing argument. In particular, do not require the erroneous `beta/8` false-positive contribution or a `T^-2` expected failure contribution. A derivation of the valid weaker quantities above is fully correct. An upper-bound proof restricted to Bernoulli rewards does not prove the public upper claim unless it supplies a valid reduction for arbitrary bounded reward laws. Theorem-critical omissions in either direction remain major.
