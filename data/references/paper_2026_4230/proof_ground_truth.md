# Reference Proof

## Proof Structure

1. Solve the reverse-KL projection onto Gaussian distributions with covariance diagonal in the fixed basis, obtaining the coordinate variances of the MFVI covariance.
2. Compare the exact covariance and MFVI covariance in each coordinate using the weighted arithmetic-harmonic mean inequality, then sum to obtain a trace inequality.
3. Establish the conserved identity \(\operatorname{Tr}(\Sigma^{-1}S^*)=P\).
4. Express empirical predictive variances as covariance traces, substitute the posterior-precision identity for the empirical covariance, and combine the trace relations to obtain the ordering.

## Complete Proof

Since \(\alpha>0\), the matrix \(\Sigma^{-1}=X^\top X/\sigma^2+\alpha I_P\) is positive definite, regardless of the rank of \(X\). Let \(e_1,\ldots,e_P\) be the fixed orthonormal coordinate basis in which the MFVI covariance is diagonal. Write
\[
\Sigma=\sum_{q=1}^P\delta_q v_qv_q^\top,
\]
where \(\delta_q>0\) and \(v_1,\ldots,v_P\) is an orthonormal eigenbasis. Let
\[
S^*=\sum_{p=1}^P d_p^*e_pe_p^\top
\]
be the covariance of the reverse-KL optimal mean-field Gaussian.

For \(S=\sum_p d_pe_pe_p^\top\), the Gaussian reverse KL is
\[
D_{\mathrm{KL}}\bigl(N(m,S)\|N(\mu,\Sigma)\bigr)
=\frac12\left[(m-\mu)^\top\Sigma^{-1}(m-\mu)
+\operatorname{Tr}(\Sigma^{-1}S)-\log\det S
+\log\det\Sigma-P\right].
\]
Positive definiteness of \(\Sigma^{-1}\) makes the mean-dependent term uniquely minimal at \(m=\mu\). Twice the covariance-dependent part, up to an additive constant, is
\[
F(d)=\sum_{p=1}^P\left[d_p\,e_p^\top\Sigma^{-1}e_p-\log d_p\right],\qquad d_p>0.
\]
Multiplication by this positive factor does not change the minimizer. For each \(p\), the coefficient \(e_p^\top\Sigma^{-1}e_p\) is positive, and the corresponding scalar summand has second derivative \(1/d_p^2>0\) and tends to infinity as \(d_p\downarrow0\) or \(d_p\to\infty\). Thus the unique global minimum exists and is obtained by setting each first derivative to zero:
\[
\frac{1}{d_p^*}=e_p^\top\Sigma^{-1}e_p.
\]
Using the spectral decomposition of \(\Sigma\), define \(w_{pq}=(e_p^\top v_q)^2\). Then \(w_{pq}\ge0\), and completeness of the orthonormal eigenbasis gives
\[
\sum_q w_{pq}=e_p^\top\left(\sum_q v_qv_q^\top\right)e_p=1.
\]
Consequently,
\[
\frac1{d_p^*}=\sum_{q=1}^P\frac{w_{pq}}{\delta_q},
\qquad
 e_p^\top\Sigma e_p=\sum_{q=1}^Pw_{pq}\delta_q.
\]
The weighted arithmetic-harmonic mean inequality states that, for positive values \(\delta_q\) and nonnegative weights summing to one,
\[
\sum_q w_{pq}\delta_q\ge\left(\sum_q\frac{w_{pq}}{\delta_q}\right)^{-1}.
\]
Its hypotheses hold here, so
\[
 e_p^\top\Sigma e_p\ge d_p^*.
\]
Summing over \(p\) yields
\[
\operatorname{Tr}(\Sigma)\ge\operatorname{Tr}(S^*).
\]
Moreover,
\[
\operatorname{Tr}(\Sigma^{-1}S^*)
 =\sum_{p=1}^Pd_p^*e_p^\top\Sigma^{-1}e_p
 =\sum_{p=1}^P1=P.
\]

Let \(\widehat\Gamma=N^{-1}X^\top X\). From
\[
\Sigma^{-1}=X^\top X/\sigma^2+\alpha I
\]
we have
\[
\widehat\Gamma=\frac{\sigma^2}{N}(\Sigma^{-1}-\alpha I).
\]
For any parameter covariance \(C\), the empirical average total predictive variance (including the common observation-noise term) is
\[
\frac1N\sum_{n=1}^N\bigl(\sigma^2+x_n^\top Cx_n\bigr)
=\sigma^2+\operatorname{Tr}(\widehat\Gamma C).
\]
Therefore the exact-minus-MFVI difference in these averages is
\[
\operatorname{Tr}(\widehat\Gamma\Sigma)-\operatorname{Tr}(\widehat\Gamma S^*)
=\frac{\sigma^2}{N}\left(\operatorname{Tr}(\Sigma^{-1}\Sigma)-\alpha\operatorname{Tr}(\Sigma)
-\operatorname{Tr}(\Sigma^{-1}S^*)+\alpha\operatorname{Tr}(S^*)\right).
\]
Using \(\operatorname{Tr}(\Sigma^{-1}\Sigma)=P\) and the conserved identity above, this equals
\[
\frac{\sigma^2\alpha}{N}\bigl(\operatorname{Tr}(S^*)-\operatorname{Tr}(\Sigma)\bigr)\le0.
\]
Hence the empirical average predictive variance under MFVI is at least that under the exact posterior.
