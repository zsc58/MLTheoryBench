# Reference Proof

## Proof structure and obligations

We verify definition closure, exponential likelihood separation, local existence and control of the tilt, a subexponential denominator lower bound, both posterior concentration assertions, predictive Wasserstein consistency, and the realized and expected oracle-growth limits. The final step also establishes the almost-sure realized variant under its stated additional hypothesis.

All probabilities and expectations below refer to the true IID sampling law unless another measure is specified. Constants in the posterior argument may depend on the true variance and the prior's positive lower bound and neighborhood, but not on the sample size or the candidate mean. Constants in the betting argument may depend on the fixed candidate mean and c.

## 1. Definition closure

Write A_{n,mu}(g)=integral exp{g(z-mu)}P_{n,mu}(dz). For every finite g this is finite and strictly positive. Its log derivative is the tilted mean minus mu, and its second derivative is the tilted variance. If tau_n>0, the base measure has support convex hull [0,1], so for every mu in (0,1) its tilted mean is strictly increasing from 0 to 1 as g runs from minus infinity to infinity. Consequently there is a unique finite root. If tau_n=0, the same argument applies precisely when min_i X_i<mu<max_i X_i. The other points receive zero likelihood as specified in the task.

Because H_mu is a Borel probability kernel, the integrals and their derivatives are jointly measurable in the data, mu, and g. On the fitting domain the unique root is measurable: its comparisons with rational numbers are determined by the signs of the increasing log-normalizer derivative. The prescribed extensions therefore make gamma, the likelihood, the posterior, and the predictive measurable. In particular Q_{n+1|n} is F_n-measurable. The fixed initial predictive supplies the n=1 betting rule.

On the fitting domain the empirical-component weights are positive and sum to at most one. Arithmetic-geometric mean gives

\[
0\le L_n(\mu)=\prod_{i=1}^n n w_{n,i}(\mu)\le\left(\sum_{i=1}^n w_{n,i}(\mu)\right)^n\le1.
\]

Thus the denominator D_n=integral L_n(mu)pi(mu)dmu lies in [0,1]. The task explicitly defines a posterior and predictive also when D_n=0. We will show that this event has probability tending to zero; no assumption of finite-sample positivity is needed.

## 2. Exponential separation

Fix a fitted mu. Let a=sum_i w_{n,i}>0 and p_i=w_{n,i}/a. With m_p=sum_i p_i X_i, the fitted mean constraint gives

\[
\mu=a m_p+(1-a)m_H
\]

for some m_H in [0,1]; when a=1 its choice is irrelevant. Hence |mu-m_p|<=1-a. If u_i=1/n, then

\[
\log L_n(\mu)=n\log a-n\operatorname{KL}(u\|p).
\]

Suppose |mu-bar X_n|>=t, where 0<t<=1. If 1-a>=t/2, then log L_n<=n log(1-t/2). Otherwise |m_p-bar X_n|>=t/2. For probability vectors on the labelled observations,

\[
|m_p-\bar X_n|\le\operatorname{TV}(p,u),\qquad
\operatorname{TV}(p,u)=\frac12\sum_i|p_i-u_i|.
\]

Pinsker's inequality, in the form KL(u||p)>=2 TV(u,p)^2, applies to these probability vectors and gives log L_n<=-nt^2/2. Zero-likelihood points satisfy the same bound automatically. Therefore

\[
\sup_{|\mu-\bar X_n|\ge t}L_n(\mu)\le e^{-n c(t)},\qquad
c(t)=\min\{-\log(1-t/2),t^2/2\}>0.
\]

## 3. Local tilt control and denominator positivity

Let psi_{n,mu}(g)=log A_{n,mu}(g). For h_mu=integral z H_mu(dz),

\[
|\psi'_{n,\mu}(0)|
=\left|\frac{n\bar X_n+\tau_n h_\mu}{n+\tau_n}-\mu\right|
\le |\bar X_n-\mu|+\frac{\tau_n}{n+\tau_n}.
\]

Fix v_0>0 and suppose s_n^2>=v_0. Mixture variance decomposition gives psi''_{n,mu}(0)>=n s_n^2/(n+tau_n), which is at least v_0/2 for all sufficiently large n. For |g|<=1, the tilted density relative to P_{n,mu} is at least e^{-2}. Using the pairwise representation of variance therefore gives

\[
\psi''_{n,\mu}(g)
\ge e^{-4}\operatorname{Var}_{P_{n,\mu}}(Z)
\ge e^{-4}v_0/2=:k_0>0.
\]

Choose eta>0 with eta<k_0/4. For all sufficiently large n, tau_n/n<k_0/4. Whenever |mu-bar X_n|<=eta, we have |psi'_{n,mu}(0)|<k_0/2. Integrating the curvature bound to -1 and 1 shows psi'_{n,mu}(-1)<0<psi'_{n,mu}(1). Thus a root exists in (-1,1), and the mean-value theorem yields

\[
|\gamma_{n,\mu}|\le C\left(|\mu-\bar X_n|+\frac{\tau_n}{n}\right),\qquad C=k_0^{-1}.
\]

