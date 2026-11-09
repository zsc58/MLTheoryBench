# Reference Proof

## Proof Structure

We compare an arbitrary optimal feasible factorization with the given one through an invertible change of basis. Simplex normalization fixes the column sums of this change of basis. The sufficiently scattered condition bounds each row norm by its row sum. Hadamard's inequality and the arithmetic-geometric-mean inequality then bound the determinant using the total of the row sums. Equality of the optimal determinants forces all row sums and row norms to equal one and the rows to be orthogonal. The second scatteredness condition then forces the change of basis to be a permutation.

## Complete Proof

### Step 001: Full ranks and change of basis

Because rank(X)=r and X=WH with inner dimension r, W has full column rank and H has full row rank. The same holds for any other feasible pair (\(\widetilde W,\widetilde H\)). Moreover,
\[
\operatorname{col}(W)=\operatorname{col}(X)=\operatorname{col}(\widetilde W).
\]
Thus there is an invertible matrix \(Q\in\mathbb R^{r\times r}\) such that \(\widetilde W=WQ^{-1}\). Substitution into \(WH=\widetilde W\widetilde H\), followed by cancellation using the full column rank of W, gives
\[
\widetilde W=WQ^{-1},\qquad \widetilde H=QH.
\]

### Step 002: Column normalization

Write \(e=\mathbf1_r\). The simplex constraints give
\[
e^TH=\mathbf1_n^T=e^TQH.
\]
Since H has full row rank, it has a right inverse, for example \(B=H^T(HH^T)^{-1}\). Multiplying \((e^TQ-e^T)H=0\) by B gives
\[
e^TQ=e^T.
\]
This fixes the column sums of Q, not its individual row sums. In particular, \(e^TQe=r\).

### Step 003: Dual-cone geometry

For a cone K, define its dual by
\[
K^*=\{y:y^Tx\ge0\text{ for every }x\in K\}.
\]
Let \(q_i^T\) be row i of Q. Since \(QH=\widetilde H\ge0\), each \(q_i\) is nonnegative on every column of H and hence on their conic hull. Therefore \(q_i\in\operatorname{cone}(H)^*\). The inclusion \(C\subseteq\operatorname{cone}(H)\) implies \(q_i\in C^*\).

We verify that
\[
C^*=\{y:e^Ty\ge\|y\|_2\}.
\]
For r=1, C is the nonnegative half-line, whose dual is itself, and the displayed characterization is exactly \(y\ge|y|\).

For r>=2, set \(u=e/\sqrt r\). Write \(x=tu+z\), where \(z\perp u\). The inequality \(e^Tx\ge\sqrt{r-1}\|x\|_2\) is equivalent to
\[
t\ge0,\qquad \|z\|_2\le\frac{t}{\sqrt{r-1}}.
\]
These inequalities also imply x>=0. Indeed, if \(e_i\) is the ith coordinate vector, then
\[
|z_i|=|(e_i-u/\sqrt r)^Tz|
\le\sqrt{\frac{r-1}{r}}\|z\|_2
\le\frac{t}{\sqrt r},
\]
so every coordinate of \(tu+z\) is nonnegative. Consequently the displayed conditions on t and z describe C exactly.

Write \(y=au+b\), where \(b\perp u\). For fixed t>=0, the minimum of \(y^Tx=at+b^Tz\) over \(\|z\|_2\le t/\sqrt{r-1}\) is
\[
t\left(a-\frac{\|b\|_2}{\sqrt{r-1}}\right).
\]
The minimum follows from Cauchy--Schwarz and is attained by taking z opposite to b when b is nonzero; if b=0 it is immediate. Thus \(y\in C^*\) if and only if \(a\ge\|b\|_2/\sqrt{r-1}\). Since \(e^Ty=\sqrt r\,a\) and \(\|y\|_2^2=a^2+\|b\|_2^2\), this is equivalent to \(e^Ty\ge\|y\|_2\), proving the characterization.

Define the row sums \(s_i=q_i^Te\). We have
\[
0<\|q_i\|_2\le s_i,\qquad \sum_{i=1}^r s_i=e^TQe=r.
\]
Strict positivity follows because Q is invertible and hence has no zero row.

### Step 004: Determinant bound

Hadamard's inequality and the arithmetic-geometric-mean inequality give
\[
|\det Q|
\le\prod_{i=1}^r\|q_i\|_2
\le\prod_{i=1}^r s_i
\le\left(\frac{\sum_i s_i}{r}\right)^r
=1.
\]
Here both bounds and their equality cases can be checked directly. Orthogonalizing the independent rows of Q by subtracting projections onto earlier rows preserves the determinant. If the resulting orthogonal rows are \(v_i^T\), then
\[
|\det Q|=\prod_i\|v_i\|_2\le\prod_i\|q_i\|_2.
\]
Each norm can only decrease under these subtractions. Equality holds exactly when every subtracted projection is zero, that is, when the original rows are mutually orthogonal. For the positive numbers s_i with sum r, the elementary inequality \(\log t\le t-1\), with equality only at t=1, yields
\[
\log\prod_i s_i=\sum_i\log s_i\le\sum_i(s_i-1)=0.
\]
The logarithmic inequality follows by differentiating \(t-1-\log t\), which has its unique minimum zero at t=1. Hence the product bound has equality exactly when all s_i=1. These arguments include r=1.

### Step 005: Optimal determinant equality

Now let the competing pair attain the same maximum as (W,H). The change of basis gives
\[
\det(\widetilde H\widetilde H^T)
=\det(QHH^TQ^T)
=\det(Q)^2\det(HH^T).
\]
Since H has full row rank, HH^T is positive definite and its determinant is positive. Equality of the two objective values therefore implies \(|\det Q|=1\).

### Step 006: Equality forces orthogonality

Every inequality in Step 004 must now be an equality. The product bound forces s_i=1 for every i. Since \(0<\|q_i\|_2\le s_i\) and the products of these positive quantities agree, every row norm is also one. Equality in Hadamard's inequality forces the rows to be mutually orthogonal. Thus \(QQ^T=I_r\), so Q is orthogonal.

### Step 007: Scatteredness forces a permutation

The inequality QH>=0 implies that Q maps every vector in \(\operatorname{cone}(H)\) into \(\mathbb R_+^r\). Since Q is orthogonal,
\[
\operatorname{cone}(H)\subseteq Q^T\mathbb R_+^r
=\operatorname{cone}(Q^T).
\]
The second scatteredness condition applied to the orthogonal matrix \(Q^T\) makes \(Q^T\), and therefore Q, a permutation matrix. Taking P=Q gives
\[
\widetilde W=WP^{-1},\qquad \widetilde H=PH.
\]
This proves the requested uniqueness for every competing maximizer, including the case r=1.
