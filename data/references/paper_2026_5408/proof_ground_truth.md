# Reference Proof

## Proof Structure

The proof retains four parts: limiting queue propensities, control of queue-induced pairwise dependence, negligibility of the nuisance remainder, and the oracle variance calculation. The theorem-critical obligations are: conditional randomization and residual centering; the finite-horizon workload limit and its conversion to a focal-unit propensity; bounded sensitivity of treated cell counts; all components of the centered-treatment dependence bound, including focal-cell mixing and conditional-mean shifts; the conditional L2 remainder bound; and convergence of the oracle variance with a negligible oracle-remainder covariance. Each obligation is derived below.

All calculations involving fitted regressions are conditional on the independent training sample. Conditional moments are moments under the experiment law for a fixed training realization. Almost-sure L2 membership and eventual positivity make these conditional moments finite; no moment condition over the training distribution is required. It suffices to consider `n>=max(n_0,2)`.

The standard independent tools used below are the strong law for iid integrable random variables, dominated convergence with an integrable dominating variable, the Efron–Stein inequality for a square-integrable function of independent coordinates, and the covariance form of Cauchy–Schwarz. The relevant Efron–Stein statement and the needed binomial identities are explicitly given at their uses. The iid efficiency-bound characterization is stated at the end. No specialized external dependency is needed.

## 1. Conditional randomization and the limiting propensity

Write `e_i=e_n(X_i)`, `m_z=mu_z`, and `m=mu_1-mu_0`.

Because budgets are deterministic, `D_i` is a measurable function of `(U_i,G_i)` and the other units' arrival and queue variables. The other units are independent of the focal unit. Conditional on `X_i`, queue randomization is independent of arrival and potential outcomes, and arrival is independent of the potential outcomes. Thus these design inputs are jointly conditionally independent of `(Y_i(0),Y_i(1))`, and

`D_i independent of (Y_i(0),Y_i(1)) given X_i`.

Consistency consequently identifies the conditional means and variances in the observed treatment arms with `mu_z` and `sigma_z^2` wherever positivity holds.

Let `F_t=P(U<=t)` for `t=1,...,H`, and set `F_0=0`. Continuity gives no mass at time zero, and support in `[0,H]` gives `F_H=1`. Let `N_{<=k,t,n}` count arrivals in the first `k` queues by period `t`, let `W_{<=k,t,n}` count their unserved members after that period, and put `J_{t,n}=sum_{s=1}^t B_{s,n}`, with all three quantities zero at `t=0`.

Priority and work conservation give

`W_{<=k,t,n}=(W_{<=k,t-1,n}+N_{<=k,t,n}-N_{<=k,t-1,n}-B_{t,n})_+`.

Induction therefore gives

`W_{<=k,t,n}=max_{0<=s<=t} [(N_{<=k,t,n}-N_{<=k,s,n})-(J_{t,n}-J_{s,n})]`.

For the induction, insert the formula at `t-1` into the recursion and combine increments. Taking the positive part adds exactly the term `s=t`, whose value is zero.

One may couple the experiments using the first `n` units of an infinite iid sequence, without changing any finite-experiment propensity or variance. Arrival independence and queue randomization imply

`P(G<=k,U<=t)=c_k F_t`.

The strong law applies to the bounded iid indicators defining each arrival count. Since there are finitely many `k,t`, it gives simultaneous almost-sure convergence `N_{<=k,t,n}/n -> c_k F_t`. The deterministic budget condition gives `J_{t,n}/n -> beta F_t`. Passing through the finite maximum yields

`W_{<=k,t,n}/n -> max_{0<=s<=t}(c_k-beta)(F_t-F_s)=(c_k-beta)_+ F_t`.

The last equality follows by choosing `s=0` when `c_k>=beta`, and `s=t` when `c_k<beta`. This includes `c_k=beta`. Subtracting workload from arrivals, at the terminal period the treated proportion in the first `k` queues converges to `min(beta,c_k)`.

Let `T_{k,n}` be the terminal number treated from queue `k`. Taking differences gives

`T_{k,n}/n -> min(beta,c_k)-min(beta,c_{k-1})` almost surely.

