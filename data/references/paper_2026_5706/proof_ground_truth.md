# Reference Proof

## Proof Structure

First partition the standardized score sum according to the two reward values. This identifies its scalar coefficient with the empirical reward standard deviation and also establishes invariance under a common baseline. In the Bernoulli-logit model, the score contrast is exactly one, so averaging over the binomial success count gives the finite-group formula. Finally, a Taylor expansion of \(f(u)=\sqrt{u(1-u)}\) around the fixed interior success probability gives the attenuation term, and the chain rule identifies the limit with an arcsine-transformed objective gradient.

The six theorem-critical obligations are the group identity, baseline invariance, scalar score contrast, exact unconditional expectation, fixed-interior asymptotic with its stated remainder, and arcsine-gradient identification. Each is derived below. The analytic background indexed by `theory_012` is ordinary Taylor expansion with integral remainder, classified as `standard_independent`. Its relevant statement and hypotheses are given explicitly below. The Bernoulli moment and tail estimates are derived directly; no specialized external theorem or concentration bound is left as an unresolved dependency.

## Complete Proof

Fix a realized non-unanimous group and write \(K=k\), where \(1\le k\le G-1\). Then \(M=k/G\) and
\[
 S=\sqrt{M(1-M)}=\frac{\sqrt{k(G-k)}}{G}.
\]
For a successful sample,
\[
 A_i=\frac{1-M}{S}=\frac{G-k}{GS},
\]
whereas for an unsuccessful sample,
\[
 A_i=-\frac{M}{S}=-\frac{k}{GS}.
\]
Partitioning the update into successful and unsuccessful samples therefore gives
\[
\begin{aligned}
 U
 &=\frac1G\left(\frac{G-k}{GS}\sum_{R_i=1}S_i
                 -\frac{k}{GS}\sum_{R_i=0}S_i\right)\\
 &=\frac1G\left(\frac{k(G-k)}{GS}\,\overline S_+
                 -\frac{k(G-k)}{GS}\,\overline S_-\right)\\
 &=\frac{k(G-k)}{G^2S}(\overline S_+-\overline S_-).
\end{aligned}
\]
Since \(S^2=k(G-k)/G^2\), the coefficient is \(S\), and hence
\[
 U=S(\overline S_+-\overline S_-).
\]
For a unanimous group, both sides are defined to be zero, as stipulated.

The baseline assertion follows directly from centering. If every reward is replaced by \(R_i-b\), its group mean becomes \(M-b\), so
\[
 (R_i-b)-(M-b)=R_i-M.
\]
Consequently both the centered rewards and their empirical standard deviation are unchanged, and so is \(U\). This argument concerns a common reward shift before centering, not an additive shift of already-standardized advantages. It also preserves the zero-update convention because the empirical standard deviation is unchanged.

Now specialize to the Bernoulli-logit model. A successful sample has score \(1-p\), while an unsuccessful sample has score \(-p\). Thus, for every mixed group,
\[
 \overline S_+-\overline S_-=(1-p)-(-p)=1.
\]
The identity just proved yields
\[
 U(k)=\frac{\sqrt{k(G-k)}}{G}
\]
for \(1\le k\le G-1\), and \(U(0)=U(G)=0\). Since \(K\sim\operatorname{Binomial}(G,p)\), averaging this expression gives
\[
 \mathbb E[U]
 =\frac1G\sum_{k=1}^{G-1}\binom Gk p^k(1-p)^{G-k}\sqrt{k(G-k)}.
\]
This proves the exact finite-group formula. The expectation is unconditional: unanimous groups remain in the experiment and contribute zero, rather than being discarded and the remaining probabilities renormalized.

For the asymptotic formula, fix \(p\in(0,1)\), let \(q=p(1-p)\), \(X=K/G\), and \(f(u)=\sqrt{u(1-u)}\) for \(u\in[0,1]\). The preceding formula, including the zero endpoint values, is equivalently \(\mathbb E[U]=\mathbb E[f(X)]\).

