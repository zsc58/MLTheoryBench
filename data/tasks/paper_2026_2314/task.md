# Problem

## Setup

Let $\mathcal P_2(\mathbb R)$ denote the Borel probability laws on $\mathbb R$ with finite second moment. Let there be $K\ge 2$ arms with reward laws $Q_1,\ldots,Q_K\in\mathcal P_2(\mathbb R)$, and let $\mathfrak U:\mathcal P_2(\mathbb R)\to\mathbb R$ be a functional. Let
\[
\Delta_K=\{w\in\mathbb R^K:w_i\ge 0,\ \sum_iw_i=1\},\qquad
\Delta_K^\circ=\{w\in\Delta_K:w_i>0\ \forall i\}.
\]
For $w\in\Delta_K$, define the mixture law $Q_w=\sum_iw_iQ_i$ and the induced utility $F(w)=\mathfrak U(Q_w)$. Assume $F$ is concave and differentiable on $\Delta_K^\circ$. A tangent direction is any $v$ with $\sum_i v_i=0$.

Assume that for every $w\in\Delta_K^\circ$ there is an integrable function $\phi_w$ (with all displayed arm-wise expectations finite) such that
\[
\mathbb E_{Q_w}[\phi_w(Y)]=0
\]
and, for every tangent $v$,
\[
\left.\frac{d}{d\varepsilon}F(w+\varepsilon v)\right|_{\varepsilon=0}
=\int \phi_w(y)\,d\Big(\sum_i v_iQ_i\Big)(y).
\]

For logits $h\in\mathbb R^K$, let $w=\sigma(h)$ with $\sigma_i(h)=e^{h_i}/\sum_j e^{h_j}$, and let $J(h)=\operatorname{diag}(w)-ww^\top$.

## Task

Prove the following integrated theorem. For every $w\in\Delta_K^\circ$, the vector
\[
g_i(w)=\mathbb E_{Q_i}[\phi_w(Y)]
\]
is the centered simplex gradient of $F$, meaning that it represents all tangent directional derivatives and satisfies $\langle w,g(w)\rangle=0$. Moreover, for every $h$ with $w=\sigma(h)$, if $A\sim\operatorname{Categorical}(w)$ and $Y\mid A=i\sim Q_i$, then the one-sample vector
\[
Z_k=(\mathbf 1\{A=k\}-w_k)\phi_w(Y),\qquad k=1,\ldots,K,
\]
is unbiased for the logit-space gradient:
\[
\mathbb E[Z]=\nabla_h(F\circ\sigma)(h)=J(h)g(w).
\]
