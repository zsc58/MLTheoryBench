# Problem

## Setup

Let \(n,m,C\) be positive integers. Let \(D\) be a probability distribution on a measurable product space \(\mathcal X\times\mathcal Y\), and let \(S=((x_i,y_i))_{i=1}^n\sim D^n\).

Fix a jointly measurable map \((v,x)\mapsto h_v(x)\in\mathbb R^C\), with \(v\in\mathbb R^m\), such that \(v\mapsto h_v(x)\) is twice continuously differentiable on \(\mathbb R^m\) for every \(x\). Let \(L:\mathbb R^C\times\mathcal Y\to\mathbb R\) be measurable. For every \(y\), assume that \(L(\cdot,y)\) is differentiable and, for fixed finite constants \(\ell,\beta\ge0\), satisfies
\[
|L(z,y)-L(z',y)|\le\ell\|z-z'\|_2,
\qquad
\|\nabla_zL(z,y)-\nabla_zL(z',y)\|_2\le\beta\|z-z'\|_2.
\]
Assume that \(L(0,y)\) is the same real number for every \(y\). Fix a measurable function \(a:\mathbb R^m\to(0,\infty)\), written \(a_v=a(v)\), such that \(\|h_v(x)\|_2\le a_v\) for every \(v,x\). Define
\[
L_D(h_v)=\mathbb E_{(x,y)\sim D}L(h_v(x),y),
\qquad
L_S(h_v)=\frac1n\sum_{i=1}^nL(h_v(x_i),y_i).
\]

Fix a finite radius \(R\ge0\), a scale \(\sigma>0\), and a finite constant \(B>0\). Set
\[
\Theta=\{w\in\mathbb R^m:\|w\|_2\le R\},
\qquad Q_w=\mathcal N(w,\sigma^2I_m).
\]
For a measurable scalar function \(f\) and a probability distribution \(Q\) satisfying \(\int\|v\|_2\,Q(dv)<\infty\) and \(\int|f(v)|\,Q(dv)<\infty\), define
\[
\operatorname{Jen}_Q[f]
=f\!\left(\int v\,Q(dv)\right)-\int f(v)\,Q(dv).
\]
Assume that, for every \(w\in\Theta\) and \((x,y)\in\mathcal X\times\mathcal Y\),
\[
\mathbb E_{v\sim Q_w}|L(h_v(x),y)|<\infty,
\qquad
\left|\operatorname{Jen}_{Q_w}\big[v\mapsto L(h_v(x),y)\big]\right|\le\sigma^2B.
\]

The following samplewise assumptions hold for \(D^n\)-almost every \(S\). Write
\[
J_i(w)=\nabla_wh_w(x_i)\in\mathbb R^{C\times m},
\qquad
H_{i,k}(w)=\nabla_w^2(h_w(x_i))_k\in\mathbb R^{m\times m}.
\]
For each \(i\), assume that the map
\[
w\longmapsto\mathbb E_{u\sim\mathcal N(0,I_m)}L(h_{w+\sigma u}(x_i),y_i)
\]
is differentiable at every \(w\in\Theta\), with each coordinate derivative obtained by differentiation under the Gaussian integral. The Gaussian integral of the absolute value of each differentiated integrand is finite at these points.

Let \(G_i,B_{i,\sigma}\in\mathbb R^{m\times m}\) be finite positive-semidefinite matrices, measurable functions of \(S\), such that
\[
J_i(w)^TJ_i(w)\preceq G_i\qquad(w\in\Theta).
\]
All expectations over \(u\) below use the standard Gaussian distribution on \(\mathbb R^m\). Define
\[
A_{i,\sigma}
=\sup_{w\in\Theta}\int_0^1
\mathbb E_u\!\left[u^TJ_i(w+t\sigma u)^TJ_i(w+t\sigma u)u\right]dt
<\infty,
\]
and
\[
B_{i,\sigma}(w)
=\int_0^1\mathbb E_u\!\left[
\sum_{k=1}^CH_{i,k}(w+t\sigma u)^Tuu^TH_{i,k}(w+t\sigma u)
\right]dt.
\]
Assume that these matrix integrals have finite entries and that
\[
B_{i,\sigma}(w)\preceq B_{i,\sigma}\qquad(w\in\Theta).
\]
Set
\[
J_{S,\sigma}=\frac1n\sum_{i=1}^nA_{i,\sigma}\operatorname{tr}G_i,
\qquad
H_{S,\sigma}=\frac1n\sum_{i=1}^n\operatorname{tr}B_{i,\sigma}.
\]

Let \(P\) be any fixed probability distribution on \(\mathbb R^m\), and fix \(\lambda>0\) and \(\delta\in(0,1]\). The distribution \(D\), hypothesis family, loss, function \(a\), prior \(P\), and all scalar parameters above are fixed independently of the sample. The matrices \(G_i,B_{i,\sigma}\) may depend on the sample as specified; the asserted conclusion will be simultaneous in \(w\), not in the prior or scalar parameters.

Use
\[
\mathrm{KL}(Q\|P)=
\begin{cases}
\displaystyle\int\log\!\left(\frac{dQ}{dP}\right)dQ,&Q\ll P,\\
+\infty,&Q\not\ll P.
\end{cases}
\]
Relative entropy and the prior exponential moment in the conclusion may be infinite; in either case the right-hand side is interpreted as \(+\infty\).

## Task

Prove that there exists a universal numerical constant \(c>0\), independent of all objects and parameters in the setup, such that, for every fixed setup satisfying these assumptions, with probability at least \(1-\delta\) over \(S\), simultaneously for every \(w\in\Theta\),
\[
L_D(h_w)\le L_S(h_w)
+\frac{2cR\sigma}{\sqrt n}\sqrt{\beta^2J_{S,\sigma}+\ell^2H_{S,\sigma}}
+8\sigma^2B\sqrt{\frac{2\ln(8/\delta)}n}
+\frac{\mathrm{KL}(Q_w\|P)+\ln\!\left(\frac{2}{\delta}\,\mathbb E_{v\sim P}\exp\!\frac{\lambda^2\ell^2a_v^2}{2n}\right)}{\lambda}.
\]
