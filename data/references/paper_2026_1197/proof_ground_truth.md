# Reference Proof

## Contract and Obligations

The feature vectors are iid with independent mean-zero 1-subgaussian coordinates in the covariance eigenbasis. The covariance is Sigma=V Lambda V^T. Consequently, every coordinate corresponding to a positive eigenvalue has variance one; coordinates with zero eigenvalue contribute nothing to the Gram matrix. Labels are arbitrary subject to their displayed bounds. The argument below is deterministic on an event depending only on X, so it does not require label-feature independence. All universal constants are chosen before n, d, the spectrum, labels, step size, and initialization.

The theorem-critical obligations are: a simultaneous Gram and inverse-Gram event; first-step sign and quantitative bounds; an explicit invariant for all subsequent times; parameter convergence to the specified projection; existence, uniqueness, and KKT characterization of the comparison optimizer; two-sided prediction discrepancies and their conversion to both parameter bounds; and empty-block cases. Each is closed below. No paper-specific result is used as an unexplained black box.

## 1. Concentration and Constant Choices

Use the audited standard-independent Gram concentration statement supplied in the source: for independent standardized mean-zero 1-subgaussian coordinates and iid rows, with G=XX^T and L=||lambda||_1,

Pr(||G-LI||_op >= tau) <= 2*9^n exp(-a min{tau^2/||lambda||_2^2, tau/||lambda||_infty})

for a universal a>0 and every tau>0. Its hypotheses hold on all positive-eigenvalue coordinates by the sampling model and covariance normalization. Zero-eigenvalue coordinates can be omitted.

Choose a universal A>=1 so that aA-log(9)>=1. With tau=A max{||lambda||_2 sqrt(n), ||lambda||_infty n}, both quantities inside the minimum are at least An. Thus, on a single event E of probability at least 1-2e^{-n},

G=LI+H,  ||H||_op<=L delta,

delta=A max{sqrt(n/d_2), n/d_infty} <= A y_min/(C_0 sqrt(n)y_max).

Choose C_g=2, C_y=2, and any fixed C_eta>=1, for example C_eta=2. Choose C_alpha and C_0 sufficiently large in accordance with the repaired public hierarchy, and choose C_lb>=4C_alpha^2 as well as its other displayed requirement. A sufficiently large universal K makes all these choices possible and ensures delta<=1/2. On E,

L/C_g <= lambda_min(G) <= lambda_max(G) <= C_g L,

||G^{-1}||_op<=C_g/L,

||LG^{-1}-I||_op = ||G^{-1}(LI-G)||_op <= C_g delta.

These estimates also give the same spectral interval for every nonempty principal Gram block. For disjoint row blocks,

||X_+X_-^T||_op <= ||X_+||_op ||X_-||_op <= C_gL.

This elementary estimate replaces the source's addition of differently sized principal blocks. All further statements take place on E; there is no union over iterations, label subsets, or initializations.

For explicit constant bookkeeping it is enough to require, in addition to the choices just made,

C_alpha>=4C_eta C_g,

C_alpha>=6C_g+3/C_g,

A C_alpha^2/C_0<=1/2,

A(C_alpha+C_g)/C_0<=min{1/(2C_alpha),1/C_g}.

The repaired public hierarchy implies these inequalities for sufficiently large K. The remaining elementary first-step estimates below are also implied by that same hierarchy.

## 2. First Update

Set beta^t=Xw^t and alpha^t=G^{-1}beta^t. Every iterate lies in the row span of X, since the initialization and all updates do. Therefore w^t=X^T alpha^t. The update equations are

beta^{t+1}=beta^t-eta G D_t(beta^t-y),

alpha^{t+1}=alpha^t-eta D_t(beta^t-y).

The gated replacement of h_w(X) by beta is exact, including at zero. Let q=eta L, so 1/(C_eta C_g)<=q<=1/C_g. Since beta^0=epsilon>0, every initial gate is one, and

alpha^1=G^{-1}epsilon+eta(y-epsilon),

beta^1=(1-q)epsilon+qy+eta H(y-epsilon).

Write M=sqrt(n)y_max and m=y_min. We have ||epsilon||<=sqrt(n)m/C_alpha and ||y-epsilon||<=2M.

