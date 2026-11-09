# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Constructs a normalized snapshot latent-variable model with the prescribed decoder and a parameter-independent latent law, and proves the marginal bound with a finite parameter-independent constant. The variational argument must handle conditional-support restrictions correctly, or use a valid alternative argument. Justifies constant finiteness on the data support.
- **3 points:** Proves both snapshot and path expected-NLL decompositions into conditional entropy plus expected KL calibration error, treating them correctly as extended-real identities and handling zero predictor probabilities and null posterior coordinates.
- **2 points:** Correctly forms the loss-gap identity only in the cases where the subtraction is defined, including either one-sided infinite case, and proves the nonnegative conditional-entropy gap by data processing or an equivalent conditional-entropy argument.
- **2 points:** Uses KL nonnegativity and representability to prove posterior calibration of every global snapshot-risk minimizer, including the finite-risk justification and the almost-sure equality conclusion.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its exact formula for the constant, or a particular choice of latent prior if the constructed model meets the task and the bound is proved.

An importance-ratio expectation under the conditional snapshot law need not equal the entire model marginal. Restricting the model integral to the conditional support gives a sufficient inequality. Do not require the invalid equality, and do not penalize a solver for correcting it.

The path loss in this task is the expected NLL for predicting the clean token from the stated path observation. It is not the separate reverse-jump training objective; no reverse-jump calibration claim is required.

Do not penalize a solver for explicitly stating the necessary finite-risk qualification. No loss-gap identity is required when both losses are infinite, and exact posterior calibration is required only under the stated representability assumption.
