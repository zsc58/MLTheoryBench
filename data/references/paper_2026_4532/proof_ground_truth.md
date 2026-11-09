# Reference Proof

## Proof Structure

1. Show that a jointly consistent collection of conditionals makes the random-scan kernel reversible with respect to the common joint law; uniqueness of the limiting distribution identifies that law with the chain's stationary distribution.
2. For the converse, apply detailed balance to pairs of distinct states that differ in exactly one component. All other scan terms vanish and the common scan weight cancels, yielding a cross-multiplied relation between stationary masses and modeled conditional probabilities. For equal component values, that relation holds tautologically.
3. Use normalization, without dividing by a possibly zero modeled probability, to identify the two conditional distributions for every component and every complement. This proves joint consistency and the final identification, including singleton components.

## Complete Proof

For every starting state \(x'\), the kernel is nonnegative and
\[
\sum_x K(x\mid x')=\sum_i\alpha_i\sum_{a\in\mathcal X_i}c_i(a\mid x'_{-i})=1.
\]
Let \(\pi\) denote its unique stationary distribution, as supplied by the setup. If \(K^N\) is strictly positive, stationarity gives
\[
\pi(x)=\sum_y K^N(x\mid y)\pi(y)>0
\]
for every \(x\), because at least one \(\pi(y)\) is positive. Consequently all stationary conditional distributions appearing below are defined at every complement.

Assume first that the modeled conditionals are jointly consistent. Thus there is a probability mass function \(\rho\) on \(\mathcal X\), with full support, such that
\[
 c_i(a\mid r)=\frac{\rho(a,r)}{\sum_t\rho(t,r)}
\]
for every component \(i\), complement \(r\), and value \(a\). If \(x,x'\) differ in more than one component, then \(K(x\mid x')=K(x'\mid x)=0\). If they differ in exactly one component \(i\), write their common complement as \(r\), and let \(x=(a,r)\), \(x'=(b,r)\), where \(a\ne b\). Then
\[
\rho(x')K(x\mid x')=\alpha_i\rho(b,r)c_i(a\mid r)
=\alpha_i\frac{\rho(a,r)\rho(b,r)}{\sum_t\rho(t,r)}
=\rho(x)K(x'\mid x).
\]
For \(x=x'\), detailed balance is an identity. Hence \(K\) satisfies detailed balance with respect to \(\rho\). Summing this equality over \(x'\) gives
\[
\sum_{x'}\rho(x')K(x\mid x')
=\rho(x)\sum_{x'}K(x'\mid x)=\rho(x),
\]
so \(\rho\) is stationary. By uniqueness, \(\rho=\pi\). Thus detailed balance with respect to \(\pi\) follows, and each modeled conditional is the corresponding conditional of \(\pi\).

Conversely, assume detailed balance with respect to \(\pi\):
\[
\pi(x')K(x\mid x')=\pi(x)K(x'\mid x)\qquad\text{for all }x,x'.
\]
Fix a component \(i\) and a complement \(r\). For distinct values \(a,b\in\mathcal X_i\), set \(x=(a,r)\) and \(x'=(b,r)\). For every \(j\ne i\), the complement to coordinate \(j\) contains coordinate \(i\), at which these states differ. Therefore the \(j\)-term vanishes in both transition directions. Detailed balance and \(\alpha_i>0\) give
\[
\pi(b,r)c_i(a\mid r)=\pi(a,r)c_i(b\mid r).
\]
When \(a=b\), this displayed equality is tautological; no assertion about vanishing scan terms is needed. Thus it holds for all \(a,b\), including when \(\mathcal X_i\) is a singleton.

Let \(u_a=\pi(a,r)\) and \(v_a=c_i(a\mid r)\). Then \(u_bv_a=u_av_b\) for all \(a,b\). Summing over \(b\), and using \(\sum_bv_b=1\), yields
\[
\left(\sum_bu_b\right)v_a=u_a.
\]
The sum \(\sum_bu_b\) is strictly positive, so
\[
 c_i(a\mid r)=\frac{\pi(a,r)}{\sum_t\pi(t,r)}=\pi(a\mid r).
\]
This argument permits modeled probabilities initially to be zero; it never divides by one. The equality holds for every component and every complement. Since \(\pi\) has full support, it witnesses joint consistency. This proves both the equivalence and the final identification.

## Private Source-Contract Verification

The source defines consistency through a common joint distribution without separately imposing full support. Under the inherited positive-power assumption, this is equivalent to the public definition. Indeed, let \(\rho\) be any common joint, interpreting its conditionals on complements with positive marginal mass. Put \(\rho_{-i}(r)=\sum_a\rho(a,r)\). On positive-mass complements,
\[
\rho(a,r)=\rho_{-i}(r)c_i(a\mid r).
\]
On a zero-mass complement, all \(\rho(a,r)\) vanish, so the same identity holds irrespective of the specified conditional there. For the single-coordinate kernel
\[
G_i(x\mid x')=c_i(x_i\mid x'_{-i})\mathbf 1\{x_{-i}=x'_{-i}\},
\]
one consequently has, on a common complement \(r\),
\[
\rho(b,r)G_i((a,r)\mid(b,r))
=\rho_{-i}(r)c_i(b\mid r)c_i(a\mid r)
=\rho(a,r)G_i((b,r)\mid(a,r)).
\]
For unequal complements both sides are zero. Each coordinate kernel, and therefore their fixed-weight mixture, is reversible with respect to \(\rho\). Summing detailed balance proves stationarity as above. Uniqueness implies \(\rho=\pi\), so the common joint necessarily has full support. This calculation also supplies the complete standard Gibbs-sampler fact used by the source; no specialized external result is left unproved.

The source's recurrent lower-bound construction and stationarity-mixture display are not needed for this characterization. The previously recorded repair of the source's ratio step is implemented by the cross-multiplied normalization argument above. All proof obligations are closed.
