# Problem

## Setup

Fix an integer $K\ge1$. For each sample size $n$, let $D_n$ be training data and let $(X,Y)$ be an independent test pair. There are $K$ prediction-set procedures $C_1,\ldots,C_K$. Let
\[
\Delta^{K-1}=\{w\in[0,1]^K:\sum_{k=1}^K w_k=1\}
\]
with its Euclidean norm. Let $R:\Delta^{K-1}\to\mathbb R$ be the population-risk function associated with the learner library, and define the nonempty closed optimal set
\[
W^*=\operatorname*{arg\,min}_{w\in\Delta^{K-1}}R(w).
\]
For each $n$, let $\widehat w_n=(\widehat w_{n,1},\ldots,\widehat w_{n,K})\in\Delta^{K-1}$ be $D_n$-measurable and satisfy
\[
\operatorname{dist}(\widehat w_n,W^*)\xrightarrow{p}0.
\]
Fix $\alpha\in(0,1)$ and define
\[
C_{\mathrm{ens}}(x;D_n)=\left\{y:\sum_{k=1}^K\widehat w_{n,k}{\bf1}\{y\in C_k(x;D_n)\}>\tfrac12\right\}.
\]
All probabilities are marginal over $D_n$ and the independent test pair, and conditional probabilities given $D_n$ refer to the test pair.

Assume either:

(A1) **Finite-sample base validity:** for every $n$ and $k$, almost surely,
\[
\Pr\{Y\notin C_k(X;D_n)\mid D_n\}\le\alpha;
\]

or

(A1') **Uniform asymptotic base validity:**
\[
\sup_{1\le k\le K}\left|\Pr\{Y\notin C_k(X;D_n)\mid D_n\}-\alpha\right|=o_p(1).
\]

## Task

Prove the following integrated coverage theorem. Under (A1),
\[
\Pr\{Y\in C_{\mathrm{ens}}(X;D_n)\}\ge1-2\alpha\qquad\text{for every }n.
\]
Under (A1'),
\[
\liminf_{n\to\infty}\Pr\{Y\in C_{\mathrm{ens}}(X;D_n)\}\ge1-2\alpha.
\]
Moreover, in either regime, suppose there is a nonempty coalition $K^*\subseteq\{1,\ldots,K\}$ such that
\[
\inf_{w\in W^*}\sum_{k\in K^*}w_k>\tfrac12
\]
and
\[
\limsup_{n\to\infty}\Pr\Bigl(\exists k\in K^*:Y\notin C_k(X;D_n)\Bigr)\le\alpha.
\]
Then
\[
\liminf_{n\to\infty}\Pr\{Y\in C_{\mathrm{ens}}(X;D_n)\}\ge1-\alpha.
\]
In particular, this applies to a dominant learner $k^*$ when
\[
\inf_{w\in W^*}w_{k^*}>\tfrac12
\]
and its miscoverage probability has limsup at most $\alpha$.
