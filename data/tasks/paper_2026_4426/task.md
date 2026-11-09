# Problem

## Setup

You observe n aligned samples from a response time series and candidate driver series. Let X\in\mathbb R^{n\times d_R} contain lagged covariates excluding one tested driver, let W\in\mathbb R^{n\times d_A} contain that driver's lags, and let Z=[W,X]\in\mathbb R^{n\times d_U}, where d_U=d_R+d_A. Assume d_R,d_A are positive integers, n>d_U, and the columns of X and W have been mean-centered. The response y\in\mathbb R^n is mean-centered and normalized so that y^Ty=1. Write
\[
H=I_n-\mathbf1\mathbf1^\top/n.
\]

All regressions below are ordinary least-squares regressions. Their fitted vectors are defined by orthogonal projection onto the indicated regression space; coefficients need not be unique. An intercept is included by adjoining the column \mathbf1, or equivalently by centering the response and feature columns and then restoring the response mean.

### Full-kernel regressions

For T\in\{X,Z\}, choose a real positive-definite kernel on its input space, let K_T=(k(t_i,t_j)), and set \bar K_T=HK_TH. Write
\[
\bar K_T=A_T\Lambda_TA_T^\top,
\]
retaining exactly its positive eigenvalues, with A_T^TA_T=I and diagonal \Lambda_T\succ0. Empty matrices are permitted if there are no positive eigenvalues; their regression space is \{0\}.

KGC regresses Hy on the columns of H\bar K_T. KPCR regresses Hy on the centered columns of
\[
F_T=\bar K_TA_T\Lambda_T^{-1/2}.
\]

### Normalized Gaussian activation regressions

Fix \sigma>0. Separately for each T\in\{X,W\}, choose m_T\ge1 k-means inducing points
\[
J_T=(j_{T,1},\ldots,j_{T,m_T})
\]
in the same Euclidean input space as the rows of T. Use
\[
k_\sigma(u,v)=\exp\!\left(-\frac{\|u-v\|^2}{2\sigma^2}\right),
\qquad
r_T(u)=\sum_{a=1}^{m_T}k_\sigma(u,j_{T,a}).
\]
Assume the inducing Gram matrix
\[
G_T=(k_\sigma(j_{T,a},j_{T,b}))_{a,b=1}^{m_T}
\]
is positive definite. Define the normalized Gaussian activation matrix by
\[
(B_T)_{ia}=\frac{k_\sigma(t_i,j_{T,a})}{r_T(t_i)}.
\]
The restricted normalized-GRBF regression uses the design [\mathbf1,B_X], and its unrestricted regression uses [\mathbf1,B_X,B_W].

For each block T, define the kernel
\[
\widetilde k_T(u,v)=\frac{k_\sigma(u,v)}{r_T(u)r_T(v)}.
\]
Let \widetilde K_{TJ_T} and \widetilde K_{J_TJ_T} be its data-inducing and inducing-inducing Gram matrices. Define the Nyström feature matrix
\[
N_T=\widetilde K_{TJ_T}\widetilde K_{J_TJ_T}^{-1/2},
\]
where the inverse square root is the symmetric positive-definite inverse square root. Let V_T have orthonormal columns consisting of all positive-eigenvalue eigenvectors of (HN_T)^T(HN_T), and put
\[
S_T=HN_TV_T.
\]
If there are no positive eigenvalues, S_T has no columns. The restricted Nyström-PCR regression uses [\mathbf1,S_X], and its unrestricted regression uses [\mathbf1,S_X,S_W]. No additional principal-component truncation is performed.

### Residual comparison

For either of the two restricted/unrestricted representations in the preceding subsection, let P_R,P_U denote the orthogonal projectors onto its full regression spaces, including the intercept. Define
\[
p_R=\operatorname{rank}(P_R),\quad
p_U=\operatorname{rank}(P_U),\quad q=p_U-p_R,
\]
\[
\operatorname{RSS}_R=\|(I_n-P_R)y\|^2,\qquad
\operatorname{RSS}_U=\|(I_n-P_U)y\|^2.
\]
The in-sample predictive-error difference is \operatorname{RSS}_R-\operatorname{RSS}_U. When q>0, n-p_U>0, and \operatorname{RSS}_U>0, define the usual least-squares comparison ratio
\[
F=\frac{(\operatorname{RSS}_R-\operatorname{RSS}_U)/q}
{\operatorname{RSS}_U/(n-p_U)}.
\]

## Task

Prove the following integrated theorem.

1. For T=X and T=Z, the centered KGC regression projector equals the KPCR projector formed from all positive-eigenvalue components of \bar K_T.
2. The normalized-GRBF restricted and additive unrestricted regressions have exactly the same fitted-space projectors as their respective Nyström-PCR representations defined above. Consequently, they have identical fitted values, residual vectors, residual sums of squares, and in-sample predictive-error differences. Their F ratios are identical whenever the stated domain conditions hold.
