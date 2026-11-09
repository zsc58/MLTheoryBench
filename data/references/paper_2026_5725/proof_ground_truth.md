# Reference Proof

## Proof Structure and Obligations

1. Compute the joint retention probability conditional on the complete baseline configurations, apply the standard independent-thinning result with its hypotheses verified, and show that forgetting the marks gives a homogeneous Poisson process with the stated finite positive rate.
2. Establish independent exponential first-arrival times, verify that a unique destination wins almost surely, and compute the allocation and its softmax representation.
3. Derive the aggregate mean by conditional expectation, including zero production, and distinguish the mean decomposition given the exposure row from normalization of a positive-total mean row.
4. Prove both directions of the intensity and score equivalences, then establish uniqueness of the centered representative at the fixed temperature, including a singleton destination set.

## Complete Proof

Fix an origin \(r\) and condition throughout on its exposure row \(X_r\). Fix the same \(\tau>0\) for all score comparisons.

### 1. Effective-opportunity process

For a destination \(j\), the baseline marked Poisson process has intensity measure
\[
 dt\,a_r(u)\,d\mu(u).
\]
Condition additionally on the complete collection of baseline point configurations at all destinations. For a point at destination \(j\) with mark \(u\), the four filter decisions are conditionally independent Bernoulli variables with the prescribed probabilities. Consequently, its conditional probability of surviving every stage is
\[
 q_{rj}(u):=b(w_j,u)s(h_{rj},u)c(v_j)d(d_{rj}).
\]
This product is measurable and lies in \([0,1]\), since its factors are measurable retention probabilities. The survival indicators for distinct baseline points are independent under the same conditioning, because each is a function of its own set of conditionally independent filter decisions. Their conditional success probabilities depend only on the specified destination exposure and point mark, not on the remaining baseline configuration.

The standard independent-thinning result used here is the following: if an existing Poisson point process has intensity measure \(\nu\), and, conditional on its entire point configuration, the retention indicators for its points are independent Bernoulli variables with prescribed measurable success probabilities \(q(z)\in[0,1]\), then the retained process is Poisson with intensity measure
\[
 \nu_q(A)=\int_A q(z)\,d\nu(z).
\]
In particular, its counts on disjoint measurable sets of finite retained intensity are independent Poisson random variables with the corresponding intensity parameters. This is the independent-thinning fact indexed by theory_014.

The baseline processes are assumed to exist. The setup supplies measurable probability-valued filters and their conditional Bernoulli law given the entire baseline configurations. The product calculation above verifies precisely the conditional randomization hypothesis of the thinning result. Independence of retention indicators only after conditioning on marks would not suffice for this application. No existence assertion for arbitrary unprovided point processes is needed.

Applying the result gives a retained marked Poisson process with intensity measure
\[
 dt\,a_r(u)b(w_j,u)s(h_{rj},u)c(v_j)d(d_{rj})\,d\mu(u).
\]
For a bounded time interval \(I\), the number of retained points whose times lie in \(I\) is therefore Poisson with parameter
\[
 |I|\,d(d_{rj})c(v_j)
 \int_{\mathcal U}a_r(u)s(h_{rj},u)b(w_j,u)\,d\mu(u).
\]
Disjoint time intervals have disjoint preimages in the time-mark space, so these counts are independent. Thus forgetting the marks gives a homogeneous Poisson process on time with rate
\[
 \alpha_{rj}
 =d(d_{rj})c(v_j)\int_{\mathcal U}a_r(u)s(h_{rj},u)b(w_j,u)\,d\mu(u).
\]
The assumed positivity and finiteness ensure \(0<\alpha_{rj}<\infty\), so all bounded-interval counts used above have finite parameters.

Conditional on all baseline configurations, the destination-specific retention laws factor across destinations, and each factor depends only on that destination's configuration and the fixed exposure row. Since the baseline configurations are independent across destinations, integrating these conditional laws preserves that factorization. Hence the effective destination processes are independent given \(X_r\).

### 2. Allocation and softmax

Let \(E_{rj}\) be the first effective-opportunity time for destination \(j\). For \(t\geq0\), the Poisson zero-count probability gives
\[
 \Pr(E_{rj}>t\mid X_r)=e^{-\alpha_{rj}t}.
\]
Thus \(E_{rj}\) has an exponential distribution with rate \(\alpha_{rj}\), is finite almost surely, and has a continuous distribution. These first-arrival times are independent. Because the destination set is finite and nonempty, a first arrival exists almost surely, and ties have probability zero.

For any \(j\in\mathcal J_r\),
\[
\begin{aligned}
 \Pr(J_r=j\mid X_r)
 &=\Pr(E_{rj}<E_{rk}\text{ for all }k\ne j\mid X_r)\\
 &=\int_0^\infty
   \alpha_{rj}e^{-\alpha_{rj}t}
   \prod_{k\ne j}e^{-\alpha_{rk}t}\,dt\\
 &=\int_0^\infty \alpha_{rj}
   e^{-t\sum_k\alpha_{rk}}\,dt
 =\frac{\alpha_{rj}}{\sum_{k\in\mathcal J_r}\alpha_{rk}}.
\end{aligned}
\]
The denominator is finite and positive. If there is only one destination, the product over competitors is the empty product, equal to 1, and the same calculation applies.

