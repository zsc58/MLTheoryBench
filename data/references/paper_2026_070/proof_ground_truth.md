# Reference Proof

## Proof Structure and Obligations

1. **step_001:** Establish measurement consistency using the Moore-Penrose identities on the range of a fixed operator.
2. **step_002:** Show that a nontrivial nullspace permits different reconstructions with the same zero consistency risk.
3. **step_003:** Establish the conditional independence needed to average the random operator while holding the reconstruction error fixed.
4. **step_004:** Derive the normalized conditional-Gram risk identity.
5. **step_005:** Prove conditional square completion, finite-risk attainment, the complete measurable nullspace family, and almost-sure uniqueness in the invertible case.

These obligations are derived below. The appendix conditional-mean and weighted-minimizer arguments are reconstructed rather than used as unproved dependencies.

## Complete Proof

### Fixed-operator consistency

Fix a deterministic matrix A with rank(A)<n. Write a singular value decomposition A=U Sigma V^T. Its pseudoinverse inverts the nonzero singular values and leaves zero singular values zero. Consequently AA^dagger is the orthogonal projector onto range(A), A^dagger A is the orthogonal projector onto range(A^T), and I-A^dagger A is the orthogonal projector onto ker(A).

Since Y=AX belongs to range(A),
\[
AA^\dagger Y=Y,
\qquad A(I-A^\dagger A)=0.
\]
Thus for every measurable v:R^m->R^n,
\[
A f_v(Y)=AA^\dagger Y+A(I-A^\dagger A)v(Y)=Y.
\]
The consistency risk is zero. Since squared losses are nonnegative, this is a global minimum. Choose a nonzero h in ker(A). Taking v=0 and v=h gives reconstructions differing by h at every input and having exactly the same measurements and zero risk. This proves the nullspace ambiguity. No integrability condition on v itself is needed for this zero residual.

### Conditioning the split experiment

The operator A and the independent splitting randomization jointly are independent of X. Therefore their measurable image (A,A1) is independent of X. In particular, for bounded measurable functions a of A and b of X,
\[
\mathbb E[a(A)b(X)\mid A_1]
=\mathbb E[a(A)\mid A_1]\,\mathbb E[b(X)].
\]
For example, this follows by testing both sides against bounded functions of A1 and using independence of X from (A,A1). It proves conditional independence of A and X given A1. The corresponding conditional law of A given (X,A1) is its law given A1. Since Z=(A1 X,A1) is a function of (X,A1), adding Z to this conditioning changes nothing.

The assumption E[||A||_F^2|A1]<infinity almost surely implies that every entry of Q(A1)=E[A^T A|A1] is finite almost surely: diagonal entries are bounded by this conditional expectation, and absolute off-diagonal entries are bounded by half the sum of the corresponding diagonal entries. Q is measurable, symmetric, and positive semidefinite. Indeed, for every rational vector u,
\[
u^\top Q u=\mathbb E[\|Au\|^2\mid A_1]\geq0,
\]
and continuity extends this inequality to every real vector on a common event of probability one.

For any measurable reconstruction f, set e=f(Z)-X. Conditional on (X,A1), e is fixed. Integrating the nonnegative squared norm against the conditional law of A gives
\[
\mathbb E[\|Ae\|^2\mid X,A_1]=e^\top Q(A_1)e.
\]
The use of nonnegative conditional integration is valid even if an unconditional operator second moment is infinite. Taking expectations and retaining the normalization gives
\[
\begin{aligned}
\mathcal L_{\rm split}(f)
&=\frac1m\mathbb E[\|Af(Z)-AX\|^2]\\
&=\frac1m\mathbb E[(f(Z)-X)^\top Q(A_1)(f(Z)-X)].
\end{aligned}
\]
In particular, the identity holds for every admissible finite-risk f. The estimator is never allowed to depend separately on A, Y, or the discarded measurements.

### Conditional minimization and attainment

