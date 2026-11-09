# Reference Proof

Let \(\mathcal R\) denote either the casewise or cellwise regime. Write \(\widehat\mu^{(k)}\) and \(\widehat\Sigma^{(k)}\) for the selected exact minimizer evaluated on a contaminated data set. All constants used for robustness below may depend on the clean data and on the fixed problem parameters, but not on the magnitudes of replacement values. The arguments apply to every exact minimizer, so they do not require a particular tie-breaking rule.

## Matrix facts and exact minimizers

For a symmetric positive-definite matrix \(S\) and a nonempty principal submatrix \(S_{JJ}\), the Rayleigh quotient gives
\[
\lambda_{\min}(S)\le\lambda_{\min}(S_{JJ})
\le\lambda_{\max}(S_{JJ})\le\lambda_{\max}(S).
\]
Indeed, a vector on \(J\) can be extended by zeros to a full vector with the same norm and quadratic form. In particular, if \(aI\preceq S\preceq CI\), then
\[
aI\preceq S_{JJ}\preceq CI,
\qquad C^{-1}I\preceq S_{JJ}^{-1}\preceq a^{-1}I.
\]
For positive-semidefinite \(S\), its nonnegative eigenvalues also give
\[
\lambda_{\max}(S)\le\operatorname{tr}(S)
\le q\max_j S_{jj}.
\]
These facts apply to every fitted covariance because its eigenvalues are at least the stipulated positive floor.

The estimators are well defined on every finite input. Here is an attainment argument, which also addresses the zero-correlation part of the normalization. Fix any finite input, not necessarily a contamination below the threshold. A feasible choice of row weights or masks, finite means, and diagonal covariances \(c_kI_q\) with \(c_k\ge a_k\) has a finite objective \(M_x\). All quadratic and penalty terms are nonnegative. A full log determinant is at least \(q\log a_k\); a partial log determinant is at least \(|J|\log a_k\). Thus the objectives are bounded below.

On the sublevel set with objective at most \(M_x\), a diverging covariance eigenvalue would force a diverging full log determinant in the casewise regime. In the cellwise regime, a largest diagonal entry belongs to a retained pattern because each column retains at least one cell; the corresponding partial log determinant would diverge. All remaining log determinants have uniform finite lower bounds. Consequently all covariance eigenvalues are bounded above on this sublevel set. For fixed finite input data, an unbounded mean would then force an unbounded retained quadratic term: there is a retained row in the casewise regime, and at least one retained cell in every coordinate in the cellwise regime. The inverse principal-submatrix bounds above justify the latter conclusion coordinate by coordinate. Hence the means are bounded as well.

There are finitely many feasible row-weight or mask configurations. For a fixed configuration, the eigenvalue-floor covariance domain is closed, and the likelihood is continuous there. The normalized penalty is lower semicontinuous. To see this, \(\theta_{ij}\) is a continuous function of the covariances. Where \(\theta_{ij}>0\), each \(\gamma_{ij}^{(k)}\) is continuous. Where \(\theta_{ij}=0\), all corresponding \(\sigma_{ij}^{(k)}\) vanish and the off-diagonal penalty contribution at that pair is zero, while every nearby contribution is nonnegative. This gives lower semicontinuity at such points. A minimizing sequence therefore has a subsequence with constant discrete configuration and convergent means and covariances; the limit is feasible and its objective is no larger than the limiting objective values. Thus a minimum is attained. This uses only finite-dimensional compactness and lower semicontinuity, with their hypotheses verified above.

## Finite benchmarks below the threshold

Fix a contamination-count vector \(r\) with \(\beta(r)<\beta_0\). Since the counts are integers,
\[
r_k\le n_k-h_k\qquad(k=1,\ldots,K).
\]
Thus, in each class there are at least \(h_k\) clean rows in the casewise regime and at least \(h_k\) clean cells in every column in the cellwise regime.

For the casewise estimator, select \(h_k\) clean rows in every class. Set \(\Sigma_0^{(k)}=c_kI_q\), where the \(c_k\ge a_k\) are fixed, use the associated normalized decomposition, and choose finite means, for example the selected-row means. Every such benchmark uses only entries of the fixed clean data. There are finitely many possible selected subsets. Taking the maximum of their finite benchmark values gives a uniform finite upper bound \(M_{\mathrm{case}}\) for the optimum over the entire contamination neighborhood.