Consequently,
\[
 p_{rj}=\frac{\alpha_{rj}}{\sum_k\alpha_{rk}}.
\]
Define \(f_{rj}=\tau\log\alpha_{rj}\), which is finite because \(\alpha_{rj}\) is finite and positive. Since \(e^{f_{rj}/\tau}=\alpha_{rj}\),
\[
 p_{rj}=\frac{e^{f_{rj}/\tau}}{\sum_k e^{f_{rk}/\tau}},
\]
which is the claimed softmax representation.

### 3. Aggregate mean and production scale

Conditional on \(N_r\) and \(X_r\), the \(N_r\) trips choose independently with probability vector \(p_r\). Summing their destination indicators gives
\[
 \mathbb E[Y_{rj}\mid N_r,X_r]=N_rp_{rj}.
\]
This also holds when \(N_r=0\), with the empty sum equal to zero. Moreover, \(0\leq Y_{rj}\leq N_r\), so the assumed finite conditional mean of \(N_r\) ensures finite conditional means for the counts. The tower property applies to these nonnegative random variables without an additional unconditional moment assumption. Taking conditional expectation once more gives
\[
 \lambda_{rj}:=\mathbb E[Y_{rj}\mid X_r]
 =\mathbb E[N_r\mid X_r]p_{rj}
 =\rho_rp_{rj}.
\]
In particular,
\[
 \sum_j\lambda_{rj}=\rho_r\sum_jp_{rj}=\rho_r.
\]
If \(\rho_r>0\), normalizing the mean row recovers \(p_r\):
\[
 \frac{\lambda_{rj}}{\sum_k\lambda_{rk}}=p_{rj}.
\]
If \(\rho_r=0\), nonnegativity implies \(N_r=0\) almost surely under the conditional law, and all counts and means are zero. This zero mean row cannot be normalized. The separately specified one-trip choice law \(p_r\) remains well-defined, and the identity \(\lambda_{rj}=\rho_rp_{rj}\) remains valid. No positive-production assumption is needed for the theorem.

### 4. Exact identifiability and centering

It remains to determine exactly what the allocation law identifies. Multiplying every rate in row \(r\) by any \(\kappa_r>0\) leaves its normalization unchanged. Conversely, suppose positive rate vectors \(\alpha_r\) and \(\widetilde\alpha_r\) give the same allocation. For every \(j,k\),
\[
 \frac{\widetilde\alpha_{rj}}{\widetilde\alpha_{rk}}
 =\frac{p_{rj}}{p_{rk}}
 =\frac{\alpha_{rj}}{\alpha_{rk}}.
\]
Fixing \(k\) shows \(\widetilde\alpha_{rj}=\kappa_r\alpha_{rj}\) for all \(j\), where \(\kappa_r=\widetilde\alpha_{rk}/\alpha_{rk}>0\). Thus row-wise positive rescaling is the complete intensity ambiguity.

At the same fixed temperature, this is exactly a common additive offset in score coordinates:
\[
 \widetilde f_{rj}=\tau\log\widetilde\alpha_{rj}
 =f_{rj}+\tau\log\kappa_r.
\]
Conversely, a common additive offset cancels from the softmax numerator and denominator. Any real score row corresponds to a positive intensity row by \(\alpha_{rj}=e^{f_{rj}/\tau}\). Hence two score vectors induce the same allocation if and only if their difference belongs to \(\operatorname{span}\{\mathbf 1\}\).

Let \(n_r=|\mathcal J_r|\) and
\[
 H_r=I_{n_r}-\frac1{n_r}\mathbf1\mathbf1^\top.
\]
For any score vector \(z\),
\[
 H_rz=z-\left(\frac1{n_r}\mathbf1^\top z\right)\mathbf1.
\]
Therefore \(H_rz=0\) if and only if \(z\) is constant across the row, so the nullspace of \(H_r\) is precisely \(\operatorname{span}\{\mathbf1\}\). Two scores yield the same allocation if and only if they have the same centered vector.

Moreover, \(\phi_r=H_rf_r\) has zero coordinate mean and differs from \(f_r\) by a row-constant vector. Every equivalence class \(f_r+\operatorname{span}\{\mathbf1\}\) has exactly one zero-mean member: if both \(z\) and \(z+c\mathbf1\) have zero mean, then \(c=0\). Thus \(\phi_r\) is precisely the representative identified by the destination-choice law at the fixed temperature. For \(n_r=1\), \(p_r=(1)\) and \(H_r=0\); all positive scalar intensities are related by positive rescaling, and the unique centered score is zero, so the characterization also covers this boundary case.

This is identifiability from the allocation law, not a claim that a zero-production count row identifies that law or that arrival-time observations have been supplied. The separate factor \(\rho_r\) controls the row total of the mean flow and does not enter the allocation formula. No statistical independence between production scale and exposure is required. This completes all four proof obligations.
