# Reference Proof

## Proof Structure

Use the continuous ELP interpolation and an auxiliary diffusion whose marginals equal the prescribed annealing densities. Evaluate both adapted drift functionals on the auxiliary path. A localized Girsanov argument and terminal data processing reduce the target to transport energy and a freezing defect. Derive the auxiliary-path moments, increments, and spatial and temporal responsibility estimates explicitly, retaining their dependence on T. Integrating these estimates gives the claimed dimension-uniform bound.

Throughout, work in a fixed dimension d and suppress superscripts when harmless. All constants denoted by c or C below are numerical constants or functions only of the numerical bounds in (A1)–(A7), unless explicitly stated otherwise. They never depend on d, T, the mesh, or the mixture weights. The imported continuous-time annealing theorem is not invoked.

## Step 001: Interpolation and Finite-Dimensional Regularity

Write b_j(t)=\underline s_j+\kappa_t\ell_j and v_{ij}(t)=s_{ij}+\kappa_t\ell_j. For fixed d, let \varphi_{i,t} be the density of \mathcal N(a_i^d,D_{i,t}^d), and define
\[
p_{i,t}(x)=\frac{w_i\varphi_{i,t}(x)}{\pi_t(x)},\qquad s_{i,t,j}(x)=-\frac{x_j-a_{ij}}{v_{ij}(t)}.
\]
Then
\[
\nabla\log\pi_t(x)=\sum_i p_{i,t}(x)s_{i,t}(x),\qquad G_t(x)=\sum_i p_{i,t}(x)c_{i,t}(x),
\]
where
\[
c_{i,t,j}(x)=\alpha_{ij}(t)x_j+\beta_{ij}(t),\quad \alpha_{ij}(t)=\frac{s_{ij}-\underline s_j}{b_j(t)v_{ij}(t)},\quad \beta_{ij}(t)=\frac{a_{ij}}{v_{ij}(t)}.
\]
The lower covariance bounds, upper covariance bounds, and bounded component means imply, for fixed d, locally uniform bounds on the Gaussian densities and each of their required spatial and time derivatives, uniformly over i and t. Since \sum_iw_i=1, differentiation of the countable mixture is justified by locally uniform domination. Thus \pi_t is strictly positive and smooth, and its score is locally Lipschitz in x, uniformly on compact time-state sets. The component-score formula also gives a fixed-d linear-growth bound for the score and G_t, uniformly in t. This establishes the needed regularity directly for countable as well as finite mixtures.

The continuous ELP interpolation satisfies, on [t_n,t_{n+1}],
\[
dY_{t,j}=-\frac{g_j}{b_j(t)}Y_{t,j}\,dt+g_jG_{t_n,j}(Y_{t_n})\,dt+\sqrt{2g_j}\,dW_{t,j},\qquad Y_{t_n}=Y_n.
\]
Variation of constants gives exactly the public recursion, coefficients, and innovation variances. Brownian increments on distinct mesh intervals and coordinates give the stated independence. Conversely, this interpolation realizes the public scheme. Its solution is obtained recursively from linear SDEs on the intervals, so it exists uniquely and is nonexplosive for every finite mesh. Since b_j(t),g_j>0, its linear factors satisfy 0<\phi_{n,j}<1.

## Step 002: Auxiliary Marginals and Transport Energy

Define
\[
u_t(x)=\frac{1}{2T}C^d\nabla\log\pi_t(x),
\]
and let Z solve
\[
dZ_t=\{\Gamma^d\nabla\log\pi_t(Z_t)+u_t(Z_t)\}\,dt+\sqrt{2\Gamma^d}\,dW_t,\qquad Z_0\sim\pi_0.
\]
For each fixed d and T, this drift is continuous in time, locally Lipschitz in space, and of at most linear growth. The diffusion matrix is constant and strictly positive. The standard finite-dimensional SDE well-posedness theorem therefore gives a unique nonexplosive strong solution. We also use the corresponding standard Fokker–Planck uniqueness statement: under these conditions, the probability solution with the prescribed initial distribution and finite second moments is unique and equals the SDE marginal law. Its hypotheses hold here by the same linear-growth bound and the finite moments of the initial Gaussian mixture.

Differentiating the Gaussian convolution gives
\[
\partial_t\pi_t=-\frac{1}{2T}\operatorname{div}(C^d\nabla\pi_t).
\]
In the Fokker–Planck equation, the score drift \Gamma^d\nabla\log\pi_t cancels the diffusion term \operatorname{div}(\Gamma^d\nabla\pi_t), and the remaining transport drift produces precisely the displayed derivative. The smooth mixture densities have finite moments, so uniqueness yields
\[
\mathcal L(Z_t)=\pi_t,\qquad \mathcal L(Z_T)=\pi_*^d.
\]

