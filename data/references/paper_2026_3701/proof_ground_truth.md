# Reference Proof

## Proof Structure

Fix the realized learned operator; all expectations below average only over a fresh test input. For each unseen test-grid point, compare the prediction and truth with their values at its assigned nearest training-grid point. Hölder continuity controls both spatial increments. An elementary square inequality converts this comparison into a bound involving the training-point squared error. Grouping by assignments and adding the observed-point contribution gives the stated coefficients. Integrating proves the bound, and taking a fixed-grid limit proves the consequence.

## Complete Proof

Write $m=|Y_{\mathrm{train}}|$, $M=|Y_{\mathrm{test}}|$, and $r=m/M$. These quantities satisfy $1\le m\le M$ and $0<r\le1$. For $v\in V$, set
\[
e_y(v)=|\widehat F_n(v)(y)-G(v)(y)|^2.
\]
These functions are nonnegative and $\mu$-measurable by the setup.

For an unseen point $y\in Y_{\mathrm{test}}\setminus Y_{\mathrm{train}}$, let $z=\operatorname{nn}(y)$. Insert the two output values at $z$:
\[
\widehat F_n(v)(y)-G(v)(y)
=[\widehat F_n(v)(y)-\widehat F_n(v)(z)]
+[\widehat F_n(v)(z)-G(v)(z)]
+[G(v)(z)-G(v)(y)].
\]
For real numbers $a,b,d$, the inequalities
\[
(a+b+d)^2\le2b^2+2(a+d)^2\le2b^2+4(a^2+d^2)
\]
follow from $(s+t)^2\le2s^2+2t^2$. Applying these inequalities and the two Hölder bounds yields
\[
e_y(v)\le2e_z(v)+8c^2\|y-z\|_2^{2\alpha}
\le2e_z(v)+8c^2\beta^{2\alpha}.
\]

For each $z\in Y_{\mathrm{train}}$, define its total assignment count and unseen assignment count by
\[
a_z=\sum_{y\in Y_{\mathrm{test}}}{\bf1}\{\operatorname{nn}(y)=z\},
\qquad
k_z=\sum_{y\in Y_{\mathrm{test}}\setminus Y_{\mathrm{train}}}{\bf1}\{\operatorname{nn}(y)=z\}.
\]
A training point is uniquely its own nearest training point: its distance to itself is zero and its distance to every other training point is positive. Thus $a_z=1+k_z$ for every $z$, and
\[
\max_z k_z=\max_z a_z-1=\nu-1.
\]
In particular, $\nu\ge1$. The prescribed tie-breaking rule supplies the assignment used here; the counting argument needs no further property of its optimization.

Summing the unseen-point bounds and grouping by their assigned training points gives
\[
\begin{aligned}
\sum_{y\in Y_{\mathrm{test}}\setminus Y_{\mathrm{train}}}e_y(v)
&\le2\sum_{z\in Y_{\mathrm{train}}}k_z e_z(v)
 +(M-m)8c^2\beta^{2\alpha}\\
&\le2(\nu-1)\sum_{z\in Y_{\mathrm{train}}}e_z(v)
 +(M-m)8c^2\beta^{2\alpha}.
\end{aligned}
\]
Adding the exact contribution from the training points and dividing by $M$ yields
\[
\frac1M\sum_{y\in Y_{\mathrm{test}}}e_y(v)
\le r(2\nu-1)\frac1m\sum_{z\in Y_{\mathrm{train}}}e_z(v)
 +(1-r)8c^2\beta^{2\alpha}.
\]
Integrating this measurable nonnegative pointwise inequality over $v\sim\mu$ proves
\[
E_\mu(\widehat F_n,G,Y_{\mathrm{test}})
\le r(2\nu-1)E_\mu(\widehat F_n,G,Y_{\mathrm{train}})
 +(1-r)8c^2\beta^{2\alpha}.
\]
The integration is valid for extended nonnegative expectations. The multiplier $r(2\nu-1)$ is strictly positive, so an infinite training-grid risk causes no undefined product. If the training-grid risk is finite, the displayed bound also proves finiteness of the test-grid risk.

For the limiting consequence, hold the grids, $\alpha$, and the common bound $c$ fixed across $n$. If the training-grid risk tends to zero, then the finite fixed coefficient $r(2\nu-1)$ times that risk tends to zero. Hence
\[
\limsup_{n\to\infty}E_\mu(\widehat F_n,G,Y_{\mathrm{test}})
\le(1-r)8c^2\beta^{2\alpha}.
\]
Since $0\le1-r\le1$, the coverage term is at most $8c^2\beta^{2\alpha}$. For $c>0$ and any $\varepsilon>0$, taking
\[
\beta\le\left(\frac{\varepsilon}{8c^2}\right)^{1/(2\alpha)}
\]
makes that term at most $\varepsilon$. If $c=0$, the coverage term is already zero. This conclusion concerns the coverage term and fixed-grid training-error convergence; it does not assert a uniform sample threshold over varying training grids without a uniform convergence premise.

Finally, if the two grids coincide, then $\nu=1$, $r=1$, and $\beta=0$, so the bound is equality. For finite nested sets, $\beta=0$ also implies that the grids coincide. Singleton training grids and the endpoint $\alpha=1$ are covered by the same argument.
