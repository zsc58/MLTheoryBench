# Reference Proof

Fix the fitted objects. Put N=n+1, S_i=s(X_i), I_i^s=1{ell(a_s(X_i),Y_i)>=c}, I_i^0=1{ell(pi_0(X_i),Y_i)>=c}, and W_i=I_i^0-I_i^s. Then W_i is in {-1,0,1} and L(Z_i;t)=I_i^s+W_i 1{S_i<t}. Atomlessness makes the N scores distinct and strictly between 0 and 1 almost surely. Write S_(1)<...<S_(N) and use parentheses for their concomitants.

The rank j(t)=#{r:S_r<t} counts observations using the baseline at t. Thus a score threshold S_(k) has rank k-1, while the formal threshold top has rank N. Thresholds 0 and S_(1) both have rank zero and the same calibration losses. Define, for every integer 0<=j<=N,

T_j=1+sum_{r=1}^N I_(r)^s+sum_{r=1}^j W_(r)-(N+1)epsilon.

At an augmented grid threshold t, bumped feasibility is equivalent to T_{j(t)}<=0. Define T_j^{-i} analogously after removing i, using the normalization N epsilon for its N-1 retained observations. For any common threshold with rank j, T_j^{-i}-T_j equals epsilon-I_i^0 if S_i<t and epsilon-I_i^s otherwise. The same identity holds for the formal partial sums at every j, taking S_i<t to mean that i's ordered rank is at most j. Consequently |T_j^{-i}-T_j|<=1. The available leave-one-out ranks consist of ranks of retained score thresholds, zero, and N. At most one intermediate rank is missing. Adjacent available thresholds change T^{-i} by at most one retained W; adjacent augmented thresholds have the same property.

Let kappa=epsilon-p_s>0 and xi=p_0-epsilon>0. Put rho=kappa/8. Hoeffding's inequality applied to the i.i.d. fallback indicators gives, outside an event of probability exp(-cN),

sum_{i=1}^N(I_i^s-epsilon)<=-kappa N/2.

On this event T_0<=-kappa N/2+1 and T_0^{-i}<=-kappa N/2+1 for every i. Since every W is at most one, T_j and T_j^{-i} are negative at every j<=floor(rho N), for all sufficiently large N. Every augmented or leave-one-out selection therefore has rank at least floor(rho N)-1: at most one rank can be absent from a leave-one-out grid.

For each i, Hoeffding's inequality gives probability at most exp(-c'(N-1)) that the mean of the N-1 baseline indicators excluding i fails to exceed epsilon+xi/2. A union bound makes these inequalities simultaneous outside an event of probability at most N exp(-c'(N-1)). Their average implies that the augmented baseline count exceeds N(epsilon+xi/2). Accordingly the centered bumped sums at top are greater than one, both for the augmented sample and for every leave-one-out sample, when N is sufficiently large. The grid threshold immediately preceding top differs by at most one retained increment, so it too is infeasible. All selected ranks are consequently interior on the intersection of these two high-probability events.

Denote the augmented selected rank by a and a leave-one-out selected rank by b_i. On that intersection, each selected partial sum is nonpositive, while its next available partial sum is positive. Their one-step differences are at most one, so -1<T_a<=0 and -1<T_{b_i}^{-i}<=0. Uniform perturbation gives -2<T_{b_i}<=1. If b_i>a, then sum_{r=a+1}^{b_i}W_(r)=T_{b_i}-T_a<2. If b_i<a, then sum_{r=b_i+1}^{a}W_(r)=T_a-T_{b_i}<2. Each sum is integer-valued and hence at most one. The intervening block starts at least at min(a,b_i)+1.

For all sufficiently large N, let i_0=floor(rho N/2)>=1; the rank lower bound places every such intervening block in the suffix {i_0,...,N}. Choose q>0 with P(S<q)<rho/4, possible because S is atomless and nonnegative. A binomial tail bound shows that S_(i_0)>=q except with probability exp(-c''N). Conditional on all ordered scores, the concomitants W_(r) are independent: conditional on the original score vector their laws form a product indexed by the scores, and reordering makes that product depend only on the ordered vector. On {S_(i_0)>=q}, their conditional means for r>=i_0 are at least lambda=c_W q^beta>0.

Let M be the longest contiguous block in that suffix with W-sum at most one, or zero if none exists. For any block of length h>=2/lambda, conditional Hoeffding gives P(block sum<=1 | ordered scores)<=exp(-lambda^2 h/8). There are at most N starts for each length, so, with d=lambda^2/8,

P(M>=h | ordered scores)<=N sum_{m=h}^N exp(-dm)

on the score event. Summing this tail after a cutoff of order d^{-1}log N+2/lambda proves E[M | ordered scores]<=C log N+C' there, with constants independent of N. The crossing argument yields K<=M on the intersection of the three good events. Always K<=N. The exceptional probabilities are exponentially small up to a polynomial factor, so their contributions N P(exception) are bounded. Enlarging the additive constant to cover finitely many small N gives E[K]<=C_1 log N+C_2.

Finally, when the leave-one-out rank exceeds the augmented rank, the corresponding observation's loss can change only if its unique score rank lies among at most K ranks immediately above the augmented rank. A downward displacement similarly accounts for at most K ranks. Since |W_i|<=1,

(1/N)sum_{i=1}^N |L(Z_i;t^{-i})-L(Z_i;t^+)|<=2K/N.

The selection rule is permutation invariant, so exchangeability gives E[L(Z_N;t(Z_1,...,Z_{N-1}))]=E[(1/N)sum_i L(Z_i;t^{-i})]. When the augmented feasible set is nonempty, bumped feasibility gives (1/N)sum_i L(Z_i;t^+)<=((N+1)epsilon-1)/N<=epsilon. If it is empty, threshold zero is infeasible. Its loss is the fallback loss, and the probability of this event is exponentially small by p_s<epsilon and Hoeffding's inequality. The augmented mean loss is always at most one. Consequently

E[L(Z_N;t(Z_1,...,Z_{N-1}))]<=epsilon+2E[K]/N+C exp(-cN).

Substitute the logarithmic bound, set N=n+1, and absorb the additive and exponentially small terms into C_3 log N/N for all sufficiently large n.
