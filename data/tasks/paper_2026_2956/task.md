# Problem

## Setup

Let \(d\ge1\), \(\lambda>0\), and let \(\Sigma\in\mathbb R^{d\times d}\) be symmetric positive definite with simple eigenvalues
\[
\sigma_1>\sigma_2>\cdots>\sigma_d>0
\]
and orthonormal eigenvectors \(u_1,\ldots,u_d\). Let \(X_1,X_2,\ldots\) be iid \(N(0,\Sigma)\). For each integer \(L\ge1\) and \(\mu,z\in\mathbb R^d\), define
\[
A_L(\mu)z=
\frac{\sum_{i=1}^L e^{\lambda(\mu^TX_i)(\mu^Tz)}X_i}
{\sum_{i=1}^L e^{\lambda(\mu^TX_i)(\mu^Tz)}}.
\]
Define the finite-prompt population reconstruction risk by
\[
R_L(\mu)=\mathbb E_{X_1,\ldots,X_L}\|A_L(\mu)X_1-X_1\|^2.
\]
Thus the reconstructed token \(X_1\) is included in the prompt, and the expectation is over the entire prompt.

For an independent \(Z\sim N(0,\Sigma)\), define
\[
A_\infty(\mu)z=\lambda\Sigma\mu\mu^Tz,
\qquad
R_\infty(\mu)=\mathbb E_Z\|A_\infty(\mu)Z-Z\|^2.
\]
Gradient flow for a risk \(R\) is \(\dot\mu=-\nabla R(\mu)\). Write
\[
B_\rho=\{\mu\in\mathbb R^d:\|\mu\|\le\rho\}.
\]

## Task

Prove the following integrated theorem.

1. The infinite-prompt risk is
\[
R_\infty(\mu)=\operatorname{tr}(\Sigma)-2\lambda\mu^T\Sigma^2\mu
+\lambda^2(\mu^T\Sigma\mu)(\mu^T\Sigma^2\mu).
\]
Its critical points are exactly
\[
\{0\}\cup\left\{\pm\frac{u_j}{\sqrt{\lambda\sigma_j}}:1\le j\le d\right\},
\]
and all are nondegenerate. The origin is a strict local maximum, the points with \(j\ge2\) are strict saddles, and the two points with \(j=1\) are the global minima. For Lebesgue-almost-every initialization in \(\mathbb R^d\), gradient flow for \(R_\infty\) exists for all nonnegative times and converges to one of these two minima.

2. There exists \(\rho_0>0\), depending only on \(\Sigma\) and \(\lambda\), such that for every fixed \(\rho\ge\rho_0\) there is an integer \(L_0=L_0(\rho,\Sigma,\lambda)\) with the following properties for every \(L\ge L_0\). The ball \(B_\rho\) is forward invariant for gradient flow of \(R_L\): every trajectory initialized there exists for all nonnegative times and stays there. The critical points of \(R_L\) in \(B_\rho\) are exactly
\[
\{\mu_{L,0}^*\}\cup\{\pm\mu_{L,j}^*:1\le j\le d\}.
\]
These \(2d+1\) points are distinct and nondegenerate. The point \(\mu_{L,0}^*\) is a strict local maximum, the pairs with \(j\ge2\) are strict saddles, and the pair with \(j=1\) consists of strict local minima. They can be labeled so that
\[
\mu_{L,0}^*\longrightarrow0,
\qquad
\mu_{L,j}^*\longrightarrow\frac{u_j}{\sqrt{\lambda\sigma_j}}
\quad(1\le j\le d)
\]
as \(L\to\infty\). For each such \(L\), Lebesgue-almost-every initialization in \(B_\rho\) yields a trajectory converging to one of \(\pm\mu_{L,1}^*\).
