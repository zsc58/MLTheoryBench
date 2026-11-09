# Problem

## Setup

Let \(d\ge1\) be an integer. Consider a federated population with sensitive groups \(s\in\{0,1\}\) and silos \(j\in\{1,\ldots,d\}\). For each \((j,s)\), let \(\nu_{j,s}\) be a probability law on \(\mathbb R\) with finite second moment, representing the local score distribution. Let \(\alpha_s\ge0\) satisfy \(\alpha_0+\alpha_1=1\), and for each s let \(\pi_{j|s}\ge0\) satisfy \(\sum_{j=1}^d\pi_{j|s}=1\).

Write \(\mathcal P_2(\mathbb R)\) for the probability laws on \(\mathbb R\) with finite second moment. For \(\mu,\eta\in\mathcal P_2(\mathbb R)\), let \(W_2\) be the 2-Wasserstein distance:
\[
W_2(\mu,\eta)^2
:=\inf_{\gamma\in\Pi(\mu,\eta)}\int_{\mathbb R^2}|x-y|^2\,d\gamma(x,y),
\]
where \(\Pi(\mu,\eta)\) is the set of probability laws on \(\mathbb R^2\) with marginals \(\mu\) and \(\eta\). For a law \(\mu\), define its cdf and generalized quantile by
\[
F_\mu(x)=\mu(({-\infty},x]),\qquad
Q_\mu(u)=\inf\{x\in\mathbb R:F_\mu(x)\ge u\},\quad 0<u<1.
\]

Define
\[
\nu_s^{\times}:=\sum_{j=1}^d\pi_{j|s}\nu_{j,s}.
\]
Let \(\nu_s^*\) and \(\nu^{\times *}\) be minimizers over \(\mathcal P_2(\mathbb R)\) of, respectively,
\[
\sum_j\pi_{j|s}W_2(\nu_{j,s},\nu)^2,
\qquad
\sum_s\alpha_sW_2(\nu_s^{\times},\nu)^2.
\]
Use the abbreviations
\[
Q_{j,s}=Q_{\nu_{j,s}},\qquad
Q_s^{\times}=Q_{\nu_s^{\times}},\qquad
Q_s^*=Q_{\nu_s^*},\qquad
Q^{\times *}=Q_{\nu^{\times *}}.
\]
Set
\[
G_2:=\sum_s\alpha_sW_2(\nu_s^{\times},\nu^{\times *})^2,\quad
V_{\rm mix}:=\sum_s\alpha_sW_2(\nu_s^{\times},\nu_s^*)^2,\quad
V_{\rm bar}:=\sum_s\alpha_sW_2(\nu_s^*,\nu^{\times *})^2,
\]
and, with \(\langle f,g\rangle=\int_0^1 f(u)g(u)\,du\) for \(f,g\in L^2((0,1))\), define
\[
R:=2\sum_s\alpha_s\langle Q_s^{\times}-Q_s^*,Q_s^*-Q^{\times *}\rangle.
\]

## Task

Prove the integrated theorem
\[
G_2=V_{\rm mix}+V_{\rm bar}+R,\qquad
|R|\le2\sqrt{V_{\rm mix}V_{\rm bar}}.
\]
Thus the federated p=2 disparity exactly decomposes into the mixture term, the within-group-barycenter disparity term, and an interaction remainder with the stated control.
