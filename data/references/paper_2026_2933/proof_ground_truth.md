# Reference Proof

## Proof Structure

1. Specify the symmetric uniform quantizer and apply the stipulated additive error-power model.
2. Evaluate the Gaussian clipping tails and the uniform stepping second moment.
3. Substitute the symmetric spacing, form the modeled SNR objective, and identify the resulting optimizer and quantizer parameters.

## Complete Proof

Use level indices \(k=0,\ldots,N-1\). Symmetry with endpoint levels \(-C\) and \(C\) gives
\[
z=-C,\qquad s=\frac{2C}{N-1},\qquad l_k=-C+sk.
\]
For \(j=1,\ldots,N-1\), the internal thresholds are
\[
t_j=s(j-\tfrac12)-C=\frac{l_{j-1}+l_j}{2},
\]
with \(t_0=-\infty\) and \(t_N=\infty\). These define a measurable quantizer on all real inputs, including when \(N=2\). Observations outside \([-C,C]\) are assigned to their corresponding endpoint levels.

The public task stipulates an additive error-power model. Its clipping component is the squared error from saturating the input at the endpoint values, and its stepping component is the stipulated uniform stepping power. This is not a derivation of an exact deterministic quantizer MSE from the Gaussian density, and the stipulated stepping power is not multiplied by an unsaturated-event probability.

For a uniform stepping-error variable on \([-s/2,s/2]\),
\[
E_s=\frac1s\int_{-s/2}^{s/2}u^2\,du
=\frac1s\left[\frac{u^3}{3}\right]_{-s/2}^{s/2}
=\frac{s^2}{12}.
\]
The Gaussian clipping component is finite because the Gaussian input has a finite second moment. Symmetry gives
\[
E_c=2\int_C^\infty (x-C)^2\frac1\sigma\phi(x/\sigma)\,dx.
\]
Set \(a=C/\sigma\) and substitute \(u=x/\sigma\). Then
\[
E_c=2\sigma^2\int_a^\infty (u-a)^2\phi(u)\,du.
\]
Since \(\phi'(u)=-u\phi(u)\), direct integration yields
\[
\int_a^\infty u\phi(u)\,du
=[-\phi(u)]_a^\infty=\phi(a).
\]
Also \((u\phi(u))'=\phi(u)-u^2\phi(u)\), so
\[
\int_a^\infty u^2\phi(u)\,du
=\int_a^\infty\phi(u)\,du-[u\phi(u)]_a^\infty
=Q(a)+a\phi(a).
\]
The boundary terms vanish because \(\phi(u)\) and \(u\phi(u)\) tend to zero as \(u\to\infty\). Expanding the squared integrand therefore gives
\[
\begin{aligned}
E_c
&=2\sigma^2\bigl[Q(a)+a\phi(a)-2a\phi(a)+a^2Q(a)\bigr]\\
&=2\sigma^2\bigl[(1+a^2)Q(a)-a\phi(a)\bigr]\\
&=2(\sigma^2+C^2)Q(C/\sigma)-2C\sigma\phi(C/\sigma).
\end{aligned}
\]
By the stipulated additive model and the spacing relation,
\[
\begin{aligned}
E(C)&=E_c+E_s\\
&=2(\sigma^2+C^2)Q(C/\sigma)-2C\sigma\phi(C/\sigma)
+\frac{C^2}{3(N-1)^2}.
\end{aligned}
\]
For every \(C>0\), this quantity is finite and strictly positive: the clipping contribution is nonnegative, and the stepping contribution is strictly positive because \(N\ge2\). The input mean-square power is \(\mathbb E[X^2]=\sigma^2\). Consequently, the task's definition of modeled SNR gives
\[
\operatorname{SNR}(C)=\frac{\sigma^2}{E(C)}.
\]
Because \(\sigma^2>0\) is fixed and \(E(C)>0\), maximizing this ratio over \(C>0\) is equivalent to minimizing \(E(C)\) over that same domain.

For completeness, this optimization domain has a global minimizer. Extend the error continuously to \(C=0\), where \(E(0)=\sigma^2\). Differentiating the clipping integral gives
\[
E_c'(C)=4\int_C^\infty(C-x)\frac1\sigma\phi(x/\sigma)\,dx
=4\bigl[C Q(C/\sigma)-\sigma\phi(C/\sigma)\bigr].
\]
Differentiation is justified locally by the integrable Gaussian first-moment bound, and the boundary integrand is zero. Thus the right derivative of the extended total error at zero is
\[
E'(0)=-4\sigma\phi(0)<0.
\]
Some positive \(C\) therefore has error strictly below \(E(0)\). Moreover,
\[
E(C)\ge\frac{C^2}{3(N-1)^2}\longrightarrow\infty
\quad\text{as }C\to\infty.
\]
Continuity and this lower bound place a global minimum on a compact interval in \([0,\infty)\); it cannot occur at zero, so it occurs at a positive clipping value. This existence argument is supplementary and does not require a particular numerical search algorithm.

Any global optimizer \(C^*\) in the stated argmax, whether obtained numerically or otherwise, determines
\[
s^*=\frac{2C^*}{N-1},\qquad z^*=-C^*,\qquad
l_k^*=-C^*+s^*k,
\]
with internal midpoint thresholds and infinite outer thresholds as above. Equivalent centered indexing gives the same quantizer. It is normal-optimal within the symmetric uniform family for the stipulated modeled error-power objective; no claim of exact deterministic-MSE optimality or guaranteed numerical-search convergence is needed.

## Obligation Closure

- The finite symmetric quantizer, all index ranges, saturation, and measurability are explicit.
- The additive model and uniform stepping power are stipulated, and the stepping second moment is integrated directly.
- The endpoint-clipping integral follows from Gaussian symmetry, and both required Gaussian moment identities are derived explicitly.
- Finiteness, positivity, the input power, and the SNR/minimization equivalence are verified.
- Compatible optimized levels and thresholds are exhibited; optimizer existence is checked by a routine boundary argument.

No theorem-critical obligation remains unresolved.
