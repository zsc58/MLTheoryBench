# Problem

## Setup

Two tasks use a common output coordinate system of dimension \(K\).  For each \(t\in\{i,j\}\), let \((a,e)\sim P_t\) take values in \(\mathbb R^d\times\mathbb R^K\).  Coordinates of \(e\) that do not belong to task \(t\)'s output block are zero.  Assume
\[
\mathbb E_{P_t}\|a\|_2^4<\infty,
\qquad
\mathbb E_{P_t}\|e\|_2^4<\infty.
\]

For an affine output head, define its per-example vectorized gradient and its second-moment matrix by
\[
g_t(a,e)=a\otimes e,\qquad F_t=\mathbb E_{P_t}[g_tg_t^\top].
\]
When both Frobenius norms are nonzero, define the alignment
\[
A(i,j)=\frac{\langle F_i,F_j\rangle_F}{\|F_i\|_F\|F_j\|_F}.
\]

Let \(\mathcal H\) be the reproducing-kernel Hilbert space of
\[
k\bigl((a,e),(a',e')\bigr)=(a^\top a')^2(e^\top e')^2,
\]
with feature map \(\varphi\), and define the joint mean embedding
\[
\mu_t=\mathbb E_{(a,e)\sim P_t}[\varphi(a,e)].
\]
Assume \(\|\mu_i\|_{\mathcal H},\|\mu_j\|_{\mathcal H}>0\).

For \(s=1,\ldots,m\), independently draw four mutually independent Rademacher vectors
\[
r_{a,s},r'_{a,s}\in\{-1,+1\}^d,
\qquad r_{e,s},r'_{e,s}\in\{-1,+1\}^K.
\]
Set
\[
\psi_s(a,e)=(r_{a,s}^\top a)(r_{e,s}^\top e)(r_{a,s}'{}^\top a)(r_{e,s}'{}^\top e),
\qquad
\widehat\varphi_m(a,e)=m^{-1/2}(\psi_1(a,e),\ldots,\psi_m(a,e)).
\]

## Task

Prove the following integrated claim.

\[
\langle F_i,F_j\rangle_F=\langle\mu_i,\mu_j\rangle_{\mathcal H},
\qquad
A(i,j)=\frac{\langle\mu_i,\mu_j\rangle_{\mathcal H}}
{\|\mu_i\|_{\mathcal H}\|\mu_j\|_{\mathcal H}}.
\]
Moreover, for every fixed \((a,e),(a',e')\), the factored sketch satisfies
\[
\mathbb E\left[\left\langle\widehat\varphi_m(a,e),
\widehat\varphi_m(a',e')\right\rangle\right]
=(a^\top a')^2(e^\top e')^2,
\]
and
\[
\operatorname{Var}\left(\left\langle\widehat\varphi_m(a,e),
\widehat\varphi_m(a',e')\right\rangle\right)
\leq \frac{81}{m}\|a\|_2^4\|a'\|_2^4\|e\|_2^4\|e'\|_2^4.
\]
Finally, show that evaluating \(\widehat\varphi_m(a,e)\) takes \(O(m(d+K))\) arithmetic operations using the displayed factored form, without forming a \(dK\)-dimensional gradient or a \(K\times K\) error moment.
