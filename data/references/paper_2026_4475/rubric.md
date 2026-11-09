# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derives the ridge-centered linear dynamics and row-space spectral contraction, then correctly controls the nonzero-teacher empirical residual to obtain the stated training threshold. Keeps the half-normalized empirical loss consistent with the objective. Establishes the initialization norm event and retains or validly bounds the residual cross term; a direct citation of a zero-teacher loss bound does not establish this step.
- **3 points:** Identifies the null-space dynamics and, conditional on the data, uses independent isotropic Gaussian initialization in an orthonormal basis of a kernel of dimension k=m-rank(Phi)>=m-n. Proves the concentration bound and obtains the full stated delayed interval. Checks that the lower bound on parameter error is nonnegative before squaring it. No full-row-rank assumption may be added.
- **2 points:** Proves convergence to the unique ridge minimizer under the step-size assumptions and proves the ridge norm and empirical-loss bounds with the correct minimizing inequality. A direct spectral proof or a correctly justified optimization result is acceptable.
- **2 points:** Establishes bounded-class uniform convergence with the stated sample-size dependence, checking the loss bound, Lipschitz constant, predictor complexity, and applicability to the data-dependent minimizer. Obtains the population comparison with 2Lhat, supplies strict limiting slack or another valid argument for the eventual 3epsilon bound, and combines probabilities correctly.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or particular universal constants. All constants must be universal and chosen consistently.

The empirical loss is half the empirical mean squared error, while population loss is the full mean squared error. Thus the ordinary empirical squared loss in the uniform-convergence inequality is 2Lhat.

The probability assertion is a high-probability implication on the original independent sampling experiment. It is not a conditional probability assertion obtained by conditioning the data distribution on the empirical hypotheses. Iteration indices are nonnegative integers; negative real training thresholds cause no difficulty. A zero empirical matrix is outside the sample-dependent antecedent, and rank-deficient nonzero matrices are included.

Treat omission of the null-space persistence mechanism or of the uniform-convergence transfer as theorem-critical gaps. An invocation of a paper-specific result is not itself a derivation. Standard concentration and uniform-convergence results may be cited in a relevant precise form with their hypotheses checked.

Do not accept the inference that convergence to a limit at most 3epsilon alone implies eventual loss at most 3epsilon. The small-regularization assumption supplies strict slack, so this issue is locally repairable when the preceding estimates are correct.
