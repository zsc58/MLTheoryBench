# Reference Proof

## Proof Structure

Establish the Plancherel identity, obtain a uniform deterministic Fourier-tail bound, and control the truncated integral by arbitrary-tag quadrature. Compare exact and empirical grid residuals pointwise for the fitted parameter, then derive the sampling moments at the deterministic nodes and take unconditional expectations.

## Complete Proof

### 1. Integrability and the Fourier Identity

Because g is a probability density in L^infinity,
\[
\|g\|_2^2\le\|g\|_\infty\|g\|_1=\|g\|_\infty<\infty.
\]
Every model is a probability density, and the positive lower scale bounds give the uniform bound
\[
\|\widehat g(\cdot;\theta)\|_\infty
\le D:=\max\left\{\frac1{\sqrt{2\pi}\sigma_-},\frac1{2b_-}\right\}.
\]
Thus every model lies in L^1 intersect L^2, with squared L^2 norm at most D. Plancherel for the convention in the task states that, for h in L^1 intersect L^2 with transform H(eta)=integral exp(i eta x)h(x)dx,
\[
\int|h(x)|^2dx=\frac1{2\pi}\int|H(\eta)|^2d\eta.
\]
Applying it to g minus the model gives, for every theta,
\[
\|g-\widehat g_\theta\|_2^2
=\frac1{2\pi}\int_{\mathbb R}F_\theta(\eta)d\eta,
\qquad F_\theta(\eta)=|\varphi(\eta)-\Phi_\theta(\eta)|^2.
\]
The identity applies samplewise to the fitted parameter. The density formula is jointly measurable in x and theta, so measurable estimator selection makes the integrated error measurable. Moreover, it is bounded by 2||g||_2^2+2D, and hence its expectation is finite.

### 2. Uniform Tail Control and Strictness

Plancherel also gives varphi in L^2. Nonnegative weights summing to one and the lower scale bounds imply
\[
|\Phi_\theta(\eta)|\le S(\eta)
:=e^{-\sigma_-^2\eta^2/2}+(1+b_-^2\eta^2)^{-1}.
\]
The function S^2 is integrable: it is bounded by the sum of twice a Gaussian and twice (1+b_-^2 eta^2)^(-2). Choose a deterministic T>0 sufficiently large that
\[
A(T):=\int_{|\eta|>T}|\varphi(\eta)|^2d\eta<\varepsilon,
\qquad
B(T):=\int_{|\eta|>T}S(\eta)^2d\eta<\varepsilon.
\]
This choice depends only on epsilon, g, and the fixed model bounds, not on the sample, P, or theta. For every theta,
\[
\int_{|\eta|>T}F_\theta(\eta)d\eta
\le\tau(T):=2A(T)+2B(T)<4\varepsilon.
\]
In particular, the strict tail margin is deterministic and uniform over fitted parameters.

### 3. Uniform Lipschitz Control and Arbitrary-Tag Quadrature

