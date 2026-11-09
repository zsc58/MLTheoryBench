# Problem

## Setup

Let N, M, and D be positive integers. Fix observations (x_n,y_n), n=1,...,N, with x_n in R^D. Let f be a zero-mean Gaussian process with covariance kernel k_psi, differentiable in its kernel parameters psi and both input arguments. The likelihood factorizes as

p(y|f;eta)=product_{n=1}^N p(y_n|f(x_n);eta).

Write theta=(psi,eta), where the likelihood-parameter vector eta may be absent if the likelihood is fixed. Let Z=(z_1,...,z_M) be inducing inputs in R^D, and define

K_{uu}=k_psi(Z,Z),
k_{nu}=k_psi(x_n,Z),
k_{un}=k_{nu}^T,
k_{nn}=k_psi(x_n,x_n).

Assume K_{uu} is symmetric positive definite. Let m in R^M and S=diag(s_1,...,s_M), with s_j>0, be variational parameters. Set K=K_{uu}+S. Let T be a symmetric positive-definite M by M auxiliary matrix, and define

P_inv=K^{-1},
P_free=2T-TKT.

For a symmetric matrix P, define the predictive quantities

mu_n(P)=k_{nu}Pm,
sigma_n^2(P)=k_{nn}-k_{nu}Pk_{un}.

For v>=0, write

F_n(a,v,eta)=E_{t~N(a,v)}[log p(y_n|t;eta)],

where N(a,0) means the point mass at a. All objectives below are considered on their domains of nonnegative predictive variances. Assume their Gaussian expectations are finite locally. At the arguments under consideration, assume each F_n is differentiable in (a,v,eta); at v=0 this means a finite first-order linear expansion relative to increments with v>=0.

Define

J_inv = sum_{n=1}^N F_n(mu_n(P_inv),sigma_n^2(P_inv),eta)
        - 1/2[-tr(P_inv K_{uu})+m^T P_inv K_{uu}P_inv m+log|K|-log|S|],

J_free = sum_{n=1}^N F_n(mu_n(P_free),sigma_n^2(P_free),eta)
         - 1/2[-tr(P_free K_{uu})-M+m^T P_free K_{uu}P_free m+tr(KT)-log|T|-log|S|].

Here |A| denotes the determinant of A and tr(A) its trace. Define J_naive by replacing every occurrence of P_free in J_free by T, leaving its explicit T terms unchanged.

Let xi=(theta,Z,m,S). Gradients with respect to S refer to its free diagonal coordinates (s_1,...,s_M). When differentiating J_free or J_naive with respect to xi, T is held fixed: dT=0.

## Task

At any parameter point xi_0 satisfying the setup, assign T the numerical value K(xi_0)^{-1} and then keep it fixed during differentiation. Prove that

nabla_xi J_inv(xi_0) = nabla_xi J_free(xi_0;T).

Also prove that the naive stop-gradient objective J_naive does not, in general, have this gradient-matching property at the same numerical assignment T=K(xi_0)^{-1}.
