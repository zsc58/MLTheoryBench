# Reference Proof

## Proof Structure

Expand the squared Hermite polynomial, integrate the Gaussian, linear-Hermite, and quadratic-Hermite parts separately over the lower orthant, and use coordinate factorization. The quadratic part is reduced coordinatewise with the Hermite product identity, producing the finite functions J.

## Complete Proof

Let A={alpha in N_0^d:2<=|alpha|<=K}. By Gaussian orthogonality, E[H_alpha(Z)]=0 for alpha !=0 and E[H_alpha(Z)H_beta(Z)]=alpha! 1_{alpha=beta}. Hence
S=E[P(Z)^2]=1+sum_{alpha in A} alpha! c_alpha^2,
and p integrates to one.

For z in R^d, integrate p over the lower orthant. Expanding P^2 gives
F_Z(z)=S^{-1}(I_0(z)+I_1(z)+I_2(z)),
where I_0 is the integral of phi_d, I_1 is twice the sum of the integrals of c_alpha H_alpha phi_d, and I_2 is the sum over alpha,beta of c_alpha c_beta H_alpha H_beta phi_d.

Since phi_d(t)=prod_i phi(t_i), the orthant integral factors by coordinate. Thus
I_0(z)=prod_i Phi(z_i).
For the linear term, the one-dimensional identity
int_{-infinity}^{x} phi(t)H_n(t)dt=G_n(x)
(with G_0=Phi and G_n=-H_{n-1}phi for n>=1) yields
I_1(z)=2 sum_{alpha in A} c_alpha prod_i G_{alpha_i}(z_i).

For the quadratic term, in coordinate i apply
H_p(t)H_q(t)=sum_{r=0}^{min(p,q)} r! binom(p,r)binom(q,r)H_{p+q-2r}(t).
After integration, the i-th coordinate contributes
J_{p,q}(z_i)=sum_{r=0}^{min(p,q)} r! binom(p,r)binom(q,r)G_{p+q-2r}(z_i).
Independence and Fubini therefore give
I_2(z)=sum_{alpha,beta in A} c_alpha c_beta prod_i J_{alpha_i,beta_i}(z_i).
Substitution of I_0,I_1,I_2 into the expansion proves the stated closed form for every z. Because it is a finite expression in Gaussian CDF/density and Hermite polynomials, lower-orthant probabilities are obtained by direct evaluation, and one-dimensional quantiles (when uniquely defined) by inversion.