For the cellwise estimator, flag all replaced cells and retain all unchanged cells. Each column then retains at least \(h_k\) cells. Use the same fixed diagonal covariances and fixed finite means. All retained entries belong to the clean data. Each partial likelihood, including \(|J|\log(2\pi)\), is finite, as are the fixed flagging penalties and normalized covariance penalties. There are finitely many possible replacement-position patterns, so their benchmark values have a finite maximum \(M_{\mathrm{cell}}\), independent of replacement magnitudes.

For later use, uniform finite lower bounds for the sums of log-determinant and Gaussian-constant terms are
\[
B_{\mathrm{case}}=
\sum_{k=1}^K h_k\bigl[q\log a_k+q\log(2\pi)\bigr]
\]
and
\[
B_{\mathrm{cell}}=
\sum_{k=1}^K n_k\min_{0\le d\le q}
 d\bigl[\log a_k+\log(2\pi)\bigr].
\]
The value \(d=0\) accounts for empty retained patterns. Consequently the sum of retained quadratic terms at an optimum is at most \(M_{\mathcal R}-B_{\mathcal R}\).

## Implosion

Every feasible covariance satisfies
\[
\lambda_{\min}(\Sigma^{(k)})\ge a_k>0.
\]
Thus, for every admissible count vector and every contaminated sample,
\[
\min_k\lambda_{\min}(\widehat\Sigma^{(k)})
\ge\min_k a_k>0.
\]
The infimum over contaminated samples is also bounded below by \(\min_k a_k\), so the set defining implosion breakdown is empty. By the stipulated convention,
\[
\epsilon_{\mathcal R,-}=1.
\]

## No scatter explosion below \(\beta_0\)

First consider the casewise estimator. If, along a sequence of samples in the fixed contamination neighborhood, \(\lambda_{\max}(\widehat\Sigma^{(k_0)})\to\infty\), then
\[
\log\det\widehat\Sigma^{(k_0)}
\ge\log\lambda_{\max}(\widehat\Sigma^{(k_0)})
 +(q-1)\log a_{k_0}\longrightarrow\infty.
\]
This log determinant occurs \(h_{k_0}\ge1\) times. Every other class's log-determinant contribution has a uniform finite lower bound. All quadratic and penalty terms are nonnegative, and the Gaussian constants are fixed. The objective therefore tends to infinity, contradicting \(M_{\mathrm{case}}\).

For the cellwise estimator, suppose instead that \(\lambda_{\max}(\widehat\Sigma^{(k_0)})\to\infty\). At each sample, choose a coordinate \(j_*\) attaining the largest diagonal entry. Then
\[
\widehat\sigma_{j_*j_*}^{(k_0)}
\ge\lambda_{\max}(\widehat\Sigma^{(k_0)})/q.
\]
Column retention supplies a row \(i_*\) whose retained pattern \(A_{i_*}\) contains \(j_*\). Its principal submatrix satisfies
\[
\lambda_{\max}(\widehat\Sigma^{(k_0)}_{A_{i_*}A_{i_*}})
\ge\widehat\sigma_{j_*j_*}^{(k_0)},
\qquad
\lambda_{\min}(\widehat\Sigma^{(k_0)}_{A_{i_*}A_{i_*}})
\ge a_{k_0}.
\]
Hence
\[
\log\det\widehat\Sigma^{(k_0)}_{A_{i_*}A_{i_*}}
\ge\log\!\bigl(\lambda_{\max}(\widehat\Sigma^{(k_0)})/q\bigr)
 +( |A_{i_*}|-1)\log a_{k_0}.
\]
The second term has a uniform finite lower bound because \(1\le |A_{i_*}|\le q\). Every other partial log determinant, in every class, has the lower bound \(|A_i^{(k)}|\log a_k\). There are finitely many rows and possible pattern sizes. The Gaussian terms, quadratic terms, and penalties cannot offset the diverging determinant term by an unbounded negative amount. This contradicts \(M_{\mathrm{cell}}\).

These contradictions give uniform upper covariance bounds over the respective neighborhoods. Indeed, if no uniform bound existed, one could choose samples with the maximum fitted eigenvalue tending to infinity and, since there are finitely many classes, pass to a subsequence with a fixed exploding class. Therefore
\[
\epsilon_{\mathrm{case},+}\ge\beta_0,
\qquad
\epsilon_{\mathrm{cell},+}\ge\beta_0.
\]

## No location explosion below \(\beta_0\)

Let \(C_\Sigma\) be a uniform upper bound for all fitted largest covariance eigenvalues over the fixed neighborhood in the regime under consideration.

