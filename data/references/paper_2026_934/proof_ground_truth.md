# Reference Proof

## Proof Structure

1. Derive the environment-wise risk decomposition using the fixed structural law, independence, and centering.
2. Average over the labeled subset, and separately identify the feature-mean covariance across all training environments with the perturbation-mean covariance.
3. Derive realizability of every admissible second moment from the richness of the perturbation-law family, then compute the exact worst-case risk.
4. Transfer minimizers by pointwise equality. Verify that singular objectives do not obstruct existence.

## Complete Proof

Write \(Z=f_0(Y,U,\varepsilon_X)\). Its joint law with \(Y\) is fixed across environments. For \(\beta\in\mathbb R^d\), define
\[
R_0(\beta)=\mathbb E[(Y-\beta^\top Z)^2].
\]
The stated second-moment assumptions make this quantity finite. They also make each environment risk finite because \(X=Z+\varepsilon_e\).

### 1. Environment-wise decomposition

The pair \((Y,Z)\) is a measurable function of the structural noises, so it is independent of \(\varepsilon_e\). Moreover,
\[
\mathbb E[Y-\beta^\top Z]=0.
\]
Consequently, expanding the square and factoring the integrable cross term gives
\[
\begin{aligned}
\mathbb E^e[(Y-\beta^\top X)^2]
&=R_0(\beta)-2\mathbb E[Y-\beta^\top Z]\,\mathbb E^e[\beta^\top\varepsilon_e]
  +\mathbb E^e[(\beta^\top\varepsilon_e)^2]\\
&=R_0(\beta)+\beta^\top M_e\beta.
\end{aligned}
\]
No centering of the perturbations is assumed or needed.

### 2. The two environment averages

Averaging only over the labeled subset gives
\[
\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[(Y-\beta^\top X)^2]
=R_0(\beta)+\beta^\top\bar M\beta.
\]
For each of the \(p\) training environments, centering of \(Z\) gives
\[
\mathbb E^{e_i}[X]=\mathbb E[Z]+\mathbb E^{e_i}[\varepsilon_{e_i}]=\mu_i.
\]
Thus \(K=[\mu_1,\ldots,\mu_p]\), and its explicitly defined covariance satisfies
\[
H=\frac1p\sum_{i=1}^p\mu_i\mu_i^\top-\bar\mu\bar\mu^\top
 =\frac1p\sum_{i=1}^p(\mu_i-\bar\mu)(\mu_i-\bar\mu)^\top=V.
\]
For every vector \(v\),
\[
v^\top Vv=\frac1p\sum_{i=1}^p\bigl(v^\top(\mu_i-\bar\mu)\bigr)^2\ge0.
\]
Hence \(V\) and \(H\) are positive semidefinite. Each \(M_e\), and therefore \(\bar M\), is also positive semidefinite, since \(v^\top M_ev=\mathbb E^e[(v^\top\varepsilon_e)^2]\ge0\).

### 3. Moment realizability and the exact supremum

By definition, every environment in \(\mathcal E_\gamma\) has second moment \(\bar M+A\) for some \(A\in\Delta_\gamma\). Conversely, fix such an \(A\) and put \(B=\bar M+A\). This is a finite symmetric positive-semidefinite matrix.

Here is an explicit realization. The finite-dimensional spectral theorem states that a real symmetric matrix admits an orthonormal eigenbasis; positive semidefiniteness makes its eigenvalues nonnegative. Write
\[
B=\sum_{j=1}^d\lambda_j u_j u_j^\top,\qquad \lambda_j\ge0.
\]
Give each of the \(2d\) values \(\sqrt{d\lambda_j}\,u_j\) and \(-\sqrt{d\lambda_j}\,u_j\), counted with multiplicity, probability \(1/(2d)\). The resulting random vector \(\eta\) satisfies
\[
\mathbb E[\eta\eta^\top]=\sum_{j=1}^d\lambda_j u_j u_j^\top=B,
\qquad
\mathbb E\|\eta\|_2^2=\sum_{j=1}^d\lambda_j<\infty.
\]
It can be taken independent of the structural noises by using their product probability law. The stipulated environment family includes this perturbation law. Hence there is an environment with \(M_e=B\), and it belongs to \(\mathcal E_\gamma\).

It follows that
\[
\{M_e-\bar M:e\in\mathcal E_\gamma\}=\Delta_\gamma.
\]
In particular, the uncertainty class is nonempty. Using the risk decomposition,
\[
\sup_{e\in\mathcal E_\gamma}\mathbb E^e[(Y-\beta^\top X)^2]
=R_0(\beta)+\beta^\top\bar M\beta
 +\sup_{0\preceq A\preceq\gamma V}\beta^\top A\beta.
\]
The order constraint gives \(\beta^\top A\beta\le\gamma\beta^\top V\beta\). Since \(\gamma\ge0\) and \(V\succeq0\), the matrix \(A=\gamma V\) is admissible. The construction above realizes its associated second moment, so the bound is attained. Therefore
\[
\begin{aligned}
\sup_{e\in\mathcal E_\gamma}\mathbb E^e[(Y-\beta^\top X)^2]
&=R_0(\beta)+\beta^\top\bar M\beta+\gamma\beta^\top V\beta\\
&=\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[(Y-\beta^\top X)^2]
 +\gamma\beta^\top H\beta.
\end{aligned}
\]
This is the required identity for every \(\beta\).

### 4. Minimizers and degenerate cases

The two objectives agree pointwise, so their sets of minimizers coincide. In particular, every \(\beta_\gamma\) specified in the task is minimax-optimal.

For completeness, the defining minimizer exists even when the objective is singular. Set
\[
C=\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[XX^\top]+\gamma H,
\qquad
b=\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[XY].
\]
The objective has the form \(c-2b^\top\beta+\beta^\top C\beta\), with \(C\succeq0\). If \(v\in\ker C\), the nonnegative terms in
\[
0=v^\top Cv=\frac1{|\mathcal L|}\sum_{e\in\mathcal L}\mathbb E^e[(v^\top X)^2]+\gamma v^\top Hv
\]
force \(v^\top X=0\) almost surely in each labeled environment. Thus \(v^\top b=0\). In an orthonormal eigenbasis of \(C\), this says that \(b\) has zero coordinates in every zero-eigenvalue direction. Dividing its other coordinates by the corresponding positive eigenvalues produces \(\beta_*\) with \(C\beta_*=b\). The objective difference from its value at \(\beta_*\) is
\[
(\beta-\beta_*)^\top C(\beta-\beta_*)\ge0.
\]
Hence a minimizer exists without an invertibility assumption.

All arguments include \(\gamma=0\), \(p=1\), singleton labeled subsets, and singular or zero \(V\). When \(\gamma V=0\), the admissible matrix set is simply \(\{0\}\), and the same realization and equality apply.

## Obligation Audit

The fixed structural baseline, cross-term cancellation, the two distinct averages, equality \(H=V\), moment realizability, supremum attainment, and minimizer transfer have all been derived. The only linear-algebra background used in the explicit constructions is the stated finite-dimensional spectral theorem, applied to finite real symmetric positive-semidefinite matrices whose hypotheses were verified. There is no unresolved specialized or paper-specific dependency.
