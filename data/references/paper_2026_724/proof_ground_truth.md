# Reference Proof

## Proof Structure and Audited Obligations

The proof uses a Sobolev generator, an explicit spectral-to-ReLU representation, independent cost-weighted sampling on time intervals, and joint estimates for the map and log-Jacobian. The following obligations are closed below:

1. Existence of a near-minimizing generator and action-controlled flow, inverse, and log-Jacobian bounds.
2. A measurable normalized ReLU representation with explicit cost bounds and a globally controlled mean extension.
3. Correct sampling normalization, including zero-cost intervals.
4. A conditional map-error estimate that does not incorrectly center a sample-dependent remainder.
5. An almost-everywhere log-Jacobian identity and a closed martingale estimate for its error.
6. Conversion of map and log-Jacobian error into global TV, including mass outside the original support.
7. Simultaneous deterministic selection, uniform action dependence, integer rounding, and the zero-action case.

The specialized Barron embedding cited by the source is not used as an unexplained proof obligation: its needed special case is derived by Fourier inversion and the elementary ReLU Taylor identity below. Sampled trajectories need not remain in the representation ball. The global mean extension avoids that unsupported assertion.

## 1. Generator and deterministic flow estimates

Put A=A_s(Φ). Choose U∈L²([0,1];H^s) generating Φ such that
\[
E^2:=\int_0^1\|U_t\|_{H^s}^2dt\le A+1.
\]
Write H(t)=\|U_t\|_{H^s}. All constants denoted by K below depend only on d,s, and the fixed domain or density bounds indicated in context, never on Φ or the chosen generator.

The Sobolev estimates needed here follow directly from Fourier inversion and Cauchy–Schwarz. In particular,
\[
\int_{\mathbb R^d}(1+|\xi|^2)|\widehat U_t(\xi)|d\xi\le K H(t),
\tag{1}
\]
because \(\int(1+|\xi|^2)^{2-s}d\xi<\infty\) when s>d/2+2. Consequently U_t has bounded continuous first and second derivatives, with
\[
\|U_t\|_\infty+\operatorname{Lip}(U_t)+\|\operatorname{div}U_t\|_\infty+\operatorname{Lip}(\operatorname{div}U_t)\le K H(t).
\tag{2}
\]
The relevant standard flow statement is: an integrably bounded, globally spatially Lipschitz time-dependent field has a unique global flow; if its spatial derivative is continuous and integrably bounded, the flow is C¹ and its derivative solves the variational equation. These hypotheses hold by (2) and \(\int H\le E\). Gronwall applied to the variational equation and to the backward flow gives
\[
\operatorname{Lip}(X_t),\operatorname{Lip}(X_t^{-1})\le e^{KE}.
\tag{3}
\]
Also \(|X_t(x)-x|\le KE\). Choose
\[
R=2\left(1+\sup_{x\in\Omega}|x|+KE\right).
\]
Then R≥2, R≤K_Ω(1+E), and all exact trajectories from Ω lie in B(0,R/2).

Jacobi's formula gives, with q_X(t,x)=log det DX_t(x),
\[
q_X(t,x)=\int_0^t\operatorname{div}U_\tau(X_\tau(x))d\tau.
\]
Thus
\[
\|q_X(1)\|_\infty\le KE,\qquad \operatorname{Lip}(q_X(1))\le KEe^{KE}.
\tag{4}
\]
These bounds are global in the initial label x.

## 2. Explicit normalized representation and its global mean

Absorb the Fourier normalization into the coefficients. Fourier inversion represents U_t as an integral of vector coefficients multiplying cos(ξ·x) and sin(ξ·x). The coefficients are measurable in (t,ξ), and (1) controls the integrals of their norms with weights 1+|ξ|².

For f equal to cos or sin and T=R|ξ|, define F_T to equal f on [-T,T] and to continue by the endpoint tangent lines outside that interval. Elementary integration twice gives, for every real z,
\[
F_T(z)=f(-T)+f'(-T)(z+T)+\int_{-T}^{T}f''(v)(z-v)_+dv.
\tag{5}
\]
The affine term is a sum of a constant feature and two ReLU features, using \(z=z_+-(-z)_+\). Moreover F_T is C¹, \(|F_T'|\le1\), and \(\operatorname{Lip}(F_T')\le1\). Formula (5) therefore produces a ReLU representation of a global vector field \(\overline U_t\) that equals U_t on B(0,R), and whose global bounds satisfy
\[
\operatorname{Lip}(\overline U_t)+\|\operatorname{div}\overline U_t\|_\infty+\operatorname{Lip}(\operatorname{div}\overline U_t)\le K H(t).
\tag{6}
\]
Indeed these bounds follow by integrating |ξ| and |ξ|² times the coefficient norms. The global C¹ property follows from dominated differentiation of F_T, whose first derivative is continuous.