To turn this into a focal-unit propensity, fix `k` with `p_k>0`. Conditional on `X_i=x,G_i=k`, the law of the design inputs determining `D_i` does not depend on `x`: `U_i` has its unchanged marginal law, the focal queue is fixed at `k`, and all other units retain their independent marginal design laws. Thus, for almost every `x` with `rho_k(x)>0`,

`P(D_i=1 | X_i=x,G_i=k)=b_{k,n}:=P(D_i=1 | G_i=k)`.

The no-tie FIFO rule is invariant under relabeling units. Exchangeability therefore implies

`E[T_{k,n}]=sum_i P(G_i=k,D_i=1)=n p_k b_{k,n}`.

Since `0<=T_{k,n}/n<=1`, bounded convergence now gives

`b_{k,n}=E[T_{k,n}/n]/p_k -> [min(beta,c_k)-min(beta,c_{k-1})]/p_k=a_k`.

Equivalently, the focal-member treated-fraction identity is `b_{k,n}=E[T_{k,n}/N_{k,n} | G_i=k]`, where `N_{k,n}` is the queue size. The conditioning is essential: under it the denominator is positive, and the expectation is not the unconditional expectation of the random queue fraction.

If `p_k=0`, nonnegativity of `rho_k` implies `rho_k(X)=0` almost surely, so that queue makes no contribution. Mixing over the focal queue gives, on one common full-measure covariate set,

`e_n(x)=sum_{k:p_k>0} rho_k(x)b_{k,n} -> sum_k rho_k(x)a_k=e_infty(x)`.

Taking the intersection of the positivity sets for the countably many `n>=n_0` also shows `gamma<=e_infty(X)<=1-gamma` almost surely. This is a consequence, not an additional assumption.

## 2. Queue-induced pairwise dependence

We prove that there is a finite constant `C`, depending only on the fixed cell probabilities and on `K,H`, such that for all `n>=2` and distinct `i,j`,

`|E[(D_i-e_n(X_i))(D_j-e_n(X_j)) | X_i,X_j]| <= C/n` almost surely.

### 2.1 Cell counts and bounded sensitivity

Let `S_i` be the first allocation period by which unit `i` has arrived, and let `C_i=(G_i,S_i)`. Thus `S_i=s` corresponds almost surely to `s-1<U_i<=s`; integer endpoints have probability zero. There are `M=KH` possible cells. Write `r_s=P(S=s)` and `lambda_(k,s)=p_k r_s`.

For a cell `c=(k,s)`, let `W_{c,t}` be its waiting count immediately before allocation at `t`, let `A^{new}_{c,t}` be its newly eligible count at that period, and let `J_{c,t}` be its newly served count. For `s>t` these waiting and service counts are zero. Eligible cells are served in lexicographic order, first by queue and then by arrival period. If `c' precedes c` denotes this order among eligible cells, then

`J_{c,t}=(B_{t,n}-sum_{c' precedes c}W_{c',t})_+ -(B_{t,n}-sum_{c' precedes c}W_{c',t}-W_{c,t})_+`.

Together with

`W_{c,t+1}=W_{c,t}-J_{c,t}+A^{new}_{c,t+1}`,

this proves that the terminal treated count `T_c=sum_t J_{c,t}` is determined by the cell-count vector, not by the within-cell ordering of unit labels.

Compare two systems differing in one unit's queue-arrival coordinate, while keeping the deterministic budgets unchanged. Let `Delta_t=sum_c |W_{c,t}-W'_{c,t}|`. Initially `Delta_1<=2`. The positive-part function is 1-Lipschitz, so the displayed service formula gives

`|J_{c,t}-J'_{c,t}|<=2 Delta_t`.

A single changed unit changes a new-arrival count vector by total absolute discrepancy at most two. Therefore

`Delta_{t+1}<=(1+2M)Delta_t+2`.

Induction gives `Delta_t<=2 sum_{h=0}^{t-1}(1+2M)^h`. With

`L=4H sum_{h=0}^{H-1}(1+2M)^h`,

we obtain, for every cell,

`|T_c-T'_c|<=sum_{t=1}^H |J_{c,t}-J'_{c,t}|<=L`.

This bound is independent of `n`, budgets, and the replaced coordinate. Also, replacing a coordinate changes any cell size by at most one.

### 2.2 Within-cell sampling and reciprocal counts

