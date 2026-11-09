# Problem

## Setup

Let $h_1,\ldots,h_n\in\mathbb R^{D_h}$ be a causal sequence and fix $i$. Only $h_{1:i}$ is available. Let there be $K$ heads of width $D_r$ and let $\tau>0$. For each head choose $A_k\in\mathbb R^{D_h\times D_h}$ and define $\beta_{kj}=A_kh_j$. Introduce $x_i\in\mathbb R^{D_h}$, initialized at $x_i=h_i$, and define
\[
\varepsilon(x_i\mid h_{1:i})=-\tau\sum_{k=1}^K\log\!\left(\sum_{j=1}^i\exp\!\left(\frac{\beta_{kj}^{\mathsf T}x_i}{\tau}\right)\right).
\]
Let $W_k^K,W_k^Q,W_k^V\in\mathbb R^{D_r\times D_h}$ and $W_k^O\in\mathbb R^{D_h\times D_r}$. The causal multi-head attention residual update is defined by
\[
\operatorname{MHA}_i=h_i+\sum_{k=1}^K W_k^O\sum_{j=1}^i a_{ij}^{(k)}W_k^Vh_j,
\]
where
\[
a_{ij}^{(k)}=\frac{\exp((W_k^Kh_j)^{\mathsf T}(W_k^Qh_i)/\tau)}{\sum_{\ell=1}^i\exp((W_k^Kh_\ell)^{\mathsf T}(W_k^Qh_i)/\tau)}.
\]

## Task

Prove that if $A_k=(W_k^Q)^{\mathsf T}W_k^K$ for every head, then one gradient-descent step
\[
x_i^+=x_i-\eta\nabla_{x_i}\varepsilon(x_i\mid h_{1:i})
\]
with $x_i=h_i$, $\eta=1$, and $\tau=\sqrt{D_r}$ satisfies $x_i^+=\operatorname{MHA}_i$ when the induced projections are tied as $W_k^V=W_k^K$ and $W_k^O=W_k^{Q\mathsf T}$. Thus the energy step is exactly causal multi-head attention with tied key/value and query/output projections.
