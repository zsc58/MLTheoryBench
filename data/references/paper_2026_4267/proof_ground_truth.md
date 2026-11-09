# Reference Proof

## Contract and obligations

The upper experiment has uncorrupted random covariates and additive sparse response contamination. Its noise is independent of the design. The lower experiment separately permits arbitrary contaminated design-response pairs. Its clean errors, but not necessarily its covariates, are Gaussian. The lower minimax infimum is over measurable estimators of the observed sample, not over procedures supplied with the unknown coefficient or outlier set.

The proof obligations are: (1) a simultaneous design/score event with the stated failure probability; (2) initialization, integer-valued sparsity control, threshold feasibility, and both first-stage rates; (3) fixed-threshold sparsity and fallback, beta-min refinement, and absorption of the transient after a uniform constant times log n steps; (4) an uncontaminated lower bound with a sufficient numerical constant; and (5) the contamination coupling and transfer to the fixed-count experiment. Each obligation is closed below.

## 1. Independent concentration tools and their application

The standard sample-covariance inequality used in the source has the following form. For r independent centered sub-Gaussian rows in dimension d, with the sub-Gaussian parameter and covariance norm bounded in terms of M, there is a constant K(M) such that, for u>0, the covariance deviation is at most max{iota,iota^2} with failure probability at most 2 exp(-u), where iota=K(M)(sqrt(d/r)+sqrt(u/r)). It applies to every fixed column restriction of the source design: independence and the scalar moment-generating-function bounds on the standardized coordinates give the required bound on every linear functional. It also applies to every fixed row-column block.

Apply this inequality and a union bound over column supports, choosing u to dominate their logarithmic count. Weyl's inequality then gives restricted sample eigenvalues in [1/(2M),2M]. For blocks, apply it with the number of selected rows as r and choose u to dominate both support counts. Taking square roots of the resulting Gram-matrix bound gives a uniform block operator bound. Noninteger support budgets mean integer sizes not exceeding the budget; if a budget exceeds the ambient dimension, use all available coordinates. These conventions also cover empty blocks.

Write Q=s log p+o log n, d=kappa-delta, B=((kappa+delta)/d)^2, A=sqrt(B)+1=2kappa/d, and f=C_M sqrt(Q/n). Choose C_M depending only on M sufficiently large for these block estimates. Then choose C_0 depending only on M,eta,kappa sufficiently large. In particular, it can cover covariance supports through (2B+2)s, block supports through (B+1)s and (B+1)o, and the smallness conditions used below. The resulting design event has failure probability O(p^-2) and satisfies

- all the specified restricted sample eigenvalues lie in [1/(2M),2M];
- ||X_{O,S}||_op/sqrt(n)<=A f whenever |S|<=(B+1)s and |O|<=(B+1)o.

The enlargement from (2B+1)s to (2B+2)s only handles integer rounding in a sparsity contradiction. It changes the sufficiently large sample-size constant, not the sample-size order or algorithm.

For a centered random vector v with E exp(a^T v)<=exp(sigma^2||a||_2^2/2), the standard quadratic-form inequality used in the source states that, for deterministic D and u>0,

P{||Dv||_2^2>sigma^2[tr(DD^T)+2||DD^T||_F sqrt(u)+2||DD^T||_op u]}<=exp(-u).

Condition on X; independence of xi from X verifies this inequality's hypothesis. Apply it to D=X_{S*}^T/n, where S*=supp(beta*) is fixed and has size s. On the design event, tr(X_{S*}^T X_{S*}/n)<=2Ms, its squared Frobenius norm is at most 4M^2s, and its operator norm is at most 2M. Using 2sqrt(su)<=s+u gives

||X_{S*}^T xi/n||_2<=sigma sqrt((4Ms+6M log(1/rho))/n)

except with conditional probability rho.

The scalar sub-Gaussian tail bound P{|V|>t}<=2 exp(-t^2/(2v^2)) applies to a scalar with sub-Gaussian parameter v. Conditional on X, the parameter for X_j^T xi/n is sigma||X_j||_2/n<=sigma sqrt(2M/n). A union bound yields