Restrict attention to cells with `lambda_c>0`, and define their smallest probability as `lambda_min>0`. At least one such cell exists, and there are finitely many. For almost every covariate value `x`, the conditional cell probabilities

`w_(k,s)(x)=rho_k(x)r_s`

are supported on these positive-probability cells. Indeed, a zero-probability arrival period is never selected, and `p_k=0` implies `rho_k(X)=0` almost surely.

Conditional on `X_i,X_j,C^n`, arrivals within each cell are iid from the continuous arrival law restricted to that period. Their ranks are uniform, and orders in distinct cells are independent. Cell totals `T_c` are already fixed by `C^n`. FIFO selects the earliest `T_c` members of each cell, so their labels form a uniform subset of that size. Write `q_c=T_c/N_c` whenever `N_c>0`. Then

`E[D_i | X_i,X_j,C^n]=q_{C_i}`.

The conditional covariance of the two selections is zero for different cells. If both focal units occupy `c`, it equals

`-q_c(1-q_c)/(N_c-1)`.

For a positive-probability cell and `B~Bin(n-2,lambda_c)`, the elementary integral identity `1/(b+1)=integral_0^1 t^b dt` gives

`E[1/(B+1)]=[1-(1-lambda_c)^(n-1)]/[(n-1)lambda_c] <= 1/[(n-1)lambda_c]`.

We will also need

`E[1/(B+1)^2] <= 2 E[1/((B+1)(B+2))] <= 2/[n(n-1)lambda_c^2]`.

For the second inequality, use `1/((b+1)(b+2))=integral_0^1 t^b(1-t)dt` and substitute `u=1-lambda_c+lambda_c t`. The expectation is

`lambda_c^(-2) integral_(1-lambda_c)^1 u^(n-2)(1-u)du <= lambda_c^(-2) integral_0^1 u^(n-2)(1-u)du =1/[n(n-1)lambda_c^2]`.

These formulas also cover `n=2` and `lambda_c=1`. When both focal units occupy `c`, `N_c=2+B`. Averaging the within-cell covariance therefore gives

`|E[Cov(D_i,D_j | X_i,X_j,C^n) | X_i,X_j]| <= 1/[4(n-1)lambda_min]`.

### 2.3 Random treated fractions with focal cells fixed

Fix focal cells `C_i=c,C_j=d`, and let `V=(C_m:m!=i,j)` be the remaining coordinates. Conditional on the focal covariates and cells, the coordinates of `V` are independent with their original cell probabilities `lambda`. The fractions `q_c(V)` and `q_d(V)` lie in `[0,1]` and their denominators are positive because the corresponding focal members remain present.

If one nonfocal coordinate is replaced by an independent copy, the preceding sensitivity and count bounds imply

`|q_c(V)-q_c(V^(r))| <= (L+1)/N_c(V)`.

Indeed, subtract the fractions, use `|T_c-T'_c|<=L`, `|N_c-N'_c|<=1`, and `T'_c<=N'_c`. Since `N_c(V)>=1+B` with `B~Bin(n-2,lambda_c)`, the reciprocal-square bound gives

`E[(q_c(V)-q_c(V^(r)))^2 | X_i,X_j,C_i=c,C_j=d] <= 2(L+1)^2/[n(n-1)lambda_min^2]`.

For independent coordinates and square-integrable `f`, Efron–Stein states

`Var(f(V)) <= (1/2) sum_r E[(f(V)-f(V^(r)))^2]`.

Its independence and integrability hypotheses hold here, including the empty-coordinate case `n=2`. Consequently

`Var(q_c | X_i,X_j,C_i=c,C_j=d) <= (L+1)^2/[n lambda_min^2]`.

The same bound holds for `q_d`, so Cauchy–Schwarz bounds their conditional covariance by

`v_n=(L+1)^2/[n lambda_min^2]`.

### 2.4 Mixing over focal cells

The preceding bound alone does not control the covariance after the focal cells are mixed out: a focal unit's own cell can change its treatment probability by order one. We therefore control only the influence of the other focal cell and retain the independence of the two focal cells.

For positive-probability cells `c,d`, define

`A_cd=E_V[q_c(c,d,V)]`, `B_cd=E_V[q_d(c,d,V)]`.

