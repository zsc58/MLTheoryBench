# Reference Proof

## Contract and obligations

Write V=V_T and let r_t=max_i mu_i(t)-mu_{I_t}(t). The public regret is R_T=E sum_{t=1}^T r_t. The means are fixed, non-increasing functions; V bounds both their range and their total variation. It need not equal realized variation. Constants may depend on the fixed tuning parameter alpha.

The theorem-critical obligations are: concentration under adaptive sampling; the selected-arm comparison for each of the two specified algorithms; first-pull and failure control; the later-pull batch estimate and endpoint-safe optimization; the Gaussian epoch information calculation; and the exact lower-bound constant, including rounding and saturation. Each is derived below.

## 1. Concentration under adaptive sampling

Index an arm's observations by its successive pulls, and subtract the mean at the corresponding calendar time. The resulting noise sequence need not be independent. Its conditional exponential moments nevertheless satisfy the same sigma^2-sub-Gaussian bound: sampling decisions are made before observing the next noise. This follows by conditioning at each possible next pull time and applying the conditional observation bound. For a finite-horizon argument, one may continue the sampling sequence after T with zero centered observations; these satisfy the same bound.

Consequently, for a fixed block of h successive pull-indexed noises, iterated conditional expectation gives

E exp(lambda sum noise) <= exp(h sigma^2 lambda^2/2).

Markov's inequality, optimized over lambda and applied to both signs, gives probability at most delta_t that its average exceeds c(h,delta_t) in absolute value. For sigma=0 the centered observations vanish almost surely and the same conclusion holds directly.

For RAW-UCB, union-bound over K arms and all endpoint-length pairs 1<=h<=n<=t-1. Define G_t to be the event that all these blocks are accurate at radius c(h,delta_t). Then

P(G_t^c) <= K t(t-1)delta_t/2 <= Kt^{2-alpha}.

For the geometric algorithm, count only blocks actually created by its deterministic pull-index refresh schedule. Level zero creates at most t-1 blocks per arm. Level j>=1 creates at most (t-1)/2^{j-1} blocks. Their total is at most 3t per arm. Defining G_t using these blocks gives

P(G_t^c) <= 3Kt delta_t = 6Kt^{1-alpha}.

The events include every statistic used at decision time t, despite the random arm counts. Neither calculation assumes independence between statistics or between pull-indexed noises.

## 2. Selected-window comparison

Let mu_*(t)=max_i mu_i(t), and let bar_mu_{i,h}(t) denote the average of the true means associated with arm i's last h observations before t.

For RAW-UCB, every past mean of a best current arm is at least its current mean, not at most it. On G_t, each of that arm's empirical upper confidence values is therefore at least mu_*(t). Its minimum index is also at least mu_*(t). Maximal-index selection and concentration imply, for every available window h of the selected arm,

mu_*(t) <= I_{I_t}(t) <= hat_mu_{I_t,h}(t)+c(h,delta_t) <= bar_mu_{I_t,h}(t)+2c(h,delta_t).

Thus its comparison constant is C_R=2sqrt(2alpha), in the form

mu_*(t)-bar_mu_{I_t,h}(t) <= C_R sigma sqrt(log(t)/h).

For the geometric algorithm, every stored block is also composed of past observations. The same optimism and maximal-index argument shows that each stored true mean of the selected arm, at level 2^j, is at least mu_*(t)-2c(2^j,delta_t).

It remains to pass from stored blocks to an arbitrary last-h average. Set q=floor(log_2(h+1)) and H=2^q-1. Then H<=h<2^{q+1}, and monotonicity gives bar_mu_{I_t,h}(t)>=bar_mu_{I_t,H}(t). Index observations by age, with age 1 most recent. Partition ages 1,...,H into blocks [2^j,2^{j+1}-1], j=0,...,q-1. The block at level j has length 2^j. The stored statistic of that level ends fewer than 2^{j-1} pulls before the current endpoint when j>=1, and ends at the current endpoint when j=0. Its samples are therefore no older, coordinate by coordinate, than the corresponding age block. Since earlier means are larger, the age-block true average is at least the stored true average.

It follows that

bar_mu_{I_t,h}(t) >= mu_*(t)-2 sum_{j=0}^{q-1} [2^j/(2^q-1)]c(2^j,delta_t).

The sum equals

