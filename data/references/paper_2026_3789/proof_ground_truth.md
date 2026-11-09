# Reference Proof

## Proof Structure

Expand each mode contraction in the local orthogonal coordinates, bound the subset terms and their differences using the stated event, and analyze normalization explicitly. This yields both the affine one-step recursion and a genuine two-point contraction. The self-map condition permits iteration for every nonnegative integer time. Completeness of the coordinate basin and Banach's theorem give the unique fixed point and convergence.

All work is deterministic for a fixed realization in the event. The random-entry assumptions require no further probabilistic input in this proof.

## Constants

Keep proof constants distinct from the single constant in the task. Put

`K_0=2^d`, `K_1=4d 2^d`.

Choose once and for all

`C_d >= max{1, 2K_0, 3K_1+16d K_0}`

and, for example, `c_d=rho_d/2`. These choices depend only on `d`. Throughout the proof write

`h=r/beta`, `q=kappa_aff=kappa_ctr`.

The assumptions give `0<h<=rho_d<=1/4` and `0<q<1`. The additional signal-scale and small-radius assumptions in the public task are retained; the estimates below already follow from the displayed signal-dominance condition and `h<=rho_d`.

## step_001: Coordinate Products

For `U,V in B_r`, write their orthogonal coordinates as `a_j,b_j`, their positive chart coefficients as `alpha_j,alpha'_j`, and put `D=d_loc(U,V)`. Since `sqrt(1-z)>=1-z` for `0<=z<=1`,

`p_i(U):=prod_{j!=i}alpha_j >= prod_{j!=i}(1-||a_j||^2) >= 1-sum_{j!=i}||a_j||^2 >= 1-d rho_d^2 >=3/4`.

For each `j`, rationalization and Cauchy–Schwarz give

`|alpha_j-alpha'_j| = | ||a_j||^2-||b_j||^2 |/(alpha_j+alpha'_j) <= (||a_j||+||b_j||)||a_j-b_j||`,

because `alpha_j+alpha'_j>=2sqrt(1-rho_d^2)>=1`. Telescoping a product over any `J subseteq[d]` therefore gives

`|prod_{j in J}alpha_j-prod_{j in J}alpha'_j| <= d(delta(U)+delta(V))D <=2d h D`.

For `J` empty the difference is zero, and the empty product is one.

## step_002: Exact Mode Expansion

For `S subseteq I_i`, define privately

`A_{i,S}(U)=prod_{j in I_i excluding S}alpha_j`.

Expanding every contracted input `u_j=alpha_j x_j+a_j` by multilinearity gives

`T(u_(-i))=beta p_i(U)x_i+sum_{S subseteq I_i}A_{i,S}(U)W_{i,S}(a_S)`.

Using the scalar and projected-vector maps defined in the task, set

`zeta_i(U)=sum_{S subseteq I_i}A_{i,S}(U)eta_{i,S}(a_S)`,

`g_i(U)=sum_{S subseteq I_i}A_{i,S}(U)H_{i,S}(a_S)`,

` s_i(U)=beta p_i(U)+zeta_i(U)`.

Then

`T(u_(-i))=s_i(U)x_i+g_i(U)`, with `g_i(U) perpendicular to x_i`.

These are derived identities, not assumptions.

## step_003: One-Point and Two-Point Noise Bounds

The event implies

`|eta_{i,empty}|+||H_{i,empty}||<=L`.

For every singleton subset the sum of the two operator norms is at most `L`; for every subset of size at least two it is at most `Theta`. These are consequences of the event's sums of maxima. No interchange of a supremum and a sum is used.

Let `delta=delta(U)`. Since `0<A_{i,S}(U)<=1`, the triangle inequality and multilinearity give

`|zeta_i(U)|+||g_i(U)|| <= L+(d-1)L delta+Theta sum_{k=2}^{d-1} binom(d-1,k)delta^k`.

As `delta<=rho_d<=1`, this is at most

`K_0[L(1+delta)+Theta delta^2]`.

In particular, define

`M=K_0[L(1+h)+Theta h^2]`.

Then `|zeta_i(U)|+||g_i(U)||<=M` uniformly on the basin, and `M<=G_{r,d}(beta)` by the choice of `C_d`.

For differences, let `B` be either `eta_{i,S}` or `H_{i,S}` and let `k=|S|>=1`. Multilinear telescoping gives