For i in S_+,

beta_i^1 >= q[m-delta||y-epsilon||] >= q m(1-2A/C_0)>0.

For j in S_-, use G^{-1}=L^{-1}I+(G^{-1}-L^{-1}I) to obtain

alpha_j^1 <= -eta m+epsilon_j/L+C_g delta||epsilon||/L

<= (m/L)[-1/(C_eta C_g)+(1+C_gA/C_0)/C_alpha]

<= -m/(2C_eta C_gL) <= -m/(C_alpha L).

The opposite estimate, dropping the nonnegative epsilon_j/L term, is

alpha_j^1 >= -eta(y_max+m/C_alpha)-C_g delta||epsilon||/L >= -3y_max/(C_gL).

For positive-label residuals, the absolute-value triangle inequality gives

|beta_i^1-y_i| <= |(1-q)(epsilon_i-y_i)|+q delta||epsilon-y||

<= y_i+2A m/(C_gC_0) <= 2y_i.

Hence ||beta_+^1-y_+||<=C_y||y_+||. This supplies both sides needed for the source's residual-square estimate, without assuming a sign for its deviation.

Also,

||alpha^1|| <= eta(||y||+||epsilon||)+||G^{-1}||||epsilon||

<= [(1+1/C_alpha)/C_g+C_g/C_alpha] M/L <= C_alpha M/L.

Finally, for every j in S_-,

beta_j^1=L alpha_j^1+(H alpha^1)_j

<= -m/C_alpha+L delta||alpha^1||

<= -m/C_alpha+A C_alpha m/C_0 <= -m/(2C_alpha)<0.

Thus the six conditions listed in the next section hold at time one. If a block is empty, its coordinate and residual statements are vacuous.

## 3. Explicit Invariant

For every t>=1 maintain:

1. beta_i^t>0 for i in S_+.
2. -3y_max/(C_gL)<=alpha_j^t<=-m/(C_alpha L) for j in S_-.
3. ||beta_+^t-y_+||<=C_y||y_+||.
4. ||alpha^t||<=C_alpha M/L.
5. beta_j^t<=0 for j in S_-.
6. h_{w^t}(x_i)=beta_i^t on S_+ and zero on S_-.

Suppose they hold at time t. Let r_+=beta_+^t-y_+. The active residual vector is r_+ padded with zeros on S_-. For i in S_+,

beta_i^{t+1}=(1-q)beta_i^t+qy_i-eta(H D_t(beta^t-y))_i

>= q[m-delta C_y M] >= q m(1-A C_y/C_0)>0.

Condition 5 makes every negative-label gate zero, so alpha_-^{t+1}=alpha_-^t, preserving condition 2. Moreover,

beta_+^{t+1}-y_+=(I-eta G_{++})(beta_+^t-y_+).

For a nonempty positive block, the eigenvalues of eta G_{++} lie in (0,1], so this map has operator norm at most one. Condition 3 is preserved. For an empty positive block it is vacuous.

To bound the full dual norm, first ||alpha_-^{t+1}||<=3M/(C_gL). When S_+ is nonempty,

alpha_+^{t+1}=G_{++}^{-1}(beta_+^{t+1}-G_{+-}alpha_-^{t+1}).

Using ||beta_+^{t+1}||<=3M, the principal-block inverse bound, and ||G_{+-}||<=C_gL gives

||alpha_+^{t+1}|| <= (C_g/L)(3M+3M)=6C_gM/L.

Therefore ||alpha^{t+1}||<=(6C_g+3/C_g)M/L<=C_alpha M/L. When S_+ is empty, all coordinates freeze and the already established norm bound persists directly.

For j in S_-, now use conditions 2 and 4 at t+1:

beta_j^{t+1} <= -m/C_alpha+L delta||alpha^{t+1}|| <= -m/(2C_alpha)<0.

This preserves condition 5, and conditions 1 and 5 imply condition 6. Induction proves stabilization for every t>=1 on the same event E.

## 4. Parameter Convergence and Projection

The stabilized update is

w^{t+1}=w^t-eta X_+^T(X_+w^t-y_+).

For S_+ nonempty, set B=X_+ and F=BB^T. Full row rank of X implies full row rank of B. The residual is

