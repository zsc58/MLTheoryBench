# Reference Proof

If M=1, the sum is empty and the claim is immediate. If sigma=0, the displayed lower bound is also zero, so assume sigma>0 and M>=2.

Fix true means with unique maximizer m_opt and gaps Delta_i satisfying the stated conditions. We construct one admissible Gaussian environment P realizing these means. In P, observations are independent Gaussian with variance sigma^2; the optimal arm has fixed bias 0, and every suboptimal arm i has fixed bias +L. Thus the observation mean of arm i is mu_i+L for i != m_opt and is mu^* for m_opt. This is an admissible subclass of the conditional bounded-bias and sub-Gaussian model.

If E_P[N]=infinity, the desired conclusion is immediate. Otherwise, fix i != m_opt and gamma>0. Define Q_i by leaving every arm other than i unchanged, changing the true mean of arm i to mu^*+epsilon+gamma, and giving arm i fixed bias -L. Under Q_i, arm i is the unique optimal arm, so it is epsilon-optimal. Both P and Q_i are admissible environments.

Let A_i={hat_m=i}. Under P, arm i is more than epsilon below the optimum, so uniform PAC correctness gives P(A_i)<=delta. Under Q_i, arm i is optimal, so Q_i(A_i)>=1-delta. Bretagnolle-Huber applied to A_i therefore gives

KL(P_traj || Q_i,traj) >= log(1/(4 delta)).

The adaptive sampling rule and stopping rule have the same conditional kernels under the two environments. The trajectory laws differ only on observations obtained when arm i is selected. The Gaussian observation-mean separation on such a pull is

(mu^*+epsilon+gamma-L) - (mu_i+L)
= Delta_i+epsilon+gamma-2L.

The stopped adaptive chain rule for relative entropy consequently gives

KL(P_traj || Q_i,traj)
= E_P[N_i] (Delta_i+epsilon+gamma-2L)^2/(2 sigma^2).

Combining the last two displays yields

E_P[N_i] >= 2 sigma^2 log(1/(4 delta)) /(Delta_i+epsilon+gamma-2L)^2.

The expectation on the left is independent of gamma. Letting gamma decrease to zero gives

E_P[N_i] >= 2 sigma^2 log(1/(4 delta)) /(Delta_i+epsilon-2L)^2.

Summing over all i != m_opt and using N=sum_i N_i gives

E_P[N] >= 2 sigma^2 log(1/(4 delta)) sum_{i != m_opt} 1/(Delta_i+epsilon-2L)^2.

This is the claimed lower bound. For delta<=1/16, log(1/(4 delta)) is comparable to log(1/delta); hence in the usual small-confidence regime the lower bound has order

sum_{i != m_opt} sigma^2 log(1/delta)/(Delta_i+epsilon-2L)^2.

More generally, the exact dependence valid throughout 0<delta<1/4 is the displayed factor log(1/(4 delta)).
