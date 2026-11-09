# Reference Proof

Let D_n=(Z_1,...,Z_n), let D_{n+1}=D_n union {Z_{n+1}}, and write S_i=s(Z_i;theta_n) for i<=n+1 and tilde S_i=s(Z_i;theta_{n+1}) for i<=n+1. Let r=ceil((1-alpha)(n+1)) and let q_* be the r-th order statistic of the ideal scores.

## 1. Private-search rank guarantee

At a query midpoint x, let C_n(x)=#{i<=n:S_i<=x}. The search changes right to x only when C_n(x)+sigma xi >= r+m_n+tau_n, where xi is standard normal and

tau_n=sigma Phi^{-1}(1-beta_n/N_n)-1.

Conditionally on the previous search history, if C_n(x)<=r+m_n-1, a false right update requires

sigma xi >= tau_n+1=sigma Phi^{-1}(1-beta_n/N_n).

The conditional probability of this event is at most beta_n/N_n. A union bound over the N_n queries gives an event G_n with probability at least 1-beta_n on which every right update occurs only at a point whose true count is at least r+m_n. Since the initial right endpoint b has count n and r+m_n<=n, the invariant C_n(right)>=r+m_n is maintained. Thus, on G_n,

qhat>=S_(r+m_n),

where S_(k) is the k-th order statistic of the n actual training scores.

## 2. Transfer from ideal to actual scores

Because the data are iid and A is permutation invariant, the ideal scores are exchangeable. The no-ties assumption implies that the test score has a uniform rank among the n+1 ideal scores, so

P(tilde S_{n+1}<=q_*)>=1-alpha.

Define the test-flip event

T={1{tilde S_{n+1}<=q_*} != 1{S_{n+1}<=q_*}}

and the excessive-down-crossing event

R={#{i<=n: tilde S_i>q_* and S_i<=q_*}>=m_n+1}.

On the event A={tilde S_{n+1}<=q_*}, no test flip, and no R, exactly r ideal scores are at most q_*. Since the test score is one of them and there are no ties, exactly r-1 ideal training scores are at most q_*. At most m_n of those above q_* can cross downward, so the actual training count at q_* is at most r+m_n-1. Hence S_(r+m_n)>q_*. The no-flip event also gives S_{n+1}<=q_*, and therefore S_{n+1}<=S_(r+m_n). Consequently,

P(S_{n+1}<=S_(r+m_n))>=1-alpha-P(T)-P(R).

Let H={||theta_{n+1}-theta_n||_2<=u_n}. On H, score Lipschitzness gives |S_i-tilde S_i|<=L u_n for every i. A test flip therefore implies that the ideal test score lies in one of the two one-sided intervals of width L u_n adjacent to q_*. The explicit anti-concentration assumptions, the stability assumption, and the no-ties rank boundary give

P(T)<=delta_n+2 fbar L u_n+1/(n+1).

For down-crossings, on H every down-crossing training score lies in (q_*,q_*+L u_n]. If

Y=sum_{i=1}^n 1{q_*<tilde S_i<=q_*+L u_n},

then R intersect H is contained in {Y>=m_n+1}. Anti-concentration gives E[Y]<=n fbar L u_n. Since

m_n=ceil(n fbar L u_n/delta_n),

Markov's inequality gives P(Y>=m_n+1)<=delta_n, and hence

P(R)<=2delta_n.

Combining these bounds with the rank guarantee and conditioning on the data, the independent search noise contributes a factor at least 1-beta_n. Therefore

P(S_{n+1}<=qhat)>=(1-beta_n)(1-alpha-2 fbar L u_n-3delta_n-1/(n+1)).

## 3. Projected DP-SGD stability

Use the synchronized coupling specified in the task. At each counted iteration the common minibatch B_t is nonempty, the augmented minibatch is B'_t=B_t union {n+1} when the independent extra mask b_{n+1,t}=1 and is B_t otherwise, and m'_t=m_t+b_{n+1,t}. The Gaussian vectors and common-point masks are shared, and the extra masks are independent Bernoulli(q). Empty common masks are discarded and resampled before an iteration is counted. Let

Delta_t=theta_n^(t)-theta_{n+1}^(t), and d_t=E||Delta_t||_2.

Projection onto the closed convex set Theta is non-expansive. Radial clipping is Euclidean projection onto the radius-C ball and is therefore non-expansive. Thus the clipped gradient is L-Lipschitz in theta. The one-step updates imply

||Delta_{t+1}||_2 <= (1+eta L)||Delta_t||_2
 + eta(2C+sigma||xi_t||_2)/(m_t+1) 1{b_{n+1,t}=1}.

Indeed, when the extra point is included, the two averaged clipped gradients differ at the same parameter by at most 2C/(m_t+1), and the different noise normalizations contribute at most sigma||xi_t||_2/(m_t+1). Taking expectations, using E||xi_t||_2<=sqrt(d), independence of the extra mask, and the binomial reciprocal identity gives

E[1{b_{n+1,t}=1}/(m_t+1)]
 <=q E[1/(K+1)]
 =[1-(1-q)^(n+1)]/(n+1),

where K has the Binomial(n,q) law. Hence

d_{t+1}<=(1+eta L)d_t
 +eta[1-(1-q)^(n+1)](2C+sigma sqrt(d))/(n+1).

The initialization is shared, so d_0=0. Unrolling the recurrence and using the geometric sum gives

d_T<=[1-(1-q)^(n+1)](2C+sigma sqrt(d))((1+eta L)^T-1)/((n+1)L).

Since (1+eta L)^T<=exp(eta L T),

E_n=d_T<=[1-(1-q)^(n+1)](2C+sigma sqrt(d))(exp(eta L T)-1)/((n+1)L).

## 4. Asymptotic specialization

The displayed E_n here is the actual expected distance, and the preceding inequality bounds it. For E_n in (0,1), choose

u_n=E_n^(2/3),    delta_n=E_n^(1/3).

Markov's inequality gives

P(||theta_n^(T)-theta_{n+1}^(T)||_2>u_n)<=E_n/u_n=delta_n.

If E_n=0 for an exceptional n, use any positive admissible sequences with the same vanishing rates; this does not affect the limit. Under eta=O(n^-1), T=O(n), L>0, and bounded 2C+sigma sqrt(d), the stability bound gives E_n=O(n^-1). Therefore

u_n=O(n^-2/3),    delta_n=O(n^-1/3),

and

m_n=ceil(n fbar L u_n/delta_n)=O(n E_n^(1/3))=O(n^(2/3))=o(n).

Thus, for all sufficiently large n, L u_n<=rho, u_n and delta_n lie in their required domains, and r+m_n<=n because r=(1-alpha)(n+1)+O(1) with alpha>0. Taking beta_n=O(n^-1), every correction term in the finite-sample bound tends to zero. The lower bound consequently converges to 1-alpha.
