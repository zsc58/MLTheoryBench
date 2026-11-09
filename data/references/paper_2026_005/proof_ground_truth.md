# Reference Proof

## Proof Structure

Work at the fixed context. Differentiate the finite exponential-family normalizer to identify the mean and natural-coordinate Fisher matrix, express the KL divergence, control the two Taylor remainders uniformly, and apply the spectral bounds and their equality criterion.

## Complete Proof

Suppress the fixed context from the notation. All sums below are over the common support S={v in V:h(v)>0}; outcomes outside S have probability zero for every parameter and contribute nothing to expectations. Since V is finite and the sufficient statistics are finite vectors, the normalizer is a finite positive sum and can be differentiated term by term. Normalization gives
\[
A(\eta)=\log\sum_{v\in S}h(v)e^{\eta^{\mathsf T}T(v)}.
\]
Consequently, writing \(\mu(\eta)=\nabla A(\eta)\),
\[
\mu(\eta)=\mathbb E_{p_\eta}[T],\qquad
\nabla_\eta\log p_\eta(v)=T(v)-\mu(\eta),\qquad
\nabla^2A(\eta)=\mathbb E_{p_\eta}[(T-\mu(\eta))(T-\mu(\eta))^{\mathsf T}].
\]
In particular, differentiation before evaluation at \(\eta_{\mathrm{ref}}\) gives exactly the score specified in the task, and
\[
F_{\mathrm{ref}}=\nabla^2A(\eta_{\mathrm{ref}}).
\]
This is a natural-coordinate identity, not an identification with a Fisher matrix in arbitrary other parameter coordinates.

Write \(\eta=\eta_{\mathrm{ref}}+\delta\). The distributions have the same support, so their log ratio is finite there. Taking its expectation under \(p_\eta\) gives
\[
D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})
=\delta^{\mathsf T}\mu(\eta)-A(\eta)+A(\eta_{\mathrm{ref}}).
\]

Let \(M\) be the stated uniform operator-norm bound for the third derivative of \(A\). The segment \(\eta_{\mathrm{ref}}+s\delta\), \(0\le s\le1\), is contained in the prescribed neighborhood whenever \(\|\delta\|<r\). Taylor's theorem, with the Euclidean norm and its induced multilinear operator norm, yields
\[
A(\eta_{\mathrm{ref}}+\delta)
=A(\eta_{\mathrm{ref}})+\mu(\eta_{\mathrm{ref}})^{\mathsf T}\delta
+\tfrac12\delta^{\mathsf T}F_{\mathrm{ref}}\delta+R_A,
\qquad |R_A|\le\frac M6\|\delta\|^3,
\]
and
\[
\mu(\eta_{\mathrm{ref}}+\delta)
=\mu(\eta_{\mathrm{ref}})+F_{\mathrm{ref}}\delta+R_\mu,
\qquad \|R_\mu\|\le\frac M2\|\delta\|^2.
\]
For the second estimate, the second directional derivative of the vector-valued function \(\mu\) has norm at most \(M\|\delta\|^2\): its inner product with any unit vector \(w\) is \(D^3A[w,\delta,\delta]\). Thus the scalar and vector estimates use the same bound and are uniform over the entire ball.

Substitution cancels the constant and linear terms and gives
\[
D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})
=\tfrac12\delta^{\mathsf T}F_{\mathrm{ref}}\delta+R_3(\delta),
\qquad R_3(\delta)=\delta^{\mathsf T}R_\mu-R_A.
\]
Therefore
\[
|R_3(\delta)|\le\|\delta\|\|R_\mu\|+|R_A|
\le\frac{2M}{3}\|\delta\|^3.
\]
One may take \(C=2M/3\), or any larger constant. It is independent of \(\delta\).

The matrix \(F_{\mathrm{ref}}\) is symmetric positive definite. Choose an orthonormal eigenbasis \(e_1,\ldots,e_d\) with eigenvalues \(\lambda_1,\ldots,\lambda_d\), and write \(\delta=\sum_i a_i e_i\). Then
\[
\delta^{\mathsf T}F_{\mathrm{ref}}\delta=\sum_i\lambda_i a_i^2,
\qquad \|\delta\|^2=\sum_i a_i^2.
\]
It follows that
\[
\lambda_{\min}(F_{\mathrm{ref}})\|\delta\|^2
\le\delta^{\mathsf T}F_{\mathrm{ref}}\delta
\le\lambda_{\max}(F_{\mathrm{ref}})\|\delta\|^2.
\]
Combining these inequalities with the remainder bound proves
\[
\tfrac12\lambda_{\min}(F_{\mathrm{ref}})\|\delta\|^2-C\|\delta\|^3
\le D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})
\le\tfrac12\lambda_{\max}(F_{\mathrm{ref}})\|\delta\|^2+C\|\delta\|^3.
\]

For nonzero \(\delta\), the leading quadratic coefficient is
\(\delta^{\mathsf T}F_{\mathrm{ref}}\delta/(2\|\delta\|^2)\). Its equality with \(\lambda_{\max}(F_{\mathrm{ref}})/2\) is equivalent to
\[
\sum_i(\lambda_{\max}(F_{\mathrm{ref}})-\lambda_i)a_i^2=0.
\]
Every summand is nonnegative, so this holds exactly when all components outside the maximal-eigenvalue eigenspace vanish. This handles repeated eigenvalues as well as the simple-eigenvalue case. At \(\delta=0\), the distributions coincide, the KL divergence and remainder are zero, and both sandwich inequalities hold; the directional coefficient assertion is deliberately restricted to nonzero displacement.
