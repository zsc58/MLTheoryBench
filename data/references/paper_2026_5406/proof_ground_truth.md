# Reference Proof

## Proof Structure

Expand a generic product `Q_mu K_nu^T` using the coupled real-component projection equations. Insert these expansions into the four Hamilton score components and collect coefficients, showing that every coefficient belongs to `U`. Then expand the shared real score, identify its coefficients, and prove that they belong to the same subspace. Verify that all constructed coefficients depend only on the weights, so that the same constructions work for every input.

## Complete Proof

Fix the dimensions and the two weight matrices `W_Q,W_K`. The matrices `Phi_{mu beta}`, `Psi_{nu gamma}`, and the subspace `U` are then fixed independently of `X`. Let `X` be an arbitrary compatible input.

For every `mu,nu` in `{0,1,2,3}`, the projection equations give

`Q_mu K_nu^T = (sum_beta X_beta Phi_{mu beta})(sum_gamma X_gamma Psi_{nu gamma})^T`

and hence, by distributivity,

`Q_mu K_nu^T = sum_{beta,gamma} X_beta [Phi_{mu beta} Psi_{nu gamma}^T] X_gamma^T`.

All dimensions are compatible: `Phi_{mu beta} Psi_{nu gamma}^T` is a real `d_in x d_in` matrix, so each summand is `T x T`.

Substitute this identity into the definitions of the four component scores and collect the coefficient of each pair `(beta,gamma)`. Define

`Lambda_0^{beta gamma} = Phi_{0 beta}Psi_{0 gamma}^T - Phi_{1 beta}Psi_{1 gamma}^T - Phi_{2 beta}Psi_{2 gamma}^T - Phi_{3 beta}Psi_{3 gamma}^T`,

`Lambda_1^{beta gamma} = Phi_{0 beta}Psi_{1 gamma}^T + Phi_{1 beta}Psi_{0 gamma}^T + Phi_{2 beta}Psi_{3 gamma}^T - Phi_{3 beta}Psi_{2 gamma}^T`,

`Lambda_2^{beta gamma} = Phi_{0 beta}Psi_{2 gamma}^T - Phi_{1 beta}Psi_{3 gamma}^T + Phi_{2 beta}Psi_{0 gamma}^T + Phi_{3 beta}Psi_{1 gamma}^T`,

`Lambda_3^{beta gamma} = Phi_{0 beta}Psi_{3 gamma}^T + Phi_{1 beta}Psi_{2 gamma}^T - Phi_{2 beta}Psi_{1 gamma}^T + Phi_{3 beta}Psi_{0 gamma}^T`.

Finite rearrangement then yields, for every `alpha`,

`C_alpha = sum_{beta,gamma} X_beta Lambda_alpha^{beta gamma} X_gamma^T`.

Every summand occurring in each `Lambda_alpha^{beta gamma}` has the form `Phi_{mu beta}Psi_{nu gamma}^T`, which is a generator of `U`. Because `U` is a linear span, every signed sum above lies in `U`. Thus

`Lambda_alpha^{beta gamma} in U`

for all indices.

For the shared score, the real quaternion inner-product identity gives directly

`R = Q_0K_0^T + Q_1K_1^T + Q_2K_2^T + Q_3K_3^T`.

Applying the generic product expansion to these four terms and collecting by `(beta,gamma)` gives

`R = sum_{beta,gamma} X_beta M^{beta gamma} X_gamma^T`,

where

`M^{beta gamma} = sum_{mu=0}^3 Phi_{mu beta}Psi_{mu gamma}^T`.

Each summand defining `M^{beta gamma}` is again a generator of `U`; hence `M^{beta gamma} in U` for every `beta,gamma`.

The displayed definitions of both coefficient families use only `Phi` and `Psi`, which are determined solely by `W_Q,W_K`. They do not depend on `X`. Since the input was arbitrary, these same coefficient matrices establish all the decompositions simultaneously for every compatible input.

Therefore all four Hamilton component scores and the shared real score have bilinear decompositions whose coefficient matrices lie in the same projection-induced subspace `U`. In particular, replacing the four component scores by the shared score introduces no coefficient interaction outside that subspace, as claimed.