Bw^t-y_+=(I-eta F)^{t-1}(Bw^1-y_+),

which tends to zero because every eigenvalue of I-eta F belongs to [0,1). Summing the update, or diagonalizing F, gives

w^infty=w^1+B^T F^{-1}(y_+-Bw^1).

This vector fits y_+, and its displacement from w^1 lies in range(B^T), orthogonal to ker(B). Hence it is the unique Euclidean projection of w^1 onto {w:Bw=y_+}. This explicitly proves the standard linear-GD projection fact used by the source.

If S_+ is empty, the stabilized update is zero, w^infty=w^1, and the projection onto the whole space is w^1. In either case, continuity and the established inactive inequalities give X_-w^infty<=0. Row-span membership also persists at the limit.

## 5. Comparison Optimizer and KKT Representation

The map w -> Xw is surjective. In particular, assigning prediction y_i on S_+ and prediction -1 on S_- gives a feasible vector, strictly satisfying every inequality that is present. The feasible set is closed and convex; the squared norm is coercive and strictly convex. Thus w^star exists and is unique. The strictly feasible point verifies the equality-constrained Slater condition when inequalities are present.

The KKT conditions therefore give multipliers l_i in R for i in S_+ and mu_j>=0 for j in S_- such that

w^star=-sum_{i in S_+} l_i x_i-sum_{j in S_-} mu_j x_j,

mu_j(x_j^T w^star)=0,

along with primal feasibility. Define T={j in S_-:mu_j>0}, U=S_-\T, and S=S_+ union T. Then beta_j^star=0 on T and the row-span coefficient alpha_j^star is zero on U. On S, w^star is in range(X_S^T) and satisfies X_Sw^star=tilde y_S, where tilde y is y on S_+ and zero on T. Consequently,

w^star=X_S^T(G_{SS})^{-1}tilde y_S,

alpha_S^star=(G_{SS})^{-1}tilde y_S, alpha_U^star=0,

||alpha^star||<=C_g M/L.

If S is empty, the representation means w^star=0 and alpha^star=0, without invoking an empty-block eigenvalue or inverse. This also follows directly when S_+ is empty, because zero is feasible and minimizes the norm.

## 6. Both Distance Bounds

Let v=w^infty-w^star and d=Xv. Positive-label coordinates of d vanish. Negative-label dual coordinates of GD have frozen at alpha_j^1. For j in T,

d_j=L alpha_j^1+(H alpha^infty)_j,

because beta_j^star=0. For j in U,

d_j=L alpha_j^1+(H(alpha^infty-alpha^star))_j,

because alpha_j^star=0. In both cases, the error in this expression is bounded in absolute value by

L delta(||alpha^infty||+||alpha^star||) <= A(C_alpha+C_g)m/C_0.

The invariant bounds pass to the limit. Therefore, for every j in S_-,

-4y_max/C_g <= d_j <= -m/(2C_alpha).

The first inequality uses the lower frozen-dual bound and A(C_alpha+C_g)/C_0<=1/C_g. The second uses the upper frozen-dual bound and A(C_alpha+C_g)/C_0<=1/(2C_alpha). These two-sided estimates justify squaring the discrepancies regardless of which KKT case occurs. Summing gives

n_- m^2/(4C_alpha^2) <= ||Xv||^2 <= 16 n_- y_max^2/C_g^2.

Both w^infty and w^star lie in range(X^T). On that space, the nonzero singular values of X have squares equal to the eigenvalues of G. Thus

(L/C_g)||v||^2 <= ||Xv||^2 <= C_gL||v||^2.

Combining these estimates and C_lb>=4C_alpha^2 yields

n_- y_min^2/(C_lb C_gL) <= ||w^infty-w^star||^2 <= 16 n_- y_max^2/(C_gL).

Taking square roots gives the target. If n_-=0, d=0 everywhere and row-span membership implies v=0, so both bounds hold exactly. If S_+ is empty, the KKT and dynamics cases above still give the same estimates.

All conclusions hold on E, whose probability is at least 1-2e^{-n}; equivalently the asserted form holds for a universal c>0. Every theorem-critical obligation has been explicitly closed.
