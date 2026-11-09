# Reference Proof

## Proof Structure

We give an explicit equal-marginal Gaussian construction, compute the population least-squares slopes directly from second moments, and apply symmetric-matrix perturbation bounds to the covariance matrices. For the subspace bound, we distinguish the regime where its right-hand side is already at least one from the regime where spectral separation can be verified.

## Complete Proof

Let \(0<\rho<1\), for example \(\rho=1/2\), and let \(s>0\). On the first two coordinates define centered Gaussian laws with covariance blocks
\[
B_+=s^2\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},\qquad
B_-=s^2\begin{pmatrix}1&-\rho\\ -\rho&1\end{pmatrix}.
\]
Both matrices are positive definite. For \(d>2\), append coordinates that are independent \(N(0,s^2)\) variables under both laws and independent of the first two coordinates. Denote the resulting laws by \(P\) and \(Q\), respectively.

Every coordinate under either law has distribution \(N(0,s^2)\), so \(P_j=Q_j\) for all \(j\). The laws are nevertheless distinct, since their first-two-coordinate covariances are \(s^2\rho\) and \(-s^2\rho\). Their marginals are continuous; by uniqueness of the copula for continuous marginals, two different joint laws with these common marginals have different copula measures. Consequently, for every characteristic kernel \(k\), the MMD of the two copula measures is strictly positive.

The covariance difference vanishes except in positions \((1,2)\) and \((2,1)\), where its entries are \(2s^2\rho\). Therefore
\[
\delta(P,Q)=\|C_P-C_Q\|_F=2\sqrt{2}\,s^2\rho.
\]
Choosing \(s\) sufficiently large makes this quantity exceed any prescribed \(M>0\). This proves part 1.

For part 2, write \(c_P=\operatorname{Cov}_P(X,Y)\) and \(c_Q=\operatorname{Cov}_Q(X,Y)\). Centering and minimizing \(\mathbb E_R[(Y-bX)^2]\) over \(b\) give
\[
\beta_R=\frac{\operatorname{Cov}_R(X,Y)}{\operatorname{Var}_R(X)}
\]
whenever \(\operatorname{Var}_R(X)>0\). The equal-variance assumption thus yields
\[
|\beta_P-\beta_Q|=\frac{|c_P-c_Q|}{\sigma_X^2}.
\]
The diagonal entries of \(C_P-C_Q\) are zero, while its two off-diagonal entries both equal \(c_P-c_Q\). Hence
\[
\delta(P,Q)=\sqrt{2}\,|c_P-c_Q|,
\]
and substituting gives the asserted equality. In the Gaussian construction above, considered in dimension two, the slopes are \(\rho\) and \(-\rho\), respectively, so they have opposite signs.

For part 3, set \(A=C_P\), \(B=C_Q\), \(E=B-A\), and \(\varepsilon=\|E\|_2\). Both covariance matrices are real symmetric and \(\varepsilon\leq\|E\|_F=\delta(P,Q)\). Weyl's eigenvalue perturbation inequality for ordered eigenvalues of real symmetric matrices gives, for every \(k\),
\[
|\lambda_k(A)-\lambda_k(B)|\leq\varepsilon\leq\delta(P,Q).
\]

Now suppose \(\gamma=\lambda_r(A)-\lambda_{r+1}(A)>0\) and \(\delta(P,Q)<\gamma\). The largest sine of principal angles between two subspaces is at most one. Thus, if \(\delta(P,Q)\geq\gamma/2\), the required bound holds for every choice of a top-\(r\) subspace of \(B\), including when its \(r\)-th eigenvalue is tied with its \((r+1)\)-st.

If \(\delta(P,Q)<\gamma/2\), then \(\varepsilon<\gamma/2\). Weyl's inequality gives
\[
\lambda_r(B)-\lambda_{r+1}(B)\geq\gamma-2\varepsilon>0,
\qquad
\lambda_r(A)-\lambda_{r+1}(B)\geq\gamma-\varepsilon>0.
\]
Choose orthonormal bases \(U\) for the top-\(r\) eigenspace of \(A\) and \(V\) for the bottom-\((d-r)\) eigenspace of \(B\). Write \(AU=UD\), \(BV=VH\), with \(D,H\) symmetric, and set \(T=U^\top V\). From \(B=A+E\),
\[
DT-TH=-U^\top EV.
\]
Every eigenvalue of \(D\) is at least \(\lambda_r(A)\), and every eigenvalue of \(H\) is at most \(\lambda_{r+1}(B)\). With \(g=\lambda_r(A)-\lambda_{r+1}(B)>0\), the solution has the convergent representation
\[
T=-\int_0^\infty e^{-tD}(U^\top EV)e^{tH}\,dt.
\]
Taking operator norms gives \(\|T\|_2\leq\varepsilon/g\leq\varepsilon/(\gamma-\varepsilon)\). Since \(V\) spans the orthogonal complement of the top-\(r\) eigenspace of \(B\), \(\|U^\top V\|_2=\|\sin\Theta(U_P,U_Q)\|_2\). Finally, \(\varepsilon<\gamma/2\) implies
\[
\|\sin\Theta(U_P,U_Q)\|_2
\leq\frac{\varepsilon}{\gamma-\varepsilon}
\leq\frac{2\varepsilon}{\gamma}
\leq\frac{2\delta(P,Q)}{\gamma}.
\]
This proves the subspace bound in both regimes and completes the proof.
