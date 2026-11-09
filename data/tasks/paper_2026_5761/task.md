# Problem

## Setup

Let T,K,d,m be positive integers with 1<=m<=d, let p in (0,1] and delta in (0,1), and let B_X>0 and S,R>=0. Across all rounds and slate positions, the ideal actions X_{t,i} are independent and identically distributed, supported on an unknown subspace span(U), where U in R^{d by m} has orthonormal columns and ||X_{t,i}||_2<=B_X almost surely. Let Sigma=E[XX^T]; its nonzero eigenvalues satisfy bar(lambda)>=lambda_1>=...>=lambda_m>0. Put P=UU^T. The unknown parameter satisfies theta* in span(U) and ||theta*||_2<=S.

For every (t,i,j), the mask variables S_{t,i,j} are mutually independent Bernoulli(p) variables, independent of all ideal actions. Before choosing an arm, the learner receives each coordinate mask and the corresponding masked vector tilde(X)_{t,i}=S_{t,i} odot X_{t,i}; thus it knows the observed coordinate set Omega_{t,i} and the values of X_{t,i} on that set, including observed zeros. It does not receive the missing coordinate values. After choosing I_t, it observes

r_t=X_{t,I_t}^T theta*+eta_t.

Let H_t denote the information available immediately before this reward is revealed: the past observations and choices, the current masked slate and masks, and the learner's randomization and current choice. Assume, for every real a,

E[exp(a eta_t)|H_t]<=exp(a^2 R^2/2).

All choices are measurable with respect to the information available when they are made. Let X_t* maximize X_{t,i}^T theta* over the full ideal slate, and define

R_T=sum_{t=1}^T (X_t*-X_{t,I_t})^T theta*.

Define

mu=sqrt(d/m) max_j ||U_{j,:}||_2,

kappa=B_X sqrt(bar(lambda))/(lambda_m sqrt(m)).

Assume

p>=C_mu (mu^2 m/d) log(8mTK/delta).

Here C_mu is a sufficiently large universal constant. Fix universal constants C_a>=12 and C_b>=(32C_a)^2. The procedure below is run with its prescribed deterministic tuning quantities; it is not supplied with U, theta*, or the unobserved ideal actions. The norm and noise bounds used in its formulas are available for tuning.

## Algorithm

Set

t_b=ceil(C_b kappa^2 m log(16dT/delta)/(p^4 K)).

For rounds t<=min(t_b,T), use any fixed admissible burn-in policy. If t_b>=T, there are no later epochs. Otherwise set tau_0=t_b+1, tau_{e+1}=2tau_e, and retain the nonempty epochs

T_e={tau_e,...,min(tau_{e+1}-1,T)}.

Let N be their number and set delta_e=delta/(2N) for each such epoch.

For a masked vector tilde(X), define

Y(tilde(X))=p^{-2}tilde(X)tilde(X)^T+(p^{-1}-p^{-2})diag(tilde(X)tilde(X)^T).

Here diag keeps the diagonal entries of a square matrix and sets its other entries to zero. For t>=2, form the estimate from all offered samples in completed rounds,

hat(Sigma)_t=((t-1)K)^{-1} sum_{s<t} sum_{i=1}^K Y(tilde(X)_{s,i}).

At the start of epoch e, take an orthonormal basis Uhat_e of a top-m eigenspace of hat(Sigma)_{tau_e} and keep it fixed throughout that epoch.

For an offered action with observed coordinate set Omega, retain its observed entries. If G=Uhat_{e,Omega}^T Uhat_{e,Omega} is invertible, fill the missing entries by

Xhat_{Omega^c}=Uhat_{e,Omega^c} G^{-1} Uhat_{e,Omega}^T X_Omega.

If G is singular, set the missing entries to zero. Row subscripts denote the indicated row restrictions. Form z_{t,i}=Uhat_e^T Xhat_{t,i}.

Within each epoch, restart ridge regression with lambda=4B_X^2. Write z_s=z_{s,I_s} and set

V_{e,t}=lambda I_m+sum_{s in T_e, s<t}z_sz_s^T,

hat(vartheta)_{e,t}=V_{e,t}^{-1}sum_{s in T_e, s<t}z_s r_s.

Use the radius

beta_{e,t}=sqrt(lambda)S

+ R sqrt(2 log(det(V_{e,t})^{1/2}/(det(lambda I_m)^{1/2}delta_e)))

+ C_a SB_X(2+2/p)(kappa/p) sqrt(m log(16dT/delta)(t-tau_e)/((tau_e-1)K)).

Choose an arm maximizing

z_{t,i}^T hat(vartheta)_{e,t}+beta_{e,t}||z_{t,i}||_{V_{e,t}^{-1}},

where ||v||_A=sqrt(v^T A v) for positive definite A. Use fixed measurable rules for eigenvector choices and all ties. Regression uses only rewards and selected features from the current epoch.

## Task

Prove that, with probability at least 1-delta, this algorithm satisfies

R_T=tilde O_delta(SB_X kappa^2m/(p^4K)+(R+SB_X)m sqrt(T)+SB_X kappa m sqrt(T)/(p^2 sqrt(K))),

where tilde O_delta hides only universal constants and logarithmic factors in d,T,K,1/delta. The statement includes t_b>=T, when all rounds are burn-in and there are no post-burn-in epochs.
