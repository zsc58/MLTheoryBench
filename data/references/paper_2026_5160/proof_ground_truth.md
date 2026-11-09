# Reference Proof

## Proof Structure

Bound each of the two objective terms above by zero, show that the uniform correct-set policy attains both bounds, and use the equality conditions to prove uniqueness.

## Complete Proof

Write \(Z=p(S)\). Every feasible policy satisfies \(0<Z\leq 1\), so
\[
\log Z\leq 0,
\]
with equality if and only if \(Z=1\). Also, by nonnegativity of KL divergence,
\[
-\tau D_{\mathrm{KL}}(u\|q)\leq 0,
\]
and, since \(\tau>0\), equality holds if and only if \(q=u\). Consequently,
\[
F(p)\leq 0
\]
for every feasible \(p\).

The policy \(p^\star\) is feasible. It has \(p^\star(S)=1\), and its conditional distribution on \(S\) is \(q^\star=u\). Hence both terms in \(F(p^\star)\) vanish and \(F(p^\star)=0\). Thus \(p^\star\) is a maximizer.

Now let \(p\) be any maximizer. Since the maximum value is \(0\), both nonpositive terms in the display defining \(F(p)\) must equal zero. Thus \(Z=1\) and \(q=u\). For every \(y\in S\),
\[
p(y)=Zq(y)=1\cdot \frac{1}{|S|}=\frac{1}{|S|}.
\]
Moreover, \(p(S)=1\) implies that \(p(y)=0\) for every \(y\notin S\). Therefore \(p=p^\star\), proving that the maximizer is unique.
