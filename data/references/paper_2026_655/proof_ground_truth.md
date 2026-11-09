# Reference Proof

## Proof Structure and Obligations

The obligations are: (i) derive the exact Kac--Rice representation and pass to the full domain; (ii) establish the Gaussian derivative laws and kernel identities; (iii) normalize while preserving both the count and the counting density; (iv) compute the normalized gradient density and bound conditional Hessian moments; (v) control the adjugate, integrate the multiplier, prove spatial integrability, and collect degree powers. All are closed below.

The standard independent results used are the local Kac--Rice zero-count theorem under the stated local hypotheses; Wick's formula, which expresses a centered Gaussian product moment as the sum over pairings of products of covariances; Gaussian regression; and Gaussian closure under mean-square limits. Specifically, for a centered jointly Gaussian pair (Y,Z) with invertible covariance C_ZZ, the law of Y given Z=z has mean C_YZ C_ZZ^(-1)z and covariance C_YY-C_YZ C_ZZ^(-1)C_ZY. For a smooth covariance kernel, difference quotients converge in mean square and their covariances converge to the corresponding kernel derivatives. All kernels differentiated below are smooth, and the conditioning covariance is explicitly shown to be invertible.

## 1. Kac--Rice reduction

Let D=R^n times (R without {0}) and F(x,lambda)=(f(x),x-xi+lambda grad f(x)). Its Jacobian is

J_F = [[grad f(x)^T,0],[I_n+lambda Hess f(x),grad f(x)]].

For any matrix A and vector v, expansion of the bordered determinant gives

|det [[v^T,0],[A,v]]| = |v^T adj(A)v|.

This is a polynomial identity and does not require A to be invertible. Thus it applies with A=I_n+lambda Hess f(x).

The local Kac--Rice theorem states that the expected zero count on a relatively compact open region U is the integral of p_F(0) E[|det J_F| | F=0]. Its hypotheses are precisely the local regularity, nondegeneracy, conditional regularity, and integrability stipulated in the problem. The affine change from (f,grad f) to F has determinant lambda^n. Consequently,

p_F(0)=|lambda|^(-n)p_(f,grad f)(0,(xi-x)/lambda),

and conditioning on F=0 is equivalent to conditioning on f=0 and grad f=(xi-x)/lambda. Substitution proves the desired representation on U. Use the increasing exhaustion U_j={||x||<j, 1/j<|lambda|<j}, for integers j>=2. Monotone convergence of counts and nonnegative integrals proves the global representation, initially allowing infinity.

## 2. Kernel and derivative identities

Put a_d=(2d-1)!!, with (-1)!!=1. For a centered Gaussian pair X,Y with variances q(x),q(y) and covariance r(x,y), Wick's formula groups pairings by the number s of X-X pairs, which also equals the number of Y-Y pairs. Their number is

binom(d,2s)^2 ((2s-1)!!)^2 (d-2s)! = c(s,d).

It follows that the given kernel is E[X^dY^d]. In particular, its diagonal is a_d q(x)^d and sum_s c(s,d)=a_d. The coefficient relation

(d-2s)c(s,d)=d^2 c(s,d-1)

holds when d-2s>=1. When d is even, the terminal term on the left is zero and is omitted on the right. With the empty-pairing convention c(0,0)=1, this also covers d=1. Summing gives

sum_s (d-2s)c(s,d)=d^2(2d-3)!!,

sum_s s c(s,d)=d(d-1)(2d-3)!!/2.

Because the kernel is polynomial, the mean-square differentiation rule applies through every derivative order needed here. The assumed path derivatives agree with these mean-square derivatives at each fixed point, by uniqueness of limits in probability. Therefore (f,grad f,Hess f) is jointly Gaussian and its covariances are the appropriate kernel derivatives.

Symmetry gives grad_x K|_(y=x)=one half of the derivative of K(x,x), hence

grad_x K|_(y=x)=d a_d q^(d-1)x/n.

For the mixed derivative, write k=d-2s. Direct product-rule differentiation of each summand, evaluated at y=x, gives the xx^T coefficient

[4s^2+4sk+k(k-1)]/n^2=[d(d-1)+2s]/n^2,

multiplying q^(d-2), and the identity coefficient k/n, multiplying q^(d-1). Summing gives

grad_x grad_y^T K|_(y=x)
=2d^2(d-1)(2d-3)!! q^(d-2)xx^T/n^2
 +d^2(2d-3)!! q^(d-1)I_n/n.

This calculation avoids the erroneous off-diagonal expansion in the source and proves its stated diagonal formula. For d=1 the first term is zero and the second is I_n/n.

## 3. Normalization and transport of the integral

