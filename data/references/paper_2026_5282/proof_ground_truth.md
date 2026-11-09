# Reference Proof

## Proof Structure

We establish the uniform one-sided approximation bounds from monotonicity and the inverse hyperbolic tangent, then differentiate the sigmoid-tanh composition to obtain both tail asymptotics and the slope at the origin. Symmetry supplies the negative half-line approximation and the negative tail limit.

## Complete Proof

Write
\[
F_{a,b}(x)=s\bigl(b\,\tau(ax)\bigr),
\]
where \(s(t)=1/(1+e^{-t})\), \(\tau(t)=\tanh t\), and \(a,b>0\). Fix \(0<\varepsilon<1/2\) and set
\[
L=\log\frac{1-\varepsilon}{\varepsilon}>0.
\]
Assume \(b>L\) and
\[
a\ge \frac{1}{2\varepsilon}\log\frac{b+L}{b-L}.
\]
The latter inequality is equivalent to
\[
\tanh(a\varepsilon)\ge \frac{L}{b},
\]
by the formula for \(\operatorname{arctanh}\). For every \(x\ge\varepsilon\), monotonicity of \(\tau\) gives \(b\tau(ax)\ge L\). Since \(s\) is increasing, \(F_{a,b}(x)\ge s(L)=1-\varepsilon\), hence
\[
\sup_{x\ge\varepsilon}|1-F_{a,b}(x)|\le\varepsilon.
\]
Because \(\tau\) is odd and \(s(-u)=1-s(u)\), we have \(F_{a,b}(-x)=1-F_{a,b}(x)\). Therefore for \(x\le-\varepsilon\), \(F_{a,b}(x)\le\varepsilon\), proving
\[
\sup_{x\le-\varepsilon}|F_{a,b}(x)|\le\varepsilon.
\]

Differentiating yields
\[
F'_{a,b}(x)=ab\,s\bigl(b\tau(ax)\bigr)\Bigl(1-s\bigl(b\tau(ax)\bigr)\Bigr)\bigl(1-\tau(ax)^2\bigr).
\]
For \(x\to+\infty\), \(\tau(ax)\to1\), and
\[
1-\tau(ax)^2=\frac{4e^{-2ax}}{(1+e^{-2ax})^2}.
\]
Consequently,
\[
\lim_{x\to+\infty}\frac{F'_{a,b}(x)}{e^{-2ax}}
=4ab\,s(b)\bigl(1-s(b)\bigr).
\]
For \(x\to-\infty\), the sigmoid product has the same limit because \(s(-u)(1-s(-u))=s(u)(1-s(u))\), while \(1-\tau(ax)^2\) is even. Thus
\[
\lim_{|x|\to\infty}\frac{F'_{a,b}(x)}{e^{-2a|x|}}
=4ab\,s(b)\bigl(1-s(b)\bigr).
\]
Finally, \(\tau(0)=0\), \(\tau'(0)=1\), and \(s(0)(1-s(0))=1/4\), so
\[
F'_{a,b}(0)=ab\,s(0)(1-s(0))=\frac{ab}{4}.
\]
The approximation threshold is controlled by the coupled conditions on \(a,b\), the tail decay exponent is \(2a\), and the central slope is proportional to the product \(ab\).
