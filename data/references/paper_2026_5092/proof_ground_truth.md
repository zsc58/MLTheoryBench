# Reference Proof

## Proof Structure

Verify the rate model and finiteness of the optimal loss, identify the tilted local posterior by conditional reweighting, reduce the objective to cross-entropy against that posterior, and identify normalized excess loss with path-space KL before passing to the terminal marginal.

## Complete Proof

### 1. Process domain, endpoint, and schedule-weighted exposure

Write \(N=|V|\). On every compact interval \([0,b]\subset[0,1)\), the hazard is bounded: \(\alpha\) is smooth and \(1-\alpha\) is bounded away from zero there. For every measurable probability-kernel family, the stated rates therefore define a finite-state inhomogeneous jump process on that interval. The constructions agree on overlapping intervals. Every jump permanently reveals one coordinate, so there are at most \(L\) jumps and the terminal left limit exists.

For any candidate kernel and coordinate \(i\), let \(S_i(t)=\mathbb P_q(X_t^i=\mathtt m)\). The total rate of revealing that coordinate, while it remains masked, is \(\lambda(t)\), independently of its token probabilities. Summing the finite-state forward equations over states with coordinate \(i\) masked gives
\[
S_i'(t)=-\lambda(t)S_i(t),\qquad S_i(0)=1.
\]
Consequently, for \(t<1\),
\[
S_i(t)=\exp\!\left(-\int_0^t\lambda(s)\,ds\right)=1-\alpha(t).
\]
Since this tends to zero, every coordinate is revealed strictly before time 1 almost surely. Thus the terminal law of every candidate is a probability law on \(V^L\). The same calculation applies to \(\mathbb P^0\) and \(\mathbb P^+\). In particular,
\[
\int_0^1\lambda(t)\mathbb E_j\!\left[\sum_{i:X_t^i=\mathtt m}1\right]dt
=L\int_0^1\alpha'(t)\,dt=L,\qquad j\in\{0,+\}.
\tag{1}
\]
The measure defining the public almost-everywhere qualification is therefore finite. These conclusions also cover schedules with intervals of zero derivative.

### 2. Conditional reweighting and the signed target

Because \(V^L\) is finite and \(r\) is real-valued, there are constants \(0<w_{\min}\leq W\leq w_{\max}<\infty\). The common conditional path law given the terminal sequence and the terminal tilt imply
\[
\frac{d\mathbb P^+}{d\mathbb P^0}=\frac WZ.
\tag{2}
\]
Indeed, disintegrating either path law over its finite terminal state space gives the same conditional path probabilities multiplied by terminal masses whose ratio is \(W/Z\). In particular the two path laws are equivalent.

Put \(M_t=\mathbb E_0[W\mid X_t]\). On supported states, \(w_{\min}\leq M_t\leq w_{\max}\). Applying (2) to a conditional indicator, or directly dividing the corresponding weighted joint probability by the weighted marginal probability, gives
\[
q_t^+(v\mid X_t,i)
=\frac{\mathbb E_0[W\mathbf1\{X_1^i=v\}\mid X_t]}{M_t}.
\tag{3}
\]
All random variables used here are bounded. Unsupported conditioning states do not affect any subsequent integral.

Expanding the specified target and using the definition of \(q^0\),
\[
\begin{aligned}
\mathbb E_0[WT_c(v\mid X_t,i,X_1)\mid X_t]
&=c q_t^0(v\mid X_t,i)
 +\mathbb E_0[(W-c)\mathbf1\{X_1^i=v\}\mid X_t]\\
&=\mathbb E_0[W\mathbf1\{X_1^i=v\}\mid X_t]\\
&=M_tq_t^+(v\mid X_t,i).
\end{aligned}
\tag{4}
\]
This is a coefficient identity; it does not require \(T_c\) to be a probability vector. The public conditional-averaging convention and (4) consequently give, including candidate kernels with zeros,
\[
\mathcal L_c(q)=\int_0^1\lambda(t)\mathbb E_0\!\left[
 M_t\sum_{i:X_t^i=\mathtt m}
 \operatorname{CE}(q_t^+(\cdot\mid X_t,i)\|q_t(\cdot\mid X_t,i))
\right]dt.
\tag{5}
\]
The coefficients after conditional averaging are nonnegative, so this is a well-defined nonnegative extended-real integral.

For every nonnegative state function \(F_t\), (2) and the tower property give
\[
\mathbb E_0[M_tF_t(X_t)]=Z\mathbb E_+[F_t(X_t)].
\tag{6}
\]
Thus (5) also equals \(Z\) times its cross-entropy integral under \(\mathbb P^+\). In particular, using entropy at most \(\log N\) and (1),
\[
0\leq\mathcal L_c(q^+)\leq ZL\log N<\infty.
\tag{7}
\]
For \(N=1\), this bound is zero. No full-support assumption on either terminal distribution is needed.

### 3. Excess loss and uniqueness

For probability vectors, with the stated zero conventions,
\[
\operatorname{CE}(p\|q)=H(p)+\operatorname{KL}(p\|q),
\]
where \(H(p)\) is finite. Gibbs' inequality gives \(\operatorname{KL}(p\|q)\geq0\), with equality exactly when \(p=q\), including when \(p\) has zero coordinates. For example, applying \(-\log u\geq1-u\) on the support of \(p\) shows nonnegativity, and equality forces agreement there and no remaining mass outside that support.

