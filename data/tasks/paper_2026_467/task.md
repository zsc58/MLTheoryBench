# Problem

## Setup

Fix `epsilon>0` and `h>0`, and put `rho=exp(-epsilon)` and `B=2h`. Two labeled datasets are label-neighbors when they differ only in one response value. A randomized dataset mechanism is epsilon label differentially private if, for every such pair `D,D'` and every measurable event `E`,

`P(A(D) in E) <= exp(epsilon) P(A(D') in E)`.

Let `p` be a probability density supported on `[n_0,n_k]`, where

`n_0<n_1<...<n_k`,

and suppose `p(y)=alpha_i` on `[n_i,n_{i+1})`, with `alpha_i>=0` (the last interval may be closed at `n_k`).

For an interval `I=[a,b]`, define

`N_y=[y-h,y+h]`, `N_I=[a-h,b+h]`, and `G(a,b)=B+rho(b-a)`.

For this fixed interval, consider conditional densities `r(t | y)`, `y in I`, which are supported on `N_I`, integrate to one, and have a common constant `v>0` such that `r(t | y)=v` for almost every `t in N_y`. Require moreover that, for almost every `t`, simultaneously for all `y,y' in I`,

`r(t | y) <= exp(epsilon) r(t | y')`.

Their prior-weighted neighborhood objective is

`J_I(r)=integral_a^b p(y)[integral_{N_y}r(t | y)dt]dy`.

Define

`F(a,b)=[B/G(a,b)]integral_a^b p(y)dy`.

The following finite candidate set will be used to select an interval. For `i<j`, set

`H_ij=alpha_i n_{i+1}+integral_{n_{i+1}}^{n_j}p(s)ds-alpha_j n_j`.

Start with the four endpoint pairs in

`{n_i,n_{i+1}} x {n_j,n_{j+1}}`.

If `alpha_i != alpha_j`, also admit

`a_ij=[B alpha_j-rho H_ij]/[rho(alpha_j-alpha_i)]`,

`b_ij=[B alpha_i-rho H_ij]/[rho(alpha_j-alpha_i)]`,

and check every pair in

`({n_i,n_{i+1}} union {a_ij}) x ({n_j,n_{j+1}} union {b_ij})`

that belongs to the cell and satisfies `a<=b`. For `i=j`, check the three vertices of

`{(a,b): n_i<=a<=b<=n_{i+1}}`.

Let `S` be the union of these candidates over all `0<=i<=j<k`, and choose `(a*,b*) in S` maximizing `F`. Write `I*=[a*,b*]` and let `pi_I(y)=min(max(y,a),b)` denote projection onto `I`.

For any interval `I=[a,b]`, define the full response kernel

`r_I(t | y)=1/G(a,b)` if `t in N_{pi_I(y)}`,

`r_I(t | y)=rho/G(a,b)` if `t in N_I minus N_{pi_I(y)}`,

and `r_I(t | y)=0` outside `N_I`.

The corresponding dataset mechanism independently replaces each response by a draw from this kernel and leaves all features unchanged.

## Task

Prove the following integrated theorem.

1. For every fixed `I=[a,b]`, the largest possible value of `J_I` is `F(a,b)`. It is attained, for `y in I`, by the two-level density `1/G(a,b)` on `N_y`, `rho/G(a,b)` on `N_I minus N_y`, and zero outside `N_I`.

2. The finite search is globally exact:

`max_{a<=b}F(a,b)=max_{(a,b) in S}F(a,b)`.

3. The dataset mechanism formed from the selected kernel `r_{I*}` is epsilon label differentially private.
