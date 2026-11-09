# Problem

## Setup

Let T>0, let d,n be positive integers, and let D be an open subset of R^d. Let X be a continuous, nonexplosive, well-posed Markov Ito diffusion satisfying

dX_t = b(t,X_t) dt + sigma(t,X_t) dW_t,

with initial probability law p_data. Here W is n-dimensional Brownian motion in the filtration to which X is adapted, b takes values in R^d, and sigma takes values in R^(d by n). Assume X_t belongs to D almost surely at positive times. The initial law need not have a density and may be supported on the closure of D.

For 0<t<=T, suppose X_t has a density p(t,x), positive on D. On (0,T) times D, assume b and sigma are continuous with continuous spatial derivatives through order two, and p has a continuous time derivative and continuous spatial derivatives through order two. Define

a(t,x) = sigma(t,x) sigma(t,x)^T,

s(t,x) = grad_x log p(t,x),

and use the row-divergence convention

(div_x a(t,x))_i = sum_(j=1)^d partial_(x_j) a_ij(t,x).

The local conditional-integrability assumption is the following. For each 0<t<T and p(t,.)-almost every x in D, there is a delta with 0<delta<t such that

E[sup_(r in [t-delta,t]) (||X_r|| + ||b(r,X_r)|| + tr a(r,X_r) + ||div_x a(r,X_r)|| + ||a(r,X_r)s(r,X_r)||) | X_t=x] < infinity.

Norms of vectors are Euclidean. Conditional expectations are regular conditional expectations, and their versions and almost-everywhere assertions are understood with respect to the law of the conditioning state. No global invertibility of a is assumed; its inverse is used only at states where it exists.

In the one-dimensional specialization, take D=(0,infinity), nu>0, and

dX_t = 2(nu+1) dt + 2 sqrt(X_t) dW_t,

with initial probability law p_data on [0,infinity) and X_t>0 at positive times. Use the same interior smoothness and local conditional-integrability conventions. Let I_nu denote the modified Bessel function of the first kind of order nu. For fixed t,x>0, the function

z -> sqrt(z) I_(nu+1)(sqrt(xz)/t) / I_nu(sqrt(xz)/t)

is defined at z=0 by its continuous value zero. Thus an atom of p_data at zero is allowed.

## Task

Prove that, for each 0<t<T and p(t,.)-almost every x in the interior state space:

1. The conditional backward-increment limit exists and

   a(t,x) s(t,x) + div_x a(t,x)

   = b(t,x) + lim_(epsilon down to 0) epsilon^(-1) E[X_(t-epsilon)-X_t | X_t=x].

   At states where a(t,x) is invertible, this is equivalently

   s(t,x) = a(t,x)^(-1) (b(t,x) + lim_(epsilon down to 0) epsilon^(-1) E[X_(t-epsilon)-X_t | X_t=x] - div_x a(t,x)).

2. For the squared-Bessel specialization, the marginal score is

   s(t,x) = nu/x - 1/(2t)

   + (1/(2t sqrt(x))) E[sqrt(X_0) I_(nu+1)(sqrt(x X_0)/t) / I_nu(sqrt(x X_0)/t) | X_t=x],

   with the zero-initial-state convention specified above.