||X^T xi/n||_infty<=4sigma sqrt(M log p/n)

with conditional failure probability at most 2p^-3. Applying the same tail bound to xi_i yields

||xi/sqrt(n)||_infty<=3sigma sqrt(log n/n)

with failure probability at most 2n^-3. Thus the design event and these two coordinate events hold jointly with probability 1-O(p^-2+n^-3). Adding the support-score event costs at most rho, not an unspecified multiple of rho.

## 2. First-stage induction

Let e_beta=beta^t-beta* and e_theta=theta^t-theta*. Direct substitution gives the exact identities

H_beta^{t+1}-beta*=(I-eta X^T X/n)e_beta-eta X^T e_theta/sqrt(n)+eta X^T xi/n,

H_theta^{t+1}-theta*=(1-eta)e_theta-eta X e_beta/sqrt(n)+eta xi/sqrt(n).

In particular, there is no XX^T factor multiplying e_theta. On the restricted supports, the learning-rate interval gives ||I-eta X_S^T X_S/n||_op<=delta, and |1-eta|<delta.

Put a_t=sqrt(s)lambda_beta,t and b_t=sqrt(o)lambda_theta,t. We prove for every iteration, including the continuation with fixed thresholds,

|supp(beta^t)\S*|<Bs,  |supp(theta^t)\O*|<Bo,

||beta^t-beta*||_2<=A a_t,  ||theta^t-theta*||_2<=A b_t.

These statements hold initially by the zero initialization and the two strict initial norm inequalities. They also cover theta*=0, since o=1.

Here is the threshold feasibility calculation. Define

alpha=4eta kappa f/d^2,
W_2=(8eta kappa/d)sigma sqrt(Ms log p/n),
W_3=(6eta kappa/d)sigma sqrt(o log n/n).

The sample-size constant can ensure alpha^2<=1/2. The prescribed thresholds give exactly

a_infty=2W_2+2alpha W_3,  b_infty=2W_3+2alpha W_2.

Consequently a_infty-alpha b_infty=2(1-alpha^2)W_2>=W_2, and b_infty-alpha a_infty>=W_3. The common-ratio initialization implies (a_t,b_t)=r_t(a_infty,b_infty), with r_t=max{kappa^t r_0,1} and r_0>1. Hence, for every t,

alpha b_t+W_2<=a_t,  alpha a_t+W_3<=b_t.

Suppose the induction holds at t. If beta^{t+1} has at least Bs off-support nonzeros, select k=ceil(Bs) such coordinates. If there are fewer than k available coordinates the alleged violation is impossible. On the selected coordinates, the raw-update norm is at least sqrt(k)lambda_beta,t+1. Its upper bound from the exact expansion, the induction, and concentration is strictly less than

delta A a_t+eta A^2 f b_t+4eta A sigma sqrt(Ms log p/n).

Strictness is justified even with threshold ties: sqrt(k)<A sqrt(s), so replacing the coordinate-noise factor by A sqrt(s) leaves strict slack. The union of the selected coordinates with the old error support has size at most (2B+2)s. Also a_t<=a_{t+1}/kappa and b_t<=b_{t+1}/kappa. The last display is therefore at most

(2delta/d)a_{t+1}+alpha b_{t+1}+W_2<=sqrt(B)a_{t+1}.

This contradicts sqrt(k)lambda_beta,t+1>=sqrt(B)a_{t+1}. The theta argument uses k=ceil(Bo), |1-eta|<delta, the same block bound, and W_3; it gives the other off-support count.

Once the new sparsity bounds hold, thresholding changes a raw update by less than its threshold on omitted true-support coordinates. On S* union supp(beta^{t+1}), the triangle inequality gives

||beta^{t+1}-beta*||_2<=a_{t+1}+delta||e_beta||_2+eta A f||e_theta||_2+4eta A sigma sqrt(Ms log p/n).

The old and new error supports together have size less than (2B+1)s. The preceding calculation bounds the right side by (1+sqrt(B))a_{t+1}=A a_{t+1}. The analogous theta calculation gives A b_{t+1}. This closes the induction, without assuming integer Bs or Bo and without treating thresholding as a top-budget projection.