`B(a_S)-B(b_S)=sum_{ell=1}^k B(b_{j_1},...,b_{j_{ell-1}},a_{j_ell}-b_{j_ell},a_{j_{ell+1}},...,a_{j_k})`.

Thus

`||B(a_S)-B(b_S)||<=k ||B||_op h^(k-1)D`,

with absolute value for a scalar map. Also,

`A_{i,S}(U)B(a_S)-A_{i,S}(V)B(b_S) = (A_{i,S}(U)-A_{i,S}(V))B(a_S)+A_{i,S}(V)(B(a_S)-B(b_S))`.

Let `B_S=L` for `k=1` and `B_S=Theta` for `k>=2`. Summing the scalar and vector estimates for this subset bounds its contribution to `|zeta_i(U)-zeta_i(V)|+||g_i(U)-g_i(V)||` by

`B_S(2d h^(k+1)+k h^(k-1))D`.

The empty subset contributes at most `2d L h D`. For `k=1` the displayed contribution is at most `(2d+1)L D`; for `k>=2` it is at most `3d Theta h D`, since `h<=1` and `k<=d-1`. There are at most `2^(d-1)` subsets. Consequently, with

`E=K_1(L+Theta h)`,

we have the uniform bound

`|zeta_i(U)-zeta_i(V)|+||g_i(U)-g_i(V)||<=E D`.

In particular, each of its two summands is at most `E D`.

## step_004: Normalization Estimates

For a unit vector `x`, a scalar `s>0`, and `g perpendicular to x`, define privately

`Phi_x(s,g)=(s x+g)/sqrt(s^2+||g||^2)`.

Its orthogonal coordinate is `g/sqrt(s^2+||g||^2)`, so its norm is at most `||g||/s`; its planted coordinate is strictly positive.

Here is the required two-input bound with its derivation. Write `R=sqrt(s^2+||g||^2)`. For a perturbation `v perpendicular to x`,

`D_g Phi_x(s,g)[v]=(I-Phi_x(s,g)Phi_x(s,g)^T)v/R`,

so `||D_g Phi_x(s,g)||<=1/s`. Direct differentiation also gives

`partial_s Phi_x(s,g)=(||g||^2 x-s g)/R^3`,

whose norm is `||g||/R^2<=||g||/s^2`. Let `m=min(s,s')>0` and suppose `||g||,||g'||<=M`. Vary `g` first at fixed `s`, and then vary `s` at fixed `g'`. Along these segments the scalar stays at least `m`, and the vector norm stays at most `M`. Integrating the derivative bounds yields

`||Phi_x(s,g)-Phi_x(s',g')|| <= ||g-g'||/m + M|s-s'|/m^2`.

This in particular supplies the source normalization estimate on its common-small-noise region. Projection onto `x`-orthogonal coordinates cannot increase the norm.

## step_005: Well-Definedness, Affine Recursion, and Self-Map

By step_001, step_003, and signal dominance,

`s_i(U)>=3beta/4-M>=beta/2`,

and

`||g_i(U)||<=M<=beta/4<=s_i(U)/2`.

Therefore every mode contraction is nonzero, and its normalized update has positive planted coordinate. For any two inputs the common-small-noise hypothesis also holds: both orthogonal norms are at most `beta/4`, while both scalar coefficients are at least `beta/2`.

Let `a_i^+` be the orthogonal coordinate of the update. Applying the one-point normalization formula and the sharper, delta-dependent estimate from step_003 gives

`||a_i^+|| <= (2K_0/beta)[L(1+delta(U))+Theta delta(U)^2]`.

Since `delta(U)^2<=h delta(U)` and `C_d>=2K_0`,

`||a_i^+|| <= C_d L/beta + (C_d L/beta+C_d Theta h/beta)delta(U)`.

Taking the maximum over modes proves

`delta(A(U))<=b_beta+kappa_aff delta(U)`.

The assumed self-map inequality now gives

`delta(A(U))<=b_beta+kappa_aff h<=h`.

Together with positivity of the planted coordinates, this proves `A(B_r) subseteq B_r`. Thus every iterate starting in the basin exists and remains there.

## step_006: Genuine Two-Point Contraction and Constant Absorption

For `U,V in B_r`, step_001 and step_003 imply

