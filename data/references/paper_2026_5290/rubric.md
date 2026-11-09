# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Uses the independent true Jacobian rows and the sampled support-witness condition to show that every witness-matrix row indexed by \(I_i\) is supported inside \(\widehat I_i\). Merely asserting a support relation without the spanning argument is insufficient.
- **2 points:** Obtains one permutation from invertibility of the inverse reparameterization and combines it with the support-pattern equality to prove \(\pi(I_i)\subseteq\widehat I_i\) for all \(i\).
- **2 points:** Correctly combines the row-wise cardinality inequalities with the global sparsity inequality to prove exact equality \(\widehat I_i=\pi(I_i)\) for every task.
- **3 points:** Derives the cross-block derivative zeros, justifies local factorization on a suitable coordinate neighborhood, forms the appropriate block-triangular inverse Jacobian, proves its diagonal task block invertible, and concludes the locally invertible within-task map with no complementary-coordinate dependence.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, a solver may use the weaker neighborhood-support consequence of the stated sampled-support hypothesis; deriving that consequence does not require equality between pointwise and neighborhood supports.

The conclusion concerning subgroup maps is local on coordinate neighborhoods; do not require an unjustified global inverse. A correct local argument may use a sufficiently small rectangular box to infer coordinate independence from vanishing partial derivatives. Do not require the row-span witnesses to persist after shrinking that box: the support restrictions have already been established on the original working neighborhoods.

A proof must not assume independence among latent coordinates. It must not assume that \(M\) is invertible or that \(M\) equals the inverse Jacobian entrywise. Neither componentwise recovery within each task subgroup nor vanishing of the opposite off-diagonal Jacobian block is required.

Empty task supports and full-coordinate task supports may be handled explicitly or through correct standard empty-block conventions. Do not deduct solely because a proof uses those conventions rather than a separate case split. The same permutation must work for every task, including when task supports overlap.
