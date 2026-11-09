# Problem

## Setup

Let d and p be positive integers, let 1<=m<=d, and let A in R^(m x d) have full row rank. Let b in R^m and suppose X={x in R^d:Ax=b,x>=0} is nonempty and bounded. Assume every vertex has exactly m positive coordinates. Write X^angle for its finite vertex set and K=|X^angle|. Fix an ordering of these vertices, and let x^star(v) be the first vertex minimizing v^T x over X.

Let c0 in R^d, let Sigma be positive definite, and set C={c:(c-c0)^T Sigma^(-1)(c-c0)<=1}. For a finite query set D subset R^d, define s(c;D)=(q^T c)_{q in D} and C(D,s(c;D))={v in C:q^T v=q^T c for every q in D}. Call D globally sufficient if equal measurements for two costs in C imply identical optimal-solution sets over X. A subspace W is globally sufficient if every finite query set spanning W is globally sufficient. Let W_star be a minimum-dimensional globally sufficient subspace, let d_star=dim(W_star), and let U be a full-column-rank matrix spanning it.

For a full-column-rank matrix V with t columns, define pi_V(c)=V^T(c-c0) and
   L_V(s)=c0+Sigma V(V^T Sigma V)^(-1)s,  s in R^t.
For t=0, use the unique empty coordinate and define L_V=c0.

Let (Z,c) have a joint distribution with Z in R^p and c in C almost surely. For a measurable predictor f, set x_f(z)=x^star(f(z)),
   ell(c,x)=c^T x-min_{y in X}c^T y,
   R_SPO(f)=E[ell(c,x_f(Z))],
   Rhat_SPO(f)=n^(-1)sum_{i=1}^n ell(c_i,x_f(Z_i)).
Define
   omega_X(C)=sup_{c in C}(max_{x in X}c^T x-min_{x in X}c^T x).

Use the fixed-intercept predictor classes
   F_aff={z -> c0+Mz:M in R^(d x p), c0+MZ in C almost surely},
   F_star={z -> L_U(Bz):B in R^(d_star x p), L_U(BZ) in C almost surely},
and write R_SPO^aff=inf_{f in F_aff}R_SPO(f). For any learned query set hat D, choose a full-column-rank basis hat U of its span, put t=dim(span(hat D)), and define
   F_hat={z -> L_hatU(Bz):B in R^(t x p), L_hatU(BZ) in C almost surely}.
Range restrictions refer to the context distribution, not to every point of R^p.

## Query Procedure

For a vertex with basis B0, let N0 be the complementary indices. For j in N0 define delta_N0(B0,j)=e_j and delta_B0(B0,j)=-A_B0^(-1)A_j. Put
   Lambda(B0)={v:v^T delta(B0,j)>=0 for every j in N0}.

The following procedure takes a cost v in C and a current query set D. Its anchor is v. Obtain the basis B0 of x^star(v) and minimize each facet functional u^T delta(B0,j) over the current fibre C(D,s(v;D)). If all minima are nonnegative, stop and return D. Otherwise choose an index of minimum facet value and a minimizing witness u_out. For every j with u_out^T delta(B0,j)<0, set
   a_j=(v^T delta(B0,j))/(v^T delta(B0,j)-u_out^T delta(B0,j)).
Choose an index minimizing a_j, add its direction delta(B0,j) to D, and repeat. If N0 is empty, stop. All nonunique choices use fixed measurable deterministic rules depending only on the current cost and query set.

Cumulative processing starts with D empty, runs this procedure on each supplied cost in sequence, and warm-starts each run from the previous query set. A sample is hard when its processing adds a query. Denote the final set by hat D and the hard-sample subsequence by T.

## Learned-Representation Setting

For this setting, assume ||Z||_2<=1 almost surely and E[ZZ^T]>=kappa I_p, where kappa>0. Suppose
   c=c0+M_mu Z+epsilon,
   E[epsilon|Z]=0,
   mu(z)=E[c|Z=z]=c0+M_mu z,
with M_mu in R^(d x p). Assume mu(Z) in C almost surely. For sigma>=0, assume that for every real lambda and every unit u in R^d,
   E[exp(lambda u^T epsilon)|Z]<=exp(lambda^2 sigma^2/2)
almost surely.

From an iid labeled sample of size n_mu, fit centered multi-response OLS by minimizing
   sum_i ||(c_i-c0)-MZ_i||_2^2.
If nonunique, choose the solution of smallest Frobenius norm. Write the fitted matrix as hat M_mu and set hat_mu(z)=c0+hat M_mu z.

Draw n_disc iid discovery contexts from the marginal law of Z, independently of the regression sample. Cumulatively process the pseudo-costs hat_mu(Z_j^disc) to obtain (hat D,T) and hat U. Define
   tilde_mu(z)=L_hatU(hatU^T(hat_mu(z)-c0)).

Let
   B_X={v in R^d:there are distinct vertices x,y in X^angle both minimizing v^T x over X}.
Distance is Euclidean; distance to the empty set is infinity. Suppose C_marg>0 and alpha>0 satisfy
   P_Z(dist(mu(Z),B_X)<=eta)<=C_marg eta^alpha
for every eta>0. Assume, almost surely over the realized regression and discovery samples, that
   P_Z(hat_mu(Z) in C)=1,
   P_Z(tilde_mu(Z) in B_X)=0,
where Z here is a fresh context and the learned objects are held fixed. All random variables, predictors, query rules, and loss events used below are measurable.

Let n,n_mu,n_disc be positive integers and delta,delta_mu in (0,1).

## Task

Prove the following statements.

1. For every prediction cost v in C, L_U(pi_U(v)) belongs to C and has the same selected optimizer as v. In particular, for every true cost c in C,
   ell(c,x^star(v))=ell(c,x^star(L_U(pi_U(v)))).
Also, inf_{f in F_star}R_SPO(f)=R_SPO^aff. With probability at least 1-delta over n iid contextual observations, simultaneously for every f in F_star,
   R_SPO(f)<=Rhat_SPO(f)
      +2 omega_X(C) sqrt(2(d_star p+1)log(n K^2)/n)
      +omega_X(C) sqrt(log(1/delta)/(2n)).

2. In the learned-representation setting, suppose
   n_mu>=(8/kappa)log(2p/delta_mu),
and define
   r_{mu,delta_mu}=4sqrt(2)sigma/sqrt(kappa)
      *sqrt(d(p+log(4d/delta_mu))/n_mu).
With probability at least 1-delta_mu-delta over the regression sample and independent discovery contexts,
   P_Z(x^star(tilde_mu(Z)) != x^star(mu(Z)))
      <=4(6|T|+log(e/delta))/n_disc+C_marg r_{mu,delta_mu}^alpha,
and
   0<=inf_{f in F_hat}R_SPO(f)-R_SPO^aff
      <=omega_X(C)[4(6|T|+log(e/delta))/n_disc
                   +C_marg r_{mu,delta_mu}^alpha].
Every population risk minimizer f_hat in F_hat, when the infimum is attained, satisfies the same excess-risk inequality. Prove |T|<=d_star, so either upper bound remains valid when |T| is replaced by d_star.
