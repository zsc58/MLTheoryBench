# Reference Proof

## Proof Structure

Show that the empirical gap is jointly Borel in the parameter and the two samples, using the prescribed zero value for empty samples. Its threshold witness set is Borel, so its projection is analytic and hence measurable in every completed finite Borel measure. Parameterize the singleton class associated with an analytic non-Borel set, compute a one-point bad event exactly, and use a section to disprove Borel measurability of the corresponding supremum. Finally, verify the implication from the supremum-Borel property to the event-completion property.

## Standard-Independent Inputs

The descriptive-set-theoretic inputs are the following standard results, recorded in theory_003 and theory_010:

1. If \(U\) is standard Borel, \(Y\) is Polish, and \(B\subseteq U\times Y\) is Borel, then its projection onto \(Y\) is analytic.
2. Every analytic subset of a Polish space is measurable in the completion of every finite Borel measure on that space.
3. Every nonempty analytic subset of \(\mathbb R\) is the range of a Borel measurable map from a standard Borel space.

These statements, rather than any paper-specific prior theorem, are the external inputs. The required finite-product fact follows directly from a standard-Borel representation: if \(U\) is measurably isomorphic to a Borel subset \(B\) of a Polish space \(Z\), then \(U\times Y\) is represented by the Borel subset \(B\times Y\) of \(Z\times Y\). The same argument applies to the product of \(U\) with the finite discrete space \(\{0,1\}\).

## Complete Proof

### 1. The parameterized class

Fix a Borel measurable target \(c\), a nonnegative integer \(m\), and \(\epsilon\in\mathbb R\). Let \(Y=X^m\times X^m\). This is Polish, including when \(m=0\), when it is a singleton.

For \(m\geq1\) and \(z=(x_1,\ldots,x_m,y_1,\ldots,y_m)\in Y\), define
\[
G(\theta,z)=\frac1m\sum_{i=1}^m
 \mathbf1\{e(\theta,y_i)\ne c(y_i)\}
-\frac1m\sum_{i=1}^m
 \mathbf1\{e(\theta,x_i)\ne c(x_i)\}.
\]
Each coordinate projection is Borel, and \(e\) and \(c\) are Borel measurable. Each disagreement indicator is therefore Borel on \(\Theta\times Y\); finite sums and differences preserve Borel measurability. Thus \(G\) is Borel. For \(m=0\), define \(G(\theta,z)=0\), as required by the empty-sample normalization. This is Borel as well.

Consequently, for every real \(\epsilon\),
\[
W=\{(\theta,z):G(\theta,z)\geq\epsilon/2\}
\]
is Borel in \(\Theta\times Y\). The range-class definition gives
\[
E_{\mathcal C_e,c,m,\epsilon}=\pi_Y(W).
\]
The parameter space \(\Theta\) is standard Borel, \(Y\) is Polish, and \(W\) is Borel, so the projection theorem applies and proves that this event is analytic. Universal measurability then makes it measurable in the completion of every finite Borel measure on \(Y\).

There is no nonemptiness assumption on \(\Theta\). If \(\Theta=\varnothing\), the witness set and its projection are empty. For \(m=0\), the event is the singleton sample space exactly when \(\Theta\ne\varnothing\) and \(\epsilon\leq0\), and otherwise is empty. If \(X=\varnothing\) and \(m\geq1\), the sample space itself is empty. All these cases are included in the argument.

For every Borel probability measure \(P\) on \(X\), \(P^m\otimes P^m\) is a finite Borel measure on \(Y\), including the usual zero-fold product when \(m=0\). Applying the preceding conclusion for \(\epsilon>0\) establishes the event-completion property. It also proves the asserted stronger analyticity and completion-measurability conclusion for all real thresholds.

### 2. The singleton class satisfies event completion

Let \(A\subseteq\mathbb R\) be analytic and non-Borel. Since the empty set is Borel, \(A\ne\varnothing\). By the stated analytic-set parametrization result, there are a standard Borel space \(U\) and a Borel measurable map \(g:U\to\mathbb R\) with range \(A\). Necessarily \(U\ne\varnothing\).

The parameter space \(\{0,1\}\times U\) is standard Borel. Define
\[
f((b,u),x)=b\,\mathbf1\{x=g(u)\}.
\]
The map \((u,x)\mapsto(g(u),x)\) is Borel, and the diagonal of \(\mathbb R^2\) is closed, so \(\{(u,x):x=g(u)\}\) is Borel. Selecting this indicator when \(b=1\) and zero when \(b=0\) therefore gives a jointly Borel evaluator.

Its range class is exactly \(\mathcal C_A\): the zero branch supplies the zero function because \(U\) is nonempty, and the other branch supplies precisely the singleton indicators at points of \(A\). The first part, applied with domain \(\mathbb R\), gives the event-completion property for \(\mathcal C_A\).

### 3. The singleton class fails the supremum-Borel property

Take \(m=1\) and the Borel target \(c\equiv0\). Identifying one-point samples with their coordinates, the zero concept has gap \(0\), and the singleton concept at \(a\in A\) has gap
\[
\mathbf1\{y=a\}-\mathbf1\{x=a\}.
\]
These values belong to \(\{-1,0,1\}\). Hence
\[
\sup_{h\in\mathcal C_A}\Gamma_h^c((x),(y))\geq\tfrac12
\quad\Longleftrightarrow\quad
 y\in A\ \text{and}\ x\ne y.
\]
Indeed, if the right-hand condition holds, the singleton at \(y\) has gap \(1\). If it fails, no singleton has gap \(1\), and the zero concept ensures that the supremum is \(0\).

Write
\[
P_A=\{(x,y):y\in A,\ x\ne y\}.
\]
The same calculation identifies \(P_A\) with \(E_{\mathcal C_A,0,1,1}\) under the coordinate identification. Thus its analyticity also follows from the first part and the evaluator just constructed.

Because \(\mathbb R\) is Borel and \(A\) is not, choose \(a_0\in\mathbb R\setminus A\). The continuous section map \(y\mapsto(a_0,y)\) has inverse image
\[
\{y:(a_0,y)\in P_A\}=A.
\]
If \(P_A\) were Borel, this inverse image would be Borel, a contradiction. Therefore the displayed superlevel set of the supremum is non-Borel. A Borel extended-real-valued map has Borel inverse images of Borel rays, so the supremum map is not Borel. This disproves the supremum-Borel property even using a Borel target.

### 4. Comparison of the properties

For a nonempty class and \(m\geq1\), all attained empirical gaps lie in the finite set
\[
\{-1,-1+1/m,\ldots,1\}.
\]
Their supremum is therefore attained. For \(m=0\), every attained gap is \(0\). For the empty class the chosen supremum is \(-\infty\). Consequently, in all cases and for every real threshold,
\[
E_{\mathcal C,c,m,\epsilon}
=\left\{(S,T):\sup_{h\in\mathcal C}\Gamma_h^c(S,T)\geq\epsilon/2\right\}.
\]
The supremum-Borel property thus makes every required positive-threshold event Borel, hence measurable in every relevant completion. Its quantification over all targets includes the Borel targets required for event completion. Together with \(\mathcal C_A\), this proves that the event-completion property is strictly weaker.

All theorem-critical obligations are closed by the displayed derivations and the three standard-independent statements with their hypotheses checked above.
