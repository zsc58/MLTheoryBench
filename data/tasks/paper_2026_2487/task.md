# Problem

## Setup

Let d>=1, p>=2, and let P be a distribution on R^d with mean mu_P and covariance matrix Sigma_P. Define

nu_{P,p} = sup_{||v||_2=1} (E_P |<v,X-mu_P>|^p)^(1/p).

Let S be measurable with P(S)>=1-epsilon, where 0<=epsilon<=1/2, and write Q=P(.|S). You observe iid samples X_1,...,X_n~Q. For n>=2, set

F = 1/binom(n,2) sum_{i<j} <X_i,X_j>.

The testing hypotheses are H0: ||mu_P||_2=0 and H1: ||mu_P||_2>=alpha, for alpha>0. Universal positive constants may be chosen independently of d,p,P,S,epsilon,alpha.

## Task

Prove the following integrated theorem.

Let gamma=2 nu_{P,p} epsilon^(1-1/p). If alpha>2gamma, then there is a universal constant C such that the test

T=1{F>alpha^2/4}

has success probability at least 2/3 under both hypotheses whenever

n>=max{2, C ||Sigma_P||_op sqrt(d)/(alpha-2gamma)^2}.

Moreover, there is a universal constant c>0 such that for every p>=2, every 0<epsilon<=1/2, and every alpha>0, one can construct distributions P_1 and P_0 on R^d and a measurable set S such that P_1 has finite nu_{P_1,p},

||mu_{P_1}||_2>=alpha,   mu_{P_0}=0,   P_1(S)>=1-epsilon,

P_1(.|S)=P_0, and alpha<=c nu_{P_1,p} epsilon^(1-1/p). Consequently, no test, even with arbitrarily many truncated samples, has worst-case error below 1/2.

The lower-bound construction may be embedded in one coordinate, and the null distribution may be observed without truncation.
