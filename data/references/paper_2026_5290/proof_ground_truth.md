# Reference Proof

## Proof Structure

1. Use the independent rows of each true task Jacobian to convert the sampled support-witness condition into a row-wise support restriction on the witness.
2. Combine that restriction with a nonzero determinant matching of the inverse reparameterization to obtain row-wise support inclusion after one permutation.
3. Use global sparsity to make all inclusions equalities.
4. Use the resulting block-zero inverse Jacobian to factor and locally invert each task block.

## Standard Background and Conventions

The analytical background used is the standard independent finite-dimensional inverse function theorem: if a map between open subsets of equal-dimensional Euclidean spaces is continuously differentiable and its derivative is invertible at a point, then its restriction to suitable neighborhoods is a continuously differentiable bijection with continuously differentiable inverse. Its hypotheses are verified below for each nonempty task block. No specialized external identifiability result is used.

Use the usual conventions that an empty family spans the zero subspace, an empty coordinate tuple belongs to the singleton space \(\mathbb R^0\), and the unique map from that singleton to itself is invertible. If a working neighborhood is empty, all its structural supports are empty and the conclusion is vacuous, with any permutation and these empty-coordinate maps. Otherwise proceed on the fixed neighborhoods \(V\) and \(\widehat V\). Support sets always refer to these original working neighborhoods, even when smaller neighborhoods are used to construct local inverse maps.

## Complete Proof

Write \(S_i=I_i\) and \(\widehat S_i=\widehat I_i\). The task-map equivalence and the chain rule give
\[
 J_{\widehat U}(\widehat z)=J_U(z)D\phi^{-1}(\widehat z),\qquad \widehat z=\phi(z).
\]

### 1. Row-wise support restriction

Fix an output index \(i\). For every \(q\notin\widehat S_i\), the \(q\)-th entry of the estimated Jacobian row vanishes throughout \(\widehat V\), hence also at every \(\widehat z_i^{(\ell)}\). The sampled support-witness assumption therefore gives
\[
 (J_U(z_i^{(\ell)}))_{i,\cdot}M_{\cdot q}=0,
 \qquad \ell=1,\ldots,r_i.
\]
Each sampled true row is supported on \(S_i\). The \(r_i=|S_i|\) independent rows consequently form a basis of the coordinate subspace
\[
 E_{S_i}=\{v\in\mathbb R^d:v_j=0\text{ for }j\notin S_i\}.
\]
For each \(j\in S_i\), express the coordinate row vector \(e_j^\top\) as a linear combination of those sampled rows and multiply by \(M_{\cdot q}\). This yields \(M_{jq}=0\). Thus
\[
 \operatorname{supp}(M_{j,\cdot})\subseteq\widehat S_i
 \quad\text{for every }j\in S_i. \tag{4}
\]
When \(S_i\) is empty, this restriction is vacuous and the same argument uses the zero-dimensional coordinate subspace.

### 2. A common permutation

Choose any point \(\widehat z_*\in\widehat V\). Since \(\phi\) is a \(C^1\) diffeomorphism, \(D\phi^{-1}(\widehat z_*)\) is invertible. Its determinant expansion therefore contains a nonzero permutation term. There is a permutation \(\pi\) of \([d]\) such that
\[
 (D\phi^{-1}(\widehat z_*))_{j,\pi(j)}\ne0
 \quad\text{for every }j\in[d].
\]
Each such entry belongs to the function support of \(D\phi^{-1}\) on \(\widehat V\). The support-pattern equality for the single matrix \(M\) gives
\[
 M_{j,\pi(j)}\ne0\quad\text{for every }j\in[d].
\]
Combining this with (4), simultaneously for all tasks, yields
\[
 \pi(S_i)\subseteq\widehat S_i\quad\text{for every }i. \tag{5}
\]
In particular, \(|\widehat S_i|\ge |S_i|\). The permutation is chosen once from the full inverse Jacobian, not separately for different tasks. No invertibility of \(M\) is needed. In dimension zero the unique empty permutation gives the same conclusion.

### 3. Exact support recovery

