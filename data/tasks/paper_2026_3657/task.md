# Problem

## Setup

Let M>=2 be an integer and let 1<=p<infinity. For each block i, let X_i be a smooth complete separable Riemannian manifold with geodesic distance d_i and volume measure dx_i. In this problem, P_p(X_i) denotes the probability measures that are absolutely continuous with respect to dx_i and have finite p-th moment. For probabilities eta and nu on X_i, define

W_p(eta,nu) = (inf_{zeta in C(eta,nu)} integral d_i(x,y)^p zeta(dx,dy))^(1/p),

where C(eta,nu) is the set of probability couplings with these marginals. This formula is allowed to take the value infinity outside the finite-moment domain.

For volume-absolutely-continuous probabilities eta and nu on the same block, let I denote relative Fisher information with normalization

I(eta||nu) = integral |gradient log(deta/dnu)|^2 deta

when eta is absolutely continuous with respect to nu. Here the gradient and its norm are Riemannian, and the logarithmic gradient is interpreted weakly when necessary. Set I(eta||nu)=infinity if absolute continuity fails, or if the logarithmic gradient does not exist in this sense or is not square-integrable under eta.

Let pi=e^(-f) dx be a target probability on the product manifold, where dx is product volume, and assume pi has finite p-th moment for the product Riemannian distance. Write

KL(alpha||pi)=integral log(dalpha/dpi) dalpha

when alpha is absolutely continuous with respect to pi, and set KL(alpha||pi)=infinity otherwise. For a vector mu=(mu^1,...,mu^M), write mu_{-i} for all components except i. Let Gamma_i be the single-valued coordinate-optimal update for this target:

Gamma_i[mu_{-i}] in argmin_{eta in P(X_i)} KL(mu^1 tensor ... tensor mu^{i-1} tensor eta tensor mu^{i+1} tensor ... tensor mu^M || pi),

where P(X_i) is the set of Borel probability measures on X_i. The maps are fixed deterministic maps. Assume they are well-defined for all inputs used below and take values in P_p(X_i).

Suppose there is a fixed point mu_*=(mu_*^1,...,mu_*^M) in the product of the P_p(X_i), with Gamma_i[mu_{*,-i}]=mu_*^i for every i. Let U be a product neighborhood of mu_* in these Wasserstein spaces. Assume there are finite constants L_ij>=0 such that, for every mu in U and every i,

I(Gamma_i[mu_{-i}]||Gamma_i[mu_{*,-i}])^(1/2) <= sum_{j!=i} L_ij W_p(mu^j,mu_*^j).

Assume also that each fixed-point marginal satisfies

lambda_i W_p(eta,mu_*^i) <= I(eta||mu_*^i)^(1/2)

for every probability eta absolutely continuous with respect to mu_*^i, where lambda_i>0 is finite and both sides have their extended-value meanings.

Define R by R_ii=0 and R_ij=L_ij/lambda_i for i!=j. Let rho(B) denote the spectral radius of a square matrix B, and suppose rho(R)<1. Choose q with rho(R)<q<1 and a strictly positive vector delta satisfying R delta<=q delta. Choose c>0 so that the product set defined by W_p(mu^i,mu_*^i)<=c delta_i for every i is contained in U. Fix a deterministic initialization mu_0 in this set.

Consider the following three schedules, each started from mu_0:

- Parallel CAVI: mu_{k+1}^i=Gamma_i[mu_{k,-i}] for every i.
- Uniform random-scan CAVI: at step k choose J_k uniformly from {1,...,M}, independently of all previous choices, set mu_{k+1}^{J_k}=Gamma_{J_k}[mu_{k,-J_k}], and leave the other marginals unchanged.
- Systematic sequential CAVI: in each sweep update i=1,...,M in this order, with mu_{k+1}^i=Gamma_i[mu_{k+1}^1,...,mu_{k+1}^{i-1},mu_k^{i+1},...,mu_k^M]. Here k counts complete sweeps.

Let R_L and R_U be the strict lower- and upper-triangular parts of R, let I_M be the M-by-M identity matrix, and set

A=(R+(M-1)I_M)/M,    G=(I_M-R_L)^(-1)R_U.

## Task

Prove that all iterates remain in U, including intermediate states within sequential sweeps and every realization of random scan. For each schedule, write e_k^i=W_p(mu_k^i,mu_*^i) and e_k=(e_k^1,...,e_k^M)^T. Prove:

1. Parallel CAVI satisfies e_{k+1}<=R e_k and converges exponentially in vector Wasserstein error with asymptotic upper rate rho(R).
2. Uniform random-scan CAVI satisfies E[e_{k+1}|e_k]<=A e_k and converges exponentially in expected vector Wasserstein error with asymptotic upper rate rho(A).
3. Systematic sequential CAVI satisfies e_{k+1}<=G e_k and converges exponentially in vector Wasserstein error with asymptotic upper rate rho(G). Moreover, rho(G)<1 whenever rho(R)<1.

All vector inequalities are componentwise. More precisely, for any fixed norm on R^M and every q' strictly larger than the relevant spectral radius and less than 1, prove that there is a finite constant C_{q'}, independent of k, such that ||e_k||<=C_{q'}(q')^k for parallel and sequential updates, and E||e_k||<=C_{q'}(q')^k for random scan. Constants may depend on the fixed problem data, the initialization, the norm, and q'. Expectations are over the coordinate choices. Thus the claimed asymptotic rates mean limsup upper bounds on ||e_k||^(1/k), or on (E||e_k||)^(1/k), rather than equality of the actual convergence rate with the matrix spectral radius.
