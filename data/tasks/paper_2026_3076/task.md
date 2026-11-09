# Problem

## Setup

Let X=\mathcal S\times\mathcal A be a measurable state-action space. Fix a policy-induced Markov kernel P_\pi, an initial law d_0, an offline law \nu, and \gamma\in[0,1). Assume d_0\ll\nu and \nu P_\pi\ll\nu. Define
\[
d_*=(1-\gamma)\sum_{t\ge0}\gamma^t d_0P_\pi^t,\qquad \omega_*:=\frac{dd_*}{d\nu},\qquad \omega_0:=\frac{dd_0}{d\nu},
\]
so \omega_*\in\Delta_\nu, the set of nonnegative \nu-densities of mass one. Define
\[
(B\omega)(x)=(1-\gamma)\omega_0(x)+\gamma\frac{d\{(\omega\nu)P_\pi\}}{d\nu}(x).
\]
For probability densities p,q, let D_\nu(p\Vert q)=\mathbb E_\nu[p\log(p/q)]. For nonnegative integrable p and positive q for which the expression is defined, let D_\nu^{\rm gen}(p\Vert q)=\mathbb E_\nu[p\log(p/q)-p+q], with 0\log 0=0.

Let \mathcal H be convex, closed, and totally bounded in L_2(\nu), with 0\in\mathcal H. Assume \log\omega_*\in L_2(\nu), \omega_*>0 \nu-a.e., \omega_*\ge m_*>0,
\[
\sup_{h\in\mathcal H}\|h-\mathbb E_\nu h\|_\infty\le R,\quad \|\omega_0\|_\infty\le B_0,\quad \left\|\frac{d(\nu P_\pi)}{d\nu}\right\|_\infty\le B_+.
\]
Use measurable versions of the functions in \mathcal H whose centered values obey the bound R on a common \nu-full set. Empirical suprema and selected exact minimizers below are understood to be measurable; the update is run with such minimizers. For h\in\mathcal H, set \Lambda_\nu(h)=\log\mathbb E_\nu e^h, \omega_h=e^{h-\Lambda_\nu(h)}, and \mathcal W=\{\omega_h:h\in\mathcal H\}. Let
\[
\varepsilon_{\rm KL}=\inf_{v\in\mathcal W}\|\log\omega_* -\log v\|_{L_2(\nu)}.
\]
Set \mathcal H^\circ=\{h-\mathbb E_\nu h:h\in\mathcal H\} and \mathcal H_\Delta=\{h_1-h_2:h_1,h_2\in\mathcal H^\circ\}. For a class \mathcal G under a probability law P and an integer n\ge1, let Z_1,\ldots,Z_n be iid with law P, independently of iid Rademacher signs \sigma_1,\ldots,\sigma_n, and define
\[
\mathfrak R_n(\mathcal G,r;P)=\mathbb E_{Z,\sigma}\sup_{g\in\mathcal G:\|g\|_{L_2(P)}\le r}\left|n^{-1}\sum_{i=1}^n\sigma_i g(Z_i)\right|.
\]
Let Q_{\nu,\Delta} be the law of (X,X) for X\sim\nu and Q_{\nu,\pi} the law of (X,X^+) for X\sim\nu, X^+|X\sim P_\pi, and define \mathcal G_\times and \mathfrak C_n, r_{n,\rm fit} by
\[
\mathcal G_\times=\{(x,x^+)\mapsto f(x)h_\Delta(x^+):f\in\mathcal W,h_\Delta\in\mathcal H_\Delta\},
\]
\[
\mathfrak C_n(r)=\max\{\mathfrak R_n(\mathcal H_\Delta,r;\nu),\mathfrak R_n(\mathcal H_\Delta,r;d_0),\mathfrak R_n(\mathcal G_\times,r;Q_{\nu,\Delta}),\mathfrak R_n(\mathcal G_\times,r;Q_{\nu,\pi})\},
\quad r_{n,\rm fit}=n^{-1/2}\vee\inf\{r>0:\mathfrak C_n(r)\le r^2\}.
\]
For \omega\in\Delta_\nu, let T^{\rm KL}_{\mathcal W}\omega minimize D_\nu(B\omega\Vert v) over v\in\mathcal W.

Given n iid samples X_i^0\sim d_0 independent of n iid pairs (X_i,X_i^+)\sim Q_{\nu,\pi}, write P_{n,0},P_{n,X},P_{n,+} for their empirical averages and, for positive f, define P_{n,f}^+g=P_{n,+}[f(X)g(X^+)]/P_{n,X}f. Set
\[
\widehat\Lambda_n(h)=\log\left(n^{-1}\sum_i e^{h(X_i)}\right),\qquad \widehat L_f(h)=\widehat\Lambda_n(h)-(1-\gamma)P_{n,0}h-\gamma P_{n,f}^+h.
\]
Initialize \widehat\omega^{(0)}\equiv1; choose any exact minimizer \widehat h_{k+1}\in\arg\min_{h\in\mathcal H}\widehat L_{\widehat\omega^{(k)}}(h) and set
\[
\widehat\omega^{(k+1)}(x)=\frac{e^{\widehat h_{k+1}(x)}}{n^{-1}\sum_i e^{\widehat h_{k+1}(X_i)}}.
\]

## Task

Prove the following integrated theorem. There are finite constants C_{\rm app} and C_{\rm fit} depending only on (R,B_0,B_+,m_*) such that:

1. For every \omega\in\mathcal W,
\[
D_\nu(T^{\rm KL}_{\mathcal W}\omega\Vert\omega_*)\le\gamma D_\nu(\omega\Vert\omega_*)+C_{\rm app}\varepsilon_{\rm KL}^2.
\]
Hence, for population iterates \omega^{(0)}\in\mathcal W, \omega^{(k+1)}=T^{\rm KL}_{\mathcal W}\omega^{(k)},
\[
D_\nu(\omega^{(K)}\Vert\omega_*)\le\gamma^K D_\nu(\omega^{(0)}\Vert\omega_*)+C_{\rm app}\frac{1-\gamma^K}{1-\gamma}\varepsilon_{\rm KL}^2.
\]

2. For every \delta\in(0,1), with probability at least 1-\delta, simultaneously for every K\ge0,
\[
D_\nu^{\rm gen}(\widehat\omega^{(K)}\Vert\omega_*)\le C_{\rm fit}\rho^K D_\nu^{\rm gen}(\widehat\omega^{(0)}\Vert\omega_*)+C_{\rm fit}\frac{\varepsilon_{\rm KL}^2}{1-\gamma}+C_{\rm fit}\frac{r_{n,\rm fit}^2+\log(1/\delta)/n}{(1-\gamma)^2},\quad \rho=\frac{1+\gamma}{2}.
\]