`|s_i(U)-s_i(V)| <= beta|p_i(U)-p_i(V)|+|zeta_i(U)-zeta_i(V)| <= (2d beta h+E)D`,

and `||g_i(U)-g_i(V)||<=E D`. Apply step_004 with `m>=beta/2` and the bound `M` on both orthogonal noise vectors. After projection,

`||a_i^+(U)-a_i^+(V)|| <= [2E/beta+4M(2d beta h+E)/beta^2]D`.

The scalar-coefficient contribution has not been omitted. Since `M/beta<=1/4`, its part involving `E` satisfies

`4ME/beta^2<=E/beta`.

The remaining coefficient is therefore at most

`3E/beta+8d M h/beta`.

Furthermore,

`M h/beta=K_0[(L/beta)(h+h^2)+(Theta h/beta)h^2] <=K_0[2L/beta+Theta h/beta]`,

using `h<=1`. Hence the full Lipschitz coefficient is at most

`(3K_1+16d K_0)L/beta+(3K_1+8d K_0)Theta h/beta <= C_d L/beta+C_d Theta h/beta = kappa_ctr`.

This verifies the coefficient with the one fixed choice of `C_d`, rather than changing that constant after its appearance in the assumptions. Maximizing over `i` proves

`d_loc(A(U),A(V))<=kappa_ctr d_loc(U,V)`.

The assumption `kappa_ctr<1` makes this a strict contraction. The public `kappa_ctr` is a sufficient upper bound on the contraction coefficient, not an assertion that it equals the source's more detailed normalization expression.

## step_007: Finite-Time Affine Bound

By the self-map property, the affine recursion applies at every nonnegative integer time. Induction gives

`delta(U_t)<=q^t delta(U_0)+b_beta sum_{j=0}^{t-1}q^j`.

For `t=0` the sum is empty and equals zero. Since `0<q<1`, evaluating the geometric sum yields

`delta(U_t)<=kappa_aff^t delta(U_0)+b_beta(1-kappa_aff^t)/(1-kappa_aff)`.

Consequently,

`limsup_{t to infinity}delta(U_t)<=b_beta/(1-kappa_aff)`.

This limit statement is justified because the self-map property has already established the recursion for all times, not merely a finite segment.

## step_008: Completeness, Fixed Point, and Convergence

The standard independent result used here is Banach's contraction theorem: if a nonempty complete metric space `(X,d)` admits a self-map `f` with `d(f(x),f(y))<=q d(x,y)` for some `0<=q<1`, then it has a unique fixed point `x_star`, and `d(f^t(x),x_star)<=q^t d(x,x_star)` for every nonnegative integer `t`.

All its hypotheses hold. The basin is nonempty because it contains the planted tuple. In orthogonal coordinates it is isometric to

`product_i {a_i in x_i perpendicular: ||a_i||<=h}`

with the maximum product norm. Each factor is a closed ball in a finite-dimensional Euclidean subspace, so the product is complete. Since `h<1`, the positive square-root chart is a bijection onto `B_r`; thus the spherical basin with `d_loc` is also complete. Step_005 establishes the self-map property, and step_006 establishes a contraction coefficient less than one.

Banach's theorem therefore gives a unique `U_star in B_r` and, for every basin initialization,

`d_loc(U_t,U_star)<=kappa_ctr^t d_loc(U_0,U_star)`.

All planted coordinates of `U_star` are positive by the definition of the basin. Applying the affine inequality to the fixed point itself gives

`delta(U_star)<=b_beta+kappa_aff delta(U_star)`.

Rearranging proves

`delta(U_star)<=b_beta/(1-kappa_aff)`.

The exact floor retains its dependence on both `L` and the contraction margin. Along a parameter sequence it is `O(1/beta)` if `L` is bounded and `1-kappa_aff` is bounded below by a positive constant; no unconditional uniform asymptotic rate is inferred merely from `kappa_aff<1`.

## Closure Check

The coordinate estimates, subset expansion, one-point and two-point noise estimates, normalization derivatives, affine recursion, contraction-coefficient absorption, and geometric summation have all been derived explicitly. The only named external result is the standard independent Banach theorem, whose relevant statement and every hypothesis are given above. There is no unresolved specialized dependency. The argument also covers zero noise contractions, coincident inputs, a planted initialization, `t=0`, and modes of dimension one without dividing by a coordinate error or by a two-point distance.
