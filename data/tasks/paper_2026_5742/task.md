# Problem

## Setup

Let `S` be a finite state space, and let `(Z_t)_(0<=t<=T)` be a time-inhomogeneous continuous-time Markov chain with generator `K_t`, initial law `mu_0`, and marginal law `mu_t`. Fix an interior window `0<t1<t2<T`. For each `x` with `mu_t1(x)>0`, write `mu_(0|t1)(.|x)` for the conditional law of `Z_0` given `Z_t1=x`.

For distinct `x,y` with `mu_t(x)>0`, define the marginal reverse rate

`a_t(x,y) = K_t(y,x) mu_t(y)/mu_t(x)`.

Let `P` be the law of the noising trajectory on `[t1,t2]`; equivalently, it has endpoint law `mu_t2` and reverse rates `a_t` on states of positive `mu_t`-mass. For each `z` with `mu_0(z)>0`, let `N_z` be the conditional law of that trajectory given `Z_0=z`.

Let `nu_t2` be another probability distribution on `S`, let `b_t(x,y)` be nonnegative reverse rates, and let `R` be the path law obtained by starting with `nu_t2` at time `t2` and running backward with rates `b_t`. Let `d(.|x)` be a probability distribution on `S` for each `x`; it serves as a decoder at the lower endpoint.

For `u,v>=0`, define

- `Phi(u,v)=v-u+u log(u/v)` if `u,v>0`;
- `Phi(0,v)=v`;
- `Phi(u,0)=+infinity` if `u>0`.

Assume that the reverse rates `a_t` on the support of `mu_t` and the rates `b_t` are bounded and measurable, and that `mu_t2 << nu_t2`. Assume that, for Lebesgue-almost every `t` and all distinct `x,y` with `mu_t(x)>0`,

`a_t(x,y)>0` implies `b_t(x,y)>0`.

Assume also

`integral_[t1,t2] E_(Z_t~mu_t)[sum_(y != Z_t) Phi(a_t(Z_t,y),b_t(Z_t,y))] dt < infinity`,

and, for `mu_t1`-almost every `x`,

`mu_(0|t1)(.|x) << d(.|x)`.

For each `z` with `mu_0(z)>0`, define the finite model slice on path space by

`M_z(dw) = d(z|w(t1)) R(dw)`.

Define the averaged negative path ELBO by

`N = sum_(z: mu_0(z)>0) mu_0(z) integral log(dN_z/dM_z)(w) N_z(dw)`,

and define `H(mu_0)=-sum_z mu_0(z)log(mu_0(z))`, with `0 log 0=0`.

## Task

Prove that

`N - H(mu_0) = E_(x~mu_t1)[KL(mu_(0|t1)(.|x) || d(.|x))] + KL(P || R)`.
