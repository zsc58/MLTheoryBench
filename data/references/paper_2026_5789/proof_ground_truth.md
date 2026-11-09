# Reference Proof

## Proof Structure

Compute the sensitivity of effective rank to its positive eigenvalues. For the new-direction regime, justify the spectral mass emerging from the kernel even when the old positive eigenvalues are repeated. Its entropy contribution dominates the changes in the old spectrum. For the in-span regime, the kernel remains inactive, and simple-eigenvalue perturbation gives the assumed positive directional derivative.

## Standard Background

We use two finite-dimensional symmetric-matrix facts. All matrix norms in the proof are operator norms.

1. If X and Y are real symmetric matrices of the same dimension, their decreasingly ordered eigenvalues satisfy
   \[
   |\lambda_j(X)-\lambda_j(Y)|\leq\|X-Y\|.
   \]
   This follows from the variational characterization
   \[
   \lambda_j(X)=\min_{\dim L=d-j+1}\ \max_{x\in L,\ \|x\|=1}x^{\mathsf T}Xx,
   \]
   since the Rayleigh quotients differ by at most \(\|X-Y\|\). No simplicity assumption is needed.
2. If a real symmetric matrix A has a simple eigenvalue \(\lambda_k\) with unit eigenvector \(u_k\), then for a fixed real symmetric B there is a differentiable local eigenvalue branch satisfying
   \[
   \lambda_k(A+tB)=\lambda_k+t\,u_k^{\mathsf T}Bu_k+O(t^2).
   \]
   The branch is considered in a neighborhood where that eigenvalue remains isolated. In the application below, simplicity and separation from zero supply this neighborhood.

## Complete Proof

The scatter definitions imply that A and B are real symmetric positive semidefinite matrices. Write
\[
T=\operatorname{tr}(A)>0,\qquad T_t=\operatorname{tr}(A+tB)=T+t\operatorname{tr}(B).
\]
Thus \(T_t>0\) for all \(t\geq0\), so every effective rank in the theorem is defined. Throughout the proof, all asymptotic constants may depend on the fixed matrices A and B and their dimension.

Let \(\lambda_1,\ldots,\lambda_r\) be the positive eigenvalues of A, counted with multiplicity, and put \(p_k=\lambda_k/T\) and \(H=H(A)\).

### Effective-rank sensitivity

As a function of positive eigenvalue coordinates,
\[
\frac{\partial p_j}{\partial\lambda_k}
=\frac{\mathbf 1_{\{j=k\}}-p_j}{T}.
\]
Using \(\sum_jp_j=1\) and \(\sum_jp_j\log p_j=-H\), differentiation gives
\[
\frac{\partial H}{\partial\lambda_k}
=-\sum_j(\log p_j+1)\frac{\mathbf 1_{\{j=k\}}-p_j}{T}
=-\frac{\log p_k+H}{T}.
\]
Consequently,
\[
\frac{\partial r_{\mathrm{eff}}}{\partial\lambda_k}
=-\frac{r_{\mathrm{eff}}(A)}{T}(\log p_k+H)=b_k
\]
whenever the coefficients in the task are used.

### New-direction regime

Suppose \(\tau=\operatorname{tr}(QBQ)>0\). In particular, \(r<d\). Choose orthonormal coordinates for \(\operatorname{range}(A)\oplus\ker(A)\), in which
\[
A=\begin{pmatrix}D&0\\0&0\end{pmatrix},\qquad
B=\begin{pmatrix}E&F\\F^{\mathsf T}&G\end{pmatrix},
\]
where \(D\) is positive definite and \(\operatorname{tr}(G)=\tau\). Both E and G are positive semidefinite.

We first derive the spectral-mass estimate without assuming that the eigenvalues of D are simple. Define the skew-symmetric matrix
\[
K=\begin{pmatrix}0&-D^{-1}F\\F^{\mathsf T}D^{-1}&0\end{pmatrix}
\]
and the orthogonal matrix \(U_t=e^{tK}\). Matrix Taylor expansion gives
\[
U_t^{\mathsf T}(A+tB)U_t
=A+t(B+AK-KA)+R_t
=\begin{pmatrix}D+tE&0\\0&tG\end{pmatrix}+R_t,
\qquad \|R_t\|=O(t^2).
\]
Indeed, the off-diagonal blocks of \(AK-KA\) are \(-F\) and \(-F^{\mathsf T}\), while its diagonal blocks vanish.

