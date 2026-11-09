# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Correctly uses the paired phase/sign randomizer and its unit-modulus entries, and gives the conjugacy argument showing that a real input produces a real surrogate.
2. **3 points:** Starting from the zero-mean DGWSS input and its diagonal spectral covariance, uses independence to derive covariance preservation, verifies that the surrogate has zero mean, and concludes DGWSS closure.
3. **4 points:** For an arbitrary fixed observed real signal, verifies that the surrogate has zero mean, computes its randomized spectral covariance, and proves all off-diagonal expectations vanish. The argument must cover independent signs, phases from distinct pairs, mixed cases, and conjugate-pair phases, either explicitly or through a complete equivalent argument.
4. **1 point:** States the resulting diagonal spectral covariance and correctly concludes that every observed-signal surrogate is DGWSS, while preserving covariance in the DGWSS-input case. Finite second moments must be respected; their preservation here follows immediately from the fixed linear maps and unit-modulus randomizer and does not require a separate lengthy estimate.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A proof that merely names phase randomization or stationarity without deriving the covariance expectations does not earn the corresponding core-step credit.

Covariance is centered in this task, and DGWSS includes zero mean. To identify a computed second moment with covariance, the proof must establish zero mean or provide an equivalent centered-covariance calculation. A readily repairable omission of this verification should be assessed under the 8-9 band when the remaining proof is complete; it must not be treated as verification of a different, uncentered definition.

No Gaussianity, orthogonality of the eigenbasis, invertibility of the graph shift, practical norm normalization, or realization-wise energy preservation is required. The fixed observed vector need not itself have zero mean or be a realization of a DGWSS input. The zero vector, zero spectral powers, and absent categories of eigenvalue indices are included; do not require separate case splits when the argument already covers them.
