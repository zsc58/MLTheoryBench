# Problem

## Setup

Let D>=2 and m>=1 be integers, let p_0>=0, and let ell,r>0. Fix a deterministic sequence of unit keys k_t in R^D, indexed by t=1,2,... .

A latent matrix state X_t in R^{D x m} has initial distribution
\[
\operatorname{vec}(X_0)\sim\mathcal N(0,I_m\otimes p_0I_D).
\]
It evolves and is observed according to
\[
X_t=X_{t-1}+E_t,\qquad
 o_t=X_t^Tk_t+\varepsilon_t,
\]
where vec(E_t) is distributed as N(0,ell^2 I_{Dm}) and epsilon_t is distributed as N(0,r^2 I_m). All process and observation noises are mutually independent across times and independent of X_0. Thus the transition has independent column noises with isotropic covariance.

Let P_t be the posterior covariance of a column of X_t given o_1,...,o_t, and let bar P_t be its predicted covariance given o_1,...,o_{t-1}, immediately before the observation at time t. The initial column covariance is P_0=p_0 I_D.

Fix unit keys k_A,k_B in R^D and write rho=k_A^T k_B. For a write using k_A, define
\[
\Delta_{B,t}=k_B^TP_tk_B-k_B^TP_{t-1}k_B.
\]
For all t>=1, define
\[
\bar\sigma_{A,t}^2=k_A^T\bar P_tk_A,
\qquad
\bar\sigma_{B,t}^2=k_B^T\bar P_tk_B,
\qquad
\rho_{\bar P_t}
=\frac{k_B^T\bar P_tk_A}
{\sqrt{\bar\sigma_{A,t}^2\bar\sigma_{B,t}^2}},
\]
and
\[
x_t=k_A^T\bar P_tk_A,
\qquad g_t=\frac{x_t}{r^2+x_t},
\qquad w_t=\bar P_tk_B.
\]
When |rho|<1, also define
\[
e_\perp=\frac{k_B-\rho k_A}{\sqrt{1-\rho^2}},
\qquad z_t=e_\perp^T\bar P_te_\perp.
\]
For nonzero vectors, angle denotes the Euclidean angle in [0,pi].

## Task

Prove the following integrated theorem. For every write using k_A,
\[
\Delta_{B,t}=\ell^2-
\frac{(k_B^T\bar P_tk_A)^2}{r^2+k_A^T\bar P_tk_A}
=\ell^2-
\frac{\bar\sigma_{B,t}^2\rho_{\bar P_t}^{\,2}\bar\sigma_{A,t}^2}
{r^2+\bar\sigma_{A,t}^2}.
\]
The subtracted contraction lies between 0 and bar sigma_{B,t}^2.

Suppose there is an integer N>=1 such that k_t=k_A for every t>=N, with no additional restriction on the earlier keys. Then, for t>=N,
\[
x_{t+1}=\ell^2+\frac{r^2x_t}{r^2+x_t},
\]
and x_t converges to
\[
x_* =\frac{\ell^2+\sqrt{\ell^4+4r^2\ell^2}}2.
\]
Moreover,
\[
\Delta_{B,t}\longrightarrow(1-\rho^2)\ell^2,
\]
which is strictly positive for |rho|<1, and
\[
g_t\longrightarrow g_* =\frac{x_*}{r^2+x_*},
\qquad
 g_*\sim\ell/r\quad\text{as }\ell/r\to0,
\qquad
 g_*\to1\quad\text{as }\ell/r\to\infty.
\]
For |rho|<1, under the same eventual repeated-key assumption,
\[
\cos\angle(w_t,k_B)\longrightarrow\sqrt{1-\rho^2}.
\]

Finally, in the special case k_t=k_A for every t>=1, prove that for |rho|<1 the following finite-time identity also holds:
\[
\cos\angle(w_t,k_B)=
\frac{\rho^2x_t+(1-\rho^2)z_t}
{\sqrt{\rho^2x_t^2+(1-\rho^2)z_t^2}}.
\]