For the casewise estimator, a retained subset in class \(k_0\) has size \(h_{k_0}\), whereas at most \(n_{k_0}-h_{k_0}<h_{k_0}\) rows are replaced. It therefore contains a clean row \(z_{i_0}^{\star(k_0)}\). Put \(R_0=\max_i\|z_i^{\star(k_0)}\|_2\). Its quadratic term is at least
\[
\frac{\|z_{i_0}^{\star(k_0)}-\widehat\mu^{(k_0)}\|_2^2}{C_\Sigma}
\ge
\frac{\max\{\|\widehat\mu^{(k_0)}\|_2-R_0,0\}^2}{C_\Sigma}.
\]
The second inequality follows from the reverse triangle inequality together with nonnegativity of a norm. The uniform bound on the sum of quadratic terms therefore bounds \(\|\widehat\mu^{(k_0)}\|_2\).

For the cellwise estimator, the unchanged cells in each column and the retained cells in that column each form sets of size at least \(h_{k_0}>n_{k_0}/2\). Their intersection is nonempty. For each coordinate \(j\), choose an index \(i(j)\) in this intersection. Writing \(A_i\) for the retained pattern in class \(k_0\), the inverse principal-submatrix bound gives
\[
\begin{aligned}
&\sum_i (x_{i,A_i}^{(k_0)}-\widehat\mu_{A_i}^{(k_0)})^T
 (\widehat\Sigma_{A_iA_i}^{(k_0)})^{-1}
 (x_{i,A_i}^{(k_0)}-\widehat\mu_{A_i}^{(k_0)})\\
&\quad\ge\frac1{C_\Sigma}\sum_i\sum_{j\in A_i}
 (x_{ij}^{(k_0)}-\widehat\mu_j^{(k_0)})^2\\
&\quad\ge\frac1{C_\Sigma}\sum_{j=1}^q
 (z_{i(j)j}^{\star(k_0)}-\widehat\mu_j^{(k_0)})^2.
\end{aligned}
\]
There is no double counting in the last inequality: the chosen pairs \((i(j),j)\) are distinct even if several coordinates choose the same row. Although the selected indices may vary with the contaminated sample, all selected values come from a fixed finite clean data matrix. In particular, if \(R_j=\max_i|z_{ij}^{\star(k_0)}|\), each selected residual has absolute value at least \(\max\{|\widehat\mu_j^{(k_0)}|-R_j,0\}\). The uniform quadratic bound therefore bounds every fitted mean coordinate.

All classes have uniformly bounded fitted means. Their selected clean-data fitted means are finite by attainment. Subtracting those fixed baseline means preserves boundedness. Hence
\[
\epsilon_{\mathrm{case},\mu}^*\ge\beta_0,
\qquad
\epsilon_{\mathrm{cell},\mu}^*\ge\beta_0.
\]

## Sharpness

Choose \(k_*\) attaining
\[
\beta_0=\frac{n_{k_*}-h_{k_*}+1}{n_{k_*}},
\]
and take the count vector with \(r_{k_*}=n_{k_*}-h_{k_*}+1\) and all other counts zero.

In the casewise regime, replace exactly \(r_{k_*}\) rows of class \(k_*\) by \(ce_1\), where \(c\to+\infty\) through finite values. Only \(h_{k_*}-1\) rows of that class remain unchanged, so every retained subset contains a replaced row. At an exact minimizer, holding the selected weights and covariance fixed and differentiating with respect to the unconstrained mean yields
\[
\sum_iw_i^{(k_*)}(\widehat\Sigma^{(k_*)})^{-1}
 (x_i^{(k_*)}-\widehat\mu^{(k_*)})=0.
\]
Multiplication by the covariance and \(\sum_iw_i^{(k_*)}=h_{k_*}\) give the weighted-mean equation. Its first coordinate is
\[
\widehat\mu_1^{(k_*)}
=\frac{c}{h_{k_*}}N_c+
 \frac1{h_{k_*}}\sum_{i\ \mathrm{retained\ and\ unchanged}}
 z_{i1}^{\star(k_*)},
\qquad N_c\ge1.
\]
The clean sum is uniformly bounded, so this coordinate tends to \(+\infty\). Subtraction of the fixed clean-data fitted mean does not change divergence. This proves location breakdown at fraction \(\beta_0\).

In the cellwise regime, replace exactly \(r_{k_*}\) cells in column one of class \(k_*\) by \(c\), leaving every other cell unchanged. Every feasible mask retains at least one of these replaced cells, because there are only \(h_{k_*}-1\) unchanged cells in that column.