Apply this identity in (5). Since (7) is finite, subtraction is legitimate even if \(\mathcal L_c(q)=+\infty\), and
\[
\mathcal L_c(q)-\mathcal L_c(q^+)
=\int_0^1\lambda(t)\mathbb E_0\!\left[
 M_t\sum_{i:X_t^i=\mathtt m}
 \operatorname{KL}(q_t^+(\cdot\mid X_t,i)\|q_t(\cdot\mid X_t,i))
\right]dt.
\tag{8}
\]
Because \(M_t\) is bounded above and bounded away from zero on supported states, (8) vanishes exactly when the local kernels agree almost everywhere under the public measure \(\mu\). This proves the first claim.

Using (6) in (8) and nonnegativity to justify the integrations gives
\[
\frac{\mathcal L_c(q)-\mathcal L_c(q^+)}Z
=\int_0^1\lambda(t)\mathbb E_+\!\left[
\sum_{i:X_t^i=\mathtt m}
\operatorname{KL}(q_t^+(\cdot\mid X_t,i)\|q_t(\cdot\mid X_t,i))
\right]dt.
\tag{9}
\]

### 4. Path KL, including zeros and infinite values

We derive the needed likelihood formula directly for this finite-jump process. Given a current state with \(k\) masked coordinates at time \(s\), the probability of no next event before \(t\) is
\[
\exp\!\left(-k\int_s^t\lambda(u)\,du\right).
\]
The density of the next event revealing a particular masked coordinate \(i\) to token \(v\) at time \(t\) is this survival factor times
\(\lambda(t)q_t(v\mid x,i)\). Summing over \(v\) shows that the law of the next event time and coordinate is independent of the token kernel. Iterating proves that all candidates have the same law \(\nu\) of ordered event times and coordinate indices. There are exactly \(L\) events almost surely, all before time 1, by Step 1.

Relative to \(\nu\) times counting measure on the \(L\) token choices, the path density for a kernel \(q\) is
\[
f_q=\prod_{j=1}^Lq_{t_j}(v_j\mid x_{j-1},i_j),
\tag{10}
\]
where \(x_{j-1}\) is the pre-jump state determined by the preceding choices. These densities normalize because each successive token kernel is a probability vector. Formula (10) is also a direct verification of cancellation of all holding-rate and coordinate-selection factors.

For probability vectors \(p,q\), the negative part of the token log ratio has the bound
\[
\sum_{v:0<p(v)<q(v)}p(v)\log\frac{q(v)}{p(v)}\leq\frac1e.
\tag{11}
\]
Indeed, write each summand as \(q(v)u\log(1/u)\), where \(u=p(v)/q(v)\in(0,1)\), and use \(u\log(1/u)\leq1/e\) and \(\sum_vq(v)\leq1\). Terms with \(p(v)>0=q(v)\) contribute positive infinity, never a negative part.

Under \(\mathbb P^+\), conditional on the event skeleton and preceding tokens, the next token has law \(q_{t_j}^+(\cdot\mid x_{j-1},i_j)\). Thus (11) bounds the total expected negative part of the finite log-ratio sum by \(L/e\). We may therefore take its expectation term by term, allowing positive infinity. From (10), including the case where \(f_q=0<f_{q^+}\), this yields
\[
\operatorname{KL}(\mathbb P^+\|\mathbb P_q)
=\mathbb E_+\sum_{j=1}^L
\operatorname{KL}\bigl(q_{t_j}^+(\cdot\mid X_{t_j-},i_j)
\|q_{t_j}(\cdot\mid X_{t_j-},i_j)\bigr).
\tag{12}
\]

For any nonnegative measurable \(F(t,x,i)\), integrating the next-event density used above over each possible preceding history gives
\[
\mathbb E_+\sum_{j=1}^L F(t_j,X_{t_j-},i_j)
=\int_0^1\lambda(t)\mathbb E_+\!\left[
\sum_{i:X_t^i=\mathtt m}F(t,X_t,i)
\right]dt.
\tag{13}
\]
One can first do this on \([0,b]\), where all rates are bounded, sum over the finitely many possible event numbers, and then let \(b\uparrow1\) by monotone convergence. The factor for token choice disappears on summing its probabilities. In the time integral \(X_t\) may replace \(X_{t-}\), since the finite set of jump times has Lebesgue measure zero on each path.

Applying (13) to the nonnegative local KL in (12) proves
\[
\operatorname{KL}(\mathbb P^+\|\mathbb P_q)
=\int_0^1\lambda(t)\mathbb E_+\!\left[
\sum_{i:X_t^i=\mathtt m}
\operatorname{KL}(q_t^+(\cdot\mid X_t,i)\|q_t(\cdot\mid X_t,i))
\right]dt.
\tag{14}
\]
This identity includes both singular support failures and infinite KL caused by very small positive candidate probabilities. A support failure confined to a set of zero true jump exposure has no effect; no pointwise support condition is imposed.

### 5. Passing to the terminal distribution

The terminal state is a measurable function of the path. For completeness, the KL contraction here follows by grouping path densities according to their terminal state. If path KL is infinite, the desired bound is immediate. Otherwise write \(f=d\mathbb P^+/d\mathbb P_q\). On each terminal fiber, Jensen's inequality for \(u\log u\) gives
\[
\int_{\{X_1=z\}}f\log f\,d\mathbb P_q
\geq\rho^+(z)\log\frac{\rho^+(z)}{\rho_q(z)}.
\]
Summing over the finite terminal state space proves
\[
\operatorname{KL}(\rho^+\|\rho_q)
\leq\operatorname{KL}(\mathbb P^+\|\mathbb P_q).
\tag{15}
\]
Combining (9), (14), and (15) gives exactly
\[
\operatorname{KL}(\rho^+\|\rho_q)
\leq\frac{\mathcal L_c(q)-\mathcal L_c(q^+)}Z.
\]
All proof obligations are closed; no specialized external theorem is needed beyond the elementary calculations supplied here.
