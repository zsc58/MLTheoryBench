# Reference Proof

## Proof Structure

First verify the conditional-law versions and the expectation domains. Condition first on the score information and then decompose the resulting score-level Bayes risk at the feature-information level. Finally, use strict propriety and the tower property to characterize equality in the grouping term.

## Complete Proof

### 1. Conditional laws, versions, and information nesting

Because \(s\) is measurable and \(S=s(X)\), we have \(\mathcal H_S\subseteq\mathcal H_X\). For a sub-\(\sigma\)-algebra \(\mathcal G\), each coordinate
\[
Q_{\mathcal G,y}=\mathbb E[\mathbf 1_{\{Y=y\}}\mid\mathcal G]
\]
is \(\mathcal G\)-measurable and lies in \([0,1]\) almost surely. Summing over the finite label set gives \(\sum_y Q_{\mathcal G,y}=1\) almost surely. Modifying on a \(\mathcal G\)-measurable null set if necessary gives a simplex-valued version. Coordinatewise uniqueness of conditional expectations, followed by a finite union of null sets, gives uniqueness of this vector up to almost-sure equality. No regular conditional distribution for a general feature space is needed.

The label indicators are bounded, so the ordinary integrable tower property applies. For every label \(y\),
\[
C_y
=\mathbb E[\mathbf 1_{\{Y=y\}}\mid\mathcal H_S]
=\mathbb E[\mathbb E[\mathbf 1_{\{Y=y\}}\mid\mathcal H_X]\mid\mathcal H_S]
=\mathbb E[Q_y\mid\mathcal H_S].
\tag{1}
\]

### 2. Well-defined expectations and conditional loss identities

All deterministic losses are finite, but expected score loss is not assumed finite. We establish the bounds needed to handle this distinction.

Let \(e_y\) be the point-mass probability vector at label \(y\), and put
\[
m=\min_{y\in\mathcal Y}\ell(e_y,y).
\]
This is finite. Propriety with truth \(e_y\) gives
\[
\ell(p,y)=L(p,e_y)\geq L(e_y,e_y)=\ell(e_y,y)\geq m
\]
for every \(p\) and \(y\). Fix any \(p_0\in\Delta(\mathcal Y)\), and put \(b=\max_y\ell(p_0,y)<\infty\). Again by propriety, for every \(q\),
\[
m\leq E_\ell(q)\leq L(p_0,q)\leq b.
\]
Thus generalized entropy is bounded, and every random loss considered below has a bounded negative part. Measurability of \(\ell\) and finite summation imply measurability of \(L\), \(E_\ell\), and \(d_\ell\).

For completeness, let \(T\) be a \(\mathcal G\)-measurable simplex-valued random variable. The identity
\[
\ell(T,Y)-m
=\sum_{y\in\mathcal Y}(\ell(T,y)-m)\mathbf 1_{\{Y=y\}}
\]
has nonnegative summands and \(\mathcal G\)-measurable coefficients. Conditional expectation therefore gives
\[
\mathbb E[\ell(T,Y)-m\mid\mathcal G]
=\sum_y(\ell(T,y)-m)Q_{\mathcal G,y}
=L(T,Q_{\mathcal G})-m.
\]
For unbounded coefficients, the pull-out identity follows first for their bounded truncations and then by conditional monotone convergence. The nonnegative tower property consequently yields
\[
\mathbb E[\ell(T,Y)]=\mathbb E[L(T,Q_{\mathcal G})]
\]
in the bounded-below extended sense. Since \(E_\ell(Q_{\mathcal G})\) is bounded and \(d_\ell(T,Q_{\mathcal G})\geq0\), splitting
\(L(T,Q_{\mathcal G})=d_\ell(T,Q_{\mathcal G})+E_\ell(Q_{\mathcal G})\)
is legitimate without subtracting infinite quantities.

### 3. Score-level decomposition

Apply the preceding identity with \(\mathcal G=\mathcal H_S\) and \(T=S\). Then
\[
\mathbb E[\ell(S,Y)]
=\mathbb E[L(S,C)]
=\mathbb E[d_\ell(S,C)]+\mathbb E[E_\ell(C)].
\tag{2}
\]
This remains valid if the first term, and hence the expected score loss, is infinite.

### 4. Feature-level decomposition of the intermediate Bayes risk

Because \(C\) is \(\mathcal H_S\)-measurable, conditioning its loss on \(\mathcal H_S\) gives
\[
\mathbb E[\ell(C,Y)]
=\mathbb E[L(C,C)]
=\mathbb E[E_\ell(C)].
\tag{3}
\]
The right-hand side is finite. Together with the lower bound on \(\ell(C,Y)\), this also shows that \(\ell(C,Y)\) is integrable.

Moreover, \(C\) is \(\mathcal H_X\)-measurable because \(\mathcal H_S\subseteq\mathcal H_X\). Conditioning this same loss on \(\mathcal H_X\) gives
\[
\mathbb E[\ell(C,Y)]
=\mathbb E[L(C,Q)]
=\mathbb E[d_\ell(C,Q)]+\mathbb E[E_\ell(Q)].
\tag{4}
\]
Both Bayes-risk expectations are finite, so (3)--(4) also show that the expected grouping term is finite. Substituting (3)--(4) into (2) proves
\[
\mathbb E[\ell(S,Y)]
=\mathbb E[d_\ell(S,C)]
+\mathbb E[d_\ell(C,Q)]
+\mathbb E[E_\ell(Q)].
\]
There is no cancellation of infinite quantities.

### 5. Strict propriety and measurable versions

Suppose that \(\ell\) is strictly proper. The random variable \(D=d_\ell(C,Q)\) is measurable and nonnegative. If \(\mathbb E[D]=0\), then for each positive integer \(n\),
\[
0=\mathbb E[D]\geq n^{-1}\mathbb P(D\geq n^{-1}),
\]
so \(D=0\) almost surely. The converse is immediate. Strict propriety and \(d_\ell(q,q)=0\) therefore give
\[
\mathbb E[d_\ell(C,Q)]=0
\quad\Longleftrightarrow\quad C=Q\text{ almost surely}.
\]
If this holds, the \(\mathcal H_S\)-measurable vector \(C\) is a version of \(Q\). Conversely, if \(\widetilde Q\) is an \(\mathcal H_S\)-measurable version of \(Q\), its coordinates are integrable and (1) gives
\[
C=\mathbb E[Q\mid\mathcal H_S]
=\mathbb E[\widetilde Q\mid\mathcal H_S]
=\widetilde Q=Q\quad\text{almost surely}.
\]
This proves both directions of the required equivalence. The argument also covers a single label, zero conditional label probabilities, constant scores, and coinciding information levels.

## Dependency Closure

The source conditional-law representation and uniqueness arguments are recovered in part 1. The conditional-expectation tower property is used only for bounded or integrable variables, or for nonnegative variables after the displayed finite shift; its hypotheses are verified at each use. Parts 2--4 derive the decomposition rather than citing the paper's chain theorem as a completed proof obligation. Part 5 derives the zero-expectation and version equivalences. All theorem-critical obligations are closed.