Here is the normalization and its quantitative cost. For a nonzero feature w(a·x+b)_+, put
\[
c=|w|(R|a|+|b|),\quad g(x)=\frac{w(a\cdot x+b)_+}{c},\quad h(x)=\frac{(w\cdot a)\mathbf1_{\{a\cdot x+b>0\}}}{c}.
\]
Discard features of cost zero, since their velocity is zero. Each remaining feature satisfies
\[
|g(x)|\le1\quad(|x|\le R),\qquad \operatorname{Lip}(g)\le R^{-1},\qquad |h(x)|\le R^{-1}\quad(x\in\mathbb R^d).
\tag{7}
\]
For one scalar Fourier ridge, the constant, two linear, and integral terms in (5) have total cost at most K(1+T²) times the vector coefficient norm: the integral term is bounded using \(\int_{-T}^T(T+|v|)dv=3T^2\). Hence the resulting positive measure λ_t on normalized features has mass r(t) satisfying
\[
\overline U_t(x)=\int g_\theta(x)d\lambda_t(\theta),\qquad
\operatorname{div}\overline U_t(x)=\int h_\theta(x)d\lambda_t(\theta)\quad\text{for a.e. }x,
\]
\[
r(t)\le KR^2H(t),\qquad P:=\|r\|_{L^2(0,1)}\le KR^2E.
\tag{8}
\]
The construction by (5), including the signs and directions of the Fourier coefficients, supplies a measurable kernel λ_t explicitly; no unproved measurable selection is needed. Differentiation under this representation is valid in the weak, almost-everywhere sense because its first-derivative integrand is bounded by c/R. Fubini and bi-Lipschitz changes of initial labels justify the same identities along the random flows used below.

This step retains the radius dependence that the source suppresses. Since R≤K_Ω(1+E), P is polynomially bounded in E. The global bounds in (6), in contrast, do not grow with R.

## 3. Cost-weighted time sampling

Choose an integer m, set Δ=1/m, t_k=kΔ, and I_k=[t_{k-1},t_k). Define
\[
M_k=\int_{I_k}\lambda_tdt,\qquad r_k=M_k(\text{parameter space}),\qquad H_k=\int_{I_k}H(t)dt.
\]
If r_k>0, independently sample θ_k from M_k/r_k and set
\[
U_m(t,x)=m r_k g_{\theta_k}(x),\qquad t\in I_k.
\tag{9}
\]
If r_k=0, set U_m=0 on I_k. Formula (9) is a single ReLU with a rescaled output vector. It has at most m−1 switches. Its global Lipschitz, linear-growth field has a unique global flow Y_t.

Let \(\mathcal F_{k-1}\) be generated by the preceding samples. The correct centering identities are
\[
\mathbb E[r_kg_{\theta_k}(z)\mid\mathcal F_{k-1}]=\int_{I_k}\overline U_t(z)dt,
\]
and the corresponding divergence identity almost everywhere. The measures and generator are fixed before all samples; θ_k is independent of \(\mathcal F_{k-1}\).

Cauchy–Schwarz gives inequalities, not the source's erroneous equalities:
\[
\sum H_k^2\le E^2/m,\quad \sum H_k^4\le E^4/m^2,\quad
\sum r_k^2\le P^2/m,\quad \sum r_k^4\le P^4/m^2.
\tag{10}
\]
Take
\[
m\ge m_0:=K\left(1+P^2/R^2+P^4/R^4\right).
\tag{11}
\]
In particular r_k/R≤1. This is only a private construction threshold, polynomially bounded by K_Ω(1+E)^8.

## 4. Map-error estimate with the random remainder retained

Write X_k=X_{t_k}, Y_k=Y_{t_k}, and e_k=X_k−Y_k, as functions on Ω. Expand both increments at the start of I_k. Since the exact trajectories lie in the region where \(\overline U=U\),
\[
e_k=e_{k-1}+A_k+\eta_k+D_k,
\]
where
\[
A_k=\int_{I_k}(\overline U_t(X_{k-1})-\overline U_t(Y_{k-1}))dt,
\]
\[
\eta_k=\int_{I_k}\overline U_t(Y_{k-1})dt-r_kg_{\theta_k}(Y_{k-1}),
\]
and D_k is the difference of the within-interval remainders. The global bound (6) gives \(\|A_k\|_2\le KH_k\|e_{k-1}\|_2\).

