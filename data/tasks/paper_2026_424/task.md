# Problem

Prove that there are universal constants \(c,C_1,C_2>0\) for which the following assertion holds.

## Setup

Let \(m,n\ge2\) and \(1\le r\le\min\{m,n\}\) be integers, and let \(k=r\). Let \(L\in\mathbb R^{m\times n}\) be fixed, with
\[
L=U\Sigma V^T,
\]
where \(U\in\mathbb R^{m\times r}\) and \(V\in\mathbb R^{n\times r}\) have orthonormal columns, \(\Sigma\) is invertible diagonal, and
\[
\max_i\|U_{i,:}\|_2\le\sqrt{\mu r/m},\qquad
\max_j\|V_{j,:}\|_2\le\sqrt{\mu r/n}
\]
for some \(\mu\ge1\).

Let \(S\in\mathbb R^{m\times n}\) have mutually independent real-valued entries with
\(\Pr(S_{ij}\ne0)=p\), where \(0<p\le1\). The distributions of their nonzero values are otherwise unrestricted. Set \(M=L+S\) and
\[
\delta_{ij}=1_{\{S_{ij}\ne0\}},\qquad
\Omega=\{(i,j):\delta_{ij}=1\}.
\]
Thus the support indicators are independent Bernoulli\((p)\) variables. Assume
\[
p\le\frac c{\log(mn)},\qquad
r\le c\sqrt{\frac{\min\{m,n\}}{\mu\log^2(mn)}}.
\]

Define
\[
f(X,Y)=\|XY^T-M\|_1,
\qquad (X,Y)\in\mathbb R^{m\times r}\times\mathbb R^{n\times r},
\]
where \(\|\cdot\|_1\) is the entrywise \(\ell_1\)-norm. Define the true-factorization set
\[
\mathcal L=\{(X,Y):X\in\mathbb R^{m\times r},\ Y\in\mathbb R^{n\times r},\ XY^T=L,\ \operatorname{rank}X=\operatorname{rank}Y=r\}
\]
and the linear space
\[
T=\{HV^T+UK^T:H\in\mathbb R^{m\times r},\ K\in\mathbb R^{n\times r}\}.
\]
Write \(P_\Omega\) and \(P_{\Omega^c}\) for the coordinate projections onto the support and its complement.

For a locally Lipschitz function, \(\partial f\) denotes its Clarke subdifferential; a point is Clarke critical if \(0\in\partial f\) there. The entrywise sign mapping is defined by \(\operatorname{sign}(z)=z/|z|\) for \(z\ne0\) and \(\operatorname{sign}(0)=[-1,1]\). Write \(\sigma_r(A)\) for the \(r\)-th largest singular value of a matrix \(A\), and define
\[
d((X,Y),\mathcal L)=\inf_{(X',Y')\in\mathcal L}
\sqrt{\|X-X'\|_F^2+\|Y-Y'\|_F^2}.
\]

## Task

Show that, with probability at least
\[
1-\exp[-C_2r\log^2(mn)]
\]
over the random support, there is an \(\varepsilon\in(0,1)\) such that simultaneously:

1. For every \(W\in T\),
\[
\|P_\Omega W\|_1\le C_1\left[
\sqrt{p\log(mn)}+
\frac{\mu r^2\log^2(mn)}{\min\{m,n\}}+
 r\log(mn)\sqrt{\frac\mu{\min\{m,n\}}}
\right]\|W\|_1
\le\frac{1-\varepsilon}{2}\|W\|_1.
\]

2. Every \((X_*,Y_*)\in\mathcal L\) is Clarke critical and is a sharp local minimum in the following precise sense: there exists \(\rho>0\), depending on \((X_*,Y_*)\), such that whenever
\[
\sqrt{\|X-X_*\|_F^2+\|Y-Y_*\|_F^2}\le\rho,
\]
we have
\[
f(X,Y)-f(X_*,Y_*)\ge
\frac\varepsilon8\min\{\sigma_r(X_*),\sigma_r(Y_*)\}\,
 d((X,Y),\mathcal L).
\]

The constant \(c\) is chosen sufficiently small but is otherwise universal. The constants \(C_1\) and \(C_2\) are universal and need not be equal.
