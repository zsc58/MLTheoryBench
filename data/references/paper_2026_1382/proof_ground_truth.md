# Reference Proof

## Proof Structure

1. Account for the per-application normalizations and show that after \(k\) oracle applications the state is proportional to \(\rho^k|\phi_0\rangle\); the doubling schedule uses \(2^T-1\) applications.
2. Decompose the initial state into the dominant eigenspace and its orthogonal complement, and bound the two spectral components.
3. Derive the normalized dominant-subspace fidelity lower bound and solve it for \(k\).
4. Apply the doubling schedule to obtain the uniform oracle complexity, including its additive constant.

## Complete Proof

The initial state is already unit, so the initial normalization leaves it unchanged. Normalizing after each application changes only the scalar of the current nonzero vector. Inductively, after \(k\) applications the current state is
\[
|\phi^{(k)}\rangle=\frac{\rho^k|\phi_0\rangle}{\|\rho^k|\phi_0\rangle\|}.
\]
The denominator is nonzero because \(\alpha>0\) and \(\lambda_1>\lambda_{R+1}\ge0\), hence \(\lambda_1>0\). In round \(t\), \(\beta_t=2^{t-1}\), so after \(T\) rounds the total number of applications is
\[
N_T=\sum_{t=1}^T2^{t-1}=2^T-1.
\]

Let \(P\) project onto \(S_R\) and let \(Q=I-P\). Decompose \(|\phi_0\rangle=P|\phi_0\rangle+Q|\phi_0\rangle\). Since \(\rho\) equals \(\lambda_1 I\) on \(S_R\),
\[
\|\rho^kP|\phi_0\rangle\|^2=\alpha\lambda_1^{2k}.
\]
All eigenvalues on the range of \(Q\) are at most \(\lambda_{R+1}\), hence
\[
\|\rho^kQ|\phi_0\rangle\|^2\le(1-\alpha)\lambda_{R+1}^{2k}.
\]
The two terms are orthogonal, so
\[
\|P|\phi^{(k)}\rangle\|^2
\ge \frac{\alpha}{\alpha+(1-\alpha)(\lambda_{R+1}/\lambda_1)^{2k}}
=\frac{\alpha}{\alpha+(1-\alpha)r^{2k}}.
\]
For \(0<r<1\), this is at least \(1-\varepsilon\) whenever
\[
(1-\alpha)r^{2k}\le \frac{\alpha\varepsilon}{1-\varepsilon},
\]
which holds when
\[
k\ge \max\left\{0,\frac{\log((1-\alpha)(1-\varepsilon)/(\alpha\varepsilon))}{2\log(1/r)}\right\}.
\]
If \(\alpha=1\), the initial state already lies in \(S_R\). If \(r=0\), one application removes the orthogonal component, so the fidelity is one. Choosing the least doubling-round count with \(N_T=2^T-1\) above the displayed threshold proves the target. The least such dyadic count is at most twice the threshold plus an additive constant, so uniformly the number of oracle calls is
\[
O\left(1+\frac{\log(1/\varepsilon)+\log(1/\alpha)}{\log(\lambda_1/\lambda_{R+1})}\right),
\]
with the one-application interpretation when \(\lambda_{R+1}=0\).
