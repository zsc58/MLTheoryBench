# Problem

## Setup

Let T^d=R^d/Z^d be the flat unit torus, with normalized Lebesgue measure dx and its geodesic distance. Let P2(T^d) be its quadratic-Wasserstein space, and write W2 for the quadratic-Wasserstein distance.

For a measure rho, define its tangent space by

T_rho P2(T^d) = closure in L2(rho) of {grad f: f is a smooth periodic function}.

Let Pi_rho be the L2(rho)-orthogonal projection onto this space. For a vector field z with weak spatial derivatives, use

||z||_H1(rho)^2 = integral (|z|^2+|Dz|_F^2) d rho,

and let H1(T^d) denote the corresponding norm with dx in place of rho. Here |Dz|_F is the Frobenius norm of its derivative matrix. All spatial fields are periodic, and norms without a measure in the subscript are taken with respect to dx.

An absolutely continuous Wasserstein curve is regular if its tangent velocity has finite time-integrated squared L2 norm and integrable spatial Lipschitz constant. It is strongly regular if that velocity has finite time-integrated squared L2 norm and uniformly bounded spatial Lipschitz constant. Write PT^W_(rho->eta) for Levi-Civita Wasserstein parallel transport along the specified regular geodesic from rho to eta. Define

Exp_rho(z) = (x -> x+z(x) modulo Z^d)#rho.

Fix constants 0<m<=M<infinity and K,L,S>0. Let C be a class of probability measures on T^d. Every measure in C has a density between m and M. For every pair alpha,beta in C, its Wasserstein geodesic (rho_t^(alpha,beta))_(0<=t<=1), parameterized over [0,1], has density r_t^(alpha,beta) and tangent velocity b_t^(alpha,beta). Require uniformly over these pairs that

m<=r_t^(alpha,beta)<=M,

sup_t ||r_t^(alpha,beta)||_W1,infinity <= K,

sup_t ||grad log r_t^(alpha,beta)||_Linfinity <= K,

sup_t ||b_t^(alpha,beta)||_W1,infinity <= K.

The map t -> r_t^(alpha,beta) is absolutely continuous from [0,1] into L-infinity(T^d), with essential supremum of ||partial_t r_t^(alpha,beta)||_Linfinity at most K. These bounds are interpreted almost everywhere where appropriate.

For every alpha,beta,beta' in C and every t in [0,1], also require

||r_t^(alpha,beta)-r_t^(alpha,beta')||_Linfinity <= K W2(beta,beta'),

||r_t^(alpha,beta)-r_t^(alpha,beta')||_W1,infinity <= K W2(beta,beta'),

||b_t^(alpha,beta)-b_t^(alpha,beta')||_Linfinity <= K W2(beta,beta').

These are the uniform admissibility assumptions. Geodesics and their tangent velocities in what follows are those covered by these assumptions.

For an admissible geodesic rho_t=(F_t)#rho_0, let F_t be its Lagrangian flow, with F_0 the identity. The bounded spatial Lipschitz velocities give invertible flow maps. Define FAN_N(rho_0->rho_1) as follows. Set h=1/N and t_k=kh, and start with z_0=v in T_(rho_0)P2(T^d). For k=0,...,N-1, set S_k=F_(t_(k+1)) composed with F_(t_k)^(-1). For each y at time t_k, take the base-torus Jacobi field J_(k,y) along

r -> F_(t_k+r)(F_(t_k)^(-1)(y)), 0<=r<=h,

with J_(k,y)(0)=0 and initial covariant derivative z_k(y). Transfer its scaled terminal value to the endpoint and project:

z_(k+1) = Pi_(rho_(t_(k+1))) (x -> h^(-1) J_(k,S_k^(-1)(x))(h)).

The terminal field z_N is FAN_N(rho_0->rho_1)v. Here N is any positive integer.

For a positive integer horizon T, let nu_0,...,nu_T be control measures in C. Let v_i be the initial displacement velocity of the geodesic from nu_i to nu_(i+1), so Exp_(nu_i)(v_i)=nu_(i+1), and suppose

||v_i||_H1(T^d) <= S, 0<=i<T.

For rho in C define

u_i(rho)=PT^W_(nu_i->rho)v_i,

u_hat_(i,N)(rho)=FAN_N(nu_i->rho)v_i.

Here the symbols u_i and u_hat_(i,N) denote vector fields; explicitly, u_i(rho)=PT^W_(nu_i->rho)v_i and u_hat_(i,N)(rho)=FAN_N(nu_i->rho)v_i. The true and predicted counterfactual sequences are

mu_(i+1)*=Exp_(mu_i*)(u_i(mu_i*)),

mu_hat_(i+1)*=Exp_(mu_hat_i*)(u_hat_(i,N)(mu_hat_i*)),

with mu_hat_0*=mu_0*. Assume all these true and predicted measures belong to C, and the exact fields u_i(mu_i*) have spatial Lipschitz constant at most L. The admissibility constants are uniform over the iterations and resolutions under consideration.

## Task

Prove that there are constants C_tr and C_WPT depending only on d,m,M,K, and a constant B depending only on d,m,M,K,S, such that for every admissible strongly regular geodesic from nu to mu, every v in T_nu P2(T^d) intersect H1(nu), and every positive integer N,

||FAN_N(nu->mu)v-PT^W_(nu->mu)v||_L2(mu) <= (C_tr/N)||v||_H1(nu).

Moreover, writing a_i=W2(mu_hat_i*,mu_i*) and q=L+S C_WPT, show that

a_(i+1) <= (1+q)a_i+B/N, a_0=0,

and hence, for every positive integer horizon T,

sum_(i=1)^T W2(mu_hat_i*,mu_i*) <= (BT/N)((1+q)^T-1)/q.

The quotient is interpreted continuously as T when q=0. In particular, for each fixed T the accumulated trajectory error is O(T/N)=o(1) as N tends to infinity; the constant in this fixed-horizon asymptotic assertion may depend on T.
