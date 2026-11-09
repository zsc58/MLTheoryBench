# Problem

## Setup

Let \(T_l:\mathbb R^{n_{l-1}}\to\mathbb R^{n_l}\), \(l=1,\ldots,L\), be Lipschitz maps. Let \(\rho_0\) be a Borel probability measure on \(\mathbb R^{n_0}\), and define recursively
\[
\rho_l=(T_l)_\#\rho_{l-1},
\qquad
(T_l)_\#\rho_{l-1}(A)=\rho_{l-1}(T_l^{-1}(A))
\]
for Borel sets \(A\).

Write \(B(z,r)=\{w:\|w-z\|_2<r\}\) for the open Euclidean ball. For a Borel probability measure \(\rho\) on a Euclidean space, define its upper and lower pointwise dimensions at \(z\) by
\[
\overline d_\rho(z)=\limsup_{r\downarrow0}\frac{\log\rho(B(z,r))}{\log r},
\qquad
\underline d_\rho(z)=\liminf_{r\downarrow0}\frac{\log\rho(B(z,r))}{\log r}.
\]
Use the convention \(\log 0=-\infty\) and interpret these limits in \([0,+\infty]\). If they agree, denote their common value by \(d_\rho(z)\). Call \(\rho\) exact-dimensional with dimension \(a\) if \(d_\rho(z)=a\) for \(\rho\)-almost every \(z\).

## Task

Prove that, for every \(l=1,\ldots,L\) and for \(\rho_{l-1}\)-almost every \(x\),
\[
\overline d_{\rho_l}(T_l(x))\leq \overline d_{\rho_{l-1}}(x),
\qquad
\underline d_{\rho_l}(T_l(x))\leq \underline d_{\rho_{l-1}}(x).
\]
Consequently, wherever both pointwise dimensions exist,
\[
d_{\rho_l}(T_l(x))\leq d_{\rho_{l-1}}(x).
\]
In particular, if every \(\rho_l\), \(l=0,\ldots,L\), is exact-dimensional with dimension \(a_l\), then
\[
a_l\leq a_{l-1}\qquad(l=1,\ldots,L).
\]