We first derive the needed centered moments. Write \(Z_i=Y_i-p\) and \(\Delta=X-p=G^{-1}\sum_{i=1}^G Z_i\). The independent variables \(Z_i\) have mean zero. Directly from the two Bernoulli outcomes,
\[
 \mathbb E[Z_i^2]=q,\qquad
 \mathbb E[Z_i^3]=q(1-2p),\qquad
 \mathbb E[Z_i^4]=q(1-3q).
\]
Independence and zero means eliminate terms containing an index that occurs only once when a power of \(\sum_i Z_i\) is expanded. Therefore
\[
 \mathbb E[\Delta]=0,\qquad
 \mathbb E[\Delta^2]=\frac qG,\qquad
 \mathbb E[\Delta^3]=\frac{q(1-2p)}{G^2}.
\]
For the fourth moment, the surviving terms have either all four indices equal or two equal pairs, giving
\[
\begin{aligned}
 \mathbb E[\Delta^4]
 &=\frac{Gq(1-3q)+6\binom G2 q^2}{G^4}\\
 &=\frac{3q^2}{G^2}+\frac{q(1-6q)}{G^3}
 =O(G^{-2}).
\end{aligned}
\]
In particular, the third moment used here is the signed centered moment; it is not a claim that \(\mathbb E|\Delta|^3=O(G^{-2})\).

Here is the precise standard Taylor result used. If \(h\) has four continuous derivatives on an interval containing \(p\) and \(u\), repeated application of the fundamental theorem of calculus gives
\[
 h(u)=\sum_{j=0}^3\frac{h^{(j)}(p)}{j!}(u-p)^j
       +\frac1{3!}\int_p^u (u-t)^3h^{(4)}(t)\,dt.
\]
If \(|h^{(4)}|\le B\) on that interval, the remainder has absolute value at most \(B|u-p|^4/24\). This result is independent of the policy-gradient setting.

To verify its hypotheses locally without assuming smoothness at the endpoints, choose
\[
 \delta=\tfrac12\min\{p,1-p\}>0,
 \qquad I=[p-\delta,p+\delta]\subset(0,1).
\]
The function \(f\) has four continuous derivatives on \(I\), with bounded fourth derivative there. Define its cubic Taylor polynomial at \(p\) by
\[
 T_3(u)=f(p)+f'(p)(u-p)+\frac12f''(p)(u-p)^2
                   +\frac16f'''(p)(u-p)^3.
\]
On the event \(E=\{|\Delta|\le\delta\}\), Taylor's formula gives
\[
 |f(X)-T_3(X)|\le C_p|\Delta|^4.
\]
For the complementary event, the pointwise inequality
\(\mathbf 1_{\{|\Delta|>\delta\}}\le |\Delta|^4/\delta^4\) gives
\[
 \mathbb P(E^c)\le\delta^{-4}\mathbb E[\Delta^4]=O(G^{-2}).
\]
Both \(f\) and \(T_3\) are bounded on \([0,1]\): \(0\le f\le1/2\), and \(T_3\) is a fixed polynomial for the chosen \(p\). Thus
\[
\begin{aligned}
 \big|\mathbb E[f(X)]-\mathbb E[T_3(X)]\big|
 &\le C_p\mathbb E[\Delta^4]
   +\sup_{u\in[0,1]}|f(u)-T_3(u)|\,\mathbb P(E^c)\\
 &=O(G^{-2}).
\end{aligned}
\]
This controls the entire complementary event, not just the unanimous outcomes, and also controls the Taylor polynomial on that event.

Taking expectations of the polynomial and using the displayed centered moments now yields
\[
\begin{aligned}
 \mathbb E[f(X)]
 &=f(p)+\frac12f''(p)\frac qG
       +\frac16f'''(p)\frac{q(1-2p)}{G^2}
       +O(G^{-2})\\
 &=f(p)+\frac12f''(p)\frac qG+O(G^{-2}).
\end{aligned}
\]
Direct differentiation gives
\[
 f''(p)=-\frac1{4q^{3/2}}.
\]
It follows that
\[
\begin{aligned}
 \mathbb E[U]
 &=\sqrt q-\frac1{8G\sqrt q}+O(G^{-2})\\
 &=\sqrt{p(1-p)}\left(1-\frac1{8Gp(1-p)}+O(G^{-2})\right).
\end{aligned}
\]
Every implicit constant here may depend on the fixed interior value \(p\). No uniform assertion as \(p\) approaches an endpoint, or along a varying sequence \(p=p_G\), is being made.

Finally, for \(H(p)=2\arcsin\sqrt p\),
\[
 H'(p)=\frac1{\sqrt{p(1-p)}}.
\]
Because \(p=(1+e^{-\theta})^{-1}\) satisfies \(dp/d\theta=p(1-p)\), the chain rule yields
\[
 \frac d{d\theta}H(p(\theta))
 =\sqrt{p(1-p)}.
\]
Thus the leading large-group term is precisely the logit-parameter gradient of the stated arcsine transform.