Put mu(Z)=E[X|Z]. A measurable version exists as a function of the finite-dimensional split observation, whose variable-dimensional representation is a finite disjoint union of Euclidean spaces. Finite second moment of X gives
\[
\mathbb E\|\mu(Z)\|^2\leq\mathbb E\|X\|^2<\infty,
\qquad \mathbb E[\|X\|^2\mid Z]<\infty\quad\text{almost surely}.
\]
In the following displays Q means Q(A1), which is known conditional on Z. Conditional square completion gives, almost surely,
\[
\mathbb E[(f-X)^\top Q(f-X)\mid Z]
=(f-\mu)^\top Q(f-\mu)
+\mathbb E[(X-\mu)^\top Q(X-\mu)\mid Z].
\]
The cross term vanishes because the conditional mean of X-mu is zero. This calculation is legitimate under the conditional law for almost every Z: Q and f(Z) are finite there and the conditional second moment of X is finite. Equivalently, one can first localize to Z-measurable events on which ||Q||, ||f(Z)||, and E[||X||^2|Z] are bounded, then exhaust the probability space. Thus no unsupported global integrability of the separate cross term is being assumed.

Define the nonnegative conditional residual
\[
r(Z)=\mathbb E[(X-\mu)^\top Q(X-\mu)\mid Z].
\]
Integration of the nonnegative decomposition yields
\[
m\mathcal L_{\rm split}(f)
=\mathbb E[(f-\mu)^\top Q(f-\mu)]+\mathbb E[r(Z)].
\]
By the assumed nonemptiness of the admissible class, choose one f0 with finite split risk. The last identity implies E[r(Z)]<=m L_split(f0)<infinity. Applying the risk identity to mu gives
\[
m\mathcal L_{\rm split}(\mu)=\mathbb E[r(Z)]<\infty.
\]
Thus mu is admissible and attains the global minimum. This also rules out an optimization problem in which every risk is infinite.

For any admissible f,
\[
\mathcal L_{\rm split}(f)-\mathcal L_{\rm split}(\mu)
=\frac1m\mathbb E[(f-\mu)^\top Q(f-\mu)].
\]
The integrand is nonnegative, so equality of risks holds exactly when this integrand is zero almost surely. A spectral decomposition of the symmetric positive-semidefinite matrix Q shows that u^T Q u=0 exactly when Qu=0. Hence f is a global minimizer if and only if
\[
Q(A_1)(f(Z)-\mu(Z))=0\quad\text{almost surely}.
\]

### Complete family and uniqueness

Let P=Q^dagger Q. Spectral decomposition shows that P is the orthogonal projector onto range(Q), and I-P is the orthogonal projector onto ker(Q). All the random matrices here are measurable. For completeness, on positive-semidefinite matrices,
\[
Q^\dagger=\lim_{k\to\infty}(Q^2+k^{-1}I)^{-1}Q,
\]
entrywise, as follows by applying the formula to each eigenvalue. Every finite-k expression is continuous, so the limit is measurable even when the rank varies.

If f is a minimizer, then P(f-mu)=0 almost surely. Taking v=f gives
\[
f(Z)=P\mu(Z)+(I-P)v(Z)\quad\text{almost surely}.
\]
Conversely, every measurable function of this form satisfies Q(f-mu)=0 and has the same finite risk as mu. In particular, the nullspace term itself need not be square integrable. This establishes the entire family
\[
f^*(Z)=Q(A_1)^\dagger Q(A_1)\mathbb E[X\mid Z]
+\bigl(I-Q(A_1)^\dagger Q(A_1)\bigr)v(Z).
\]
The characterization is up to almost-sure equality; values outside the support of Z are unconstrained. If Q=0 on an event, the formula allows every output on that event, as it should.

Finally, if Q(A1) is invertible almost surely, P=I almost surely and the displayed family reduces to f*(Z)=mu(Z)=E[X|Y1,A1]. Equivalently, Q(f-mu)=0 forces f=mu almost surely. No uniform lower bound on the eigenvalues is needed. This proves the stated uniqueness.

## Source Repairs and Closure

The proof retains 1/m throughout, corrects the domains of the arbitrary nullspace functions, and retains the residual risk in square completion. These are the local source repairs recorded for theory_011, theory_012, theory_021, and theory_022. All five proof obligations are closed; there is no unresolved private proof dependency.
