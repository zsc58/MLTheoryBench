# Reference Proof

## Contract and Proof Obligations

The claim concerns the globally defined population vector field and its necessary spatial-gradient condition. A spatial potential is not being asserted to suffice for the existence of a scalar distributional energy or a Wasserstein gradient flow. In the smooth pointwise setting, the source's velocity formula is the negative spatial gradient of a first variation; its sign can be absorbed into the scalar potential.

The theorem-critical obligations are:

1. Establish finiteness, positivity, and the regularity needed to differentiate the displayed quantities, without assuming that the weighted measures have finite total mass.
2. Relate the defining destination integrals to the functions Z and Phi.
3. Derive the alignment condition from the existence of a C2 scalar potential.
4. Evaluate the atomic configuration and exhibit a nonzero violation.

All four obligations are closed below. The positive-density assumptions used for the source's KL calculations and the finite weighted-mass assumption used for its separate consistency theorem are not hypotheses of this pointwise obstruction.

## Complete Proof

### 1. Well-definedness and regularity

Because p and q are probability measures and the Gaussian kernel is strictly positive and at most one,
\[
0<p_\tau(x)\le1,\qquad 0<q_\tau(x)\le1
\]
for every x.

Choose R>0 such that
\[
m=q(\{z:\|z\|\le R\})>0.
\]
Such an R exists because these balls exhaust the space. For every y,
\[
q_\tau(y)\ge m\exp\!\left(-\frac{(\|y\|+R)^2}{\tau}\right).
\]
Consequently, for \(\|x\|\le M\),
\[
\frac{k(x,y)}{\sqrt{q_\tau(y)}}
\le m^{-1/2}\exp\!\left(
-\frac{\|y\|^2}{2\tau}
+\frac{(2M+R)\|y\|}{\tau}
+\frac{R^2}{2\tau}
\right).
\]
The right-hand side remains bounded as a function of y after multiplication by any fixed polynomial in \(\|y\|\). Every spatial derivative of the Gaussian kernel is the kernel multiplied by a polynomial in x-y. Therefore, for every derivative order and every bounded set of x, the corresponding derivative of
\[
f(x,y)=\frac{k(x,y)}{\sqrt{q_\tau(y)}}
\]
is uniformly bounded in y. The same is true after multiplication by any component of y.

These bounds establish absolute integrability against both p and q. They also justify differentiating the integrals: Taylor's theorem in a coordinate direction bounds the error between a difference quotient and the corresponding derivative by a constant times the increment, uniformly in y, using the next derivative bound on a slightly larger bounded set of x. Integrating this error against a probability measure preserves that bound. Repeating the argument gives derivatives of every order, and the next derivative bound also gives their continuity.

It follows that
\[
h_p=k*\widetilde p,\qquad h_q=k*\widetilde q
\]
are finite, strictly positive, and smooth on all of \(\mathbb R^d\), and their first-moment destination integrals are absolutely convergent. The unweighted convolutions p_tau and q_tau are smooth as well, by the same argument without the denominator. The weighted measures are locally finite, since q_tau is continuous and strictly positive on compact sets. Their total masses need not be finite.

Thus the row integrals, cross-weighted destination integrals, Z, Phi, and V are well defined and smooth everywhere. This supplies all regularity required below, without adding a moment assumption.

### 2. Representation of the velocity

