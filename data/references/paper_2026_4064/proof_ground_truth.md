# Reference Proof

## Proof Structure and Obligations

The proof must establish: (1) a simultaneous confidence event with exactly the specified radius under the sequential observation model; (2) the constrained-estimator reduction needed for that event; (3) the optimism and Lipschitz instantaneous-regret bound; (4) truncation and a multi-output determinant telescope; and (5) the cumulative bound and its probability. All five obligations are derived below. In particular, the specialized concentration citation in the source is not taken as an unproved premise.

Fix delta in (0,1). All statements concern the policy run with this fixed delta; no simultaneous assertion over different delta values is needed. If N=0, both sides of the requested bound are zero, so assume N>=1.

## 1. Simultaneous Concentration

Let F_n=sigma(I_n). The chosen action and A_n=A_n(u_n) are F_n-measurable. Since theta* is deterministic, the observation model makes v_n measurable with respect to F_{n+1}. The conditional noise assumption given (I_n,u_n) is therefore the conditional assumption given F_n.

For 0<=n<=N define

H_n=sum_{i<n} A_i^T V A_i,
s_n=sum_{i<n} A_i^T V v_i,
b=Lambda_0(mu_0-theta*),
beta=b^T Lambda_0^{-1}b=||mu_0-theta*||_{Lambda_0}^2<=c_theta^2.

Thus Lambda_n=Lambda_0+H_n. For each fixed t in R^d, put

X_n(t)=exp((t^T s_n-(1/2)t^T H_n t)/c_v^2).

The ratio X_{n+1}(t)/X_n(t) is

exp(t^T A_n^T Vv_n/c_v^2 - t^T A_n^T V A_n t/(2c_v^2)).

Applying conditional subgaussianity in the F_n-measurable direction V A_n t/c_v^2 shows that this ratio has conditional expectation at most one. Consequently X_n(t) is a nonnegative supermartingale and X_0(t)=1.

Let Q be the fixed Gaussian probability measure N(Lambda_0^{-1}b,c_v^2 Lambda_0^{-1}) on R^d, and define

Z_n=integral X_n(t) Q(dt).

Although Q involves theta*, it is used only in this proof, not by the policy. The parameter and regularization data are deterministic, so Q is not selected from the observations. Conditional Tonelli gives E[Z_{n+1}|F_n]<=Z_n and Z_0=1.

The density of Q is

(det Lambda_0)^(1/2)/(2 pi c_v^2)^(d/2)
 times exp(-(t-Lambda_0^{-1}b)^T Lambda_0(t-Lambda_0^{-1}b)/(2c_v^2)).

Multiplying by X_n(t), the exponent becomes

[-t^T Lambda_n t+2t^T(s_n+b)-beta]/(2c_v^2).

Completing the square around Lambda_n^{-1}(s_n+b) and integrating the resulting Gaussian gives

Z_n=det(Lambda_0^{-1}Lambda_n)^(-1/2)
 times exp((||s_n+b||_{Lambda_n^{-1}}^2-beta)/(2c_v^2)).

Here every Lambda_n is positive definite. Its determinant ratio with Lambda_0 is positive, so the expression is well-defined.

For completeness, stop Z_n at the first index in {0,...,N} at which Z_n>=1/delta, or at N if there is no crossing. The stopped process is a nonnegative supermartingale: before stopping its conditional increment has nonpositive expectation, and after stopping its increment is zero. Hence its terminal expectation is at most Z_0=1. On the crossing event its terminal value is at least 1/delta. Therefore

P(exists n<=N: Z_n>=1/delta)<=delta.

Outside that event, simultaneously for 0<=n<=N,

||s_n+b||_{Lambda_n^{-1}}^2
 <= beta+c_v^2 log det(Lambda_0^{-1}Lambda_n)+2c_v^2 log(1/delta)
 <= gamma_n(delta)^2.

This establishes the precise shifted self-normalized inequality needed here without invoking an unproved research-specific theorem.

## 2. Constrained Least-Squares Confidence

Let psi_n be the least-squares objective and e_n=mu_n-theta*. Expanding at theta* yields

psi_n(theta)=(1/2)||theta-theta*||_{Lambda_n}^2
 -(s_n+b)^T(theta-theta*)+constant.

Since Theta is convex and mu_n is an attained minimizer, the directional derivative toward theta* is nonnegative:

( Lambda_n e_n-(s_n+b) )^T(theta*-mu_n)>=0.

