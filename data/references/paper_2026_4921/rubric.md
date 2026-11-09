# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly establishes availability of admissible projections using full column rank. The orthogonal-complement argument for each latent index is sufficient. Equivalent work within a complete direct construction also earns these points; a separately stated upstream lemma is not mandatory.
- **4 points:** Establishes that, outside a Lebesgue-null set of full-column-rank measurement matrices, $p$ admissible projections can be selected with invertible squared-coordinate matrix. For the witness-and-polynomial route, this requires an invertible witness, a valid passage to a nonzero polynomial controlling exceptional measurement matrices, and simultaneous verification of orthogonality and nonzero target gains. One witness-compatible chart with its null complement handled is sufficient; a finite-chart argument is also acceptable if its nontriviality claims are justified. Other complete valid methods receive equivalent credit.
- **2 points:** Derives the projected interventional-variance equations $q=T_2\sigma^2$ using the measurement model, independence in the relevant intervention regime, the common diagonal noise covariance, and the known finite targeted variances. Interventions may target additional coordinates.
- **2 points:** Uses invertibility of $T_2$ to conclude unique recovery of all measurement-noise variances and the unique least-squares minimizer. Explains that the exact population solution is nonnegative, so the unconstrained and nonnegative-domain conclusions agree.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Do not require the witness, target assignment, chart parameterization, or polynomial construction to match the reference proof.

A joint polynomial zero set in measurement entries and free parameters being null does not alone establish that its projection onto measurement-matrix space is null. A proof must justify the required conclusion about measurement matrices, for example by fixing witness free coordinates, using a nonzero coefficient polynomial, or giving a valid fiber argument. Likewise, a witness on one minor chart does not by itself establish polynomial nontriviality on all other charts. A single chart is sufficient when its complement is separately controlled.

Orthogonality alone does not establish admissibility: the selected target gain must also be nonzero. A simultaneous polynomial-avoidance argument, a justified perturbation argument, or another complete verification is acceptable.

The proof must cover $d=1$ and $p=d$; a uniform construction with correct empty-matrix conventions suffices without separate case proofs. Known targeted variances and measurement-noise variances may be zero. Do not require finite moments of latent coordinates whose contributions are annihilated by the projections.

This is an existence and exact-population identification task. Do not require a proof that a particular thresholded random-sampling algorithm terminates, any finite-sample accuracy guarantee, or recovery for every full-column-rank measurement matrix. Do not award full genericity credit for merely naming genericity or invoking a witness without the necessary measure-zero argument.
