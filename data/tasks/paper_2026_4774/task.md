# Problem

## Setup

Fix a parameter value \(\theta\) and a prompt \(x\). Let \(Y\sim\pi_\theta(\cdot\mid x)\) and let \(Z\) be its terminal reward. Assume \(|Z|\le M\) almost surely, \(\mathbb E\|S(Y)\|^2<\infty\), differentiation may be interchanged with expectation, and
\[
S(Y):=\nabla_\theta\log\pi_\theta(Y\mid x),\qquad \mathbb E[S(Y)]=0.
\]
Write \(V:=\mathbb E[Z\mid x]\) and \(g:=\mathbb E[S(Y)Z\mid x]\). For an integer \(G\ge2\), draw iid copies \((Y_i,Z_i)_{i=1}^G\), and set \(S_i=S(Y_i)\). Define
\[
\widehat g_{\rm loo}:=\frac1G\sum_{i=1}^G S_i\left(Z_i-\frac1{G-1}\sum_{j\ne i}Z_j\right),
\]
and the oracle estimator \(\widehat g_{\rm or}:=G^{-1}\sum_{i=1}^GS_i(Z_i-V)\), with \(\Sigma_{\rm or}:=\operatorname{Cov}(S(Y)(Z-V)\mid x)\). A prompt-only-baseline estimator has the form \(\widehat g_b:=G^{-1}\sum_iS_i(Z_i-b(x))\), where \(b(x)\) is deterministic. Assume additionally that \(\|S(Y)\|^2\) and \(Z\) are conditionally uncorrelated given \(x\).

## Task

Prove the following integrated theorem. The leave-one-out estimator is the symmetric order-two U-statistic
\[
\widehat g_{\rm loo}=\binom G2^{-1}\sum_{i<j}h((Y_i,Z_i),(Y_j,Z_j)),\qquad h((y,z),(y',z')):=\tfrac12(S(y)-S(y'))(z-z').
\]
Its mean-squared error satisfies
\[
\mathbb E\|\widehat g_{\rm loo}-g\|^2
=\frac{\operatorname{tr}\Sigma_{\rm or}}{G}+O\!\left(\frac{\mathbb E\|S(Y)\|^2}{G^2}\right),
\]
where the implied constant depends only on \(M\). In particular, it has the same asymptotic MSE coefficient as the oracle estimator. Moreover, every unbiased prompt-only-baseline estimator obeys
\[
\operatorname{MSE}(\widehat g_b\mid x)=\frac{1}{G}\left(\operatorname{tr}\Sigma_{\rm or}+\mathbb E[\|S(Y)\|^2(V-b(x))^2\mid x]\right),
\]
so the leave-one-out estimator is asymptotically no worse than any such estimator, with strict improvement over the zero baseline whenever the final expectation with \(b=0\) is positive.
