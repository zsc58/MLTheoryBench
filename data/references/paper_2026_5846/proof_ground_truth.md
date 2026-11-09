# Reference Proof

## Proof Structure and Obligations

1. Verify that the population update is defined, fixes the true strength vector, and is homogeneous. Derive its Jacobian and an explicit symmetric similarity; verify the hypotheses of Perron-Frobenius.
2. Differentiate the normalization and prove that it replaces the simple leading eigenvalue by zero.
3. Verify the hypotheses of analytic symmetric perturbation theory, derive the eigenvalue differential identity and its coefficient bounds, and integrate the inequalities.
4. Pass from analytic branches to ordered extreme eigenvalues without assuming that the ordered eigenvalues are analytic at crossings. Prove strict monotonicity, quasi-convexity, and the two optimizer cases.
5. Derive the optimizer interval and both all-parameter bounds for the factor.

All five obligations are closed below. The only external background is the standard-independent spectral theory recorded as theory_025. No population-to-sample approximation or asynchronous result is used.

## Standard Background Used

An irreducible nonnegative matrix with a positive eigenvector has that eigenvector's eigenvalue as its algebraically simple spectral radius. A real symmetric matrix has a real orthonormal eigenbasis. A real-analytic real-symmetric finite matrix family on an open real interval admits real-analytic eigenvalue branches and an orthonormal real-analytic eigenbasis, including at eigenvalue coincidences. These are the relevant independent standard results in theory_025; their application hypotheses are checked below. The quotient estimates used below are derived directly as weighted averages.

## Complete Proof

### 1. Fixed point and explicit population Jacobian

Put p=pi* and write p_i for its coordinates. All comparison counts on nonedges and on the diagonal are zero. Because n>=2 and the graph is connected, each vertex has a neighbor. On every edge both directed expected wins are positive. Thus the numerator and denominator defining every coordinate of F_alpha are positive for every positive input and every alpha>=0, including alpha=0.

Introduce the following private proof notation:
\[
a_{ij}=\frac{m_{ij}}{(p_i+p_j)^2},\qquad
W_{ij}=p_i a_{ij},\qquad
r_i=p_i\sum_j a_{ij},\qquad
c_i=\sum_j p_j a_{ij}.
\]
Here a_ii=W_ii=0, a_ij=a_ji, and r_i,c_i>0. Let
\[
R=\operatorname{diag}(r_i),\quad C=\operatorname{diag}(c_i),\quad
B_\alpha=C+\alpha R,\quad d_i(\alpha)=c_i+\alpha r_i.
\]
The denominator of the update at p is d_i(alpha), while its numerator is
\[
\sum_j m_{ij}\frac{p_i(\alpha p_i+p_j)}{(p_i+p_j)^2}
=p_i d_i(\alpha).
\]
Therefore F_alpha(p)=p. Also F_alpha(tx)=tF_alpha(x) for t>0, so differentiating in t at t=1 gives J_alpha p=p.

For completeness, let N_i(x) and Q_i(x) be the numerator and denominator of the update. For j!=i, quotient differentiation at p, using N_i(p)=p_iQ_i(p), gives
\[
(J_\alpha)_{ij}
=\frac{\partial_jN_i(p)-p_i\partial_jQ_i(p)}{d_i(\alpha)}
=\frac{p_i[(1-\alpha)\bar w_{ij}+\alpha\bar w_{ij}+\bar w_{ji}]}{d_i(\alpha)(p_i+p_j)^2}
=\frac{p_i a_{ij}}{d_i(\alpha)}.
\]
The identity J_alpha p=p then determines the diagonal:
\[
(J_\alpha)_{ii}=1-\frac{\sum_{j\ne i}p_j a_{ij}}{d_i(\alpha)}
=\frac{\alpha r_i}{d_i(\alpha)}.
\]
Consequently,
\[
J_\alpha=B_\alpha^{-1}(W+\alpha R).
\]
This recovers the source's population matrix identity directly from the public update.

The matrix J_alpha is nonnegative, with a positive off-diagonal entry in both directions of every comparison edge. Connectedness therefore makes it irreducible. Since p>0 and J_alpha p=p, Perron-Frobenius implies that 1 is its algebraically simple spectral radius.

Define
\[
D_\alpha=\operatorname{diag}\!\left(\sqrt{p_i/d_i(\alpha)}\right),\qquad
H_\alpha=D_\alpha^{-1}J_\alpha D_\alpha.
\]
For i!=j,
\[
(H_\alpha)_{ij}=a_{ij}\sqrt{\frac{p_i p_j}{d_i(\alpha)d_j(\alpha)}},
\]
which is symmetric in i,j. Thus H_alpha is real symmetric, and J_alpha is diagonalizable with real eigenvalues. Together with the simple Perron eigenvalue, this proves
\[
\lambda_n(\alpha)\le\cdots\le\lambda_2(\alpha)<\lambda_1(\alpha)=1.
\]
In particular every nonleading eigenvalue is strictly below 1, even when an eigenvalue equals -1 at alpha=0.

