# Problem

## Setup

Let \(d,M,r,F\) be fixed positive integers, let \(\nu\) be a probability measure supported on a manifold \(\mathcal X\subset\mathbb R^d\), and fix \(\lambda>0\). Let \(\mathcal D\) be a fixed, nonempty dictionary of \(M\) kernel-bandwidth pairs \(\theta=(k,\sigma)\), with \(\sigma>0\), chosen independently of the observations. Write \(k_\theta\) for the kernel at the specified bandwidth. Each \(k_\theta\) is a real, twice continuously differentiable positive-definite kernel on \(\mathbb R^d\), and there is a finite constant \(\kappa_\infty\) such that
\[
k_\theta(x,x)\le\kappa_\infty
\qquad(\theta\in\mathcal D,\ x\in\mathbb R^d).
\]

For each \(\theta\), let \(\mathcal H_\theta\) be its real reproducing kernel Hilbert space. Assume its gradient form is bounded: there is a finite \(B_\theta\) such that
\[
\int_{\mathcal X}\sum_{a=1}^d|\partial_a h(x)|^2\,d\nu(x)
\le B_\theta\|h\|_{\mathcal H_\theta}^2
\qquad(h\in\mathcal H_\theta).
\]
Define the covariance and gradient operators on \(\mathcal H_\theta\) by
\[
\langle g,\Sigma_\theta h\rangle_{\mathcal H_\theta}
=\int_{\mathcal X}g(x)h(x)\,d\nu(x),
\qquad
\langle g,L_\theta h\rangle_{\mathcal H_\theta}
=\int_{\mathcal X}\sum_{a=1}^d\partial_a g(x)\partial_a h(x)\,d\nu(x).
\]
Here \(g,h\in\mathcal H_\theta\). With \(I\) denoting the identity on that space, set
\[
T_{\theta,\lambda}
=(L_\theta+\lambda I)^{-1/2}\Sigma_\theta(L_\theta+\lambda I)^{-1/2}.
\]
Let \(\mu_1^\infty(\theta),\ldots,\mu_r^\infty(\theta)\) be its first \(r\) eigenvalues in nonincreasing order, counted with multiplicity; take \(r\) such that these eigenvalues exist for every candidate.

For sample sizes \(N\) divisible by \(F\), observe \(X_1,\ldots,X_N\) independently with common law \(\nu\). Partition their indices into \(F\) equal folds, using a partition fixed in advance or randomized independently of the observations. Denote the common held-out size by \(N_f=N/F\). For each candidate and fold, let \(\widehat\mu_j^{(f)}(\theta)\), \(1\le j\le r\), be given real-valued measurable held-out eigenvalue estimates of the corresponding population eigenvalues. Any landmark set used to compute these estimates is fixed in advance. Probabilities include the randomness of the data, any randomized fold partition, and any randomness used in computing the estimates.

Assume there is a constant \(c>0\), independent of \(N\) and uniform over candidates, folds, and \(1\le j\le r\), such that for every \(t>0\),
\[
\mathbb P\left(\left|\widehat\mu_j^{(f)}(\theta)-\mu_j^\infty(\theta)\right|>t\right)
\le 2\exp(-cN_f t^2).
\]
The dictionary, distribution, regularization, and integers \(M,r,F\) remain fixed as \(N\to\infty\), so \(N_f\to\infty\). Define
\[
R(\theta)=-\sum_{j=1}^r\mu_j^\infty(\theta),\qquad
\widehat R_N(\theta)=-\frac1F\sum_{f=1}^F\sum_{j=1}^r\widehat\mu_j^{(f)}(\theta),
\]
and let \(\widehat\theta_N\) be any measurable minimizer of \(\widehat R_N\) over \(\mathcal D\).

Suppose the population risk has a unique minimizer \(\theta^*\), with a fixed margin \(\Delta>0\):
\[
R(\theta)-R(\theta^*)\ge\Delta
\qquad(\theta\in\mathcal D,\ \theta\ne\theta^*).
\]

## Task

Prove that, for all sufficiently large admissible sample sizes,
\[
\mathbb P(\widehat\theta_N\ne\theta^*)
\le 2MFr\exp\left(-\frac{cN_f\Delta^2}{4r^2}\right),
\]
and conclude that \(\widehat\theta_N\) converges in probability to \(\theta^*\) as \(N\to\infty\), with the dictionary equipped with its discrete topology.
