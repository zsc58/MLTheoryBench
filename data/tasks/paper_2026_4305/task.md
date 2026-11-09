# Problem

## Setup

Fix integers `N>=1`, `d>=1`, and `p>=1`, and numbers `h>0`, `T=Nh`, and `H in (0,1)`. Let `(xi_0,...,xi_{N-1})` be a centered real Gaussian vector with covariance

`E[xi_i xi_j]=1/2(|i-j+1|^{2H}+|i-j-1|^{2H}-2|i-j|^{2H})`.

Let `G_0` be the trivial sigma-field, let `G_n=sigma(xi_0,...,xi_{n-1})` for `1<=n<=N`, and define

`V_H(N)=max_{0<=n<N} E[(E[xi_n|G_n])^2]`.

Let `U` be a closed convex subset of `R^p` containing the origin, and let `x_0 in R^d` be deterministic. Define the ambient parameter space `H_det=(R^p)^N`, its feasible subset `U_det=U^N`, and the inner product and norm

`<u,v>_h=h sum_{n=0}^{N-1}<u_n,v_n>`,
`||u||_h^2=h sum_{n=0}^{N-1}||u_n||^2`.

Write `Pi_{U_det}` for metric projection in this ambient norm. Norms on individual Euclidean spaces are Euclidean, and `*` denotes the Euclidean adjoint of a linear map.

Let

`b,sigma:{0,...,N-1} x R^d x R^p -> R^d`,
`ell:{0,...,N-1} x R^d x R^p -> R`,
`Phi:R^d -> R`

be deterministic maps. Assume they are twice continuously differentiable in their continuous arguments, with bounded globally Lipschitz first and second derivatives, uniformly in the discrete index. Assume there is a finite constant `L'>0` such that, for every `(n,x,u)`,

`||b(n,x,u)||<=L'(1+||x||+||u||)`,
`||sigma(n,x,u)||<=L'`.

For every deterministic `u in H_det`, define

`X_0=x_0`,
`X_{n+1}=X_n+h b(n,X_n,u_n)+sqrt(h) sigma(n,X_n,u_n)xi_n`,

and

`J(u)=E[Phi(X_N)+h sum_{n=0}^{N-1}ell(n,X_n,u_n)]`.

For one realized trajectory, write

`A_n=I_d+h b_x(n,X_n,u_n)`,
`B_n=sqrt(h)sigma_x(n,X_n,u_n)`,
`Lambda_n=ell_x(n,X_n,u_n)`.

Define the reverse sweep and estimator by

`hat p_N=Phi_x(X_N)`,
`hat p_n=A_n^*hat p_{n+1}+B_n^*hat p_{n+1}xi_n+h Lambda_n`,
`hat g_n=b_u(n,X_n,u_n)^*hat p_{n+1}+ell_u(n,X_n,u_n)+h^{-1/2}sigma_u(n,X_n,u_n)^*hat p_{n+1}xi_n`.

Let `hat g(u)=(hat g_0,...,hat g_{N-1}) in H_det`.

Assume `J:H_det -> R` is Frechet differentiable, and let `nabla J` denote its gradient for `<.,.>_h`. Assume there are constants `mu>0` and `L_J<infinity` such that, for all `u,v in U_det`,

`<nabla J(u)-nabla J(v),u-v>_h>=mu||u-v||_h^2`,
`||nabla J(u)-nabla J(v)||_h<=L_J||u-v||_h`.

Assume also that there are finite nonnegative constants `M_2,M_4`, independent of the feasible parameter `u`, such that, for every deterministic `u in U_det`,

`max_{0<=n<=N}E||hat p_n^u||^2<=M_2(1+V_H(N))`,
`max_{0<=n<=N}E||hat p_n^u||^4<=M_4(1+V_H(N))^2`.

The architecture `(N,h,H)` is fixed; these moment constants may depend on it.

## Task

Prove the following integrated theorem. For every deterministic `u in U_det`, the reverse-sweep estimator is unbiased:

`E[hat g(u)]=nabla J(u)`.

In particular, evaluating the estimator at a current iterate using a trajectory sampled independently of that iterate gives conditional expectation equal to the gradient there.

Moreover, let `u*` be the unique minimizer of `J` on `U_det`. Starting from any fixed `u^0 in U_det`, run

`u^{k+1}=Pi_{U_det}(u^k-alpha_k hat g^k)`,
`alpha_k=alpha_0/(k+1)`, where `alpha_0>1/mu`.

Here `hat g^k` is obtained by the displayed forward and reverse recursions at `u^k`, using a new Gaussian vector with the specified covariance, independently of all trajectories sampled at earlier iterations. Then there are finite constants `C_0,C_1`, independent of `K`, such that, for every integer `K>=1`,

`E||u^K-u*||_h^2 <= C_0(1+V_H(N))/K + C_1(1+V_H(N))/(K h)`.

The constants may depend on the fixed architecture, the coefficient and moment bounds, `mu`, `L_J`, `alpha_0`, and the initial error, but not on the iteration count `K`.