### 2. Normalization and the local factor

At the product-one vector p, differentiating S gives
\[
DS(p)=I-\frac1n p(p^{\circ-1})^T=:P.
\]
This projection has kernel span{p} and image
\[
\mathcal T=\{h:(p^{\circ-1})^Th=0\}.
\]
Since F_alpha(p)=p, the chain rule gives DT_alpha(p)=PJ_alpha. The identity J_alpha p=p implies
\[
PJ_\alpha P=PJ_\alpha,
\]
because the image of I-P is contained in span{p}.

Choose an eigenbasis x_1=p,x_2,...,x_n of J_alpha, counting multiplicities. Then
\[
PJ_\alpha p=0,\qquad
PJ_\alpha(Px_i)=PJ_\alpha x_i=\lambda_i Px_i\quad(i\ge2).
\]
The vectors p,Px_2,...,Px_n are independent: a dependence would give a linear combination of x_2,...,x_n in span{p}, contradicting the original eigenbasis. Hence the normalized spectrum is exactly 0,lambda_2,...,lambda_n. Since n>=2, the nonleading spectrum is nonempty, and its largest absolute value is
\[
\rho_{\rm sync}(\alpha)=\max\{\lambda_2(\alpha),-\lambda_n(\alpha)\}.
\]
This uses the public definition of the local factor as a spectral radius; no additional claim about convergence of every trajectory is needed.

### 3. Analytic branches and differential control

Choose epsilon>0 smaller than min_i c_i/r_i. For alpha in the open interval (-epsilon,infinity), every d_i(alpha)>0. The displayed formulas for D_alpha and H_alpha therefore define real-analytic matrix families on that interval, and H_alpha remains real symmetric there. Analytic symmetric perturbation theory applies and supplies real-analytic eigenvalues psi_i and orthonormal analytic eigenvectors z_i.

On [0,infinity), label the simple leading branch psi_1 identically 1. The remaining branches cannot meet 1 because it is simple everywhere. They may be indexed initially so that psi_i(0)=lambda_i(0), although their ordering may subsequently change.

For any branch set
\[
v_i=D_\alpha z_i,\qquad u_i=D_\alpha^{-1}z_i.
\]
Then J_alpha v_i=psi_i v_i, u_i^T J_alpha=psi_i u_i^T, and u_i^T v_i=1. Differentiating the right eigenvalue equation and multiplying by u_i^T cancels the eigenvector derivative and yields
\[
\psi_i'=\frac{u_i^T J_\alpha'v_i}{u_i^Tv_i}.
\]
This calculation is valid at repeated eigenvalues because the eigenpairs have been chosen analytically.

Differentiating the explicit population matrix identity gives
\[
J_\alpha'=-B_\alpha^{-1}R J_\alpha+B_\alpha^{-1}R
=B_\alpha^{-1}R(I-J_\alpha).
\]
Also u_i=D_alpha^{-2}v_i=B_alpha diag(p)^{-1}v_i. Hence
\[
\psi_i'=(1-\psi_i)
\frac{v_i^T\operatorname{diag}(p)^{-1}Rv_i}
{v_i^T\operatorname{diag}(p)^{-1}(C+\alpha R)v_i}
=\frac{1-\psi_i}{\alpha+\gamma_i(\alpha)},
\]
where
\[
\gamma_i(\alpha)=
\frac{v_i^T\operatorname{diag}(p)^{-1}Cv_i}
{v_i^T\operatorname{diag}(p)^{-1}Rv_i}.
\]
The denominator is positive because R and diag(p) are positive diagonal matrices and v_i is nonzero.

For each vertex j,
\[
\frac{c_j}{r_j}
=\frac{\sum_\ell a_{j\ell}(p_\ell/p_j)}{\sum_\ell a_{j\ell}}.
\]
This is a weighted average of adjacent strength ratios. Every such ratio belongs to [kappa^{-1},kappa]. Moreover gamma_i is a weighted average of c_j/r_j with nonnegative weights (r_j/p_j)(v_i)_j^2, whose sum is positive. Therefore
\[
\kappa^{-1}\le\gamma_i(\alpha)\le\kappa.
\]
For i>=2, psi_i<1, so
\[
\frac{1-\psi_i}{\alpha+\kappa}
\le\psi_i'
\le\frac{1-\psi_i}{\alpha+\kappa^{-1}},
\]
and psi_i'>0.

