# Problem

## Setup

Fix positive integers \(d,k\), a measurable safety oracle
\[
S:\mathbb R^d\longrightarrow\{\mathrm{safe},\mathrm{unsafe}\}
\]
for a fixed operating domain, and a measurable feature map \(\varphi:\mathbb R^d\to\mathbb R^k\). Write \(E_+=S^{-1}(\{\mathrm{safe}\})\) and \(E_-=S^{-1}(\{\mathrm{unsafe}\})\).

At step \(n\ge1\), the proposed parameter has a probability law \(\mu_n\) with a density with respect to Lebesgue measure on \(\mathbb R^d\), and assume \(0<\mu_n(E_+)<1\). For every Borel set \(E\subseteq\mathbb R^d\), define the conditional parameter laws
\[
Q_n^+(E)=\frac{\mu_n(E\cap E_+)}{\mu_n(E_+)},
\qquad
Q_n^-(E)=\frac{\mu_n(E\cap E_-)}{\mu_n(E_-)}.
\]
Both kinds of gate are evaluated on these same proposal laws and safety labels. Assume their induced feature laws are stationary: for every Borel \(A\subseteq\mathbb R^k\),
\[
P^+(A)=Q_n^+(\varphi^{-1}(A)),\qquad
P^-(A)=Q_n^-(\varphi^{-1}(A))
\]
do not depend on \(n\).

A classifier gate is a measurable map \(g_n:\mathbb R^k\to\{0,1\}\), and accepts a proposed parameter \(\theta\) exactly when \(g_n(\varphi(\theta))=1\). Put
\[
A_n=\{x:g_n(x)=1\},\qquad
\delta_n=P^-(A_n),\qquad
\operatorname{TPR}_n=P^+(A_n).
\]
Safe self-improvement means that the gate's conditional false-acceptance and true-positive rates satisfy
\[
\sum_{n\ge1}\delta_n<\infty,
\qquad
\sum_{n\ge1}\operatorname{TPR}_n=\infty.
\]
Assume \(P^+\ll P^-\), fix real constants \(p>1\) and \(c>0\), and consider classifier sequences satisfying \(\delta_n\le c n^{-p}\) for every \(n\). For real \(\alpha>1\), define
\[
D_\alpha(P^+\Vert P^-)
=\frac1{\alpha-1}\log\int\left(\frac{dP^+}{dP^-}\right)^\alpha dP^-.
\]
Assume this divergence is finite for some real \(\alpha_0>p/(p-1)\).

A verifier is a measurable map \(h:\mathbb R^d\to\{0,1\}\). It is sound when \(h(\theta)=1\) implies \(S(\theta)=\mathrm{safe}\). Its conditional rates at step \(n\) are
\[
\delta_n^{\mathrm{ver}}=Q_n^-(\{\theta:h(\theta)=1\}),
\qquad
\operatorname{TPR}_n^{\mathrm{ver}}=Q_n^+(\{\theta:h(\theta)=1\}).
\]

Let \(F:\mathbb R^d\to\mathcal Y\) describe the safety-relevant trajectories over the same fixed operating domain, where \((\mathcal Y,\rho)\) is a metric space and \(U\subseteq\mathcal Y\) is its unsafe set. Define \(\operatorname{dist}(y,U)=\inf_{u\in U}\rho(y,u)\), with \(\inf\varnothing=+\infty\). Assume
\[
F(\theta)\notin U\quad\Longrightarrow\quad S(\theta)=\mathrm{safe}.
\]
Suppose there are \(\theta_0\in\mathbb R^d\) and finite real constants \(m,L>0\) such that
\[
\operatorname{dist}(F(\theta_0),U)\ge m,
\qquad
\rho(F(\theta),F(\theta_0))\le L\|\theta-\theta_0\|_2
\quad\text{for every }\theta\in\mathbb R^d.
\]
For \(r>0\), write \(B(\theta_0,r)=\{\theta:\|\theta-\theta_0\|_2<r\}\). Assume that a constant \(q\in(0,1]\), independent of \(n\), satisfies
\[
Q_n^+\bigl(B(\theta_0,m/L)\bigr)\ge q
\quad\text{for every }n\ge1.
\]

## Task

Prove the following integrated theorem:

(i) Every classifier sequence satisfying the stationary feature assumptions and the stated power-law schedule has \(\sum_{n\ge1}\operatorname{TPR}_n<\infty\), so no such sequence satisfies both safe self-improvement conditions.

(ii) The verifier accepting exactly the open ball \(B(\theta_0,m/L)\) is sound, satisfies \(\delta_n^{\mathrm{ver}}=0\) at every step, and has \(\sum_{n\ge1}\operatorname{TPR}_n^{\mathrm{ver}}=\infty\).
