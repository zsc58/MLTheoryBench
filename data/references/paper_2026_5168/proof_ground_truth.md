# Reference Proof

## Proof Structure

1. Verify well-definedness, identify the independent-sample difference law, and justify coordinate factorization, including degenerate covariance.
2. Evaluate the one-dimensional Gaussian quadratic exponential for both positive and zero variance, then reassemble the determinant and regularized quadratic form.
3. Normalize the affinities and distinguish dependence of the normalized affinities from dependence of the unnormalized affinity matrix.

## Complete Proof

Fix classes \(a,b\), and write \(\delta=m_a-m_b\). When \(a=b\), the affinity uses two independent draws from \(\nu_a\), not one draw compared with itself.

Since \(C\) is symmetric positive semidefinite and \(\varepsilon>0\), the matrix \(\varepsilon I+C\) is positive definite, so every \(q_{ab}\) is finite and well-defined. The kernel is a strictly positive measurable function bounded by one. Consequently, \(0<A_{ab}\leq1\), and every finite row sum defining \(T\) is positive.

Independence gives
\[
D:=X_a-X_b\sim\mathcal N(\delta,2C).
\]
Indeed, using the Gaussian characteristic function and independence, for every \(u\in\mathbb R^d\),
\[
\mathbb E[e^{\mathrm i u^\top D}]
=\exp\!\left(\mathrm i u^\top m_a-\tfrac12u^\top Cu\right)
 \exp\!\left(-\mathrm i u^\top m_b-\tfrac12u^\top Cu\right)
=\exp\!\left(\mathrm i u^\top\delta-u^\top Cu\right),
\]
which is the characteristic function of \(\mathcal N(\delta,2C)\), also when \(C\) is singular.

Choose an orthogonal matrix \(U\) such that
\[
C=U\operatorname{diag}(\lambda_1,\ldots,\lambda_d)U^\top,
\qquad \lambda_i\geq0,
\]
and put \(\widetilde\delta=U^\top\delta\). The characteristic function of \(U^\top D\) factors as
\[
\prod_{i=1}^d\exp\!\left(\mathrm i u_i\widetilde\delta_i-\lambda_i u_i^2\right).
\]
Thus its coordinates are independent, with coordinate \(i\) distributed as \(\mathcal N(\widetilde\delta_i,2\lambda_i)\). Coordinates with \(\lambda_i=0\) are deterministic. Since the Euclidean norm is invariant under the rotation,
\[
A_{ab}=\prod_{i=1}^d
\mathbb E\left[\exp\left(-\frac{G_i^2}{4\varepsilon}\right)\right],
\qquad G_i\sim\mathcal N(\widetilde\delta_i,2\lambda_i).
\]

We evaluate the scalar expectation. Let \(G\sim\mathcal N(m,s^2)\), where \(s^2\geq0\), and let \(t\geq0\). If \(s^2=0\), then \(G=m\) almost surely, and the expectation is \(e^{-tm^2}\). If \(s^2>0\), put \(h=1+2ts^2>0\). Completing the square gives
\[
-tx^2-\frac{(x-m)^2}{2s^2}
=-\frac{h}{2s^2}\left(x-\frac{m}{h}\right)^2
-\frac{tm^2}{h}.
\]
Therefore
\[
\begin{aligned}
\mathbb E[e^{-tG^2}]
&=\frac{e^{-tm^2/h}}{\sqrt{2\pi s^2}}
\int_{\mathbb R}\exp\!\left[-\frac{h}{2s^2}\left(x-\frac{m}{h}\right)^2\right]dx\\
&=h^{-1/2}e^{-tm^2/h}.
\end{aligned}
\]
Together with the zero-variance case, this proves
\[
\mathbb E[e^{-tG^2}]
=(1+2ts^2)^{-1/2}
\exp\left(-\frac{tm^2}{1+2ts^2}\right)
\]
for every \(s^2\geq0\) and \(t\geq0\).

Applying this identity with \(t=1/(4\varepsilon)\), \(s^2=2\lambda_i\), and \(m=\widetilde\delta_i\) gives
\[
\mathbb E\left[e^{-G_i^2/(4\varepsilon)}\right]
=\left(1+\frac{\lambda_i}{\varepsilon}\right)^{-1/2}
\exp\left(-\frac{\widetilde\delta_i^2}{4(\varepsilon+\lambda_i)}\right).
\]
All hypotheses hold because \(\varepsilon>0\) and \(\lambda_i\geq0\). Multiplying over coordinates,
\[
A_{ab}
=\prod_{i=1}^d\left(1+\frac{\lambda_i}{\varepsilon}\right)^{-1/2}
\exp\left[-\frac14\sum_{i=1}^d
\frac{\widetilde\delta_i^2}{\varepsilon+\lambda_i}\right].
\]
The determinant and inverse satisfy
\[
\det(I+C/\varepsilon)=\prod_{i=1}^d\left(1+\frac{\lambda_i}{\varepsilon}\right),
\qquad
\delta^\top(\varepsilon I+C)^{-1}\delta
=\sum_{i=1}^d\frac{\widetilde\delta_i^2}{\varepsilon+\lambda_i}.
\]
Hence, with
\[
A_0=\det(I+C/\varepsilon)^{-1/2}>0,
\]
we obtain
\[
A_{ab}=A_0e^{-q_{ab}}.
\]
This calculation includes singular \(C\), the case \(C=0\), and coincident class means.

Finally, \(A_0\) is independent of both class indices. For every fixed row \(a\),
\[
T_{ab}=\frac{A_{ab}}{\sum_{r=1}^K A_{ar}}
=\frac{A_0e^{-q_{ab}}}{A_0\sum_{r=1}^K e^{-q_{ar}}}
=\frac{e^{-q_{ab}}}{\sum_{r=1}^K e^{-q_{ar}}}.
\]
The denominator is positive; in particular, \(q_{aa}=0\), so its \(r=a\) term equals one. This also covers \(K=1\).

Thus the affinity matrix up to its common prefactor, \((A_{ab}/A_0)_{a,b}\), and the mean-field transition matrix exactly are determined by \((q_{ab})_{a,b}\). The unnormalized affinity matrix additionally depends on \(A_0\), which depends on \(C\) and \(\varepsilon\); it is not determined by the separation matrix alone across the permitted models. The transition formula concerns the defined ratio of averaged affinities, not an expectation of pointwise normalized kernel probabilities.
