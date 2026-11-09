# Reference Proof

Let d=(K-1)+Kr+K r(r+1)/2 and use the fixed coordinate representation
vartheta(Theta)=(pi_1,...,pi_{K-1},mu_1,...,mu_K,vech(Sigma_1),...,vech(Sigma_K)) in R^d, with pi_K determined by the simplex constraint. Let G={g_{k,Theta}: g_{k,Theta}(x)=psi_k(x;Theta), 1<=k<=K, Theta in Phi}.

For group s, write P_s g=E_{P_s}[g(X)] and P_{n_s,s}g=n_s^{-1} sum_i g(X_i^(s)). For every Theta, the max and absolute-value inequalities imply

|hatDelta(Theta)-Delta(Theta)| <= max_k |(P_{n_1,1}-P_1)g_{k,Theta}| + max_k |(P_{n_2,2}-P_2)g_{k,Theta}|.

Therefore it suffices to control the two uniform deviations over G.

Define the logarithmic component scores

a_k(x;Theta)=log(pi_k) -(1/2)log det(Sigma_k) -(1/2)(x-mu_k)^T Sigma_k^{-1}(x-mu_k).

The common Gaussian normalizing constant is omitted because it cancels in the softmax. Thus

psi_k(x;Theta)=exp(a_k(x;Theta))/sum_l exp(a_l(x;Theta)).

For ||x||_2<=x_max and Theta in Phi, the parameter constraints imply uniform derivative bounds. In particular,

|partial a_k/partial pi_k|<=1/xi,

||partial a_k/partial mu_k||_2<=zeta^{-1}(x_max+nu),

and

||partial a_k/partial Sigma_k||_F <= (1/2)||Sigma_k^{-1}||_F +(1/2)||Sigma_k^{-1}(x-mu_k)(x-mu_k)^T Sigma_k^{-1}||_F.

The last expression is bounded by a constant depending only on zeta, nu, x_max, and r. Equivalence of Frobenius and vech norms contributes only a factor depending on r. Since K is fixed, the full score vector has uniformly bounded gradient in the d-dimensional coordinates. The softmax Jacobian has bounded operator norm, so there is L=L(xi,zeta,nu,x_max,K,r) such that

|psi_k(x;Theta)-psi_k(x;Theta')|<=L||vartheta(Theta)-vartheta(Theta')||_2

for all k, x in the support, and Theta,Theta' in Phi. The parameter class is convex in these coordinates, so the inequality follows by integrating the gradient along the segment between the two parameters. Also, every g in G is [0,1]-valued.

The class G is separable: Phi is a subset of finite-dimensional Euclidean space, and (x,Theta) maps continuously to psi_k(x;Theta) on the stated positive-definite parameter domain. A countable dense subset of Phi therefore has the same pointwise suprema as Phi, and boundedness gives the corresponding measurable empirical and population suprema.

Fix a group sample of size m and use the empirical L2 metric ||.||_{m,2}. A Euclidean covering of the parameter ball maps to a function-class covering, and the finite union over k gives the valid all-scale bound

log N(u,G,||.||_{m,2}) <= log K + d log(1+4LB/u),

for u>0. The factor 4 accommodates the standard conversion between covers with centers in the ambient ball and centers indexed by the parameter class. Unlike the expression log K+d log(3LB/u), this bound remains valid when u>LB.

Apply the standard Dudley entropy-integral inequality for [0,1]-valued classes. It gives

Rhat_m(G) <= inf_{alpha>=0} [4alpha +(C_D/sqrt(m)) integral_alpha^1 sqrt(log N(u,G,||.||_{m,2})) du].

Using the preceding covering bound and the substitution u=LB t on the part of the integral where u is of order LB, together with the elementary bound log(1+v)<=v for small v and a constant bound for the remaining scales, yields

Rhat_m(G)<=C_0 sqrt(d/m),

where C_0 depends only on xi,zeta,nu,x_max,K,r,B. The log K term is absorbed because d>=1 and K is fixed.

The bounded-loss Rademacher inequality for a separable [0,1]-valued class states that, for confidence parameter eta, with probability at least 1-eta,

sup_{g in G}|(P_m-P)g| <=2 Rhat_m(G)+4 sqrt(2 log(4/eta)/m).

Its boundedness hypothesis is supplied by 0<=psi_k<=1, its measurability hypothesis by the separability argument above, and its metric is exactly the empirical L2 metric used in the entropy calculation. Apply this inequality to each group with eta=delta/2. With probability at least 1-delta/2 for each s,

sup_{g in G}|(P_{n_s,s}-P_s)g| <=2C_0 sqrt(d/n_s)+4 sqrt(2 log(8/delta)/n_s).

A union bound over the two group events gives simultaneous validity with probability at least 1-delta. Combining the two deviations and using n'=min(n_1,n_2) gives

sup_{Theta in Phi}|hatDelta(Theta)-Delta(Theta)| <=4C sqrt(d/n')+8 sqrt(2 log(8/delta)/n'),

for C depending only on xi,zeta,nu,x_max,K,r,B. This proves the target.
