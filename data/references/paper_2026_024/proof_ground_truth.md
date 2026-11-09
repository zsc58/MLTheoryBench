# Reference Proof

## Proof Structure

1. Compute the conditional Gaussian law under the common covariance and show that the mean-shift condition makes the conditional laws under the two regimes identical.
2. Use the resulting residual representation to prove that the predictive-oracle conformity scores have the same (indeed IID continuous) distribution before and after the change.
3. Apply smoothed conformal validity to the score sequence and conclude that the p-values remain IID Uniform[0,1].
4. Conclude from the definition of crypticity and the martingale testing setup that every conformal test martingale is blind to the change.

## Complete Proof

Write
\[
\Sigma=\begin{pmatrix}s_X^2&r s_Xs_Y\\r s_Xs_Y&s_Y^2\end{pmatrix},
\qquad s_X,s_Y>0,
\qquad |r|<1,
\]
so that \(\Sigma\) is positive definite. For \(j\in\{0,1\}\), if \((X,Y)\sim P_j=\mathcal N(\mu_j,\Sigma)\), the conditional distribution of \(Y\) given \(X=x\) is Gaussian with variance
\[
v=(1-r^2)s_Y^2
\]
and mean
\[
m_j(x)=\mu_{jY}+r\frac{s_Y}{s_X}(x-\mu_{jX}).
\]
The predictive-oracle score fixed from the baseline law is therefore
\[
A(x,y)=\frac{1}{\sqrt{2\pi v}}\exp\!\left(-\frac{(y-m_0(x))^2}{2v}\right).
\]

Assume
\[
\mu_{1Y}-\mu_{0Y}=r\frac{s_Y}{s_X}(\mu_{1X}-\mu_{0X}).
\]
Rearranging gives \(m_1(x)=m_0(x)\) for every real \(x\). The conditional variances are already equal because the covariance matrix is common. Hence \(Y\mid X=x\) has the same Gaussian law under \(P_0\) and \(P_1\).

More explicitly, under either regime we may write
\[
Y=m_0(X)+\varepsilon,
\qquad \varepsilon\sim\mathcal N(0,v),
\]
with \(\varepsilon\) independent of \(X\). Consequently
\[
A(X,Y)=\frac{1}{\sqrt{2\pi v}}\exp\!\left(-\frac{\varepsilon^2}{2v}\right),
\]
whose distribution is the same in both regimes and is continuous. Since the observations are independent within the pre- and post-change segments, the entire score sequence is IID with this common distribution, even though the marginal distribution of \(X\) (and hence the joint law of \((X,Y)\)) may change.

For each time, the smoothed conformal p-value is the randomized rank of the current score among the scores seen up to that time (with an independent uniform tie breaker). IID continuous scores are exchangeable, so the standard smoothed conformal validity theorem yields IID \(\operatorname{Uniform}[0,1]\) p-values. This remains true across the change point because the score law did not change. Thus \((P_0,P_1)\) is \(A\)-cryptic by definition.

A conformal test martingale adapted to the p-value filtration is therefore operating under exactly its IID-uniform null law both before and after the change. Its distribution, and the Ville-type false-alarm guarantee for threshold crossings, are unchanged by the shift; there is no systematic post-change signal for any such martingale. Hence every conformal test martingale is blind to this change. The admissible post-change means form the affine line
\[
\mu_{1Y}=\mu_{0Y}+r\frac{s_Y}{s_X}(\mu_{1X}-\mu_{0X}),
\]
which contains shifts of arbitrarily large magnitude.
