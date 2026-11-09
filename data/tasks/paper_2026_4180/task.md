# Problem

## Setup

Let \(d\ge1\). Write \(\Gamma_0(\mathbb R^d)\) for the proper lower-semicontinuous convex functions \(f:\mathbb R^d\to\mathbb R\cup\{+\infty\}\), and let \(\operatorname{dom}f=\{x:f(x)<+\infty\}\). For such a function, its Fenchel conjugate and subdifferential are
\[
f^*(v)=\sup_{z\in\mathbb R^d}\{\langle v,z\rangle-f(z)\},
\qquad
\partial f(x)=\{v:f(z)\ge f(x)+\langle v,z-x\rangle\text{ for every }z\}
\]
when \(x\in\operatorname{dom}f\), with \(\partial f(x)=\varnothing\) otherwise. Set \(\operatorname{dom}\partial f=\{x:\partial f(x)\ne\varnothing\}\). For a convex set, \(\operatorname{aff}\) denotes its affine hull and \(\operatorname{ri}\) its interior relative to that affine hull. Write \(\operatorname{Span}M\) for the column space of a matrix \(M\), and \(\operatorname{Argmin}\) for the set of minimizers.

Let \(M\in\mathbb R^{d\times d}\) be symmetric positive semidefinite, let \(q\in\operatorname{Span}M\), and let \(c\in\mathbb R\). Define
\[
\ell(x)=\tfrac12\langle x,Mx\rangle-\langle q,x\rangle+c.
\]
Let \(h\in\Gamma_0(\mathbb R^d)\) have nonempty closed convex domain \(C=\operatorname{dom}h\), and assume \(\operatorname{dom}h^*=\mathbb R^d\). Define
\[
\sigma_C(v)=\sup_{z\in C}\langle v,z\rangle,
\qquad
\iota_C(z)=\begin{cases}0,&z\in C,\\+\infty,&z\notin C.\end{cases}
\]

A mirror flow for a potential \(g\in\Gamma_0(\mathbb R^d)\) is a pair of functions \((w,x):[0,\infty)\to\mathbb R^d\times\mathbb R^d\) such that, for almost every \(t\), \(w\) is differentiable and
\[
\dot w(t)=-\nabla\ell(x(t)),\qquad w(t)\in\partial g(x(t)).
\]
Here \(w\) is the dual trajectory and \(x\) an associated primal trajectory. All assertions of almost-everywhere validity refer to Lebesgue measure.

For each \(\varepsilon>0\), let \((w^\varepsilon,x^\varepsilon)\) be such a mirror flow for \(h\), with \(w^\varepsilon\) Lipschitz on \([0,\infty)\) and \(w^\varepsilon(0)=w_0^\varepsilon\). Assume
\[
\mu_\varepsilon:=\|w_0^\varepsilon\|\longrightarrow\infty
\quad\text{as }\varepsilon\to0.
\]
For sufficiently small \(\varepsilon\), so that \(\mu_\varepsilon>0\), define
\[
\bar w^\varepsilon(s)=\mu_\varepsilon^{-1}w^\varepsilon(\mu_\varepsilon s),\qquad
\bar x^\varepsilon(s)=x^\varepsilon(\mu_\varepsilon s),\qquad
\bar w_0^\varepsilon=\mu_\varepsilon^{-1}w_0^\varepsilon.
\]
Assume \(\bar w_0^\varepsilon\to\bar w_0\), with
\[
\bar w_0\in\operatorname{dom}\partial\sigma_C\cap
\bigl(\operatorname{ri}\operatorname{dom}\sigma_C+\operatorname{Span}M\bigr),
\]
and, for all sufficiently small \(\varepsilon\),
\[
\bar w_0^\varepsilon-\bar w_0\in\operatorname{aff}\operatorname{dom}\sigma_C.
\]

## Task

Prove that there exists a unique Lipschitz dual trajectory \(\bar w:[0,\infty)\to\mathbb R^d\) that admits an associated primal trajectory making it a mirror flow for \(\iota_C\), with \(\bar w(0)=\bar w_0\).

Prove further that, for any associated primal trajectory \(\bar x\) and every \(S>0\), the following hold as \(\varepsilon\to0\):

1. \(\bar w^\varepsilon\to\bar w\) uniformly on \([0,S]\).
2. The gradient and loss converge in the following weighted senses:
   \[
   \int_0^S s\,\|\nabla\ell(\bar x^\varepsilon(s))-\nabla\ell(\bar x(s))\|^2\,ds\longrightarrow0,
   \]
   \[
   \int_0^S s\,|\ell(\bar x^\varepsilon(s))-\ell(\bar x(s))|\,ds\longrightarrow0.
   \]
3. For almost every \(s\in[0,S]\),
   \[
   \bar x(s)\in\operatorname*{Argmin}_{z\in\partial\sigma_C(\bar w(s))}\ell(z).
   \]
   Moreover, let \(\bar y:[0,S]\to\mathbb R^d\) be any function for which there exists a sequence \(\varepsilon_k\to0\) such that
   \[
   \bar x^{\varepsilon_k}(s)\longrightarrow\bar y(s)
   \quad\text{for almost every }s\in[0,S].
   \]
   Then
   \[
   \bar y(s)\in\operatorname*{Argmin}_{z\in\partial\sigma_C(\bar w(s))}\ell(z)
   \quad\text{for almost every }s\in[0,S].
   \]
