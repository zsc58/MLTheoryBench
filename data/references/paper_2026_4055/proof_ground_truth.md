# Reference Proof

## Proof Obligations

1. Verify well-definedness of the expectations and the hypotheses of the conditional bounded-difference moment inequality.
2. Combine the conditional sampling moment bound with the assumed mixture moment bound and derive both tails, including a zero effective proxy.
3. Compute the conditional mean of every integrable linear contrast, establish zero-sum cancellation, and prove the converse without assuming a finite second moment.
4. Verify conditional bounded support, compute the subsample contrast coefficients and their squared norm, and obtain the tail and confidence bounds, including a zero interval width.

## Standard Independent Result Used

For independent random variables Y_1,...,Y_k and a measurable real-valued function g with finite bounded-difference constants c_1,...,c_k on their product state space, the bounded-difference moment inequality states that
\[
\mathbb E\exp\{\lambda(g(Y)-\mathbb Eg(Y))\}
\le \exp\!\left(\frac{\lambda^2}{8}\sum_{i=1}^k c_i^2\right),
\qquad \lambda\in\mathbb R.
\]
This is the standard independent result recorded as theory_005 and explicitly used in the source at L000102-L000103. It is a moment inequality, not an inference from a two-sided tail inequality. It applies to each conditional product law with the same deterministic constants. The directing conditional product law is already supplied in the task; its existence is also the standard de Finetti result, whose infinite-exchangeability and standard-Borel hypotheses are satisfied.

## Complete Proof

### Well-definedness and general concentration

Fix a point z^* in the nonempty product space \(\mathcal Z^m\). Successively changing its coordinates to those of z gives
\[
|h(z)-h(z^*)|\le \sum_{i=1}^m d_i.
\]
Thus h is bounded, and H and all its conditional expectations are integrable.

Put
\[
W=H-\mathbb E[H\mid\Lambda],
\qquad B_h=\mathbb E[H\mid\Lambda]-\mathbb EH.
\]
Conditional on \(\Lambda\), the variables are independent with common law \(\Lambda\). The measurable function h retains its bounded-difference constants on this product law. Consequently, for every fixed real \(\lambda\), the standard independent moment inequality gives, almost surely,
\[
\mathbb E[e^{\lambda W}\mid\Lambda]
\le \exp\!\left(\frac{\lambda^2}{8}\sum_{i=1}^m d_i^2\right).
\]
The conditional centering agrees with integration under \(\Lambda^{\otimes m}\), by the given conditional product law. Since \(B_h\) is measurable with respect to \(\Lambda\), the tower property and the assumed mixture bound yield
\[
\begin{aligned}
\mathbb E e^{\lambda(H-\mathbb EH)}
&=\mathbb E\left[e^{\lambda B_h}\mathbb E(e^{\lambda W}\mid\Lambda)\right]\\
&\le \exp\!\left(\frac{\lambda^2}{8}\sum_{i=1}^m d_i^2\right)\mathbb E e^{\lambda B_h}\\
&\le \exp\!\left\{\frac{\lambda^2}{2}
\left(\frac14\sum_{i=1}^m d_i^2+s_{\mathrm{mix}}^2\right)\right\}.
\end{aligned}
\]
No independence between W and \(B_h\) is asserted or needed.

Write
\[
s_{\mathrm{eff}}^2=\frac14\sum_{i=1}^m d_i^2+s_{\mathrm{mix}}^2.
\]
For \(t>0\) and \(\lambda>0\), Markov's inequality gives
\[
\mathbb P(H-\mathbb EH\ge t)
\le \exp\!\left(-\lambda t+\frac{\lambda^2s_{\mathrm{eff}}^2}{2}\right).
\]
If \(s_{\mathrm{eff}}^2>0\), choose \(\lambda=t/s_{\mathrm{eff}}^2\). Applying the same argument to \(-(H-\mathbb EH)\) and taking a union bound gives
\[
\mathbb P(|H-\mathbb EH|\ge t)
\le 2\exp\!\left(-\frac{t^2}{2s_{\mathrm{eff}}^2}\right).
\]
If \(s_{\mathrm{eff}}^2=0\), the upper-tail bound is at most \(e^{-\lambda t}\) for every \(\lambda>0\), hence is zero by letting \(\lambda\) increase to infinity. The lower tail is zero in the same way. This proves the stated tail bound under the zero-denominator convention as well.

