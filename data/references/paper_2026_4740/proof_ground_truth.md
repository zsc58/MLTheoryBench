# Reference Proof

## Proof Structure

1. Derive the exponential-path lower bound directly from DR-submodularity and nonnegativity, including the zero-path case.
2. Establish that the integral potential is finite on K and compute its gradient.
3. Bound the comparator pairing using the DR increment inequality and the trajectory pairing using integration by parts.
4. Add the bounds to obtain the stated linearizability inequality.

## Complete Proof

Products and exponentials are coordinatewise. Write u\oplus v=u+(1-u)\odot v and h_z(x)=1-e^{-zx}. If x\in K and 0\le z\le1, then 0\le h_z(x)\le x, so h_z(x)\in K.

We first prove the exponential-path bound rather than assuming the paper-specific auxiliary result. Fix x,y\in K, put m=\max_i x_i, and define w(s)=h_s(x)\oplus y=1-(1-y)\odot e^{-sx} for 0\le s\le1. These points lie in the cube, where f is nonnegative and DR-submodular. If m=0, then x=0 and w(s)=y, so f(w(s))=f(y). If m>0, set v(s)=x\odot(1-w(s))/m. Both v(s) and w(s)+v(s) belong to the cube. DR-submodularity implies concavity along every nonnegative direction: f(u+v)\le f(u)+\langle\nabla f(u),v\rangle whenever u,v\ge0 and u+v lies in the cube. Consequently,
\[
0\le f(w(s)+v(s))\le f(w(s))+\frac1m\langle\nabla f(w(s)),x\odot(1-w(s))\rangle
=f(w(s))+\frac1m\frac{d}{ds}f(w(s)).
\]
Thus \(\frac{d}{ds}(e^{ms}f(w(s)))\ge0\), which gives, at s=z,
\[
f(h_z(x)\oplus y)\ge e^{-zm}f(y)\ge e^{-z}f(y). \tag{1}
\]
The last inequality uses m\le1 and f(y)\ge0. This argument closes the lower-bound obligation without invoking the inherited, nonstandard exponential-path inequality.

Put \(\beta=1-e^{-1}\) and define
\[
F(x)=\int_0^1\frac{e^{z-1}}{\beta z}\bigl(f(h_z(x))-f(0)\bigr)\,dz.
\]
For x\in K, the segment from 0 to h_z(x) lies in K. The source's bounded-gradient assumption on K and \(\|h_z(x)\|\le z\|x\|\) imply \(|f(h_z(x))-f(0)|\le M_1z\|x\|\). Hence the apparent singularity at z=0 is removable and F is finite, including at x=0. The Lipschitz continuity of \(\nabla f\) on K justifies differentiation along feasible directions and gives the canonical gradient field
\[
\nabla F(x)=\int_0^1\frac{e^{z-1}}{\beta}\,\nabla f(h_z(x))\odot e^{-zx}\,dz. \tag{2}
\]
This formula also specifies the gradient field at boundary or lower-dimensional points of K.

Fix x,y\in K. Applying concavity along the nonnegative direction \(e^{-zx}\odot y\) at \(h_z(x)\) is legitimate because their sum is \(h_z(x)\oplus y\in[0,1]^d\). Equations (1) and (2) therefore give
\[
\begin{aligned}
\beta\langle\nabla F(x),y\rangle
&\ge\int_0^1 e^{z-1}\bigl(f(h_z(x)\oplus y)-f(h_z(x))\bigr)\,dz\\
&\ge e^{-1}f(y)-\int_0^1e^{z-1}f(h_z(x))\,dz. \tag{3}
\end{aligned}
\]
On the other hand, \(\frac{d}{dz}f(h_z(x))=\langle\nabla f(h_z(x)),x\odot e^{-zx}\rangle\). Integration by parts yields
\[
\begin{aligned}
\beta\langle\nabla F(x),-x\rangle
&=-\int_0^1e^{z-1}\frac{d}{dz}f(h_z(x))\,dz\\
&=-f(h(x))+e^{-1}f(0)+\int_0^1e^{z-1}f(h_z(x))\,dz\\
&\ge-f(h(x))+\int_0^1e^{z-1}f(h_z(x))\,dz. \tag{4}
\end{aligned}
\]
Adding (3) and (4) cancels the integral terms. Thus, for all x,y\in K,
\[
\frac1e f(y)-f(h(x))\le(1-e^{-1})\langle\nabla F(x),y-x\rangle.
\]
Since h(x)\le x coordinatewise, h maps K into K. Taking \(g_f=\nabla F\), \(\alpha=1/e\), and \(\beta=1-e^{-1}>0\) proves the claim.