Summing the cardinality inequalities gives
\[
 |\operatorname{supp}(J_{\widehat U})|
 =\sum_i|\widehat S_i|
 \ge\sum_i|S_i|
 =|\operatorname{supp}(J_U)|.
\]
The sparsity assumption supplies the reverse inequality. Every difference \(|\widehat S_i|-|S_i|\) is nonnegative and their finite sum is zero, so each difference is zero. Together with (5), this proves
\[
 \widehat S_i=\pi(S_i)\quad\text{for every }i. \tag{6}
\]
This also shows that an empty true task support has empty estimated support.

### 4. Local task-block recovery

Fix a task \(i\), and put \(I=S_i\). If \(I\) is empty, the required relation is between empty coordinate tuples and is realized by the unique invertible map on \(\mathbb R^0\). If \(I=[d]\), the full reparameterization itself, with the prescribed coordinate ordering, provides the required local map. It remains to consider \(0<|I|<d\).

For \(c\in I\) and \(r\notin I\), equation (6) implies \(\pi(r)\notin\widehat S_i\). Equation (4) gives \(M_{c,\pi(r)}=0\). Because the support of \(M\) equals the function support of the inverse Jacobian, this entry of the inverse Jacobian vanishes identically on \(\widehat V\):
\[
 \frac{\partial(\phi^{-1})_c}{\partial\widehat z_{\pi(r)}}=0
 \quad(c\in I,\ r\notin I). \tag{7}
\]

Fix an arbitrary \(\widehat z_0\in\widehat V\), and choose an open rectangular box \(Q\subseteq\widehat V\) containing it. Order the estimated coordinates as \((\pi(I),\pi(I)^c)\), write the box as \(Q_X\times Q_Y\), and write \(\widehat z_0=(x_0,y_0)\) in this ordering. Define
\[
 F_i(x)=(\phi^{-1}(x,y_0))_I,\qquad x\in Q_X.
\]
This map is \(C^1\). For fixed \(x\), any two points of \(Q_Y\) can be joined by successive coordinate-line segments within \(Q_Y\). Along each segment, every component of \((\phi^{-1}(x,y))_I\) has derivative zero by (7), and is therefore constant. Consequently,
\[
 (\phi^{-1}(x,y))_I=F_i(x)
 \quad\text{for all }(x,y)\in Q_X\times Q_Y. \tag{8}
\]
This proves local factorization without requiring globally connected coordinate fibers.

Order the true coordinates as \((I,I^c)\). On this box, the inverse Jacobian has the block form
\[
 D\phi^{-1}(x,y)=
 \begin{pmatrix}
 A(x)&0\\
 B(x,y)&C(x,y)
 \end{pmatrix},\qquad A(x)=DF_i(x).
\]
The reordered full Jacobian is invertible. The determinant of this block-triangular matrix is \(\det A(x)\det C(x,y)\); hence \(A(x_0)\) is invertible. The map \(F_i\) is \(C^1\), has domain open in \(\mathbb R^{|I|}\), has codomain of the same dimension, and has invertible derivative at \(x_0\). The stated inverse function theorem applies. It gives neighborhoods \(X_0\subseteq Q_X\) of \(x_0\) and \(Z_0\) of \((\phi^{-1}(\widehat z_0))_I\) such that \(F_i:X_0\to Z_0\) is a \(C^1\) diffeomorphism.

Define \(h_i=F_i^{-1}\). For \(\widehat z=(x,y)\) sufficiently close to \(\widehat z_0\), equation (8) gives \(z_I=F_i(x)\), so
\[
 \widehat z_{\pi(I_i)}=h_i(z_{I_i}).
\]
The function \(h_i\) is locally invertible and has no complementary-coordinate argument. The base point was arbitrary. Since there are finitely many tasks, their local neighborhoods can be intersected when simultaneous local relations are desired; the permutation remains the single permutation already selected.

All four theorem-critical obligations are closed. The argument permits overlapping task supports, uses no latent-independence assumption, asserts no componentwise recovery within a task block, and requires no unjustified global subgroup inverse.