For later estimates, introduce only private notation:
\[
q_j=\overline s_j+\ell_j+\overline a_j^2,\quad \delta_j=\overline s_j-\underline s_j,\quad A_j=\frac{\delta_j}{\underline s_j^2},\quad M_j=\frac{\overline a_j}{\underline s_j},
\]
\[
R_j=\frac{\Delta a_j}{\underline s_j}+\overline a_jA_j,\quad D_j=\frac{\ell_j\delta_j}{\underline s_j^3},\quad F_j=\frac{\ell_j\overline a_j}{\underline s_j^2}.
\]
Set
\[
Q=\sum_jq_j,\quad K=\sum_jg_j,\quad L=\sum_j\frac{g_j^2q_j}{\underline s_j^2},\quad U=\sum_jg_jA_j^2,\quad V=\sum_jg_jM_j^2,
\]
\[
P_A=\sum_jA_j^2q_j,\quad P_R=\sum_jR_j^2,\quad D_0=\sum_jD_jq_j,\quad D_1=\sum_jg_jD_j^2q_j,
\]
\[
R_{\rm tm}=\sum_j\frac{\ell_j^2R_j^2}{\underline s_j^2},\quad F_2=\sum_jg_jF_j^2,\quad H=\sum_j\frac{\ell_j^2}{g_j\underline s_j}.
\]
These are finite and controlled by the public numerical bounds. In particular,
\[
P_R\le2\sum_j\frac{\Delta a_j^2}{\underline s_j^2}+2P_A,
\]
and R_tm is at most twice the first sum in (A6). Also \sup_jg_j\le K and \sum_j\ell_j^2/\underline s_j\le KH.

By Jensen's inequality for the responsibilities, followed by p_{i,t}(x)\pi_t(x)=w_i\varphi_{i,t}(x),
\[
\mathbb E_{\pi_t}|\partial_j\log\pi_t|^2\le\sum_iw_i\mathbb E_{\varphi_{i,t}}\frac{(X_j-a_{ij})^2}{v_{ij}(t)^2}=\sum_i\frac{w_i}{v_{ij}(t)}\le\frac1{b_j(t)}\le\frac1{\underline s_j}.
\]
Consequently, for
\[
J_d(T)=\frac14\mathbb E\int_0^T\|\Gamma^{-1/2}u_t(Z_t)\|^2\,dt,
\]
we have
\[
J_d(T)\le\frac1{16T}\sum_{j=1}^d\frac{\ell_j^2}{g_j\underline s_j}.
\]
A fourth-moment estimate is also needed. Jensen gives
\[
\mathbb E\|u_t(Z_t)\|^4\le\frac1{16T^4}\sum_iw_i\mathbb E_{\varphi_{i,t}}\|C^ds_{i,t}(X)\|^4.
\]
Under component i the vector inside the last expectation is centered Gaussian, with coordinate variances \ell_j^2/v_{ij}(t). Its fourth moment is at most three times the square of the sum of these variances. Thus
\[
\mathbb E\|u_t(Z_t)\|^4\le\frac{3(KH)^2}{16T^4}.
\]

## Step 003: Localized Path-Space Entropy

Let P be the path law of Z and Q_ELP the path law of the ELP interpolation. On [t_n,t_{n+1}), their adapted drift functionals are
\[
b_t^P(\omega)=-\Gamma B_t^{-1}\omega_t+\Gamma G_t(\omega_t)+u_t(\omega_t),
\]
\[
b_t^Q(\omega)=-\Gamma B_t^{-1}\omega_t+\Gamma G_{t_n}(\omega_{t_n}).
\]
Both functionals are progressively measurable; in particular, the frozen value is evaluated on the same canonical path as the current value. Along Z define
\[
\Delta_t=\Gamma^{1/2}\{G_t(Z_t)-G_{t_n}(Z_{t_n})\},\qquad A_t^{\rm tr}=\Gamma^{-1/2}u_t(Z_t).
\]
The weighted drift mismatch is A_t^{tr}+\Delta_t. It is not a defect evaluated under the ELP law.

