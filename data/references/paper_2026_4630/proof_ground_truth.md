# Reference Proof

## Proof Structure

Expand the EMA-weighted row and column Gram matrices of the transformed sequence in terms of the fixed SPD factors. Orthogonality yields two matrix equations. Positive definiteness and uniqueness of the SPD inverse square root solve them, and substitution proves the converse.

The theorem-critical obligations are: finite second moments for all transformed quantities; positive definiteness of the two moment matrices; both Gram expansions with fixed factors outside expectation; solution of each SPD matrix equation; and the converse. The derivations below close all five obligations.

## Complete Proof

Define
\[
M(A,B)=\mathsf{EMA}_\beta\!\left[\mathbb E(G_tB^2G_t^\top)\right]_{t=1}^T,
\qquad
N(A,B)=\mathsf{EMA}_\beta\!\left[\mathbb E(G_t^\top A^2G_t)\right]_{t=1}^T.
\]
Every entry of a fixed linear transform of \(G_t\) is a finite linear combination of square-integrable entries. Products of such entries are integrable, as follows from \(2|xy|\le x^2+y^2\). Consequently all displayed expectations are finite, and \(Z_t\) is square-integrable.

By assumption these matrices are full rank. They are positive semidefinite EMA-weighted sums of expected Gram matrices, hence they are SPD. More explicitly, all weights \((1-\beta)\beta^{T-t}\) are nonnegative, and for \(u\in\mathbb R^m\) and \(v\in\mathbb R^n\),
\[
u^\top M(A,B)u=(1-\beta)\sum_{t=1}^T\beta^{T-t}\mathbb E\|BG_t^\top u\|_2^2\ge0,
\]
\[
v^\top N(A,B)v=(1-\beta)\sum_{t=1}^T\beta^{T-t}\mathbb E\|AG_tv\|_2^2\ge0.
\]
Symmetry and full rank therefore give positive definiteness.

Since \(Z_t=AG_tB\) and \(A,B\) are symmetric,
\[
\mathsf{EMA}_\beta\!\left[\mathbb E(Z_tZ_t^\top)\right]_{t=1}^T=A\,M(A,B)\,A,
\]
and
\[
\mathsf{EMA}_\beta\!\left[\mathbb E(Z_t^\top Z_t)\right]_{t=1}^T=B\,N(A,B)\,B.
\]
The factors can be taken outside expectations and finite sums because they are fixed, nonrandom matrices and do not vary with \(t\). No independence between the \(G_t\) is used.

Thus \(\{Z_t\}\) is time-averaged orthogonal in expectation exactly when \(A M(A,B)A=I_m\) and \(B N(A,B)B=I_n\).

For any SPD matrix \(M\), the unique SPD matrix \(X\) satisfying \(XMX=I\) is \(M^{-1/2}\). Here is the elementary justification. Multiplying on both sides by \(X^{-1}\) gives
\[
M=X^{-2}.
\]
The standard finite-dimensional real spectral theorem states that a real symmetric matrix has an orthogonal diagonalization; positive definiteness makes all its eigenvalues positive. Its hypotheses apply to \(X\), so write \(X=Q\operatorname{diag}(x_i)Q^\top\) with \(Q\) orthogonal and \(x_i>0\). Then
\[
M=Q\operatorname{diag}(x_i^{-2})Q^\top,
\qquad
M^{-1/2}=Q\operatorname{diag}(x_i)Q^\top=X.
\]
Conversely, the spectral definition of the SPD inverse square root gives \(M^{-1/2}MM^{-1/2}=I\). This argument does not assume commutativity of arbitrary SPD matrices or appeal to a specialized whitening theorem.

Therefore the two identities are equivalent to
\[
A=M(A,B)^{-1/2},\qquad B=N(A,B)^{-1/2}.
\]
These equations are coupled because the first right-hand side depends on \(B\), while the second depends on \(A\).

Conversely, if the displayed coupled equations hold, then the defining property of the SPD inverse square root gives \(A M(A,B)A=I_m\) and \(B N(A,B)B=I_n\), which are precisely the two time-averaged orthogonality identities for \(Z_t\).

## Boundary and Scope Checks

At \(\beta=0\), only the term \(t=T\) has nonzero weight. The same finite-sum expansions and SPD argument apply without modification. There is no division by \(\beta\), and no bias-correction factor is introduced.

The argument proves a characterization of any fixed pair \((A,B)\) satisfying the stated domain conditions; it does not assert existence or joint uniqueness of a pair. In particular,
\[
\operatorname{tr}\!\left(\mathsf{EMA}_\beta[\mathbb E(Z_tZ_t^\top)]_{t=1}^T\right)
=
\operatorname{tr}\!\left(\mathsf{EMA}_\beta[\mathbb E(Z_t^\top Z_t)]_{t=1}^T\right).
\]
Thus either simultaneous condition forces \(m=n\). For \(m\ne n\), neither condition holds, which is consistent with the equivalence and does not require restricting the public dimensions. Full rank is required of the two averaged moment matrices, not of each realization of each \(G_t\).
