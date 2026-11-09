# Problem

## Setup

Let mu and nu be probability measures on R, with nu atomless. Let Y ~ mu, and, independently, let Z_1,...,Z_K be iid samples from nu. Define the rank count

A_K = sum_{i=1}^K 1{Z_i <= Y},

and let p_K(n)=P(A_K=n), n=0,...,K. Let u_K be the uniform probability mass function on {0,...,K}. For a convex lower-semicontinuous generator f:[0,infinity) -> R union {+infinity} with f(1)=0 and positive recession slope f'_infinity=lim_{t->infinity} f(t)/t in (0,+infinity], define

Delta_K(mu)=D_f(p_K || u_K)=(1/(K+1)) sum_{n=0}^K f((K+1)p_K(n)).

Define the continuous divergence by Delta(mu || nu)=integral f(dmu/dnu) dnu when mu << nu, and +infinity otherwise. Write F_nu(y)=nu((-infinity,y]), and define the generalized quantile q_nu(u)=inf{y in R:F_nu(y)>=u} for 0<u<1; it pushes Lebesgue measure on (0,1) to nu. When mu << nu, define rho(u)=(dmu/dnu)(q_nu(u)) for Lebesgue-almost every u in (0,1). The regularity assumptions on rho below mean that this almost-everywhere function admits a continuous representative extending to [0,1], and refer to that extension.

## Task

Prove that for every integer K >= 0, Delta_K is convex as a functional of mu; if F_nu is continuous, it is weakly lower semicontinuous; and

Delta_K(mu) <= Delta_{K+1}(mu) <= Delta(mu || nu).

Moreover, if mu << nu, rho is continuous on [0,1], and f is Lipschitz on the range of rho, then Delta_K(mu) -> Delta(mu || nu). Quantitatively, under these same assumptions, for constants independent of K >= 1:

- if rho is Holder with exponent alpha in (0,1], then 0 <= Delta-Delta_K <= C K^(-alpha/2);
- if rho is C^2 on [0,1], then 0 <= Delta-Delta_K <= C K^(-1);
- if rho is Lipschitz and f is C^2 with bounded second derivative on an interval in [0,infinity) containing the range of rho, then 0 <= Delta-Delta_K <= C K^(-1).

Here Delta abbreviates Delta(mu || nu). The constants may depend on f, rho, and their stated regularity bounds, but not on K.
