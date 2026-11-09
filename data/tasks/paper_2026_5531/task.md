# Problem

## Setup

Let \(p,n,m\) be positive integers, and let \(\eta>0\) and \(\sigma>0\) be deterministic parameters, which may depend on \(p,n,m\). Let \(X\in\mathbb R^{p\times m}\) have independent \(N(0,I_p)\) columns. Independently of \(X\), initialize \(U(0)\in\mathbb R^{n\times p}\) with independent \(N(0,\sigma^2)\) entries. Let \(x\sim N(0,I_p)\) be an independent test vector.

For \(U\in\mathbb R^{n\times p}\), define the tied linear autoencoder \(f_U(x)=U^TUx\) and the population and training losses
\[
L(U)=\mathbb E_x\frac{\|x-U^TUx\|_2^2}{2p}
=\frac{\|I_p-U^TU\|_F^2}{2p},\qquad
\widehat L(U)=\frac{\|X-U^TUX\|_F^2}{2pm}.
\]
The training matrix is held fixed along gradient flow:
\[
\dot U(t)=-\eta\nabla_U\widehat L(U(t)).
\]
Write \(L(t)=L(U(t))\) and \(\widehat L(t)=\widehat L(U(t))\).

Define \(Y_s\) and \(\widehat Y_s\), for integer \(s\ge0\), by the formal averaged Taylor expansions at \(t=0\):
\[
\mathbb E[L(t)]\sim\frac12+\sum_{s\ge0}\left(\frac{-\eta}{pm}\right)^sY_s\frac{t^s}{s!},\qquad
\mathbb E[\widehat L(t)]\sim\frac12+\sum_{s\ge0}\left(\frac{-\eta}{pm}\right)^s\widehat Y_s\frac{t^s}{s!}.
\]
Here expectation averages each Taylor coefficient over \(U(0)\) and \(X\). The series are interpreted coefficientwise; convergence of the averaged series or of large-system loss trajectories is not asserted.

The coefficients are finite polynomials in \(p,n,m,\sigma^2\). Collecting like monomials, write
\[
Y_s=\sum_{q\in Q_s}c_{q;s}p^{q_p}n^{q_n}m^{q_m}\sigma^{q_\sigma},\qquad
\widehat Y_s=\sum_{q\in\widehat Q_s}\widehat c_{q;s}p^{q_p}n^{q_n}m^{q_m}\sigma^{q_\sigma},
\]
where \(Q_s,\widehat Q_s\subset\mathbb N_0^4\) are the supports of the collected polynomials and all displayed coefficients are nonzero real constants depending only on their indices and \(s\). These supports are taken before specializing the parameters to a scaling sequence.

Consider power-law scalings, as \(a\to\infty\),
\[
p\asymp a^{\alpha_p},\quad n\asymp a^{\alpha_n},\quad m\asymp a^{\alpha_m},\quad \sigma\asymp a^{\alpha_\sigma},
\]
where \(\alpha_p,\alpha_n,\alpha_m>0\) and \(\alpha_\sigma\in\mathbb R\). The notation \(\asymp\) means that the ratio is bounded above and below by positive constants for sufficiently large \(a\). Put \(\alpha=(\alpha_p,\alpha_n,\alpha_m,\alpha_\sigma)\). Define the maximal monomial weight and leading index set by
\[
\alpha_{Y_s}=\max_{q\in Q_s}q^T\alpha,\qquad
S_{\alpha;s}=\operatorname*{argmax}_{q\in Q_s}q^T\alpha,
\]
and define \(\alpha_{\widehat Y_s}\) and \(\widehat S_{\alpha;s}\) analogously. These are definitions based on monomial supports, not assertions excluding cancellation after numerical parameter specialization.

Define Pareto dominance by
\[
q\preceq q'\iff q_p\le q'_p,\quad q_n\le q'_n,\quad q_m\le q'_m,\quad q_\sigma=q'_\sigma.
\]
The Pareto set \(P_s\) consists of those \(q\in Q_s\) for which no distinct \(q'\in Q_s\) satisfies \(q\preceq q'\); define \(\widehat P_s\) analogously. Write \(H_s=\operatorname{conv}(P_s)\) and \(\widehat H_s=\operatorname{conv}(\widehat P_s)\).

## Formal Learning Regimes

Two admissible scaling vectors belong to the same formal learning regime when they have the same joint sequence
\[
\bigl(S_{\alpha;s},\widehat S_{\alpha;s}\bigr)_{s\ge0}.
\]
A basic extreme regime means one whose leading indices select a two-dimensional proper face at every order where the corresponding coefficient hull is three-dimensional. Combinations of basic extremes refer to nonempty lower-dimensional intersections of their maximizing faces.

The following names refer to these sets of admissible scaling vectors:

- **Large-data:** \(\alpha_m>\alpha_p=\alpha_n=-2\alpha_\sigma\).
- **Small-data:** \(\alpha_m<\alpha_p=\alpha_n=-2\alpha_\sigma\).
- **Mean-field:** \(\alpha_n=-2\alpha_\sigma>\alpha_p=\alpha_m\).
- **Narrow-latent:** \(\alpha_n<-2\alpha_\sigma=\alpha_p=\alpha_m\).
- **Free:** \(-2\alpha_\sigma<\alpha_n=\alpha_p=\alpha_m\).

## Task

Prove that, for every integer \(s\ge0\),
\[
\widehat P_s=\left\{\left(s+s_D-q_n-q_m+1,\ q_n,\ q_m,\ 2(s_D+1)\right):\begin{array}{l}
s_D\in\{0,1,\ldots,s+1\},\\
q_n\in\{1,\ldots,s_D+1\},\\
q_m\in\{0,1,\ldots,s\}
\end{array}\right\}.
\]
Moreover, prove that \(P_0=\widehat P_0\), while, for every integer \(s\ge1\),
\[
P_s=\left\{\left(s+s_D-q_n-q_m+1,\ q_n,\ q_m,\ 2(s_D+1)\right):\begin{array}{l}
s_D\in\{0,1,\ldots,s+1\},\\
q_n\in\{1,\ldots,s_D+1\},\\
q_m\in\{1,\ldots,s\}
\end{array}\right\}.
\]

Establish the associated convex-hull geometry, including the low-order cases: \(\widehat H_s\) is a three-dimensional triangular prism for \(s\ge1\), and \(H_s\) is a three-dimensional triangular prism for \(s\ge2\); the remaining hulls are triangles. For the nondegenerate prisms, identify which of the five two-dimensional boundary faces each named regime selects. Prove that these give exactly the basic extreme regimes of the joint formal coefficient hierarchy and that its lower-dimensional extreme leading sets are the nonempty intersections of those faces.
