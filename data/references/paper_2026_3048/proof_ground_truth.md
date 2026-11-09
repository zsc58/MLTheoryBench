# Reference Proof

## Proof Structure

1. Prove a compact-uniform local tail-ratio lemma for the normal scale-mixture marginal induced by the heavy-tailed mixing density.
2. Use the Gaussian exponential-family cumulant identity for the sample mean to prove posterior convergence after centering at the diverging residual mean.
3. Evaluate the limiting posterior predictive density and prove the fixed-variance limiting score is strictly increasing in the centered-residual deviation.
4. For the plug-in construction, derive the exact augmented-variance identity, apply the compact-uniform tail-ratio lemma, and prove the corresponding limiting score is strictly increasing.

## Complete Proof

Write \(b_m=\bar r_n^{(m)}\). For \(q>0\), define the normal scale-mixture density
\[
f_q(z)=\int_0^\infty \phi(z;0,q+\gamma w)g(w)\,dw,
\]
where \(\phi(\cdot;\mu,V)\) is the \(N(\mu,V)\) density.

We first establish the needed local-ratio property. Let \(K\subset(0,\infty)\) be compact and let \(B\subset\mathbb R\) be bounded. Since \(g(w)\sim Cw^{-\delta}\) with \(\delta>1\), splitting the defining integral for \(f_q\) at a sufficiently large fixed \(T\) shows that the contribution from \(0<w<T\) is exponentially small in \(|z|\), uniformly over \(q\in K\). For the remaining contribution, put \(y=|z|\) and use \(w=y^2u/\gamma\). Then, uniformly over \(q\in K\), its ratio to \(y^{1-2\delta}\) is an integral whose integrand converges pointwise to
\[
C\gamma^{\delta-1}(2\pi)^{-1/2}u^{-\delta-1/2}e^{-1/(2u)}.
\]
For sufficiently large \(T\), the regular-variation remainder is uniformly bounded on the integration region, and the integrand is dominated by a constant multiple of
\[
u^{-\delta-1/2}e^{-1/(4u)},
\]
which is integrable on \((0,\infty)\). Dominated convergence therefore yields, uniformly over \(q\in K\),
\[
f_q(z)\sim A|z|^{1-2\delta},
\]
for a finite positive constant \(A\) independent of \(q\). Consequently,
\[
\sup_{q\in K,\,\xi\in B}\left|\frac{f_q(x+\xi)}{f_q(x)}-1\right|\longrightarrow0
\qquad (|x|\to\infty),
\]
because \(|x+\xi|/|x|\to1\) uniformly for \(\xi\in B\).

For the fixed-variance statement, take \(q=\sigma^2/n\). Conditional on \(\theta\), the likelihood of \(r_{1:n}^{(m)}\) as a function of \(\theta\) is proportional to
\[
\exp\left\{-\frac{n(\theta-b_m)^2}{2\sigma^2}\right\}.
\]
The Gaussian exponential-family identity for the sample-mean likelihood gives, for every fixed \(t\in\mathbb R\),
\[
\log\mathbb E\left[e^{t(\theta-b_m)}\mid r_{1:n}^{(m)}\right]
=
\log\frac{f_{\sigma^2/n}(b_m+\sigma^2t/n)}{f_{\sigma^2/n}(b_m)}
+\frac{\sigma^2t^2}{2n}.
\]
The local-ratio result makes the first term tend to zero. The conditional moment-generating functions therefore converge pointwise on \(\mathbb R\) to that of \(N(0,\sigma^2/n)\), and hence
\[
\theta-b_m\mid r_{1:n}^{(m)}\Rightarrow N\left(0,\frac{\sigma^2}{n}\right).
\]

For a fixed \(\Delta\), the posterior predictive density at \(b_m+\Delta\) is
\[
\mathbb E\left[\phi\left(\Delta-(\theta-b_m);0,\sigma^2\right)\mid r_{1:n}^{(m)}\right].
\]
The integrand is bounded and continuous, so weak convergence yields the Gaussian convolution limit
\[
p(b_m+\Delta\mid r_{1:n}^{(m)})
\longrightarrow
\frac{1}{\sqrt{2\pi\sigma^2(1+1/n)}}
\exp\left\{-\frac{\Delta^2}{2\sigma^2(1+1/n)}\right\}.
\]
Negating this expression gives \(h_n(|\Delta|)\). Its corresponding positive Gaussian density is strictly decreasing for positive \(u\), so \(h_n\) is strictly increasing on \([0,\infty)\). Thus the limiting score ordering is exactly the ordering by \(|\Delta|\).

For the plug-in statement, write
\[
\widehat v_m^2=\frac1n\sum_{i=1}^n(r_i^{(m)}-b_m)^2
\quad\text{and}\quad r_{n+1}^{(m)}=b_m+\Delta.
\]
The mean of the augmented \(n+1\) residuals is \(b_m+\Delta/(n+1)\). Expanding the centered sum of squares and using \(\sum_{i=1}^n(r_i^{(m)}-b_m)=0\) gives the exact identity
\[
\widehat a_{m,\Delta}
:=\frac1n\sum_{i=1}^{n+1}\left(r_i^{(m)}-\bar r_{n+1}^{(m)}\right)^2
=\widehat v_m^2+\frac{\Delta^2}{n+1}.
\]
Thus \(\widehat a_{m,\Delta}\to a_\Delta\), where
\[
a_\Delta=v^2+\frac{\Delta^2}{n+1}\in(0,\infty).
\]
For every fixed \(\Delta\), the values \(\widehat a_{m,\Delta}/n\) eventually lie in one compact subset of \((0,\infty)\). Repeating the preceding moment-generating-function argument, now using the compact-uniform local-ratio property, yields
\[
\theta-b_m\mid r_{1:n}^{(m)}
\Rightarrow N\left(0,\frac{a_\Delta}{n}\right).
\]
Since the observation variance is also \(\widehat a_{m,\Delta}\), bounded-continuous convergence together with \(\widehat a_{m,\Delta}\to a_\Delta\) gives
\[
S(b_m+\Delta,r_{1:n}^{(m)})
\longrightarrow
-\frac{1}{\sqrt{2\pi(1+1/n)a_\Delta}}
\exp\left\{-\frac{\Delta^2}{2(1+1/n)a_\Delta}\right\}
=h_{n,v}(|\Delta|).
\]

Finally, set \(V(u)=v^2+u^2/(n+1)\) and let \(q(u)=-h_{n,v}(u)>0\). For \(u>0\),
\[
\frac{d}{du}\log q(u)
=-\frac{u}{(n+1)V(u)}
-\frac{uv^2}{(1+1/n)V(u)^2}<0.
\]
Hence \(q\) is strictly decreasing on \((0,\infty)\), and continuity at zero implies that \(h_{n,v}=-q\) is strictly increasing on \([0,\infty)\). This proves the same limiting centered-residual ordering in the plug-in construction.
