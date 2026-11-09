# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly derives the per-kernel chronological affine recurrence, including the decay factor, the immediately preceding event contribution, and the initial zero state. Does not access an undefined predecessor event at the first item.
2. **3 points:** Uses affine-to-linear augmentation or an equivalent direct affine-composition argument to derive a compressed scalar-vector product. Proves closure, associativity with the correct chronological multiplication order, and O(M) combine cost and storage. Identifies a valid identity/initial transition.
3. **3 points:** Shows that the ordered prefix scan yields every exact state and uses those states to compute all event intensities and the full Hawkes log-likelihood. Includes the compensator integral and correctly treats zero marked intensities under the extended-real convention.
4. **2 points:** Gives the qualified resource analysis: O(KM(N/P+L_N)) scan time for L_N=max{1,log_2 N}, the original O(KM(N/P+log N)) form for N≥2, reduction to O(KMN/P) in the stated dominance regime, and O(KMN) unbatched compressed-state memory. Accounts for initialization and does not claim unlimited speedup for a singleton input. Any claim that the full likelihood computation fits the same time bound must also justify its auxiliary computations.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. In particular, direct composition of affine maps can earn full Step 2 credit without displaying augmented matrices. A method name without deriving the Hawkes-specific transition representation earns no credit for Step 2. Propagate a missing recurrence or invalid transition algebra to later steps when it leaves exactness unsupported; independently correct complexity accounting may still receive Step 4 credit.

A precisely stated standard work-efficient ordered-scan result may be used once associativity, product order, item cost, and its other relevant hypotheses have been verified. Do not require the reference proof's particular tree implementation. Non-power-of-two lengths and singleton inputs may be handled by standard identity padding and a separate base case.

Treat O(KM(ceil(N/P)+log N)), O(KM(N/P+1+log N)), and O(KM(N/P+L_N)) as equivalent uniform bounds. A proof may state the ordinary-log bound for N≥2 and treat N=1 separately. Do not accept a uniform O(KM/P) initialization-and-evaluation claim at N=1 with arbitrarily large P. Do not require pointwise computations or reductions over K and M to have span independent of those dimensions; a valid event-parallel schedule with O(KM) work per event suffices.

The memory target is compressed-state storage, not the dense input parameter tensor. Correctly noting additional O(KM^2) input storage must not be penalized. Do not require stationarity, strictly positive base rates, or strictly positive marked intensities. When a marked intensity is zero, the correct likelihood is -infinity, while the finite compensator remains well defined.
