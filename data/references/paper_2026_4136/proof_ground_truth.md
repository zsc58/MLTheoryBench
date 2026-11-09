# Reference Proof

## Proof Structure

Construct the fallback-plus-region mixture, compute its density ratio, and derive the total-variation and both KL bounds directly. Compute its mixture-average reporting cost. Then count the one-representative supports and compare exact-support truncation with the single-region report.

## Complete Proof

### step_001: Components and feasible weights

For every dictionary component, positivity of its retained mass gives
\[
\sum_{\gamma\in\Gamma}\pi_{w_m}(\gamma)
=\alpha_m^{-1}\sum_{\gamma\in\Gamma}\pi_0(\gamma)w_m(\gamma)=1.
\]
For each selected region,
\[
\pi_{w_r}(\gamma)=\frac{\pi_0(\gamma)1_{C_r}(\gamma)}{p_r}.
\]
Disjointness gives \(\pi_0(U_I)=\alpha_I\), and \(1\ge\alpha_I\ge1-\epsilon>0\). In particular, the selected set is nonempty. All proposed weights are nonnegative, the unselected weights vanish, and
\[
q_0+\sum_{r\in I}q_r
=\zeta+(1-\zeta)\alpha_I^{-1}\sum_{r\in I}p_r=1.
\]
Also \(q_0=\zeta\ge\epsilon_0\), so the report is well-defined and satisfies the fallback floor.

### step_002: Density ratio and total variation

On the support of \(\pi_0\), disjointness and the chosen weights give
\[
h(\gamma)=\begin{cases}
\zeta+(1-\zeta)/\alpha_I,&\gamma\in U_I,\\
\zeta,&\gamma\notin U_I.
\end{cases}
\]
Write \(h_{\rm in}=\zeta+(1-\zeta)/\alpha_I\). Since \(\alpha_I\le1\), we have \(h_{\rm in}\ge1\). The report and the reference law both vanish outside the support of \(\pi_0\). Thus the finite-sum definition of TV gives
\[
\begin{aligned}
\operatorname{TV}(\pi_0,\bar\pi_q)
&=\tfrac12\mathbb E_{\pi_0}|h-1|\\
&=\tfrac12\left[\alpha_I(h_{\rm in}-1)+(1-\alpha_I)(1-\zeta)\right]\\
&=(1-\zeta)(1-\alpha_I)
\le(1-\zeta)\epsilon.
\end{aligned}
\]

### step_003: Both KL bounds

Because \(h\ge\zeta>0\) on the support of \(\pi_0\), both KL divergences are finite. Substitution into their definitions yields
\[
D_{\rm KL}(\pi_0\|\bar\pi_q)
=-\alpha_I\log h_{\rm in}-(1-\alpha_I)\log\zeta.
\]
The first term is nonpositive, so
\[
D_{\rm KL}(\pi_0\|\bar\pi_q)
\le(1-\alpha_I)\log(1/\zeta)
\le\epsilon\log(1/\zeta).
\]
In the opposite direction,
\[
D_{\rm KL}(\bar\pi_q\|\pi_0)
=\alpha_Ih_{\rm in}\log h_{\rm in}
 +(1-\alpha_I)\zeta\log\zeta.
\]
The second term is nonpositive. Moreover,
\[
\alpha_Ih_{\rm in}=\alpha_I\zeta+1-\zeta
=1-\zeta(1-\alpha_I)\le1.
\]
Since \(\log h_{\rm in}\ge0\), it follows that
\[
D_{\rm KL}(\bar\pi_q\|\pi_0)
\le\log h_{\rm in}
\le\log\!\left(\zeta+\frac{1-\zeta}{1-\epsilon}\right),
\]
where the last inequality uses \(\alpha_I\ge1-\epsilon>0\).

### step_004: Expected reporting cost

The reporting cost is averaged over component labels with probabilities \(q_m\). Therefore, using the zero weights on unselected components,
\[
C_{\rm exp}(q)=\sum_{m=0}^Rq_mc_m
=\zeta c_0+(1-\zeta)\alpha_I^{-1}\sum_{r\in I}p_rc_r.
\]
This is not an assertion about the sum of costs of every displayed region.

### step_005: Product count and atom-truncation lower bound

Each tuple \((j_k)_{k\in S^*}\) with \(j_k\in G_k\) defines the binary vector whose active coordinates are exactly those chosen coordinates. Pairwise disjointness makes this correspondence a bijection between \(\prod_{k\in S^*}G_k\) and \(C^*\). Consequently,
\[
|C^*|=M^*=\prod_{k\in S^*}m_k.
\]
If \(S^*=\varnothing\), the sole admissible vector is the zero vector, agreeing with the empty product \(M^*=1\).

Uniformity gives mass \(1/M^*\) to each vector in \(C^*\) and zero mass elsewhere. For a nonempty \(A\subseteq C^*\), put \(a=|A|\). Then \(\pi_0(A)=a/M^*>0\), and \(\pi_A\) assigns mass \(1/a\) to each element of \(A\). Since \(1\le a\le M^*\),
\[
\begin{aligned}
\operatorname{TV}(\pi_0,\pi_A)
&=\tfrac12\left[a\left(\frac1a-\frac1{M^*}\right)
 +(M^*-a)\frac1{M^*}\right]\\
&=1-\frac a{M^*}.
\end{aligned}
\]
If \(a\le M\), this is at least \(1-M/M^*\). If the truncation also has TV at most \(\epsilon\), then
\[
a\ge(1-\epsilon)M^*,\qquad M\ge(1-\epsilon)M^*.
\]
For integer budgets this is equivalently \(M\ge\lceil(1-\epsilon)M^*\rceil\). If \(M=0\), there is no admissible nonempty truncation. If \(M>M^*\), the displayed lower bound remains valid, although it may be negative.

### step_006: Single-region comparison and endpoints

The hard kernel \(1_{C^*}\) has retained mass \(\pi_0(C^*)=1\), so its restricted law is exactly \(\pi_0\). Hence TV and both KL divergences are zero. Mixing this law with any fallback weight also leaves it unchanged. The region is specified by the active group pattern and the one-coordinate requirement, rather than by enumerating its atoms; no quantitative inequality between arbitrary declared costs is needed.

All formulas remain valid when \(\alpha_I=1\), including \(\epsilon=0\): the report then equals \(\pi_0\). Zero reporting costs, singleton groups, and full truncation \(A=C^*\) cause no additional cases or undefined expressions.
