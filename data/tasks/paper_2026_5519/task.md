# Problem

## Setup

Fix \(\theta\in\mathbb R^d\), integers \(N\ge1\), \(d\ge2\), \(1\le k<d\), \(T_1\ge1\), \(B\ge1\), constants \(C_1,C_2>0\), and \(\sigma_1,\sigma_2>0\). Let clipped per-example gradients \(\bar g_i(\theta)\in\mathbb R^d\) satisfy \(\|\bar g_i(\theta)\|_2\le C_2\), and set \(G=N^{-1}\sum_{i=1}^N\bar g_i(\theta)\). For a support \(A\subseteq\{1,\ldots,d\}\) with \(|A|=k\), let \(\bar A=A^c\) and let \(P_{\bar A}\) project onto inactive coordinates. Put \(\nu_2^2=(\sigma_2C_2/B)^2\). Let \(\eta_A\) have independent \(N(0,\nu_2^2)\) coordinates on \(A\) and zero coordinates on \(\bar A\), and let \(\eta_{\rm full}\) have independent \(N(0,\nu_2^2)\) coordinates in all \(d\) positions. Define
\[
E(A)=\mathbb E\|P_{\bar A}G+\eta_A\|_2^2,\qquad E_{\rm full}=\mathbb E\|\eta_{\rm full}\|_2^2.
\]

During warm-up, assume independent \(z_{t,p}\sim N(0,\sigma_1^2C_1^2)\) and \(\widetilde g_{t,p}=G_p+z_{t,p}/B\) for \(t=1,\ldots,T_1\), \(p=1,\ldots,d\). Let \(\nu_1^2=(\sigma_1C_1/B)^2\), define \(a_p=T_1^{-1}\sum_{t=1}^{T_1}(\widetilde g_{t,p}^2-\nu_1^2)\), and let \(\operatorname{TopK}(v,k)\) return the indices of the \(k\) largest entries, with deterministic tie-breaking.

## Task

Prove the following integrated theorem. For every support \(A\) of size \(k\),
\[
E(A)<E_{\rm full}\iff\|P_{\bar A}G\|_2^2<(d-k)\nu_2^2.
\]
Let \(S^*=\operatorname{TopK}((G_1^2,\ldots,G_d^2),k)\) and assume uniqueness, so \(\Delta_{pq}=G_p^2-G_q^2>0\) for all \(p\in S^*\), \(q\notin S^*\). Prove that for every such pair,
\[
\Pr\{a_p<a_q\}\le\frac{4\nu_1^4+4\nu_1^2(G_p^2+G_q^2)}{T_1\Delta_{pq}^2},
\]
and consequently
\[
\Pr\{\operatorname{TopK}((a_1,\ldots,a_d),k)\ne S^*\}\le\sum_{p\in S^*}\sum_{q\notin S^*}\frac{4\nu_1^4+4\nu_1^2(G_p^2+G_q^2)}{T_1\Delta_{pq}^2}.
\]
In particular, for any \(\delta\in(0,1)\), if every summand is at most \(\delta/[k(d-k)]\), then \(\operatorname{TopK}((a_1,\ldots,a_d),k)=S^*\) with probability at least \(1-\delta\).