We derive the mean identity needed for this construction directly from the stated objective. Suppress the class index and write \(n=n_{k_*}\). For a retained pattern \(J\), let \(P_J\) be the coordinate-selection matrix, so \(P_Jv=v_J\) and \(\Sigma_{JJ}=P_J\Sigma P_J^T\). At an exact minimizer, the selected mask and covariance can be held fixed while the unconstrained mean is varied. The penalties and log determinants do not depend on the mean. Differentiating its quadratic terms therefore gives
\[
\sum_{i:J_i\ne\varnothing}
 P_{J_i}^T\widehat\Sigma_{J_iJ_i}^{-1}
 (x_{i,J_i}-\widehat\mu_{J_i})=0.
\]
Multiplying this full vector equation by \(\widehat\Sigma\) yields
\[
\sum_{i:J_i\ne\varnothing}
 \widehat\Sigma_{\cdot,J_i}\widehat\Sigma_{J_iJ_i}^{-1}
 (x_{i,J_i}-\widehat\mu_{J_i})=0.
\]
Define
\[
t_i=\widehat\mu+
 \widehat\Sigma_{\cdot,J_i}\widehat\Sigma_{J_iJ_i}^{-1}
 (x_{i,J_i}-\widehat\mu_{J_i})
\]
for a nonempty pattern, and \(t_i=\widehat\mu\) for an empty pattern. The multiplied score equation is exactly
\[
\widehat\mu=\frac1n\sum_{i=1}^nt_i.
\]
This is the conditional-completion mean identity, obtained here by algebra rather than assumed from an EM update. If coordinate one is retained, the first row of \(\widehat\Sigma_{\cdot,J_i}\) is the corresponding row of \(\widehat\Sigma_{J_iJ_i}\); multiplication by its inverse selects that coordinate. Thus \(t_{i1}=x_{i1}\). If coordinate one is not retained, put \(O_i=J_i\); then
\[
t_{i1}=\widehat\mu_1+
 \widehat\Sigma_{1,O_i}\widehat\Sigma_{O_iO_i}^{-1}
 (x_{i,O_i}-\widehat\mu_{O_i}),
\]
with the correction term defined as zero when \(O_i=\varnothing\). Taking the first coordinate gives precisely
\[
\widehat\mu_1
=\frac1n\sum_{i:m_{i1}=1}x_{i1}
 +\frac1n\sum_{i:m_{i1}=0}
 \left[\widehat\mu_1+
 \widehat\Sigma_{1,O_i}\widehat\Sigma_{O_iO_i}^{-1}
 (x_{i,O_i}-\widehat\mu_{O_i})\right].
\]

Now suppose that both breakdown suprema at this count vector were finite. The location-displacement supremum being finite implies a uniform bound \(\|\widehat\mu^{(k_*)}\|_2\le U\), since the clean-data fitted mean is fixed and finite. The scatter-explosion supremum being finite implies \(\lambda_{\max}(\widehat\Sigma^{(k_*)})\le V\) uniformly over this replacement sequence. The eigenvalue floor gives \(\|\widehat\Sigma_{O_iO_i}^{-1}\|_{\mathrm{op}}\le a_{k_*}^{-1}\), and the covariance bound gives \(\|\widehat\Sigma_{1,O_i}\|_2\le V\). Every coordinate in \(O_i\) lies outside column one and is therefore an unchanged clean coordinate. Its data vector has norm bounded by a fixed clean-data constant \(D\). Consequently every completion correction has absolute value at most
\[
Va_{k_*}^{-1}(D+U),
\]
uniformly over masks, replacement values, and rows; the empty-pattern correction is zero.

The retained first-column sum contains \(N_cc\) with \(N_c\ge1\), plus a uniformly bounded sum of clean entries. All the unretained completion terms are uniformly bounded by the preceding estimate. Thus the right-hand side of the first-coordinate identity is \(N_cc/n\) plus a uniformly bounded term, whereas its left-hand side is uniformly bounded. This is impossible as \(c\to+\infty\).

It follows that the location-displacement supremum or the scatter-explosion supremum is infinite at this permitted count vector. This is exactly the disjunction required by the breakdown definitions. It does not assert that one fixed mode diverges along the entire original sequence. If a witnessing divergent sequence is desired, choose a subsequence along which the quantity with infinite supremum tends to infinity; all its samples remain permitted finite replacements at fraction \(\beta_0\).

The two constructions prove sharpness of \(\beta_0\) as the common lower bound for location and scatter explosion. Together with the lower bounds and the uniform exclusion of implosion, they establish all stated conclusions.
