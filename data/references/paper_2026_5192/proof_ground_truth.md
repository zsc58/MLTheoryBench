# Reference Proof

## Proof Structure

Establish a local co-Lipschitz bound for the prediction map on its full-rank tangent space. Pack that local ball, transfer separation to limiting hidden means using prediction accuracy and decoder Lipschitzness, and compare the resulting packing after orthogonal projection onto the affine subspace. The conditional stability assumption is part of the source setting; the geometric argument uses the stipulated limiting means directly and does not infer pointwise conditional convergence from averaged stability.

## Complete Proof

### Step 1: Finiteness and a local lower bound

First, the diameter assumption and the fact that \(b\in S\) imply, for every \(z\in U\),
\[
0\le\operatorname{dist}(m(z),S)
\le\|m(z)-b\|
\le M+\|m(z_0)-b\|.
\]
Consequently \(0\le\varepsilon<\infty\).

Write \(A=Dg(z_0)|_E\). The space \(E\) has dimension \(d_0\), and the singular values of \(A\) are precisely the nonzero singular values of \(Dg(z_0)\). Hence
\[
\|Av\|_2\ge s_0\|v\|_2\qquad(v\in E).
\]

Since \(z_0\) is an interior point of \(U\) and \(g\) is \(C^1\) near \(z_0\), continuity of its derivative permits a choice of \(r_{\rm loc}\in(0,r_0]\) such that \(B(z_0,r_{\rm loc})\subseteq U\), this ball lies in a neighborhood on which \(g\) is \(C^1\), and
\[
\|(Dg(w)-Dg(z_0))|_E\|_{\rm op}\le s_0/2
\qquad(w\in B(z_0,r_{\rm loc})).
\]
This radius is chosen before \(\rho\).

