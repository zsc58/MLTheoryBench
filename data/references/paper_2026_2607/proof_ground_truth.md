# Reference Proof

## Proof Structure

We verify the ratio-based definition, derive the differential condition from the integral generator, use the logarithmic reparameterization to establish convexity and nonnegativity, and obtain the uniform derivative and Lipschitz bounds.

## Complete Proof

Let
\[
\phi(r)=C+\int_{r_0}^{r}\frac{g(s)}{s}\,ds,
\qquad r>0,
\]
where, if \(r_0=0\), the integral denotes the improper limit \(\lim_{\varepsilon\downarrow0}\int_{\varepsilon}^{r}g(s)/s\,ds\), assumed to exist and be finite by hypothesis. Since \(g\in C^1\),
\[
\phi'(r)=\frac{g(r)}r,
\qquad
\phi''(r)=\frac{g'(r)}r-\frac{g(r)}{r^2},
\]
so \(\phi'(r)+r\phi''(r)=g'(r)\ge0\).

Set \(f(s)=\phi(e^s)\). Then
\[
f''(s)=e^s\bigl(\phi'(e^s)+e^s\phi''(e^s)\bigr)=e^s g'(e^s)\ge0,
\]
so \(f\) is convex. Define
\[
\ell(r)=\phi(r)+\phi(r^{-1})-2\phi(1).
\]
For \(r=e^s\), midpoint convexity gives
\[
\ell(e^s)=f(s)+f(-s)-2f(0)\ge0,
\]
and clearly \(\ell(1)=0\). Thus \(\ell\) is measurable and nonnegative. Since \(u(t)=e^t\) is measurable, monotone, and surjective from \(\mathbb R\) onto \((0,\infty)\), \(L(x,y,t)=\ell(e^t/y)\) is ratio-based.

For fixed \(y>0\),
\[
L(x,y,t)=f(t-\log y)+f(\log y-t)-2f(0),
\]
which is convex in \(t\) as a sum of convex functions composed with affine maps.

Writing \(q=e^t/y\), differentiation gives
\[
\partial_tL(x,y,t)=g(q)-g(q^{-1}).
\]
The assumption \(|g(r)|\le M\) implies \(|\partial_tL(x,y,t)|\le2M\) uniformly. The mean-value theorem therefore yields
\[
|L(x,y,t)-L(x,y,t')|\le2M|t-t'|
\]
for all \(x\in X\), \(y>0\), and \(t,t'\in\mathbb R\).
