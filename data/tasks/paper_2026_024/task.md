# Problem

## Setup

Let \(P_0=\mathcal N(\mu_0,\Sigma)\) and \(P_1=\mathcal N(\mu_1,\Sigma)\) be two bivariate Gaussian laws on \(\mathbb R^2\), where \(\mu_j=(\mu_{jX},\mu_{jY})^\top\) and
\[
\Sigma=\begin{pmatrix}s_X^2&r s_Xs_Y\\r s_Xs_Y&s_Y^2\end{pmatrix},
\qquad s_X,s_Y>0,\quad |r|<1.
\]
Consider an independent sequence of examples \(Z_t=(X_t,Y_t)\) that has law \(P_0\) before a fixed change point and law \(P_1\) afterwards. Fix the predictive-oracle conformity measure based on the baseline law,
\[
A(x,y)=f^{(0)}_{Y\mid X}(y\mid x),
\]
the conditional density under \(P_0\). At each time, form a smoothed conformal p-value by taking the randomized rank of the current score \(A(X_t,Y_t)\) among all scores available up to that time, using an independent Uniform[0,1] tie breaker. The resulting p-values are processed by conformal test martingales adapted to their filtration; under IID Uniform[0,1] p-values these martingales constitute the null testing process.

Call \((P_0,P_1)\) \(A\)-cryptic if this conformal transducer continues to output IID Uniform[0,1] p-values when the data law changes from \(P_0\) to \(P_1\). A change point with this property is an \(A\)-cryptic change point.

## Task

Prove that whenever
\[
\mu_{1Y}-\mu_{0Y}=r\frac{s_Y}{s_X}(\mu_{1X}-\mu_{0X}),
\]
the pair \((P_0,P_1)\) is \(A\)-cryptic: the smoothed conformal p-values remain IID Uniform[0,1] across the change, and every conformal test martingale is blind to the change. Equivalently, characterize the admissible post-change means as the affine line
\[
\mu_{1Y}=\mu_{0Y}+r\frac{s_Y}{s_X}(\mu_{1X}-\mu_{0X}),
\]
which permits arbitrarily large mean shifts.