Here is the localization argument, including its limit justification. Let
\[
\beta_t=\frac1{\sqrt2}\Gamma^{-1/2}(b_t^P-b_t^Q)(Z),\qquad \tau_m=\inf\left\{t:\int_0^t\|\beta_r\|^2dr\ge m\right\}\wedge T.
\]
The stopped exponential
\[
E_m=\exp\left(-\int_0^{\tau_m}\beta_t\cdot dW_t-\frac12\int_0^{\tau_m}\|\beta_t\|^2dt\right)
\]
is a true martingale density, since its quadratic variation is bounded by m. This is the stopped form of the standard Girsanov theorem: under the probability with density E_m, W_t+\int_0^{t\wedge\tau_m}\beta_rdr is Brownian and Z has drift b^Q until \tau_m. The initial distribution is unchanged because the density has conditional expectation one given the initial sigma field. Recursive uniqueness of the ELP equation identifies the stopped path law with the stopped Q_ELP law.

Write S_m for canonical stopping at \tau_m. Data processing and the zero expectation of the stopped stochastic integral give
\[
\mathrm{KL}(P\circ S_m^{-1}\|Q_{\rm ELP}\circ S_m^{-1})\le\frac14\mathbb E_P\int_0^{\tau_m}\|A_t^{\rm tr}+\Delta_t\|^2dt.
\]
The integrability on the right follows from the transport estimate and the nonlinear growth and marginal moments derived below: \mathbb E\int\|\Delta_t\|^2dt<\infty.

For fixed d,T, the canonical integrand is bounded on every continuous path: its range is compact, the coefficients are uniformly locally bounded in time, and there are finitely many mesh intervals. Thus the canonical total energy is finite on every continuous path, under both P and Q_ELP. It follows that S_m(\omega) converges uniformly to \omega under both laws. The stopped laws therefore converge weakly to the full laws. Lower semicontinuity of relative entropy under weak convergence of both probability arguments gives the full-path inequality. Equivalently, apply the variational formula for KL to each bounded continuous path functional and pass to the limit before taking the supremum. No assertion about uniform integrability of the unstopped exponential is needed.

Using \|a+b\|^2\le2\|a\|^2+2\|b\|^2 now gives the correctly normalized comparison
\[
\mathrm{KL}(P\|Q_{\rm ELP})\le2J_d(T)+\frac12\mathbb E\int_0^T\|\Delta_t\|^2dt.
\]
Terminal data processing gives the same upper bound for \mathrm{KL}(\pi_*^d\|\mathcal L(Y_N^d)).

## Step 004: Uniform Moments, Increments, and Freezing Estimates

### Marginal Moments and Auxiliary Increments

For a Gaussian vector m+\eta with diagonal covariance D, elementary Gaussian moments give
\[
\mathbb E\|\eta\|^4\le3(\operatorname{Tr}D)^2,\qquad \mathbb E\|\eta\|^8\le105(\operatorname{Tr}D)^4.
\]
The second estimate follows by Minkowski in L^4 applied to \sum_j\eta_j^2 and the identity \mathbb E|\eta_j|^8=105D_{jj}^4. Combining these with \|m+\eta\|^q\le2^{q-1}(\|m\|^q+\|\eta\|^q), and averaging over the components, yields
\[
\sup_{d,t,T}\mathbb E\|Z_t\|^q\le c_qQ^{q/2},\qquad q=2,4,8.
\]
Also, uniformly in j,d,t,T,
\[
(\mathbb E|Z_{t,j}|^8)^{1/4}\le c q_j.
\]
The last bound remains valid for every component separately. No independence of coordinates under the unconditional mixture is used.

The affine coefficients obey
\[
0\le\alpha_{ij}(t)\le A_j,\quad |\beta_{ij}(t)|\le M_j,\quad |\dot\alpha_{ij}(t)|\le\frac{2D_j}{T},\quad |\dot\beta_{ij}(t)|\le\frac{F_j}{T}.
\]
These follow by differentiating b_j and v_{ij}, whose derivatives are both -\ell_j/T. In particular,
\[
\sup_i\|\Gamma^{1/2}c_{i,t}(x)\|\le K_c(x):=\sqrt{2V}+\sqrt{2U}\|x\|,
\]
and convexity gives the same bound for \|\Gamma^{1/2}G_t(x)\|.

Under any component, \Gamma B_t^{-1}X is Gaussian. Its squared mean and covariance trace are each bounded by L, so
\[
\mathbb E\|\Gamma B_t^{-1}Z_t\|^4\le c L^2.
\]
Furthermore,
\[
\|\Gamma G_t(x)\|\le\sqrt K K_c(x).
\]
The marginal fourth moment and the transport fourth moment therefore give, for the auxiliary drift b_t^P,
\[
\mathbb E\|b_t^P(Z)\|^4\le B_0+B_1/T^4,
\]
where B_0,B_1 depend only on the public bounds.

