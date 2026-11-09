# Problem

## Setup

Let \(d\) be finite. Let \(H\) be a nonzero symmetric positive-semidefinite \(d\) by \(d\) matrix and let \(P\) be a symmetric positive-definite \(d\) by \(d\) matrix satisfying \(PH=HP\). Consider the quadratic model
\[
f(x)=\tfrac12 x^\top Hx
\]
with minimizer \(x^*=0\). Fix \(\beta\in[0,1)\) and \(\eta>0\). Let \(u_t\) be independent \(N(0,I_d)\) vectors and define
\[
g_t=u_tu_t^\top Hx_t,\qquad
m_{t+1}=\beta m_t+(1-\beta)g_t,\qquad
x_{t+1}=x_t-\eta P^{-1}m_{t+1},
\]
from arbitrary deterministic \(x_0\in\mathbb R^d\) and \(m_0=0\).

Mean stability means \(\sup_t\|\mathbb E[x_t]\|<\infty\) for every initialization \(x_0\). Mean-square stability means \(\sup_t\mathbb E\|x_t\|^2<\infty\) for every initialization \(x_0\). Define \(\eta_{\rm mean}^*\) and \(\eta_{\rm ms}^*\) as the suprema of the positive step sizes for which the corresponding stability property holds for every initialization \(x_0\), with \(m_0=0\).

Let \(0\le\widetilde\lambda_1,\ldots,\widetilde\lambda_d\) be the eigenvalues of \(P^{-1}H\), let
\[
L=\max_i\widetilde\lambda_i,
\qquad
\tau=\sum_i\widetilde\lambda_i=\operatorname{Tr}(P^{-1}H).
\]

## Task

Prove the following theorem. The mean critical step size is
\[
\eta_{\rm mean}^*=\frac{2(1+\beta)}{(1-\beta)L}.
\]

Moreover, \(\eta_{\rm ms}^*\) is the unique number in \((0,(1+\beta)/L)\) satisfying
\[
\sum_{i=1}^d
\frac{\eta_{\rm ms}^*\widetilde\lambda_i}
{2\left(1-\eta_{\rm ms}^*\widetilde\lambda_i/(1+\beta)\right)}=1,
\]
and
\[
\frac{2}{\tau+2L/(1+\beta)}
\le\eta_{\rm ms}^*
\le\frac{2}{\tau}.
\]
