# Problem

## Setup

Let n and m be positive integers and let 0<delta<1. Let X and Z be nonempty Borel subsets of finite-dimensional Euclidean spaces, with their Euclidean metrics and Borel sigma-algebras. For a set A, write diam(A)=sup_{a,a' in A}||a-a'||_2. Fix finite nonnegative constants B_x, B_z, B_xz, and B_g such that

diam(X)<=B_x, diam(Z)<=B_z, and diam(X x Z)<=B_xz.

Let pi be a probability distribution on X x Z. Draw n+m independent pairs (X_i,Z_i) with law pi. The first n pairs are observed, and only X_i is observed for the remaining m indices.

Let F be a fixed nonempty class of measurable predictors f:X->Z. Let G be a fixed nonempty class of real-valued B_g-Lipschitz functions on X x Z, symmetric in the sense that g in G if and only if -g in G. These classes and their bounds are fixed before sampling. Assume that sample-dependent suprema and infima over F, G, and the induced class H defined below are measurable.

For a probability measure mu and an integrable function g, write mu g for its integral. Define

pi_l=(1/n)sum_{i=1}^n delta_(X_i,Z_i),
pi_l^f=(1/n)sum_{i=1}^n delta_(X_i,f(X_i)),
pi_u^f=(1/m)sum_{i=n+1}^{n+m} delta_(X_i,f(X_i)),
pi_ul^f=(1/(n+m))sum_{i=1}^{n+m} delta_(X_i,f(X_i)).

Here delta_w denotes the probability measure concentrated at w. For each fixed f, let pi^f be the law of (X,f(X)) when (X,Z) has law pi. Set

d_G(mu,nu)=sup_{g in G}|mu g-nu g|,
R(f)=d_G(pi,pi^f).

Fix a measurable, finite real-valued primary loss ell:X x Z x Z->R, and write L^f(x,z)=ell(x,z,f(x)). All the following minimizations are over F:

F1=argmin_{f in F} pi_l L^f,
F2=argmin_{f in F} d_G(pi_l,pi_l^f),
F3=argmin_{f in F} d_G(pi_l,pi_u^f),
F4=argmin_{f in F} d_G(pi_l,pi_ul^f).

Define F*={f in F:f(X_i)=Z_i for every 1<=i<=n}. Assume that, almost surely under the stated sampling experiment,

F1=F2=F*,
F* intersect F3 is nonempty, and
F* intersect F4 is nonempty.

Let f_V be a measurable selection from F1 using the labeled sample, and let f_M be a measurable selection from F2 intersect F3 using the observed labeled pairs and the remaining feature vectors. Neither selection uses the unobserved Z_i for i>n.

Define the fixed induced class

H={x -> g(x,f(x)):g in G, f in F}.

For a class C of real-valued functions and a sample t_1,...,t_s, define its empirical Rademacher complexity by

Rhat_s(C;t_1,...,t_s)=E_sigma[sup_{c in C}(1/s)sum_{i=1}^s sigma_i c(t_i)],

where the sigma_i are independent uniform signs, independent of the data, and the expectation is over these signs only. Abbreviate

Rhat_n(G)=Rhat_n(G;(X_1,Z_1),...,(X_n,Z_n)),
Rhat_n(H)=Rhat_n(H;X_1,...,X_n),
Rhat_{n+m}(H)=Rhat_{n+m}(H;X_1,...,X_{n+m}).

Allow these complexities to take the value +infinity, in which case an upper bound with that right-hand side has its extended-real meaning. Set

Delta=3 B_g B_xz sqrt(2 ln(delta^{-1})).

## Task

Prove each of the following probability guarantees:

1. With probability at least 1-2delta,

R(f_V)-inf_{f in F}R(f)
<=4 Rhat_n(G)+4 Rhat_n(H)+2 Delta/sqrt(n).

2. With probability at least 1-2delta,

R(f_M)-inf_{f in F}R(f)
<=4 Rhat_n(G)+4 Rhat_{n+m}(H)
  +Delta(1/sqrt(n)+1/sqrt(n+m)).
