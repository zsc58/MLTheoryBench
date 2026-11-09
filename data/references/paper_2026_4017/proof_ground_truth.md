# Reference Proof

## Proof Structure

1. Prove by Schur-complement induction that the recursive construction is a smooth bijection with smooth inverse from unconstrained coordinates to the SPD cone and factorizes the determinant into the positive pivots.
2. Use triangular dependence of the Schur stages to compute the forward Jacobian, verify the log-pivot coordinate determinant, and derive the inverse Jacobian on symmetric matrices.
3. Differentiate the block recursion with all predecessor coordinates allowed to vary and prove the exact additive Fisher-Rao metric recursion.
4. Compute the determinants of the stage metric blocks, transfer to the independent volume-shape coordinates, and normalize the off-diagonal coordinates to obtain constant volume density.

## Complete Proof

### 1. Global diffeomorphism and determinant

Write $a_j=e^{s_j}>0$. At one recursive stage put $A=\Theta_{j-1}$, $a=a_j$, $r=r_j$, and $\beta=r/a$. Then
\[
\Theta_j=\begin{pmatrix}A+a\beta\beta^\top&a\beta\\a\beta^\top&a\end{pmatrix}
=B\begin{pmatrix}A&0\\0&a\end{pmatrix}B^\top,
\qquad B=\begin{pmatrix}I&\beta\\0&1\end{pmatrix}.
\]
The matrix $B$ is invertible and has determinant one. This factorization proves that $\Theta_j$ is positive definite exactly when $A$ is positive definite and $a>0$, and that
\[
\det\Theta_j=a_j\det\Theta_{j-1}.
\]
Conversely, given any positive-definite block matrix $\begin{pmatrix}C&r\\r^\top&a\end{pmatrix}$, its lower-right entry is positive. The same factorization, with $A=C-rr^\top/a$, implies $A\succ0$. Thus its last pivot, last off-diagonal column, and predecessor are uniquely recovered. Recursing down to the scalar stage proves bijectivity between the SPD cone and the coordinates $(a_1,\ldots,a_p,r_2,\ldots,r_p)$ with positive pivots and unrestricted off-diagonal columns.

All forward expressions are smooth. The inverse uses only matrix entries, division by strictly positive pivots, and logarithms of strictly positive pivots, so it is smooth on the SPD cone. Exponentiation of each pivot and the invertible linear transformation
\[
v=\sum_{j=1}^p s_j,\qquad d_j=s_j-v/p\quad(2\leq j\leq p),
\]
with inverse $s_1=v/p-\sum_{j=2}^p d_j$ and $s_j=v/p+d_j$ for $j\geq2$, complete the global diffeomorphism. Its domain dimension is $p+p(p-1)/2=p(p+1)/2$.

Starting with $\det\Theta_1=a_1$, the determinant recursion gives
\[
\det\Theta_p=\prod_{j=1}^p a_j=\exp\left(\sum_{j=1}^p s_j\right)=e^v.
\]
The factorization also gives, by inverting its factors,
\[
\Theta_j^{-1}=\begin{pmatrix}
A^{-1}&-A^{-1}\beta\\
-\beta^\top A^{-1}&a^{-1}+\beta^\top A^{-1}\beta
\end{pmatrix}.
\]
These calculations explicitly verify the Schur identities used here, with positive pivots and positive-definite predecessors at every stage.

### 2. Forward and inverse Jacobians

All Jacobians in this proof are absolute determinants with respect to the stated independent-entry Lebesgue measures. At a recursive stage, the map from $(A,r,a)$ to the independent entries of $\Theta_j$ is
\[
(A,r,a)\longmapsto(A+a^{-1}rr^\top,r,a).
\]
Its derivative is triangular with identity diagonal blocks, so its Jacobian is one. Iteration gives unit Jacobian for the map from all pivot and off-diagonal coordinates $(a,r)$ to $\Theta$.

Passing from $(s,r)$ to $(a,r)$ contributes $\prod_j e^{s_j}$. To check the independent-coordinate normalization, the derivative of $(v,d_2,\ldots,d_p)\mapsto(s_1,\ldots,s_p)$ has first row $(1/p,-1,\ldots,-1)$ and remaining rows consisting of first entry $1/p$ and an identity block. Adding the remaining rows to the first row turns it into $(1,0,\ldots,0)$, proving that this determinant is one. For $p=1$ the transformation is simply $s_1=v$. Consequently
\[
J_{(v,d,r)\to\Theta}=\prod_{j=1}^p e^{s_j}=e^v=\det\Theta.
\]

For inversion, differentiating $\Theta\Sigma=I$ gives
\[
d\Sigma=-\Theta^{-1}(d\Theta)\Theta^{-1}.
\]
Let $\lambda_1,\ldots,\lambda_p>0$ be the eigenvalues of $\Theta$. Conjugating into an orthonormal eigenbasis is a change of basis on the vector space of symmetric matrices and does not change the determinant of this linear operator. In that basis, the diagonal symmetric directions are multiplied in absolute value by $\lambda_i^{-2}$ and the off-diagonal symmetric directions by $(\lambda_i\lambda_j)^{-1}$ for $i<j$. Its absolute determinant is therefore
\[
\prod_{i=1}^p\lambda_i^{-2}\prod_{i<j}(\lambda_i\lambda_j)^{-1}
=\prod_{i=1}^p\lambda_i^{-(p+1)}
=(\det\Theta)^{-(p+1)}.
\]
The chain rule yields
\[
J_{(v,d,r)\to\Sigma}=e^v e^{-(p+1)v}=e^{-pv}.
\]