It follows that

||e_n||_{Lambda_n}^2 <= (s_n+b)^T e_n
 <= ||s_n+b||_{Lambda_n^{-1}} ||e_n||_{Lambda_n}.

If e_n=0, the desired inequality holds immediately. Otherwise division gives

||theta*-mu_n||_{Lambda_n}<=||s_n+b||_{Lambda_n^{-1}}.

Together with Section 1, this proves

P(E)>=1-delta,
where E={||theta*-mu_n||_{Lambda_n}<=gamma_n(delta) for every n<N}.

## 3. Optimism and Instantaneous Regret

Fix a realization in E. For each n<N, the pair (u_n*,theta*) is feasible for the joint minimization. Optimality of (u_n,theta_tilde_n) therefore gives

phi_n(u_n,theta_tilde_n)<=phi_n(u_n*,theta*).

Because u_n* minimizes the true loss,

0<=r_n<=phi_n(u_n,theta*)-phi_n(u_n,theta_tilde_n).

Both A_n(u_n)theta* and A_n(u_n)theta_tilde_n belong to the explicitly defined set Z_n. Applying the loss assumption, the Euclidean operator norm, and the two confidence-ellipsoid memberships yields

r_n<=L_z||A_n(u_n)(theta*-theta_tilde_n)||_V
 <=L_z||V^(1/2)A_n(u_n)Lambda_n^(-1/2)||_2
   (||theta*-mu_n||_{Lambda_n}+||theta_tilde_n-mu_n||_{Lambda_n})
 <=2L_z gamma_n(delta)||V^(1/2)A_n(u_n)Lambda_n^(-1/2)||_2.

Also r_n<=c_r.

## 4. Truncation and Determinant Potential

Define

M_n=V^(1/2)A_n(u_n)Lambda_0^(-1/2),
S_n=Lambda_0^(-1/2)Lambda_n Lambda_0^(-1/2)
   =I_d+sum_{i<n}M_i^T M_i,
B_n=M_n S_n^(-1)M_n^T,
rho_n=lambda_max(B_n).

All matrix square roots are the symmetric positive-definite ones. Direct inversion of the congruence defining S_n shows

B_n=V^(1/2)A_n(u_n)Lambda_n^(-1)A_n(u_n)^T V^(1/2).

Thus B_n is positive semidefinite and

rho_n=||V^(1/2)A_n(u_n)Lambda_n^(-1/2)||_2^2.

The sequence det(Lambda_n) is nondecreasing: Lambda_{n+1} is Lambda_n plus a positive-semidefinite matrix, and its determinant ratio with Lambda_n is the determinant of an identity plus a positive-semidefinite matrix. Hence gamma_n(delta)<=gamma_N(delta). Set

C_N=max{c_r,2L_z gamma_N(delta)}.

The two instantaneous-regret bounds give

r_n^2<=C_N^2 min{1,rho_n}<=2C_N^2 log(1+rho_n).

For 0<=rho_n<=1, the last inequality follows from log(1+x)>=x/2; for rho_n>1, it follows from 2log(1+rho_n)>=2log 2>=1. These inequalities also hold at rho_n=0.

The nonnegative eigenvalues of B_n imply

log(1+rho_n)<=log det(I_k+B_n).

Use the determinant identity det(I_k+AB)=det(I_d+BA) for A in R^(k x d) and B in R^(d x k). Its hypotheses hold with A=M_n S_n^(-1) and B=M_n^T. Therefore

log det(I_k+B_n)
 =log det(I_d+M_n^T M_n S_n^(-1))
 =log det(S_n+M_n^T M_n)-log det(S_n)
 =log det(S_{n+1})-log det(S_n).

Summing over n telescopes. Since S_0=I_d and det(S_N)=det(Lambda_0^(-1)Lambda_N),

sum_{n<N} r_n^2
 <=2C_N^2 log det(Lambda_0^(-1)Lambda_N).

No division by rho_n or by the log determinant occurs; in particular, zero information gain is covered.

## 5. Cumulative Regret

Cauchy-Schwarz gives, on E,

R_N=sum_{n<N}r_n
 <=sqrt(N sum_{n<N}r_n^2)
 <=max{c_r,2L_z gamma_N(delta)}
   sqrt(2N log det(Lambda_0^(-1)Lambda_N)).

The probability of E is at least 1-delta. This proves the requested bound, with its realized information matrix and confidence radius, for each fixed delta in (0,1).
