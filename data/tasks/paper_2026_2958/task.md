# Problem

## Setup

Fix an integer \(d\ge1\). Let \(X,X_1,\ldots,X_n\in\mathbb R^d\) be iid on a common probability space \((\Omega,\mathcal A,\mathbb P)\), with
\[
X\sim t_\nu(\mu,\Sigma),\qquad \nu>2,
\]
where \(t_\nu(\mu,\Sigma)\) denotes the multivariate Student t law with location \(\mu\in\mathbb R^d\), finite symmetric nonnegative-definite scatter matrix \(\Sigma\), and degrees of freedom \(\nu\). These distributional parameters are fixed as \(n\to\infty\).

Let \(\mathcal W\subseteq\mathbb R^d\setminus\{0\}\) be the direction parameter space, equipped with its trace Borel sigma-algebra. Fix \(w_0\in\mathcal W\), a measurable neighborhood \(U\subseteq\mathcal W\) of \(w_0\), an interval \(I\subseteq\mathbb R\) containing \(q_\alpha(w)\) for every \(w\in U\), and a fixed \(\alpha\in(0,1)\). For \(w\in\mathcal W\), define
\[
\ell_w(x)=-w^\top x,
\quad F(w,t)=\mathbb P\{\ell_w(X)\le t\},
\quad F_n(w,t)=\frac1n\sum_{i=1}^n\mathbf 1\{\ell_w(X_i)\le t\}.
\]
Define
\[
q_\alpha(w)=\inf\{t:F(w,t)\ge\alpha\},\qquad
\widehat q_\alpha(w)=\inf\{t:F_n(w,t)\ge\alpha\}.
\]
Assume:

1. For every \(w\in U\), \(F(w,\cdot)\) is differentiable near \(q_\alpha(w)\), with derivative \(f_w\), and \(f_w(q_\alpha(w))\ge c>0\) uniformly on \(U\), where \(c\) is fixed. In particular, the local projected distributions used here are nondegenerate.
2. The class \(\{x\mapsto\mathbf 1\{-w^\top x\le t\}:w\in U,t\in I\}\) is VC, the supremum below is measurable, and
\[
\sup_{w\in U,\,t\in I}|F_n(w,t)-F(w,t)|\xrightarrow{P}0.
\]
3. For each \(n\), \(\widehat w\) is a measurable \(\mathcal W\)-valued random vector, possibly depending on the same observations, and \(\mathbb P\{\widehat w\in U\}\to1\).
4. There are jointly measurable random functions \(r_n:\Omega\times U\to\mathbb R\), written \(r_n(w)\), such that, for each \(n\), almost surely simultaneously for every \(w\in U\),
\[
\widehat q_\alpha(w)-q_\alpha(w)
=\frac{\alpha-F_n(w,q_\alpha(w))}{f_w(q_\alpha(w))}+r_n(w).
\]
The assumed local uniform Bahadur representation includes the higher-order remainder property
\[
\sqrt n\,\sup_{w\in U}|r_n(w)|\xrightarrow{P}0,
\]
with this supremum measurable.

## Task

Prove that, with probability tending to one,
\[
\widehat q_\alpha(\widehat w)-q_\alpha(w_0)
=\underbrace{q_\alpha(\widehat w)-q_\alpha(w_0)}_{\Delta_{\rm dir}}
+\underbrace{\frac{\alpha-F_n(\widehat w,q_\alpha(\widehat w))}{f_{\widehat w}(q_\alpha(\widehat w))}}_{\Delta_{\rm emp}}
+\underbrace{r_n(\widehat w)}_{\Delta_{\rm rem}}.
\]
The local density and remainder evaluations in this assertion are understood on \(\{\widehat w\in U\}\). The three displayed terms are respectively the population directional movement, empirical fluctuation at the perturbed direction, and the Bahadur remainder.