### 3. Full metric recursion

For $j\geq2$, again write $A=\Theta_{j-1}$, $S=A^{-1}$, $a=e^{s_j}$, $\beta=r_j/a$, and $B=\begin{pmatrix}I&\beta\\0&1\end{pmatrix}$. Allow all coordinates, including those of $A$, to vary. Differentiating the block representation gives
\[
d\Theta_j=\begin{pmatrix}
dA+\beta\beta^\top da+a(d\beta\,\beta^\top+\beta\,d\beta^\top)&\beta\,da+a\,d\beta\\
\beta^\top da+a\,d\beta^\top&da
\end{pmatrix}.
\]
Multiplying this differential on the left by $B^{-1}$ and on the right by $B^{-\top}$ gives
\[
H:=B^{-1}(d\Theta_j)B^{-\top}
=\begin{pmatrix}dA&a\,d\beta\\a\,d\beta^\top&da\end{pmatrix}.
\]
Since $\Theta_j=B\operatorname{diag}(A,a)B^\top$, the matrix $\Theta_j^{-1}d\Theta_j$ is similar to
\[
\operatorname{diag}(S,a^{-1})H
=\begin{pmatrix}S\,dA&aS\,d\beta\\d\beta^\top&da/a\end{pmatrix}.
\]
Squaring this block matrix and taking its trace proves
\[
\operatorname{Tr}\big((\Theta_j^{-1}d\Theta_j)^2\big)
=\operatorname{Tr}\big((S\,dA)^2\big)
+2a\,(d\beta)^\top S\,d\beta+(da/a)^2.
\]
Thus the full metric, not merely its restriction to a frozen-predecessor slice, satisfies
\[
\frac12\operatorname{Tr}\big((\Theta_j^{-1}d\Theta_j)^2\big)
=\frac12\operatorname{Tr}\big((\Theta_{j-1}^{-1}d\Theta_{j-1})^2\big)
+\frac12(ds_j)^2
+e^{-s_j}(dr_j-r_jds_j)^\top\Sigma_{j-1}(dr_j-r_jds_j),
\]
where we used $da/a=ds_j$ and $d\beta=a^{-1}(dr_j-r_jds_j)$. The calculation explicitly shows that there are no mixed differential terms between the predecessor variation and the new slice.

The scalar base case is $\frac12\operatorname{Tr}((\Theta_1^{-1}d\Theta_1)^2)=\frac12(ds_1)^2$. Telescoping the full recursion now gives
\[
ds_{\rm FR}^2=\frac12\sum_{j=1}^p(ds_j)^2+
\sum_{j=2}^p e^{-s_j}(dr_j-r_jds_j)^\top\Sigma_{j-1}(dr_j-r_jds_j).
\]
The coefficients of a later stage can depend on earlier coordinates; the assertion proved here is the absence of mixed differential terms between stages in $(s,r)$ coordinates.

### 4. Volume density and normalization

In the coordinates grouped as $s_1,(s_2,r_2),\ldots,(s_p,r_p)$, the metric is block diagonal. At each point, the change of differential basis
\[
(ds_j,dr_j)\longmapsto(ds_j,dr_j-r_jds_j)
\]
has determinant one. In this basis the stage-$j$ metric has diagonal blocks $1/2$ and $e^{-s_j}\Sigma_{j-1}$. Hence for $j\geq2$,
\[
\det G_j=\frac12e^{-(j-1)s_j}\det\Sigma_{j-1}.
\]
The initial block has determinant $1/2$. From determinant factorization,
\[
\det\Sigma_{j-1}=\exp\left(-\sum_{k<j}s_k\right).
\]
Multiplying the stage determinants therefore yields
\[
\det G=2^{-p}\exp\left[-\sum_{j=2}^p\left((j-1)s_j+\sum_{k<j}s_k\right)\right]
=2^{-p}e^{-(p-1)v}.
\]
Indeed, each $s_k$ has total coefficient $(k-1)+(p-k)=p-1$ in the exponent. Taking the square root and using the unit absolute determinant of $(v,d)\mapsto s$ gives
\[
d\operatorname{vol}_{\rm FR}=2^{-p/2}e^{-(p-1)v/2}\,dv\,dd\,dr.
\]

Finally, write $N=p(p-1)/2$ for the number of off-diagonal coordinates and set $r_j=e^{v/p}\rho_j$. The full change $(v,d,\rho)\mapsto(v,d,r)$ has block triangular derivative: its $(v,d)$ block is the identity and its $\rho$ block is $e^{v/p}I_N$. The derivatives of $r$ with respect to $v$ do not affect its determinant. Thus
\[
dv\,dd\,dr=e^{Nv/p}\,dv\,dd\,d\rho
=e^{(p-1)v/2}\,dv\,dd\,d\rho.
\]
Substitution gives
\[
d\operatorname{vol}_{\rm FR}=2^{-p/2}\,dv\,dd\,d\rho.
\]
When $p=1$, all shape blocks are empty, $\Theta=[e^v]$, the two Jacobians are $e^v$ and $e^{-v}$, the metric is $\frac12dv^2$, and both volume formulas reduce to $2^{-1/2}dv$. Thus the entire stated parameter range is covered, and all assertions follow.
