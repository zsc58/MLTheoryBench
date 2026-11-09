# Reference Proof

## Obligations and independent background

The proof must establish: (i) oracle-order invariance and the parameter-to-AUROC bound; (ii) localization and concentration of both empirical minimizers; (iii) the actual-versus-ideal augmented population displacement; (iv) an exponentially large local packing; (v) incompatibility of small AUROC regrets under distinct packing experiments, including ties; (vi) product-experiment KL control; and (vii) a measurable decoding reduction, Fano bound, and expectation conversion. All seven obligations are closed below.

We use the following standard independent inequalities, indexed by theory_023. If independent scalar variables lie in [-B,B], the average centered deviation exceeds t in absolute value with probability at most 2 exp(-m t^2/(2B^2)). If independent centered self-adjoint d-by-d matrices have operator norm at most B_H, their average has operator norm at least t with probability at most
\[
2d\exp\left\{-\frac{m t^2}{2B_H^2+(2/3)B_Ht}\right\}.
\]
This is the bounded-variance specialization of matrix Bernstein, since the variance proxy of the sum is at most m B_H^2. Finally, if V is uniform on M hypotheses and D is the observation, every decoder satisfies
\[
P(\widehat V\ne V)\ge 1-\frac{I(V;D)+\log 2}{\log M}.
\]
The hypotheses of these inequalities are checked at their applications. The packing and transport bounds used below are derived directly.

## 1. Alignment, ties, and AUROC stability

Alignment of restricted population minimizers is an assumption, not a consequence of strict propriety alone. Strict propriety identifies the unrestricted probability-valued Bayes score, but a restricted class need not contain it.

A strictly increasing transformation preserves both strict comparisons and ties. Thus, for every aligned population minimizer,
\[
\operatorname{AUC}(s_{\theta_\alpha^*})=\operatorname{AUC}(\Lambda).
\]
Let \(H(v)=\mathbf 1\{v>0\}+\tfrac12\mathbf 1\{v=0\}\). If \(q=s_{\theta_\alpha^*}\) and \(\|\theta-\theta_\alpha^*\|=v\), score Lipschitzness gives
\[
|(s_\theta(x)-s_\theta(z))-(q(x)-q(z))|\le 2L_s v.
\]
Outside \(\{|q(X_1)-q(X_0)|\le2L_sv\}\), the two comparisons agree. Since H takes values in [0,1],
\[
|\operatorname{AUC}(s_\theta)-\operatorname{AUC}(q)|
\le P(|q(X_1)-q(X_0)|\le2L_sv).
\]
Put \(\overline C=\max\{C_{ac},t_0^{-1}\}\). The assumed bound for margins up to t0, together with the trivial probability bound 1 for larger margins, implies
\[
|\operatorname{AUC}(s_\theta)-\operatorname{AUC}(q)|\le2\overline C L_s\|\theta-\theta_\alpha^*\|. \tag{1}
\]
The zero-displacement case is immediate. This argument also handles ties of the estimated score.

For later use, oracle optimality can be proved without a continuity assumption. Fix any experiment, write \(L=dP_1/dP_0\), \(Q=P_0\otimes P_0\), and \(\Delta(x,z)=L(x)-L(z)\). Symmetry gives
\[
\operatorname{AUC}(s)=\frac12\int[L(x)H(s(x)-s(z))+L(z)H(s(z)-s(x))]dQ.
\]
Define \(D_s(x,z)\) to be zero when \(\Delta=0\); otherwise it is zero for the correct strict order, one half for a tie, and one for the opposite strict order. Comparing the integrands for s and L yields
\[
\mathcal E(s):=\operatorname{AUC}(\Lambda)-\operatorname{AUC}(s)
=\frac12\int|\Delta|D_s\,dQ\ge0. \tag{2}
\]
Indeed, if \(L(x)>L(z)\), the three possible excess contributions are respectively 0, \((L(x)-L(z))/4\), and \((L(x)-L(z))/2\); the other strict order is symmetric. The integrals are finite because \(\int|\Delta|dQ\le2\).

## 2. Empirical localization and concentration

