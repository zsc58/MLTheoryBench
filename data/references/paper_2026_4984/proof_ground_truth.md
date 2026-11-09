# Reference Proof

## Proof Structure

1. Use the block-Gaussian conditioning formula to compute the conditional law of the task score given the observed concepts.
2. Identify the Bayes rule under 0-1 loss as the sign threshold of the conditional mean, with either label optimal at a tie.
3. Decompose the score into an observed Gaussian signal and an independent residual. Handle zero observed-signal variance directly, then apply the Gaussian sign-agreement identity in the nondegenerate case.
4. Expand the observed-signal variance into known-known, cross-aligned, and recoverable-unknown terms; the residual term is independent of the coupling parameter.

## Complete Proof

Fix alpha. Throughout the proof, all probabilities and expectations are under the specified law for this alpha. Write C=B_ku(alpha) and

B(alpha) = [[B_kk, C], [C^T, B_temp+C^T B_kk^{-1} C]].

The Gaussian covariance is assumed in the problem. Its consistency can also be checked directly: for x in R^p and z in R^q,

[x;z]^T B(alpha) [x;z]
= (x+B_kk^{-1}Cz)^T B_kk (x+B_kk^{-1}Cz) + z^T B_temp z.

This is positive for every nonzero pair (x,z), because B_kk and B_temp are positive definite. This consistency check is not a separate required conclusion of the task.

### 1. Conditional Gaussian law

The standard block-Gaussian conditioning result states that, for centered jointly Gaussian vectors (X,Z) with covariance blocks [[A,C],[C^T,D]] and invertible A, the conditional law of Z given X is Gaussian with mean C^T A^{-1}X and covariance D-C^T A^{-1}C. Here the vectors are jointly Gaussian by assumption and B_kk is positive definite, so the result applies and gives

E[chi_u | chi_k] = C^T B_kk^{-1} chi_k,

Cov(chi_u | chi_k) = B_uu(alpha)-C^T B_kk^{-1}C = B_temp.

Because eta is independent of the entire concept vector and has distribution N(0,sigma_y^2), the conditional law of the task score is

tau | chi_k ~ N(phi(alpha)^T chi_k, v_R),

where

phi(alpha)=psi_k+B_kk^{-1}C psi_u,

v_R=psi_u^T B_temp psi_u+sigma_y^2.

In particular, v_R is strictly positive, since sigma_y^2>0, and is independent of alpha because B_temp, psi_u, and sigma_y^2 are fixed.

### 2. Bayes optimality

Let Phi denote the standard normal cumulative distribution function. The conditional probability of label 1 is

p_alpha(chi_k)=P(y=1 | chi_k)
=Phi(phi(alpha)^T chi_k / sqrt(v_R)).

For a measurable binary classifier g, its conditional error probability is p_alpha(chi_k) when g(chi_k)=0 and 1-p_alpha(chi_k) when g(chi_k)=1. Thus a pointwise conditional-risk minimizer predicts 1 when p_alpha(chi_k)>1/2 and 0 when p_alpha(chi_k)<1/2; either prediction is optimal at equality. Taking expectations of these conditional risks proves optimality for the population 0-1 risk over all measurable classifiers using only chi_k.

Since Phi is strictly increasing and Phi(0)=1/2, the measurable classifier

h_alpha(chi_k)=1{phi(alpha)^T chi_k>0}

is therefore Bayes optimal. It chooses 0 at a tie, which is an allowed optimal choice.

### 3. Exact accuracy, including zero observed signal

Define

S=phi(alpha)^T chi_k,

e=chi_u-C^T B_kk^{-1}chi_k,

R=tau-S=psi_u^T e+eta.

The pair (e,chi_k) is jointly Gaussian and

Cov(e,chi_k)=C^T-C^T B_kk^{-1}B_kk=0.

For jointly Gaussian vectors, zero cross-covariance implies independence. Consequently e is independent of chi_k. Its mean is zero and its covariance is

E[e e^T]=B_uu(alpha)-C^T B_kk^{-1}C=B_temp.

Independence of eta from the entire concept vector then shows that R is independent of chi_k, and hence of S, with

R ~ N(0,v_R).

Also

S ~ N(0,v_S),

v_S=phi(alpha)^T B_kk phi(alpha) >= 0.

First suppose v_S=0. Then S=0 almost surely, h_alpha=0 almost surely, and tau=R. Since v_R>0, R is a centered nondegenerate Gaussian variable. Therefore

P(h_alpha(chi_k)=y)=P(R<=0)=1/2.

This equals the required expression because arctan(sqrt(0/v_R))=0. No correlation or nondegenerate sign-agreement formula is used in this case.

Now suppose v_S>0. Both S and S+R have continuous nondegenerate Gaussian laws, so each is zero with probability zero. Accordingly,

P(h_alpha(chi_k)=y)=P(sign(S)=sign(S+R)).

The pair (S,S+R) is centered jointly Gaussian with covariance matrix

[[v_S,v_S],[v_S,v_S+v_R]].

Its determinant is v_S v_R>0, and its correlation is

rho = v_S / sqrt(v_S(v_S+v_R))
= sqrt(v_S/(v_S+v_R)),

which lies strictly between 0 and 1.

The standard Gaussian sign-agreement identity states that a centered nonsingular bivariate Gaussian pair (U,V) with correlation rho satisfies

P(sign(U)=sign(V))=1/2+(1/pi)arcsin(rho).

All its hypotheses have just been verified. Applying it yields

P(h_alpha(chi_k)=y)
=1/2+(1/pi)arcsin(sqrt(v_S/(v_S+v_R))).

For positive a and b, the angle theta=arctan(sqrt(a/b)) belongs to (0,pi/2) and satisfies sin(theta)=sqrt(a/(a+b)). Hence

arcsin(sqrt(a/(a+b)))=arctan(sqrt(a/b)).

Using a=v_S and b=v_R, and combining with the zero-signal case, proves

P(h_alpha(chi_k)=y)
=1/2+(1/pi)arctan sqrt([phi(alpha)^T B_kk phi(alpha)]/[psi_u^T B_temp psi_u+sigma_y^2]).

### 4. Signal decomposition and alpha dependence

Substituting phi(alpha)=psi_k+B_kk^{-1}C psi_u and using symmetry of B_kk and its inverse gives

phi(alpha)^T B_kk phi(alpha)
=psi_k^T B_kk psi_k
 +2 psi_k^T C psi_u
 +psi_u^T C^T B_kk^{-1}C psi_u.

Replacing C by B_ku(alpha) gives the requested expansion. The first term is independent of alpha. Only the cross-aligned and recoverable-unknown terms can depend on alpha through B_ku(alpha); they need not change for every choice of parameters. The residual denominator psi_u^T B_temp psi_u+sigma_y^2 is independent of alpha. Since alpha was arbitrary, all conclusions hold for every alpha in I.

## Proof-Obligation Closure

- The conditional law follows from the stated standard Gaussian conditioning result with its invertibility and joint-Gaussian hypotheses verified.
- Bayes optimality follows by explicit comparison of the two conditional 0-1 risks and then taking expectations.
- Residual independence follows from the computed zero cross-covariance and the standard jointly Gaussian independence criterion.
- The accuracy calculation handles zero signal directly and verifies positive variances and nonsingularity before invoking the stated standard sign-agreement identity.
- The numerator expansion and alpha independence follow by direct algebra with the fixed parameters.

No unresolved proof obligation remains.