c(1,delta_t)/[(sqrt(2)-1)(2^{q/2}+1)] <= [sqrt(2)/(sqrt(2)-1)]c(h,delta_t).

Hence the geometric algorithm has the same arbitrary-window comparison with C_E=4sqrt(alpha)/(sqrt(2)-1):

mu_*(t)-bar_mu_{I_t,h}(t) <= C_E sigma sqrt(log(t)/h).

In what follows C denotes the appropriate one of these constants.

## 3. First pulls and failures

Partition the horizon into M nonempty consecutive batches. Initialization is handled directly, not by a concentration assertion before every arm has been observed.

For each arm, charge its initial pull by -mu_i at that pull, which upper-bounds its regret because mu_*<=0. At a later favorable first pull of that arm in a batch, let s be the preceding pull time of the arm. The h=1 comparison bounds its regret by

C sigma sqrt(log T) + mu_i(s)-mu_i(t).

All such decrement terms are nonnegative. For each arm their intervals are disjoint consecutive-pull intervals. Together with the initial charge they sum to at most -mu_i(T)<=V. Thus the initial pulls and all favorable batch-first pulls cost at most

C sigma min(MK,T)sqrt(log T)+KV.

At a bad round after initialization, r_t<=V. For RAW-UCB with alpha>=4, expected bad-round cost is at most KV sum_{t>K}t^{-2}<=V. For the geometric algorithm with alpha>=3, it is at most 6KV sum_{t>K}t^{-2}<=6V<=3KV, since K>=2. In particular a common bound of 6KV covers the telescoping and failure contributions together.

## 4. Later pulls and the batch bound

Choose M nearly equal batches with lengths tau_k in {floor(T/M),ceil(T/M)}. In batch k let A_k be the nonempty set of arms pulled, n_{i,k} their pull counts, and D_{i,k} the decrease in arm i's mean from the first to the last calendar time of the batch.

At its ell-th pull in this batch, ell>=2, the arm's last ell-1 observations all belong to the batch. Their true average exceeds the current mean by at most D_{i,k}. On G_t, therefore,

r_t <= D_{i,k}+C sigma sqrt(log T/(ell-1)).

The total decrement charge in batch k is bounded by

sum_{i in A_k}(n_{i,k}-1)D_{i,k} <= (tau_k-|A_k|)max_i D_{i,k} <= (T/M)max_i D_{i,k}.

The last step uses |A_k|>=1 and ceil(T/M)-1<=T/M. Only transitions inside batches are counted, so

sum_k max_i D_{i,k} <= sum_{t=1}^{T-1}max_i[mu_i(t)-mu_i(t+1)] <= V.

For the confidence terms, sum_{ell=2}^n(ell-1)^{-1/2}<=2sqrt(n). Cauchy-Schwarz across at most MK arm-batch pairs and sum n_{i,k}=T gives total at most 2C sigma sqrt(MKT log T). Thus, for every 1<=M<=T,

R_T <= VT/M + 2C sigma sqrt(MKT log T) + C sigma min(MK,T)sqrt(log T) + 6KV.

When M=T there are no later pulls, so the sharper version is R_T<=C sigma T sqrt(log T)+6KV, with no decrement or later-pull confidence term.

## 5. Optimization and endpoints

If V=0, all means are zero and regret is zero. If sigma=0, all comparisons are exact and singleton batches give R_T<=KV directly from the first-pull telescope.

Otherwise set q=(V^2 T/(C^2 sigma^2 K log T))^{1/3}.

If q<1, choose M=1. Then VT<C sigma sqrt(KT log T), and K<=sqrt(KT), so the bound is O(C sigma sqrt(KT log T)+KV).

If 1<=q<=T, choose M=ceil(q). Then q<=M<=2q. Define

A=(C^2 sigma^2 VKT^2 log T)^{1/3},
B=(C sigma V^2 K^2 T sqrt(log T))^{1/3}.

The decrement and later-pull confidence terms are O(A), and the first-pull confidence term is O(B). Since B^2=A KV, we have B<=A+KV. This gives O(A+KV).

If q>T, choose singleton batches. The defining inequality implies V>C sigma T sqrt(K log T), so C sigma T sqrt(log T)<=KV. Hence the bound is O(KV).

Combining cases proves the public upper rate with constants depending only on the fixed alpha and the chosen algorithm. The partition is solely an analysis device: neither algorithm uses T or V.

