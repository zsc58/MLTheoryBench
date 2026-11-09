# Reference Proof

## Proof Structure

1. Identify the finite-location arm means, derive the augmented-score bias and replacement bounds, and establish the canonical gradient in the nonparametric observed-data model.
2. Apply the nuisance bounds separately within each of the fixed validation folds to prove asymptotic linearity, covariance consistency, and ridge-inverse convergence.
3. Use the QMD local experiment, a joint central limit theorem, contiguity and Gaussian likelihood tilting to obtain the local Gaussian and noncentral chi-square limits; differentiate the population criterion along the same path.
4. Derive bounded-Lipschitz uniform empirical control, transfer fitted population moments to oracle moments using the specified nuisance errors, control the ridge criterion, and bound the population optimization gap.

## Standard Background Used

The standard-independent results indexed by theory_015 are used in the following forms. A dominated regular iid QMD path with score $g\in L_2^0(P_0)$ yields, for fixed $h$, the LAN expansion $h n^{-1/2}\sum_i g(Z_i)-h^2 E_0g^2/2+o_{P_0}(1)$ and contiguity of its local alternatives with respect to $P_0^{\otimes n}$. Le Cam's third lemma exponentially tilts a joint statistic/log-likelihood limit; when the statistic and score limits are jointly centered Gaussian, this changes the statistic's mean by $h$ times its covariance with the score and leaves its covariance unchanged. The finite-second-moment multivariate CLT, law of large numbers, continuous mapping and Slutsky are also used. For independent scalar observations bounded in absolute value by $B$, Hoeffding's inequality gives the tail bound $2\exp\{-nt^2/(2B^2)\}$ for a sample-mean error exceeding $t$; it applies conditionally when the evaluated function is determined by independent training information. Finally, the squared norm of $N(b,I_J)$ is $\chi_J^2(\|b\|^2)$.

The QMD, independence, boundedness and finite-second-moment hypotheses needed for these uses are verified below. No paper-specific technical lemma is taken as an unexplained external result.

## Complete Proof

### Identification and Canonical Gradient

All expectations in the fixed-law argument are under $P$. Fix $V$ and write $K=K_V$. Armwise exchangeability, consistency and iterated expectation give
\[
E[K(Y(a))]=E\{E[K(Y(a))\mid X]\}
=E\{E[K(Y)\mid A=a,X]\}=E[m_a(X;V)].
\]
Positivity ensures the observed arm conditionals identify these quantities almost surely with respect to $P_X$. Boundedness of $K$ makes all means finite.

For a deterministic nuisance tuple with positive propensity bounded away from zero and bounded regression, conditioning on $X$ gives
\[
E[\phi_V^a(Z;\eta)\mid X]
=\frac{\pi_0(a\mid X)}{\pi(a\mid X)}\{m_a(X;V)-r_a(X;V)\}+r_a(X;V).
\]
Consequently,
\[
E\phi_V^a(Z;\eta)-\mu_{a,V}
=E\left[\frac{\pi_0(a\mid X)-\pi(a\mid X)}{\pi(a\mid X)}\{m_a(X;V)-r_a(X;V)\}\right]. \tag{1}
\]
This also proves double robustness when either nuisance component is correct, although double robustness is not an additional conclusion demanded by the public task.

For the gradient, let $s$ be the score of a regular observed-data path at $P$, and let $s_X=E[s\mid X]$. Conditional-score differentiation of the identified arm mean gives
\[
\dot\mu_{a,V}(s)
=E[m_a(X;V)s_X(X)]
+E\left[E\{(K(Y)-m_a(X;V))s(Z)\mid A=a,X\}\right]. \tag{2}
\]
To see the conditional-outcome term, the conditional score of $Y$ given $(A,X)$ is $s-E[s\mid A,X]$. Differentiating the conditional mean therefore gives $E[(K-m_a)s\mid A=a,X]$, since the residual has zero conditional mean. Differentiating the marginal law of $X$ gives the first term. These identities can first be checked directly for bounded likelihood tilts and then extended by the regular conditional-score calculus; all represented derivatives are continuous in $L_2(P)$ because $K$, the arm regressions and the inverse true propensities are bounded.