This argument also proves local feasibility; in the unregularized case a finite root for a nondegenerate empirical law implies that mu is strictly inside its empirical convex hull. All bounds are uniform over mu and require no continuity of H_mu in mu.

By the strong law for the bounded IID variables X_i and X_i^2, bar X_n tends to mu* and s_n^2 tends to sigma^2 almost surely. Let a_0>0 and r>0 be the public prior lower-bound constants. With probability tending to one, s_n^2>=sigma^2/2 and

\[
B_n=[\bar X_n-1/n,\bar X_n+1/n]
\subset(\mu^*-r,\mu^*+r)\subset(0,1).
\]

For all sufficiently large n the preceding local argument ensures feasibility throughout B_n and

\[
\sup_{\mu\in B_n}|\gamma_{n,\mu}|\le C(1+\tau_n)/n.
\]

For a fitted mu, bounded support gives

\[
nw_{n,i}(\mu)
\ge\frac{n}{n+\tau_n}e^{-2|\gamma_{n,\mu}|}.
\]

Using n log(1+tau_n/n)<=tau_n, uniformly on B_n we obtain

\[
L_n(\mu)\ge\exp\{-C_1(1+\tau_n)\}.
\]

Consequently, on an event whose probability tends to one,

\[
D_n\ge\frac{2a_0}{n}\exp\{-C_1(1+\tau_n)\}>0.
\]

In particular P(D_n=0) tends to zero, and the denominator is subexponential because tau_n=o(n). Together with D_n<=1 this also gives log D_n=o_P(n), interpreting log 0 as minus infinity on the exceptional event.

## 4. Posterior concentration and vanishing tilt

For 0<epsilon<=1, on the event |bar X_n-mu*|<=epsilon/2,

\[
\int_{|\mu-\mu^*|>\varepsilon}L_n(\mu)\pi(\mu)d\mu
\le e^{-n c(\varepsilon/2)}.
\]

Combining this with the denominator lower bound gives, on an event of probability tending to one,

\[
\Pi_n(|\mu-\mu^*|>\varepsilon)
\le\frac{n}{2a_0}\exp\{-n c(\varepsilon/2)+C_1(1+\tau_n)\}\longrightarrow0.
\]

For epsilon>1 the set is empty. Thus the first assertion holds, including under the specified posterior completion on D_n=0.

Next fix epsilon>0. Use the local tilt constants with v_0=sigma^2/2 and choose 0<rho<eta such that C rho<epsilon/2. For sufficiently large n, on the event s_n^2>=v_0,

\[
|\mu-\bar X_n|\le\rho\quad\Longrightarrow\quad
|\gamma_{n,\mu}|<\varepsilon.
\]

On D_n>0 the posterior assigns zero mass to nonfitting points. Moreover,

\[
\Pi_n(|\mu-\bar X_n|>\rho)
\le\Pi_n(|\mu-\mu^*|>\rho/2)
+\mathbf1\{|\bar X_n-\mu^*|>\rho/2\}.
\]

The right side tends to zero in probability. The events D_n=0 and s_n^2<v_0 also have probabilities tending to zero. Hence Pi_n(|gamma_{n,mu}|>epsilon) tends to zero in probability.

## 5. Predictive Wasserstein consistency

The standard Kantorovich-Rubinstein duality states that, for probability measures on [0,1], W_1 is the supremum of differences of integrals over real 1-Lipschitz functions. Such functions can be normalized by f(0)=0, in which case |f|<=1. All measures here have bounded support, so the finite-first-moment hypothesis is automatic.

For fitted mu, write the tilted distribution as its labelled empirical component plus its tilted regularizer component, with regularizer weight w_{n,H}. Duality gives

\[
W_1(\widetilde P_{n,\mu},P_n)
\le\sum_i|w_{n,i}(\mu)-1/n|+w_{n,H}.
\]

If g=gamma_{n,mu}, then w_{n,H}<=(tau_n/n)e^{2|g|}. Regard the empirical weights as functions of g. Differentiation gives

\[
w'_{n,i}(g)=w_{n,i}(g)\{X_i-\mu-m(g)\},
\]

where m(g) is the tilted expectation of Z-mu and belongs to [-1,1]. Since sum_i w_{n,i}(g)<=1, we have sum_i |w'_{n,i}(g)|<=2. Also w_{n,i}(0)=1/(n+tau_n). Therefore

\[
W_1(\widetilde P_{n,\mu},P_n)
\le 2|\gamma_{n,\mu}|+\frac{\tau_n}{n+\tau_n}
+\frac{\tau_n}{n}e^{2|\gamma_{n,\mu}|}.
\]

It is essential not to integrate the unbounded right-hand side without controlling its tails. Since W_1<=1 for probability measures on [0,1], for each fixed delta>0, on D_n>0,

\[
\int W_1(\widetilde P_{n,\mu},P_n)\Pi_n(d\mu)
\le 2\delta+\frac{\tau_n}{n+\tau_n}
+\frac{\tau_n}{n}e^{2\delta}
+\Pi_n(|\gamma_{n,\mu}|>\delta).
\]

