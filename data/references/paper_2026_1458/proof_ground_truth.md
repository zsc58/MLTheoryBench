# Reference Proof

## Proof Structure

The theorem-critical obligations are: (1) justify the logarithmic gap decomposition and its integrability; (2) establish conditional unbiasedness and the nuisance Jensen inequality; (3) define and normalize the tilted contrastive law and derive its KL representation by symmetry; and (4) prove both conditional strong-law limits and justify passage to expectations. All four obligations are derived below. In particular, the specialized contrastive identity is not assumed as an external result.

## Complete Proof

Fix the policy and horizon, and abbreviate the history by \(H\). Write
\[
q_T(h)=p(h\mid\theta_T^{(0)},\pi),\qquad q(h)=p(h\mid\pi),
\]
where \(q_T\) retains its dependence on the generating target. Put
\[
U_M=\frac{\widehat p_M(H\mid\theta_T^{(0)},\pi)}{q_T(H)},\qquad
V_L=\frac{\widehat p_L(H\mid\pi)}{q(H)},\qquad
A_M=-\log U_M,\quad B_L=\log V_L.
\]
All ratios are positive and finite almost surely.

### Conditional nuisance sampling

Conditional on \((\theta_T^{(0)},H)\), the nuisance samples are iid with law \(p(\theta_N\mid\theta_T^{(0)})\), independently of the history. Consequently,
\[
\mathbb E[U_M\mid\theta_T^{(0)},H]
=\frac{\int p(H\mid\theta_T^{(0)},n,\pi)p(n\mid\theta_T^{(0)})\,dn}{q_T(H)}=1.
\]
In particular, \(\mathbb E U_M=1\). Writing \(x^- =\max\{-x,0\}\), we have
\[
A_M^-=(\log U_M)_+\le U_M,
\qquad \mathbb E A_M^-\le1.
\]

### Contrastive symmetry and normalization

Let \(P_L\) denote the product of \(L+1\) copies of the prior, on a tuple \(\vartheta=(\theta^{(0)},\ldots,\theta^{(L)})\). For a fixed history with \(q(h)>0\), define
\[
r_\ell(h,\vartheta)=\frac{p(h\mid\theta^{(\ell)},\pi)}{q(h)},\qquad
v_h(\vartheta)=\frac1{L+1}\sum_{\ell=0}^L r_\ell(h,\vartheta).
\]
The marginal definition gives
\[
\int r_\ell(h,\vartheta)\,P_L(d\vartheta)=1,
\qquad \int v_h\,dP_L=1.
\]
Thus \(Q_h(d\vartheta)=v_h(\vartheta)P_L(d\vartheta)\) is a probability law.

After the nuisance samples are integrated out, the actual joint law of \((H,\vartheta)\) is
\[
q(h)\,\mu(dh)\,r_0(h,\vartheta)P_L(d\vartheta),
\]
where \(\mu\) is the common history reference measure. For any nonnegative measurable function \(f\), permutation invariance of \(P_L\) and of \(v_h\) gives
\[
\int r_0 f(v_h)\,dP_L
=\frac1{L+1}\sum_{\ell=0}^L\int r_\ell f(v_h)\,dP_L
=\int v_h f(v_h)\,dP_L.
\]
This argument does not regard the generating parameter as an independent prior draw conditional on the history.

Taking \(f(v)=(-\log v)_+\) and using \(v(-\log v)_+\le1/e\) yields
\[
\mathbb E B_L^-
=\int q(h)\,\mu(dh)\int v_h(-\log v_h)_+\,dP_L
\le1/e.
\]

### Integrability and the finite-sample inequality

Pointwise,
\[
S:=A_M+B_L
=\log\frac{q_T(H)}{q(H)}
-\log\frac{\widehat p_M(H\mid\theta_T^{(0)},\pi)}{\widehat p_L(H\mid\pi)}.
\]
The public finite-expectation assumptions make both terms on the right integrable, so \(S\) is integrable. Since
\[
A_M^+\le S^++B_L^-,\qquad B_L^+\le S^++A_M^-,
\]
the negative-part bounds already proved show that \(A_M\) and \(B_L\) are individually integrable. The gap decomposition is therefore justified:
\[
I_K^{\mathrm{tgt}}(\pi)-\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)
=\mathbb E A_M+\mathbb E B_L.
\]

Conditional Jensen, applied to the positive mean-one variable \(U_M\), gives
\[
\mathbb E[A_M\mid\theta_T^{(0)},H]
\ge-\log\mathbb E[U_M\mid\theta_T^{(0)},H]=0.
\]
Thus \(\mathbb E A_M\ge0\). This normalized argument does not require separate integrability of \(\log q_T(H)\).

Apply the symmetry identity separately to the positive and negative parts of \(\log v_h\). The established integrability gives
\[
\mathbb E B_L
=\int q(h)\,\mu(dh)\int v_h\log v_h\,dP_L
=\int q(h)\,\mathrm{KL}(Q_h\|P_L)\,\mu(dh)\ge0.
\]
Here the KL divergence is the displayed integral; its nonnegativity follows directly from \(x\log x\ge x-1\) and \(\int v_h\,dP_L=1\). Therefore
\[
\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)\le I_K^{\mathrm{tgt}}(\pi).
\]

### Convergence

Couple all sample counts by using infinite fresh contrastive and nuisance sequences with the prescribed conditional laws. Conditional on \((\theta_T^{(0)},H)\), the nuisance likelihood ratios are iid, have mean one, and lie in \([\kappa_{1,N},\kappa_{2,N}]\). The conditional strong law gives \(U_M\to1\) almost surely. Integrating the conditional probability-one assertion gives the same conclusion under the full experiment.

Conditional on \((\theta^{(0)},H)\), the ratios \(r_\ell(H,\vartheta)\), \(\ell\ge1\), are iid with mean one and lie in \([\kappa_1,\kappa_2]\). The generating ratio is not one of these conditionally iid samples. Instead, write
\[
V_L=\frac{r_0}{L+1}+\frac{L}{L+1}\left(\frac1L\sum_{\ell=1}^L r_\ell\right).
\]
The first term tends to zero and the parenthesized average tends to one by the conditional strong law. Hence \(V_L\to1\) almost surely.

The uniform bounds imply
\[
|A_M|\le\max\{|\log\kappa_{1,N}|,|\log\kappa_{2,N}|\},\qquad
|B_L|\le\max\{|\log\kappa_1|,|\log\kappa_2|\}.
\]
Both logarithms tend to zero almost surely. Bounded convergence therefore gives \(\mathbb E A_M\to0\) as \(M\to\infty\) and \(\mathbb E B_L\to0\) as \(L\to\infty\). The first expectation is independent of \(L\), and the second is independent of \(M\). Their sum tends to zero whenever both counts diverge, without any restriction on their relative growth. The gap decomposition proves
\[
\widehat{\mathcal L}_K^{\mathrm{tgt}}(\pi,L,M)\longrightarrow I_K^{\mathrm{tgt}}(\pi).
\]