Since $Es=0$, the first term in (2) equals $E[(m_a-\mu_{a,V})s]$. The second term equals
\[
E\left[\frac{1\{A=a\}}{\pi_0(a\mid X)}\{K(Y)-m_a(X;V)\}s(Z)\right].
\]
Thus the arm gradient is $\phi_V^a(Z;\eta_0)-\mu_{a,V}$, and subtracting arms gives the gradient $\psi_V$ of $\mu_V$.

This gradient is mean zero and square integrable by boundedness and positivity. In the nonparametric observed-data model, bounded mean-zero scores generate regular likelihood tilts and are dense in $L_2^0(P)$. Small bounded tilts preserve a positive propensity lower bound, with a possibly different constant, so these scores remain available in the model. Its tangent space is therefore $L_2^0(P)$. The displayed gradient belongs to this tangent space and represents every path derivative, establishing that it is the canonical gradient, with covariance $\Sigma_V$.

### Nuisance Replacement Bounds

Write $I_a=1\{A=a\}$, $\pi_a=\pi(a\mid X)$ and $\pi_{0,a}=\pi_0(a\mid X)$. Direct subtraction gives
\[
D_a:=\phi_V^a(Z;\eta)-\phi_V^a(Z;\eta_0)
=\left(1-\frac{I_a}{\pi_{0,a}}\right)(r_a-m_a)
+I_a\left(\frac1{\pi_a}-\frac1{\pi_{0,a}}\right)(K-r_a). \tag{3}
\]
If $\alpha_a=\|\pi_a-\pi_{0,a}\|_{L_2(P_X)}$ and $\beta_a=\|r_a-m_a\|_{L_2(P_X;\mathbb R^J)}$, (1), fitted positivity and Cauchy-Schwarz imply
\[
\|ED_a\|\le C\alpha_a\beta_a. \tag{4}
\]
On the event of fitted positivity and regression boundedness, the first coefficient in (3) is bounded, the inverse-propensity difference is at most $C|\pi_a-\pi_{0,a}|$, and $K-r_a$ is bounded. Squaring (3) with $\|u+v\|^2\le2\|u\|^2+2\|v\|^2$ gives
\[
E\|D_a\|^2\le C(\alpha_a^2+\beta_a^2). \tag{5}
\]
The constants depend only on the fixed kernel, regression and positivity bounds. For the contrast difference $d=D_1-D_0$, these yield
\[
\|Pd\|\le C\sum_a\alpha_a\beta_a,
\qquad P\|d\|^2\le C\sum_a(\alpha_a^2+\beta_a^2). \tag{6}
\]

### Cross-Fitted Expansion and Covariance

Let $n_k=|\mathcal I_k|$, let $P_{n,k}$ be the empirical measure on fold $k$, and set $z_0=z_V^{\rm dr}(\cdot;\eta_0)$ and $d_k=z_V^{\rm dr}(\cdot;\widehat\eta_k)-z_0$. The assumed fold-uniform rates and (6) give
\[
\max_k\|Pd_k\|=o_p(n^{-1/2}),
\qquad \max_k P\|d_k\|^2=o_p(1). \tag{7}
\]
Bounds are established on the training-measurable events of fitted boundedness and positivity, whose probabilities tend to one.

Decompose
\[
\sqrt n(\bar z_{n,V}^{\rm dr}-\mu_V)
=\frac1{\sqrt n}\sum_i\psi_V(Z_i)
+\sqrt n\sum_k\frac{n_k}{n}Pd_k
+\sum_k\sqrt n\frac{n_k}{n}(P_{n,k}-P)d_k. \tag{8}
\]
The bias term is $o_p(1)$ by (7). Let $\mathcal F_k$ contain only the information used to train $\widehat\eta_k$ and the independent fold assignment. Conditional on this information, fold $k$ consists of iid observations independent of $d_k$. Hence
\[
E\left[\left\|\sqrt n\frac{n_k}{n}(P_{n,k}-P)d_k\right\|^2\,\middle|\,\mathcal F_k\right]
\le\frac{n_k}{n}P\|d_k\|^2=o_p(1). \tag{9}
\]
Conditional Markov gives an $o_p(1)$ contribution for each fold. Formally, the conditional probability is bounded by the minimum of one and the conditional second moment divided by any fixed positive threshold squared; this bounded quantity converges to zero in probability and hence in expectation. Since $K$ is fixed, the sum in (8) is $o_p(1)$, proving the asserted expansion.

