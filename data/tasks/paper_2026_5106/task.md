# Problem

## Setup

Fix p in (0,1) and a deterministic sequence (X_i)_{i>=1} in [0,1]^infinity. Define

Y_i=X_i-p,  S_n=sum_{i=1}^nY_i,  V_n=sum_{i=1}^nY_i^2,

I=[-1/p,1/(1-p)],  F_n(lambda)=prod_{i=1}^n(1-lambda Y_i).

Let b=min{p,1-p}, c=max{p,1-p}, and define the density q on I minus {0} by

q(lambda)=ln ln(6.6e)/[2lambda ln(6.6e/((1-p)lambda))[ln ln(6.6e/((1-p)lambda))]^2] for 0<lambda<=1/(1-p),

and

q(lambda)=ln ln(6.6e)/[2|lambda|ln(6.6e/(p|lambda|))[ln ln(6.6e/(p|lambda|))]^2] for -1/p<=lambda<0.

Set

F_n=int_I F_n(lambda)q(lambda)d lambda,  F_n^*=sup_{lambda in I}F_n(lambda),  r_n=ln F_n^*-ln F_n.

At time zero, set F_0(lambda)=F_0=1. Choose any maximizer lambda_n^* of F_n(lambda) over I. For alpha in (0,1), let

E_alpha={sup_{n>=1}ln F_n<=ln(1/alpha)}.

For v>=0 define

Lambda_2(v)=ln ln(e^e+v),  Lambda_3(v)=ln ln ln(e^(e^e)+v).

For the probability statements, P is a probability law on [0,1]^infinity, the X_i are the coordinate random variables, and supermartingales are understood with respect to G_n=sigma(X_1,...,X_n), with G_0 trivial, including the transition from time zero.

## Task

Prove the following integrated claim.

For every n>=1, if V_n=0, then r_n=0. If V_n>0, the regret satisfies the corresponding one of these four bounds:

r_n<=2/b^2+1+ln(8/ln ln(6.6e))+ln ln((14ec/b)sqrt(1+V_n))+2ln ln ln((14ec/b)sqrt(1+V_n))

if |S_n|<sqrt(2V_n) and lambda_n^* is interior;

r_n<=1/b^2-ln(ln ln(6.6e)/[4ln(6.6e)[ln ln(6.6e)]^2])

if |S_n|<sqrt(2V_n) and lambda_n^* is on the boundary;

r_n<=1+ln(4/ln ln(6.6e))+ln(20|S_n|/[3sqrt(4|S_n|/3+2V_n)])+ln ln((14e/b)(1+sqrt(V_n)))+2ln ln ln((14e/b)(1+sqrt(V_n)))

if sqrt(2V_n)<=|S_n|<=bV_n/5;

r_n<=(1/2)ln F_n^*+ln4+ln ln(6.6e)+ln ln ln(6.6e)+2ln(2c+5/b)

if sqrt(2V_n)<=|S_n| and bV_n/5<|S_n|.

Moreover, for each alpha in (0,1), there are constants K_alpha,C_1,C_2>0, depending only on p and alpha, such that on E_alpha, for every n,

r_n<=K_alpha+C_1Lambda_2(V_n)+C_2Lambda_3(V_n).

If (F_n)_{n>=0} is a nonnegative supermartingale under P, then P(E_alpha)>=1-alpha.

Finally, on

tilde E={V_n->infinity and limsup_{n->infinity}F_n<infinity},

one has, eventually,

r_n<=ln ln(V_n)(1+o(1)),  S_n/V_n->0,

and

limsup_{n->infinity}|S_n|/sqrt(2V_n ln ln V_n)<=1.

Consequently, if (F_n)_{n>=0} is a nonnegative supermartingale and V_n->infinity almost surely, these three conclusions hold almost surely.
