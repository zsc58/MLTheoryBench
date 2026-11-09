# Problem

## Setup

Let \(m,n,B,T\) be positive integers, \(L>0\), \(\sigma\ge0\), and \(\varepsilon>0\). Let \(X_0\in\mathbb R^{m\times n}\) be deterministic. Let \(f:\mathbb R^{m\times n}\to\mathbb R\) be continuously differentiable with
\[
f_*:=\inf_{X\in\mathbb R^{m\times n}}f(X)>-\infty,
\qquad d=\min\{m,n\},\qquad \Delta=f(X_0)-f_*.
\]
For a matrix, \(\|\cdot\|_*\), \(\|\cdot\|_{\rm op}\), and \(\|\cdot\|_F\) denote respectively the sum, maximum, and Euclidean norm of its singular values. Assume that for all \(X,Y\),
\[
\|\nabla f(X)-\nabla f(Y)\|_*\le L\|X-Y\|_{\rm op}.
\]

Suppose \(f(X)=\mathbb E_\xi[f(X;\xi)]\), with differentiable sample losses and measurable stochastic gradients satisfying, for every deterministic \(X\),
\[
\mathbb E_\xi[\nabla f(X;\xi)]=\nabla f(X),
\qquad
\mathbb E_\xi\|\nabla f(X;\xi)-\nabla f(X)\|_F^2\le\sigma^2.
\]
The samples \(\xi_{t,i}\), for \(1\le t\le T\) and \(1\le i\le B\), are iid and independent of the initialization. At iteration \(t\), the fresh mini-batch produces
\[
\widehat G_t=\frac1B\sum_{i=1}^B\nabla f(X_{t-1};\xi_{t,i}).
\]
All expectations below are over these samples.

For a matrix \(A=U\Sigma V^\top\), use the compact singular value decomposition containing only its positive singular values and define
\(\mathcal P(A)=UV^\top\), with \(\mathcal P(0)=0\).
A run is \(\varepsilon\)-stationary in the nuclear-norm metric after \(T\) iterations when
\[
\frac1T\sum_{t=1}^T\mathbb E\|\nabla f(X_{t-1})\|_*\le\varepsilon.
\]

Consider two momentum methods, both initialized with \(V_0=0\). Each run uses parameters fixed before sampling begins.

1. **Vector-style update:**
\[
V_t=\rho V_{t-1}+\widehat G_t,
\qquad X_t=X_{t-1}-\alpha V_t.
\]
When \(\sigma\Delta>0\), set
\[
q=1-\rho=\min\left\{\frac{\sqrt{L\Delta B}}{\sigma\sqrt T},1\right\},
\qquad
\alpha=\min\{q/L,q^2/(4L)\}.
\]
When \(\sigma=0\) and \(\Delta>0\), set \(q=1\), \(\rho=0\), and \(\alpha=1/(4L)\). When \(\Delta=0\), use the zero-gap convention \(\rho=0\) and \(\alpha=0\), so that the iterates remain at \(X_0\).

2. **Polar update:**
\[
V_t=\rho V_{t-1}+\widehat G_t,
\qquad X_t=X_{t-1}-\alpha\mathcal P(V_t),
\]
where \(\alpha>0\) and \(\rho\in[0,1)\) may depend on \(L,\Delta,\sigma,B,T,d\), but not on the sampled batches.

## Task

Prove that there is a universal constant \(C\), independent of all the parameters and the objective, such that the vector-style method satisfies
\[
\frac1T\sum_{t=1}^T\mathbb E\|\nabla f(X_{t-1})\|_*
\le C\left[
\sqrt{\frac{dL\Delta}{T}}+
\left(\frac{d^2\sigma^2L\Delta}{BT}\right)^{1/4}
\right],
\]
whereas the polar method admits choices of \(\alpha,\rho\) for which
\[
\frac1T\sum_{t=1}^T\mathbb E\|\nabla f(X_{t-1})\|_*
\le C\left[
\sqrt{\frac{L\Delta}{T}}+
\frac{\sigma d}{\sqrt{BT}}+
\left(\frac{d\sigma^2L\Delta}{BT}\right)^{1/4}
\right].
\]

Deduce the respective sufficient iteration bounds
\[
T=O\left(\frac{dL\Delta}{\varepsilon^2}+
\frac{d^2\sigma^2L\Delta}{B\varepsilon^4}\right)
\]
and
\[
T=O\left(\frac{L\Delta}{\varepsilon^2}+
\frac{d^2\sigma^2}{B\varepsilon^2}+
\frac{d\sigma^2L\Delta}{B\varepsilon^4}\right),
\]
with universal implied constants, integer rounding, and a minimum of one iteration understood. Explain precisely how the polar update improves the rank dependence under this common stationarity metric.