For covariance, put
\[
A_{n,k}=\frac{n_k}{n}P_{n,k}\|d_k\|^2,
\qquad A_n=\sum_k A_{n,k}.
\]
Condition separately on each $\mathcal F_k$:
\[
E[A_{n,k}\mid\mathcal F_k]=\frac{n_k}{n}P\|d_k\|^2=o_p(1).
\]
Conditional Markov and fixed $K$ imply $A_n=o_p(1)$. Importantly, this argument does not condition simultaneously on all cross-fitted nuisance estimates. That joint conditioning need not leave any fold independent of the conditioned information; this is the local repair to source line 476.

Writing $\widehat M_n=n^{-1}\sum_i z_{i,V}^{\rm dr}z_{i,V}^{{\rm dr}\top}$, expansion of each outer product and Cauchy-Schwarz give
\[
\left\|\widehat M_n-\frac1n\sum_i z_0(Z_i)z_0(Z_i)^\top\right\|_F
\le A_n+2A_n^{1/2}\left\{\frac1n\sum_i\|z_0(Z_i)\|^2\right\}^{1/2}=o_p(1).
\]
The oracle features are iid and bounded, so their first and second empirical moments converge to their population moments. The expansion also implies $\bar z_{n,V}^{\rm dr}\to_p\mu_V$. Therefore
\[
S_{n,V}^{\rm dr}
=\frac n{n-1}\{\widehat M_n-\bar z_{n,V}^{\rm dr}\bar z_{n,V}^{{\rm dr}\top}\}
\to_p P[z_0z_0^\top]-\mu_V\mu_V^\top=\Sigma_V.
\]
Positive definiteness and $\gamma_n\to0$ imply convergence of the ridge inverse to $\Sigma_V^{-1}$ by continuity of inversion. Positive $\gamma_n$ also ensures that each finite-sample inverse exists.

### Local Experiment and Population Criterion

Here all oracle quantities are evaluated at $P_0$, the same cross-fitted statistic is a measurable function of the $n$ observations and independent algorithmic randomization, and the nuisance assumptions hold under $P_0^{\otimes n}$. Write
\[
W_n=n^{-1/2}\sum_i\psi_V(Z_i),\qquad G_n=n^{-1/2}\sum_i g(Z_i),\qquad I_g=E_0g^2.
\]
The influence function is bounded and $g\in L_2^0(P_0)$, so the multivariate CLT applies and gives
\[
(W_n,G_n)\Rightarrow N\left(0,
\begin{pmatrix}\Sigma_V&\eta_V(g)\\\eta_V(g)^\top&I_g\end{pmatrix}\right).
\]
QMD and fixed $h$ verify the hypotheses of the standard LAN and contiguity result. The log-likelihood limit is $L=hG-h^2I_g/2$, with $E e^L=1$, including when $I_g=0$. Gaussian exponential tilting in the third lemma gives
\[
W_n\Rightarrow N(h\eta_V(g),\Sigma_V)
\quad\text{under }P_{n,h,g}.
\]
The likelihood ratio is unchanged by adjoining independent algorithmic randomization with the same law in both experiments. Thus contiguity applies to the entire statistic. It transfers the null $o_p(1)$ remainder, covariance convergence and inverse convergence to the local alternatives. Since $\mu_V(P_0)=0$, this proves the asserted shifted Gaussian limit for $\sqrt n\bar z_{n,V}^{\rm dr}$.

By Slutsky,
\[
T_n(V)\Rightarrow H^\top\Sigma_V^{-1}H,
\qquad H\sim N(h\eta_V(g),\Sigma_V).
\]
Whitening gives the squared norm of $N(h\Sigma_V^{-1/2}\eta_V(g),I_J)$, hence the noncentrality $h^2\lambda_V(g)$ and the required chi-square limit. The argument covers zero drift and zero score without division by the drift or score variance.