Let s(x)=sqrt(a_d)q(x)^(d/2) and g=f/s. The factor s is smooth and strictly positive. On f=0, grad f=s grad g. Therefore (x,lambda) is a critical pair for f if and only if (x,t), with t=s(x)lambda, is a critical pair for g. This is a bijection of the full domains with nonzero multipliers.

There is also a direct transport of the Kac--Rice density, so no extra unverified applicability assumption for g is needed. Write T(x,t)=(x,t/s(x)) and G(x,t)=(g,x-xi+t grad g). Then

G(x,t)=L(x,t)F(T(x,t)),

where L=[[1/s,0],[-t grad s/s^2,I_n]]. Both det L and det DT equal 1/s. At a zero, the derivative of L multiplying F vanishes, so J_G=L J_F DT. Also p_G(0)=s p_(F(T))(0), and the two conditioning events correspond under this invertible linear map. Thus

p_G(0)E[|det J_G| | G=0]
=s^(-1)p_(F(T))(0)E[|det J_F(T)| | F(T)=0].

The factor s^(-1) is precisely the change-of-variable Jacobian. The already established global integral therefore becomes the same adjugate formula for g with multiplier t.

Define rho(x,y)=r(x,y)/sqrt(q(x)q(y)) and

Phi(z)=a_d^(-1) sum_s c(s,d) z^(d-2s).

The covariance of g is Phi(rho). The coefficients of Phi are nonnegative and sum to one, so Phi(1)=1 and 0<=Phi''(1)<=d^2. The coefficient identities give

alpha=Phi'(1)=d^2/(2d-1), with d/2<=alpha<=d.

These statements include d=1.

## 4. The normalized gradient density

Differentiating rho on the diagonal gives rho=1, both first derivatives zero, and

B(x)=grad_x grad_y^T rho|_(y=x)=I_n/(nq)-xx^T/(n^2q^2).

Thus g(x) is standard normal, independent of grad g(x), and

Sigma(x)=Cov(grad g(x))=alpha B(x).

The eigenvalues of B are 1/(nq) in directions orthogonal to x and 1/(nq^2) in the radial direction. At x=0 all eigenvalues equal 1/n. In particular, B is positive definite everywhere, and

det Sigma=alpha^n/(n^n q^(n+1)),
Sigma^(-1)=(nq/alpha)(I_n+xx^T/n).

The invertible relation f=sg, grad f=s grad g+g grad s also proves that (f,grad f) has a nondegenerate Gaussian law everywhere.

Put u=xi-x,
D_x=||u||^2+(x^T u)^2/n,
beta(x)=nq D_x/(2alpha).

Then, with C_n=(2pi)^(-(n+1)/2)n^(n/2),

p_(g,grad g)(0,u/t)=C_n alpha^(-n/2)q^((n+1)/2)exp(-beta(x)/t^2).

The full quadratic form D_x must be retained; its radial term supplies the required tail decay. For x!=xi, beta(x)>0.

## 5. Conditional Hessian moments

Let H=Hess g(x). A third derivative of rho gives

A_(ij,k)=-[delta_ik x_j+delta_jk x_i]/(n^2q^2)+2x_i x_j x_k/(n^3q^3).

Since first derivatives of rho vanish on the diagonal, the chain rule gives Cov(H_ij,partial_k g)=alpha A_(ij,k). Gaussian regression, using Cov(g,grad g)=0 and conditioning on g=0, gives

M(x,v)=E[H | g=0,grad g=v]=alpha A Sigma^(-1)v
=-(xv^T+vx^T)/(nq).

For the contraction, A_(ij,.)=-(x_j B_(i,.)+x_i B_(j,.))/(nq), which immediately yields the displayed expression. Hence

||M(x,v)||_op <= C_n q^(-1/2)||v||.

For completeness, all derivatives of rho of total order k<=4 on the diagonal are bounded in absolute value by C_(n,k)q^(-k/2). Indeed, repeated differentiation gives |partial^a q^(-1/2)|<=C_(n,a)q^(-(1+|a|)/2). In rho=r q(x)^(-1/2)q(y)^(-1/2), diagonal derivatives of r of order 0,1,2 are respectively O(q), O(sqrt(q)), O(1), and higher derivatives vanish. The product rule gives the claimed bound.

At the diagonal, the fourth derivative of Phi(rho) is

Phi''(1)(rho_ab rho_cd+rho_ac rho_bd+rho_ad rho_bc)+Phi'(1)rho_abcd,

because every other chain-rule term contains a vanishing first derivative of rho. Applying this to two x and two y derivatives yields

|Cov(H_ij,H_kl)|<=C_n d^2 q^(-2).

