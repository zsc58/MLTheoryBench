# Reference Proof

## Proof Structure

1. Specify the split-half score on its domain, including the zero-half convention, and distinguish the finite estimator from its partition expectation.
2. Construct explicit matrices X and Q, verify orthogonality, and compute Y=XQ.
3. Verify that centered linear CKA is defined and equals one.
4. Compute every equipartition score for X and Y, including all nondegeneracy and tied-rank checks.
5. Average the scores and conclude non-invariance of the finite estimator from its differing expectations.

## Complete Proof

For a feature half A, write x_i^A for row i restricted to A. Its RDM vector lists D^A_{ij}=1-(x_i^A\cdot x_j^A)/(\|x_i^A\|\|x_j^A\|), i<j, in a common row-pair order. If either restricted half is identically zero, assign the split score zero without evaluating its RDM. Otherwise both halves must have nonzero restricted rows and nonconstant RDM rank vectors, and the split score is Pearson correlation of their midranks. These conditions must hold for every equipartition for the estimator to be defined.

For a fixed four-coordinate matrix, let c_1,c_2,c_3 be its three unordered equipartition scores. Independent uniform sampling gives
\[
\mathbb E[S_{30}(X)]=\frac1{30}\sum_{k=1}^{30}\mathbb E[c_{\pi_k}(X)]=\frac{c_1+c_2+c_3}{3}=\bar S(X).
\]
All scores are bounded, so these expectations exist.

Take
\[
X=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\-1&-1&-1&-1\end{pmatrix},\qquad
Q=\frac1{\sqrt2}\begin{pmatrix}1&0&1&0\\-1&0&1&0\\0&1&0&1\\0&-1&0&1\end{pmatrix}.
\]
The columns of Q have norm one. Columns with disjoint supports are orthogonal; the two pairs with common supports have inner product (1-1)/2=0. Thus Q^TQ=I_4, and, since Q is square, QQ^T=I_4 as well.

Let a=(1,1,-1)^T and b=(1,-1,-1)^T. Then X=[a\ a\ b\ b], and direct multiplication gives
\[
Y=XQ=[0\ 0\ \sqrt2a\ \sqrt2b].
\]
Consequently
\[
YY^T=XQQ^TX^T=XX^T.
\]
For H=I_3-\tfrac13\mathbf1\mathbf1^T, put K_U=HUU^TH. The first row of HX is (2/3,2/3,4/3,4/3), so
\[
(K_X)_{11}=\|(HX)_{1,:}\|^2=40/9>0.
\]
Hence K_X is nonzero. Since K_Y=K_X, both CKA normalization factors are positive and
\[
\operatorname{CKA}(X,Y)=\frac{\langle K_X,K_X\rangle_F}{\|K_X\|_F^2}=1.
\]

Use row-pair order (12,13,23). A half with columns [a\ a] has RDM vector u=(0,2,2), whereas a half with columns [b\ b] has RDM vector v=(2,2,0). Both halves have nonzero rows. Their midrank vectors are
\[
r=(1,5/2,5/2),\qquad s=(5/2,5/2,1).
\]
Both rank means are 2. Thus
\[
r-2\mathbf1=(-1,1/2,1/2),\qquad s-2\mathbf1=(1/2,1/2,-1),
\]
whose inner product is -3/4 and whose squared norms are both 3/2. Their Pearson correlation is therefore -1/2.

A half with one a column and one b column has row vectors (1,1), (1,-1), and (-1,-1), up to a coordinate permutation. These rows have norm sqrt(2), and the RDM vector is w=(1,2,1). Its rank vector (3/2,3,3/2) is nonconstant, so the correlation of two such RDMs is defined and equals 1.

It follows that for X the partition {1,2}|{3,4} has score -1/2, while {1,3}|{2,4} and {1,4}|{2,3} each have score 1. Every score is defined, and
\[
\bar S(X)=\frac{-1/2+1+1}{3}=\frac12.
\]

For Y, the partition {1,2}|{3,4} has an identically zero first half, so its score is 0 by the stated convention. Each remaining partition has one half consisting of a zero column and a sqrt(2)a column and the other consisting of a zero column and a sqrt(2)b column, up to coordinate order. Every restricted row in these halves is nonzero. Their RDM vectors are u and v, so both scores are -1/2. Thus Y also belongs to the estimator domain, and
\[
\bar S(Y)=\frac{0-1/2-1/2}{3}=-\frac13.
\]

Finally, E[S_30(X)]=1/2 and E[S_30(Y)]=-1/3. Equality in distribution would imply equality of these finite expectations, so the estimator distributions differ. In particular, the estimator cannot be invariant almost surely under the rotation when the same random partition sequence is used for both matrices. This proves non-invariance in general; it does not claim the displayed expectation values hold for every realized sequence of 30 partitions.
