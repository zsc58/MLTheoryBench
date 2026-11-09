# Problem

## Setup

Let p>=2 and d be integers. Let phi:R->R be a fixed Borel-measurable even activation satisfying |phi(x)|<=B(1+|x|^r) for some finite constants B,r>0. Let delta>0 be fixed. Neither phi nor delta depends on p or d.

For each p,d, let U* be a p x d matrix whose rows are independent N(0,I_d/d). Let X_i be independent N(0,I_d) covariates and let xi_i be independent N(0,1) noises, all mutually independent. The observations are

Y_i=p^(-1/2) sum_{k=1}^p phi(<u_k*,X_i>)+sqrt(delta) xi_i.

First take d,n to infinity with p fixed and n/d->alpha in (0,infinity), and then take p to infinity.

Define

beta_*=min{b in {1,2,3,...}: mu_b!=0},

mu_b=E[phi(G)^b(G^2-1)],  G~N(0,1),

and assume beta_* is finite.

For a p x d matrix U, let N(U) normalize every nonzero row to unit Euclidean norm and map a zero row to zero. Write 1_p=(1,...,1)^T.

An estimator U-hat is a measurable p x d matrix-valued function of the observations and independent algorithmic randomness, with access to the known model parameters. It weakly recovers U* if there exist epsilon>0 and a deterministic unit vector v in R^p such that, with probability 1-o_d(1),

||N(U-hat)N(U*)^T v||_2>=epsilon.

The witness may depend on the fixed model parameters, p, and alpha, but not on d, the samples, or the estimator's realization. An estimator is unspecialized when every witnessing v lies in span{1_p}, and specialized when some witnessing v is orthogonal to 1_p.

## AMP Convention

AMP means Bayes-matched Gaussian multi-index approximate message passing for the known prior and observation channel, with isotropic vanishing side-information initialization and no choice of planted direction based on the data. Its limiting-performance convention is specified below so that the thresholds and the order of limits are explicit.

For a symmetric matrix Q with 0<=Q<I_p, let V,Z be independent N(0,I_p) vectors, put

T_Q=(I_p-Q)^(1/2)Z+Q^(1/2)V,

and define the conditional density

J_Q(y,V)=E_Z[(2 pi delta)^(-1/2) exp(-(y-p^(-1/2)sum_{k=1}^p phi((T_Q)_k))^2/(2 delta))].

Set

Psi(Q)=integral_R E_V[J_Q(y,V) log J_Q(y,V)] dy.

The gradient is taken in the space of real symmetric matrices with the Frobenius inner product; values needed at a boundary are understood by continuous extension from the interior.

For initialization strength eta in (0,1), the limiting overlap profile is Q_eta^0=eta I_p and

Q_eta^(t+1)=(I_p+2 alpha grad Psi(Q_eta^t))^(-1)(2 alpha grad Psi(Q_eta^t)),  t=0,1,2,... .

At every fixed eta and fixed t>=1, Q_eta^t specifies both the limiting row Gram matrix U-hat^t(U-hat^t)^T and the limiting planted cross-overlap U-hat^t(U*)^T in the proportional experiment. No additional planted information is available after initialization.

For a positive semidefinite matrix Q, define R(Q) by dividing its k-th row by sqrt(Q_kk) if Q_kk>0 and setting that row to zero otherwise. This specifies the normalized overlap profile.

At fixed p and alpha, the AMP weak-recovery event means that there are epsilon>0 and a deterministic unit vector v, independent of eta and of all experiment realizations, such that

liminf_{eta->0+} sup_{t>=1} ||R(Q_eta^t)v||_2>=epsilon.

The specialization event has the same definition with the additional requirement v perpendicular to 1_p. The supremum is over finite integer iteration counts: an iteration count may depend on eta and the fixed model parameters, but not on d. Thus the proportional limit is taken first, amplification is permitted next, and the initialization strength is removed last.

Define alpha_WR^Alg(p) and alpha_spec^Alg(p) as the infima of alpha>0 for which these respective events hold, with infimum of the empty set equal to infinity.

## Task

Prove that the AMP weak-recovery and specialization thresholds coincide and that their common value satisfies

alpha_WR^Alg(p)=alpha_spec^Alg(p)=Theta(p^(beta_*))

as p tends to infinity. Explicitly, prove that there exist constants 0<c<=C, depending only on the fixed activation and noise strength and not on p, such that

c p^(beta_*)<=alpha_WR^Alg(p)=alpha_spec^Alg(p)<=C p^(beta_*)

for all sufficiently large p.