## 6. Epoch information calculation

Assume sigma>0. Use M nearly equal epochs, indexed k=0,...,M-1, and choose a designated arm a_k separately in each epoch. Its mean is -k Delta; all other means are -(k+1)Delta. Take independent Gaussian observation noise of variance sigma^2. Every arm is non-increasing, its range is contained in [-M Delta,0], and each boundary decrement is at most 2Delta. Thus sufficient budget conditions are M Delta<=V and 2(M-1)Delta<=V.

Fix the designated arms outside epoch k. Let P_0 be the experiment in which all arms have mean -(k+1)Delta in epoch k, and let P_i raise arm i's mean there by Delta. Their distributions before the epoch coincide. The sequential likelihood ratio has identical policy factors in numerator and denominator; observation factors differ only when arm i is pulled during the epoch. The expected Gaussian log likelihood ratio on each such pull is Delta^2/(2sigma^2). Thus, for the transcript through the epoch,

KL(P_0,P_i)=Delta^2 E_0[N_i^k]/(2sigma^2).

For completeness, the probability inequality needed here follows from elementary convexity. Apply the log-sum inequality to an event and its complement to obtain KL(P,Q)>=kl(P(A),Q(A)). As a function of its first argument, binary relative entropy has second derivative 1/[p(1-p)]>=4 and value and first derivative zero at p=q. Hence kl(p,q)>=2(p-q)^2. Taking the supremum over events gives TV(P,Q)<=sqrt(KL(P,Q)/2). Integration of indicator level sets then yields |E_P Z-E_Q Z|<=b TV(P,Q) for 0<=Z<=b.

Apply this with Z=N_i^k and b=tau_k. Averaging over i and using Cauchy-Schwarz and sum_i E_0 N_i^k=tau_k gives

(1/K)sum_i E_i N_i^k <= tau_k/K + Delta tau_k^{3/2}/(2sigma sqrt(K)).

Average independently and uniformly over the designated arms in every epoch. The average regret is consequently at least

Delta[T(1-1/K)-Delta sum_k tau_k^{3/2}/(2sigma sqrt(K))].

Since tau_k<=2T/M and sum tau_k=T, the sum of their three-halves powers is at most T sqrt(2T/M).

## 7. Exact lower bound, rounding, and saturation

Suppose V>=sigma sqrt(K/(8T)), and set x=(V^2 T/(Ksigma^2))^{1/3}>=1/2.

First suppose x<=T/2. Choose M=floor(2x), so 1<=M<=T and x<=M<=2x. Set Delta=sigma sqrt(KM/T)/(4sqrt(2)). If M>=2, the condition 2MDelta<=V follows from M<=2x, and implies both budget requirements. If M=1, the same inequality is sufficient and still follows from M<=2x. Thus all constructed instances satisfy the full range and variation contract.

The information penalty inside the square brackets is at most T/8. Since K>=2, the average regret is at least

3Delta T/8 = [3/(32sqrt(2))]sigma sqrt(KTM)
>= [1/(16sqrt(2))]sigma sqrt(KT)sqrt(x)
= [1/(16sqrt(2))](sigma^2 VKT^2)^{1/3}.

Now suppose x>T/2. Use M=T singleton epochs and Delta=V/(2T). The means lie in [-V/2,0], and total variation is at most V(T-1)/T. Because each epoch's designated arm is independent and uniform before that round's observation, any policy chooses it with probability 1/K under the averaged experiment. Average regret is therefore (1-1/K)TDelta>=V/4.

Here V^2>sigma^2 KT^2/8, so (sigma^2 VKT^2)^{1/3}<2V. Its required multiple is less than V/(8sqrt(2)), which is below V/4. Thus this case also proves the exact target.

In either case, some fixed designated-arm vector has regret at least the average. Its means are fixed in advance; no adaptive environment or advance disclosure is used. The argument applies to randomized policies by including their independent randomization in the transcript. If sigma=0, the lower target is zero and an all-zero instance suffices.

## Source-local repairs used

The proof explicitly replaces the optional-skipping independence assertion by conditional exponential moments; normalizes the favorable-event and decision-time notation; retains the sharper epoch estimate and treats saturation; restricts batch sums to pulled arms and transitions before T; excludes initialization from failure probabilities; and retains the appendix's KV boundary term. These are recorded in provenance. All theorem-critical obligations listed at the start are closed.
