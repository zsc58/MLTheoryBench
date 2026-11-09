# Problem

## Setup

Fix an integer \(p\ge1\), a quantile level \(\tau\in(0,1)\), and constants \(s>1/2\) and \(Q>0\). Let \((X,Y)\) take values in \([0,1]^p\times\mathbb R\). Define
\[
m_\tau(x)=\inf\{v\in\mathbb R:F_{Y\mid X=x}(v)\ge\tau\},
\qquad
\rho_\tau(u)=u\bigl(\tau-\mathbf1\{u\le0\}\bigr).
\]

For each \(k=1,\ldots,p\), let \(\{\psi_{k,j}\}_{j\ge1}\) be a measurable centered orthonormal system on \([0,1]\) with respect to Lebesgue measure:
\[
\int_0^1\psi_{k,j}(v)\,dv=0,
\qquad
\int_0^1\psi_{k,i}(v)\psi_{k,j}(v)\,dv=\mathbf1\{i=j\}.
\]
Assume there is a common finite constant \(M\ge1\) such that \(|\psi_{k,j}(v)|\le M\) for all \(k,j,v\). Suppose the true quantile has the additive expansion
\[
m_\tau(x)=\alpha+\sum_{k=1}^p\sum_{j\ge1}\beta_{k,j}\psi_{k,j}(x^{(k)}),
\qquad
\sum_{j\ge1}j^{2s}\beta_{k,j}^2\le Q^2
\quad(k=1,\ldots,p).
\]
Fix a finite radius \(R>0\) such that every finite truncation of this expansion, including its intercept, belongs to the full coefficient \(\ell_1(R)\)-ball; explicitly,
\[
|\alpha|+\sum_{k=1}^p\sum_{j=1}^J|\beta_{k,j}|\le R
\qquad\text{for every integer }J\ge1.
\]
Put \(B=MR\).

Assume \(X\) has a density satisfying
\[
0<C_1\le p_X(x)\le C_2<\infty
\qquad(x\in[0,1]^p).
\]
Assume the conditional distribution of \(Y\) given \(X=x\) is absolutely continuous, with a density satisfying
\[
0<c_1\le p_{Y\mid X}(y\mid x)\le c_2<\infty
\qquad(x\in[0,1]^p,\ y\in[-B,B]).
\]

Let \((n_t)_{t\ge1}\) be a deterministic sequence of positive integers, and put \(N_t=\sum_{i=1}^t n_i\). At iteration \(t\), receive a batch \(\{(X_{t,i},Y_{t,i})\}_{i=1}^{n_t}\). All observations across all batches are independent copies of \((X,Y)\).

Initialize \(J_0=0\) and \(\theta_0=0\) in the intercept coordinate. For a nondecreasing sequence of positive truncation levels \(J_t\), let
\[
\Psi_t(x)=\left(1,\bigl(\psi_{k,j}(x^{(k)})\bigr)_{1\le j\le J_t,\ 1\le k\le p}\right)^\top,
\]
with the nonconstant coordinates ordered first by \(j\), then by \(k\). When \(J_t>J_{t-1}\), append zeros to \(\theta_{t-1}\) for the new coordinates, leaving all existing basis coefficients unchanged. Define
\[
G_t=\frac1{n_t}\sum_{i=1}^{n_t}
\left(\tau-\mathbf1\{Y_{t,i}\le\theta_{t-1}^\top\Psi_t(X_{t,i})\}\right)\Psi_t(X_{t,i}),
\]
\[
\widetilde\theta_t=\theta_{t-1}+\gamma_tG_t,
\qquad
\theta_t=\underset{\vartheta\in\mathbb R^{1+pJ_t}:\,\|\vartheta\|_1\le R}{\operatorname{argmin}}
\|\widetilde\theta_t-\vartheta\|_2^2,
\qquad
\widehat q_t(x)=\theta_t^\top\Psi_t(x).
\]

## Task

Prove that for every such batch-size sequence satisfying \(n_t/N_t\to0\), and for a sufficiently large fixed constant \(A\), the choices
\[
\gamma_t=A\frac{n_t}{N_t},
\qquad
J_t=\left\lceil N_t^{1/(2s+1)}\right\rceil
\]
yield
\[
\mathbb E\,\|\widehat q_t-m_\tau\|_{L^2([0,1]^p)}^2
=O\!\left(N_t^{-2s/(2s+1)}\right)
\qquad(t\to\infty).
\]
Here the norm uses Lebesgue measure, and the expectation is over all observed data. The constant \(A\) is independent of \(t\) and may depend on the fixed model bounds. The implicit rate constant may also depend on the fixed batch-size sequence, but not on \(t\).
