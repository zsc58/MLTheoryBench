# Problem

## Setup

Throughout, ||.|| denotes the Euclidean norm. Let X={x_1,...,x_n} be a nonempty finite pool with known masses mu_i>=0 satisfying sum_i mu_i=1. Let S subset R^d be a nonempty bounded polyhedron, with diameter

Delta(S)=sup_{w,v in S}||w-v||.

Let C subset R^d be a nonempty bounded label space, and let rho(C)<infinity be a nonnegative constant such that ||c||<=rho(C) for every c in C. For each cost vector u in R^d, let w*(u) minimize u^T w over S under a fixed consistent tie-breaking rule: the selected point depends only on the set of minimizers.

Define

ell(u,c)=c^T w*(u)-c^T w*(c).

For each pool point x_i, let Q_i be a fixed, unknown distribution of a C-valued random vector. For a predictor h:X->C, define

R_SPO(h)=sum_i mu_i E_{C~Q_i}[ell(h(x_i),C)].

Let H be a nonempty finite class of such predictors, fixed before the sequential observations, with h(x_i)!=0 for every h in H and every i. Let h* be a minimizer of R_SPO over H.

Let C^o be the set of cost vectors in R^d for which minimization of the linear objective over S has multiple minimizers, and define

nu_S(u)=inf_{v in C^o}||u-v||,

with inf(empty set)=+infinity. Assume that a constant eta>0 satisfies, for every h in H and every pool point x_i,

nu_S(h(x_i))/||h(x_i)|| >= eta.

Set

L=Delta(S)rho(C)/(2eta)

and

gamma=sum_{i=1}^n max_{h,h' in H} ||h(x_i)/||h(x_i)||-h'(x_i)/||h'(x_i)||||.

Fix delta in (0,1). Run the following sequential procedure, making all choices using only observations already obtained and any independent algorithmic randomization.

Initialize H_0=H. At round t>=1, for each i let

p_{t,i}=max_{h,h' in H_{t-1}} ||h(x_i)/||h(x_i)||-h'(x_i)/||h'(x_i)||||.

If all p_{t,i}=0, stop and set H_s=H_{t-1} for every s>=t. Otherwise put P_t=sum_i p_{t,i} and pi_{t,i}=p_{t,i}/P_t. Conditional on the history F_{t-1} before this round, sample I_t with probabilities pi_{t,i}. Then observe a fresh label C_t at x_{I_t}: conditional on F_{t-1} and I_t=i, its distribution is Q_i.

At every round that draws a label, define

hat R_t(h)=t^{-1} sum_{s=1}^t [mu_{I_s}/pi_{s,I_s}] ell(h(x_{I_s}),C_s).

Only the selected indices occur in this expression, so each denominator is positive. Choose any empirical minimizer hhat_t of hat R_t over H_{t-1}, and retain

H_t={h in H_{t-1}: hat R_t(h)<=hat R_t(hhat_t)+r_t},

where

r_t=2gamma L sqrt(log(2t|H|/delta)/t).

For every integer horizon T>=1, output any h_T in H_T, using the extended sets just defined if the procedure has stopped.

## Task

Prove that, with probability at least 1-delta over the adaptive sampling, labels, and algorithmic randomization, simultaneously for every integer T>=1 and every allowed output h_T in H_T,

R_SPO(h_T)-R_SPO(h*) <= 4gamma L sqrt(log(2T|H|/delta)/T).
