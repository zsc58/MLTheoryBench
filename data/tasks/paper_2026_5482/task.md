# Problem

## Setup

Let `d>=1` and `N>=2` be integers, and let `ell_1,...,ell_N:R^d->R` be fixed twice-differentiable losses. Let `Gamma` be a fixed symmetric positive-definite `d`-by-`d` matrix and set `R(theta)=1/2 theta^T Gamma theta`. Fix `theta_hat in R^d` satisfying
`N^{-1} sum_{n=1}^N grad ell_n(theta_hat)+N^{-1}Gamma theta_hat=0`.

Define `g_n=grad ell_n(theta_hat)`, `J_n=grad^2 ell_n(theta_hat)`, `J=N^{-1}sum_n J_n`, and `H-hat=J+Gamma/N`.

Fix an integer minibatch size `B` with `1<=B<=N`. At each step let `S_t=(I_{t1},...,I_{tB})`. In the with-replacement scheme, its entries are independent uniform draws from `{1,...,N}`. In the without-replacement scheme, it is uniform over all ordered `B`-tuples of distinct indices. Minibatches are drawn independently at different steps and independently of the pre-update state and the past. Every sum over `S_t` counts all `B` entries, including repeated indices in the with-replacement scheme. Define
`G_t(theta)=B^{-1}sum_{b=1}^B[g_{I_{tb}}+J_{I_{tb}}(theta-theta_hat)]+N^{-1}Gamma theta`.

For a fixed symmetric positive-definite step matrix `Lambda` and `beta in (0,infinity]`, run
`psi_t=psi_{t-1}-Lambda G_t(psi_{t-1})+sqrt(2 beta^{-1}Lambda) xi_{t-1}`,
where `beta^{-1}=0` when `beta=infinity`, the matrix square root is the symmetric positive-semidefinite square root, and the `xi_t` are independent standard Gaussian vectors in `R^d`. The Gaussian innovations are independent of the minibatches and the initial state, and each fresh minibatch is independent of the initial state and preceding innovations.

Assume this affine chain has a stationary distribution with finite second moment and that `Lambda H-hat` is invertible. Fix any such stationary distribution and let `Sigma_psi` be its covariance. For a pre-update state with this stationary distribution, let `C-bar_psi` be the stationary expectation of the conditional covariance, given that state, of
`B^{-1}sum_{b=1}^B(g_{I_{tb}}+J_{I_{tb}}(psi_{t-1}-theta_hat))`.
Finally set `mathcal I=N^{-1}sum_n g_n g_n^T`.

## Task

Prove
`Lambda H-hat Sigma_psi+Sigma_psi H-hat Lambda = Lambda(C-bar_psi+H-hat Sigma_psi H-hat)Lambda+2 beta^{-1}Lambda`.

Moreover, show that

- with replacement,
`C-bar_psi=B^{-1}[mathcal I-Gamma theta_hat theta_hat^T Gamma^T/N^2+N^{-1}sum_n J_n Sigma_psi J_n^T-J Sigma_psi J^T]`;
- without replacement,
`C-bar_psi=((N-B)/(B(N-1)))[mathcal I-Gamma theta_hat theta_hat^T Gamma^T/N^2+N^{-1}sum_n J_n Sigma_psi J_n^T-J Sigma_psi J^T]`.

Thus substitution gives a closed matrix relation between `Lambda` and `Sigma_psi` in either sampling scheme.
