# Problem

## Setup

Fix an integer `d>=1`. Define

`B_+^d={z in R^d: z_k>=0 for every k and ||z||_2<=1}`

and let `Omega=B_+^d x B_+^d`, with coordinate projections `x=(g(x),r(x))`. Let `rho` be a nonnegative Lebesgue density on `Omega` with total mass

`Lambda=integral_Omega rho(x) dx`, where `0<Lambda<infinity`,

and let `mu(dx)=rho(x)dx/Lambda`. Assume neither coordinate marginal of `mu` is supported on a proper linear subspace of `R^d`.

A perennial latent graph model draws `N~Poisson(Lambda)` and, conditional on `N`, draws iid points `X_1,...,X_N~mu`. It retains all `N` labeled vertices, including isolated vertices. Conditional on these points, for every ordered pair `1<=i,j<=N`, including `i=j`, the edge indicator for `i->j` is an independent Bernoulli variable with parameter

`K(X_i,X_j)`, where `K(x,y)=g(x) dot r(y)`.

Thus `0<=K<=1`.

A digraphon is a Borel measurable kernel `V:[0,1]^2->[0,1]`. Its graph law on `n` labeled vertices is obtained by drawing iid uniform labels `T_1,...,T_n` and then, conditional on the labels, sampling independent Bernoulli edge indicators with parameters `V(T_i,T_j)` for every ordered pair, including self-pairs. Two digraphons are weakly equivalent if these graph distributions agree for every `n>=1`.

For a scalar function `f:[0,1]->R`, its total variation is

`Var(f)=sup sum_{j=1}^m |f(t_j)-f(t_{j-1})|`,

where the supremum is over all finite partitions `0=t_0<...<t_m=1`. A kernel `V` is sectionally bounded variation if, for Lebesgue-almost every fixed first coordinate, its section in the second coordinate has finite total variation, and, for Lebesgue-almost every fixed second coordinate, its section in the first coordinate has finite total variation.

Two distinct labels `s,s'` are twins for a kernel `V` if both `V(s,t)=V(s',t)` for almost every `t` and `V(t,s)=V(t,s')` for almost every `t`. The kernel is almost twin-free if there is a single null set outside which no two distinct labels are twins.

Assume the following directed lifting property on standard atomless probability spaces: whenever kernels `U_0` and `W_0` are weakly equivalent and `W_0` is almost twin-free, there exists a measurable measure-preserving map `psi` from the probability space of `U_0` to that of `W_0` such that

`U_0(s,t)=W_0(psi(s),psi(t))`

for product-almost every `(s,t)`. On probability spaces other than `[0,1]`, the sampling and twin definitions use their respective probability measures. A map is measure-preserving when its pushforward is the stated target measure.

## Task

Prove the following integrated theorem. The model admits a digraphon representation: there is a measure-preserving Borel isomorphism `phi:([0,1],Lebesgue)->(Omega,mu)` such that

`W(u,v)=g(phi(u)) dot r(phi(v))`

induces exactly the same graph law as the latent model conditional on every finite vertex count, and hence the same unconditional law when the vertex count on both sides is `Poisson(Lambda)`. Here a Borel isomorphism is a bijection that is Borel measurable and has a Borel measurable inverse. Moreover, every digraphon `U` weakly equivalent to `W` fails to be sectionally bounded variation.
