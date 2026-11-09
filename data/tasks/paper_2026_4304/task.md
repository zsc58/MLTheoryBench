# Problem

## Setup

Condition on fixed training objects. Let \(\mathcal X\subseteq\mathbb R^p\), let \(\mathcal Y\) be a measurable response space, and let
\[
(X_1,Y_1),\ldots,(X_n,Y_n),(X_{n+1},Y_{n+1})
\]
be i.i.d. from a distribution \(P\) (under this conditioning). Let \((X,Y)\sim P\) denote a generic draw. Fix \(\alpha\in(0,1)\), a measurable score \(s:\mathcal X\times\mathcal Y\to\mathbb R\), and fixed prototypes \(w_1,\ldots,w_K\in\mathbb R^p\). Define
\[
b(x)=\operatorname*{argmin}_{1\le k\le K}\|x-w_k\|_2,
\]
using deterministic tie breaking. The prototype indices have a fixed grid placement and associated Chebyshev grid distance \(d\). For a fixed radius \(r\ge0\), set
\[
A_k=\{j:d(k,j)\le r\}.
\]

For a finite calibration index set \(S\) of size \(m\), let
\[
\ell_m=\lceil(1-\alpha)(m+1)\rceil,
\]
and let \(\widehat q_S\) be the \(\ell_m\)-th order statistic of \(\{s(X_i,Y_i):i\in S\}\) if \(\ell_m\le m\), and \(+\infty\) otherwise. Define
\[
C_\alpha(x;q)=\{y\in\mathcal Y:s(x,y)\le q\}.
\]

Write \(\pi_k=P\{b(X)=k\}\), \(K_+=\{k:\pi_k>0\}\), and
\[
I_A=\{i\in\{1,\ldots,n\}:b(X_i)\in A\},\qquad
\pi_A=\sum_{j\in A}\pi_j.
\]
For every \(k\) with \(\pi_{A_k}>0\), set \(q_k=\widehat q_{I_{A_k}}\). For \(k\in K_+\), define
\[
F_k(t)=P\{s(X,Y)\le t\mid b(X)=k\},
\]
and, for \(A\) with \(\pi_A>0\),
\[
F_A(t)=\sum_{j\in A\cap K_+}\frac{\pi_j}{\pi_A}F_j(t).
\]
Finally, define
\[
D(k,j)=\sup_t|F_k(t)-F_j(t)|,
\qquad
\varepsilon_k=\sum_{j\in A_k\cap K_+}\frac{\pi_j}{\pi_{A_k}}D(k,j).
\]
Set \(\widehat q=q_{b(X_{n+1})}\) when \(\pi_{A_{b(X_{n+1})}}>0\), and set \(\widehat q=+\infty\) otherwise. The latter event has probability zero.

## Task

Prove the following integrated claim.

For every \(k\) with \(\pi_{A_k}>0\),
\[
P\!\left\{s(X_{n+1},Y_{n+1})\le q_k\mid b(X_{n+1})\in A_k\right\}\ge1-\alpha.
\]
Moreover, for every \(k\in K_+\), the deployed prediction set satisfies
\[
P\!\left\{Y_{n+1}\in C_\alpha(X_{n+1};\widehat q)\mid b(X_{n+1})=k\right\}
\ge1-\alpha-\varepsilon_k.
\]
