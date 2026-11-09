# Problem

## Setup

Let d>=1, D=[0,1]^d with Lebesgue measure, and let C(D) be the real-valued continuous functions on D. For a scalar function h, write h^+=max(h,0) and h^-=max(-h,0). Let rho(t)=max(t,0), applied coordinatewise to vectors. An affine map is a map x |-> Ax+b. A width-m multigrade ReLU residual-sum architecture consists of a sequence of affine maps B_1:R^d->R^m and B_j:R^m->R^m (j>=2), together with scalar affine output maps C_j:R^m->R, where m=5d+1, states z_1=rho(B_1x), z_j=rho(B_jz_{j-1}), and partial outputs F_k(x)=sum_{j=1}^k C_j(z_j). Set r_k=f-F_k and r_0=f. Norms ||.||_p are taken on D for 1<=p<infinity, and ||.||_infinity is the sup norm.

## Task

Prove that for every f in C(D) there exists such an infinite sequence of affine maps, with the first output map C_1 allowed to be zero, for which, for every k>=1 and every x in D,

1. |r_k(x)|<=|r_{k-1}(x)|, and |r_k(x)| tends to 0 uniformly in x;
2. for every finite p, ||r_k||_p<=||r_{k-1}||_p, with strict inequality whenever k>=2 and r_{k-1} and r_k are not both identically zero.

Equivalently, the residual-sum outputs F_k converge uniformly to f while retaining the stated pointwise and finite-L^p monotonicity at every grade; the first grade is only an indexing grade and may leave the residual unchanged.