At T_1, a_t=a_infty and b_t=b_infty. With a=s log p and b=o log n, the endpoint formulas imply

a_infty<=C sigma[sqrt(a/n)+sqrt((a+b)b)/n],
b_infty<=C sigma[sqrt(b/n)+sqrt((a+b)a)/n].

Since sqrt((a+b)b)<=sqrt(ab)+b and b/n is bounded by the sample condition, sqrt(ab)/n<=C sqrt(a/n). Interchanging a,b gives the other estimate. Squaring proves both first-stage rates. Support sizes are at most (B+1)s and (B+1)o. The same invariant holds throughout stage two and proves its sparsity and beta fallback rate without beta-min.

## 3. Signal-adaptive refinement

Work additionally on the support-score event with rho=varrho. Write z_t for the non-noise part of H_beta^{t+1}-beta*, and w=eta X^T xi/n. The threshold formula and coordinate event imply

||w||_infty<=d lambda_beta/(4kappa).

Put h=d/(3kappa+delta). If a true beta coordinate is removed, beta-min implies |z_{t,j}|>lambda_beta/h. Its discarded raw value therefore has magnitude at most h|z_{t,j}|. If a false coordinate is retained, |z_{t,j}|>=lambda_beta-||w||_infty, so |w_j|<=h|z_{t,j}|. The two exceptional sets are disjoint. Thus their combined Euclidean contribution is bounded by h times the Euclidean norm of z_t on S* union supp(beta^{t+1}). The remaining noise need only be bounded on S*.

Using the induction's support bounds and the restricted design event gives

||tilde beta^{t+1}-beta*||_2
<=r||tilde beta^t-beta*||_2+[8kappa^2 eta/((3kappa+delta)d)]f||tilde theta^t-theta*||_2
+eta sigma sqrt((4Ms+6M log(1/varrho))/n),

where r=4kappa delta/(3kappa+delta)<1. The fixed-threshold theta invariant implies

f||tilde theta^t-theta*||_2<=C sigma Q/n.

Consequently, with R=sigma[sqrt((s+log(1/varrho))/n)+Q/n],

||tilde beta^t-beta*||_2<=r^t||beta_hat-beta*||_2+C R/(1-r).

The first-stage bound and Q/n<=1/C_0 give ||beta_hat-beta*||_2<=C sigma. Since s>=1, R>=sigma/sqrt(n). Choose the iteration multiplier C depending only on M,eta,kappa so that r^{ceil(C log n)}<=n^-1/2. This absorbs the transient uniformly in the coefficient magnitudes, initial thresholds, and varrho. Squaring yields the refined rate with probability at least 1-varrho-O(p^-2+n^-3).

## 4. Uncontaminated lower bound, including its constant

Write C_s=C_{2s} and let P_beta be the clean one-observation law. For any two coefficient vectors whose difference has at most 2s nonzero entries, conditioning on the covariate gives

KL(P_beta^{\otimes n}||P_gamma^{\otimes n})
=n(beta-gamma)^T Sigma(beta-gamma)/(2sigma^2)
<=n C_s||beta-gamma||_2^2/(2sigma^2).

This calculation needs neither Gaussian covariates nor a covariance lower bound.

We use two standard finite-testing inequalities. For m equiprobable hypotheses, Fano's inequality gives average classification error at least 1-(I+log 2)/log m, and mutual information I is at most the average pairwise KL divergence. For two equiprobable hypotheses, minimum average classification error is (1-TV)/2; the bound TV<=sqrt(KL) suffices here. These are the independent finite-testing tools indexed by theory_019; no specialized regression theorem is assumed.

First suppose m=floor(p/s)>=4. Partition sm coordinates into s blocks of size m. In each block put one nonzero coefficient of magnitude a, with its position independently uniform, and set the remaining coordinates to zero. Take a^2=sigma^2 log m/(8n C_s). Reveal the positions in all other blocks when testing one block; this only makes testing easier. Every pair of hypotheses for that block has squared coefficient separation 2a^2, hence KL<=log m/8. Fano gives error at least 3/8. Decode a block by the closest of its m possible coefficient vectors in lq norm. A decoding error implies lq loss to the qth power at least 2a^q/2^q>=a^q/2. Summing block losses gives risk at least 3s a^q/16. Since log(ep/s)<=2log m, this is at least

