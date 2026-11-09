# Reference Proof

## Proof Structure

Establish the single-level moments by centered-sum calculations, derive the covariance of nested sample variances, and combine the expected empirical variances using iid outer replicates within each level. Independence between levels is not needed.

## Complete Proof

Fix x and write Z_t=D(x;\theta_t)-\mu. These variables are iid and centered, with E[Z_t^2]=\mu_2 and E[Z_t^4]=\mu_4<\infty. For n\ge2, let
\[
A_n=\sum_{i=1}^n Z_i,\qquad Q_n=\sum_{i=1}^n Z_i^2,\qquad
V_n=\frac{Q_n-A_n^2/n}{n-1}.
\]
All products used below are integrable by the finite fourth moment. Linearity and independence give E[Y_n]=\mu, Var(Y_n)=\mu_2/n, E[Q_n]=n\mu_2, and E[A_n^2]=n\mu_2. Consequently E[V_n]=\mu_2.

Expanding the sums and using centering and independence gives
\[
E[Q_n^2]=n\mu_4+n(n-1)\mu_2^2,
\qquad
E[Q_nA_n^2]=n\mu_4+n(n-1)\mu_2^2,
\]
and
\[
E[A_n^4]=n\mu_4+3n(n-1)\mu_2^2.
\]
For the first identity, the contributions have either equal or distinct indices. For the second, all terms involving a product Z_iZ_j with i\ne j vanish: even when the squared factor shares one of those indices, the other centered factor has expectation zero. For the third, the only nonzero index patterns are four equal indices or two pairs; the latter contribute 6\binom n2\mu_2^2.

It follows that
\[
E[V_n^2]
=\frac{E[Q_n^2]-2E[Q_nA_n^2]/n+E[A_n^4]/n^2}{(n-1)^2}
=\frac{\mu_4}{n}+\frac{n^2-2n+3}{n(n-1)}\mu_2^2.
\]
Subtracting (E[V_n])^2 yields
\[
\operatorname{Var}(V_n)
=\frac1n\left(\mu_4-\frac{n-3}{n-1}\mu_2^2\right)
=\frac{\mu_4-3\mu_2^2}{n}+\frac{2\mu_2^2}{n-1}.
\]

Now consider one coupled pair with coarse sample size n, fine sample size m, and r=m-n\ge2. Reuse the first n observations, and let B_r be the centered sum of the independent fresh block and V'_r its unbiased sample variance. Splitting each block's residuals around its own mean gives
\[
V_m=\frac{n-1}{m-1}V_n+\frac{r-1}{m-1}V'_r+
\frac{nr}{m(m-1)}\left(\frac{A_n}{n}-\frac{B_r}{r}\right)^2.
\]
Indeed, the cross terms within each block sum to zero, and the two squared block-mean displacements from the pooled mean sum to nr/m times the squared difference of block means.

The new-block variance V'_r is independent of V_n. Also B_r is centered and independent of the entire coarse block. Expanding the squared difference therefore gives
\[
\operatorname{Cov}\left(V_n,\left(\frac{A_n}{n}-\frac{B_r}{r}\right)^2\right)
=\frac1{n^2}\operatorname{Cov}(V_n,A_n^2).
\]
The centered-sum moments already computed imply
\[
\begin{aligned}
E[V_nA_n^2]
&=\frac{E[Q_nA_n^2]-E[A_n^4]/n}{n-1}\\
&=\mu_4+(n-3)\mu_2^2.
\end{aligned}
\]
Since E[V_n]E[A_n^2]=n\mu_2^2,
\[
\operatorname{Cov}(V_n,A_n^2)=\mu_4-3\mu_2^2.
\]
Thus
\[
\operatorname{Cov}(V_m,V_n)
=\frac{n-1}{m-1}\operatorname{Var}(V_n)
+\frac{r}{nm(m-1)}(\mu_4-3\mu_2^2).
\]
Substituting the single-level variance formula and using r=m-n simplifies this to
\[
\operatorname{Cov}(V_m,V_n)
=\frac{\mu_4-3\mu_2^2}{m}+\frac{2\mu_2^2}{m-1}
=\operatorname{Var}(V_m).
\]
Consequently the coupled difference has variance
\[
\begin{aligned}
\operatorname{Var}(V_m-V_n)
&=\operatorname{Var}(V_m)+\operatorname{Var}(V_n)-2\operatorname{Cov}(V_m,V_n)\\
&=\left(\frac1n-\frac1m\right)(\mu_4-3\mu_2^2)
+2\mu_2^2\left(\frac1{n-1}-\frac1{m-1}\right).
\end{aligned}
\]

At level zero, each outer replicate has the distribution of V_{T_0}; at level \ell\ge1, each has the distribution of the coupled difference \Delta V_\ell. Denote these component replicates by W_{\ell,j}, for j=1,\ldots,M_\ell. This notation does not identify samples belonging to different levels. The variables W_{\ell,j} are iid in j at each fixed level, while different levels may be dependent.

The single-level unbiasedness gives E[W_{0,j}]=\mu_2 and E[W_{\ell,j}]=0 for \ell\ge1. Hence, by linearity,
\[
E[\mathcal V]=\mu_2.
\]

For any M iid real variables W_1,\ldots,W_M with mean a and finite variance \tau^2, write \overline W=M^{-1}\sum_jW_j. The identity
\[
\sum_{j=1}^M(W_j-\overline W)^2
=\sum_{j=1}^M(W_j-a)^2-M(\overline W-a)^2
\]
and Var(\overline W)=\tau^2/M show that the empirical variance with denominator M-1 has expectation \tau^2. This applies to every component here because each has finite second moment and M_\ell\ge2.

Applying this identity level by level and then using linearity of expectation gives
\[
E[S_V^2]=\frac1{M_0}\operatorname{Var}(V_{T_0})+
\sum_{\ell=1}^L\frac1{M_\ell}\operatorname{Var}(\Delta V_\ell).
\]
No independence between levels is used. Substituting the single-level and correction variances yields
\[
\begin{aligned}
E[S_V^2]={}&\frac1{M_0T_0}\left(\mu_4-\frac{T_0-3}{T_0-1}\mu_2^2\right)\\
&+\sum_{\ell=1}^L\frac1{M_\ell}\left(\frac1{T_{\ell-1}}-\frac1{T_\ell}\right)(\mu_4-3\mu_2^2)\\
&+\sum_{\ell=1}^L\frac{2\mu_2^2}{M_\ell}\left(\frac1{T_{\ell-1}-1}-\frac1{T_\ell-1}\right).
\end{aligned}
\]
If \mu_4=3\mu_2^2, the middle sum vanishes and the first term becomes 2\mu_2^2/[M_0(T_0-1)]. Therefore
\[
E[S_V^2]=2\mu_2^2\left[\frac1{M_0(T_0-1)}+
\sum_{\ell=1}^L\frac1{M_\ell}\left(\frac1{T_{\ell-1}-1}-\frac1{T_\ell-1}\right)\right].
\]
All calculations remain valid for T_0=2, new blocks of size two, M_\ell=2, and an empty correction sum. If \mu_2=0, the centered output is zero almost surely and all variance quantities vanish, consistently with the formulas. No division by \mu_2 is used.
