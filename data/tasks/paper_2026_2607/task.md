# Problem

## Setup

Let \((X,\mathcal A)\) be a measurable space and let \(Y=(0,\infty)\). A loss is ratio-based if
\[
L(x,y,t)=\ell\!\left(\frac{u(t)+c}{y+c}\right),
\]
where \(c\ge0\), \(u:\mathbb R\to Y\) is measurable, monotone, and surjective, and \(\ell:(0,\infty)\to[0,\infty)\) is measurable with \(\ell(1)=0\). Take \(c=0\) and \(u(t)=e^t\).

Let \(g\in C^1((0,\infty))\) be increasing and suppose that for some finite \(M>0\),
\[
-M\le g(r)\le M\qquad(r>0).
\]
Choose \(r_0\ge0\) and \(C\) so that
\[
\phi(r)=C+\int_{r_0}^{r}\frac{g(s)}{s}\,ds
\]
is well-defined, finite, and nonnegative on \((0,\infty)\); if \(r_0=0\), the integral is the improper limit \(\lim_{\varepsilon\downarrow0}\int_{\varepsilon}^{r}g(s)/s\,ds\). Define
\[
\ell(r)=\phi(r)+\phi(r^{-1})-2\phi(1),
\qquad
L(x,y,t)=\ell(e^t/y).
\]

## Task

Prove that \(L\) is a ratio-based loss, that for every \(x\in X\) and \(y>0\) the map \(t\mapsto L(x,y,t)\) is convex, and that \(L\) is globally Lipschitz in \(t\) with Lipschitz constant at most \(2M\); namely,
\[
|L(x,y,t)-L(x,y,t')|\le2M|t-t'|
\quad\text{for all }x\in X,\ y>0,\ t,t'\in\mathbb R.
\]
