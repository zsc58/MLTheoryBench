# Problem

## Setup

Let \(V\) be a nonempty finite alphabet, let \(\mathtt m\notin V\), let \(L\geq1\) be an integer, and set \(\mathcal X=(V\cup\{\mathtt m\})^L\). Let \(\alpha:[0,1]\to[0,1]\) be a smooth nondecreasing masking schedule satisfying
\[
\alpha(0)=0,\qquad \alpha(1)=1,\qquad \alpha(t)<1\quad(0\leq t<1),
\]
and define \(\lambda(t)=\alpha'(t)/(1-\alpha(t))\) for \(0\leq t<1\). All time integrals below are over \([0,1)\).

Fix \(r:V^L\to\mathbb R\), \(A>0\), \(0\leq a<A\), and \(0<h\leq A-a\). Let \(\rho^0\) and \(\rho^+\) be probability laws on \(V^L\) satisfying
\[
\rho^+(z)=\frac{\rho^0(z)e^{hr(z)}}Z,
\qquad Z=\sum_{z\in V^L}\rho^0(z)e^{hr(z)}\in(0,\infty),
\]
and write \(W=e^{hr(X_1)}\).

Let \(\mathbb P^0\) and \(\mathbb P^+\) be masked-CTMC path laws, both starting at \(\mathtt m^L\), with terminal laws \(\rho^0\) and \(\rho^+\), respectively. Paths are right-continuous on \([0,1)\), change only by revealing one currently masked coordinate, and have terminal value \(X_1=\lim_{t\uparrow1}X_t\). Assume the conditional law of the entire path given \(X_1\) is identical under these two laws. Write \(\mathbb E_0\) and \(\mathbb E_+\) for their expectations. For \(t<1\) and \(x^i=\mathtt m\), define
\[
q_t^0(v\mid x,i)=\mathbb P^0(X_1^i=v\mid X_t=x),\qquad
q_t^+(v\mid x,i)=\mathbb P^+(X_1^i=v\mid X_t=x).
\]
Use measurable versions of these probability kernels; their values at conditioning states of probability zero may be chosen arbitrarily.

A candidate local-kernel family \(q\) consists of probability vectors \(q_t(\cdot\mid x,i)\) on \(V\), measurable in \(t\), for every \(t<1\), \(x\in\mathcal X\), and \(i\in\{1,\ldots,L\}\) with \(x^i=\mathtt m\). Its rates are
\[
R_t^q(x,x[x^i\leftarrow v])=\lambda(t)q_t(v\mid x,i),
\qquad x^i=\mathtt m,\quad v\in V,
\]
where \(x[x^i\leftarrow v]\) denotes replacement of coordinate \(i\) by \(v\). All other off-diagonal rates are zero, and the diagonal is minus the total exit rate. Assume specifically that \(\mathbb P^0\) and \(\mathbb P^+\) have rates \(R^{q^0}\) and \(R^{q^+}\), respectively. For any candidate \(q\), let \(\mathbb P_q\) be the CTMC starting at \(\mathtt m^L\) with rates \(R^q\) and the same terminal left-limit convention, and let \(\rho_q\) be its terminal law.

Fix \(c\in\mathbb R\) and define the possibly signed target
\[
T_c(v\mid X_t,i,X_1)=
\frac{c q_t^0(v\mid X_t,i)+(W-c)\mathbf1\{X_1^i=v\}}W.
\]
For probability vectors, let
\(\operatorname{CE}(s\|q)=-\sum_{v\in V}s(v)\log q(v)\).
For signed vectors and strictly positive \(q\), use the same linear formula. Define
\[
\mathcal L_c(q)=\int_0^1\lambda(t)\mathbb E_0\!\left[
\sum_{i:X_t^i=\mathtt m}W\operatorname{CE}\bigl(T_c(\cdot\mid X_t,i,X_1)\|q_t(\cdot\mid X_t,i)\bigr)
\right]dt.
\]
The expectation in this definition is interpreted by first conditioning on \(X_t\) and averaging each coefficient \(WT_c(v\mid X_t,i,X_1)\), and only then multiplying by \(-\log q_t(v\mid X_t,i)\) and summing. This convention also defines the loss when candidate probabilities vanish; it does not require assigning a value to a samplewise difference of positive and negative infinities. Use \(0(-\log0)=0\), and a positive coefficient times \(-\log0\) has value \(+\infty\). For KL divergence between probability vectors use \(\operatorname{KL}(p\|q)=\sum_vp(v)\log(p(v)/q(v))\), with zero-mass terms equal to zero and a term with \(p(v)>0=q(v)\) equal to \(+\infty\).

The schedule-weighted measure on time, state, and coordinate is
\[
\mu(dt,\{x\},\{i\})
=\lambda(t)\mathbb P^0(X_t=x)\mathbf1\{x^i=\mathtt m\}\,dt.
\]

## Task

Prove the following integrated claim.

1. \(\mathcal L_c\) is uniquely minimized by \(q=q^+\), up to \(\mu\)-null sets.
2. For every candidate kernel family \(q\), allowing extended-real quantities,
\[
\operatorname{KL}(\rho^+\|\rho_q)
\leq\frac{\mathcal L_c(q)-\mathcal L_c(q^+)}Z.
\]
