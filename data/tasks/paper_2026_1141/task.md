# Problem

## Setup

Fix an integer n>=2. Let S^n be the real symmetric n x n matrices, ordered by the Loewner relation A<=B when B-A is positive semidefinite. Define

VPM^o(n)={X in S^n: X is positive definite and I-X is positive definite}.

For X,Y in VPM^o(n), define the Hilbert metric of the embedded bicone by

M_H(X,Y)=inf{t>0: X<=tY and I-X<=t(I-Y)},

d_H(X,Y)=log M_H(X,Y)+log M_H(Y,X).

Let lambda_1,...,lambda_n>0 be the generalized eigenvalues of Y^{-1}X (equivalently, the eigenvalues of Y^{-1/2}XY^{-1/2}). Define the restricted affine-invariant distance by

d_AIRM^parallel(X,Y)=(sum_{i=1}^n (log lambda_i)^2)^{1/2}.

## Task

Prove the following integrated theorem. For every X,Y in VPM^o(n),

1. (1/sqrt(n)) d_AIRM^parallel(X,Y) <= d_H(X,Y), and the constant 1/sqrt(n) is sharp: it cannot be replaced by any larger universal constant.
2. There is no finite universal kappa such that d_H(X,Y) <= kappa d_AIRM^parallel(X,Y) for all X,Y in VPM^o(n).
