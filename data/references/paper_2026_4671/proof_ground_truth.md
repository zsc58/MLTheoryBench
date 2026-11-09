# Reference Proof

## Contract and obligations

The learner uses only past revealed feedback. Current loss and constraint vectors are generated before the fresh arm draw, which is conditionally independent of those vectors. Conditional means may depend on the past. All statements below are therefore valid also for predictable, nonstationary environments. Hindsight quantities such as the optimizer and the strictly feasible strategy need not be predictable; the concentration arguments used for them are uniform over simplex strategies.

The obligations are: (1) simultaneous constraint concentration and nonemptiness; (2) feasible mixture comparators; (3) correct phase counting and mixture cost; (4) fixed-share entropic regret on the moving projection sets; (5) conversion to realized regret against the mean-loss benchmark; (6) positive violation; and (7) all small-horizon and degenerate learning-rate cases. Each is proved below.

## 1. Small horizons and algorithmic well-definedness

Write L=ln(TKm/delta) and B=ln(KT). No update is performed after round T. In particular, when K=T=1, eta=0 is never used in an objective. For T>1, eta>0, and the played distributions have positive coordinates because of the post-projection share. Nonempty projection sets are compact and convex, and the KL objective with a positive prior has a unique minimizer. An empty set triggers the stated uniform fallback, so the algorithm is defined on every sample path.

For T=2 or T=3, R_T<=T deterministically because OPT>=0, while 4log_2(T)sqrt(T ln(KT))>=T. For T=1 and delta<1/3, 4sqrt(ln(K/delta))>1>=R_T; for delta>=1/3 the requested regret probability is nonpositive and hence imposes no condition. For T<=3 the violation bound follows directly from V_T<=T and the displayed right-hand side, which is at least T. It remains to prove both guarantees for T>=4.

## 2. A single constraint event

For the proof, index empirical estimates after observations: for 1<=s<=T, let h_{s,i}=s^{-1}sum_{r=1}^s g_{r,i}, mu_{s,i}=s^{-1}sum_{r=1}^s bar g_{r,i}, and r_s=4sqrt(L/s). Define H_s={x in Delta_K:(h_{s,i}-r_s 1)^T x<=0 for every i}. For s<T, this is the public set X_{s+1}. H_T is used only for a virtual terminal update in the proof.

We use the standard martingale inequality: if conditionally centered increments have absolute value at most b, then P(sum_{r=1}^N Z_r>=h)<=exp(-h^2/(2Nb^2)); the two-sided bound has an additional factor 2. Constraint coordinate differences g_{r,i}(a)-bar g_{r,i}(a) are conditionally centered and have absolute value at most 2. Thus, for each s,i,a,

P(|h_{s,i}(a)-mu_{s,i}(a)|>r_s)<=2exp(-2L).

A union bound over at most TKm triples has failure probability at most 2delta^2/(TKm)<=delta, since T>=4. Let E_g be the resulting simultaneous event.

Everything in the next deterministic arguments holds on E_g. In particular, for every simplex x,

(h_{s,i}-r_s 1)^T x<=mu_{s,i}^T x.

Therefore (h_{s,i}-r_s 1)^T x^diamond<=-rho, so every H_s is nonempty. This is stronger than merely asserting nonemptiness with a separate probability cost. It also shows that the fallback is never used on E_g.

The corruption definition gives, coordinatewise,

|mu_{s,i}(a)-g_i^circ(a)|<=C/s,

and hence

|h_{s,i}(a)-g_i^circ(a)|<=r_s+C/s.

Writing G_i=T^{-1}sum_{r=1}^T bar g_{r,i}, the triangle inequality gives ||G_i-g_i^circ||_1<=C/T. Consequently, for every simplex x,

(h_{s,i}-r_s 1)^T x<=G_i^T x+C/s+C/T.

These inequalities hold simultaneously for all x, including hindsight-dependent choices.

## 3. Feasible comparators and phase accounting

Let x^* attain OPT. Existence follows from compactness and nonemptiness of its feasible set. Since G_i^T x^*<=0, the previous bounds imply

(h_{s,i}-r_s 1)^T x^*<=C/s+C/T,

whereas the corresponding value at x^diamond is at most -rho.

For each s, define b_s=C/s+C/T, alpha_s=rho/(rho+b_s), and q_s=(1-alpha_s)x^diamond+alpha_s x^*. For every r>=s,

(h_{r,i}-r_r 1)^T q_s<=-(1-alpha_s)rho+alpha_s(C/r+C/T)<=0.

Thus q_s belongs to H_r for every r>=s. This formula also covers C=0, when q_s=x^*.

Partition the loss rounds into phases beginning at s_j=2^{j-1}, stopping at T. Their number is S=1+floor(log_2 T), and phase j has length d_j<=s_j. Use comparator q_{s_j} throughout phase j. It belongs to every projection set H_t used during that phase.

Because losses belong to [0,1]^K, the observed-loss mixture cost is at most

sum_j d_j(1-alpha_{s_j})
<= (C/rho)sum_j d_j(1/T+1/s_j)
<= (C/rho)(1+S)
<= (2C/rho)log_2 T,

where the last step uses T>=4 and S<=1+log_2 T. This retains the sharper C/T+C/s expression already available from the empirical comparison, rather than introducing an incorrect phase count.

