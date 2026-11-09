# Reference Proof

## Proof Structure

We establish local reward-quantile concentration and uniform concentration of the recomputed score correction. We control calibration drift using the score-density assumption, then combine the estimates with an index comparison and a summable pull-count argument. All probability bounds are for fixed arm-local sample counts before taking unions over counts; no concentration inequality is applied conditionally on an adaptively selected count.

## Complete Proof

All distributions and numerical parameters are fixed as the admissible integer horizon varies. If there is no suboptimal arm, both conclusions are immediate. Otherwise fix a suboptimal arm when needed below.

### Population quantiles and calibration drift

For a continuous CDF H and p in (0,1), its lower p-quantile q is finite and H(q)=p. If its density is at least h>0 on [q-r,q+r], integration gives
\[
H(q+\delta)\ge p+h\delta,\qquad H(q-\delta)\le p-h\delta
\quad(0<\delta\le r).
\]
If another CDF satisfies \(\|\widetilde H-H\|_\infty<h\delta\), then
\(\widetilde H(q-\delta)<p<\widetilde H(q+\delta)\), so its lower p-quantile lies within delta of q. The strict CDF-error premise is intentional; the unrestricted non-strict version can fail when delta=r.

The score distribution is continuous because the preimage of any score value under the maximum of the two affine score branches contains at most two reward values. Also,
\[
G_j(0)=\Pr(a_j\le Y_{j,1}\le b_j)=1-\alpha.
\]
The density lower bound around \(c_j(\alpha)\) makes it the unique point with CDF value \(1-\alpha\): any other such point would contradict strict increase immediately to the left or right of this quantile. Thus \(c_j(\alpha)=0\), and \(v_j=b_j\). In particular, the reward-density assumption includes the stated radius neighborhoods of the uncorrected anchors.