From the definitions of the row integrals,
\[
s^+(x)=\frac{h_p(x)}{\sqrt{p_\tau(x)}},\qquad
s^-(x)=\frac{h_q(x)}{\sqrt{q_\tau(x)}}.
\]
For either \(\mu=\widetilde p\) or \(\mu=\widetilde q\), the differentiation justified above gives
\[
\nabla(k*\mu)(x)
=\frac{2}{\tau}\left(\int y\,k(x,y)\,d\mu(y)-x(k*\mu)(x)\right).
\]
Since the convolution is positive,
\[
\int y\,k(x,y)\,d\mu(y)
=(k*\mu)(x)\left[x+\frac{\tau}{2}\nabla\log(k*\mu)(x)\right].
\]
Using the definition of \(\widetilde p\), the first destination integral in V becomes
\[
\begin{aligned}
\int W^+(x,y)y\,dp(y)
&=\frac{s^-(x)}{\sqrt{p_\tau(x)}}\int yk(x,y)\,d\widetilde p(y)\\
&=Z(x)\left[x+\frac{\tau}{2}\nabla\log h_p(x)\right].
\end{aligned}
\]
Likewise,
\[
\begin{aligned}
\int W^-(x,y)y\,dq(y)
&=\frac{s^+(x)}{\sqrt{q_\tau(x)}}\int yk(x,y)\,d\widetilde q(y)\\
&=Z(x)\left[x+\frac{\tau}{2}\nabla\log h_q(x)\right].
\end{aligned}
\]
Subtracting cancels the two Z(x)x terms and yields
\[
V(x)=Z(x)\nabla\Phi(x).
\]

### 3. Necessary alignment condition

Suppose \(V=\nabla U\) on all of \(\mathbb R^d\) for some \(U\in C^2(\mathbb R^d)\). Equality of the mixed partial derivatives of a C2 scalar function gives
\[
\partial_jV_i=\partial_iV_j.
\]
This is the necessary direction of the spatial integrability criterion; no converse concerning distributional energies is used.

Since \(V_i=Z\partial_i\Phi\),
\[
\partial_jV_i=(\partial_jZ)(\partial_i\Phi)+Z\partial_{ji}\Phi,
\]
while
\[
\partial_iV_j=(\partial_iZ)(\partial_j\Phi)+Z\partial_{ij}\Phi.
\]
The regularity proved in the first part gives \(\Phi\in C^2\), so its mixed derivatives agree. Cancellation therefore gives
\[
(\partial_iZ)(\partial_j\Phi)=(\partial_jZ)(\partial_i\Phi)
\]
for every x and every i,j. No division by either gradient is used, so the argument also covers points where one or both gradients vanish.

### 4. Atomic configuration

Let
\[
a=(-1,0),\qquad b=(1,0),\qquad p=\delta_b,\qquad q=\delta_a.
\]
Then
\[
p_\tau(x)=k(x,b),\qquad q_\tau(x)=k(x,a),
\]
and
\[
q_\tau(b)=e^{-4/\tau},\qquad q_\tau(a)=1.
\]
Consequently,
\[
\widetilde p=e^{2/\tau}\delta_b,\qquad \widetilde q=\delta_a,
\]
so
\[
h_p(x)=e^{2/\tau}k(x,b),\qquad h_q(x)=k(x,a).
\]
Because \(\|x-a\|^2-\|x-b\|^2=4x_1\),
\[
\Phi(x)=\frac{\tau}{2}\left[\frac{2}{\tau}+\frac{4x_1}{\tau}\right]=1+2x_1.
\]
The row-integral formulas also give
\[
Z(x)=e^{2/\tau}\sqrt{k(x,b)k(x,a)}
=\exp\!\left(\frac{1-x_1^2-x_2^2}{\tau}\right).
\]
Thus
\[
\nabla\Phi(0,1)=(2,0),\qquad
\nabla Z(0,1)=Z(0,1)(0,-2/\tau),\qquad Z(0,1)=1.
\]
For \((i,j)=(1,2)\),
\[
\partial_1Z(0,1)\,\partial_2\Phi(0,1)=0,
\]
but
\[
\partial_2Z(0,1)\,\partial_1\Phi(0,1)
=-\frac{4}{\tau}Z(0,1)=-\frac4\tau\ne0.
\]
The alignment condition fails for every \(\tau>0\). Therefore no global C2 scalar-potential representation exists. In particular, the field fails the necessary spatial-gradient condition for a smooth pointwise Wasserstein-gradient-flow velocity.
