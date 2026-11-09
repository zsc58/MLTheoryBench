# Reference Proof

## Proof Structure

First, symmetry forces every convex classwise loss to be both convex and concave, hence affine. Permutation invariance then reduces all linear coefficients to one target coefficient and one off-target coefficient. Symmetry, monotonicity, and nontriviality determine their signs and ratio, yielding the centered linear loss up to a positive scale and a common additive constant. Finally, at an equal-score vector, differentiating permutation invariance and symmetry shows that the first-order approximation has the same structural properties, so the affine characterization applies to it.

## Complete Proof

Write \(L_y(z)=L(z,y)\).

### Global characterization

Suppose \(L\) satisfies the hypotheses in part (a). By symmetry, there is a constant \(K\) such that
\[
\sum_{j=1}^C L_j(z)=K
\qquad\text{for every }z\in\mathbb R^C.
\]
For each fixed \(y\),
\[
L_y(z)=K-\sum_{j\ne y}L_j(z).
\]
Every \(L_j\) is convex, so the right-hand side is concave. Thus \(L_y\) is both convex and concave on \(\mathbb R^C\), and consequently it is affine. Hence
\[
L_y(z)=c_y+\sum_{k=1}^C a_{y,k}z_k.
\]

Permutation invariance constrains these coefficients. A permutation fixing \(y\) can exchange any two coordinates different from \(y\), so all off-target coefficients in row \(y\) are equal. A permutation sending one label to another shows that the target coefficients are equal across labels, the off-target coefficients are equal across labels, and the intercepts are equal. Therefore there are constants \(c,d,e\) such that
\[
L_y(z)=c+d z_y+e\sum_{k\ne y}z_k.
\]

Summing over \(y\) gives
\[
\sum_{y=1}^C L_y(z)
 =Cc+\bigl(d+(C-1)e\bigr)\sum_{k=1}^Cz_k.
\]
Since this expression is independent of \(z\),
\[
d+(C-1)e=0. \tag{1}
\]
Non-increasingness in the target score gives \(d\le 0\). If \(d=0\), equation (1) gives \(e=0\), and the common-intercept formula would make \(L\) constant, contrary to nontriviality. Thus \(d<0\).

Set
\[
b=-\frac{C}{C-1}d>0.
\]
Equation (1) gives \(e=-d/(C-1)=b/C\), while \(d=-b(C-1)/C\). Consequently
\[
L(z,y)=c+b\left(-z_y+\frac1C\sum_{k=1}^Cz_k\right)=c+bU(z,y).
\]
This proves the asserted necessity.

Conversely, let \(L=c+bU\) with \(b>0\). It is affine and hence convex, and it is nontrivial. Its target-coordinate slope is
\[
-b+\frac bC=-\frac{b(C-1)}C<0,
\]
so it is non-increasing in the target score. The formula is unchanged by simultaneous permutation of scores and labels. Moreover,
\[
\sum_{y=1}^C U(z,y)
=-\sum_{y=1}^Cz_y+\frac1C\sum_{y=1}^C\sum_{k=1}^Cz_k=0,
\]
so \(\sum_yL(z,y)=Cc\), independently of \(z\). Thus all the hypotheses hold, completing part (a).

### Local characterization

Now suppose \(L\) satisfies the hypotheses in part (b), and put \(z^\star=t\mathbf 1\). For each label let
\[
q_y=L(z^\star,y),\qquad g_y=\nabla_zL(z^\star,y).
\]
Because every coordinate permutation fixes \(z^\star\), permutation invariance shows that all \(q_y\) are equal. Differentiating
\[
L(\pi z,\pi(y))=L(z,y)
\]
at \(z=z^\star\) shows that the gradients transform by the same coordinate permutations. It follows directly that
\[
A(z,y)=q_y+g_y^\top(z-z^\star)
\]
is permutation invariant.

Symmetry gives \(\sum_yL(z,y)=K\). Differentiating this identity at \(z^\star\) yields
\[
\sum_{y=1}^C g_y=0.
\]
Therefore
\[
\sum_{y=1}^C A(z,y)
 =\sum_{y=1}^C q_y+
 \left(\sum_{y=1}^C g_y\right)^\top(z-z^\star)
 =K,
\]
so \(A\) is symmetric. Since each one-variable restriction obtained by varying only \(z_y\) is differentiable and non-increasing at \(z^\star\),
\[
(g_y)_y\le 0.
\]
Thus the affine loss \(A\) is non-increasing in its target score. The assumed nonzero gradient makes \(A\) nontrivial. It is affine, hence convex, so part (a) applies and gives constants \(a\in\mathbb R\) and \(b>0\) such that
\[
A(z,y)=a+bU(z,y).
\]
This proves part (b).
