# Reference Proof

## Proof Structure

First expand the expected squared errors of the masked and full Gaussian updates to obtain the signal-loss plus active-noise decomposition, then compare the two expressions. For warm-up ranking, compute denoised score means and variances, apply Chebyshev to each oracle boundary pair, and use a union bound.

## Complete Proof

Fix \(\theta\) and write \(G=N^{-1}\sum_i\bar g_i(\theta)\). For a support \(A\), let \(\eta_A\) have independent \(N(0,\nu_2^2)\) coordinates on \(A\) and zero coordinates on \(\bar A\). Since \(P_{\bar A}G\) is deterministic and \(\mathbb E\eta_A=0\),
\[
E(A)=\mathbb E\|P_{\bar A}G+\eta_A\|_2^2=\|P_{\bar A}G\|_2^2+\mathbb E\|\eta_A\|_2^2=\|P_{\bar A}G\|_2^2+k\nu_2^2.
\]
For the full update, let \(\eta_{\rm full}\) have independent \(N(0,\nu_2^2)\) coordinates in all \(d\) positions. Then \(E_{\rm full}=\mathbb E\|\eta_{\rm full}\|_2^2=d\nu_2^2\). Consequently,
\[
E(A)-E_{\rm full}=\|P_{\bar A}G\|_2^2-(d-k)\nu_2^2,
\]
proving the first equivalence.

For warm-up, put \(\xi_{t,p}=z_{t,p}/B\). These variables are independent centered Gaussians with variance \(\nu_1^2=(\sigma_1C_1/B)^2\), and \(\widetilde g_{t,p}=G_p+\xi_{t,p}\). Using \(\mathbb E\xi=0\), \(\mathbb E\xi^2=\nu_1^2\), and \(\mathbb E\xi^4=3\nu_1^4\),
\[
\mathbb E[(G_p+\xi)^2-\nu_1^2]=G_p^2,
\]
so \(\mathbb E a_p=G_p^2\). Also,
\[
(G_p+\xi)^2-\nu_1^2-G_p^2=2G_p\xi+(\xi^2-\nu_1^2),
\]
whose variance is \(4G_p^2\nu_1^2+2\nu_1^4\), because the covariance term is zero. Averaging \(T_1\) independent observations gives
\[
\operatorname{Var}(a_p)=\frac{2\nu_1^4+4G_p^2\nu_1^2}{T_1}.
\]
For distinct coordinates \(p,q\), independence gives, with \(\Delta_{pq}=G_p^2-G_q^2>0\),
\[
\mathbb E(a_p-a_q)=\Delta_{pq},\qquad
\operatorname{Var}(a_p-a_q)=\frac{4\nu_1^4+4\nu_1^2(G_p^2+G_q^2)}{T_1}.
\]
The event \(a_p<a_q\) implies a deviation of magnitude at least \(\Delta_{pq}\), so Chebyshev yields
\[
\Pr(a_p<a_q)\le\frac{4\nu_1^4+4\nu_1^2(G_p^2+G_q^2)}{T_1\Delta_{pq}^2}.
\]
If \(S^*=\operatorname{TopK}(G^2,k)\) is unique, a failure of \(\operatorname{TopK}(a,k)=S^*\) entails a boundary pair \(p\in S^*\), \(q\notin S^*\) with \(a_p\le a_q\). Equality has probability zero, so a union bound over all boundary pairs gives the stated sum. If every summand is at most \(\delta/[k(d-k)]\), the failure probability is at most \(\delta\), proving the final recovery claim.
