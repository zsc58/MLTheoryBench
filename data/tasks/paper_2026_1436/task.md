# Problem

## Setup

Let X={(b,d) in R^2:b<d} and Delta={(t,t):t in R}. Give X union Delta the metric d_infty(p,q)=||p-q||_infinity, and write pi_Delta(b,d)=((b+d)/2,(b+d)/2). For p=(b,d) in X, let pers(p)=(d-b)/2. For every p in R^2, let r(p)=||(1,p)||_2, where (1,p) is the vector in R^3 obtained by adjoining a first coordinate equal to one. Let M be the finite nonnegative Borel measures mu on X with integral r(p) dmu(p)<infinity. Define Pers(mu)=integral pers(p) dmu(p).

A partial transport plan between mu,nu in M is a finite nonnegative Borel measure gamma on X times X whose marginals gamma_1,gamma_2 are bounded by mu,nu. Its cost is

integral ||p-q||_infinity dgamma(p,q) + integral ||p-pi_Delta(p)||_infinity d(mu-gamma_1)(p) + integral ||q-pi_Delta(q)||_infinity d(nu-gamma_2)(q).

Set POT_1(mu,nu) to be the infimum of this cost over all partial transport plans.

For finite signed Borel measures sigma on X union Delta with integral r d|sigma|<infinity, define

Lambda(sigma)(v)=integral (<v,(1,p)>)_+ d sigma(p), v in R^3,

where z_+=max{z,0} and |sigma| is the total variation measure. Put mu^Delta=(pi_Delta)#mu, mu^aug=mu-mu^Delta, S(mu)=Lambda(mu^aug)|_{S^2}, and mu op_Delta nu=mu+nu^Delta. Here S^2={v in R^3:||v||_2=1}, and # denotes pushforward of measures.

For functions on S^2, use ||f||_infinity=sup_{v in S^2}|f(v)| and ||f||_2=(integral_{S^2}|f(v)|^2 domega(v))^{1/2}, where domega is ordinary surface area measure, of total mass 4pi. The space L2(S^2) uses this measure.

For nonnegative Borel measures A,B on R^2, say they are compatible when A is Radon, B is finite, and

A(B_R)B(R^2\B_{R-1})/R -> 0 as R -> infinity,

where B_R={p:||p||_2<=R}. Let M(A,B) consist of those mu in M such that for every Borel U subset R^2,

integral_{U cap X} r(p) dmu(p) <= A(U),

integral_{U cap X} r(p) pers(p) dmu(p) <= B(U).

Let M_c(A,B) be the members of M(A,B) whose support is compact in X. All occurrences of compact support below mean compact support in X.

## Task

Prove the following integrated theorem. For all mu,nu in M,

||S(mu)-S(nu)||_infinity <= 2sqrt(2) POT_1(mu,nu).

The map S is injective on M. If mu_n,mu in M, mu has compact support, and ||S(mu_n)-S(mu)||_infinity tends to zero, then POT_1(mu_n,mu) tends to zero.

Finally, for every compatible pair A,B, the restriction

S:(M_c(A,B),POT_1) -> (L2(S^2),||.||_2)

is an injective homeomorphism onto its image and satisfies, for all mu,nu in M_c(A,B),

||S(mu)-S(nu)||_2 <= 4sqrt(2pi) POT_1(mu,nu).

Moreover, if mu_n,mu in M_c(A,B) and ||S(mu_n)-S(mu)||_2 tends to zero, then ||S(mu_n)-S(mu)||_infinity tends to zero and POT_1(mu_n,mu) tends to zero.
