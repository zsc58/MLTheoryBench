# Problem

## Statistical model and functions

Let Z_1,...,Z_n be independent copies of Z=(X,T,Y), where n>=2 and T,Y take values in {0,1}. Write P_X for the marginal distribution of X and define

e(x)=P(T=1|X=x),

p_t(x)=P(Y=1|X=x,T=t),  t in {0,1}.

All functions below are measurable, and equalities between functions are understood P_X-almost surely. For a fixed c_0 in (0,1/2), assume the true nuisance eta_0=(p_1,p_0,e) and every candidate or fitted nuisance eta=(q_1,q_0,pi) have all three coordinates in [c_0,1-c_0].

Define the following maps on (0,1)^2, so that they are also defined at every point of [c_0,1-c_0]^2:

psi_OR(u,v)=u(1-v)/(v(1-u)),

psi_logOR(u,v)=logit(u)-logit(v),

psi_RR(u,v)=u/v,

psi_logRR(u,v)=log(u)-log(v),

where logit(u)=log(u/(1-u)).

Fix any one of these four maps, denote it by psi_theta, and put a_1=partial_1 psi_theta and a_0=partial_2 psi_theta. Define

phi_theta(Z;eta)=psi_theta(q_1(X),q_0(X))
+a_1(q_1(X),q_0(X)) T(Y-q_1(X))/pi(X)
+a_0(q_1(X),q_0(X)) (1-T)(Y-q_0(X))/(1-pi(X)),

and theta(X)=psi_theta(p_1(X),p_0(X)).

For f in L2(P_X), let

L_theta(f,eta)=E[(phi_theta(Z;eta)-f(X))^2].

Let F be a deterministic class of measurable real-valued functions containing theta, with

M=max{sup_{f in F}||f||_infty,1}<infinity.

For a measurable triple g=(g_1,g_0,g_e), define

||g||_G=(E_X[(g_1(X)^2+g_0(X)^2+g_e(X)^2)^2])^(1/4).

Here and below E_X integrates over P_X. When its integrand contains fitted functions, those functions are held fixed; equivalently, X is an independent test covariate. Write ||h||_2=(E_X[h(X)^2])^(1/2).

## Estimator

Partition the indices into I_1 and I_2 of sizes m_1=floor(n/2) and m_2=n-m_1. The partition is fixed in advance or randomized independently of the observations. For j in {1,2}, fit eta_hat^(j) using only observations outside I_j. Any auxiliary training randomness is independent of the observations. On I_j, choose a measurable exact minimizer

theta_hat^(j) in argmin_{f in F} m_j^{-1} sum_{i in I_j}[phi_theta(Z_i;eta_hat^(j))-f(X_i)]^2.

Assume these minimizers exist. Define

theta_hat=(theta_hat^(1)+theta_hat^(2))/2,

E_n^4=(1/2)sum_{j=1}^2 ||eta_hat^(j)-eta_0||_G^4.

No convexity of F is assumed, and the averaged estimator is not required to belong to F.

## Localized-complexity convention

The following specifies the critical-radius term. Define

H_theta={a(f-theta)/(2M): f in F, 0<=a<=1}.

For a positive integer m and s>=0, let

R_m(s)=E_{X_1',...,X_m',epsilon_1,...,epsilon_m} sup_{h in H_theta, ||h||_2<=s}|m^{-1}sum_{i=1}^m epsilon_i h(X_i')|,

where X_i' are independent with distribution P_X and epsilon_i are independent uniform signs in {-1,1}, independent of the X_i'. Assume the displayed suprema and all empirical-process suprema used for this class are measurable.

Choose a deterministic r_n satisfying, for j=1,2,

r_n>=m_j^{-1/2},  R_{m_j}(r_n)<=r_n^2,

and define delta_n=M r_n. Any such admissible radius may be used; no rate of decay is assumed.

## Task

Prove the following for each of the four choices of psi_theta.

1. For every fixed admissible nuisance eta,

E[phi_theta(Z;eta)|X]=theta(X)+R_theta(X;eta),

where R_theta is a sum of propensity/outcome error cross-products and a term quadratic in (p_1-q_1,p_0-q_0). It satisfies

|R_theta(X;eta)|<=C_theta[|e-pi|(|p_1-q_1|+|p_0-q_0|)+|(p_1-q_1,p_0-q_0)|_2^2],

with C_theta depending only on c_0 and the chosen map. It vanishes when q_1=p_1 and q_0=p_0. In particular E[phi_theta(Z;eta_0)|X]=theta(X).

2. The population risk minimizer over L2(P_X), unique up to null sets, is

m_theta,eta(X)=E[phi_theta(Z;eta)|X].

For every f in L2(P_X),

L_theta(f,eta_0)-L_theta(theta,eta_0)=E_X[(f(X)-theta(X))^2].

The squared loss is Neyman-orthogonal in the sense that

D_eta D_f L_theta(theta,eta_0)[h,k]=0.

Here D denotes directional differentiation, h ranges over L2(P_X), and k initially ranges over bounded measurable triples. Derivatives in eta are computed from the displayed formulas on (0,1)^3, even when a true coordinate equals c_0 or 1-c_0. The mixed derivative is also understood on L4(P_X;R^3) by its continuous extension from bounded nuisance directions.

3. There are constants C_1,C_2 depending only on c_0, M, and the chosen map such that, for every delta in (0,1), with probability at least 1-delta over the observations and fitting randomness,

E_X[(theta_hat(X)-theta(X))^2]
<=C_1[delta_n^2/M^2+log(1/delta)/n]+C_2 E_n^4.

If all four targets are fitted on the same sample, the four inequalities can be taken to hold on a common event of probability at least 1-delta, after enlarging constants by a fixed numerical factor. Each target may use its own class F, bound M, and admissible radius, with the notation above applied separately.
