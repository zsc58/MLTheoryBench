# Problem

## Setup

Fix a time index `t` and a step size `h>0`. Let `p(.,t)` be a strictly positive differentiable probability density on `R^d`, and suppose an exact score oracle is available:
`s(x,t)=nabla_x log p(x,t)`.

From a current state `x`, draw a Gaussian Langevin proposal `y` with density
`q(y|x)=N(y; x+(h/2)s(x,t), h I_d)`.
Define
`H(x,y)=q(x|y)/q(y|x)` and `r(x,y)=p(y,t)/p(x,t)`.
For `v=y-x`, define the score line integrand
`I_{x,y}(u)=<s(x+uv,t),v>`, `0<=u<=1`.
Let `C:R^d x R^d -> [0,infinity)` be a known finite-valued Borel-measurable function such that, for every pair `(x,y)`,
`|I_{x,y}(u)|<=C(x,y)` for all `u in [0,1]`.
When `C(x,y)=0`, use the degenerate convention specified below.

Given `(x,y)`, the score-only correction repeatedly performs outer trials, keeping the pair and its bound fixed. Set
`alpha'=1/(1+H(x,y) exp(C(x,y)))`.
In each trial, return REJECT immediately with probability `alpha'`. Otherwise generate a product coin as follows: if `C=C(x,y)>0`, sample `N~Poisson(2C)`, independently sample iid `U_j~Uniform[0,1]`, form
`W=product_{j=1}^N [1/2+I_{x,y}(U_j)/(2C)]`,
with the empty product equal to one, and toss a Bernoulli coin with conditional success parameter `W`; if `C=0`, let this product coin succeed deterministically. Return ACCEPT when the product coin succeeds. If it fails, restart the outer trial for the same pair `(x,y)`.

Conditional on `(x,y)`, use independent random variables for the initial rejection flips, Poisson counts, uniform locations, and uniforms realizing the product-coin flips, with fresh variables on every restart. At each Markov-chain iteration, draw a fresh proposal and run a fresh correction. On ACCEPT the next state is `y`; on REJECT the next state is `x`. Keep `t` and `h` fixed throughout the chain.

## Task

Prove that, under these assumptions, the correction terminates almost surely and accepts `y` with probability
`alpha_B(x,y)=H(x,y)r(x,y)/(1+H(x,y)r(x,y))`.
Consequently, the Markov chain obtained by iterating the Gaussian proposal followed by this correction is reversible with invariant density `p(.,t)` and converges to `p(.,t)` in total variation from every initial state.
