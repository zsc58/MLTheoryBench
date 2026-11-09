# Problem

## Setup

Let $\phi:\mathcal X\to\mathbb R^d$ be fixed. Given training data $D_{\rm tr}=\{(x_i,y_i)\}_{i=1}^n$ with $n\ge1$, assume
\[
y\mid x,\theta\sim\mathcal N(\theta^\top\phi(x),\sigma^2),\qquad \theta\sim\mathcal N(0,\tau^2 I_d),
\]
where $\sigma^2,\tau^2>0$. Write $\Phi$ for the matrix with rows $\phi(x_i)^\top$ and $y=(y_1,\ldots,y_n)^\top$. The source posterior is
\[
\pi_s(\theta\mid D_{\rm tr})=\mathcal N(\hat\theta_s,\Sigma_\theta),\quad
\Sigma_\theta=(\tau^{-2}I_d+\sigma^{-2}\Phi^\top\Phi)^{-1},\quad
\hat\theta_s=\Sigma_\theta\Phi^\top y/\sigma^2.
\]
Assume conditional label shift $p_t(x\mid y)=p_s(x\mid y)$, target absolute continuity with respect to source, and the known density ratio
\[
w(y)=\frac{p_t(y)}{p_s(y)}=\frac{e^{\beta y}}{Z_w},\qquad Z_w=\int e^{\beta u}p_s(u)\,du\in(0,\infty),
\]
for a real $\beta$. For each $x$ and $\theta$, define
\[
Z_\theta(x)=\int p_s(u\mid x,\theta)w(u)\,du,
\]
and define the likelihood-ratio-adjusted posterior by
\[
\pi^\star(\theta\mid D_{\rm tr})\propto \pi_s(\theta\mid D_{\rm tr})\prod_{i=1}^n Z_\theta(x_i)^{-1}.
\]
Let $\bar\phi=n^{-1}\sum_{i=1}^n\phi(x_i)$.

## Task

Prove that
\[
\pi^\star(\theta\mid D_{\rm tr})=\mathcal N(\hat\theta_t,\Sigma_\theta),
\qquad
\hat\theta_t=\hat\theta_s-\beta n\Sigma_\theta\bar\phi.
\]
In particular, the target adjustment changes only the posterior mean and leaves the covariance unchanged.