These are defined by inserting focal cells `c,d` and integrating the independent remaining cell coordinates. They do not depend on the numerical focal covariate values. Holding `c,V` fixed and changing only `d` changes the fraction for cell `c` by at most `(L+1)/(1+B)`, where `B` counts nonfocal members of `c`. Hence

`sup_(d,d') |A_cd-A_cd'| <= h_n`,

where `h_n=(L+1)/[(n-1)lambda_min]`. Similarly,

`sup_(c,c') |B_cd-B_c'd| <= h_n`.

Now fix `X_i=x,X_j=y`. Under this conditioning the focal cells are independent, with probabilities `w_c(x)` and `w_d(y)`. Set

`Abar_c=sum_d w_d(y)A_cd`, `Bbar_d=sum_c w_c(x)B_cd`.

Then `Cov(Abar_(C_i),Bbar_(C_j) | X_i,X_j)=0`. The differences `A_(C_i,C_j)-Abar_(C_i)` and `B_(C_i,C_j)-Bbar_(C_j)` are centered under this conditioning and have absolute values at most `h_n`. Since both averaged fractions lie in `[0,1]`, expansion of the covariance gives

`|Cov(A_(C_i,C_j),B_(C_i,C_j) | X_i,X_j)| <= 2h_n+h_n^2`.

Combining the two successive total-covariance decompositions with the within-cell and fixed-focal-cell bounds gives

`|Cov(D_i,D_j | X_i,X_j)| <= 1/[4(n-1)lambda_min]+v_n+2h_n+h_n^2`.

### 2.5 Correct centering by marginal propensities

It remains to compare the conditional mean given both covariates with the propensity conditioned on only the focal covariate. The definitions above give

`E[D_i | X_i=x,X_j=y]=sum_c w_c(x) sum_d w_d(y)A_cd`,

whereas

`e_n(x)=sum_c w_c(x) sum_d lambda_d A_cd`.

For each fixed `c`, subtract `Atilde_c=sum_d lambda_d A_cd` inside the difference. The coefficients sum to zero, the total absolute difference between two probability vectors is at most two, and `|A_cd-Atilde_c|<=h_n`. Thus

`|E[D_i | X_i,X_j]-e_n(X_i)|<=2h_n`.

The same estimate holds for unit `j`. Finally,

`E[(D_i-e_n(X_i))(D_j-e_n(X_j)) | X_i,X_j]`

`=Cov(D_i,D_j | X_i,X_j) + (E[D_i | X_i,X_j]-e_n(X_i))(E[D_j | X_i,X_j]-e_n(X_j))`.

Its absolute value is at most

`1/[4(n-1)lambda_min]+v_n+2h_n+5h_n^2 <= C/n`.

The last inequality holds for every `n>=2` after choosing a finite constant depending only on `L,lambda_min`. This closes every component of the pairwise centered-treatment bound, uniformly over focal covariates outside a null set.

## 3. The nuisance remainder

Let `delta_z=hat mu_z-mu_z`, and define

`g(x)=delta_1(x)/e_n(x)+delta_0(x)/(1-e_n(x))`.

Set

`xi_(i,n)=m(X_i)-tau + D_i{Y_i(1)-mu_1(X_i)}/e_i -(1-D_i){Y_i(0)-mu_0(X_i)}/(1-e_i)`.

Direct substitution into the estimator gives

`hat tau_n=tau+n^(-1)sum_i xi_(i,n)-R_n`,

where

`R_n=n^(-1)sum_i (D_i-e_i)g(X_i)`.

Since training is independent of the experiment and `E[D_i-e_i | X_i]=0`, we have `E[R_n | T]=0`. Let `E_T` denote expectation over the experiment with the fitted functions fixed. Positivity gives

`E_T[g(X)^2] <= (2/gamma^2)(||delta_1||_2^2+||delta_0||_2^2)=o_P(1)`.

Expanding the scaled variance,

`n Var(R_n | T) = (1/n)sum_i E_T[(D_i-e_i)^2 g(X_i)^2] +(1/n)sum_(i!=j) E_T[(D_i-e_i)(D_j-e_j)g(X_i)g(X_j)]`.