For sufficiently small positive t, all r eigenvalues of \(D+tE\) are bounded away from zero, whereas the eigenvalues of \(tG\) are \(O(t)\). Apply the eigenvalue norm bound to the two real symmetric matrices in the last display. Orthogonal conjugation preserves eigenvalues, so the d−r eigenvalues of \(A+tB\) converging to zero have total mass
\[
t\operatorname{tr}(G)+O(t^2)=t\tau+O(t^2).
\]
This argument includes repeated positive eigenvalues of A and zero eigenvalues of G. All eigenvalues of \(A+tB\) are nonnegative, so permanently zero eigenvalues do not affect this mass or the entropy.

The same eigenvalue norm bound applied directly to A and \(A+tB\) shows that the r old eigenvalues differ from the positive eigenvalues of A by \(O(t)\). After division by \(T_t=T+O(t)\), their normalized weights differ from \(p_1,\ldots,p_r\) by \(O(t)\). Since \(-x\log x\) is smooth near each positive \(p_k\), their combined entropy contribution is \(H(A)+O(t)\).

The total normalized mass of the new positive eigenvalues is
\[
\varepsilon_t=\frac{t\tau+O(t^2)}{T_t}
=\frac{\tau}{T}t+O(t^2)>0
\]
for sufficiently small positive t. Write their weights as \(\varepsilon_t a_1,\ldots,\varepsilon_t a_s\), with \(a_j>0\) and \(\sum_j a_j=1\). Their entropy contribution satisfies
\[
-\sum_j\varepsilon_ta_j\log(\varepsilon_ta_j)
=-\varepsilon_t\log\varepsilon_t
+\varepsilon_t\left(-\sum_j a_j\log a_j\right)
\geq-\varepsilon_t\log\varepsilon_t.
\]
Here
\[
-\varepsilon_t\log\varepsilon_t
=\frac{\tau}{T}t\log(1/t)+O(t).
\]
Combining the old- and new-spectrum contributions, there is a finite constant C such that, for all sufficiently small positive t,
\[
H(A+tB)-H(A)
\geq\frac{\tau}{T}t\log(1/t)-Ct.
\]
Since \(\tau/T>0\), this is strictly positive throughout a sufficiently small right neighborhood of zero. Exponentiation gives the required strict effective-rank increase.

### In-span regime

Suppose instead that the second alternative holds. Because B is symmetric and \(\operatorname{range}(B)\subseteq\operatorname{range}(A)\), it annihilates \(\ker(A)\): for \(x\in\ker(A)\) and every y,
\[
y^{\mathsf T}Bx=(By)^{\mathsf T}x=0.
\]
It has no cross-block between the range and kernel of A. On \(\operatorname{range}(A)\), the restriction of A is positive definite and that of B is positive semidefinite. Hence \(A+tB\) has exactly the same kernel as A for every \(t\geq0\). The restricted matrix also stays positive definite in a sufficiently small two-sided neighborhood of zero, where effective rank is a smooth function of its r positive eigenvalues.

The positive eigenvalues of A are simple and separated from each other and from zero. The stated simple-eigenvalue perturbation result therefore applies and gives
\[
\lambda_k(A+tB)=\lambda_k+t\,u_k^{\mathsf T}Bu_k+O(t^2).
\]
The chain rule and the sensitivity formula yield
\[
\left.\frac{d}{dt}r_{\mathrm{eff}}(A+tB)\right|_{t=0}
=\sum_{k=1}^r b_k\,u_k^{\mathsf T}Bu_k=:c.
\]
The hypothesis says \(c>0\). Differentiability gives
\[
r_{\mathrm{eff}}(A+tB)-r_{\mathrm{eff}}(A)=ct+o(t)>0
\]
for every sufficiently small positive t.

Thus either alternative supplies a number \(t_0>0\) with the claimed inequality for every \(t\in(0,t_0)\).
