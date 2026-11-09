# Problem

## Setup

Fix integers d>=1 and K>=2. Let Z be a d-dimensional standard Gaussian with independent coordinates, density phi_d(z)=product_{i=1}^d phi(z_i), where phi and Phi are the one-dimensional Gaussian density and CDF. Let H_n denote the probabilists' Hermite polynomials (H_0=1, H_1(x)=x, H_{n+1}(x)=xH_n(x)-nH_{n-1}(x)), and for a multi-index alpha define |alpha|=sum_i alpha_i, alpha!=product_i alpha_i!, and H_alpha(z)=product_i H_{alpha_i}(z_i).

Let A={alpha in N_0^d: 2<=|alpha|<=K}, choose real coefficients c_alpha, and set
P(z)=1+sum_{alpha in A} c_alpha H_alpha(z),
S=1+sum_{alpha in A} alpha! c_alpha^2.
Define p(z)=phi_d(z)P(z)^2/S.

For n>=0 define
G_0(x)=Phi(x), and G_n(x)=-H_{n-1}(x)phi(x) for n>=1.
For p,q>=0 define
J_{p,q}(x)=sum_{r=0}^{min(p,q)} r! binom(p,r)binom(q,r)G_{p+q-2r}(x).

## Task

Prove that the lower-orthant CDF F(z)=int_{t_i<=z_i for all i} p(t)dt has, for every z in R^d, the explicit finite form

F(z)=1/S [ product_{i=1}^d Phi(z_i)
+2 sum_{alpha in A} c_alpha product_{i=1}^d G_{alpha_i}(z_i)
+sum_{alpha,beta in A} c_alpha c_beta product_{i=1}^d J_{alpha_i,beta_i}(z_i) ].

Conclude that lower-orthant probabilities are obtained by direct evaluation of this expression (and one-dimensional quantiles, when uniquely defined, by inversion).
