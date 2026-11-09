# Problem

## Setup

Let N and T be integers with 1<=T<N. Fix lambda>0, delta in (0,1), and known finite bounds R,C>=0. All these quantities and the graph below are fixed before the procedure starts. All logarithms are natural.

Let an undirected weighted graph have N nodes and Laplacian L=Q diag(eta_1,...,eta_N)Q^T, where Q is orthogonal and 0<=eta_1<=...<=eta_N. For each arm i in {1,...,N}, let b_i in R^N be the transpose of row i of Q. Set A=diag(eta_1,...,eta_N)+lambda I_N. For a positive definite matrix M, write ||x||_M=(x^T M x)^{1/2}.

Define d as the largest integer in {1,...,N} satisfying
(d-1)eta_d <= T/log(1+T/lambda).
Set
v=R sqrt(6d log((lambda+T)/(delta lambda)))+C.

Fix an unknown, nonrandom vector mu in R^N such that ||mu||_A<=C and |b_i^T mu|<=1 for every arm. Initialize B_1=A and hat_mu(1)=0. At each round t=1,...,T, conditional on the preceding history, draw a fresh sample
 tilde_mu(t)~N(hat_mu(t),v^2 B_t^{-1}),
choose an arm a(t) maximizing b_i^T tilde_mu(t), and then observe
 r(t)=b_{a(t)}^T mu+epsilon_t.
Use a fixed measurable rule to resolve ties. Here the preceding history consists of all earlier draws, selected arms, and observed rewards. In the sequential feedback model, after the current draw and arm selection and before observing r(t), the noise satisfies, for every u in R,
 E[exp(u epsilon_t) | preceding history, tilde_mu(t), a(t)] <= exp(u^2 R^2/2).
Thus it is conditionally mean-zero and R-sub-Gaussian at the time the reward is generated. A Gaussian distribution with zero covariance is interpreted as its deterministic value.

Update
 B_{t+1}=B_t+b_{a(t)}b_{a(t)}^T,
 hat_mu(t+1)=B_{t+1}^{-1}sum_{s=1}^t b_{a(s)}r(s).

Let a^* be any fixed maximizer of b_i^T mu, define
 Delta_i=b_{a^*}^T mu-b_i^T mu,
 R(T)=sum_{t=1}^T Delta_{a(t)},
and set
 p=1/(4e sqrt(pi)),
 g=sqrt(4 log(TN))(R sqrt(6d log((lambda+T)/(delta lambda)))+C)+R sqrt(2d log(((lambda+T)T^2)/(delta lambda)))+C.

## Task

Prove that, with probability at least 1-delta over the sampling and reward observations,
R(T)<= (11g/p) sqrt(((4+4lambda)/lambda)dT log((lambda+T)/lambda)) + 1/T + (g/p)(11/sqrt(lambda)+2) sqrt(2T log(2/delta)).
In particular, the leading dependence is d sqrt(T log N) up to logarithmic factors and problem-dependent constants.
