# Reference Proof

## Proof Structure

Establish estimates relating the gradients at the current and perturbed points; use them to prove the scheduler is well defined away from an optimum and to derive a one-step squared-distance decrease. Strong convexity converts that decrease into a recurrence, while convexity and Jensen's inequality give the averaged bound.

## Complete Proof

Write, for a fixed iteration,
\[
g=\nabla f(x),\qquad y=x+r g,\qquad h=\nabla f(y),\qquad F=f(x)-f^*,
\]
and set
\[
A=f(y)-f^*-r\langle h,g\rangle.
\]

Convexity and monotonicity of the gradient give
\[
\langle h,g\rangle\ge \|g\|^2,
\qquad
r\langle h,g\rangle\ge f(y)-f(x).
\]
The first inequality is immediate when \(r=0\); for \(r>0\), apply gradient monotonicity to \(x,y\). Smoothness gives
\[
\|h\|\le (1+Lr)\|g\|.
\]
Applying the descent lemma with base point \(y\) and endpoint \(x=y-rg\) yields
\[
f(x)\le f(y)-r\langle h,g\rangle+\frac{Lr^2}{2}\|g\|^2,
\]
and therefore
\[
A\ge F-\frac{Lr^2}{2}\|g\|^2.
\]
For a convex \(L\)-smooth function with a minimizer,
\[
\|g\|^2\le 2L F.
\]
Indeed, the descent lemma at \(x-L^{-1}g\), together with \(f^*\le f(x-L^{-1}g)\), proves it. Consequently,
\[
A\ge \bigl(1-(Lr)^2\bigr)F\ge0.
\]
Thus the positive part in the step-size formula is redundant whenever its denominator is nonzero. If \(F=0\), convex differentiability gives \(g=0\), hence \(y=x\), \(h=0\), and the stipulated no-op convention applies. If \(F>0\), then \(g\ne0\), and \(\langle h,g\rangle\ge\|g\|^2\) ensures \(h\ne0\). In this case the preceding estimates give
\[
\frac{A^2}{\|h\|^2}
\ge
\frac{(1-(Lr)^2)^2F^2}{2L(1+Lr)^2F}
=
\frac{(1-Lr)^2}{2L}F. \tag{1}
\]
This remains valid at \(r=1/L\), when its right-hand side is zero.

We next prove the key distance decrease. Convexity at \(y\) implies
\[
\langle h,x-x^*\rangle
=\langle h,y-x^*\rangle-r\langle h,g\rangle
\ge f(y)-f^*-r\langle h,g\rangle=A.
\]
Since \(\alpha=A/\|h\|^2\) when \(h\ne0\), expansion of the update gives
\[
\begin{aligned}
\|x^+-x^*\|^2
&=\|x-x^*\|^2-2\alpha\langle h,x-x^*\rangle+\alpha^2\|h\|^2\\
&\le \|x-x^*\|^2-\frac{A^2}{\|h\|^2}\\
&\le \|x-x^*\|^2-\frac{(1-Lr)^2}{2L}\bigl(f(x)-f^*\bigr). \tag{2}
\end{aligned}
\]
If \(h=0\), the earlier inequality \(\langle h,g\rangle\ge\|g\|^2\) gives \(g=0\). Thus \(x\) is a minimizer and (2) also holds under the no-op convention. Applying (2) at every iteration proves
\[
\|x_{t+1}-x^*\|^2\le \|x_t-x^*\|^2-\frac{(1-Lr)^2}{2L}\bigl(f(x_t)-f^*\bigr). \tag{3}
\]

If \(f\) is \(m\)-strongly convex, convexity of \(z\mapsto f(z)-m\|z\|^2/2\), applied at the minimizer \(x^*\) where \(\nabla f(x^*)=0\), gives
\[
f(x_t)-f^*\ge \frac m2\|x_t-x^*\|^2.
\]
Substitution into (3) yields
\[
\|x_{t+1}-x^*\|^2
\le \left(1-\frac{m(1-Lr)^2}{4L}\right)\|x_t-x^*\|^2.
\]
In positive dimension, strong convexity and \(L\)-smoothness imply \(m\le L\): apply strong gradient monotonicity and the Lipschitz bound to two distinct points. Thus the factor is nonnegative, and iteration proves the first claimed bound. In the zero-dimensional case every iterate equals \(x^*\), so the claim is immediate.

For the convex case, summing (3) from \(t=0\) to \(T-1\) and telescoping gives
\[
\frac{(1-Lr)^2}{2L}\sum_{t=0}^{T-1}\bigl(f(x_t)-f^*\bigr)
\le \|x_0-x^*\|^2.
\]
Convexity and the definition of \(\bar x_T\) imply
\[
f(\bar x_T)-f^*\le \frac1T\sum_{t=0}^{T-1}\bigl(f(x_t)-f^*\bigr).
\]
Combining the last two displays proves
\[
(1-Lr)^2\bigl(f(\bar x_T)-f^*\bigr)
\le \frac{2L\|x_0-x^*\|^2}{T}.
\]
When \(r<1/L\), division by \((1-Lr)^2\) gives the stated \(O(1/T)\) bound. No division is made at \(r=1/L\). This completes the proof.