## 4. Fixed-share entropic regret

For t<T, write p_{t+1} for the public projected point. On E_g, also define a virtual p_{T+1} by the same optimization over H_T and put x_{T+1}=(1-1/T)p_{T+1}+u/T. This virtual point is only a telescoping device and is not an extra played round.

For this section extend the KL divergence to positive, not necessarily normalized second arguments by

D(v||w)=sum_a[v(a)ln(v(a)/w(a))-v(a)+w(a)].

Set w_{t+1}(a)=x_t(a)exp(-eta ell_t(a)). Expanding the objective shows that p_{t+1} minimizes D(x||w_{t+1}) over H_t. For q in H_t, convex first-order optimality gives the Bregman projection inequality

D(q||w_{t+1})>=D(q||p_{t+1})+D(p_{t+1}||w_{t+1})>=D(q||p_{t+1}).

For completeness, the first inequality follows by subtracting the three divergences: the difference is the inner product of q-p_{t+1} with the gradient of D(·||w_{t+1}) at its minimizer, which is nonnegative. On E_g, the strict constraint margin at x^diamond allows a small mixture with u, so H_t contains a full-support point. An entropic minimizer with positive w_{t+1} then has full support: otherwise moving toward that point has a negative infinite one-sided entropy derivative. Thus the gradient calculation is legitimate.

The fixed share gives x_{t+1}(a)>=(1-1/T)p_{t+1}(a), and hence

D(q||x_{t+1})<=D(q||p_{t+1})-ln(1-1/T).

Expanding D(q||w_{t+1}) and using e^{-z}<=1-z+z^2/2 for z>=0 yields

eta ell_t^T(x_t-q)
<=D(q||x_t)-D(q||x_{t+1})+eta^2/2-ln(1-1/T).

Here sum_a x_t(a)ell_t(a)^2<=1. This inequality does not require x_t itself to belong to H_t; it requires the comparator to belong to the projection set.

Telescope within each phase. Every played coordinate is at least 1/(KT), and sum_a q(a)ln q(a)<=0, so every phase-start divergence is at most ln(KT)=B. Discard the nonnegative phase-end divergences and use -T ln(1-1/T)<=T/(T-1)<=2. We obtain

sum_t ell_t^T(x_t-q_{s_{j(t)}})<=SB/eta+2/eta+eta T/2
=(S+2/B+1/2)sqrt(TB).

For T>=4, S<=log_2 T+1, B>=ln 4, and

S+2/B+1/2<=log_2 T+3<=4log_2 T.

Combining this with the mixture cost proves, on E_g,

sum_t ell_t^T(x_t-x^*)
<=4log_2(T)sqrt(T ln(KT))+(2C/rho)log_2(T).

## 5. Realized regret and probability accounting

Conditional on the past and the current vectors, the fresh arm draw has law x_t. Thus ell_t(A_t)-ell_t^T x_t is a conditionally centered increment with absolute value at most 1. With probability at least 1-delta,

sum_t[ell_t(A_t)-ell_t^T x_t]<=sqrt(2T ln(1/delta)).

For each arm a, ell_t(a)-bar ell_t(a) is conditionally centered and has absolute value at most 1. A one-sided martingale bound and a union bound over K arms give, with probability at least 1-delta,

max_a sum_t[ell_t(a)-bar ell_t(a)]<=sqrt(2T ln(K/delta)).

The latter event implies the same bound after taking the inner product with every simplex vector. In particular it applies to the hindsight-dependent x^*, without falsely assuming that x^* is predictable.

Adding these two inequalities to the deterministic observed-loss comparison gives the desired regret bound because

sqrt(2T ln(1/delta))+sqrt(2T ln(K/delta))<=4sqrt(T ln(TK/delta)).

Together with E_g, the union bound gives probability at least 1-3delta. No martingale argument involving the phasewise hindsight comparators is needed.

## 6. Positive constraint violation

Remain on E_g. Put p_1=u. Then x_t=(1-1/T)p_t+u/T for every played round. Convexity of the positive part and bounded constraints imply, for each i,

sum_t[bar g_{t,i}^T x_t]^+<=1+sum_t[bar g_{t,i}^T p_t]^+.

The first projected-point term is at most 1. For t>=2, p_t belongs to H_{t-1}. Put d_{t,i}=||bar g_{t,i}-g_i^circ||_1. The empirical-to-g_i^circ bound and optimistic feasibility give

[bar g_{t,i}^T p_t]^+
<=d_{t,i}+[g_i^circ{}^T p_t]^+
<=d_{t,i}+C/(t-1)+8sqrt(L/(t-1)).

This uses the instantaneous deviation d_{t,i}, not an invalid per-round replacement by C/T. By definition, sum_{t=2}^T d_{t,i}<=C. Therefore

sum_t[bar g_{t,i}^T x_t]^+
<=2+C+C sum_{s=1}^{T-1}1/s+8sqrt(L)sum_{s=1}^{T-1}1/sqrt(s)
<=2+2C+C ln(T)+16sqrt(TL).

The harmonic and inverse-square-root estimates follow by comparison with their integrals. The event E_g is already simultaneous over all constraints, so maximizing over i requires no additional probability loss. Its probability is at least 1-delta.

All obligations are closed. The algorithm uses neither C nor rho; these enter only the analysis.