Let y_i=1-psi_i>0. Integrating the last inequalities from 0 to alpha gives
\[
\log(1+\alpha/\kappa)
\le\log\frac{y_i(0)}{y_i(\alpha)}
\le\log(1+\kappa\alpha).
\]
Thus
\[
\frac{y_i(0)}{1+\kappa\alpha}
\le y_i(\alpha)
\le\frac{y_i(0)}{1+\kappa^{-1}\alpha},
\]
which is equivalent to
\[
\frac{\psi_i(0)+\kappa^{-1}\alpha}{1+\kappa^{-1}\alpha}
\le\psi_i(\alpha)
\le\frac{\psi_i(0)+\kappa\alpha}{1+\kappa\alpha}.
\]
The upper bound on y_i tends to zero, proving psi_i(alpha) increases to 1. The leading branch is identically 1 and satisfies the corresponding non-strict identities without division by 1-psi_1.

### 4. Ordered extremes, quasi-convexity, and the optimizer

Define
\[
f(\alpha)=\lambda_2(\alpha)=\max_{i\ge2}\psi_i(\alpha),\qquad
h(\alpha)=\lambda_n(\alpha)=\min_{i\ge2}\psi_i(\alpha).
\]
These functions are continuous. Both are strictly increasing: for b>a, every difference psi_i(b)-psi_i(a) is positive, and the minimum of these finitely many differences is positive; both the maximum and minimum therefore increase by at least that amount. Since all finitely many branches tend to 1, so do f and h. No analyticity of f or h at a crossing is assumed.

Set g=-h. Then rho_sync=max{f,g}, where f is strictly increasing and g strictly decreasing. Every sublevel set of this maximum is the intersection of a sublevel set of f and a sublevel set of g, each an interval in [0,infinity). Hence rho_sync is quasi-convex.

The continuous function
\[
s(\alpha)=\frac{f(\alpha)+h(\alpha)}2
\]
is strictly increasing, starts at s_0, and tends to 1. Also f>=g exactly when s>=0.

If s_0>=0, then s(alpha)>=0 for all alpha>=0. Therefore rho_sync=f is strictly increasing and has the unique minimizer alpha_opt=0. This includes s_0=0.

If s_0<0, continuity, strict increase, and the limit 1 give a unique alpha_opt>0 with s(alpha_opt)=0. Equivalently,
\[
\lambda_2(\alpha_{\rm opt})=-\lambda_n(\alpha_{\rm opt}).
\]
Before this crossing rho_sync=g is strictly decreasing; after it rho_sync=f is strictly increasing. The crossing is thus the unique global minimizer, including when its value is zero.

### 5. Optimizer and factor bounds

For compact notation define, only within this proof,
\[
L_\alpha(t)=\frac{t+\kappa^{-1}\alpha}{1+\kappa^{-1}\alpha},\qquad
U_\alpha(t)=\frac{t+\kappa\alpha}{1+\kappa\alpha}.
\]
Both are increasing affine functions of t. Taking maxima and minima in the individual branch inequalities therefore gives, for r=2 and r=n,
\[
L_\alpha(\lambda_r(0))\le\lambda_r(\alpha)\le U_\alpha(\lambda_r(0)).
\]
Averaging the two extreme inequalities yields
\[
\frac{s_0+\kappa^{-1}\alpha}{1+\kappa^{-1}\alpha}
\le s(\alpha)\le
\frac{s_0+\kappa\alpha}{1+\kappa\alpha}.
\]
When s_0<0, substituting s(alpha_opt)=0 and using positive denominators gives
\[
\kappa^{-1}|s_0|\le\alpha_{\rm opt}\le\kappa|s_0|.
\]
For every alpha>=0, the same extreme bounds imply
\[
\max\{L_\alpha(\lambda_2(0)),-U_\alpha(\lambda_n(0))\}
\le\rho_{\rm sync}(\alpha)
\le
\max\{U_\alpha(\lambda_2(0)),-L_\alpha(\lambda_n(0))\}.
\]
Expanding these expressions proves exactly the final displayed inequalities in the public task. The proof does not require either term in either maximum to be positive individually.

For completeness, the source's additional optimal-factor estimates follow privately from the same argument, but are not additional public obligations. If s_0>=0, rho_sync(0)=lambda_2(0), so the bounds reduce to L_alpha(rho_sync(0))<=rho_sync(alpha)<=U_alpha(rho_sync(0)). If s_0<0, put b=|s_0| and r_0=rho_sync(0)=-lambda_n(0). Monotonicity of lambda_n and b/kappa<=alpha_opt<=kappa b give
\[
\rho_{\rm sync}(\alpha_{\rm opt})
\ge-\lambda_n(\kappa b)
\ge\frac{r_0-\kappa^2b}{1+\kappa^2b},
\]
and
\[
\rho_{\rm sync}(\alpha_{\rm opt})
\le-\lambda_n(b/\kappa)
\le\frac{r_0-\kappa^{-2}b}{1+\kappa^{-2}b}.
\]
These optional consequences are not needed to finish the requested proof.
