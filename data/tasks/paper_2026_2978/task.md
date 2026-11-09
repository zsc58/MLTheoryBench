# Problem

## Setup

Fix integers s>=8 and N>=1, and finite constants B>=1 and Lambda_max>=2. Let Lambda=[0,Lambda_max]^s.

An instance is a mixed-integer linear program P=(c,A,b,C,h). Its finite dimensions are nonnegative integers m,p,t with m+p>=1, and
c in R^{m+p}, A in R^{s x (m+p)}, b in R^s, C in R^{t x (m+p)}, h in R^t.
The variable domain is R_+^m x {0,1}^p, the coupling constraints are Ax>=b, and the hard constraints are Cx>=h. The instance class includes all such finite dimensions and coefficient tuples satisfying the conditions below. Write
X(P)={x in R_+^m x {0,1}^p:Cx>=h}.
For lambda in Lambda, define
nu(lambda,P)=min_{x in X(P)}{c^T x+lambda^T(b-Ax)}.
Assume X(P) is nonempty and this minimum is finite and attained for every lambda in Lambda. Require
|b_k|<=B and |(Ax)_k|<=B
for every x in X(P) and every k=1,...,s.

Define the box-restricted optimal multiplier set and its minimum-norm member by
K(P)=argmax_{lambda in Lambda}nu(lambda,P),
z(P)=argmin_{lambda in K(P)}||lambda||_2^2.
Use the usual Borel structure on the finite-dimensional instance coefficient spaces, with their disjoint union when dimensions vary, and require P->z(P) to be measurable.

Let D range over all probability distributions supported on this instance class. Define the warm-start loss and population risk by
ell(w,P)=||w-z(P)||_2^2,
R_D(w)=E_{P~D} ell(w,P), for w in Lambda.
From iid full-instance observations S=(P_1,...,P_N)~D^N, define the ERM
w_hat_N in argmin_{w in Lambda} N^{-1}sum_{i=1}^N ell(w,P_i).
Define the minimax expected excess risk by
M_{N,s}=inf_A sup_D E_{S~D^N}[R_D(A(S))-min_{w in Lambda}R_D(w)],
where A ranges over measurable estimators of the observed instances taking values in Lambda. The dependence of M_{N,s} on the fixed constants B and Lambda_max is suppressed in the notation.

## Task

Prove that the ERM is
w_hat_N=N^{-1}sum_{i=1}^N z(P_i)
and, for every admissible D, satisfies
E_S[R_D(w_hat_N)-min_{w in Lambda}R_D(w)]<=s Lambda_max^2/(4N).

Moreover, prove that there is a universal constant c>0, independent of s,N,B,Lambda_max, such that
M_{N,s}>=c s/N
for every parameter choice in the stated regime. Hence, for fixed B and Lambda_max, the minimax expected excess risk for deterministic warm-start multiplier learning is Theta(s/N).
