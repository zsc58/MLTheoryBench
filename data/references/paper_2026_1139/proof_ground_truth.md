# Reference Proof

## Proof Structure

1. Show that the adaptive residuals are exchangeable under the exchangeability of the data and the fixed measurable score, feature map, and regressor.
2. Apply an exchangeable-rank argument to the calibration residuals augmented by an infinity value.
3. Translate the residual event into membership in the prediction set.

## Complete Proof

Let
\[
R_i=s(X_i,Y_i)-\psi(\omega(X_i)),\qquad i=1,\ldots,n+1.
\]
The map \(h(x,y)=s(x,y)-\psi(\omega(x))\) is measurable and real-valued. For any permutation \(\sigma\) of the indices, applying \(h\) coordinatewise to the exchangeability identity for the data gives
\[
(R_1,\ldots,R_{n+1})\stackrel{d}{=}(R_{\sigma(1)},\ldots,R_{\sigma(n+1)}).
\]
Thus the residual sequence is exchangeable. This uses the same fixed measurable map at every index.

Put \(m=n+1\) and \(k=\lceil m(1-\alpha)\rceil\). Since \(\alpha\in(0,1)\), we have \(1\le k\le m\). Let \(\widehat q\) be the \(k\)-th order statistic of \(R_1,\ldots,R_n,+\infty\). This is a measurable extended-real random variable: a finite-list order statistic can be expressed using finitely many minima and maxima. In particular, \(\{R_m\le\widehat q\}\) is measurable.

On an auxiliary product probability space, introduce independent identically distributed \(U_1,\ldots,U_m\), each uniform on \((0,1)\), independent of all data. Adding this independent randomness does not change the probability of events involving only the data. The sequence \((R_i,U_i)_{i=1}^m\) is exchangeable because the residual sequence is exchangeable and the independent auxiliary vector has a permutation-invariant law. Order these pairs lexicographically and let \(A_i\) be the rank of index \(i\), with the smallest pair having rank one. The pairs are almost surely distinct, since the auxiliary variables are almost surely pairwise distinct. Their rank vector is exchangeable.

For every \(r\in\{1,\ldots,m\}\), exactly one index has rank \(r\), almost surely. Consequently,
\[
\sum_{i=1}^m\mathbb P\{A_i=r\}=1.
\]
Exchangeability makes all summands equal, so \(\mathbb P\{A_m=r\}=1/m\), and hence
\[
\mathbb P\{A_m\le k\}=\frac{k}{m}.
\]

If \(k=m\), then \(\widehat q=+\infty\), and the finite residual \(R_m\) satisfies \(R_m\le\widehat q\) surely. If \(k\le n\) and \(R_m>\widehat q\), at least \(k\) calibration residuals satisfy \(R_i\le\widehat q<R_m\). Their pairs precede the test pair lexicographically, so \(A_m>k\). Thus in every case
\[
\{A_m\le k\}\subseteq\{R_m\le\widehat q\}.
\]
Only this inclusion is needed; ties can make the residual event strictly larger. Therefore
\[
\mathbb P\{R_{n+1}\le\widehat q\}\ge\frac{k}{m}\ge 1-\alpha.
\]

By definition, using that \(s\) and \(\psi\) are real-valued and interpreting the threshold in the extended reals when \(\widehat q=+\infty\),
\[
Y_{n+1}\in\Gamma(X_{n+1})
\Longleftrightarrow
s(X_{n+1},Y_{n+1})\le\psi(\omega(X_{n+1}))+\widehat q
\Longleftrightarrow
R_{n+1}\le\widehat q.
\]
Hence \(\mathbb P\{Y_{n+1}\in\Gamma(X_{n+1})\}\ge1-\alpha\).