[3/(16*16^{q/2})] C_s^{-q/2} sigma^q s(log(ep/s)/n)^{q/2}.

If m<4, use the first s coordinates with independent signs and magnitude a=sigma/sqrt(16n C_s). Reveal the other signs when testing one sign. Neighboring hypotheses have KL<=1/8, so TV<1/2 and average sign error is at least 1/4. A wrong sign incurs coordinate loss at least a^q. Since p/s<4 and log(ep/s)<3, the risk is at least

[1/(4*48^{q/2})] C_s^{-q/2} sigma^q s(log(ep/s)/n)^{q/2}.

For every q in [1,2], both displayed constants are larger than (8C_s)^(-q/2)/80 after including the C_s factor. All these priors are supported on ||beta||_0<=s. Because the clean experiment is contained in M(beta,o), its minimax risk, and hence the contaminated minimax risk, is at least

D_q sigma^q s(log(ep/s)/n)^{q/2},  D_q=(8C_s)^(-q/2)/80.

## 5. Contamination lower bound and fixed-count transfer

For every allowed s,p, take beta^(1)=0 and beta^(2)=lambda 1_[s], where lambda=sigma o/(sqrt(8C_s s)n). Both belong to the parameter class, without parity or p>=3s/2 restrictions. Set L=s lambda^q. Their one-observation KL is at most (o/(4n))^2, and their lq separation to the qth power is L.

Let v=TV(P_1,P_2). If v=0, the two clean sample laws coincide and the two-point Bayes risk is at least L/2^q>=L/4, which already suffices. Otherwise define epsilon=v/(1+v)<o/(4n). Relative to the dominating measure P_1+P_2, let p_1,p_2 be the densities and set q_1=(p_2-p_1)_+/v and q_2=(p_1-p_2)_+/v. Each integrates to one. Direct substitution gives

(1-epsilon)p_1+epsilon q_1=(1-epsilon)p_2+epsilon q_2.

Therefore their n-fold contaminated product laws coincide. Under the equal prior on the alternatives, for each of the first s coordinates and every estimate x, convexity gives (|x|^q+|x-lambda|^q)/2>=lambda^q/2^q. The Bayes risk in the independent-mixture experiment is at least L/2^q.

Generate independent Bernoulli contamination indicators with mean epsilon and let K be their sum. Conditional on K=k and a particular outlier subset, the sample law is an element of P_{beta,k}: all clean observations are independent with law P_beta and the bad ones have law Q_beta. Let t=P(K>o). Condition the prior experiment on K<=o and denote its optimal Bayes risk by R_tr. This is an average over admissible fixed-subset laws, so the minimax risk is at least R_tr; no assertion that their mixture itself belongs to a fixed-subset class is needed.

For these alternatives, coordinatewise clipping to [0,lambda] on the first s coordinates, and setting the others to zero, cannot increase loss and bounds loss pointwise by L. Apply an arbitrarily near-optimal clipped estimator from the truncated experiment also to the untruncated experiment. Letting its approximation error tend to zero gives

L/2^q<=(1-t)R_tr+tL,

and hence R_tr>=L(1/4-t).

The independent Bernoulli Bernstein inequality is P(K-EK>=u)<=exp(-u^2/[2EK+2u/3]). Since EK<o/4, it yields t<=exp(-9o/16). For o>=9, 1/4-exp(-9o/16)>1/80. Thus the contaminated minimax risk is at least

D_q sigma^q s^{1-q/2}o^q/n^q.

Combining this with Section 4 and max{x,y}>=(x+y)/2 proves the requested lower bound for every 0<c_q<(8C_{2s})^(-q/2)/160. This also checks odd s, nearly dense s<p, possibly singular lower-bound covariance, discrete covariates, and the fixed-count rather than independent-mixture observation model.

All theorem-critical obligations are closed. The local source repairs are integer support/tie bookkeeping and the unrestricted two-point alternatives; neither changes a public conclusion or introduces a substantive assumption.
