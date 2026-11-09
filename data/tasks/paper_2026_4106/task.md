# Problem

## Setup

Throughout, $\|\cdot\|$ denotes the Euclidean norm, and measurability on Euclidean spaces refers to their Borel sigma-algebras. Let $(X,Y)$ have law $P$ on $\mathbb R^p\times(\mathbb R^d\setminus\{0\})$. Assume $\mathbb E_P\|Y\|<\infty$ and, for some finite $B_y>0$, $0<\|Y\|\le B_y$ almost surely. Let $S\subset\mathbb R^d$ be nonempty and compact, with $\|w\|\le B_S$ for all $w\in S$, where $B_S>0$ is finite.

Fix a Borel-measurable oracle $w^*:\mathbb R^d\to S$ satisfying
\[
w^*(c)\in\arg\min_{w\in S}c^\top w.
\]
Its deterministic tie-breaking rule depends only on the minimizing set, not on the cost vector generating that set. Define
\[
\ell_{\rm dec}(\hat y,y)=y^\top w^*(\hat y)-y^\top w^*(y),\qquad R_P^{\rm dec}(f)=\mathbb E_P[\ell_{\rm dec}(f(X),Y)].
\]
Set $C=\mathbb E_P\|Y\|$, $T(x,y)=(x,y/\|y\|)$, define $\widetilde Q$ by $d\widetilde Q/dP=\|y\|/C$, and let $Q$ be the push-forward of $\widetilde Q$ under $T$, writing its coordinates as $(X,Z)$. Define
\[
\ell_{\rm ws}(\hat y,y)=\|y\|\left\|\hat y-\frac{y}{\|y\|}\right\|^2
\]
for $y\ne0$, and $R_P^{\rm ws}(f)=\mathbb E_P[\ell_{\rm ws}(f(X),Y)]$.

Predictors are all measurable functions $f:\mathbb R^p\to\mathbb R^d$. Expectations of nonnegative losses are understood in $[0,\infty]$, and Bayes minimization is over this entire predictor class.

## Task

Prove the following integrated theorem: for every measurable predictor $f$,
\[
\mathbb E_Q\|f(X)-Z\|^2=\frac1C R_P^{\rm ws}(f),
\]
and
\[
\mathbb E_Q[\ell_{\rm dec}(f(X),Z)]=\frac1C R_P^{\rm dec}(f).
\]
Moreover, every Bayes minimizer of $R_P^{\rm ws}$ induces a Bayes-optimal downstream decision: if $f^*$ minimizes $R_P^{\rm ws}$ over measurable predictors, then $f^*$ minimizes $R_P^{\rm dec}$ (equivalently, $w^*(f^*(x))$ minimizes $\mathbb E_P[Y\mid X=x]^\top w$ over $w\in S$ for $P_X$-almost every $x$, where $P_X$ is the marginal law of $X$).
