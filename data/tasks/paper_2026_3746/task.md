# Problem

## Setup

Let \(\|\cdot\|\) and \(\langle\cdot,\cdot\rangle\) denote the Euclidean norm and inner product on \(\mathbb{R}^d\). Let \(f:\mathbb{R}^d\to\mathbb{R}\) be differentiable, convex, and \(L\)-smooth for some \(L>0\), meaning
\[
\|\nabla f(u)-\nabla f(v)\|\le L\|u-v\|\quad\text{for all }u,v.
\]
Assume that \(f\) attains its minimum. Fix \(x^*\in\operatorname*{argmin} f\) and write \(f^*=f(x^*)\). Let \(r\in[0,1/L]\) be constant.

Starting from an arbitrary \(x_0\in\mathbb{R}^d\), define
\[
g_t=\nabla f(x_t),\qquad y_t=x_t+r g_t,\qquad h_t=\nabla f(y_t),
\]
and, when \(h_t\ne0\),
\[
\alpha_t=
\frac{\bigl[f(y_t)-f^*-r\langle h_t,g_t\rangle\bigr]_+}{\|h_t\|^2},
\qquad
x_{t+1}=x_t-\alpha_t h_t,
\]
where \([a]_+=\max\{a,0\}\). If \(h_t=0\), retain \(x_{t+1}=x_t\). For \(T\ge1\), define
\[
\bar x_T=\frac1T\sum_{t=0}^{T-1}x_t.
\]

## Task

Prove the following integrated claim.

1. If \(f\) is additionally \(m\)-strongly convex for some \(m>0\), then, for every \(t\ge0\),
\[
\|x_t-x^*\|^2\le
\left(1-\frac{m(1-Lr)^2}{4L}\right)^t\|x_0-x^*\|^2.
\]

2. In the convex case, for every \(T\ge1\),
\[
(1-Lr)^2\bigl(f(\bar x_T)-f^*\bigr)
\le \frac{2L\|x_0-x^*\|^2}{T}.
\]
Consequently, when \(r<1/L\),
\[
f(\bar x_T)-f^*\le
\frac{2L\|x_0-x^*\|^2}{T(1-Lr)^2}.
\]
