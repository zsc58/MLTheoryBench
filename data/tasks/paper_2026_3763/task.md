# Problem

## Setup

Let \(p,t\) be integers with \(p\ge 1\) and \(2^p>t>p\). Let \(P=\{1,\ldots,p\}\), and identify each coalition \(S\subseteq P\) with its binary vector \(z\in\{0,1\}^p\). Let \(Z\) denote the matrix whose rows list all \(2^p\) coalitions in a fixed order. For a value function \(\nu:2^P\to\mathbb R\), write \(\vartheta=\nu(Z)\in\mathbb R^{2^p}\). For \(j\in P\), define
\[
\phi_j(\nu)=\sum_{S\subseteq P\setminus\{j\}}\frac{\nu(S\cup\{j\})-\nu(S)}{p\binom{p-1}{|S|}}.
\]
Let \(A\in\mathbb R^{p\times 2^p}\) be the matrix implementing this linear map, so \(\phi=A\vartheta\).

Let \(D_{t-1}\) contain \(t-1\) previously evaluated distinct coalitions and their observations, and let \(X=(x_1,\ldots,x_{t-1})\) list their binary vectors. Work conditional on this realized data and on fixed, given kernel parameters. The Gaussian-process surrogate has posterior
\[
\vartheta\mid D_{t-1}\sim N(\mu,\Sigma).
\]
For finite lists \(U,V\) of binary vectors, define \(K(U,V)_{ab}=k(U_a,V_b)\), where
\[
k(x,x')=\prod_{r=1}^p\exp\!\left(-\frac{\mathbf 1[x_r\ne x'_r]}{\ell_r^2}\right),\qquad \ell_r\in(0,\infty).
\]
The observation model uses independent Gaussian errors of a fixed variance \(\sigma_\epsilon^2>0\), independent of the latent coalition values. The posterior covariance is
\[
\Sigma=K(Z,Z)-K(Z,X)[K(X,X)+\sigma_\epsilon^2I_{t-1}]^{-1}K(X,Z).
\]
For a candidate coalition \(z_i\), the \(i\)-th row of \(Z\), not yet observed, let \(e_i\) be its coordinate vector in \(\mathbb R^{2^p}\). Its prospective observation is
\[
y_i=e_i^\top\vartheta+\epsilon,\qquad \epsilon\sim N(0,\sigma_\epsilon^2),
\]
where this fresh error is independent of the latent vector and the previous observations. The same fixed kernel and noise parameters are used when conditioning on this prospective observation.

Define the expected information gain under the surrogate by
\[
\mathcal I_i=h(\phi\mid D_{t-1})-\mathbb E_{y_i\mid D_{t-1}}\bigl[h(\phi\mid y_i,D_{t-1})\bigr].
\]
Here \(h(W)=-\int f_W(w)\log f_W(w)\,dw\) denotes differential entropy for a vector with density \(f_W\). The expectation is over the prospective observation at the fixed candidate, not over previous datasets.

## Task

Prove that \(\mathcal I_i\) is, up to a positive candidate-independent scaling and an additive candidate-independent constant,
\[
\log\!\bigl(e_i^\top(\Sigma+\sigma_\epsilon^2I_{2^p})e_i\bigr)-\log\!\bigl(e_i^\top(\Sigma+\sigma_\epsilon^2I_{2^p}-Q)e_i\bigr),
\qquad Q=(A\Sigma)^\top(A\Sigma A^\top)^{-1}(A\Sigma),
\]
and that this quantity can be evaluated for any candidate coalition in \(O(p^4+t^3)\) time.

For the computational claim, the input is the finite description consisting of \(X\), the binary candidate, the lengthscales, and the noise variance. Count arithmetic operations and scalar square-root, exponential, and logarithm evaluations at unit cost.
