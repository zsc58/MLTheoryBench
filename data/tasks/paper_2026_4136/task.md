# Problem

## Setup

Let \(\Gamma\) be a finite set and let \(\pi_0\) be a probability distribution on it. For a kernel \(w:\Gamma\to[0,1]\) with retained mass \(\alpha=\mathbb E_{\pi_0}[w]>0\), define
\[
\pi_w(\gamma)=\frac{\pi_0(\gamma)w(\gamma)}{\alpha}.
\]
Given kernels indexed by \(m=0,1,\ldots,R\), each with retained mass \(\alpha_m>0\), with \(w_0\equiv1\), and weights \(q_m\ge0\) satisfying \(\sum_{m=0}^R q_m=1\), define
\[
\bar\pi_q(\gamma)=\sum_{m=0}^R q_m\pi_{w_m}(\gamma),\qquad
h_q(\gamma)=\frac{\bar\pi_q(\gamma)}{\pi_0(\gamma)}=\sum_{m=0}^R q_m\frac{w_m(\gamma)}{\alpha_m}
\]
on the support of \(\pi_0\).

For probability laws \(\mu,\nu\) on \(\Gamma\), use
\[
\operatorname{TV}(\mu,\nu)=\frac12\sum_{\gamma\in\Gamma}|\mu(\gamma)-\nu(\gamma)|,
\qquad
D_{\rm KL}(\mu\|\nu)=\sum_{\gamma:\mu(\gamma)>0}\mu(\gamma)\log\frac{\mu(\gamma)}{\nu(\gamma)}.
\]
Here logarithms are natural, and the KL divergence is infinite if \(\nu(\gamma)=0<\mu(\gamma)\) for some \(\gamma\).

Let \(I\subseteq\{1,\ldots,R\}\), and let \(C_r\subseteq\Gamma\), \(r\in I\), be pairwise disjoint regions with \(p_r=\pi_0(C_r)>0\) and hard kernels \(w_r=1_{C_r}\). Put \(U_I=\bigcup_{r\in I}C_r\), \(\alpha_I=\sum_{r\in I}p_r\), and assume \(\alpha_I\ge1-\epsilon\) for some \(0\le\epsilon<1\). Let \(0<\epsilon_0\le\zeta<1\). For finite nonnegative reporting costs \(c_m\), define the expected reporting cost of a mixture by
\[
C_{\rm exp}(q)=\sum_{m=0}^R q_mc_m.
\]

For the converse, specialize to \(\Gamma=\{0,1\}^p\), where \(p\) is a positive integer, and write \(\operatorname{supp}(\gamma)=\{j:\gamma_j=1\}\). Let \(G_1,\ldots,G_K\) be nonempty pairwise disjoint subsets of \(\{1,\ldots,p\}\), with sizes \(m_k=|G_k|\). Let \(S^*\subseteq\{1,\ldots,K\}\), and define
\[
C^*=\left\{\gamma\in\{0,1\}^p:
\operatorname{supp}(\gamma)\subseteq\bigcup_{k\in S^*}G_k,
\quad\sum_{j\in G_k}\gamma_j=1\text{ for every }k\in S^*
\right\}.
\]
Assume \(\pi_0\) is uniform on \(C^*\) and zero outside it, and write \(M^*=|C^*|=\prod_{k\in S^*}m_k\), with the empty product equal to one. Let \(M\) be a nonnegative integer. For any nonempty listed subset \(A\subseteq C^*\), define its exact-support truncation by \(\pi_A=\pi_0(\cdot\mid A)\).

## Task

Prove the following integrated theorem. Define \(q_0=\zeta\) and \(q_r=(1-\zeta)p_r/\alpha_I\) for \(r\in I\), and set \(q_m=0\) for \(m\notin\{0\}\cup I\). Then the resulting report satisfies
\[
\operatorname{TV}(\pi_0,\bar\pi_q)=(1-\zeta)(1-\alpha_I)\le(1-\zeta)\epsilon,
\]
\[
D_{\rm KL}(\pi_0\|\bar\pi_q)\le\epsilon\log(1/\zeta),
\qquad
D_{\rm KL}(\bar\pi_q\|\pi_0)\le\log\!\left(\zeta+\frac{1-\zeta}{1-\epsilon}\right),
\]
and its expected cost is
\[
C_{\rm exp}(q)=\zeta c_0+(1-\zeta)\alpha_I^{-1}\sum_{r\in I}p_rc_r.
\]
Moreover, under the converse assumptions, for every nonempty \(A\subseteq C^*\) with \(|A|\le M\), the exact-support truncation satisfies
\[
\operatorname{TV}(\pi_0,\pi_A)=1-|A|/M^*\ge1-M/M^*.
\]
Hence such a truncation with TV distortion at most \(\epsilon\) requires \(M\ge(1-\epsilon)M^*\). In contrast, the single hard region \(C^*\) yields zero TV and both KL distortions.