For r=t-s, integrate the auxiliary SDE and use Jensen and Gaussian fourth moments of the Brownian increment:
\[
\mathbb E\|Z_t-Z_s\|^4\le C\{(1+T^{-4})r^4+K^2r^2\}\le C(1+T^2+T^{-2})r^2,
\]
since r\le T. Consequently,
\[
\|Z_t-Z_s\|_{L^4}^2\le C(1+T+T^{-1})(t-s).
\]
All hypotheses used for this increment bound remain in force in the following spatial estimate.

### Spatial Freezing

Pairwise component-score differences satisfy
\[
|s_{i,t,j}(x)-s_{l,t,j}(x)|\le A_j|x_j|+R_j.
\]
Let \mathcal A_d(x)=(\sum_{j\le d}A_j^2x_j^2)^{1/2}. Then
\[
\|s_{i,t}(x)-s_{l,t}(x)\|\le\sqrt2\mathcal A_d(x)+\sqrt{2P_R}.
\]
Indeed, the reciprocal-variance difference is at most A_j, while
\[
\left|\frac{a_{ij}}{v_{ij}}-\frac{a_{lj}}{v_{lj}}\right|\le\frac{\Delta a_j}{\underline s_j}+\overline a_jA_j=R_j.
\]
Differentiating the responsibilities yields
\[
\nabla p_{i,t}=p_{i,t}\left(s_{i,t}-\sum_l p_{l,t}s_{l,t}\right),\qquad \sum_i\|\nabla p_{i,t}(x)\|\le\sqrt2\mathcal A_d(x)+\sqrt{2P_R}.
\]
Integration along the segment joining x and y, and the triangle inequality for \mathcal A_d, imply
\[
\sum_i|p_{i,t}(x)-p_{i,t}(y)|\le\{\sqrt2\mathcal A_d(x)+\sqrt2\mathcal A_d(y)+\sqrt{2P_R}\}\|x-y\|.
\]
Splitting G_t(x)-G_t(y) into affine-correction and responsibility increments therefore gives
\[
\|\Gamma^{1/2}(G_t(x)-G_t(y))\|\le\sqrt U\|x-y\|+K_c(y)\{\sqrt2\mathcal A_d(x)+\sqrt2\mathcal A_d(y)+\sqrt{2P_R}\}\|x-y\|.
\]
Minkowski and the coordinate eighth-moment bound give
\[
\|\mathcal A_d(Z_r)\|_{L^8}^2\le\sum_{j\le d}A_j^2\|Z_{r,j}\|_{L^8}^2\le cP_A.
\]
Also K_c(Z_s) has a uniformly bounded L^8 norm. Apply Hölder with exponents (4,4,2) to the square of the responsibility product, and use the L^4 increment estimate. The affine term is controlled by U\mathbb E\|Z_t-Z_s\|^2. Thus
\[
\mathbb E\|\Gamma^{1/2}(G_t(Z_t)-G_t(Z_s))\|^2\le C_{\rm sp}(1+T+T^{-1})(t-s).
\]

### Temporal Freezing

Set \zeta_{i,r}(x)=\partial_r\log\varphi_{i,r}(x). Direct differentiation gives
\[
\zeta_{i,r}(x)=\frac1{2T}\sum_{j\le d}\ell_j\left[\frac1{v_{ij}(r)}-\frac{(x_j-a_{ij})^2}{v_{ij}(r)^2}\right].
\]
Expanding the difference between components uses the bounds
\[
\left|v_{ij}^{-2}-v_{lj}^{-2}\right|\le\frac{2\delta_j}{\underline s_j^3},\quad \left|a_{ij}v_{ij}^{-2}-a_{lj}v_{lj}^{-2}\right|\le\frac{2R_j}{\underline s_j},
\]
\[
\left|a_{ij}^2v_{ij}^{-2}-a_{lj}^2v_{lj}^{-2}\right|\le\frac{2\overline a_jR_j}{\underline s_j}.
\]
With \mathcal D_d(x)=\sum_{j\le d}D_jx_j^2, Cauchy–Schwarz consequently gives
\[
|\zeta_{i,r}(x)-\zeta_{l,r}(x)|\le\frac1T\{H_0+H_1\|x\|+\mathcal D_d(x)\},
\]
where one can take
\[
H_0=\tfrac12D_0+\sqrt{Q R_{\rm tm}},\qquad H_1=2\sqrt{R_{\rm tm}}.
\]
Here \sum_j\ell_jA_j=\sum_jD_j\underline s_j\le D_0, and \sum_j\ell_j\overline a_jR_j/\underline s_j\le\sqrt{Q R_{\rm tm}}.

