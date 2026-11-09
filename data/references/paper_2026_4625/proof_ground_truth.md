# Reference Proof

## Audited Contract and Proof Obligations

The smoothness constants are uniform over all locations and all real coefficient vectors, not merely over an algorithmic trajectory. The objective family includes augmented sample counts. These quantifiers are essential: they make the literal hypothesis substantially stronger than bounded-weight smoothness.

The obligations are: derive the location Hessian and its splitting-matrix comparison; handle the augmented-displacement normalization in Taylor's theorem; establish the claimed split and gradient accounting; and justify termination and the total-iteration claim without imposing an unstated lower bound on the splitting step. An elementary consequence of the full source assumption closes all of them. No external theorem or specialized method is needed.

## 1. Derivatives and Hessian Comparison — steps 001 and 004

Fix a representation and write
\[
r=a-\sum_iw_i g(z_i),\qquad J_i=w_iDg(z_i).
\]
Differentiating with weights held fixed gives
\[
\nabla_{z_i}F=-2J_i^\top r,
\qquad
H_{ii}=2J_i^\top J_i+S_i,
\qquad
H_{ij}=2J_i^\top J_j\quad(i\ne j),
\]
where \(H=\nabla_z^2F\). Consequently, for any block vector \(u=(u_i)_i\),
\[
u^\top Hu
=2\left\|\sum_iJ_i u_i\right\|^2+\sum_i u_i^\top S_i u_i.
\]
If \(\kappa=\min_i\lambda_{\min}(S_i)\), the right side is at least \(\kappa\sum_i\|u_i\|^2\). Taking the minimum over unit vectors yields
\[
\lambda_{\min}(H)\ge\min_i\lambda_{\min}(S_i).
\]
These formulas also hold for zero or negative weights; no division by a weight is involved.

## 2. Consequence of the Full Smoothness Quantifier — step 006

Consider the two-sample objective at locations \((x,x)\) and weights \((t,t)\). Its off-diagonal Hessian block is
\[
H_{12}=2t^2Dg(x)^\top Dg(x).
\]
For any unit vector \(u\in\mathbb R^d\), the block vectors \(e=(u,0)\) and \(f=(0,u)\) are unit vectors. The global Hessian bound therefore gives
\[
2t^2\|Dg(x)u\|^2=e^\top Hf\le\|H\|\le\ell.
\]
The same \(\ell\) works for every positive \(t\). Letting \(t\) tend to infinity gives \(Dg(x)u=0\). Since \(x\) and \(u\) were arbitrary, \(Dg\) vanishes everywhere.

For any two points, restrict each component of \(g\) to the line segment joining them. Its derivative along that segment is zero, so the one-dimensional mean-value theorem shows that its endpoint values agree. Thus \(g\equiv c\) for some \(c\in\mathbb R^m\).

It follows for every representation that
\[
F(z,w)=\left\|a-\left(\sum_iw_i\right)c\right\|^2,
\qquad
\nabla_zF=0,
\qquad
\nabla_z^2F=0,
\qquad
\nabla_z^3F=0,
\qquad
S_i=0.
\]
In particular, the initial representation already satisfies both stationarity inequalities and the algorithm's stopping test. It performs no gradient updates and no splits. Therefore the requested bounds hold, including when \(F_0=0\), and indeed hold with both iteration counts equal to zero for every admissible choice of step sizes.

This argument uses the literal source hypothesis. It must not be replaced by an assumption that the derivative bounds hold only for the current weights. The theorem under that weaker assumption would be a different task.

## 3. Balanced-Splitting Expansion and Normalization — step 002

For completeness, retain the source's splitting calculation and check its normalization explicitly. For a nonzero parent weight, write \(\alpha_{ij}=w_i^{[j]}/w_i>0\). Suppose \(\sum_j\alpha_{ij}=1\) and \(\sum_jw_i^{[j]}\delta_i^{[j]}=0\). Let \(G\) denote the augmented objective, let \(y_0\) be the coincident-offspring locations, and let \(\delta\) be the concatenation of all offspring displacements.

