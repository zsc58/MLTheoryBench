# Reference Proof

## Proof Structure

The proof closes five obligations: (1) averaging and lifting respect the box domains and averaging preserves color sums; (2) averaging cannot increase the objective; (3) averaging preserves original feasibility and every reduced feasible point lifts to an original feasible point; (4) the reduced functions are well-defined and convex; and (5) both asserted optimality implications hold. The first-order convexity inequality used below is derived directly on the box, so no global extension of convexity, constraint qualification, or specialized external result is required.

## Complete Proof

### 1. Domains and color sums

Write
\[
B=\prod_{T\in Q}[\ell_T,u_T],\qquad
D_Q=\{x\in D:x_j=x_k\text{ whenever }j,k\in T\text{ for some }T\in Q\}.
\]
For each \(T\in Q\),
\[
(A_Qx)_T=\frac1{|T|}\sum_{j\in T}x_j,
\qquad (L_Qy)_j=y_T\quad(j\in T).
\]
Every color is nonempty, so these averages are defined. For \(x\in D\), common bounds within each color give
\[
\ell_T\le \frac1{|T|}\sum_{j\in T}x_j\le u_T.
\]
Thus \(A_Qx\in B\). Conversely, if \(y\in B\), then \(L_Qy\in D_Q\). In particular, for
\[
\hat x=L_QA_Qx
\]
we have \(\hat x\in D_Q\) and
\[
\sum_{j\in T}\hat x_j=\sum_{j\in T}x_j
\quad\text{for every }T\in Q.
\]
These claims also hold when a color has a single coordinate or its common lower and upper bounds coincide.

### 2. Objective inequality

First derive the needed convexity inequality. Let \(h\) be any differentiable convex function on \(D\), and let \(a,z\in D\). For \(0<t\le1\), the segment point \(a+t(z-a)\) lies in \(D\), and convexity gives
\[
h(a+t(z-a))\le (1-t)h(a)+t h(z).
\]
Consequently,
\[
\frac{h(a+t(z-a))-h(a)}t\le h(z)-h(a).
\]
Letting \(t\downarrow0\) and using differentiability yields
\[
h(z)\ge h(a)+\nabla h(a)\cdot(z-a).
\]
This argument uses only points in the box. At a boundary point it uses the derivative along the displayed feasible segment; a fixed coordinate has zero displacement. The case \(z=a\) is immediate.

Now fix \(x\in D\) and set \(\hat x=L_QA_Qx\). For each \(T\in Q\), let \(c_T\) denote the common value of \(\partial_jF(\hat x)\) for \(j\in T\). By preservation of color sums,
\[
\nabla F(\hat x)\cdot(x-\hat x)
=\sum_{T\in Q}c_T\left(\sum_{j\in T}x_j-\sum_{j\in T}\hat x_j\right)=0.
\]
Applying the preceding convexity inequality with \(h=F\), \(a=\hat x\), and \(z=x\) gives
\[
F(L_QA_Qx)=F(\hat x)\le F(x).
\]
More generally, the same calculation shows that \(\hat x\) minimizes \(F\) among points \(z\in D\) having the same color sums as \(x\). This auxiliary minimization is over the intersection of the affine slice with \(D\), not over points outside the domain of \(F\).

### 3. Feasibility in both directions

Fix \(S\in P\), and put
\[
H_S=\sum_{i\in S}G_i.
\]
This function is differentiable and convex: its differential is the sum of those of the \(G_i\), and its convexity follows by summing their defining convexity inequalities. At \(\hat x\), the coordinates of \(\nabla H_S(\hat x)\) agree within each variable color. The same color-sum calculation therefore gives
\[
\nabla H_S(\hat x)\cdot(x-\hat x)=0,
\qquad H_S(\hat x)\le H_S(x).
\]
Suppose now that \(x\) is original-feasible. Write \(b_S\) for the common value of \(b_i\) on \(S\). Then
\[
H_S(x)=\sum_{i\in S}G_i(x)\le |S|b_S.
\]
Because \(\hat x\in D_Q\), all values \(G_i(\hat x)\), \(i\in S\), coincide. Calling their common value \(d_S\), we obtain
\[
|S|d_S=H_S(\hat x)\le H_S(x)\le |S|b_S.
\]
Since \(|S|>0\), this proves \(G_i(\hat x)\le b_i\) for every \(i\in S\). Doing this for every constraint color proves that \(\hat x\) is original-feasible. Its representative inequalities show that \(A_Qx\) is reduced-feasible.

Conversely, let \(y\in B\) satisfy the reduced inequalities and set \(x=L_Qy\). The first part gives \(x\in D_Q\). For any \(S\in P\) and \(i\in S\), the assumptions yield
\[
G_i(x)=G_{i_S}(x)\le b_{i_S}=b_i.
\]
Thus \(L_Qy\) is original-feasible. If there are no inequality constraints, these arguments have no constraint colors to check and box feasibility is sufficient.

### 4. Reduced functions and convexity

On \(B\), define
\[
F_Q(y)=F(L_Qy),\qquad
G_{Q,S}(y)=G_{i_S}(L_Qy).
\]
The functions are defined because \(L_QB\subseteq D\). At every lifted point, constraints in a given color have equal values and equal right-hand sides. Consequently, any representative gives the same reduced constraint function on \(B\), and its inequality is equivalent to all inequalities in that color at the lifted point.

For \(y,z\in B\) and \(t\in[0,1]\), the point \((1-t)y+tz\) belongs to \(B\), and linearity gives
\[
L_Q((1-t)y+tz)=(1-t)L_Qy+tL_Qz.
\]
For \(h=F\) or \(h=G_{i_S}\), convexity on \(D\) therefore gives
\[
h(L_Q((1-t)y+tz))
\le (1-t)h(L_Qy)+t h(L_Qz).
\]
This is exactly convexity of every reduced objective or constraint function on the reduced box. The box inequalities themselves are affine.

### 5. Optimality in both directions

Let \(x^*\) be an original optimum, and put \(y^*=A_Qx^*\) and \(\hat x^*=L_Qy^*\). Both \(y^*\) and \(\hat x^*\) are feasible in their respective programs. The objective inequality and original optimality give the two inequalities
\[
F(\hat x^*)\le F(x^*)\le F(\hat x^*).
\]
Hence
\[
F_Q(y^*)=F(\hat x^*)=F(x^*).
\]
For any reduced feasible \(y\), its lift is original-feasible, so
\[
F_Q(y)=F(L_Qy)\ge F(x^*)=F_Q(y^*).
\]
Thus \(A_Qx^*\) is reduced-optimal.

Conversely, let \(y^*\) be reduced-optimal and set \(x^*=L_Qy^*\). Its lift is original-feasible. For any original feasible \(x\), its average \(A_Qx\) is reduced-feasible, so
\[
F(x^*)=F_Q(y^*)\le F_Q(A_Qx)=F(L_QA_Qx)\le F(x).
\]
Therefore \(L_Qy^*\) is original-optimal.

No existence or uniqueness of an optimizer was assumed. If one feasible set is empty, the feasibility implications show that the other is empty as well, and the conditional optimality assertions are vacuous. The argument does not assert that every original optimum is color-constant or that averaging is injective on the original optimal set. All five proof obligations are closed.
