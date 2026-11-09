# Problem

## Setup

Let \(\rho\) be a positive semidefinite Hermitian operator on a finite-dimensional space with operator norm \(\|\rho\|_{\mathrm{op}}\le 1\), orthonormal eigenvectors \(\{ |\psi_j\rangle\}_{j=1}^d\), and eigenvalues \(\lambda_1\ge\cdots\ge\lambda_d\ge0\). Fix \(1\le R<d\) such that \(\lambda_1=\cdots=\lambda_R>\lambda_{R+1}\). Let \(S_R=\operatorname{span}\{|\psi_1\rangle,\ldots,|\psi_R\rangle\}\), with orthogonal projector \(P\). Let \(|\phi_0\rangle\) be a unit vector and define
\[
\alpha=\|P|\phi_0\rangle\|^2>0,
\qquad r=\frac{\lambda_{R+1}}{\lambda_1}<1.
\]

The procedure first normalizes \(|\phi_0\rangle\). For a nonnegative integer \(T\), in round \(t=1,\ldots,T\), set \(\beta_t=2^{t-1}\), apply \(\rho\) exactly \(\beta_t\) times, and normalize after every application. Let \(|\phi_T\rangle\) denote the final state, and count each application of \(\rho\) as one oracle call.

## Task

Prove that for every \(\varepsilon\in(0,1)\), in the nontrivial case \(0<\alpha<1\) and \(0<r<1\), choosing \(T\) so that
\[
2^T-1\ge \max\left\{0,\frac{\log((1-\alpha)(1-\varepsilon)/(\alpha\varepsilon))}{2\log(\lambda_1/\lambda_{R+1})}\right\}
\]
ensures
\[
\|P|\phi_T\rangle\|^2\ge1-\varepsilon.
\]
If \(\alpha=1\), the initial state already has fidelity one; if \(r=0\), one application has fidelity one. Consequently, for \(0<\alpha<1\) and \(0<r<1\), the number of oracle calls is
\[
O\left(1+\frac{\log(1/\varepsilon)+\log(1/\alpha)}{\log(\lambda_1/\lambda_{R+1})}\right),
\]
with the evident one-application interpretation when \(r=0\).
