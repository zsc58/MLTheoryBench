# Problem

## Setup

Let \((p_t)_{t\in[0,1]}\) be a family of strictly positive probability densities on \(\mathbb R^d\), with \(p_1\) absolutely continuous with respect to \(p_0\). Let \(L\in[0,\infty)\), and assume that for every \(x\), the map \(t\mapsto\log p_t(x)\) is \(L\)-Lipschitz on \([0,1]\). Define
\[
s^{(t)}(x,t)=\partial_t\log p_t(x)
\]
where the derivative exists, taking its value to be zero elsewhere.

Let \(s_\theta:\mathbb R^d\times[0,1]\to\mathbb R\) be a jointly measurable model score. Call \(\theta\) admissible when, for Lebesgue-almost every \(x\), \(t\mapsto s_\theta(x,t)\) is absolutely continuous on \([0,1]\), its almost-everywhere time derivative has a jointly measurable version, and
\[
\int_0^1\mathbb E_{X\sim p_t}
\left[s_\theta(X,t)^2+|\partial_t s_\theta(X,t)|\right]dt<\infty,
\]
\[
\mathbb E_{p_0}|s_\theta(X,0)|+
\mathbb E_{p_1}|s_\theta(X,1)|<\infty.
\]
Time derivatives on their exceptional null sets may be assigned the value zero.

Set
\[
\ell(x)=\log\frac{p_1(x)}{p_0(x)},\qquad
\widehat\ell_\theta(x)=\int_0^1s_\theta(x,t)\,dt,
\]
\[
\mathcal L_{\rm fit}(\theta)=\int_0^1
\mathbb E_{X\sim p_t}
\left[(s^{(t)}(X,t)-s_\theta(X,t))^2\right]dt,
\]
\[
\mathcal L_{\rm ibp}(\theta)=
\int_0^1\mathbb E_{p_t}
\left[s_\theta(X,t)^2+2\,\partial_t s_\theta(X,t)\right]dt
-2\mathbb E_{p_1}[s_\theta(X,1)]
+2\mathbb E_{p_0}[s_\theta(X,0)],
\]
and
\[
V=\int_0^1\operatorname{Var}_{X\sim p_t}
\left(s^{(t)}(X,t)\right)dt.
\]
All time integrals use Lebesgue measure on \([0,1]\). The estimator \(\widehat\ell_\theta\) is defined almost everywhere in \(x\); it may be assigned the value zero on the exceptional spatial null set.

## Task

Prove the following integrated theorem: for every admissible \(\theta\),
\[
\mathbb E_{X\sim p_1}
\left[(\ell(X)-\widehat\ell_\theta(X))^2\right]
\le e^L\left[\mathcal L_{\rm ibp}(\theta)+V\right],
\]
and establish
\[
\mathcal L_{\rm fit}(\theta)=\mathcal L_{\rm ibp}(\theta)+V.
\]
Conclude that, with \(L\) held fixed, jointly reducing the surrogate term \(\mathcal L_{\rm ibp}(\theta)\) and the path-dependent variance term \(V\) reduces this upper bound. When comparing designable paths, interpret this conclusion for paths with the same endpoints that satisfy the stated Lipschitz condition with the same chosen \(L\).
