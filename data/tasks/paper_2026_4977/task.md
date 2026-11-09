# Problem

## Setup

Let $m,n$ be positive integers with $m\ge n$. For matrices, let $\|\cdot\|_F$ denote the Frobenius norm and $\|\cdot\|_2$ the spectral operator norm. Let $f:\mathbb R^{m\times n}\to\mathbb R$ satisfy
\[
f(X)=\mathbb E_{\xi\sim\mathcal D}[f(X;\xi)],\qquad f(X)\ge f^*>-\infty,
\]
and suppose that, for a constant $L>0$,
\[
\|\nabla f(Y)-\nabla f(X)\|_F\le L\|Y-X\|_F\qquad\text{for all }X,Y.
\]
Assume the stochastic gradient is jointly measurable in $(X,\xi)$ and, for every fixed $X$, satisfies
\[
\mathbb E_{\xi\sim\mathcal D}[\nabla f(X;\xi)]=\nabla f(X),\qquad
\mathbb E_{\xi\sim\mathcal D}\|\nabla f(X;\xi)-\nabla f(X)\|_F^2\le\sigma^2
\]
for a finite constant $\sigma>0$. Let $(\xi_t)_{t\ge1}$ be independent samples from $\mathcal D$.

For a nonzero matrix $A$, write its compact SVD using only its positive singular values as $A=U\Sigma V^\top$, and define $\operatorname{Orth}(A)=UV^\top$. Set $\operatorname{Orth}(0)=0$. Let $P_r(A)$ divide every nonzero row of $A$ by its Euclidean norm and leave zero rows unchanged.

Fix a deterministic initial point $X_1$, a deterministic number $\rho\ge0$, and a nonnegative deterministic weight-decay schedule $(\lambda_t)_{t\ge1}$, independently of the gradient samples. Set
\[
a=0.2\sqrt{\max\{m,n\}},\qquad \eta_t=t^{-3/4},\qquad \beta_t=1-t^{-1/2},
\]
and initialize $M_1=\nabla f(X_1;\xi_1)$. For $t\ge1$, form $O_t$ from $M_t$ as specified below, and then set
\[
X_{t+1}=X_t-\eta_t(aO_t+\lambda_tX_t),
\]
\[
M_{t+1}=\beta_{t+1}M_t+(1-\beta_{t+1})\nabla f(X_{t+1};\xi_{t+1}).
\]
The exact-polar method uses $O_t=\operatorname{Orth}(P_r(M_t))$.

For the finite-step method, define $\operatorname{NS5}(A)=Y^{(5)}(A)$ by
\[
Y^{(0)}(A)=\frac{A}{\max\{1,\|A\|_F\}},
\]
\[
Y^{(k+1)}(A)=\left(\frac{15}{8}I_m-\frac54Y^{(k)}(A)Y^{(k)}(A)^\top+\frac38\bigl(Y^{(k)}(A)Y^{(k)}(A)^\top\bigr)^2\right)Y^{(k)}(A),\quad k=0,\ldots,4,
\]
and use $O_t=\operatorname{NS5}(P_r(M_t))$.

## Task

Prove the following guarantee for every positive integer $T$. For the exact-polar method set $\varepsilon=0$. For the finite-step method define
\[
\varepsilon_{\mathrm{ns},T}=\max_{1\le t\le T}\|\operatorname{NS5}(P_r(M_t))-\operatorname{Orth}(P_r(M_t))\|_2.
\]
Use either $\varepsilon=\varepsilon_{\mathrm{ns},T}$, or a deterministic $\varepsilon\in[0,1)$ satisfying $\varepsilon_{\mathrm{ns},T}\le\varepsilon$ almost surely. Assume $0\le\varepsilon<1$ almost surely. The trajectory-defined choice of $\varepsilon$ is allowed to be random; it does not change the previously fixed inputs.

Let
\[
\gamma=1-\varepsilon,\quad c=\frac{\gamma}{\sqrt m}+(1+\varepsilon)\sqrt n,\quad d=a(1+\varepsilon)\sqrt n+\rho,\quad \kappa=\frac{a\gamma}{\sqrt m}-\rho.
\]
Suppose, almost surely,
\[
0\le\rho<\frac{a\gamma}{\sqrt m},\qquad
0\le\lambda_t\le\frac{\rho}{\|X_1\|_F+4a(1+\varepsilon)\sqrt n}\,t^{-1/4}\quad\text{for every }t\ge1.
\]
Then, with
\[
C_{1,\rho}=\frac aL\left(2\sqrt2L^2d^2+\sigma^2\right)+aLc^2,
\qquad C_{2,\rho}=\frac{a\sigma^2}{L}+\frac{3L}{2}d^2,
\]
prove
\[
\frac1T\sum_{t=1}^T\mathbb E\|\nabla f(X_t)\|_F
\le\frac{f(X_1)-f^*+C_{1,\rho}(1+\ln T)+C_{2,\rho}}{\kappa T^{1/4}}.
\]
The expectations are over the full gradient-sampling experiment, without conditioning on the realized approximation error. When $\varepsilon$ is random, the displayed conclusion is an almost-sure comparison of its deterministic left side with its random right side. Thus the statement covers both exact polar and finite-step NS5, with the displayed constants and $T^{-1/4}$ dependence.
