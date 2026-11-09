# Reference Proof

## Contract and proof obligations

All inference probabilities and limits refer to the public experiment with fixed predictor, fixed score and fixed target rule. Learned probabilities may depend jointly on the inference covariates and auxiliary training information; their associated observations are not assumed iid. Conditional on the full data and training information, labeling is fresh independent Bernoulli randomization.

The obligations are: (1) square integrability and the oracle first-order expansion; (2) a full-statistic learned-to-oracle comparison, rather than an unjustified iid expansion for learned probabilities; (3) the scalar HT comparison and resulting learned-policy expansion; (4) the oracle CLT and variance identification; (5) transfer of all three variance-estimation averages under only the stated moments; and (6) positive limiting variance and interval coverage. Each is established below.

## 1. Integrability and oracle expansion

Write p_i=pi_tau^*(X_i), q_i=hat pi_tau(X_i), a_i=h_1(Y_i), b_i=h_1^mu(hat Y_i), and d_i=a_i-b_i. These a_i and b_i denote population projections, not the supplied score-building functions in the public setup. Conditional Jensen gives E[a_i^2]<infinity and E[b_i^2]<infinity, hence E[d_i^2]<infinity. Let D_I=h(Y_I)-h(hat Y_I). Then E[D_I^2]<infinity.

Enlarge the experiment using iid uniforms U_i independent of the full data and policy-training information. Represent the learned indicators as 1{U_i<=q_i} and define oracle indicators as 1{U_i<=p_i}. This preserves the public learned experiment; the coupling is a proof construction, not an added assumption. Set B_i=1{U_i<=p_i}/p_i.

The oracle statistic is an ordinary U-statistic on iid W_i=(X_i,Y_i,U_i), with fixed kernel

K(W_I)=h(hat Y_I)+D_I product_{i in I} B_i.

Positivity bounds the weights and makes K square integrable. Conditional expectation over labeling gives E K=theta*. Integrating out W_2,...,W_r gives

E[K(W_1,...,W_r)|W_1]=b_1+B_1 d_1=:Z_1.

The independent background result used here is the square-integrable Hoeffding decomposition: for a fixed symmetric order-r kernel K on iid observations, U_n(K)-E K=(r/n)sum_i(E[K|W_i]-E K)+R_n, with E[R_n^2]<=C_r E[K^2]/n^2 for sufficiently large n. The bound follows from the orthogonal components of orders at least two and does not require nondegeneracy; for r=1 the remainder is zero. Its fixed-kernel, iid and moment hypotheses have just been verified. Therefore

U_AIPW^p-theta*=(r/n)sum_i(Z_i-theta*)+O_p(n^-1).

## 2. Full-statistic transfer for learned probabilities

Let F_n contain the full inference sample and all policy-training information, but not the fresh uniforms. Let E_n={min_i q_i>=pi_min/2}; P(E_n)->1. Throughout this section work on E_n. Put A_i=1{U_i<=q_i}/q_i and delta_n=max_i|q_i-p_i|.

Given F_n, coordinate pairs (A_i,B_i) are independent, E[A_i|F_n]=E[B_i|F_n]=1, and

E[(A_i-B_i)^2|F_n]=|q_i-p_i|/(p_i q_i)<=C delta_n.

All A_i and B_i are bounded by a constant depending only on pi_min. For a tuple I, set H_I=product_{i in I} A_i-product_{i in I} B_i. Its conditional mean is zero. Telescoping the products, applying (sum_{j=1}^r t_j)^2<=r sum_{j=1}^r t_j^2, and bounding the other factors shows

E[H_I^2|F_n]<=C_r delta_n.

For disjoint tuples I,J, conditional independence and centering give E[H_I H_J|F_n]=0. For intersecting tuples, conditional Cauchy-Schwarz gives |E[H_I H_J|F_n]|<=C_r delta_n.

Let M=binom(n,r) and A_n=M^-1 sum_I D_I^2. Each tuple intersects at most r binom(n-1,r-1) other tuples. Since 2|D_I D_J|<=D_I^2+D_J^2,

Var(M^-1 sum_I D_I H_I | F_n)
<=C_r delta_n M^-2 sum_{I,J:I intersect J nonempty}|D_I D_J|
<=C_r delta_n A_n/n.

Here and below constants can depend on fixed r and pi_min, but not on n or the fitted probabilities. Moreover E[A_n]=E[D_{1:r}^2]<infinity, so A_n=O_p(1). The conditional mean of the statistic difference is zero. H2 and conditional Chebyshev, localized to events on which sqrt(n)delta_n and A_n are bounded, give

U_AIPW^q-U_AIPW^p=O_p(n^-3/4)=o_p(n^-1/2).

