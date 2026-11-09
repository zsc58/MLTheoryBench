# Problem

## Setup

Fix positive integers $N,m,d_0,\ldots,d_N,k_1,\ldots,k_N,s_1,\ldots,s_N$ satisfying
\[
d_i=\frac{d_{i-1}-k_i}{s_i}+1,\qquad 1\le i\le N.
\]
Consider a depth-$N$, single-channel, one-dimensional linear convolutional network with layer filters $w^{(i)}\in\mathbb R^{k_i}$. There is no padding or bias. Define the layer matrix
\[
W_i(w^{(i)})=\Pi_{(d_{i-1},d_i),k_i,s_i}(w^{(i)})\in\mathbb R^{d_i\times d_{i-1}}
\]
by its action
\[
\bigl(W_i(w^{(i)})x\bigr)_j
=\sum_{n=1}^{k_i}w_n^{(i)}x_{(j-1)s_i+n},
\qquad x\in\mathbb R^{d_{i-1}},\quad 1\le j\le d_i.
\]
Write $w=(w^{(1)},\ldots,w^{(N)})\in\mathbb R^{\sum_i k_i}$ and
\[
\Pi(w)=W_N(w^{(N)})\cdots W_1(w^{(1)}),\qquad v=\pi(w),
\]
where $v$ is the effective convolution filter of the composed matrix. Its effective stride is $\prod_i s_i$ and its filter width is
\[
k_v=k_1+\sum_{i=2}^N(k_i-1)\prod_{h<i}s_h.
\]
Empty products equal one and empty sums equal zero.

Fix training pairs $(x_r,y_r)_{r=1}^m$ with $x_r\in\mathbb R^{d_0}$ and $y_r\in\mathbb R^{d_N}$. Write $X=[x_1\ \cdots\ x_m]$ and assume $XX^\top$ is invertible. For a differentiable loss $\ell$, define
\[
L(w)=\sum_{r=1}^m\ell(\Pi(w)x_r,y_r),\qquad
\dot w(t)=-\nabla L(w(t)),\quad w(0)=w_0,
\]
where the gradient is taken with respect to the standard Euclidean coordinates of all layer filters.

For $z,y\in\mathbb R^{d_N}$, choose any one of the following losses, with its parameters fixed in the indicated range:
\[
\ell_p(z,y)=\frac1p\|z-y\|_p^p,\quad p\ge2\text{ an even integer};
\]
\[
\ell_{\rm PH}(z,y)=\delta\sum_{j=1}^{d_N}\sqrt{1+((z_j-y_j)/\delta)^2},\quad \delta>0;
\]
\[
\ell_{\rm GH}(z,y)=\frac1\alpha\sum_{j=1}^{d_N}\log\!\big(e^{\alpha(z_j-y_j)}+e^{-\alpha(z_j-y_j)}+\beta\big),\quad \alpha>0,\ \beta>-2;
\]
\[
\ell_{\rm LC}(z,y)=\frac1\alpha\sum_{j=1}^{d_N}\log\cosh(\alpha(z_j-y_j)),\quad \alpha>0.
\]

## Task

Prove that for every initialization $w_0\in\mathbb R^{\sum_i k_i}$, the gradient-flow initial-value problem has a solution for all $t\ge0$, the trajectory $w(t)$ is bounded, and $w(t)$ converges as $t\to\infty$ to a critical point of $L$ (that is, $\nabla L(w_\infty)=0$).
