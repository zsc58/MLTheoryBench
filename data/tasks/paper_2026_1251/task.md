# Problem

## Setup

Let n be a positive integer and let Z_1,...,Z_{n+1} be iid. Let A be a possibly randomized training rule whose output law is invariant under every permutation of the input data, and let theta_n=A(D_n), theta_{n+1}=A(D_{n+1}), where D_n=(Z_1,...,Z_n) and D_{n+1}=D_n union {Z_{n+1}}. Let the parameter space be Theta. Define

S_i=s(Z_i;theta_n), i=1,...,n+1,

tilde S_i=s(Z_i;theta_{n+1}), i=1,...,n+1.

Let r=ceil((1-alpha)(n+1)) and let q_* be the r-th order statistic of tilde S_1,...,tilde S_{n+1}. Assume alpha in (0,1), u_n>0, delta_n in (0,1),

P(||theta_{n+1}-theta_n||_2>u_n)<=delta_n,

and, for every Z and theta,theta' in Theta,

|s(Z;theta)-s(Z;theta')|<=L||theta-theta'||_2

for a constant L>0. Assume that all pairwise ideal-score ties have probability zero. Assume there are finite fbar and rho>0 such that, for every i in {1,...,n+1} and every h in (0,rho],

P(q_*<tilde S_i<=q_*+h)<=fbar h,

P(q_*-h<=tilde S_i<q_*)<=fbar h.

Require L u_n<=rho. Set

m_n=ceil(n fbar L u_n/delta_n)

and require r+m_n<=n.

Given the actual training scores S_1,...,S_n, choose a positive integer N_n and run the following one-sided noisy binary search on [a,b], where b>=max_{i<=n}S_i. Initialize left=a and right=b. At each of the at most N_n adaptive midpoint queries, query

C_n(x)+sigma xi,    C_n(x)=#{i<=n:S_i<=x},

where the query noises are independent standard normal variables scaled by sigma>0. If the noisy count is at least

r+m_n+tau_n,    tau_n=sigma Phi^{-1}(1-beta_n/N_n)-1,

set right to the midpoint; otherwise set left to the midpoint. Return the final right endpoint qhat. Here beta_n in (0,1).

For the stability specialization, let Theta be nonempty, closed, and convex in R^d, with d a positive integer. Run T>=1 projected DP-SGD iterations with constant step eta>0, clipping radius C>0, noise multiplier sigma>0, Poisson sampling rate q in (0,1), and nonempty minibatches. Write

bar g(theta;z)=clip_C(gradient ell(theta;z)),

hat g_t(theta)=m_t^{-1} sum_{i in B_t} bar g(theta;Z_i),

and update

theta^(t+1)=Pi_Theta(theta^(t)-eta[hat g_t(theta^(t))+(sigma/m_t)xi_t]),

where xi_t are iid N(0,I_d). Couple the D_n and D_{n+1} runs with shared initialization, shared Gaussian vectors, and shared masks for the common n points, plus independent iid Bernoulli(q) masks b_{n+1,t} for Z_{n+1}. Use the synchronized nonempty-minibatch convention: empty common masks are discarded and resampled before an iteration is counted, the accepted common minibatch B_t is nonempty, and B'_t=B_t union {Z_{n+1}} when b_{n+1,t}=1 and B'_t=B_t otherwise. Assume each loss gradient is L-Lipschitz on Theta.

## Task

Prove the following integrated theorem. First, under the preceding regularity assumptions, the private-search output satisfies

P(S_{n+1}<=qhat)>=(1-beta_n)(1-alpha-2 fbar L u_n-3 delta_n-1/(n+1)).

Then prove that, for the projected DP-SGD procedure,

E_n:=E||theta_n^(T)-theta_{n+1}^(T)||_2

satisfies

E_n<=[1-(1-q)^(n+1)](2C+sigma sqrt(d))(exp(eta L T)-1)/((n+1)L).

Finally, under eta=O(n^-1), T=O(n), beta_n=O(n^-1), and bounded 2C+sigma sqrt(d), use u_n=E_n^(2/3), delta_n=E_n^(1/3), and the above m_n to show that the coverage lower bound tends to 1-alpha. The power choices apply whenever E_n>0; if E_n=0, use positive admissible sequences with the same vanishing rates.
