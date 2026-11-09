# Problem

## Setup

Let d be a positive integer. Fix a real-valued, bounded, compactly supported orthonormal scaling function phi on R, associated with a multiresolution system, whose integer translates are orthonormal and for which int_R phi(x) dx=1. For an integer j>=1, define phi_{-j,k}(x)=2^{j/2}phi(2^j x-k) and Phi_{-j,k}(x)=prod_{r=1}^d phi_{-j,k_r}(x_r), for k in Z^d. Let

I(j)={k in Z^d: supp(Phi_{-j,k}) is contained in [0,1]^d}, and n=|I(j)|.

Consider scales for which n>=1. For this fixed scaling function, n is comparable to 2^{dj} on these scales, with comparison constants depending only on phi and d. On R^d with Lebesgue reference measure, let S be the projection determinantal point process with kernel

K_j(x,y)=sum_{k in I(j)} Phi_{-j,k}(x)Phi_{-j,k}(y).

For a test function f, set Lambda_S(f)=sum_{Y in S} f(Y).

Fix s in (0,1]. A test function f:R^d->R is bounded, vanishes outside U=(0,1)^d, and belongs either to the global Holder class C^{0,s}(R^d) or to H^s(U). In the Holder case use

|f|_{C^{0,s}}=sup_{x neq y in R^d}|f(x)-f(y)|/||x-y||^s.

In the Sobolev case, f|_U belongs to L^2(U); for 0<s<1 use

|f|_{H^s(U)}^2=int_U int_U |f(x)-f(y)|^2/||x-y||^{d+2s} dx dy,

and for s=1 assume f|_U has an L^2 weak gradient and use |f|_{H^1(U)}=||nabla f||_{L^2(U)}.

## Task

Prove that one constant C, depending only on d and the fixed scaling function, satisfies, for every s in (0,1], every admissible scale j, and every test function in either specified class,

Var[Lambda_S(f)] <= C |f|_s^2 n^{1-2s/d},

where |f|_s denotes the seminorm for the applicable class above. The conclusion is required separately for the Holder and Sobolev classes.
