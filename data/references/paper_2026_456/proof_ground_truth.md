# Reference Proof

## Proof Structure

Derive the sufficient-statistic moments from the log-partition function, verify the restricted MLE's asymptotic normality and Fisher information, compute the optimally weighted control-variate variance, and identify the two covariance matrices through a Schur complement.

## Complete Proof

All limiting statements are at a fixed true interior parameter. Write this parameter as \(\eta_0\), its mean as \(\nu_0\), and \(V=\nabla^2\psi(\eta_0)\). Suppress the sample-size subscript on \(y\) when convenient.

### 1. Moments and sufficient-statistic asymptotics

The normalizing identity is
\[
\int \exp\{n\eta^\top y(X)\}g(X)\,dX=\exp\{n\psi(\eta)\}.
\]
At an interior natural parameter, differentiation under this integral is justified by exponential integrability in a neighborhood. In particular, polynomial factors in the sufficient statistic can be dominated by a finite sum of exponential factors at nearby natural parameters. This also supplies smoothness of the log-partition function to every finite order locally.

Differentiating the log normalizer once and twice gives
\[
\mathbb E_\eta[y]=\nabla\psi(\eta),\qquad
\operatorname{Cov}_\eta(y)=\frac1n\nabla^2\psi(\eta).
\]
Thus at the true parameter, \(\mathbb E[y]=\nu_0\), \(\operatorname{Cov}(y)=V/n\), and \(y\to\nu_0\) in probability.

We will also need its limiting distribution. For each fixed \(u\in\mathbb R^p\), the normalizing identity gives, for all sufficiently large \(n\),
\[
\log\mathbb E_{\eta_0}\exp\{u^\top\sqrt n(y-\nu_0)\}
=n\left[\psi(\eta_0+u/\sqrt n)-\psi(\eta_0)-u^\top\nu_0/\sqrt n\right].
\]
Taylor expansion makes this converge to \(u^\top Vu/2\). The moment-generating-function convergence theorem states that convergence of moment generating functions on a neighborhood of zero to the moment generating function of a probability distribution implies weak convergence to that distribution. Its hypotheses hold here by interior exponential integrability and the displayed expansion. Therefore
\[
\sqrt n(y-\nu_0)\Rightarrow N(0,V).
\]
This argument uses the stated joint density for every \(n\); it does not require an additional assumption about independence of the observations.

### 2. Restricted information and verification of MLE asymptotics

First suppose \(t>0\). Let
\[
P=\begin{pmatrix}I_t\\0\end{pmatrix},\qquad \theta=\nu_E,\qquad \theta_0=(\nu_0)_E.
\]
The mean identity holds throughout the parameter domain. Since its canonical Jacobian is \(V\) and \(V\) is nonsingular, the inverse-function theorem gives a smooth local inverse mean parameterization. Holding \(\nu_K\) fixed, its Jacobian at the truth is
\[
J_0:=\frac{\partial\eta}{\partial\theta}(\theta_0)=V^{-1}P.
\]
The restricted score is
\[
U_n(\theta)=nJ(\theta)^\top\bigl[y-(\theta,\nu_K)\bigr].
\]
Consequently its Fisher information at the truth is
\[
\mathbb E[U_n(\theta_0)U_n(\theta_0)^\top]
=nJ_0^\top VJ_0=nP^\top V^{-1}P.
\]
Set \(I=P^\top V^{-1}P=(V^{-1})_{EE}\). It is positive definite because \(P\) has full column rank.

We now verify the existence, consistency, and likelihood-expansion obligations behind the asymptotic-normality step, rather than assume them. For a possible sufficient-statistic value \(z\), define locally
\[
F(\theta,z)=J(\theta)^\top\bigl[z-(\theta,\nu_K)\bigr].
\]
At \((\theta_0,\nu_0)\), this is zero and
\[
D_\theta F=-J_0^\top P=-I,\qquad D_zF=J_0^\top.
\]
The implicit-function theorem gives neighborhoods on which the unique solution of \(F(\theta,z)=0\) is a smooth function \(\theta=h(z)\), with
\[
h(\nu_0)=\theta_0,\qquad Dh(\nu_0)=I^{-1}J_0^\top.
\]

