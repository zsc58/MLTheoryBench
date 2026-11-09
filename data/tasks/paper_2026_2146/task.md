# Problem

## Setup

Let n be a positive integer and let A be a nonempty family of subsets of [n]={1,...,n}. Define

`m=max_{A in A}|A|`.

Assume a fixed finite sequence of admissible actions `A_1,...,A_L`, with `L>=1`, has been specified such that every pair `(i,j) in [n]^2` is contained in at least one action of this sequence.

The outcome vectors `X_t in R^n` are i.i.d., with unknown mean `mu*` and covariance matrix `Sigma*`. At each round the action is selected using only previous actions and their observed coordinates, before observing the current outcome. Selecting `A_t` reveals exactly `X_{t,i}` for `i in A_t`.

Assume the following normalized moment bounds:

- For every `i in [n]` and every real `a`,
  `E exp(a(X_i-mu_i*)) <= exp(a^2/2)`.
- For every `lambda in R^n` with `||lambda||_1<=1/2`,
  `log E exp(lambda^T(X-mu*)) <= lambda^T Sigma* lambda`.

Here `X` has the common outcome distribution. All logarithms are natural, `e=exp(1)`, and `x vee y=max{x,y}`.

Let `e_A` be the incidence vector of an action. Fix an optimal action `A* in argmax_{A in A} e_A^T mu*`, and define

`Delta(A)=(e_{A*}-e_A)^T mu*`,

`R_T=E[sum_{t=1}^T Delta(A_t)]`.

## Algorithm

First play the specified initialization sequence. For every subsequent round `t>L`, define

`N_{i,t-1}=sum_{s<t} 1{i in A_s}`,

`N_{ij,t-1}=sum_{s<t} 1{i,j in A_s}`,

`overline mu_{i,t-1}=N_{i,t-1}^{-1} sum_{s<t:i in A_s} X_{s,i}`,

and

`overline Sigma_{ij,t-1}=N_{ij,t-1}^{-1} sum_{s<t:i,j in A_s}(X_{s,i}-overline mu_{i,t-1})(X_{s,j}-overline mu_{j,t-1})`.

For each ordered pair `i,j`, set

`g_{ij}(t)=16[(3 log t)/N_{ij,t-1} vee sqrt((3 log t)/N_{ij,t-1})]`

`             +sqrt(48(log t)^2/(N_{ij,t-1}N_{i,t-1}))`

`             +sqrt(36(log t)^2/(N_{ij,t-1}N_{j,t-1}))`,

and let

`Sigma_{ij,t}=overline Sigma_{ij,t-1}+g_{ij}(t)`.

For each action `A`, define

`C_t(A)={overline mu_{t-1}+xi : xi in R^n,`

`         sum_{i in A} N_{i,t-1}xi_i^2/(|A||xi_i|+sum_{j in A}(0 vee Sigma_{ij,t}))`

`         <=8(log t+log log t)+4em}`.

An empty sum is zero. Choose

`(A_t,mu_t) in argmax_{A in A, mu in C_t(A)} e_A^T mu`,

using a fixed measurable tie-breaking rule based only on the observed history.

## Task

If every action has zero gap, show that `R_T=0` for all `T`. Otherwise, let `Delta` and `Delta_max` be the smallest and largest positive action gaps, and define

`S=sum_{i=1}^n max_{A in A:i in A} sum_{j in A}(0 vee Sigma*_{ij})`.

Prove that there are positive universal constants `c,c'` such that, whenever

`Delta vee (Delta+Delta log(Delta_max/Delta))^(3/2) <= c[((log(m+1))/n^2)S]^(3/2)`,

the algorithm satisfies

`limsup_{T->infinity} Delta R_T/log T <= c' log^2(m+1)S`.
