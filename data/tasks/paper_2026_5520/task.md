# Problem

## Setup

At a round, conditional on the previously accepted states and release decisions, represented by a filtration \(\mathcal F_{t-1}\), form a Poisson-sampled batch \(B\) by including each record with nominal probability \(q\in(0,1]\). Let \(E(B)\in\mathbb R\) be the batch evaluation metric, and fix constants \(C\in\mathbb R\) and \(\Delta\in\mathbb R\). Define the threshold distance
\[
X(B)=C-\Delta E(B).
\]
Release the batch exactly when
\[
v>X(B),
\]
where \(v\sim\mathcal N(0,\sigma_v^2)\), with \(\sigma_v>0\), independently of the sampling and of \(\mathcal F_{t-1}\). Assume \(X(B)\in[-C_{\max},C_{\max}]\) for every possible batch and history, where \(C_{\max}\ge0\). Assume that, when a fixed record is added to or removed from a coupled batch, the resulting threshold distance can decrease by at most \(s>0\) (the direction that facilitates release).

For a fixed record \(z\), define
\[
q_{\mathrm{cond}}(z\mid\mathcal F_{t-1})
=\Pr(z\in B\mid \mathrm{release},\mathcal F_{t-1}),
\qquad
\rho(z\mid\mathcal F_{t-1})=q_{\mathrm{cond}}(z\mid\mathcal F_{t-1})/q.
\]
Let \(\Phi_{\sigma_v}\) denote the CDF of \(\mathcal N(0,\sigma_v^2)\).

## Task

Prove that, for every prior history and every record \(z\),
\[
\rho(z\mid\mathcal F_{t-1})\le
\min\left\{
\frac{1-\Phi_{\sigma_v}(C_{\max}-s)}{1-\Phi_{\sigma_v}(C_{\max})},\frac1q
\right\}.
\]
Equivalently,
\[
q_{\mathrm{cond}}(z\mid\mathcal F_{t-1})
\le q\min\left\{
\frac{1-\Phi_{\sigma_v}(C_{\max}-s)}{1-\Phi_{\sigma_v}(C_{\max})},\frac1q
\right\},
\]
so the bound is independent of the realized history.