Consider either the raw or the actual augmented risk. Let m be its sample size, \(\theta_*\) its population minimizer, and \(\widehat R\) its empirical risk. The observations are independent, though their class distributions need not be identical. The population risk is the expectation of precisely this normalized empirical risk. Interior optimality and differentiation under the finite local expectations give \(E\nabla\widehat R(\theta_*)=0\).

The coordinate gradient bound and scalar Hoeffding, followed by a union bound over d coordinates, give, with failure probability at most \(\delta/4\),
\[
\|\nabla\widehat R(\theta_*)\|\le G_m:=B\sqrt{\frac{2d\log(8d/\delta)}m}. \tag{3}
\]
Each centered Hessian summand is independent, centered, self-adjoint, and bounded by B_H. Matrix Bernstein with \(t=\lambda/4\) therefore gives, with failure probability at most \(\delta/4\),
\[
\|\nabla^2\widehat R(\theta_*)-\nabla^2R(\theta_*)\|_{op}\le\lambda/4, \tag{4}
\]
provided
\[
m\ge\left(\frac{32B_H^2}{\lambda^2}+\frac{8B_H}{3\lambda}\right)\log(8d/\delta).
\]
Individual Hessian regularity and \(L_Hr\le\lambda/4\) imply on this event that
\[
\nabla^2\widehat R(\theta)\succeq(\lambda/2)I
\quad\text{for }\|\theta-\theta_*\|\le r. \tag{5}
\]
Take the sample sizes sufficiently large also that \(G_m\le\lambda r/4\). At a boundary point with \(v=\theta-\theta_*\) and \(\|v\|=r\), integrating the empirical Hessian yields
\[
v^T\nabla\widehat R(\theta)\ge-rG_m+\lambda r^2/2\ge\lambda r^2/4>0.
\]
Convexity excludes an empirical minimizer outside this ball: along the segment from \(\theta_*\) to such a minimizer, the boundary point would have a strictly positive directional derivative toward a point of no larger empirical risk, contradicting the convex first-order inequality. A boundary minimizer is also impossible, since the ball is contained in the interior of the parameter domain and its gradient would have to vanish. Consequently every empirical minimizer is interior to the ball.

Integrating (5) along the segment to \(\widehat\theta\), and using \(\nabla\widehat R(\widehat\theta)=0\), gives
\[
\frac\lambda2\|\widehat\theta-\theta_*\|^2
\le-\langle\widehat\theta-\theta_*,\nabla\widehat R(\theta_*)\rangle,
\]
so
\[
\|\widehat\theta-\theta_*\|\le\frac2\lambda G_m. \tag{6}
\]
The zero-error case needs no division. Apply this argument at both population minimizers, with m=n and m=N. The four events have total failure probability at most delta; dependence between the raw and augmented estimators does not affect this union bound. Since N>=n, one threshold on the real sample sizes suffices for both experiments. The same proof works when ntilde=0; no synthetic sample mean is then introduced. The source's sufficiently-large-sample qualification is thus essential and has been restored in the public task.

## 3. Synthetic population displacement and upper bounds

Let \(F=R_{\alpha_{aug}}\), \(\theta_I=\theta_{\alpha_{aug}}^*\), \(\theta_A=\theta_{aug}^*\), and \(w=\tilde n/N\). Actual augmented interior optimality and the population-risk definitions imply
\[
\nabla F(\theta_A)=-w\{E_{P_{syn}}\nabla_\theta\ell(\theta_A;X,1)-E_{P_1}\nabla_\theta\ell(\theta_A;X,1)\}.
\]
For any coupling (U,V) of P_syn and P1, Lipschitzness of the vector-valued gradient gives
\[
\|E\nabla\ell(\theta_A;U,1)-E\nabla\ell(\theta_A;V,1)\|
\le E\|\nabla\ell(\theta_A;U,1)-\nabla\ell(\theta_A;V,1)\|
\le L_g E\|U-V\|.
\]
Taking the infimum over couplings proves
\[
\|\nabla F(\theta_A)\|\le wL_g\varepsilon_{syn}. \tag{7}
\]
This argument does not require identifying scalar transport duality with a vector-valued equality.

