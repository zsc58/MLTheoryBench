# Problem

## Setup

Fix integers n >= 1 and d >= 1, and a deterministic point xi in R^n. Let q(x)=1+||x||^2/n and r(x,y)=1+x^T y/n. For integers 0 <= s <= floor(d/2), set
c(s,d)=(d!)^2/[2^(2s)(s!)^2(d-2s)!].
Let f:R^n -> R be the centered Gaussian process with covariance
K(x,y)=sum_{s=0}^{floor(d/2)} c(s,d)q(x)^s q(y)^s r(x,y)^(d-2s).
Assume f has almost surely C^2 sample paths.

On D=R^n times (R without {0}), define
F(x,lambda)=(f(x),x-xi+lambda grad f(x)),
and let J_F(x,lambda) be its Jacobian with respect to (x,lambda).
Assume the following local Kac--Rice conditions: for Lebesgue-almost every (x,lambda) in D, the Gaussian vector F(x,lambda) has nonsingular covariance and
P(det J_F(x,lambda)=0 | F(x,lambda)=0)=0;
furthermore, the function
p_{F(x,lambda)}(0) E[|det J_F(x,lambda)| | F(x,lambda)=0]
is integrable on every compact subset of D. Here p denotes a Gaussian density, and conditional expectations at specified values are evaluated using the Gaussian conditional laws of the field and its derivatives.

For lambda != 0, call (x,lambda) an ED-critical pair at xi when
f(x)=0,     x-xi+lambda grad f(x)=0.
Let N_xi be the number of such pairs in D, counted without multiplicity, with value +infinity allowed initially.

## Task

Prove the following integrated theorem.

1. The expected count has the Kac--Rice representation
E N_xi=integral_{R^n} integral_{R\{0}} |lambda|^(-n) p_{(f(x),grad f(x))}(0,(xi-x)/lambda)
 E[|grad f(x)^T adj(I_n+lambda Hess f(x))grad f(x)| | f(x)=0, grad f(x)=(xi-x)/lambda] d lambda dx.
2. For each fixed n and xi there is a finite constant C_{n,xi}, independent of d, such that for every integer d >= 1,
E N_xi <= C_{n,xi} d^(n/2).

Here p denotes the joint Gaussian density where it exists and adj is the classical adjugate matrix.
