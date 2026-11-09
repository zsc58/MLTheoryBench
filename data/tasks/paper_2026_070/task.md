# Problem

## Setup

Let n and m be positive integers. Let \(X\in\mathbb R^n\) be a random signal with \(\mathbb E\|X\|^2<\infty\). All reconstruction functions are measurable. Write \(I\) for the identity matrix of the appropriate size, \(\|\cdot\|\) for the Euclidean norm, and \(B^\dagger\) for the Moore-Penrose pseudoinverse of a matrix \(B\).

For a deterministic operator \(A\in\mathbb R^{m\times n}\), put \(Y=AX\) and define the measurement-consistency risk by expectation over the signal law:
\[
\mathcal L_{\rm cons}(f;A)=\frac1m\,\mathbb E_X\bigl[\|Af(AX)-AX\|^2\bigr],
\qquad f:\mathbb R^m\to\mathbb R^n.
\]

In the split experiment, let \(A\in\mathbb R^{m\times n}\) instead be random and independent of \(X\), and observe noiseless measurements \(Y=AX\). Select a subset of the rows of \(A\) using a sampling rule that depends only on \(A\) and auxiliary randomness independent of \((X,A)\). Let \(A_1\) consist of the selected rows, either in their original order with the other rows omitted, or with the other rows replaced by zeros. Fix the representation convention as part of the experiment. Apply the same selection to \(Y\), giving \(Y_1=A_1X\). The reconstruction input is only \(Z=(Y_1,A_1)\); the full \(A\), full \(Y\), and auxiliary randomness are not additional inputs. For variable row counts, the split-observation space is the disjoint union of the corresponding finite-dimensional vector/matrix spaces with their Borel sigma-algebras.

Define
\[
\mathcal L_{\rm split}(f)=\frac1m\,\mathbb E\bigl[\|Af(Z)-Y\|^2\bigr],
\qquad
Q(A_1)=\mathbb E[A^\top A\mid A_1].
\]
Assume \(\mathbb E[\|A\|_F^2\mid A_1]<\infty\) almost surely, where \(\|A\|_F^2=\sum_{i=1}^m\sum_{j=1}^n A_{ij}^2\), so the conditional Gram matrix is finite almost surely. Minimize \(\mathcal L_{\rm split}\) over all measurable functions from the split-observation space to \(\mathbb R^n\) having finite split risk, and assume this class is nonempty. Conditional expectations and minimizer identities are understood up to almost-sure equality.

## Task

Prove the following integrated theorem. First, for every deterministic \(A\) with \(\operatorname{rank}(A)<n\) and every measurable function \(v:\mathbb R^m\to\mathbb R^n\), the reconstruction
\[
f_v(y)=A^\dagger y+(I-A^\dagger A)v(y)
\]
has zero measurement-consistency risk; hence ordinary consistency cannot identify the nullspace component.

Second, for the split experiment and every admissible \(f\), show that
\[
\mathcal L_{\rm split}(f)=\frac1m\,\mathbb E\bigl[(f(Z)-X)^\top Q(A_1)(f(Z)-X)\bigr],
\]
and characterize all global minimizers as
\[
f^*(Z)=Q(A_1)^\dagger Q(A_1)\,\mathbb E[X\mid Z]
+\bigl(I-Q(A_1)^\dagger Q(A_1)\bigr)v(Z),
\]
where \(v\) is an arbitrary measurable function from the split-observation space to \(\mathbb R^n\) for which the displayed reconstruction has finite split risk.

Finally, prove that when \(Q(A_1)\) is invertible almost surely, the minimizer is unique up to almost-sure equality and equals \(\mathbb E[X\mid Y_1,A_1]\).