The responsibility derivative identity
\[
\partial_rp_{i,r}=p_{i,r}\left(\zeta_{i,r}-\sum_l p_{l,r}\zeta_{l,r}\right)
\]
then implies
\[
\sum_i|p_{i,t}(x)-p_{i,s}(x)|\le\frac{t-s}{T}\{H_0+H_1\|x\|+\mathcal D_d(x)\}.
\]
For the affine part of G_t(x)-G_s(x), the coefficient derivative bounds give
\[
\mathbb E\left\|\Gamma^{1/2}\sum_i p_{i,t}(Z_s)\{c_{i,t}(Z_s)-c_{i,s}(Z_s)\}\right\|^2\le C\frac{(t-s)^2}{T^2}(D_1+F_2).
\]
For the responsibility part, its norm is at most
\[
\frac{t-s}{T}K_c(Z_s)\{H_0+H_1\|Z_s\|+\mathcal D_d(Z_s)\}.
\]
Minkowski gives
\[
\|\mathcal D_d(Z_s)\|_{L^4}\le\sum_{j\le d}D_j\|Z_{s,j}\|_{L^8}^2\le cD_0.
\]
The marginal moment bounds and Hölder therefore control the square of this product uniformly. Combining the two contributions yields
\[
\mathbb E\|\Gamma^{1/2}(G_t(Z_s)-G_s(Z_s))\|^2\le C_{\rm tm}\frac{(t-s)^2}{T^2}.
\]
All component sums above are justified directly by nonnegative summation, the locally dominated derivative formulas, and the displayed envelope bounds. The estimates apply without a restriction on the number of mixture components.

## Step 005: Mesh Integration and Conclusion

On [t_n,t_{n+1}), split \Delta_t into its spatial and temporal parts. The preceding estimates give
\[
\mathbb E\|\Delta_t\|^2\le2C_{\rm sp}(1+T+T^{-1})(t-t_n)+\frac{2C_{\rm tm}}{T^2}(t-t_n)^2.
\]
Hence
\[
\mathbb E\int_0^T\|\Delta_t\|^2dt\le C_{\rm sp}(1+T+T^{-1})\sum_nh_n^2+\frac{2C_{\rm tm}}{3T^2}\sum_nh_n^3.
\]
For every finite mesh,
\[
\sum_nh_n^2\le Th_{\max},\qquad \sum_nh_n^3\le h_{\max}\sum_nh_n^2\le T^2h_{\max}.
\]
Thus the freezing energy is bounded by
\[
\left[C_{\rm sp}(1+T+T^2)+\frac{2C_{\rm tm}}3\right]h_{\max}.
\]
Combining this with Step 003 and the transport estimate gives
\[
\mathrm{KL}(\pi_*^d\|\mathcal L(Y_N^d))\le\frac1{8T}\sum_{j=1}^d\frac{\ell_j^2}{g_j\underline s_j}+\left[\frac{C_{\rm sp}}2(1+T+T^2)+\frac{C_{\rm tm}}3\right]h_{\max}.
\]
Since T\le(1+T^2)/2, a permissible positive constant is
\[
C_{\rm disc}=1+\frac34C_{\rm sp}+\frac13C_{\rm tm}.
\]
It depends only on the public numerical summability bounds and gives the requested discretization term C_disc(1+T^2)h_max for every T>0. No factor depending on T is absorbed into a T-independent constant.

Finally the finite partial annealing sum is bounded by H. Taking the supremum over d, with the same T and mesh, proves the dimension-uniform consequence. For any positive prescribed tolerances, selecting T with H/(8T)\le\varepsilon_ann and then a mesh with C_disc(1+T^2)h_max\le\varepsilon_disc gives the asserted sum of tolerances.

## Proof-Obligation Audit

The interpolation identity, fixed-dimensional analytic closure, auxiliary marginal identity, transport second and fourth moments, marginal moments, auxiliary drift and increment estimates, spatial and temporal responsibility estimates, stopped entropy comparison and its limit, and mesh integration have all been derived above or supplied by the explicitly stated standard finite-dimensional SDE/Fokker–Planck and stopped-Girsanov results with their hypotheses verified. There is no remaining specialized external dependency or unresolved proof obligation.