To show that the global restricted MLE is this root with probability tending to one, define
\[
K(\eta)=\psi(\eta)-\psi(\eta_0)-\nu_0^\top(\eta-\eta_0).
\]
Choose a small closed natural-parameter ball of radius \(r>0\), centered at \(\eta_0\), contained in the parameter domain and small enough that its points on the mean-constraint set map into the preceding implicit-function neighborhood. Local positive definiteness of the Hessian implies
\[
\kappa:=\min_{\|\eta-\eta_0\|=r}K(\eta)>0.
\]
The natural log-partition function is convex on its convex domain of finiteness. Along a segment from \(\eta_0\) to any admissible \(\eta\) with \(\|\eta-\eta_0\|\ge r\), convexity and \(K(\eta_0)=0\) imply
\[
K(\eta)\ge\frac{\kappa}{r}\|\eta-\eta_0\|.
\]
This uses the normalizer's convex domain even if a model is expressed on an open subdomain of it. The normalized log-likelihood difference at statistic value \(z\) is
\[
(\eta-\eta_0)^\top(z-\nu_0)-K(\eta).
\]
When \(\|z-\nu_0\|<\kappa/(2r)\), this difference is strictly negative for every admissible \(\eta\) outside or on the sphere.

Inside the closed ball, the set defined by \(\mu_K(\eta)=\nu_K\) is nonempty and compact. The continuous likelihood therefore attains a maximum on that set. No maximizer lies on the sphere, and every parameter outside the ball has smaller likelihood than the feasible true parameter. Hence this is a global restricted maximum. It lies in the interior of the ball and satisfies the restricted score equation. By the chosen neighborhoods it must be the unique root \(h(z)\).

Since \(y\to\nu_0\) in probability, this argument proves that the global restricted maximum exists uniquely and equals \(h(y)\) with probability tending to one. The prescribed measurable extension on the exceptional event cannot change convergence in probability or in distribution. In particular the MLE is consistent, and differentiability of \(h\), together with the sufficient-statistic limit, gives
\[
\sqrt n(\widehat\nu_E-\nu_E)
=I^{-1}J_0^\top\sqrt n(y-\nu_0)+o_P(1)
\Rightarrow N(0,I^{-1}),
\]
because \(J_0^\top VJ_0=I\). This closes the regular-MLE obligation with its hypotheses checked. For a fixed \(\alpha\), the corresponding scalar limiting variance is \(\alpha^\top I^{-1}\alpha\).

### 3. Optimal control coefficient and variance

Partition
\[
V=\begin{pmatrix}A&B\\B^\top&D\end{pmatrix}.
\]
For any deterministic coefficient \(c\), mean matching gives \(\mathbb E[T_c]=\alpha^\top\nu_E\), and the covariance identity gives
\[
n\operatorname{Var}(T_c)=\alpha^\top A\alpha+2c^\top B^\top\alpha+c^\top Dc.
\]
The principal block \(D\) is positive definite when nonempty. Completing the square,
\[
n\operatorname{Var}(T_c)
=\alpha^\top(A-BD^{-1}B^\top)\alpha
+(c+D^{-1}B^\top\alpha)^\top D(c+D^{-1}B^\top\alpha).
\]
Thus the unique minimizing coefficient is
\[
c^*=-D^{-1}B^\top\alpha,
\]
and
\[
n\operatorname{Var}(T_{c^*})=\alpha^\top(A-BD^{-1}B^\top)\alpha.
\]
These are exact finite-sample variance identities for the deterministic population coefficients, not identities for coefficients estimated from the observations.

### 4. Matrix identification and degenerate cases

Put \(S=A-BD^{-1}B^\top\). For every nonzero \(x\in\mathbb R^t\),
\[
x^\top Sx=
\begin{pmatrix}x\\-D^{-1}B^\top x\end{pmatrix}^{\!\top}
V
\begin{pmatrix}x\\-D^{-1}B^\top x\end{pmatrix}>0.
\]
Thus \(S\) is positive definite. The factorization
\[
V=
\begin{pmatrix}I&BD^{-1}\\0&I\end{pmatrix}
\begin{pmatrix}S&0\\0&D\end{pmatrix}
\begin{pmatrix}I&0\\D^{-1}B^\top&I\end{pmatrix}
\]
shows upon inversion that \((V^{-1})_{EE}=S^{-1}\). Therefore
\[
\alpha^\top[(V^{-1})_{EE}]^{-1}\alpha
=\alpha^\top(A-BD^{-1}B^\top)\alpha
=n\operatorname{Var}(T_{c^*}).
\]

If \(t=p\), the control block is empty, \(c^*\) is the unique empty vector, and the same calculation reduces to \(S=V\). If \(t=0\), the estimated parameter and its limiting normal distribution are zero-dimensional, the target is zero, and the unique minimizing control coefficient is zero. For \(\alpha=0\), the same conclusion follows immediately from the completed square. Thus all displayed conclusions hold with the stated empty-block conventions.

Here asymptotic variance means the variance of the limiting normal law after multiplication by \(\sqrt n\). No convergence of the MLE's finite-sample second moments is asserted or needed.
