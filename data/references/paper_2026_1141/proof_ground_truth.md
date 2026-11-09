# Reference Proof

## Proof Structure

1. Derive the two-component Birkhoff ratios from the order-based Hilbert metric on the embedded bicone.
2. Compare those ratios with the extreme logarithms of the generalized eigenvalues of Y^{-1}X, first proving that both Hilbert factors are at least one, and then use the Euclidean-versus-maximum norm inequality.
3. Use scalar pairs approaching the zero boundary to show that the factor 1/sqrt(n) is optimal.
4. Use scalar pairs approaching the identity boundary to show that restricted AIRM can vanish while Hilbert distance stays bounded away from zero.

## Complete Proof

For the embedded points (X,I-X) and (Y,I-Y), let

M_H(X,Y)=inf{t>0: X <= tY and I-X <= t(I-Y)}.

For positive definite A and B, the least t>0 such that A<=tB is
lambda_max(B^{-1/2}AB^{-1/2}), equivalently the largest generalized eigenvalue of B^{-1}A. Since the two components of the product-cone order must satisfy the inequalities simultaneously,

M_H(X,Y)=max{lambda_max(Y^{-1}X), lambda_max((I-Y)^{-1}(I-X))},

and

d_H(X,Y)=log M_H(X,Y)+log M_H(Y,X).

Let lambda_1,...,lambda_n>0 be the generalized eigenvalues of Y^{-1}X and put u_i=log lambda_i. Then

lambda_max(Y^{-1}X)=exp(max_i u_i),

and

lambda_max(X^{-1}Y)=exp(-min_i u_i).

Write R=M_H(X,Y) and S=M_H(Y,X). Each of R and S is at least one. Indeed, if lambda_max(Y^{-1}X)<1, then X<Y, so I-X>I-Y and therefore lambda_max((I-Y)^{-1}(I-X))>1. If lambda_max(Y^{-1}X)>=1, the conclusion is immediate. The same argument with X and Y exchanged proves S>=1.

If max_i u_i>=0, then log R>=max_i u_i and log S>=0. If max_i u_i<0, then log R>=0 and

log S>=log lambda_max(X^{-1}Y)=-min_i u_i.

Consequently,

d_H(X,Y)=log R+log S>=max{max_i u_i,-min_i u_i}=max_i|u_i|.

By definition,

d_AIRM^parallel(X,Y)=(sum_i u_i^2)^{1/2}<=sqrt(n) max_i|u_i|<=sqrt(n)d_H(X,Y).

This proves the stated lower comparison.

For sharpness, fix c>1 and take X_t=tI and Y_t=ctI with 0<t<1/c. Then

d_AIRM^parallel(X_t,Y_t)=sqrt(n)log c.

Moreover,

M_H(X_t,Y_t)=max{1/c,(1-t)/(1-ct)},

and

M_H(Y_t,X_t)=max{c,(1-ct)/(1-t)}.

As t tends to zero, the first quantity tends to one and the second tends to c. Hence d_H(X_t,Y_t) tends to log c, so

d_H(X_t,Y_t)/d_AIRM^parallel(X_t,Y_t) tends to 1/sqrt(n).

Therefore no larger universal constant can replace 1/sqrt(n).

For the reverse direction, take 0<epsilon<1/2 and set

X_epsilon=(1-epsilon)I,  Y_epsilon=(1-2epsilon)I.

Both matrices belong to VPM^o(n). With

r_epsilon=(1-epsilon)/(1-2epsilon),

we have r_epsilon>1 and r_epsilon tends to one. Thus

d_AIRM^parallel(X_epsilon,Y_epsilon)=sqrt(n)log r_epsilon tends to zero.

The direct ratio is r_epsilon, the complementary ratio in that orientation is 1/2, and the two ratios in the reverse orientation are 1/r_epsilon and 2. Therefore

d_H(X_epsilon,Y_epsilon)=log(2r_epsilon),

which tends to log 2>0. A finite universal inequality d_H<=kappa d_AIRM^parallel would contradict this sequence. Hence no finite universal kappa exists.
