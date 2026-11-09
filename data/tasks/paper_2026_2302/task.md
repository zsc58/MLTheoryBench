# Problem

## Setup

Let \((X_t,Y_t)_{t\ge1}\) have inputs in a measurable space \(\mathcal X\) and responses in \(\mathbb R^d\), where \(d\ge1\). Let \(f:\mathcal X\to\mathbb R^d\) be a measurable regression function, and let \(\widehat f\) be a measurable predictor fitted on a separate training sample. Define the true and estimated residuals by
\[
\varepsilon_t=Y_t-f(X_t),\qquad
\widehat\varepsilon_t=Y_t-\widehat f(X_t).
\]
All probabilities below refer to their joint training, calibration, and test experiment.

Assume that \((\varepsilon_t)_{t\ge1}\) is stationary. For every integer \(j\ge0\), define
\[
\alpha_\varepsilon(j)=\sup_{n\ge1}\sup_{\substack{A\in\sigma(\varepsilon_1,\ldots,\varepsilon_n)\\ C\in\sigma(\varepsilon_{n+j},\varepsilon_{n+j+1},\ldots)}}
\left|\Pr(A\cap C)-\Pr(A)\Pr(C)\right|,
\]
and assume
\[
\sum_{j=0}^{\infty}\alpha_\varepsilon(j)\le M<\infty.
\]

Let \(k\) be a measurable positive-definite kernel on \(\mathbb R^d\), with feature map \(\phi\) into an RKHS \(\mathcal H\), satisfying \(k(z,z)\le B^2\) for every \(z\), where \(B>0\). Assume the feature random elements are strongly measurable. The population mean and covariance
\[
\mu=\mathbb E\phi(\varepsilon_t),\qquad
\Sigma=\mathbb E[(\phi(\varepsilon_t)-\mu)\otimes(\phi(\varepsilon_t)-\mu)]
\]
are known and used in the score. For a fixed \(\lambda>0\), define
\[
S(z)=\langle\phi(z)-\mu,(\Sigma+\lambda I)^{-1}(\phi(z)-\mu)\rangle_{\mathcal H}.
\]
Let \(F_S\) be the CDF of \(S(\varepsilon_t)\), and assume that for a constant \(L>0\),
\[
|F_S(u)-F_S(v)|\le L|u-v|\qquad(u,v\in\mathbb R).
\]

For calibration indices \(1,\ldots,T\) and test index \(T+1\), assume \(T\ge2\) and that a deterministic number \(\delta_T\ge0\) satisfies, almost surely,
\[
\frac1T\sum_{t=1}^T\|\phi(\widehat\varepsilon_t)-\phi(\varepsilon_t)\|_{\mathcal H}^2\le\delta_T^2,
\qquad
\|\phi(\widehat\varepsilon_{T+1})-\phi(\varepsilon_{T+1})\|_{\mathcal H}\le\delta_T.
\]

Fix \(\alpha\in(0,1)\), put \(\widehat S_t=S(\widehat\varepsilon_t)\), and define
\[
\widehat F_T(u)=\frac1T\sum_{t=1}^T\mathbf1\{\widehat S_t\le u\},\qquad
m=\lceil(1-\alpha)(T+1)\rceil.
\]
If \(m\le T\), let
\[
\widehat q_{1-\alpha}=\inf\{u\in\mathbb R:\widehat F_T(u)\ge m/T\};
\]
if \(m=T+1\), set \(\widehat q_{1-\alpha}=+\infty\). Define
\[
\widehat{\mathcal C}_{T,\alpha}(x)=
\{y\in\mathbb R^d:S(y-\widehat f(x))\le\widehat q_{1-\alpha}\}.
\]

## Task

Prove that, with probability at least \(1-(M(\log T)^2/(2T))^{1/3}\),
\[
\left|\Pr\{Y_{T+1}\in\widehat{\mathcal C}_{T,\alpha}(X_{T+1})\}-(1-\alpha)\right|
\le16(M/2)^{1/3}(\log T)^{2/3}T^{-1/3}
+4(L+1)\left(\sqrt{4B\delta_T/\lambda}+4B\delta_T/\lambda\right).
\]
The coverage probability in this display is unconditional, integrating over training, calibration, and test randomness; it is not conditional on the calibration data or the test input.

Moreover, suppose \(\delta_T=O(T^{-\rho})\) for some \(\rho>0\) and \(\lambda=T^{-\beta}\). Assume the hypotheses hold along this sequence with the same constants \(B,M,L\). Prove that the marginal coverage error is \(O(T^{-1/3}(\log T)^{2/3})\) when \(\rho>2/3\) and \(0<\beta<\rho-2/3\), and is \(O(T^{(\beta-\rho)/2})\) when \(0<\rho\le2/3\) and \(0<\beta<\rho\), with the same probability statement.
