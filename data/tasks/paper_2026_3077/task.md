# Problem

## Setup

Let d>=1 be an integer, sigma>0, and z in R^d. Let e~N(0,sigma^2 I_d). For each measurable f:R^d->R with E[f(z+e)^2]<infinity, write

g(y)=E[f(y+e)],    y in R^d.

Here g denotes the smoothed function associated with the particular f under consideration.

Fix a finite real C>=0 and G in R^d. Define F(C,G) to be the class of these measurable, nominally square-integrable functions satisfying

Var(f(z+e))<=C,    nabla g(z)=G.

Assume F(C,G) is nonempty; equivalently, assume

C>=sigma^2||G||_2^2.

Perturbations are measured in the Euclidean norm.

## Task

Prove the following integrated claim. For every finite R>=0,

sup_{||delta||_2<=R} sup_{f in F(C,G)} |g(z+delta)-g(z)|=Phi(R),

where

Phi(R)=sqrt(C-sigma^2||G||_2^2) sqrt(exp(R^2/sigma^2)-1-R^2/sigma^2)+R||G||_2.

For a fixed delta with r=||delta||_2>0, a function maximizing the signed shift g(z+delta)-g(z) over F(C,G) is

f_delta^*(x)=m+G^T(x-z)+k_delta[exp(delta^T(x-z)/sigma^2-r^2/(2sigma^2))-1-delta^T(x-z)/sigma^2],

with arbitrary m in R and

k_delta=sqrt((C-sigma^2||G||_2^2)/(exp(r^2/sigma^2)-1-r^2/sigma^2)).

Moreover, on the radius-R sphere an optimizer for the absolute shift may be chosen as delta=R G/||G||_2 when ||G||_2>0; if G=0, every direction gives the same optimized value.

For any finite tolerance epsilon>=0, every f in F(C,G) and every ||delta||_2<=R have prediction shift at most epsilon if and only if Phi(R)<=epsilon. Define the certified-radius endpoint by

R_cert=sup{R>=0:Phi(R)<=epsilon},

with value +infinity if this set of finite radii is unbounded. Prove that R_cert is the supremum of the radii certified uniformly over F(C,G). When R_cert is finite, it is attained and is the largest such radius.
