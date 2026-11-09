# Problem

## Setup

Let \(d\ge 1\), \([d]=\{1,\ldots,d\}\), and let \(f:2^{[d]}\to\mathbb R\). For \(S\subseteq[d]\), write \(S^c=[d]\setminus S\). Define
\[
f_{\rm odd}(S)=\frac{f(S)-f(S^c)}2,\qquad
f_{\rm even}(S)=\frac{f(S)+f(S^c)}2.
\]
Thus a function is odd if \(h(S^c)=-h(S)\) and even if \(h(S^c)=h(S)\), and every \(f\) has the unique decomposition \(f=f_{\rm odd}+f_{\rm even}\).

For player \(i\in[d]\), define the Shapley value
\[
\phi_i(f)=\sum_{S\subseteq[d]\setminus\{i\}}p_{|S|}\bigl(f(S\cup\{i\})-f(S)\bigr),
\qquad
p_\ell=\frac1d\binom{d-1}{\ell}^{-1}\quad(0\le \ell\le d-1).
\]

Let \(V\) be a finite-dimensional linear space of set functions that is closed under the odd/even projections; write \(V_o\) and \(V_e\) for its odd and even subspaces. Define the boundary-constrained affine class
\[
\mathcal F(f)=\{g\in V:g(\varnothing)=f(\varnothing),\ g([d])=f([d])\},
\]
and component classes \(\mathcal F_o(f_{\rm odd})\) and \(\mathcal F_e(f_{\rm even})\) analogously inside \(V_o,V_e\), matching both boundary values.

Let \(\mathcal S\) be a finite multiset of coalitions closed under complementation: whenever \(S\) occurs, so does \(S^c\) with the same multiplicity. Let all weights be positive and depend only on coalition size, with
\[
w_{|S|}=w_{d-|S|}.
\]
For \(g\in\mathcal F(f)\), set
\[
Q(g)=\sum_{S\in\mathcal S}w_{|S|}\bigl(f(S)-g(S)\bigr)^2.
\]

## Task

Prove the integrated theorem: for every player \(i\), \(\phi_i(f)=\phi_i(f_{\rm odd})\) (equivalently, \(\phi_i(f_{\rm even})=0\)); and the paired weighted least-squares minimizers satisfy
\[
\operatorname*{argmin}_{g\in\mathcal F(f)}Q(g)
=\operatorname*{argmin}_{g_o\in\mathcal F_o(f_{\rm odd})}Q_o(g_o)
+\operatorname*{argmin}_{g_e\in\mathcal F_e(f_{\rm even})}Q_e(g_e),
\]
where \(+\) denotes the Minkowski sum and
\[
Q_o(g_o)=\sum_{S\in\mathcal S}w_{|S|}(f_{\rm odd}(S)-g_o(S))^2,\qquad
Q_e(g_e)=\sum_{S\in\mathcal S}w_{|S|}(f_{\rm even}(S)-g_e(S))^2.
\]