Conditional centering holds for η_k. Since X_{k-1} lies in B(0,R/2), (7) gives
\[
|g_{\theta}(Y_{k-1}(x))|\le1+|e_{k-1}(x)|/R,
\]
and hence
\[
\mathbb E[\|\eta_k\|_2^2\mid\mathcal F_{k-1}]
\le K_\Omega r_k^2+K r_k^2R^{-2}\|e_{k-1}\|_2^2.
\tag{12}
\]
The exact remainder is bounded pointwise by KH_k². For the sampled remainder, the global Lipschitz constant mr_k/R and an elementary within-step Gronwall estimate yield
\[
|Y_t-Y_{k-1}|\le r_ke^{r_k/R}|g_{\theta_k}(Y_{k-1})|,
\]
\[
\|D_k\|_2\le K_\Omega(H_k^2+r_k^2/R)+K r_k^2R^{-2}\|e_{k-1}\|_2.
\tag{13}
\]
No sampled-path containment is assumed.

D_k depends on θ_k, so its cross term with η_k cannot be discarded by conditional centering. Apply Young's inequality before conditioning:
\[
\|e_k\|_2^2\le(1+\Delta)\|e_{k-1}+A_k+\eta_k\|_2^2+(1+\Delta^{-1})\|D_k\|_2^2.
\]
Only e_{k-1}+A_k is measurable with respect to the preceding samples, and its cross term with η_k does vanish. From (12)–(13), after increasing fixed constants,
\[
\mathbb E\|e_k\|_2^2\le
\exp\!\left(KH_k+K\Delta+Kr_k^2/R^2+Km r_k^4/R^4\right)\mathbb E\|e_{k-1}\|_2^2
+K_\Omega\left(r_k^2+mH_k^4+mr_k^4/R^2\right).
\tag{14}
\]
Summing the exponents with (10)–(11) bounds their total by KE+K. Iteration, for every k≤m, therefore gives
\[
\mathbb E\|e_k\|_2^2\le\frac{K_\Omega e^{KE}}{m}\left(P^2+E^4+P^4/R^2\right).
\tag{15}
\]
Since P≤KR²E and R≤K_Ω(1+E), the parenthesis is bounded by K_Ω E²(1+E)^8.

## 5. Log-Jacobian estimate

A constant ReLU field has a continuous piecewise-affine flow with two affine regions. On the active side, z=a·Y+b solves z'=(a·w)z; on the inactive side it remains unchanged. The sign of z is therefore invariant on an interval. The determinant is exp((a·w)τ) on the active region and 1 on the inactive region. Thus every sampled interval flow, and their finite composition, is an orientation-preserving bi-Lipschitz piecewise-affine map. Its derivative and positive determinant are defined almost everywhere, which suffices for all integrals and changes of variables here.

With q_Y=log det DY, this exact calculation gives
\[
q_Y(t_k,x)-q_Y(t_{k-1},x)=r_kh_{\theta_k}(Y_{k-1}(x))\quad\text{for a.e. }x.
\]
Put δ_k=q_X(t_k)−q_Y(t_k). The global mean extension allows the decomposition
\[
\delta_k=\delta_{k-1}+B_k+\zeta_k+S_k,
\]
where
\[
\|B_k\|_2\le KH_k\|e_{k-1}\|_2,\qquad \|S_k\|_2\le K_\Omega H_k^2,
\]
and
\[
\zeta_k=\int_{I_k}\operatorname{div}\overline U_t(Y_{k-1})dt-r_kh_{\theta_k}(Y_{k-1}).
\]
By independence, the almost-everywhere divergence representation, and the bi-Lipschitz nature of Y_{k-1}, ζ_k is an L²(Ω)-valued martingale difference with
\[
\mathbb E[\|\zeta_k\|_2^2\mid\mathcal F_{k-1}]\le |\Omega|r_k^2/R^2.
\]
Orthogonality of these martingale differences and Minkowski's inequality close the estimate directly:
\[
\bigl(\mathbb E\|\delta_m\|_2^2\bigr)^{1/2}
\le KE\max_{k\le m}\bigl(\mathbb E\|e_k\|_2^2\bigr)^{1/2}
+|\Omega|^{1/2}P/(R\sqrt m)+K_\Omega E^2/m.
\tag{16}
\]
Equations (15)–(16) imply
\[
\mathbb E\left(\|e_m\|_2^2+\|\delta_m\|_2^2\right)
\le K_\Omega e^{KE}E^2(1+E)^{10}/m.
\tag{17}
\]
This explicitly supplies the previously omitted coupled estimate without an unsupported conditional remainder cancellation or an unproved recursion.