The Gaussian conditional covariance equals the unconditional covariance minus a positive semidefinite matrix. Thus each entry of the centered conditional residual Z=H-M has variance at most C_n d^2 q^(-2). For a centered scalar Gaussian of variance sigma^2, its m-th absolute moment is sigma^m times the finite m-th absolute moment of a standard normal. Bounding the operator norm by the Frobenius norm and then by the sum of the absolute entries gives, for each integer m>=1,

E[||Z||_op^m | g=0,grad g=v]<=C_(n,m)(d/q)^m.

Using (a+b)^m<=2^(m-1)(a^m+b^m), we obtain

E[||H||_op^m | g=0,grad g=v]
<=C_(n,m)[d^m q^(-m)+q^(-m/2)||v||^m].

For m=0 the moment is one and is handled directly.

## 6. Adjugate estimate and multiplier integration

The singular values of adj(A) are products of n-1 singular values of A. Consequently,

||adj(I_n+tH)||_op <= (1+|t| ||H||_op)^(n-1).

This includes n=1, where the adjugate is the scalar 1 and the product is empty. Taking v=u/t, expanding the binomial, and applying the conditional moment estimates yields

I_g(x,t)<=C_n sum_(m=0)^(n-1)[d^m q^(-m)||u||^2 |t|^(m-2)+q^(-m/2)||u||^(m+2)|t|^(-2)].

The m=0 terms are interpreted directly as constant zeroth moments. Combining this with the density gives

E N_xi <= C_n sum_(m=0)^(n-1)(A_(m,d)+B_(m,d)),

where

A_(m,d)=alpha^(-n/2)d^m integral_R^n q^((n+1-2m)/2)||u||^2 [integral_(R without {0}) |t|^(m-n-2)exp(-beta/t^2)dt]dx,

B_(m,d)=alpha^(-n/2) integral_R^n q^((n+1-m)/2)||u||^(m+2) [integral_(R without {0}) |t|^(-n-2)exp(-beta/t^2)dt]dx.

All interchanges use nonnegativity. For r>1 and beta>0, evenness and the substitution z=beta/t^2 give

integral_(R without {0}) |t|^(-r)exp(-beta/t^2)dt
=Gamma((r-1)/2) beta^(-(r-1)/2).

Here r=n-m+2>=3 for the A-family and r=n+2>=3 for the B-family. The formula is applied only for x!=xi. At x=xi the original conditional adjugate factor is zero because v=0; this measure-zero spatial set does not affect the integral.

Substituting beta=nqD_x/(2alpha), define

J_m(xi)=integral_R^n q^(-m/2)||u||^2 D_x^(-(n-m+1)/2)dx,

K_m(xi)=integral_R^n q^(-m/2)||u||^(m+2)D_x^(-(n+1)/2)dx.

Their integrands can be assigned any value at x=xi. Then

A_(m,d)<=C_(n,m)alpha^((1-m)/2)d^m J_m(xi),
B_(m,d)<=C_(n,m)alpha^(1/2)K_m(xi).

In particular, the second contribution uses K_m, not a second copy of J_m.

## 7. Spatial integrability and degree growth

Near x=xi, q is bounded above and below by positive constants and D_x>=||u||^2. Both integrands are bounded by C_(n,xi,m)||u||^(m-n+1). With polar volume factor r^(n-1), the local integral is bounded by a constant times integral_0^delta r^m dr, which is finite for every m>=0.

For R=||x||>=2||xi||+2, we have ||u||<=3R/2 and

|x^T u|>=R^2/2,
D_x>=R^4/(4n),
q>=R^2/n.

The J_m integrand is therefore bounded by C_(n,xi,m)R^(-2n+m), and the K_m integrand by C_(n,xi,m)R^(-2n). Their radial integrals are bounded respectively by integrals of R^(-n+m-1) and R^(-n-1). Since 0<=m<=n-1 and n>=1, both converge. On the remaining compact set away from xi, the integrands are continuous. Thus every J_m(xi) and K_m(xi) is finite and independent of d.

For m=0, alpha^((1-m)/2)d^m=sqrt(alpha)<=sqrt(d). For 1<=m<=n-1,

alpha^((1-m)/2)d^m <= 2^((m-1)/2)d^((m+1)/2).

Also sqrt(alpha)<=sqrt(d). The finitely many terms therefore give

E N_xi <= C_(n,xi)d^(n/2),

with C_(n,xi) independent of d. This proves the asserted finiteness and rate. When n=1 only m=0 occurs, so the same argument applies without a Hessian moment estimate. The conventions and estimates already specified cover d=1 as well.

## Audit Notes

The source-local repairs are the product-rule correction for the intermediate off-diagonal derivative expansion, restoration of K_m in the final B contribution, and use of alpha<=d rather than alpha>=d/2 for the positive-exponent m=0 contribution. No assumptions or targets have been changed to obtain the bound. No proof obligation remains open.