The complement of E_n has vanishing probability, so the conclusion is unconditional, including the public zero-probability convention. This argument also applies to r=1. It supplies the learned-policy remainder justification missing from the source's direct substitution into an iid Hoeffding expansion.

## 3. Scalar coupling and learned first-order representation

Given F_n, the differences A_i-B_i are independent and centered. Hence

Var(n^-1 sum_i d_i(A_i-B_i)|F_n)
<=C delta_n n^-2 sum_i d_i^2.

The empirical second moment is O_p(1), and H2 gives

n^-1 sum_i d_i(A_i-B_i)=O_p(n^-3/4).

Combining this estimate, the full-statistic comparison, and the oracle expansion proves

U_AIPW^q-theta*=(r/n)sum_i[b_i+A_i d_i-theta*]+o_p(n^-1/2).

This is now derived rather than assumed. The rate assumption used for the trimmed rules is H2. No separate argument requiring tau>0 or tau<1 is needed.

## 4. Gaussian limit and positive variance

The oracle Z_i are iid and square integrable. Conditional on (X_i,Y_i), E[Z_i|X_i,Y_i]=a_i and

Var(Z_i|X_i,Y_i)=d_i^2(1/p_i-1).

Thus E Z_i=theta* and

Var(Z_i)=Var(h_1(Y))+E[d_i^2(1/p_i-1)].

This is finite by positivity and the projection second moments, and it is strictly positive because Var(h_1(Y))>0. In particular sigma_*^2=r^2 Var(Z_i)>0. The iid finite-variance CLT, followed by the oracle remainder bound, gives

sqrt(n)(U_AIPW^p-theta*) => N(0,sigma_*^2).

The full-statistic comparison and Slutsky give the identical limit for U_AIPW^q. These calculations include p_i=1; no strictly-less-than-one restriction is needed.

## 5. Variance-estimator consistency without fourth moments

We first establish the needed transfer estimate. Let omega_i be any fixed measurable function of the ith observation with E|omega_i|<infinity, and let eta be bounded and Lipschitz on [pi_min/2,1]. On E_n, split

1{U_i<=q_i}eta(q_i)-1{U_i<=p_i}eta(p_i)
=1{U_i<=q_i}[eta(q_i)-eta(p_i)]
+[1{U_i<=q_i}-1{U_i<=p_i}]eta(p_i).

After multiplication by omega_i and averaging, the absolute value of the first part is at most L_eta delta_n n^-1 sum_i|omega_i|=o_p(1), by the integrable iid law of large numbers. This is the fixed-indicator Lipschitz argument from the source, with its sufficient first-moment hypothesis made explicit.

For the second part, conditional on F_n the expected average absolute value is at most

||eta||_infinity delta_n n^-1 sum_i|omega_i|,

because P(1{U_i<=q_i} differs from 1{U_i<=p_i}|F_n)=|q_i-p_i|. This upper bound is o_p(1). Conditional Markov's inequality, localized to events where the bound is small, proves that the second part is o_p(1). Removing E_n does not affect convergence. Thus both the probabilities and their associated indicators may be changed in these integrable weighted averages.

Apply this result to

- omega_i=a_i, eta(t)=t^-1;
- omega_i=a_i^2, eta(t)=t^-1;
- omega_i=d_i^2, eta(t)=t^-2-t^-1.

Each omega_i is integrable by the already verified second moments. Both functions eta are bounded and Lipschitz on the closed positivity interval. No fourth moment is used.

Under the oracle policy these averages are iid averages of integrable variables. Their expectations, obtained by conditioning on (X,Y), are respectively E[a_i], E[a_i^2], and E[d_i^2(1/p_i-1)]. The iid law of large numbers and the transfer just established therefore imply

hat m_1 ->p E[a_i],
hat m_2 ->p E[a_i^2],
Varhat_1 ->p r^2 Var(a_i),
Varhat_2 ->p r^2 E[d_i^2(1/p_i-1)].

The variance identity in Section 4 shows that Varhat_1+Varhat_2 ->p sigma_*^2.

## 6. Coverage and exceptional cases

The raw HT variance sum can be negative in finite samples. Nevertheless it converges to the strictly positive sigma_*^2. Consequently hat sigma=sqrt(max{0,Varhat_1+Varhat_2}) ->p sigma_*>0, and the event hat sigma=0 has probability tending to zero. Slutsky gives the standard normal limit for the studentized statistic on its positive-standard-error event. Since the standard normal distribution has no atom at either critical value, the stated closed interval has limiting coverage 1-alpha for every fixed alpha in (0,1).

Zero learned probabilities can occur only outside E_n for sufficiently large n and are covered by the public finite-sample convention. Certainty sampling, tau=0, tau=1 and r=1 are included in the preceding bounds. No unresolved theorem-critical proof obligation remains.