### Linear contrasts

Suppose the variables are real-valued and \(\mathbb E|Z_1|<\infty\). Identical marginal distributions give integrability of every \(Z_i\), and hence of any finite deterministic linear contrast L. Moreover,
\[
\mathbb E|m(\Lambda)|\le \mathbb E|Z_1|<\infty.
\]
Conditional identical distribution and linearity give
\[
\mathbb E[L\mid\Lambda]
=\sum_{i=1}^N b_i\mathbb E[Z_i\mid\Lambda]
=\left(\sum_{i=1}^N b_i\right)m(\Lambda).
\]
Taking expectations and subtracting shows
\[
B_L:=\mathbb E[L\mid\Lambda]-\mathbb EL
=\left(\sum_{i=1}^N b_i\right)
\bigl(m(\Lambda)-\mathbb E m(\Lambda)\bigr).
\]
If the coefficient sum is zero, this identity directly proves \(B_L=0\) almost surely. Its moment generating function is therefore one for every real parameter, so a zero mixture proxy is valid. This argument does not multiply zero by a potentially infinite variance.

Conversely, suppose \(\operatorname{Var}(m(\Lambda))>0\) and the coefficient sum is nonzero. The extended variance being positive means that \(m(\Lambda)\) is not almost surely constant. Thus the displayed expression for \(B_L\) is not almost surely zero. A zero mixture proxy would imply \(\mathbb E e^{\lambda B_L}\le1\) for every real \(\lambda\). Since \(B_L\) is integrable and centered, Jensen's inequality at \(\lambda=1\) gives \(\mathbb E e^{B_L}\ge1\). Equality in strict convexity forces \(B_L\) to be almost surely constant, and its mean then forces that constant to be zero, a contradiction. This proves the converse whether the positive variance is finite or infinite.

### Subsample-minus-full contrast

Now assume \(Z_i\in[\ell,u]\) almost surely, with finite \(\ell\le u\), and set \(R=u-\ell\). These variables are integrable. Their conditional law is supported on the same interval: indeed,
\[
\mathbb E[\Lambda([\ell,u])]=\mathbb P(Z_1\in[\ell,u])=1,
\]
so \(\Lambda([\ell,u])=1\) almost surely. We may therefore apply the general result on the standard Borel state space \([\ell,u]\).

For fixed integers \(1\le n<N\), write
\[
D_{n,N}=\sum_{j=1}^N b_jZ_j,
\qquad
b_j=\begin{cases}
\frac1n-\frac1N,&j\le n,\\
-\frac1N,&n<j\le N.
\end{cases}
\]
Their sum is
\[
n\left(\frac1n-\frac1N\right)-(N-n)\frac1N=0.
\]
The linear-contrast result gives \(\mathbb E[D_{n,N}\mid\Lambda]=0\), \(\mathbb E D_{n,N}=0\), and a zero mixture proxy.

On \([\ell,u]^N\), changing coordinate j changes the contrast by at most \(R|b_j|\). Thus its bounded-difference constants are \(d_j=R|b_j|\), and
\[
\begin{aligned}
\sum_{j=1}^N b_j^2
&=n\left(\frac1n-\frac1N\right)^2+(N-n)\frac1{N^2}\\
&=\frac{(N-n)^2+n(N-n)}{nN^2}
=\frac{N-n}{nN}.
\end{aligned}
\]
Its effective proxy is therefore
\[
s_{\mathrm{eff}}^2=\frac{R^2(N-n)}{4nN}.
\]
The general tail inequality yields, for every \(t>0\),
\[
\mathbb P(|D_{n,N}|\ge t)
\le2\exp\!\left(-\frac{2t^2nN}{R^2(N-n)}\right).
\]
This includes \(R=0\) under the stated convention. More directly, in that case every \(Z_i=\ell\) almost surely, so \(D_{n,N}=0\) almost surely, and the confidence statement with zero half-width also holds.

For \(R>0\) and \(0<\alpha<1\), set
\[
q=R\sqrt{\frac{N-n}{2nN}\log\frac2\alpha}>0.
\]
Substituting \(t=q\) in the tail bound gives \(\mathbb P(|D_{n,N}|\ge q)\le\alpha\), and hence \(\mathbb P(|D_{n,N}|\le q)\ge1-\alpha\), as required.

All listed proof obligations are closed.
