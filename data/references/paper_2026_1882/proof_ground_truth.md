# Reference Proof

## Proof Structure

Represent the RKHS as the image of the feature-integral operator from $L^2(P)$. At each fixed input, differentiate the pointwise feature map in $L^2(P)$ using the Lipschitz envelope and dominated convergence. The exceptional null set may depend on that input. The resulting derivative lies in the orthogonal complement of the operator kernel, so the RKHS norm of its image equals its $L^2(P)$ norm. Prove the two derivative/Lipschitz inequalities on the open convex domain, and differentiate the kernel identity in operator norm to obtain the mixed-derivative formula.

## Complete Proof

Put $G=L^2(P)$ and let $\theta(x)=\phi(\cdot,x)\in G$. Cauchy–Schwarz makes $k(x,y)=\langle\theta(x),\theta(y)\rangle_G$ finite. It is symmetric, and for every finite collection of points and real coefficients,
\[
\sum_{i,j}c_ic_j k(x_i,x_j)=\left\|\sum_i c_i\theta(x_i)\right\|_G^2\ge0.
\]
Thus its RKHS is well defined.

### 1. RKHS representation and norm

Define
\[
(Su)(x)=\langle u,\theta(x)\rangle_G,
\qquad V=\overline{\operatorname{span}}\{\theta(x):x\in X\}.
\]
On finite linear combinations, the assignment
\[
\sum_i c_i\theta(x_i)\longmapsto\sum_i c_i k(x_i,\cdot)
\]
is well defined and isometric: the squared norms on both sides are $\sum_{i,j}c_ic_jk(x_i,x_j)$. It extends to an isometry from $V$ onto $H_k$, since the kernel sections have dense span in $H_k$. Its value at $v\in V$, evaluated at $x$, is $\langle v,\theta(x)\rangle_G$, so this isometry is $S|_V$.

Directly from its definition, $\ker S=V^\perp$. For $u=v+w$ with $v\in V$ and $w\in V^\perp$, we have $Su=Sv$ and
\[
\|Su\|_{H_k}=\|v\|_G\le\sqrt{\|v\|_G^2+\|w\|_G^2}=\|u\|_G.
\]
Consequently $S(G)=H_k$, $S$ is contractive, and
\[
\|Su\|_{H_k}=\inf_{w\in\ker S}\|u+w\|_G.
\]
Also $\Phi(x)=S\theta(x)$.

### 2. Differentiation in $L^2(P)$

Fix $x\in X$. Intersect the probability-one event on which the envelope inequality holds with a probability-one event on which $\phi(\omega,\cdot)$ is Frechet differentiable at this particular $x$. No event common to every input is needed.

Directional difference quotients, using openness of $X$, give
\[
|D\phi(\omega,x)[z]|\le F(\omega)\|z\|_E
\]
on this event, for every $z\in E$. The measurable derivative evaluations therefore define
\[
B_x:E\to G,\qquad B_xz=D\phi(\cdot,x)[z].
\]
Pointwise linearity on a full-measure event shows that $B_x$ is linear as a map into equivalence classes, and
\[
\|B_xz\|_G\le\|F\|_{L^2}\|z\|_E.
\]

For $x+h\in X$, set
\[
r_x(\omega;h)=\phi(\omega,x+h)-\phi(\omega,x)-D\phi(\omega,x)[h].
\]
For any sequence of nonzero $h_n\to0$ with $x+h_n\in X$, the measurable functions
\[
\beta_n(\omega)=\frac{|r_x(\omega;h_n)|^2}{\|h_n\|_E^2}
\]
converge almost surely to zero by differentiability at the fixed input $x$. Moreover,
\[
\beta_n\le4F^2\quad\text{almost surely}.
\]
The dominating function is integrable. The dominated convergence theorem, which states that almost-sure convergence under a common integrable absolute bound implies convergence of the integrals, yields $\int\beta_n\,dP\to0$. Because this holds for every such sequence and $E$ is a metric space,
\[
\frac{\|r_x(\cdot;h)\|_G}{\|h\|_E}\longrightarrow0.
\]
Thus $\theta$ is Frechet differentiable at $x$ with $D\theta(x)=B_x$. Contractivity of $S$ now gives
\[
\frac{\|\Phi(x+h)-\Phi(x)-SB_xh\|_{H_k}}{\|h\|_E}
\le\frac{\|r_x(\cdot;h)\|_G}{\|h\|_E}\longrightarrow0.
\]
Hence $D\Phi(x)=SB_x$ at every $x\in X$.

