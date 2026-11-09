# Reference Proof

## Proof Structure

First, exhibit a continuum of independent Gaussian latent/noise decompositions having the same marginal predictive law. Second, condition the privileged-supervision risk on the query-context pair, identify the two conditional minimizers, and establish that their jointly attainable finite-risk pair forces every population minimizer to agree with them almost everywhere.

## Complete Proof

The background variance identity applies at pairs for which the specified posterior predictive second moment is finite. Within that fixed conditional experiment, the law of total variance applied to the task gives the stated identity. The finite-second-moment qualification verifies the hypothesis of that standard result; it is not used as a global assumption in the auxiliary-risk argument.

For the first claim, fix `(x_*,D)` and suppose the marginal predictive law is `N(m,s^2)` with `s^2>0`. For any `a` with `0<a<s^2`, let `F_*` and `epsilon_*` be independent, with `F_*~N(m,a)` and `epsilon_*~N(0,s^2-a)`, and set `Y_*=F_*+epsilon_*`. Both component variances are positive. The sum of independent Gaussian variables is Gaussian, with mean `m` and variance `a+(s^2-a)=s^2`; hence `Y_*~N(m,s^2)`. Distinct values of `a` give distinct latent and residual variances while preserving the same marginal law. Thus the marginal posterior predictive cannot determine a unique epistemic--aleatoric split. This is a pointwise compatibility statement and does not require the alternatives to share a fixed task prior or form one decomposition across all query-context pairs.

For the second claim, write `Z=(x_*,D)`, `F_*=f_T(x_*)`, `S_*=sigma_T^2(x_*)`, `J=B(F_*)`, and `L=log S_*`. The containing-bin convention makes `J` a measurable random variable with values in `{1,...,K}`. Define `p_j(Z)=P(J=j|Z)` and `mu(Z)=E[L|Z]`, using measurable versions. Since `L` is square-integrable, `mu` is square-integrable and finite almost surely. On any exceptional null set, choose an arbitrary categorical vector and an arbitrary finite value of `mu`.

For a categorical head `q(Z)=pi^(f)(Z)` and `h(Z)=log sigma_hat^2(Z)`, conditioning the objective on `Z` gives

`lambda_f E[-log q_J(Z)|Z] + lambda_sigma E[(h(Z)-L)^2|Z]`.

For each conditioning value where these conditional quantities are defined, the categorical risk is

`-sum_j p_j log q_j = H(p)+D_KL(p||q)`.

Here `H(p)=-sum_j p_j log p_j`, zero-weight terms are zero, and a positive `p_j` paired with `q_j=0` gives infinite risk. Gibbs' inequality gives `D_KL(p||q)>=0`, with equality exactly when `q=p`. This remains true when some `p_j` are zero: equality requires matching all positive coordinates, and their total mass is already one, leaving zero mass for every other coordinate. Thus the unique minimizing categorical vector is `p`.

For the log-variance head, conditional-mean orthogonality gives

`E[(h-L)^2|Z] = Var(L|Z)+(h-mu)^2`

whenever the squared risk is finite. Thus the unique conditional minimizer is `h=mu`, and its corresponding positive variance is `exp(mu)`.

To justify the conclusion for every population minimizer, rather than only describe pointwise minimizers, use joint model richness to realize the pair `(p,exp(mu))`. This pair has finite risk: `0<=H(p)<=log K` and `E[(mu-L)^2]<=E[L^2]<infinity`. Consequently any population minimizer also has finite risk. For such a minimizer, `h` is square-integrable because

`h^2 <= 2(h-L)^2+2L^2`.

Taking expectations in the preceding decompositions therefore yields the excess-risk identity

`R(q,h)-R(p,mu) = lambda_f E[D_KL(p||q)] + lambda_sigma E[(h-mu)^2]`.

Both summands are nonnegative and both weights are strictly positive. A population minimizer must make both expectations zero. Hence `q=p` and `h=mu` almost surely. Since there are only finitely many bins, the equalities for all coordinates hold on one common set of full probability.

Therefore, for almost every `(x_*,D)`, every population minimizer satisfies

`pi_j^(f)(x_*,D)=P(B(F_*)=j|x_*,D)` for every `j`,

and

`log sigma_hat^2(x_*,D)=E[log S_*|x_*,D]`.

Exponentiating gives `sigma_hat^2=exp(E[log S_*|x_*,D])`. The latent head recovers the conditional law of the discretized clean signal, while the variance head is the Bayes-optimal predictor under squared log-variance loss. This is a conditional geometric-mean summary, not a claim that the head equals `E[S_*|x_*,D]`. The proof concerns only the stated auxiliary risk; it does not establish the same minimizers for a risk that also contains an observation-predictive loss.
