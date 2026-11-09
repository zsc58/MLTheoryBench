# Problem

## Setup

Let d be a positive integer, and let
\[
B^d=\{z\in\mathbb R^d:\|z\|_2\le1\},\qquad
\mathbb S^{d-1}=\{z\in\mathbb R^d:\|z\|_2=1\}.
\]
Let P,Q be Borel probability measures supported on B^d. Fix numbers -1\le\ell_{\min}\le\ell_{\max}\le1 with \ell_{\min}<1, and set
\[
\phi_\ell(u)=u_+ + \ell u_-,\qquad u_+=\max\{u,0\},\quad u_-=\min\{u,0\}.
\]
Define the discriminator class
\[
\mathcal F=\{f:B^d\to\mathbb R:\ f(z)=\phi_\ell(\theta^\top z+\mu),\ \theta\in\mathbb S^{d-1},\ \mu\in[-1,1],\ \ell\in[\ell_{\min},\ell_{\max}]\}.
\]
For Borel probability measures R,S supported on B^d, define
\[
D(R,S)=\sup_{f\in\mathcal F}\left|\mathbb E_R f-\mathbb E_S f\right|.
\]
Given mutually independent observations X_1,\ldots,X_n with common law P and Y_1,\ldots,Y_m with common law Q, let \widehat P_n,\widehat Q_m be their empirical measures and write \widehat D_{n,m}=D(\widehat P_n,\widehat Q_m). Let \Lambda=\max\{1,|\ell_{\min}|,|\ell_{\max}|\}.

For the two-sample test use equal sample sizes n=m. Fix \alpha\in(0,1) and a deterministic real threshold sequence \eta_{\alpha,n}=o(1), and define
\[
T_n=\mathbf 1\{\widehat D_{n,n}\ge\eta_{\alpha,n}\}.
\]

## Task

Prove the following integrated theorem. There is a constant c_d=O(\sqrt d), depending only on d and the fixed slope interval, such that:

1. (**Discrimination**) D(P,Q)=0 if and only if P=Q.
2. (**Uniform estimation**) For every n,m\ge1 and every \varepsilon>0,
\[
\Pr\!\left\{|\widehat D_{n,m}-D(P,Q)|>c_d\left(\frac1{\sqrt n}+\frac1{\sqrt m}\right)+\varepsilon\right\}
\le2\exp\!\left(-\frac{\varepsilon^2nm}{8\Lambda^2(n+m)}\right).
\]
3. (**Fixed-alternative power**) If P\ne Q, then for all sufficiently large n,
\[
\Pr_{P,Q}(T_n=1)\ge1-\frac{c_3}{\sqrt n}
\]
for some finite constant c_3>0 depending on P,Q,d, and consequently \Pr_{P,Q}(T_n=1)\to1.
