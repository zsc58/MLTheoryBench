# Reference Proof

## Contract and proof obligations

The base-rule assumption is uniform over fixed indexed datasets. It is not merely an assertion along a sequential run of the base rule. The available history is causal and contains no information about unrevealed responses through evaluation timing. Queries are assigned only to available workers. We must establish: the posterior law after fantasization; transfer of the base-rule inequality and its moments with justified integrability; a pathwise variance-information bound; a valid expected-regret decomposition; the finite-set Gaussian maximum bound with the stated constant; and the delayed variance bound. Each obligation is established below.

## 1. Conditional Gaussian resampling

Let H_t denote the information immediately before the current fantasy draw, including selected locations, completed responses, completed/pending indicators, and past algorithmic randomness. The causal observation convention implies that the conditional law of f given H_t is GP(mu(.;D_{N_{t-1}}),k_{D_{N_{t-1}}}). To see why adaptive locations do not change this posterior, write the likelihood of a realized transcript as the product of Gaussian likelihoods for its revealed responses and the selection, randomization, and scheduling factors. Conditional on the realized transcript, the latter factors do not depend on the unknown function. The remaining likelihood is exactly the GP regression likelihood for the completed responses. This argument also applies to degenerate Gaussian priors, by multiplying the prior measure by the positive Gaussian noise likelihoods.

Conditional on H_t, g_t is an independent draw from this posterior. Pending locations are now fixed. Conditioning g_t on the current fantasy labels multiplies its posterior measure by the independent Gaussian likelihoods at those locations. Thus, writing D_t^F=D^{fant}_{t-1},

`Law(g_t | H_t,D_t^F)=GP(mu(.;D_t^F),k_{D_t^F}).`

The distribution on the right depends on H_t only through D_t^F. The fresh internal randomness used by A is independent of g_t conditional on this dataset. Therefore the fixed-dataset base-rule assumption applies to g_t and x_t=A(D_t^F). This is a posterior update identity; no equality with the history law of a separate sequential run of A is asserted or needed.

## 2. Pathwise variance-information inequality

Fix any realized location sequence a_1,...,a_m and arbitrary labels at these locations. Let s_j^2 be the posterior variance at a_j after the preceding j-1 locations. Positive noise variance makes every observation covariance matrix invertible, and Gaussian conditioning gives 0<=s_j^2<=k(a_j,a_j)<=1.

For a>0 and b in [0,1], convexity of x -> (1+a)^x gives `(1+a)^b<=1+ab`. Taking logarithms with a=sigma_noise^{-2} and b=s_j^2 yields

`s_j^2 log(1+sigma_noise^{-2}) <= log(1+sigma_noise^{-2}s_j^2).`

Successive Schur complements give

`sum_{j=1}^m log(1+sigma_noise^{-2}s_j^2)=log det(I+sigma_noise^{-2}K_m).`

For the fixed-design Gaussian experiment, subtracting the entropy of the independent observation noise from the entropy of the noisy vector gives

`I(y;f_a)=(1/2)log det(I+sigma_noise^{-2}K_m).`

The noisy covariance is positive definite even if K_m is singular, so this calculation needs no strict positivity assumption on k. By the definition of gamma_m this mutual information is at most gamma_m. Consequently

`sum_{j=1}^m s_j^2 <= C1 gamma_m.`

For m=0 both sides are zero. Since the argument holds for every fixed location sequence and posterior covariance is label-independent, it holds pathwise when evaluated on adaptively selected locations. It does not identify a random variance sum with unconditional mutual information under adaptive selection.

## 3. Fantasy-path regret and integrable mean functions

Write E_D for expectation in the fixed-dataset experiment from the base-rule assumption. For every dataset D of length t-1 define

`rho_t(D)=E_D[h^*-h(A(D))]`,

`q_t(D)=E_D[sigma^2(A(D);D)]`,

`c_t(D)=E_D[U_t(D) sigma(A(D);D)]`,

`vbar_t(D)=E_D[V_t(D)]`.

These are measurable functions of D. Each expectation is well-defined: the posterior is a finite Gaussian vector, 0<=sigma<=1, U_t(D) has a finite second moment, and V_t(D) is integrable in the fixed-dataset experiment. The assumptions and Cauchy-Schwarz give