The aggregate diagonal contribution is at most `E_T[g(X)^2]`, not `n^(-1)E_T[g(X)^2]`. For the off-diagonal contribution, condition on the two covariates and apply the bound proved in Section 2. Conditional on training, `X_i,X_j` remain independent with law `P_X`, so

`(1/n)sum_(i!=j) |E_T[(D_i-e_i)(D_j-e_j)g(X_i)g(X_j)]|`

`<= C(n-1)/n (E_T|g(X)|)^2 <= C E_T[g(X)^2]`.

Therefore

`n Var(R_n | T) <= (1+C)E_T[g(X)^2]=o_P(1)`.

No convergence rate stronger than the stated L2 consistency is used.

## 4. Oracle variance and conclusion

Let `epsilon_(i,z)=Y_i(z)-mu_z(X_i)` and let `H_n` be the sigma-field generated by all covariates, arrivals, and queue assignments. Given `H_n`, treatments are fixed. Moreover, by iid sampling, arrival exogeneity conditional on covariates, and independent queue randomization, the potential-outcome pairs are independent across units conditional on `H_n`, and each has its conditional law given `X_i`. In particular,

`E[epsilon_(i,z) | H_n]=0`.

This verifies conditional independence directly from the product experiment; it does not infer conditional independence merely from unconditional independence.

It follows that `E[xi_(i,n)]=0`. For `i!=j`, every cross-product containing an outcome residual vanishes after conditioning on `H_n`, and

`E[xi_(i,n)xi_(j,n) | H_n]=(m(X_i)-tau)(m(X_j)-tau)`.

The expectation of the right-hand side is zero by independence of the covariates. Thus the oracle summands have exactly zero cross-unit covariances.

For a diagonal term, conditional randomization gives the conditional second moments of the residuals in their respective arms. Their product within a unit is multiplied by `D_i(1-D_i)=0`, and their cross-products with `m(X_i)-tau` have expectation zero. Consequently

`Var(xi_(i,n))=E[sigma_1^2(X)/e_n(X)+sigma_0^2(X)/(1-e_n(X))]+Var(m(X))=:V_n`.

The second-moment assumption and conditional Jensen inequality imply that `sigma_z^2` is integrable and `m` is square-integrable. By Section 1, the propensities converge on a common full-measure set and both their finite-sample and limiting values lie in `[gamma,1-gamma]`. The variance integrands are dominated by `(sigma_1^2+sigma_0^2)/gamma`. Dominated convergence therefore gives

`V_n -> E[sigma_1^2(X)/e_infty(X)+sigma_0^2(X)/(1-e_infty(X))]+Var(m(X))=:V<infinity`.

The oracle term is independent of training, so its exact scaled conditional variance is

`n Var(n^(-1)sum_i xi_(i,n) | T)=V_n`.

Cauchy–Schwarz and Section 3 imply

`n |Cov(n^(-1)sum_i xi_(i,n),R_n | T)| <= sqrt(V_n) sqrt(n Var(R_n | T))=o_P(1)`.

Equivalently,

`|n Var(hat tau_n | T)-V_n| <= n Var(R_n | T)+2 sqrt(V_n n Var(R_n | T)) ->_P 0`.

Combining this with `V_n->V` proves the target. This argument also covers `V=0`; no strict positivity of the limiting variance or conditional outcome variances is needed.

For completeness, the standard independent iid comparison result used here is the following: for iid observed triples `(X,D,Y)` with consistency, conditionally randomized treatment with propensity `e(X)` bounded away from zero and one, and square-integrable potential outcomes, the ATE efficient influence function in the ordinary nonparametric observed-data model is

`mu_1(X)-mu_0(X)-tau + D{Y-mu_1(X)}/e(X) -(1-D){Y-mu_0(X)}/(1-e(X))`.

Its variance, and hence the iid ATE efficiency bound, is

`E[sigma_1^2(X)/e(X)+sigma_0^2(X)/(1-e(X))]+Var(mu_1(X)-mu_0(X))`.

This is the standard-independent comparison recorded in theory_024 and invoked in the source. Taking an iid benchmark with the same covariate and potential-outcome law and propensity `e=e_infty` verifies all its hypotheses by the moment assumption and the inherited positivity proved above. Its bound is exactly `V`. The conclusion is equality with this iid benchmark, not an additional lower-bound theorem for the dependent queue experiment.