The ideal-risk inequality applies at \(\theta_A\) because the assumed neighborhood contains it. Young's inequality gives
\[
F(\theta_A)-F(\theta_I)
\le\langle\nabla F(\theta_A),\theta_A-\theta_I\rangle-\frac\mu2\|\theta_A-\theta_I\|^2
\le\frac{\|\nabla F(\theta_A)\|^2}{2\mu}.
\]
Combining with ideal-risk quadratic growth yields
\[
\|\theta_A-\theta_I\|\le\frac{L_g}{\sqrt{2\mu L_\alpha}}w\varepsilon_{syn}. \tag{8}
\]
These constants must not be replaced by lambda without an additional relation not assumed in the source.

Use (1) at the raw aligned population minimizer and (6) to obtain the raw bound. For augmentation, use (1) at the ideal aligned population minimizer, then the triangle inequality, (6), and (8). Thus both claimed inequalities hold simultaneously. Replacing log(8d/delta) by log(6d/delta) only enlarges a numerical multiplier, since their ratio is uniformly bounded for d>=1 and delta in (0,1). The constant C can depend only on C_ac and t0, with all displayed curvature, gradient, and score factors kept explicit.

## 4. Local sphere packing

Write \(\gamma\in(0,1)\) for the angular separation constant and set \(b=(1+\gamma)/2\). Take a maximal \(\gamma\)-separated set \(v_1,\ldots,v_M\) in the radius-b ball of \(\mathbb R^{d-1}\). Such a finite maximal set exists by compactness. Its radius-gamma balls cover the radius-b ball, so comparison of Euclidean volumes gives
\[
M\ge(b/\gamma)^{d-1}.
\]
Embed it in the sphere by \(u_j=(v_j,\sqrt{1-\|v_j\|^2})\). Distances do not decrease, so \(\|u_i-u_j\|\ge\gamma\). For d>=2,
\[
\log M\ge\kappa d,\qquad \kappa=\tfrac12\log((1+\gamma)/(2\gamma))>0.
\]
Set \(\eta_j=\eta_0+hu_j\), with \(0<h\le h_0\) and \(h<r_0\). These are admissible local parameters, and their pairwise distances are at most 2h as well as at least gamma h. Exact equality of all pairwise distances is neither claimed nor needed.

## 5. Regret incompatibility, not scalar oracle-value separation

Apply identity (2) in each experiment. Write \(\mathcal E_j(s)=\operatorname{AUC}_{\eta_j}(\Lambda_{\eta_j})-\operatorname{AUC}_{\eta_j}(s)\), and let \(D_{j,s}\) be its tie-aware disagreement loss. On \(\mathcal R_{ij}=\{\Delta_{\eta_i}\Delta_{\eta_j}<0\}\), the two strict oracle orders oppose one another. For every score, including scores with ties,
\[
D_{i,s}+D_{j,s}=1\quad\text{on }\mathcal R_{ij}.
\]
Consequently, measure domination and weighted separation give
\[
\begin{aligned}
\mathcal E_i(s)+\mathcal E_j(s)
&\ge\frac{c_Q}{2}\int_{\mathcal R_{ij}}\bigl(|\Delta_{\eta_i}|D_{i,s}+|\Delta_{\eta_j}|D_{j,s}\bigr)dQ_0\\
&\ge\frac{c_Q}{2}\int_{\mathcal R_{ij}}\min\{|\Delta_{\eta_i}|,|\Delta_{\eta_j}|\}\,dQ_0
\ge\frac{c_Qc_{rk}}2h.
\end{aligned} \tag{9}
\]
In particular, with \(\epsilon_h=c_Qc_{rk}h/8\), every score satisfies \(\max\{\mathcal E_i(s),\mathcal E_j(s)\}\ge2\epsilon_h\). This is the separation needed for testing. The numerical optimal AUROC values in two experiments need not be different.

## 6. KL control for the actual observation experiment