At coincidence, weight preservation gives \(G(y_0)=F(z,w)\). Its directional first derivative is
\[
DG(y_0)[\delta]
=-2r^\top\sum_{i,j}w_i^{[j]}Dg(z_i)\delta_i^{[j]}=0.
\]
Its directional second derivative is
\[
D^2G(y_0)[\delta,\delta]
=2\left\|\sum_{i,j}w_i^{[j]}Dg(z_i)\delta_i^{[j]}\right\|^2
+\sum_{i,j}\alpha_{ij}(\delta_i^{[j]})^\top S_i\delta_i^{[j]}.
\]
The squared-norm term vanishes by the same balance condition. Ordinary Taylor control would give
\[
G(y_0+\eta\delta)
=F+\frac{\eta^2}{2}\sum_{i,j}\alpha_{ij}(\delta_i^{[j]})^\top S_i\delta_i^{[j]}+R,
\qquad
|R|\le\frac{\rho\eta^3}{6}\|\delta\|^3.
\]
The hypotheses \(\|\delta_i^{[j]}\|\le1\) do not imply \(\|\delta\|\le1\). For a single binary split with directions \(v,-v\), \(\|\delta\|=\sqrt2\). Thus one must not obtain the smaller displayed remainder in the old reference merely by dropping this factor.

Under the actual contract, however, Section 2 proves that \(G\) is independent of all its locations. Its actual remainder is exactly zero, as is every splitting quadratic form. Hence the source's stated upper estimate with \(\rho\eta^3/6\) is valid here, for the explicit reason just established. This closes the remainder obligation without changing the step-size range or introducing a new norm convention. A zero-weight sample has \(S_i=0\), cannot trigger a split, and needs no ratio notation.

## 4. Negative-Curvature Choice and Split Accounting — step 003

The algebra underlying the second-order choice is also valid. If a symmetric matrix \(S\) has \(\kappa=\lambda_{\min}(S)<0\), then for \(\|q\|\le1\),
\[
q^\top Sq\ge\kappa\|q\|^2\ge\kappa.
\]
A positive weighted average of these quadratic forms is therefore at least \(\kappa\). Equal weights on the two opposite unit minimum-eigenvectors attain equality and satisfy balance. If \(S\succeq0\), the quadratic coefficient is nonnegative. This last observation concerns the second-order model; it is not, by itself, a finite-step nondecrease theorem in a zero-curvature direction.

For the binary choice, the upper estimate justified in Section 3 is
\[
F_{\mathrm{split}}\le F+\frac{\eta^2}{2}\lambda_{\min}(S_i)+\frac{\rho\eta^3}{6}.
\]
Conditionally on \(\lambda_{\min}(S_i)<-\epsilon_H\), the allowed step size gives
\[
F-F_{\mathrm{split}}
\ge\frac{\epsilon_H\eta^2}{2}-\frac{\rho\eta^3}{6}
\ge\frac{\epsilon_H\eta^2}{4},
\]
because \(\rho\eta/6\le\sqrt{\rho\epsilon}/4\). Nonnegativity of the objective would then yield
\[
N_s\le\frac{4F_0}{\epsilon_H\eta^2}
=\frac{4F_0}{\sqrt\rho\,\eta^2}\epsilon^{-1/2}.
\]
Under the restored assumptions the negative-curvature antecedent never occurs: every \(S_i=0\), and actually \(N_s=0\). The conditional calculation is retained to identify exactly what the original descent accounting uses.

## 5. Gradient Accounting, Termination, and Total Iterations — step 005

For fixed weights, the Hessian bound holds on the entire gradient-update segment. Applying the one-dimensional second-order Taylor bound along that segment gives
\[
F(z-\eta_g\nabla F,w)
\le F(z,w)-\eta_g\left(1-\frac{\ell\eta_g}{2}\right)\|\nabla F\|^2
\le F(z,w)-\frac{\eta_g}{2}\|\nabla F\|^2.
\]
Thus an update taken when \(\|\nabla F\|>\epsilon\) would decrease the objective by at least \(\eta_g\epsilon^2/2\), and nonnegativity gives
\[
N_g\le\frac{2F_0}{\eta_g\epsilon^2}.
\]
Together with the split estimate, the generic accounting is
\[
N_g+N_s\le\frac{2F_0}{\eta_g\epsilon^2}
+\frac{4F_0}{\sqrt\rho\,\eta^2\sqrt\epsilon}.
\]
This expression alone does not imply a bound uniform in arbitrarily small epsilon-dependent choices of \(\eta\). In particular, an upper bound on \(\eta\) is not a lower bound. We do not add such a lower bound or discard the split term. Section 2 already establishes the stronger actual conclusion \(N_g+N_s=0\), which proves the stated total complexity under the complete source contract.

At any stopping point the algorithm has \(\|\nabla_zF\|\le\epsilon\) and all splitting eigenvalues at least \(-\epsilon_H\). The Hessian comparison in Section 1 yields
\[
\lambda_{\min}(\nabla_z^2F)\ge\min_i\lambda_{\min}(S_i)\ge-\epsilon_H=-\sqrt{\rho\epsilon}.
\]
The inequality direction is a lower bound. In this task these conditions hold already at initialization. All theorem-critical obligations are closed.
