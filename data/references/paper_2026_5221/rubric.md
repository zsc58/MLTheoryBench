# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly expresses the order-averaged autoregressive objective as a sum of per-position expected conditional log-likelihoods and converts that sum into an expectation over a uniformly sampled position.
- **4 points:** Establishes the central permutation-combinatorial fact: at a fixed position, the revealed prefix is uniform over subsets of the corresponding size, and the next index is uniform over the complement conditional on that subset.
- **3 points:** Uses the conditional uniformity to derive the exact factor `d/(d-K)` and the sum over all indices outside the sampled context, thereby proving the stated expectation identity or an equivalent unbiased-estimator formulation.
- **1 point:** Correctly concludes from the construction that the mask law is independent of the values of `x` and hence gives the claimed MCAR-style interpretation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A claim of uniform masking without a valid derivation of the prefix-subset and conditional-next-index laws does not earn the central 4 points. An argument that treats a fixed-size uniform mask as uniform over all subsets is incorrect, though it may still receive credit for correctly established portions.

A direct counting or coefficient-matching argument can earn full credit without introducing the reference proof's auxiliary position variable or separately naming the two conditional laws, provided it establishes the equivalent probabilities and the exact identity. Equal one-coordinate inclusion probabilities alone do not establish a uniform subset law or independence of the complete mask from data values.

The data vector and model parameters are fixed during objective evaluation. Random masks are sampled by the stated value-independent procedure. The claim concerns the averaged conditional log-likelihood, not the logarithm of the permutation-mixture likelihood. Neither independence between mask coordinates nor unbiased gradients nor a generalization guarantee for imputation is part of the task.

The argument must cover the stated range, including `d=1`, the empty context, and contexts of size `d-1`. A formula or counting argument that already covers these cases needs no separate case split. All denominators are positive because `K` never equals `d`.

# Private Source-Repair Notes

The source's expanded objective at L000036 and step decomposition at L000055 omit, respectively, the full permutation probability and the prefix probability; L000036 also misplaces parameter subscripts. The repaired source records are `theory_001` and `theory_002`. The correct full-order expansion weights each permutation by `p(z)`. The correct per-step expansion first averages over the prefix distribution and then over the next index conditional on that prefix. These repairs are fixed by the expectation definition, the prefix factorization at L000062, and the context sampling at L000068; they leave the final estimator unchanged.

Do not credit an unweighted sum over prefixes as the expected per-position contribution. Conversely, do not penalize a solution for using the public task's correctly normalized objective rather than reproducing the erroneous source displays. Solvers are not required to identify or discuss these private source errors, and no additional scoring obligation is introduced by their repair.
