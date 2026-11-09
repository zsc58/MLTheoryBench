# Reference Proof

## Proof Structure

The proof has four parts. First, exponential clocks and conditioning on the clocks outside a fixed `K`-set give exact cancellation of its conditional inclusion probability. Second, the joint density of the retained set and threshold permits differentiation under the integral after the same cancellation removes all reciprocal inclusion factors. Third, an exponential-race calculation gives an integral representation of the sequential without-replacement set probability and hence the factorized integral for the estimator. Finally, reward ordering partitions the subsets by their first index, and elementary-symmetric recurrences evaluate the resulting sum.

## Complete Proof

Fix `theta` and abbreviate `p_i=p_i(theta)`.

### 1. Unbiasedness

Set `T_i=exp(-Y_i)`. Since `Y_i=log p_i+xi_i` with standard Gumbel `xi_i`, the variables `T_i` are independent exponentials with rates `p_i`. Thus `A` consists of the indices of the `n` smallest clocks, and `tau=exp(-kappa)` is the `(n+1)`-st smallest clock.

Fix a set `S` of size `K`. Condition on all clocks with indices outside `S`, and let `b` be the `(n-K+1)`-st smallest among these `M-K` clocks. This order statistic exists because `M>=n+1`. Except on a null tie event,

`S subset A` if and only if `T_i<b` for every `i in S`.

Indeed, if all these clocks are below `b`, exactly `n-K` outside clocks also precede `b`, so these `n` clocks form the retained pool and the next clock is `b`. Conversely, if `S subset A`, the other `n-K` retained clocks must be the smallest outside clocks; the next outside clock is therefore the overall threshold. Consequently, on the inclusion event `tau=b`. Conditional independence gives

`E[ 1{S subset A} / product_{i in S} q_i(kappa) | (T_j)_{j notin S} ]`
`= product_{i in S}(1-exp(-p_i b)) / product_{i in S}(1-exp(-p_i b)) = 1`.

Multiplying by the deterministic coefficient `P_theta(S) r_S`, where `r_S=max_{i in S}r_i`, and summing over all `K`-sets yields

`E_theta[widehat L] = sum_{|S|=K}P_theta(S)r_S = L_K(theta)`.

These expectations are absolutely integrable: each reciprocal-inclusion term with its indicator is nonnegative with expectation one, and there are finitely many bounded reward coefficients.

### 2. Exact gradient identity

It remains to justify differentiation rather than merely invoke a formal score identity. Work in the threshold coordinate `tau=exp(-kappa)`. For a retained set `A`, threshold index `m notin A`, and `tau>0`, independence of the clocks gives the joint density

`tilde f_theta(A,m,tau)`
`= p_m exp(-(1-sum_{i in A}p_i)tau) product_{i in A}(1-exp(-p_i tau))`.

Its support consists of all such pairs `(A,m)` and all positive `tau`, independently of `theta`. The density in the `kappa` coordinate differs by the Jacobian factor `tau`, which is independent of `theta`; hence its score is the same.

For `S subset A`, multiply the corresponding summand of `widehat L` by this density. Every denominator indexed by `S` cancels, leaving

`P_theta(S) r_S p_m exp(-(1-sum_{i in A}p_i)tau)`
`times product_{i in A\S}(1-exp(-p_i tau))`.

Choose a compact neighborhood of the parameter under consideration contained in `Theta`. By positivity and continuous differentiability, throughout this neighborhood all probabilities are at least some `p_min>0`, while their first derivatives are bounded. The finite sequential formula for `P_theta(S)` and its derivative are also bounded there: at every one of its first `K` stages the remaining mass is at least `(M-K+1)p_min`, so its denominators are uniformly separated from zero.

The complement of every retained set has `M-n` indices, and hence

`1-sum_{i in A}p_i >= (M-n)p_min`.

Differentiating the displayed cancelled expression introduces only bounded coefficients and at most one factor proportional to `tau`. Thus its value and first derivative are bounded by

`C(1+tau) exp(-(M-n)p_min tau)`,

for a constant `C` independent of `A,m,S` and of the parameter in the chosen neighborhood. This envelope is integrable on `(0,infinity)`. There are only finitely many configurations and subsets, so dominated differentiation gives

`grad_theta E_theta[widehat L]`
`= E_theta[grad_theta widehat L + widehat L grad_theta log f_theta(Z)]`.

Pointwise, the density times the vector inside this last expectation is the derivative of `widehat L` times the density as a product. The same envelope therefore also proves absolute integrability of the combined gradient estimator. The stop-gradient operator changes derivatives but not the realized value in the second term, so the right side is `E_theta[widehat g]`. Combining this with the already proved identity `E_theta[widehat L]=L_K(theta)` gives

`E_theta[widehat g]=grad_theta L_K(theta)`.

### 3. Integral factorization

Independent exponential clocks also realize the sequential without-replacement law: the first clock has index `i` with probability `p_i`, and the memoryless property gives the successive conditional probabilities in the definition of `P_theta(S)`.

