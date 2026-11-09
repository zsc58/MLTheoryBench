# Problem

## Setup

Let d,n_0,n_1,...,n_d be positive integers. Let X=X_1 x ... x X_d, where each X_nu is a subset of R, and let mu be a Borel probability measure on X. For each mode nu, let V_nu be a finite-dimensional space of continuous real-valued functions on X_nu with basis phi_1^nu,...,phi_{n_nu}^nu. Set

`Phi_nu(x_nu)=(phi_1^nu(x_nu),...,phi_{n_nu}^nu(x_nu))^T`,

`Phi(x)=Phi_1(x_1) otimes ... otimes Phi_d(x_d)`.

Let E=R^{n_0} otimes R^{n_1} otimes ... otimes R^{n_d}, with its Euclidean coefficient inner product and the class mode first. For A in E, define G(A)(x) by contracting A with Phi(x) in the feature modes. Thus G is defined linearly on the entire ambient coefficient space.

Let T be a smooth embedded fixed-rank tensor-tree-network manifold in E. Let M be a smooth finite-dimensional Riemannian manifold and tau:M->T a smooth surjective submersion. Write H=G(T). In every displayed coefficient-operator composition, D tau(Theta) denotes the differential of tau followed by the inclusion T_{tau(Theta)}T->E, and D tau(Theta)^* denotes its adjoint from E to T_Theta M.

Let

`S={p in R^{n_0}: p_j>0 for every j, sum_j p_j=1}`,

` sigma_j(z)=exp(z_j)/sum_k exp(z_k)`.

Let P={sigma o h:h in H} be the output model, and define bar F:M->P by bar F(Theta)=sigma o G(tau(Theta)). Assume P is a smooth finite-dimensional manifold of functions on X and bar F is a smooth surjective submersion. Tangent vectors to P are represented by measurable vector-valued functions eta with sum_j eta_j(x)=0.

For p in S, define

`F(p)=diag(1/p_1,...,1/p_{n_0})`,

`<u,v>_p^FR=u^T F(p)v` for u,v in T_p S={w:sum_j w_j=0}.

Equip P with the integrated metric

`<eta,chi>_s=int_X eta(x)^T F(s(x))chi(x) mu(dx)`.

More explicitly, assume that for every s in P and eta in T_s P, the integral `int_X sum_j eta_j(x)^2/s_j(x) mu(dx)` is finite, is positive for every nonzero eta, and that these inner products form a smooth Riemannian metric on P. The adjoint of D bar F uses this metric and the given metric on M. Define

`Z(Theta)=D bar F(Theta)^*D bar F(Theta)`.

Let R:P->R be a differentiable objective. For a fixed integer m>=1 and inputs x^1,...,x^m in X, where x^i=(x_1^i,...,x_d^i), let ell_i:S->R be differentiable pointwise losses and define

`R_m(s)=(1/m)sum_{i=1}^m ell_i(s(x^i))`.

Define the sampled output map

`bar F_m(Theta)=(bar F(Theta)(x^1),...,bar F(Theta)(x^m)) in S^m`.

At q=(q_1,...,q_m) in S^m use the averaged product metric

`<u,v>_{m,q}=(1/m)sum_{i=1}^m u_i^T F(q_i)v_i`,

and define the empirical pullback operator

`hat Z_m(Theta)=D bar F_m(Theta)^*D bar F_m(Theta)`.

Gradients on M and minimum norms in its tangent spaces use its given Riemannian metric. In the matrix expression defining C below, the star on D sigma means Euclidean transpose, not its Fisher-Rao adjoint.

## Task

For Theta in M, writing f_x=G(tau(Theta))(x), prove

`D bar F(Theta)^*D bar F(Theta) = int_X D tau(Theta)^*[ C(f_x) otimes (Phi_1(x_1)Phi_1(x_1)^T) otimes ... otimes (Phi_d(x_d)Phi_d(x_d)^T) ]D tau(Theta) mu(dx)`,

where

`C(z)=D sigma(z)^*F(sigma(z))D sigma(z)`.

Prove also that for every fixed sample x^1,...,x^m,

`hat Z_m(Theta)=(1/m)sum_{i=1}^m D tau(Theta)^*[ C(f_{x^i}) otimes (Phi_1(x_1^i)Phi_1(x_1^i)^T) otimes ... otimes (Phi_d(x_d^i)Phi_d(x_d^i)^T) ]D tau(Theta)`.

Finally state the population and empirical natural-gradient equations

`Z(Theta)[zeta]=grad(R o bar F)(Theta)`,

`hat Z_m(Theta)[zeta_m]=grad(R_m o bar F)(Theta)`,

and justify the Moore-Penrose minimum-norm solution formulas, including when either system is singular.