Let L_varphi(T) be a Lipschitz constant of varphi on [-T,T]. Differentiating a Gaussian CF component and a Laplace CF component gives, on this interval,
\[
\left|\frac d{d\eta}e^{i\eta\mu-\sigma^2\eta^2/2}\right|
\le H+\sigma_+^2T,
\]
\[
\left|\frac d{d\eta}\frac{e^{i\eta\nu}}{1+b^2\eta^2}\right|
\le H+2b_+^2T.
\]
The weights sum to one, so Phi_theta has a Lipschitz constant bounded uniformly by
\[
D_T=H+T\max\{\sigma_+^2,2b_+^2\}.
\]
Both characteristic functions have modulus at most one. Applying
\[
\big||u|^2-|v|^2\big|\le(|u|+|v|)|u-v|
\]
to u=varphi(eta)-Phi_theta(eta) and v=varphi(xi)-Phi_theta(xi) shows that every F_theta is Lipschitz with the common constant
\[
L_F(T)=4\bigl(L_\varphi(T)+D_T\bigr).
\]
For any training node eta_p in its cell,
\[
\left|\Delta_pF_\theta(\eta_p)
-\int_{\xi_{p-1}}^{\xi_p}F_\theta(\eta)d\eta\right|
\le L_F(T)\int_{\xi_{p-1}}^{\xi_p}|\eta-\eta_p|d\eta
\le\frac{L_F(T)}2\Delta_p^2.
\]
Summing over cells and using Delta_p<=c_1/P yields
\[
\left|\sum_p\Delta_pF_\theta(\eta_p)
-\int_{-T}^TF_\theta(\eta)d\eta\right|
\le\frac{L_F(T)c_1^2}{2P}
\le\frac{C'(T)c_1^2}{P},
\]
where, for example, C'(T)=1+L_F(T)/2 is finite and independent of P, theta, and the sample. No endpoint-node restriction is needed.

Define the exact-grid quantities
\[
\mathrm{MSE}_P^*(\theta)=\frac1P\sum_p|\varphi(\eta_p)-\Phi_\theta(\eta_p)|^2,
\]
\[
R_P^*(\theta)=\frac1P\sum_p\left(
|\Re(\varphi(\eta_p)-\Phi_\theta(\eta_p))|
+|\Im(\varphi(\eta_p)-\Phi_\theta(\eta_p))|\right),
\]
and Loss_P^*(theta)=MSE_P^*(theta)+lambda R_P^*(theta). The weighted sum itself satisfies
\[
\sum_p\Delta_pF_\theta(\eta_p)
\le c_1\,\mathrm{MSE}_P^*(\theta).
\]
Consequently, uniformly in theta,
\[
\int_{-T}^TF_\theta(\eta)d\eta
\le c_1\,\mathrm{MSE}_P^*(\theta)+\frac{C'(T)c_1^2}{P}.
\]
Combining with the tail estimate and applying the result samplewise gives
\[
2\pi\|g-\widehat g_{\widehat\theta}\|_2^2
\le\tau(T)+c_1\,\mathrm{MSE}_P^*(\widehat\theta)
+\frac{C'(T)c_1^2}{P}.
\]

### 4. Pointwise Comparison at the Fitted Parameter

Set
\[
a_p=\varphi(\eta_p)-\Phi_{\widehat\theta}(\eta_p),
\qquad b_p=\widehat\varphi_M(\eta_p)-\varphi(\eta_p).
\]
The empirical residual is a_p+b_p. Pointwise, even though the fitted parameter depends on the sample,
\[
|a_p|^2\le2|a_p+b_p|^2+2|b_p|^2,
\]
and the real/imaginary triangle inequalities give
\[
|\Re a_p|+|\Im a_p|
\le|\Re(a_p+b_p)|+|\Im(a_p+b_p)|
+|\Re b_p|+|\Im b_p|.
\]
Averaging, multiplying the second inequality by lambda>=0, and using nonnegativity of the empirical MAE term yields
\[
\mathrm{Loss}_P^*(\widehat\theta)
\le2\,\mathrm{Loss}_{M,P}(\widehat\theta)
+\frac2P\sum_p|b_p|^2
+\frac\lambda P\sum_p(|\Re b_p|+|\Im b_p|).
\]
This argument does not apply a fixed-parameter expectation identity to a data-dependent minimizer.

### 5. Sampling Moments at Deterministic Nodes

For each fixed node, put Z_m=exp(i eta_p X_m). Then E Z_m=varphi(eta_p), |Z_m|=1, and
\[
\mathbb E|Z_m-\varphi(\eta_p)|^2=1-|\varphi(\eta_p)|^2.
\]
Independence makes the off-diagonal centered cross moments vanish. Since b_p is the average of these centered variables,
\[
\mathbb E|b_p|^2
=\frac{1-|\varphi(\eta_p)|^2}{M}.
\]
Also,
\[
\mathbb E(|\Re b_p|+|\Im b_p|)
\le\sqrt2\,\mathbb E|b_p|
\le\sqrt{2\,\mathbb E|b_p|^2}
=\sqrt{\frac2M}\sqrt{1-|\varphi(\eta_p)|^2}.
\]
Thus V_P and W_P are well defined and nonnegative. Taking unconditional expectations in the pointwise loss comparison and using the assumed almost-sure loss bound gives
\[
\mathbb E\,\mathrm{MSE}_P^*(\widehat\theta)
\le\mathbb E\,\mathrm{Loss}_P^*(\widehat\theta)
\le2\varepsilon_1+\frac{2V_P}{M}
+\lambda\sqrt{\frac2M}\,W_P.
\]
No independence between the fitted parameter and the sample is required.

### 6. Combination

Taking expectations in the Fourier bound yields
\[
2\pi\,\mathbb E\|g-\widehat g_{\widehat\theta}\|_2^2
\le\tau(T)+c_1\left(2\varepsilon_1+\frac{2V_P}{M}
+\lambda\sqrt{\frac2M}\,W_P\right)
+\frac{C'(T)c_1^2}{P}.
\]
Because tau(T)<4 epsilon, this proves the required strict inequality. All estimates also cover lambda=0, zero individual mixture weights, a component family with count zero, and P=1 whenever the stated mesh conditions hold.

## Alternative Proof Note

A complete proof may omit the exact MAE comparison and instead use
\[
\mathrm{MSE}_P^*(\widehat\theta)
\le2\,\mathrm{MSE}_{M,P}(\widehat\theta)+\frac2P\sum_p|b_p|^2
\le2\varepsilon_1+\frac2P\sum_p|b_p|^2.
\]
This gives the stronger expected bound with training/sampling term 2 epsilon_1+2V_P/M. Adding the nonnegative displayed lambda term proves the requested conclusion. Such a proof is fully valid and does not need to derive the dispensable W_P contribution.
