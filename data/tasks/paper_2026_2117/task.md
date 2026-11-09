# Problem

## Setup

Fix alpha in (0,1), and consider sequences of positive integers n,D tending to infinity with n/D tending to alpha. For each sufficiently large pair (n,D), draw independent observations X_1,...,X_D from P_n=N(0,I_n), and define the empirical covariance by

S=(1/D) sum_{j=1}^D X_j X_j^T.

The population mean is known to be zero; no sample mean is subtracted. Let lambda_1>=...>=lambda_n be the eigenvalues of S, with corresponding orthonormal eigenvectors u_1,...,u_n.

For a fixed epsilon in (0,1) and a deterministic integer rank k in {0,...,n}, define Q_{epsilon,k} to be the zero-mean Gaussian with covariance

sum_{i=1}^k lambda_i u_i u_i^T + epsilon sum_{i=k+1}^n u_i u_i^T.

Thus retained variances are the empirical eigenvalues, and discarded variances are epsilon. The covariance is positive definite almost surely for all sufficiently large n,D.

For r in [0,1], let G_epsilon(r) denote the limiting expected KL error per coordinate,

G_epsilon(r)=lim (1/n) E[D_KL(P_n||Q_{epsilon,k})],

along deterministic rank sequences k/n tending to r and the dimension sequences specified above. The expectation is over the training observations, and D_KL(P||Q)=integral p(x)log(p(x)/q(x))dx uses natural logarithms.

The limiting empirical eigenvalue density is

rho(lambda)=[1/(2 pi alpha lambda)] sqrt((lambda_+-lambda)(lambda-lambda_-)),  lambda in [lambda_-,lambda_+],

where lambda_±=(1±sqrt(alpha))^2, and rho is zero outside this interval. For c in [lambda_-,lambda_+], define

r(c)=integral_c^{lambda_+} rho(lambda)d lambda.

This identifies a limiting rank ratio with its spectral cutoff, with r(lambda_-)=1 and r(lambda_+)=0.

## Task

Prove the following integrated theorem for the limiting expected-error curve.

For every epsilon in (lambda_-,1), the unique interior local minimum of G_epsilon on the rank-ratio interval [0,1] is attained at cutoff c=epsilon, with rank ratio

r_epsilon=integral_epsilon^{lambda_+} rho(lambda)d lambda.

Equivalently, in the limiting cutoff description, this choice retains the empirical eigenvalues above epsilon.

There exists a unique epsilon_*(alpha) in (lambda_-,1) such that

G_{epsilon_*}(r(epsilon_*))=G_{epsilon_*}(0).

Moreover, for 0<epsilon<1, a global minimizer r_* of G_epsilon over [0,1] is given by the three phases:

1. If 0<epsilon<=lambda_-(alpha), retain all components: r_*=1.
2. If lambda_-(alpha)<epsilon<epsilon_*(alpha), use the interior rank: r_*=r_epsilon.
3. If epsilon_*(alpha)<=epsilon<1, collapse to rank zero: r_*=0.

At epsilon=epsilon_*(alpha), both the interior rank and collapse have equal limiting error and are global minimizers.