Fix two local parameters eta and eta', put \(v=\eta-\eta'\), and let \(\eta_t=\eta'+tv\). Continuous differentiability of the densities gives
\[
p_{y,\eta}(x)-p_{y,\eta'}(x)=\int_0^1v^TS_y(x;\eta_t)p_{y,\eta_t}(x)dt.
\]
The comparability assumptions give common class-specific supports up to null sets. On zero-density sets the derivative of a nonnegative differentiable density at an interior parameter is zero, so the formula is consistent with taking S_y=0 there. Cauchy-Schwarz, Tonelli, and comparability imply
\[
\begin{aligned}
\chi^2(P_{y,\eta},P_{y,\eta'})
&\le\|v\|^2\int_0^1\int\|S_y(x;\eta_t)\|^2\frac{p_{y,\eta_t}(x)^2}{p_{y,\eta'}(x)}d\nu(x)dt\\
&\le B_{lr}\|v\|^2\int_0^1E_{y,\eta_t}\|S_y(X;\eta_t)\|^2dt
\le B_{lr}I_y\|v\|^2.
\end{aligned}
\]
The elementary inequality log u<=u-1 gives KL<=chi-squared. Independence of the stratified observations and expansion of the product log density give
\[
D_{KL}(\mathbb P_\eta^{(n)}\|\mathbb P_{\eta'}^{(n)})
=n_0D_{KL}(P_{0,\eta}\|P_{0,\eta'})+n_1D_{KL}(P_{1,\eta}\|P_{1,\eta'})
\le B_{lr}I_{max}n\|v\|^2.
\]
Hence packing experiments have KL at most \(4B_{lr}I_{max}nh^2\). This verifies the observation model used in the lower bound; no additional observations or unknown-parameter-dependent side information are available to the estimator.

## 7. Decoding, Fano, and expectation

Choose a>0 small enough that \(4B_{lr}I_{max}a^2\le\kappa/4\); one may use a denominator involving \(1+I_{max}\) to avoid any division by zero. Take \(h=a\sqrt{d/n}\), subject to the two stated radius restrictions. Let V be uniform on the packing and draw D from the corresponding stratified experiment.

For any measurable score estimator, define \(\widehat V\) to minimize \(\mathcal E_j(\widehat s)\) over the finite set, breaking ties by the smallest index. Joint measurability of the score and integration of bounded measurable comparison functions make this decoder measurable. If \(\mathcal E_i(\widehat s)<\epsilon_h\), (9) forces every other regret to be at least \(2\epsilon_h\), so decoding must be correct. Thus
\[
P(\widehat V\ne V)\le\frac1M\sum_iP_{\eta_i}(\mathcal E_i(\widehat s)\ge\epsilon_h). \tag{10}
\]
If \(\overline P=M^{-1}\sum_j\mathbb P_{\eta_j}^{(n)}\), concavity of log yields
\[
I(V;D)=\frac1M\sum_iD_{KL}(\mathbb P_{\eta_i}^{(n)}\|\overline P)
\le\frac1{M^2}\sum_{i,j}D_{KL}(\mathbb P_{\eta_i}^{(n)}\|\mathbb P_{\eta_j}^{(n)})
\le\tfrac14\log M.
\]
Fano applies to this finite experiment and gives testing error at least \(3/4-\log2/(\kappa d)\). Choose d0 large enough that this is at least 1/4 for d>=d0. Independent estimator randomization, if present, adds no information about V and does not change this conclusion.

By nonnegativity of regret, (10) implies
\[
\sup_{\eta\in\mathcal H}E_\eta\mathcal E_\eta(\widehat s)
\ge\frac1M\sum_iE_{\eta_i}\mathcal E_i(\widehat s)
\ge\epsilon_h P(\widehat V\ne V)
\ge\frac{c_Qc_{rk}a}{32}\sqrt{d/n}.
\]
This holds for every estimator, so also after taking the infimum over estimators. All packing points lie in the specified local neighborhood. Constants depend on the stated family constants; bounded information moments are not silently assumed dimension-uniform.

## Interpretation

At fixed dimension and fixed regularity constants, the upper bounds have n^{-1/2} stochastic dependence, and the local family has an n^{-1/2} minimax obstruction. The upper bound retains its displayed logarithmic dimension factor. A uniform upper/lower comparison on the local family requires the upper assumptions and their constants to hold uniformly there; the mere existence of a separate local lower-bound family does not prove sharpness for every well-specified classification problem. Augmentation changes the stochastic sample-size term from n to N and adds the displayed synthetic-distribution bias. No unresolved proof obligation remains.