`0<=rho_t(D)<=c_t(D)+vbar_t(D)`,

`0<=q_t(D)<=1`,

`|c_t(D)|<=sqrt(zeta_t q_t(D))<=sqrt(zeta_t)`,

`vbar_t(D)<=xi_t`.

Since rho_t(D)>=0, the first inequality also implies

`vbar_t(D)>=-c_t(D)>=-sqrt(zeta_t).`

Thus both c_t(D) and vbar_t(D) are bounded, uniformly over D for each fixed t. In particular, c_t(D_t^F) and vbar_t(D_t^F) are integrable. This argument does not assert that a raw witness V_t(D_t^F) is integrable. Equivalently, one may replace V_t(D) by its deterministic fixed-dataset mean vbar_t(D); that replacement preserves the base-rule inequality and its mean bound and produces an integrable witness under any dataset mixture.

By Section 1, the conditional expected fantasy regret given D_t^F is rho_t(D_t^F), and the conditional second moment of its selected posterior standard deviation is q_t(D_t^F). Therefore

`A1 := E sum_{t=1}^T(g_t^*-g_t(x_t)) = sum_t E[rho_t(D_t^F)]`

`<= sum_t E[c_t(D_t^F)] + sum_t E[vbar_t(D_t^F)]`

`<= sum_t sqrt(zeta_t) E[sqrt(q_t(D_t^F))] + sum_t xi_t`

`<= sum_t sqrt(zeta_t) sqrt(E[q_t(D_t^F)]) + sum_t xi_t`

`<= sqrt((sum_t zeta_t)(sum_t E[q_t(D_t^F)])) + sum_t xi_t.`

The first expectation identity is also valid initially for nonnegative variables; the ensuing bounded upper bounds establish finiteness. The penultimate inequality is Jensen's inequality, and the last is Cauchy-Schwarz over the finite time index set.

The full actual dataset D_{t-1} and D_t^F contain precisely the same indexed locations, so their posterior variances agree. Setting s_t=sigma(x_t;D_{t-1}), the conditional distribution of the base-rule action gives

`E[q_t(D_t^F)] = E[sigma^2(x_t;D_t^F)] = E[s_t^2].`

Section 2 yields `sum_t s_t^2<=C1 gamma_T` pathwise. Hence

`A1 <= sqrt(C1 gamma_T sum_t zeta_t)+sum_t xi_t = B_T.`

No nonnegativity or dataset-measurability of the original auxiliary variables is required. Nor is any unconditional absolute-moment bound on the original V_t witnesses required.

## 4. Signed discrepancy and the correct posterior center

Conditional on H_t, f and g_t have the same distribution. Hence E[f^*]=E[g_t^*], and the exact decomposition is

`BCR_T=A1+A2`,

where `A2=E sum_t(g_t(x_t)-f(x_t))`.

Given H_t, the current fantasy sample, fantasy noises, and fresh base-rule randomization are independent of f. As x_t is a function of these variables,

`E[f(x_t) | H_t,g_t,(epsilon_i^(t))_i,base-rule randomness] = mu(x_t;D_{N_{t-1}}).`

It follows that

`A2 = E sum_t [g_t(x_t)-mu(x_t;D_{N_{t-1}})].`

This is an equality after conditional expectation. In particular, one must not claim a pathwise bound on `(g_t(x_t)-f(x_t))_+` using a standardized deviation of g_t alone.

## 5. Finite-set Gaussian maximum

Write m_t(x)=mu(x;D_{N_{t-1}}) and b_t(x)=sigma(x;D_{N_{t-1}}). Define Z_t(x)=(g_t(x)-m_t(x))/b_t(x) when b_t(x)>0 and Z_t(x)=0 otherwise. At a zero-variance point the residual is identically zero, so this convention preserves `g_t(x)-m_t(x)=Z_t(x)b_t(x)`.

Let `W_t=max(0,max_{x in X}Z_t(x))`. Conditional on H_t, every nondegenerate Z_t(x) is standard normal. Put n=|X|. If n=1, `E[W_t^2|H_t]` is either 1/2 or zero, and therefore is at most `2-2 log 2=C2`.

