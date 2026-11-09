# Problem

## Setup

Let n, N, and B be fixed positive integers, and let \(\mathcal X\) be a measurable space. Let \((A_i,B_i)_{i=1}^n\) be iid calibration pairs from a distribution P on \(\mathcal X\times\{0,1\}\). Let \((G_j,C_j)_{j=1}^N\) be iid generated pairs from Q, independent of the calibration sample; the covariates G_j are observed while the labels C_j are unobserved. Assume covariate shift: \(Q\ll P\) and
\[
\frac{dQ}{dP}(x,y)=w(x),
\]
where \(w:\mathcal X\to[0,\infty)\) is a known finite-valued measurable version of the density ratio.

Let \(I_0=\{i:B_i=0\}\) and \(n_0=|I_0|\). For every \(m\in\{0,\ldots,n\}\) and \(k\in\{1,\ldots,N\}\), fix a measurable conformity score
\[
s_{m,k}:\mathcal X^{m+k}\to\mathbb R
\]
independently of all calibration and generated data. For each k, form
\[
z^{(k)}=(A_i:i\in I_0;G_1,\ldots,G_k)\in\mathcal X^{n_0+k},
\]
listing the retained calibration indices in increasing order. Write \(S_M\) for the permutations of \(\{1,\ldots,M\}\), and, for \(z\in\mathcal X^M\), write \(z_\sigma=(z_{\sigma(1)},\ldots,z_{\sigma(M)})\).

For \(\sigma\in S_{n_0+k}\), define
\[
W(\sigma;z^{(k)})=\prod_{r=1}^k w\!\left(z^{(k)}_{\sigma(n_0+r)}\right).
\]
For each k, take \(\sigma_k^{(0)}\) to be the identity and draw \(\sigma_k^{(1)},\ldots,\sigma_k^{(B)}\) uniformly using independent auxiliary randomness. More precisely, conditional on all calibration and generated pairs, the permutations \(\sigma_k^{(b)}\), for \(1\le k\le N\) and \(1\le b\le B\), are independent and each is uniform on \(S_{n_0+k}\). Define
\[
r_k=
\frac{\sum_{b=0}^{B}W(\sigma_k^{(b)};z^{(k)})\,
\mathbf1\!\left\{s_{n_0,k}\!\left(z^{(k)}_{\sigma_k^{(b)}}\right)\ge s_{n_0,k}(z^{(k)})\right\}}
{\sum_{b=0}^{B}W(\sigma_k^{(b)};z^{(k)})}.
\]
The ratio is interpreted almost surely. Set
\[
p_k=\max_{j=k,\ldots,N}r_j,
\]
so \(p_1\ge\cdots\ge p_N\). Let \(H_k\) denote \(C_1=\cdots=C_k=0\). For a fixed level \(\alpha\in[0,1]\), define
\[
\hat K=\min\{k\in\{1,\ldots,N\}:p_k\le\alpha\},
\]
and set \(\hat K=0\) if the set is empty.

## Task

Prove the integrated finite-sample guarantee. For every \(k\in\{1,\ldots,N\}\) and every \(t\in[0,1]\),
\[
\Pr(r_k\le t,H_k)\le t\Pr(H_k).
\]
Equivalently, whenever \(\Pr(H_k)>0\), \(\Pr(r_k\le t\mid H_k)\le t\). Consequently, for \(\psi=\mathbf1\{p_N\le\alpha\}\),
\[
\Pr(\psi=1,H_N)\le\alpha\Pr(H_N),
\]
and the nested rule satisfies
\[
\Pr\bigl(\hat K>0\ \text{and}\ C_1=\cdots=C_{\hat K}=0\bigr)\le\alpha.
\]