The gradient calculation gives, along the regular path,
\[
\mu_V(P_{t,g})=t\eta_V(g)+o(|t|).
\]
For fixed nonzero $h$, set $t_n=h/\sqrt n$. Then $\sqrt n\mu_V(P_{t_n,g})\to h\eta_V(g)$. The assumed covariance continuity and nonsingularity imply $\Sigma_V(P_{t_n,g})^{-1}\to\Sigma_V(P_0)^{-1}$. Substitution into the quadratic form proves
\[
n\Lambda_V(P_{t_n,g})\to h^2\lambda_V(g).
\]
If $h=0$, the argument is exact: $P_{t_n,g}=P_0$, $\mu_V(P_0)=0$, and both sides equal zero.

For interpretation only, the same drift expansion shows that the feasible estimator, centered at $\mu_V(P_{t_n,g})$, has local limit $N(0,\Sigma_V)$ along every regular path. Together with its canonical gradient, this is the no-extra-noise regular limit described by the convolution theorem. Neither a separate convolution proof nor an omnibus uniformly-most-powerful claim is required by the public target.

### Uniform Location Learning

Return to the fixed law $P$. Condition on the nuisance-training information $\mathcal F_\eta$, including independent training randomization, and write
\[
\widehat z_V(z)=z_V^{\rm dr}(z;\widehat\eta),\quad
z_V^0(z)=z_V^{\rm dr}(z;\eta_0),\quad
\mu_V^\eta=P\widehat z_V,\quad
M_V^\eta=P[\widehat z_V\widehat z_V^\top],\quad
\Sigma_V^\eta=M_V^\eta-\mu_V^\eta\mu_V^{\eta\top}.
\]
Here $P$ integrates a fresh observation, keeping the fitted functions fixed. These are private proof quantities, not additional assumptions.