### 3. Exact derivative norm

For $u\in\ker S$, the scalar function $Su$ is identically zero. The preceding $L^2$ remainder estimate gives
\[
\frac{|(Su)(x+h)-(Su)(x)-\langle u,B_xh\rangle_G|}{\|h\|_E}
\le\|u\|_G\frac{\|r_x(\cdot;h)\|_G}{\|h\|_E}\longrightarrow0.
\]
Its derivative is therefore $z\mapsto\langle u,B_xz\rangle_G$, and this derivative is zero. Consequently $B_xz\in(\ker S)^\perp=V$. The isometry of $S$ on $V$ implies
\[
\|D\Phi(x)[z]\|_{H_k}=\|B_xz\|_G
=\left(\int_\Omega|D\phi(\omega,x)[z]|^2\,dP(\omega)\right)^{1/2}.
\]
In particular,
\[
M:=\sup_{x\in X}\|D\Phi(x)\|_{\mathrm{op}}
=\sup_{x\in X,\ \|z\|_E\le1}\|B_xz\|_G
\le\|F\|_{L^2}<\infty.
\]

### 4. Optimal Lipschitz constant

If $E=\{0\}$, then $X=\{0\}$, both derivatives have zero operator norm, and $\operatorname{Lip}(\Phi)=0$ by the stated convention. The mixed derivative below is also zero, so the result holds. Assume otherwise for the difference-quotient argument.

For $x,y\in X$, convexity keeps their segment in $X$. If $\Phi(y)=\Phi(x)$, the desired increment bound is immediate. Otherwise put
\[
e=\frac{\Phi(y)-\Phi(x)}{\|\Phi(y)-\Phi(x)\|_{H_k}},
\qquad g(t)=\langle\Phi(x+t(y-x)),e\rangle_{H_k}.
\]
This real function is continuous on $[0,1]$ and differentiable on $(0,1)$, and
\[
|g'(t)|\le M\|y-x\|_E.
\]
The scalar mean-value theorem gives
\[
\|\Phi(y)-\Phi(x)\|_{H_k}=|g(1)-g(0)|\le M\|y-x\|_E.
\]
This proves $\operatorname{Lip}(\Phi)\le M$ without any continuity assumption on the derivative.

Conversely, fix $x\in X$ and $z\ne0$. Openness permits $x+tz\in X$ for sufficiently small $t$, and
\[
\|D\Phi(x)[z]\|_{H_k}
=\lim_{t\to0}\left\|\frac{\Phi(x+tz)-\Phi(x)}{t}\right\|_{H_k}
\le\operatorname{Lip}(\Phi)\|z\|_E.
\]
The same inequality is immediate for $z=0$. Taking suprema gives $M\le\operatorname{Lip}(\Phi)$. Therefore
\[
\operatorname{Lip}(\Phi)
=\sup_{x\in X,\ \|z\|_E\le1}
\left(\int_\Omega|D\phi(\omega,x)[z]|^2\,dP(\omega)\right)^{1/2}.
\]

### 5. Iterated mixed Frechet derivative

Since $\theta$ is Frechet differentiable and the inner product is continuous,
\[
D_2k(x,y)[w]=\langle\theta(x),B_yw\rangle_G.
\]
For fixed $y$, the map $v\mapsto(w\mapsto\langle v,B_yw\rangle_G)$ is bounded linear from $G$ into the normed space of bounded linear functionals on $E$, with operator norm at most $\|B_y\|_{\mathrm{op}}$. More explicitly, the remainder in differentiating $x\mapsto D_2k(x,y)$ satisfies
\[
\sup_{\|w\|_E\le1}
\left|D_2k(x+h,y)[w]-D_2k(x,y)[w]-\langle B_xh,B_yw\rangle_G\right|
\le\|r_x(\cdot;h)\|_G\,\|B_y\|_{\mathrm{op}}.
\]
After division by $\|h\|_E$, the right-hand side tends to zero. Thus the iterated mixed derivative exists in operator norm and
\[
D_1D_2k(x,y)[z,w]=\langle B_xz,B_yw\rangle_G.
\]
Setting $y=x$ and $w=z$ yields
\[
D_1D_2k(x,x)[z,z]=\|B_xz\|_G^2
=\int_\Omega|D\phi(\omega,x)[z]|^2\,dP(\omega)\ge0.
\]
Substitution proves the final curvature formula.

All theorem-critical obligations are closed. The proof does not require joint measurability, a common differentiability event for all inputs, separability of $E$, continuity of the derivative, or a second derivative in either individual kernel argument.