## 6. Correct global TV transfer

The required support-local estimate follows from equal mass, not from restricting the full change-of-variables integral to the support. Let η be a bijection for which change of variables holds, and put j=|det Dη|>0 almost everywhere. For ρ supported in ω,
\[
\operatorname{TV}(\mu,\eta_\#\mu)=\int_{\mathbb R^d}|\rho(\eta(x))j(x)-\rho(x)|dx.
\]
Both nonnegative densities in this integral have mass one. Consequently this integral equals twice the negative part, which vanishes outside ω. On ω,
\[
(\rho-\rho(\eta)j)_+
\le |\rho-\rho(\eta)|+\|\rho\|_\infty(1-j)_+
\le L|\eta-x|+B|\log j|,
\]
using \((1-e^a)_+\le|a|\). Therefore
\[
\operatorname{TV}(\mu,\eta_\#\mu)
\le2L\|\eta-\mathrm{id}\|_{L^1(\omega)}+2B\|\log j\|_{L^1(\omega)}.
\tag{18}
\]
This elementary estimate is stronger than the repaired version with a factor e^M, and it applies to the piecewise-affine sampled flows. In particular it avoids introducing an exponential of the polynomially radius-dependent feature cost.

Select one realization with the sum of the squared errors in (17) at most twice its expectation, and denote its terminal map by Ψ. Set η=Φ^{-1}∘Ψ and ω=supp ρ. By (3),
\[
\|\eta-\mathrm{id}\|_{L^1(\omega)}\le |\Omega|^{1/2}e^{KE}\|e_m\|_2.
\]
The almost-everywhere chain rule gives
\[
\log\det D\eta(x)=q_Y(1,x)-q_X(1,\eta(x)).
\]
Thus (4) yields
\[
\|\log\det D\eta\|_{L^1(\omega)}
\le |\Omega|^{1/2}\|\delta_m\|_2+KEe^{KE}\|\eta-\mathrm{id}\|_{L^1(\omega)}.
\]
TV is invariant under the bijection Φ^{-1}. Applying (18) proves simultaneous map and global TV bounds of the form
\[
\|\Psi-\Phi\|_{L^2(\Omega)}+\operatorname{TV}(\Psi_\#\mu,\Phi_\#\mu)
\le K e^{KE}E(1+E)^7/\sqrt m.
\tag{19}
\]
All polynomial factors can be absorbed into a larger fixed exponential: \((1+E)^q\le e^{qE}\). This tracks, rather than suppresses, every action-dependent constant.

## 7. Rate, rounding, and boundary cases

Choose m as the ceiling of a sufficiently large
\[
K e^{KE}(1+E^2)\varepsilon^{-2}.
\]
Increasing K makes this dominate the polynomial threshold (11) and makes each error in (19) at most ε. Since E²≤A+1 and \(\sqrt{A+1}\le1+\sqrt A\), integer rounding and the number m−1 of switches give
\[
\#\text{switches}\le C e^{C\sqrt A}(1+A)\varepsilon^{-2}.
\]
The selected realization establishes both public conclusions simultaneously.

If A=0, generators with energies tending to zero give \(\|\Phi-\mathrm{id}\|_\infty\le K\sqrt{\text{energy}}\), hence Φ=id. The zero field is a width-one control with zero switches and zero errors.

For completeness, the source's sharper displayed A-prefactor is not obtained by absorbing +1 into A. It can instead be recovered by choosing E²≤2A when A>0. Estimate (18), applied directly to Φ and the identity, and the deterministic bounds above show that the zero control already gives both errors at most KE. If ε≥KE, use it. Otherwise E²ε^{-2} is bounded below by a fixed positive constant, so the polynomial threshold and integer rounding are absorbed into \(C e^{CE}E^2\varepsilon^{-2}\). Estimate (19) then proves the sharper source rate. This also verifies that the unchanged public 1+A rate is a valid consequence, including at A=0.

## Quality Status

All seven theorem-critical obligations listed at the start are closed. No private GT quality warning is required.