For any desired positive tolerance, first choose delta sufficiently small and then let n tend to infinity. The preceding posterior result and tau_n/n tending to zero show that this integral tends to zero in probability. The event D_n=0 is negligible and all distances remain bounded by one there.

Duality also yields convexity under probability mixtures, so

\[
W_1(Q_{n+1\mid n},P^*)
\le W_1(P_n,P^*)+
\int W_1(\widetilde P_{n,\mu},P_n)\Pi_n(d\mu).
\]

The standard empirical-measure result used here is that an IID empirical measure converges weakly almost surely to its sampling law, and on a compact metric space this implies W_1 convergence. Its hypotheses hold on [0,1]. Thus W_1(P_n,P*) tends to zero almost surely, proving the requested predictive convergence in probability.

## 6. Oracle log-growth

Fix a candidate mu in (0,1). Define

\[
f_\lambda(x)=\log(1+\lambda(x-\mu)),\qquad
M_n(\lambda)=\int f_\lambda(x)Q_{n\mid n-1}(dx).
\]

On the compact set I_{mu,c} times [0,1], every factor is at least 1-c>0. Thus f_lambda is jointly continuous and bounded in absolute value by a finite constant B_{mu,c}. Its derivative in x has absolute value at most

\[
K_{\mu,c}=\frac{c}{(1-c)\min\{\mu,1-\mu\}}.
\]

The predictive result, shifted by one time index, and duality give

\[
Z_n:=\sup_{\lambda\in I_{\mu,c}}|M_n(\lambda)-M(\lambda,\mu)|
\le K_{\mu,c}W_1(Q_{n\mid n-1},P^*)\longrightarrow0
\]

in probability. The arbitrary fixed initialization does not affect this limit.

The function M is continuous on the compact coefficient interval. For distinct coefficients, strict concavity of the logarithm is strict whenever X is not equal to mu; this event has positive probability because sigma^2>0. Hence M is strictly concave and has a unique maximizer lambda*(mu).

For any epsilon>0, let A_epsilon consist of the coefficients at distance at least epsilon from lambda*. If this set is empty there is nothing to prove. Otherwise compactness and uniqueness give

\[
\Delta_\varepsilon=M(\lambda^*,\mu)-\sup_{\lambda\in A_\varepsilon}M(\lambda,\mu)>0.
\]

The maximality of the selected coefficient for M_n implies

\[
0\le M(\lambda^*,\mu)-M(\widehat\lambda_n,\mu)\le2Z_n.
\]

Therefore P(|lambda_hat_n-lambda*|>=epsilon)<=P(2Z_n>=Delta_epsilon), which tends to zero.

Set Y_n=f_{lambda_hat_n}(X_n). Independence of X_n from F_{n-1} and measurability of lambda_hat_n give the true conditional expectation

\[
\mathbb E[Y_n\mid\mathcal F_{n-1}]=M(\widehat\lambda_n,\mu),
\]

not M_n(lambda_hat_n). The differences D'_n=Y_n-M(lambda_hat_n,mu) are martingale differences bounded by 2B_{mu,c}. The martingale strong law used here states that square-integrable martingale differences with sum_n E[(D'_n)^2|F_{n-1}]/n^2 finite almost surely have n^{-1}sum_{i<=n}D'_i tending to zero almost surely. In this case the sum is bounded by 4B_{mu,c}^2 sum_n n^{-2}, so its hypothesis is verified.

Continuity and boundedness of M, together with coefficient convergence in probability, imply

\[
\mathbb E|M(\widehat\lambda_n,\mu)-M(\lambda^*,\mu)|\longrightarrow0.
\]

Indeed, convergence in probability plus a uniform bound implies L1 convergence. Consequently,

\[
\mathbb E\left|\frac1n\sum_{i=1}^nM(\widehat\lambda_i,\mu)-M(\lambda^*,\mu)\right|
\le\frac1n\sum_{i=1}^n\mathbb E|M(\widehat\lambda_i,\mu)-M(\lambda^*,\mu)|\longrightarrow0.
\]

Using

\[
\frac1n\log W_n(\mu)=\frac1n\sum_{i=1}^nM(\widehat\lambda_i,\mu)+\frac1n\sum_{i=1}^nD'_i
\]

proves the realized convergence in probability. Taking expectations directly gives

\[
\frac1n\mathbb E\log W_n(\mu)
=\frac1n\sum_{i=1}^n\mathbb E M(\widehat\lambda_i,\mu)
\longrightarrow M(\lambda^*,\mu).
\]

Finally, under almost-sure predictive Wasserstein convergence, Z_n tends to zero almost surely. The same separation argument gives almost-sure coefficient convergence, and ordinary pathwise Cesaro averaging gives almost-sure convergence of the average true conditional means. The martingale strong law then gives the almost-sure realized normalized log-wealth limit.

All theorem-critical obligations are closed. No nonstandard external dependency is required.
