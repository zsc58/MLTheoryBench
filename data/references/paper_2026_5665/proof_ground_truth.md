# Reference Proof

## Proof Structure

First force a directional constraint on each one-coordinate section of the aggregation rule by realizing an arbitrary two-point gradient change with a convex rank-one quadratic. This constraint makes every section affine with a nonnegative scalar slope; compatibility among sections makes those slopes global constants. The converse follows by summing the component inequalities. The same construction, scaled to have smoothness constant \(L\), proves the co-coercivity necessity.

## Complete Proof

Write \(\Delta g_i=g_i(x)-g_i(y)\).

Assume first that statement 1 holds. Fix an index \(i\) and fix all inputs other than the \(i\)-th one. Let \(h:\mathbb R^d\to\mathbb R^d\) be the resulting one-coordinate section of \(A\). We claim that, for all \(u,v\),
\[
h(u)-h(v)\in \{\lambda(u-v):\lambda\geq 0\}. \tag{1}
\]
Suppose otherwise. Put \(a=u-v\) and \(b=h(u)-h(v)\). Then \(a\ne0\), and elementary separation of the ray \(\{\lambda a:\lambda\geq0\}\) gives a vector \(z\) such that
\[
\langle z,a\rangle>0,\qquad \langle z,b\rangle<0.
\]
Let
\[
H=\frac{aa^{\mathsf T}}{\langle z,a\rangle},\qquad
q(w)=\tfrac12 w^{\mathsf T}Hw+\langle v,w\rangle.
\]
The matrix \(H\) is positive semidefinite, so \(q\) is convex, and \(\nabla q(0)=v\) and \(\nabla q(z)=u\). For every other coordinate choose a linear convex function having the previously fixed gradient. The induced field has difference \(b\) between \(z\) and \(0\), whereas monotonicity would require \(\langle z,b\rangle\geq0\), a contradiction. Thus (1) holds.

We next show that every such section is affine with a constant nonnegative scalar slope. For distinct points \(p,q,r\) with \(p-q\) and \(q-r\) linearly independent, apply (1) to the three pairs and use
\[
h(p)-h(r)=[h(p)-h(q)]+[h(q)-h(r)].
\]
Comparing the coefficients of the two independent vectors shows that the three corresponding multipliers in (1) are equal. Since \(d>1\), auxiliary points outside any prescribed affine line connect arbitrary distinct pairs by such non-collinear triangles. Hence there is one \(\alpha\geq0\) such that \(h(u)-h(v)=\alpha(u-v)\) for every \(u,v\), and therefore \(h(u)=\alpha u+c\).

Applying this conclusion to every coordinate section gives, initially,
\[
A(x_1,\ldots,x_n)=\alpha_i(x_{-i})x_i+B_i(x_{-i}) \tag{2}
\]
for each \(i\), where \(\alpha_i(x_{-i})\geq0\). We show that \(\alpha_i\) is independent of the other inputs. Fix \(j\ne i\) and fix all remaining coordinates. Compare (2) at two \(j\)-th inputs \(s,s'\), and then take the difference of the resulting identities at two \(i\)-th inputs \(r,r'\). Since the \(j\)-th section is also affine, this yields
\[
[\alpha_i(s)-\alpha_i(s')](r-r')
=[\alpha_j(r)-\alpha_j(r')](s-s').
\]
Choose \(r-r'\) linearly independent of \(s-s'\). Both coefficients must vanish, so \(\alpha_i(s)=\alpha_i(s')\). Repeating for every \(j\ne i\) shows that \(\alpha_i\) is a constant, still denoted \(\alpha_i\). This also covers \(n=1\) directly. Thus
\[
R(x_1,\ldots,x_n):=A(x_1,\ldots,x_n)-\sum_{i=1}^n\alpha_i x_i
\]
has zero difference whenever any one coordinate is varied. Varying coordinates one at a time shows that \(R\) is constant, say \(c\). We have proved statement 3.

Conversely, suppose statement 3 holds. For convex differentiable \(f_i\), each gradient is monotone, and hence
\[
\langle x-y,G_f(x)-G_f(y)\rangle
=\sum_{i=1}^n\alpha_i\langle x-y,\Delta g_i\rangle\geq0.
\]
Therefore statement 1 holds.

Now assume statement 2. If statement 3 failed, the section analysis above implies that there would be a coordinate section and points \(u,v\) for which (1) fails. Choose a separating vector \(z_0\) as above, and rescale it to a vector \(z\) satisfying
\[
\langle z,a\rangle=\frac{\|a\|^2}{L}.
\]
The matrix
\[
H=\frac{aa^{\mathsf T}}{\langle z,a\rangle}
=\frac{Laa^{\mathsf T}}{\|a\|^2}
\]
is positive semidefinite and has operator norm \(L\). The associated quadratic \(q\) is therefore convex and \(L\)-smooth; the other required functions may again be taken linear, hence \(L\)-smooth. The induced field has output difference \(b\) between \(z\) and \(0\), with \(\langle z,b\rangle<0\). This contradicts co-coercivity, which would imply
\[
\langle z,b\rangle\geq\beta\|b\|^2\geq0
\]
for some \(\beta>0\). Hence statement 2 implies statement 3.

Finally suppose statement 3 holds and every \(f_i\) is convex and \(L\)-smooth. The standard co-coercivity inequality for such a gradient, whose hypotheses hold here, gives
\[
\langle x-y,\Delta g_i\rangle\geq \frac1L\|\Delta g_i\|^2.
\]
Let \(s=\sum_i\alpha_i\). If \(s=0\), then \(G_f\equiv c\), so it is co-coercive. If \(s>0\), weighted Cauchy--Schwarz gives
\[
\left\|\sum_i\alpha_i\Delta g_i\right\|^2
\leq s\sum_i\alpha_i\|\Delta g_i\|^2.
\]
Consequently,
\[
\langle x-y,G_f(x)-G_f(y)\rangle
\geq \frac1L\sum_i\alpha_i\|\Delta g_i\|^2
\geq \frac1{Ls}\|G_f(x)-G_f(y)\|^2.
\]
Thus \(G_f\) is co-coercive, proving statement 2.

If \(A\) is idempotent, substituting \((z,\ldots,z)\) into statement 3 and using \(A(z,\ldots,z)=z\) for every \(z\) gives \(\sum_i\alpha_i=1\) and \(c=0\). Permutation invariance makes all \(\alpha_i\) equal, so \(\alpha_i=1/n\). Hence \(A\) is the arithmetic mean.