Put \(c=s_0/2\) and
\[
U_E=(z_0+E)\cap B(z_0,r_{\rm loc}).
\]
For \(z,z'\in U_E\), the segment joining them lies in \(U_E\), and \(v=z-z'\in E\). The fundamental theorem of calculus therefore gives
\[
\begin{aligned}
\|g(z)-g(z')\|_2
&\ge\|Av\|_2-
\int_0^1\|(Dg(z'+tv)-Dg(z_0))v\|_2\,dt\\
&\ge(s_0-s_0/2)\|v\|_2
=c\|z-z'\|_2.
\end{aligned}
\]

### Step 2: A finite separated set and separation of its hidden means

Fix any \(0<\rho<r_{\rm loc}\) with \(c\rho>2\delta\). Choose a maximal subset \(\{z_1,\ldots,z_N\}\subset U_E\) whose distinct points have distance at least \(\rho\).

Such a finite maximal set exists. Indeed, for any finite \(\rho\)-separated subset of \(U_E\), the open balls of radius \(\rho/2\) about its points, taken inside \(z_0+E\), are disjoint and lie in the ball of radius \(r_{\rm loc}+\rho/2\) about \(z_0\). Comparing \(d_0\)-dimensional volumes bounds its cardinality by \((1+2r_{\rm loc}/\rho)^{d_0}\). Thus a process of adding points while preserving separation must stop after finitely many additions.

Maximality implies that the open balls of radius \(\rho\) centered at \(z_1,\ldots,z_N\) cover \(U_E\). If \(\omega_{d_0}\) is the volume of the unit ball in \(\mathbb R^{d_0}\), volume subadditivity gives
\[
\omega_{d_0}r_{\rm loc}^{d_0}
\le N\omega_{d_0}\rho^{d_0},
\qquad
N\ge(r_{\rm loc}/\rho)^{d_0}.
\]
In particular, \(N>1\).

Let \(q_i=m(z_i)\). For \(i\ne j\), the local bound, prediction accuracy, and the triangle inequality yield
\[
\begin{aligned}
\|D(q_i)-D(q_j)\|_2
&\ge\|g(z_i)-g(z_j)\|_2
-\|D(q_i)-g(z_i)\|_2
-\|D(q_j)-g(z_j)\|_2\\
&\ge c\rho-2\delta.
\end{aligned}
\]
The decoder condition, which is only used at hidden means, consequently gives
\[
\|q_i-q_j\|\ge\lambda,
\qquad
\lambda=\frac{c\rho-2\delta}{L}>0.
\]

### Step 3: Projection and the upper packing comparison

Suppose first that \(\lambda>2\varepsilon\). Let \(P_S\) be affine orthogonal projection onto \(S=b+V\), and put
\[
y_i=P_Sq_i,\qquad r_i=q_i-y_i.
\]
Then \(r_i\in V^\perp\), \(\|r_i\|\le\varepsilon\), and \(y_i-y_j\in V\). Since \(\lambda>0\), it is legitimate to square the hidden-mean separation estimate. Orthogonality gives
\[
\begin{aligned}
\|y_i-y_j\|^2
&=\|q_i-q_j\|^2-\|r_i-r_j\|^2\\
&\ge\lambda^2-4\varepsilon^2.
\end{aligned}
\]
Thus the projected points are separated by at least
\[
\Delta=\sqrt{\lambda^2-4\varepsilon^2}>0.
\]

Orthogonal projection is nonexpansive on differences, so the diameter assumption implies
\[
\|y_i-y_1\|\le\|q_i-q_1\|\le M.
\]
The open \(k_\star\)-dimensional balls in \(S\), centered at the \(y_i\) and having radius \(\Delta/2\), are pairwise disjoint. They are contained in the ball in \(S\) of radius \(M+\Delta/2\) centered at \(y_1\). Comparing their volumes gives
\[
N(\Delta/2)^{k_\star}
\le(M+\Delta/2)^{k_\star},
\qquad
N\le\left(1+\frac{2M}{\Delta}\right)^{k_\star}.
\]
This comparison also holds when \(M=0\); it then bounds \(N\) by one, so the present branch cannot occur with \(N>1\).

Combining the lower and upper comparisons, whenever \(\lambda>2\varepsilon\), yields
\[
(r_{\rm loc}/\rho)^{d_0}
\le\left(1+\frac{2M}{\sqrt{\lambda^2-4\varepsilon^2}}\right)^{k_\star}.
\]

### Step 4: The asserted lower bound and all cases

Set
\[
B=(r_{\rm loc}/\rho)^{d_0/k_\star}>1.
\]
If \(\lambda\le2\varepsilon\), then
\[
\varepsilon\ge\lambda/2
\ge\frac12\left[\lambda^2-
\left(\frac{2M}{B-1}\right)^2\right]_+^{1/2}.
\]

Otherwise \(\lambda>2\varepsilon\), so Step 3 and the positivity of \(k_\star\) imply
\[
B\le1+\frac{2M}{\sqrt{\lambda^2-4\varepsilon^2}}.
\]
Multiplying by the positive square root and dividing by \(B-1>0\) gives
\[
\sqrt{\lambda^2-4\varepsilon^2}\le\frac{2M}{B-1}.
\]
Squaring these nonnegative quantities and rearranging yields
\[
4\varepsilon^2\ge\lambda^2-
\left(\frac{2M}{B-1}\right)^2.
\]
Together with \(\varepsilon\ge0\), this proves
\[
\varepsilon\ge\frac12\left[\lambda^2-
\left(\frac{2M}{B-1}\right)^2\right]_+^{1/2}.
\]
Substitution of \(\lambda\) and \(B\) proves the required formula. This covers a zero or negative bracket without a positivity assumption on the bound, and it does not require \(d_0>k_\star\). If no \(\rho\in(0,r_{\rm loc})\) satisfies \(c\rho>2\delta\), the universal assertion about such \(\rho\) is vacuous. The radius was already chosen independently of \(\rho\), as required.

## Proof-Obligation Audit

- Finite confinement radius: derived directly from the hidden-mean diameter and one fixed finite hidden mean.
- One common local radius and the constant \(s_0/2\): derived from continuity of the derivative and integration along segments.
- Finite maximal separated set and its cardinality lower bound: established by disjoint-ball and covering volume comparisons.
- Hidden-mean separation: derived using the two approximation errors and decoder Lipschitzness only on the hidden-mean image.
- Projected separation and dimension-sensitive cardinality upper bound: derived from orthogonality, nonexpansiveness, and disjoint-ball volumes.
- Final rearrangement: proved with all relevant sign, zero-bracket, zero-diameter, and empty-scale cases covered.

The Euclidean volume facts are the standard-independent material theory_013; their relevant statements, proofs, and hypotheses are explicit here. No nonstandard dependency or unresolved theorem-critical obligation remains.