We next justify the calibration bound over the entire level interval, rather than merely inside one score neighborhood. Let p and p' belong to \([1-\overline\alpha,1-\underline\alpha]\), with \(|p'-p|<g_{\min}r_s\). The density lower bound around \(G_j^{-1}(p)\) brackets \(G_j^{-1}(p')\) inside that radius. Integrating between the two quantiles then gives
\[
|G_j^{-1}(p')-G_j^{-1}(p)|\le |p'-p|/g_{\min}.
\]
For arbitrary p,p' in the interval, subdivide the interval between them into finitely many increments smaller than \(g_{\min}r_s\), apply this estimate to each increment, and sum. Consequently,
\[
|c_j(\beta)-c_j(\alpha)|\le |\beta-\alpha|/g_{\min}.
\tag{1}
\]
This also establishes continuity of the population correction on the calibration interval.

### Local reward-quantile concentration

We use Hoeffding's inequality in the following standard form: for independent Bernoulli variables with common mean p, their empirical mean \(\overline Z_m\) satisfies
\[
\Pr(\overline Z_m-p\ge u)\le e^{-2mu^2},\qquad
\Pr(p-\overline Z_m\ge u)\le e^{-2mu^2}.
\]
For an empirical lower tau-quantile \(\widehat q_m\), its upper deviation past \(q+\varepsilon\) forces the empirical CDF there below tau. Its population CDF is at least \(\tau+f_{\min}\varepsilon\). The lower deviation similarly forces the empirical CDF at \(q-\varepsilon\) to be at least tau, although its expectation is at most \(\tau-f_{\min}\varepsilon\). The empirical CDF values are averages of independent Bernoulli variables because the fixed arm-local rewards are i.i.d. Hence
\[
\Pr(|\widehat q_m-q|>\varepsilon)
\le 2e^{-2m\varepsilon^2f_{\min}^2},
\qquad 0<\varepsilon\le r_y.
\tag{2}
\]
The same bound for a non-strict error event follows by taking positive thresholds increasing to epsilon. We will only need the strict form below.

### Uniform recomputed-score concentration

Fix an arm j, a local time s, and m=s-1. Form the oracle scores
\(S_i=s(Y_{j,i};a_j,b_j)\), and let \(\widehat G_m^\circ\) be their empirical CDF. These scores are i.i.d., being the same deterministic function of the i.i.d. arm-local rewards. The standard DKW inequality with Massart's constant states that
\[
\Pr(D_m>u)\le2e^{-2mu^2},\qquad
D_m=\|\widehat G_m^\circ-G_j\|_\infty.
\]
Taking thresholds increasing to u also gives \(\Pr(D_m\ge u)\le2e^{-2mu^2}\).

Let \(0<\varepsilon\le\rho\). On \(D_m<g_{\min}\varepsilon/2\), the strict-premise inverse-CDF fact gives an oracle empirical quantile error at most epsilon/2 simultaneously for every calibration level. The radius condition holds because \(\varepsilon/2\le r_s\). Therefore, writing \(\widehat c_{j,s}^\circ(\beta)\) for the oracle empirical correction,
\[
\Pr\left(\sup_\beta|\widehat c_{j,s}^\circ(\beta)-c_j(\beta)|>\varepsilon/2\right)
\le 2e^{-m\varepsilon^2g_{\min}^2/2}.
\tag{3}
\]
All suprema here and below range over \([\underline\alpha,\overline\alpha]\). They are measurable: each empirical quantile function has finitely many rank intervals, while the population quantile function is continuous, so the supremum is determined by finitely many interval endpoints and one-sided limits.

The inequality \(|\max(x_1,x_2)-\max(y_1,y_2)|\le\max_i|x_i-y_i|\) shows that the recomputed and oracle scores differ coordinatewise by at most
\[
E_{j,s}=|\widehat a_{j,s}-a_j|+|\widehat b_{j,s}-b_j|.
\]
If two vectors differ coordinatewise by at most E, their kth order statistics differ by at most E: the k coordinates below the kth order statistic of either vector give the corresponding upper bound for the other vector, and the reverse inequality follows by interchanging them. Their lower empirical quantiles therefore differ by at most E at every level.

If \(E_{j,s}>\varepsilon/2\), at least one anchor error exceeds epsilon/4. Applying (2) to both anchors and using \(\varepsilon/4\le r_y\) yields
\[
\Pr(E_{j,s}>\varepsilon/2)\le4e^{-m\varepsilon^2f_{\min}^2/8}.
\]
Combining this with (3) gives the strict uniform-error bound. Taking positive thresholds increasing to epsilon gives its non-strict version, without changing constants, even at epsilon=rho:
\[
\Pr\left(\sup_\beta|\widehat c_{j,s}(\beta)-c_j(\beta)|\ge\varepsilon\right)
\le2e^{-m\varepsilon^2g_{\min}^2/2}
+4e^{-m\varepsilon^2f_{\min}^2/8}.
\tag{4}
\]
The uniform event controls evaluation at the random level \(\beta_{j,s}\) pathwise; independence of that level and the sample is neither assumed nor needed.

### Endpoint concentration at decision times

For fixed t<=n and s_0<=m<=t-1, put
\[
d_{m,t}=b\sqrt{\frac{\log t}{m}},\qquad x_{m,t}=d_{m,t}/4.
\]
Initialization ensures \(x_{m,t}\le\rho\). The source update at local time m outputs \(\beta_{j,m+1}\), so projection and (1) imply
\[
|c_j(\beta_{j,m+1})|
\le\frac{\lambda}{g_{\min}}\sqrt{\frac{\log m}{m}}
\le d_{m,t}/4.
\tag{5}
\]
Decompose
\[
\widehat V_{j,m+1}-v_j
=(\widehat b_{j,m+1}-b_j)
+(\widehat c_{j,m+1}(\beta_{j,m+1})-c_j(\beta_{j,m+1}))
+c_j(\beta_{j,m+1}).
\]
If the absolute values of both random error terms are at most d_{m,t}/4, (5) bounds the total error by \(3d_{m,t}/4<d_{m,t}\). Thus even the non-strict event with total error at least d_{m,t} is contained in the union of the two strict random-error events at threshold d_{m,t}/4. Applying (2) and (4) gives
\[
\Pr\bigl(|\widehat V_{j,m+1}-v_j|\ge d_{m,t}\bigr)
\le2t^{-b^2f_{\min}^2/8}
+2t^{-b^2g_{\min}^2/32}
+4t^{-b^2f_{\min}^2/128}
\le8t^{-4}.
\tag{6}
\]
Here \(b\ge64/h_{\min}\) makes the three exponents at least 512, 128, and 32, respectively. All applications are inside their local density radii. These are unconditional fixed-count estimates; no independence across arms is required.

### Index comparison and pull counting

Fix j!=A and let
\[
\ell_j=\left\lceil\frac{4b^2\log n}{\Delta_j^2}\right\rceil\vee s_0.
\]
Suppose j is selected after initialization at time t, with \(m=T_j(t-1)\ge\ell_j\) and \(m_A=T_A(t-1)\). Define the bad events
\[
\widehat V_{A,m_A+1}\le v_A-d_{m_A,t},\qquad
\widehat V_{j,m+1}\ge v_j+d_{m,t}.
\]
If neither occurs, the optimal index is strictly greater than v_A, while the selected index is strictly less than \(v_j+2d_{m,t}\). Since the selected index is at least the optimal index, this would imply \(\Delta_j<2d_{m,t}\). But m>=ell_j and t<=n give \(2d_{m,t}\le\Delta_j\), a contradiction. Thus a selected suboptimal arm beyond the threshold requires one of the two bad events. This argument includes arbitrary index ties.

For each fixed t there are at most t^2 possible count pairs. Equation (6) and a union bound therefore imply
\[
\Pr\{I_t=j,\ T_j(t-1)\ge\ell_j\}\le16t^{-2}
\]
for post-initialization times. At most ell_j pulls occur before reaching the threshold, including initialization, so
\[
\mathbb E[T_j(n)]\le\ell_j+16\sum_{t=1}^{\infty}t^{-2}.
\tag{7}
\]
This also holds if ell_j exceeds n.

The gap-radius assumptions give \(\rho\ge\Delta_j/8\). With \(L_j=4b^2\log n/\Delta_j^2\), it follows that
\[
s_0\le\lceil L_j\rceil\vee2,\qquad
\ell_j\le L_j+2.
\]
Thus (7) proves the desired result, for example with the finite horizon-independent choice
\[
B_j=2+16\sum_{t=1}^{\infty}t^{-2}.
\]
Multiplying by the fixed gaps and summing over the finite set of suboptimal arms yields
\[
R_n\le\sum_{j\ne A}\frac{4b^2\log n}{\Delta_j}
+\sum_{j\ne A}\Delta_j B_j,
\]
whose final term is independent of n.

## Source-Local Repairs and Obligation Closure

The inverse-CDF lemma uses the strict error premise appearing in its source proof. Elementary limits recover all non-strict concentration bounds, including the boundary radius. The source's final undefined gap symbol is interpreted as the upper-tail gap, as already recorded for theory_004. The reward-quantile argument, uniform oracle comparison, order-statistic perturbation, calibration drift, fixed-count concentration, tie-safe index comparison, initialization, and regret summation are all derived above. The only external results are the explicitly stated Hoeffding and DKW inequalities, with their independence hypotheses verified. No unresolved proof obligation remains.
