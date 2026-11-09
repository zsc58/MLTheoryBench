# Problem

## Setup

Let \((X,T,Y(0),Y(1))\) denote a generic observation from an i.i.d. sample with joint law \(P\), where \(X\in\mathbb R^d\), \(T\in\{0,1\}\), and \(0<\Pr(T=1)<1\). Let \(P^t\) be the conditional law given \(T=t\), let \(Y=TY(1)+(1-T)Y(0)\), and assume \((Y(0),Y(1))\perp T\mid X\), \(P_X^1\ll P_X^0\), square-integrability of \(dP_X^1/dP_X^0(X)\) under \(P^0\), and square-integrability of \(Y\) under \(P\). Define
\[
\tau=\mathbb E_{P^1}[Y(1)-Y(0)].
\]
For any measurable representation \(Z=\psi(X)\), write
\[
m_0(Z)=\mathbb E_{P^0}[Y\mid Z],\qquad
\tau_Z=\mathbb E_{P^1}[Y]-\mathbb E_{P^1}[m_0(Z)].
\]
In expressions involving \(x\), \(m_0(x)\) denotes a version of the control regression \(\mathbb E_{P^0}[Y\mid X=x]\). A representation \(\phi(X)\) is deconfounding when \(\tau_{\phi(X)}=\tau\). For any random variable \(Z\) with \(P_Z^1\ll P_Z^0\), define
\[
\mathcal O(Z)=\mathbb E_{P^0}\!\left[\left(\frac{dP_Z^1}{dP_Z^0}(Z)\right)^2\right];
\]
if this absolute continuity fails, set \(\mathcal O(Z)=+\infty\).

Let \(\alpha,\beta\in\mathbb R^d\) be unit vectors, put \(\rho=\alpha^\top\beta\in(-1,1)\), and let \(m:\mathbb R\to\mathbb R\) be measurable. Consider either:

(A) \(P_X^0=N(0,I_d)\), \(m_0(x)=m(\alpha^\top x)\) for \(P_X^0\)-almost every \(x\), and
\[
\frac{dP_X^1}{dP_X^0}(x)=\frac{h(\beta^\top x)}{\mathbb E[h(Z)]},\qquad Z\sim N(0,1),
\]
where \(h:\mathbb R\to[0,\infty)\) is measurable and the normalizer is finite and positive; or

(B) \(P_X=N(0,I_d)\), and for \(P_X\)-almost every \(x\),
\[
m_0(x)=m(\alpha^\top x),\qquad e(x)=\Pr(T=1\mid X=x)=h(\beta^\top x),
\]
where \(h:\mathbb R\to[0,1)\) is measurable.

For an integer \(K\ge1\), constants \(C>1\), \(0\le\lambda<1/4\), and \(0\le\lambda'<(1-4\lambda)/6\), define \(H_{C,\lambda}^K\) as the class of \(K\)-times differentiable functions \(h:\mathbb R\to\mathbb R\) satisfying
\[
|h^{(k)}(z)|\le C\exp(\lambda z^2)\quad\text{for all }z\in\mathbb R,\ k=0,\ldots,K,
\]
and define \(H'_{C,\lambda,\lambda'}^K\) as the class of \(K\)-times differentiable functions \(h:\mathbb R\to\mathbb R\) satisfying, for all \(z\),
\[
h(z)\ge0,\qquad 1-h(z)\ge C^{-1}\exp(-\lambda' z^2),\qquad
|h^{(k)}(z)|\le C\exp(\lambda z^2)\quad (k=1,\ldots,K).
\]

## Task

Let
\[
u_+=(\alpha+\beta)/\sqrt{2+2\rho},\qquad u_-=(\alpha-\beta)/\sqrt{2-2\rho}.
\]
Prove that every unit vector
\[
\gamma=w_1u_++w_2u_-+n,
\quad n\perp\operatorname{span}\{\alpha,\beta\},\quad
\|n\|^2=1-w_1^2-w_2^2,
\]
with
\[
(1+\rho)w_1^2-(1-\rho)w_2^2=2\rho
\]
is a linear deconfounding score \(\phi_\gamma(X)=\gamma^\top X\).

All minimization statements below are over this family of unit vectors.

Under (A) with \(h\in H_{C,\lambda}^2\), or (B) with \(h\in H'_{C,\lambda,\lambda'}^2\), prove that \(\mathcal O(\gamma^\top X)\) is nondecreasing as \(|\beta^\top\gamma|\) increases within this family. If \(\rho\ne0\), \(\gamma=\alpha\) and \(\gamma=-\alpha\) are global overlap minimizers; if \(\rho=0\), every member of the family whose projection onto \(\operatorname{span}\{\alpha,\beta\}\) is \(t\alpha\) for some \(|t|\le1\) is a global minimizer.

Under any of the following strict regimes, prove that the monotonicity is strict and that the preceding minimizers are the only minimizers:

- (A) with \(h\in H_{C,\lambda}^{K+1}\) for some integer \(K\ge2\) and \(\mathbb E_{Z\sim N(0,1)}[h^{(K)}(Z)]\ne0\);
- (A) with \(h(z)=\mathbf 1\{z\le z_0\}\) for some \(z_0\in\mathbb R\);
- (A) with \(h(z)=\max\{z,0\}\);
- (B) with \(h\in H'_{C,\lambda,\lambda'}^{K+1}\) for some integer \(K\ge2\) and \(\mathbb E_{Z\sim N(0,1)}[h^{(K)}(Z)]\ne0\).
