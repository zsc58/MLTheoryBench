# Reference Proof

## Proof Structure

1. Prove forward invariance of each hidden-state cube and derive uniform gate and candidate bounds in the induced infinity norm.
2. For two trajectories, apply the sigmoid `1/4`-Lipschitz and tanh `1`-Lipschitz inequalities to obtain the coupled incremental recursion. The displayed parameter condition makes its state coefficient strictly smaller than one, yielding layer delta-ISS.
3. Compose the layer recursions through the stack as a nonnegative lower-triangular comparison system. Its diagonal contractions imply Schur stability, and matrix-power decay plus the convergent input-response series yield network delta-ISS.

## Complete Proof

Use `||.||_infty` and its induced operator norm throughout. Write `d_l(k)=||h_k^{a,(l)}-h_k^{b,(l)}||_infty` and `e_k=||u_k^a-u_k^b||_infty`. For layer `l`, set `r_l=||[W_f^(l) R_f^(l) b_f^(l)]||_infty`, `s_l=||[W_h~^(l) R_h~^(l) b_h~^(l)]||_infty`, `bar_sigma_l=sigma(r_l)`, and `bar_phi_l=tanh(s_l)`. Because the concatenated vector `(u~_k^(l),h_k^(l),1)` has infinity norm at most one on the stated cubes, every gate satisfies `1-bar_sigma_l <= f_{j,k} <= bar_sigma_l`, and every candidate state satisfies `||h~_k^(l)||_infty <= bar_phi_l`.

The hidden update is a componentwise convex combination of `h_k^(l)` and `h~_k^(l)`. Induction from the bounded initial state therefore proves that `H_l=[-1,1]^{n_l}` is forward invariant. Consequently the stacked layer inputs remain in `V_1=U` and `V_l=H_{l-1}` for `l>1`.

For two trajectories of one layer, the sigmoid and tanh Lipschitz bounds give
`||Delta f_k||_infty <= (1/4)(||R_f^(l)||_infty d_l(k)+||W_f^(l)||_infty ||Delta u~_k^(l)||_infty)`
and
`||Delta h~_k||_infty <= ||W_h~^(l)||_infty ||Delta u~_k^(l)||_infty + ||R_h~^(l)||_infty(bar_sigma_l d_l(k)+||Delta f_k||_infty)`.
Using `||h_k||_infty<=1`, `||h~_k||_infty<=bar_phi_l`, and `|1-f|<=bar_sigma_l` in the update difference yields `d_l(k+1)<=alpha_l d_l(k)+beta_l ||Delta u~_k^(l)||_infty`, with `alpha_l=bar_sigma_l+bar_sigma_l^2||R_h~^(l)||_infty+(1/4)||R_f^(l)||_infty(bar_sigma_l||R_h~^(l)||_infty+bar_phi_l+1)` and `beta_l=bar_sigma_l||W_h~^(l)||_infty+(1/4)||W_f^(l)||_infty(bar_sigma_l||R_h~^(l)||_infty+bar_phi_l+1)`. The hypothesis gives `0<alpha_l<1`. Iteration gives `d_l(k)<=alpha_l^k d_l(0)+beta_l(1-alpha_l)^(-1) max_{0<=t<k}||Delta u~_t^(l)||_infty`. Thus `psi_l(r,k)=alpha_l^k r` is in `KL`, and a linear gain with slope at least `beta_l/(1-alpha_l)` (increased by any positive constant if necessary) is in `K_infinity`.

For the stack, let `d(k)=(d_1(k),...,d_L(k))^T`. Layer one obeys `d_1(k+1)<=alpha_1d_1(k)+beta_1e_k`; for `l>1`, `d_l(k+1)<=alpha_ld_l(k)+beta_ld_{l-1}(k+1)`. Eliminating the latter-time terms recursively gives `d(k+1)<=Ad(k)+Be_k`, where `A` is nonnegative lower triangular with `A_ll=alpha_l`, `A_lj=beta_lA_(l-1),j` for `j<l`, `B_1=beta_1`, and `B_l=beta_lB_(l-1)`. Since all diagonal entries lie in `(0,1)`, `A` is Schur stable. Hence for some `C>0`, `rho in (0,1)`, `||A^k||_infty<=Crho^k`, and `S=sum_{j>=0}||A^jB||_infty<infinity`. Unrolling yields `||d(k)||_infty<=Crho^k||d(0)||_infty+S max_{0<=t<k}e_t`. A `KL` majorant of the first term and a linear `K_infinity` gain with slope at least `S` prove delta-ISS of the stacked network on `H` with respect to `U`.