Fix a `K`-set `S`. It is the set of the `K` smallest clocks exactly when the largest clock within `S` precedes every clock outside `S`. If `i in S` is the member attaining that largest clock at time `x`, its contribution has density

`p_i exp(-p_i x) product_{ell in S\{i}}(1-exp(-p_ell x)) product_{j notin S}exp(-p_j x)`.

Because `sum_j p_j=1`, factoring `exp(-p_ell x)` from every factor indexed by `ell in S\{i}` turns this into

`exp(-x) p_i product_{ell in S\{i}}(exp(p_ell x)-1)`.

Summing over `i in S` and integrating proves

`P_theta(S)=integral_0^infinity exp(-x) [sum_{i in S}p_i product_{ell in S\{i}}(exp(p_ell x)-1)] dx`.

Substitute this finite-sum identity into `widehat L` and interchange the finite subset sum with the integral. For each `S subset A`,

`[1/product_{i in S}q_i(kappa)] sum_{i in S}p_i product_{ell in S\{i}}(exp(p_ell x)-1)`
`= (product_{i in S}h_i(x))(sum_{i in S}c_i(x))`.

For completeness, this expression causes no endpoint integrability problem. Put `P_S=sum_{i in S}p_i` and let

`H_S(x)=exp(-x)(product_{i in S}h_i(x))(sum_{i in S}c_i(x))`.

The exact finite-sum expression gives, for every `x>0`,

`0 <= H_S(x) <= [1/product_{i in S}q_i(kappa)] sum_{i in S}p_i exp(-(1-P_S+p_i)x)`.

Here each `q_i(kappa)>0`, and each exponential rate `1-P_S+p_i` is positive. The bound follows directly from `exp(p_ell x)-1 <= exp(p_ell x)`. It is integrable on the entire positive half-line. Thus the finite reward-weighted sum is absolutely integrable, including for signed or zero rewards and for `K=1`.

The factorization, together with the recurrence verification below, proves the exact identity

`widehat L=integral_0^infinity exp(-x)F(x)dx`.

Private source-repair note: the supplementary asymptotic at source line 148 omits a multiplicity. If `p_min,S=min_{i in S}p_i` and `d_S=|{i in S:p_i=p_min,S}|`, the correct equivalence is

`H_S(x) ~ [d_S p_min,S/product_{i in S}q_i(kappa)] exp(-(1-P_S+p_min,S)x)`.

Indeed, each summand indexed by `i` has leading coefficient `p_i/product_{j in S}q_j(kappa)` and rate `1-P_S+p_i`; precisely the `d_S` minimum-rate summands contribute to the leading coefficient. This corrects only the coefficient, not the source's positive decay rate or integrability conclusion. The upper bound above makes the proof independent of this asymptotic calculation.

### 4. Dynamic program and cost

Fix `x>0` and use the reward ordering `a_1,...,a_n`. Every `K`-subset of `A` has a unique smallest ordered index `j`; its maximum reward is `r_{a_j}`, including under arbitrary deterministic tie-breaking. Write its remaining indices as a `(K-1)`-subset of `{a_{j+1},...,a_n}`.

Before iteration `j`, the recurrence arrays satisfy the invariants

`E_s = sum_{T subset {a_{j+1},...,a_n}, |T|=s} product_{i in T}h_i(x)`,

`G_s = sum_{T subset {a_{j+1},...,a_n}, |T|=s} (product_{i in T}h_i(x))(sum_{i in T}c_i(x))`.

The initialization gives these formulas for the empty suffix. For a subset whose smallest index is `j`, summing over its remaining set `T` gives exactly

`r_{a_j}h_{a_j}(x)(c_{a_j}(x)E_{K-1}+G_{K-1})`.

Such a subset can exist only when `j<=n-K+1`; otherwise both relevant size-`K-1` sums vanish. These contributions partition all `K`-subsets, proving the formula for `F(x)` used by the algorithm.

When `a_j` is inserted into the suffix, a size-`s` subset either omits it or consists of it and a previous size-`s-1` subset. The product sum therefore changes by `h_{a_j}E_{s-1}`. For the weighted sum, the new subsets contribute

`h_{a_j}(G_{s-1}+c_{a_j}E_{s-1})`.

These are precisely the stated updates. Descending `s` ensures that every right-hand side uses the old suffix values, completing the induction. Only degrees through `K-1` are needed. The argument also covers `K=1`, where `E_0=1`, `G_0=0`, and the update loop is empty.

Sorting costs `O(n log n)`. Each node requires `O(nK)` arithmetic and `O(K)` working memory. Therefore the `Q`-node Gauss-Laguerre expression is computed in `O(n log n+nKQ)` time. This is the evaluation cost given the retained probabilities and rewards, not a cost for sampling, computing rewards, or obtaining policy probabilities. The subset sum at every node and the integral identity are exact; the proof makes no claim that a finite-`Q` quadrature equals the integral.