If n>=2, the elementary Gaussian survival bound follows by writing, for c>=0,

`Pr(Z>c)=exp(-c^2/2) integral_0^infinity phi(u) exp(-cu) du <= (1/2)exp(-c^2/2)`,

where phi is the standard normal density.

A union bound, requiring no spatial independence, gives for s>=0

`Pr(W_t^2>s | H_t) <= min(1,(n/2)exp(-s/2)).`

With a=2 log(n/2)>=0, tail integration yields

`E[W_t^2|H_t] <= integral_0^a 1 ds + integral_a^infinity (n/2)exp(-s/2) ds = 2+2 log(n/2)=C2.`

Thus `E[W_t^2]<=C2` in all cases. Section 4 and the definition of W_t imply

`A2 <= E sum_t W_t b_t(x_t)`

`<= sqrt((sum_t E W_t^2)(E sum_t b_t(x_t)^2))`

`<= sqrt(C2 T) sqrt(E sum_t b_t(x_t)^2).`

### Audited auxiliary upper-tail statement

The source's finite-set upper-tail lemma needs the following local endpoint correction. For nonempty X' and delta in (0,1), use `beta_delta=max(0,2 log(|X'|/(2 delta)))`. If beta_delta>0, the preceding Gaussian survival bound and union bound prove its simultaneous upper-confidence event. If beta_delta=0, the only possibility is |X'|=1 and delta>=1/2; the event at the posterior mean has probability at least 1/2, which suffices. For empty X' the simultaneous event is certain without defining beta_delta. This correction leaves the n>=2 calculation and the final C2 unchanged.

## 6. Delayed variance bound

For worker q let its assigned evaluation indices, in increasing order, be t_{q,1},...,t_{q,m_q}. The counts satisfy sum_q m_q=T, including workers with m_q=0. Because each query is assigned to an available worker, all indices t_{q,1},...,t_{q,j-1} lie in N_{t_{q,j}-1}.

Adding Gaussian observations can only decrease posterior variance: the covariance update subtracts a positive semidefinite matrix, with an invertible noisy observation covariance. Hence

`sigma^2(x_{t_{q,j}};D_{N_{t_{q,j}-1}}) <= sigma^2(x_{t_{q,j}};D_{ {t_{q,1},...,t_{q,j-1}} }).`

Section 2 applied to each worker's sequence gives, pathwise,

`sum_{t=1}^T b_t(x_t)^2 <= C1 sum_{q=1}^Q gamma_{m_q} <= C1 sum_{q=1}^Q gamma_bar(m_q).`

Concavity on [0,infinity) and sum_q m_q=T give

`sum_{q=1}^Q gamma_bar(m_q) <= Q gamma_bar(T/Q).`

The definition at zero covers unused workers, and the real-argument domain covers Q>T. Therefore

`sum_{t=1}^T b_t(x_t)^2 <= C1 Q gamma_bar(T/Q).`

## 7. Conclusion and integrability

Combining Sections 3–6 proves, for every positive integer T,

`BCR_T <= B_T + sqrt(C1 C2 Q T gamma_bar(T/Q)).`

The actual objective satisfies `E[max_{x in X}|f(x)|]<infinity` because X is finite. Conditional on H_t, g_t has the same law as f, so the nonnegative tower property gives `E[max_x|g_t(x)|]=E[max_x|f(x)|]<infinity`. Consequently the objective and fantasy regret terms and the signed discrepancy are integrable. Also, for each x, `m_t(x)=E[f(x)|H_t]` implies `E|m_t(x)|<=E|f(x)|`; summing over finite X justifies integrability at a randomly selected x_t. Section 3 integrates only bounded fixed-dataset mean functions and bounded conditional variance functions, not raw signed witnesses. Section 5 supplies the Gaussian maximum second moment, and the variance sums have deterministic bounds. These facts justify every expectation used in the proof; arbitrary raw V_t witnesses need not be integrable after mixing over datasets.

Singleton domains, zero posterior variances, repeated locations, empty initial histories, unused workers, and Q>T are included. All theorem-critical proof obligations are closed.