On the high-probability event in the learning assumptions, fitted positivity and the scalar regression/kernel bounds give constants $B_z,L_z<\infty$, independent of both sample sizes, such that
\[
\sup_{V,z}\|\widehat z_V(z)\|\le B_z,
\qquad\|\widehat z_V(z)-\widehat z_{V'}(z)\|\le L_z\|V-V'\|.
\]
Indeed, vector kernel and regression bounds are $\sqrt J B_k$ and $\sqrt J B_m$, and their vector Lipschitz constants are $L_k$ and $L_m$. Apply the score formula and the propensity lower bound to each arm. True scalar regressions inherit kernel bounds by conditional expectation, so the oracle features also have uniform boundedness and Lipschitzness; enlarge constants to cover both versions if necessary.

Let $m=Jd$ and $N=n_{\rm tr}$. A compact subset of the fixed cube has a $\delta$-net of cardinality at most $(1+C R\sqrt m/\delta)^m$. This form also covers $R=0$. For a scalar class $f_V$ with bound $B$ and Lipschitz constant $L$, its empirical error satisfies
\[
\sup_V|(P_N-P)f_V|
\le\max_{U\text{ in the net}}|(P_N-P)f_U|+2L\delta.
\]
Conditional on $\mathcal F_\eta$, the learning observations remain iid from $P$. Hoeffding and a union bound give
\[
\Pr\left(\max_U|(P_N-P)f_U|>t\mid\mathcal F_\eta\right)
\le2(1+C R\sqrt m/\delta)^m\exp\{-Nt^2/(2B^2)\}.
\]
Take $\delta=N^{-1/2}$ and $t=C_1\sqrt{m\log N/N}$ with a sufficiently large fixed $C_1$. This proves the required stochastic order, also unconditionally since the boundedness event has probability tending to one.

Apply the scalar argument to all fitted feature coordinates and to all coordinate products. The product classes have bound $B_z^2$ and Lipschitz constant at most $2B_zL_z$. Fixed $J$ gives, with $a_N=\sqrt{Jd\log N/N}$,
\[
\sup_V\|\widehat\mu_V-\mu_V^\eta\|=O_p(a_N),
\qquad\sup_V\|\widehat M_V-M_V^\eta\|_F=O_p(a_N).
\]
The inequality $\|uu^\top-vv^\top\|_F\le(\|u\|+\|v\|)\|u-v\|$, together with the factor $N/(N-1)$ and bounded moments, gives
\[
\sup_V\|\widehat\Sigma_V-\Sigma_V^\eta\|_F=O_p(a_N).
\]
Continuity in $V$ and compactness make these suprema measurable via a countable dense subset.

It remains to derive nuisance transfer from the actual $\rho_{n_\eta}$. For each arm and tuple,
\[
\|\widehat m_a(\cdot;V)-m_a(\cdot;V)\|_{L_2(P_X;\mathbb R^J)}
\le\sqrt J\sup_{v\in\Pi(\mathcal V)}\|\widehat m_a(\cdot;v)-m_a(\cdot;v)\|_{L_2(P_X)}.
\]
The uniform version of (5), followed by the two-arm inequality, therefore gives, for $d_V=\widehat z_V-z_V^0$,
\[
\sup_V P\|d_V\|^2\le C\rho_{n_\eta}^2.
\]
Hence $\sup_V\|\mu_V^\eta-\mu_V\|\le C\rho_{n_\eta}$. Expanding
\[
\widehat z_V\widehat z_V^\top-z_V^0z_V^{0\top}
=d_Vd_V^\top+d_Vz_V^{0\top}+z_V^0d_V^\top
\]
and using the oracle bound gives a second-moment difference at most $C(\rho_{n_\eta}^2+\rho_{n_\eta})$. The means are uniformly bounded, so their outer-product difference is at most $C\rho_{n_\eta}$. Since $\rho_{n_\eta}=o_p(1)$,
\[
\sup_V\|\Sigma_V^\eta-\Sigma_V\|_F=O_p(\rho_{n_\eta}).
\]
Combining empirical and population replacement yields uniform mean and covariance errors $O_p(a_N+\rho_{n_\eta})$. With a random nonnegative $\rho$, these statements mean the ratios by $a_N+\rho$ are tight; the derived bounds establish that interpretation directly.

For positive semidefinite $A,\widetilde A$, the ridge inverses have norm at most $\tau^{-1}$ and
\[
(A+\tau I)^{-1}-(\widetilde A+\tau I)^{-1}
=(A+\tau I)^{-1}(\widetilde A-A)(\widetilde A+\tau I)^{-1}.
\]
If $\|u\|,\|\widetilde u\|\le B$, adding and subtracting the quadratic form with common inverse gives
\[
|u^\top(A+\tau I)^{-1}u-\widetilde u^\top(\widetilde A+\tau I)^{-1}\widetilde u|
\le\frac{2B}{\tau}\|u-\widetilde u\|+
\frac{B^2}{\tau^2}\|A-\widetilde A\|_F.
\]
All empirical and population covariances are positive semidefinite. Applying this bound uniformly proves
\[
\Delta_{\rm tr}:=\sup_V|\widehat P_\tau(V)-P_\tau(V)|
=O_p\left(\sqrt{Jd\log n_{\rm tr}/n_{\rm tr}}+\rho_{n_\eta}\right).
\]
No covariance nonsingularity is required on the learning class because $\tau$ is fixed and positive.

The oracle features are bounded and Lipschitz, so $P_\tau$ is continuous; on the nonempty compact class it attains its maximum. For any maximizer $V^\star$, adding and subtracting empirical values gives the deterministic inequality
\[
0\le P_\tau(V^\star)-P_\tau(\widehat V)
\le2\Delta_{\rm tr}+
\{\sup_V\widehat P_\tau(V)-\widehat P_\tau(\widehat V)\}
\le2\Delta_{\rm tr}+e_{\rm tr}.
\]
This proves the claimed near-optimality rate, including $e_{\rm tr}=0$. All hidden constants may depend on the fixed dimensions, cube radius, kernel and regression bounds, Lipschitz constants, positivity constants and $\tau$, but not on either sample size. All theorem-critical obligations are closed.
