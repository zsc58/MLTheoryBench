# Problem

## Setup

Let \(M\) be a compact, connected, orientable smooth manifold without boundary of dimension \(m\ge1\). Let
\(h:[0,\infty)\to[0,\infty)\) be continuous, \(C^2\) on \((0,\infty)\), not identically zero, and suppose that for \(k=0,1,2\) there are constants \(c,c_k>0\) such that \(|h^{(k)}(r)|\le c_k e^{-cr}\) for every \(r>0\).

Let \(D:M\times M\to[0,\infty)\) be continuous, symmetric, vanish exactly when its arguments agree, and smooth on a neighborhood of the diagonal. Assume that
\[
 g_p:=\tfrac12\operatorname{Hess}_p\bigl(D(p,\cdot)\bigr)
\]
is positive definite for every \(p\). Let \(g\) be the resulting Riemannian metric and \(d_g\) its geodesic distance. For \(\varepsilon>0\), set
\[
 K_\varepsilon(x,y)=h\!\left(D(x,y)/\varepsilon\right),\qquad
 \mathcal L^{(\varepsilon,N)}f(x)=\sum_{j=1}^N K_\varepsilon(x,X_j)\,[f(x)-f(X_j)].
\]
Write \(dV_g\) and \(\operatorname{vol}_g(M)\) for the Riemannian volume and total volume. Define
\[
 m_0=\int_{\mathbb R^m}h(\|u\|^2)\,du,\qquad
 m_2=\int_{\mathbb R^m}u_1^2h(\|u\|^2)\,du.
\]
Use the nonnegative Laplace-Beltrami convention, characterized by
\[
 \Delta_g(ab)=a\Delta_gb+b\Delta_ga-2g(\nabla_ga,\nabla_gb).
\]
Finally, let \(X_1,\ldots,X_N\) be iid with density \(P\in C^3(M)\), \(P\ge0\), \(\int_M P\,dV_g=1\).

## Task

Prove the following integrated theorem. First, there is a constant \(K>0\), depending only on \(D\) and \(g\), such that for all \(p,q\in M\),
\[
 |D(p,q)-d_g(p,q)^2|\le K d_g(p,q)^4.
\]
Second, for every \(f\in C^3(M)\), every fixed \(x\in M\), every \(\alpha>0\), and every positive bandwidth sequence satisfying \(\varepsilon_N\to0\) and \(\varepsilon_N\ge c_0N^{-1/(m+2+\alpha)}\) for some \(c_0>0\) and all sufficiently large \(N\), prove that, almost surely,
\[
\frac{\mathcal L^{(\varepsilon_N,N)}f(x)}{N\varepsilon_N^{m/2+1}}
\longrightarrow
\frac{m_2}{2}\left[P(x)\Delta_g f(x)-2g_x(\nabla_g f(x),\nabla_g P(x))\right].
\]
In the special case of uniform sampling \(P\equiv1/\operatorname{vol}_g(M)\), the limit is \(\frac{m_2}{2\operatorname{vol}_g(M)}\Delta_g f(x)\).
