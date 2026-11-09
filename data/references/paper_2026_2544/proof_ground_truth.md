# Reference Proof

## Proof Structure

1. Use the variational formula for log-sum-exp to establish convexity and positive homogeneity of the radial extension, and verify smoothness away from zero.
2. Establish the gauge-sublevel and support-gradient representations for positive differentiable sublinear functions.
3. Approximate a target body by a polytope and transfer a uniform log-sum-exp approximation to Hausdorff error in the support representation, retaining positivity.
4. Use an inner polytope, its polar representation, and reciprocal radial bounds for the gauge representation.

## Complete Proof

Let \(\Delta_m=\{q\in\mathbb R^m:q_i\ge0,\ \sum_iq_i=1\}\), and set \(S(q)=-\sum_iq_i\log q_i\), with \(0\log0=0\). The conjugate of \(f(z)=\log\sum_{i=1}^m e^{z_i}\) equals \(-S(q)\) on \(\Delta_m\) and is \(+\infty\) outside it. Since \(f\) is proper, closed, and convex, Fenchel--Moreau gives the variational representation
\[
 f(z)=\sup_{q\in\Delta_m}\{q\cdot z+S(q)\}.
\]
For \(A=W^\top\), this yields, for \(x\ne0\),
\[
 p_\theta(x)=\beta\sup_{q\in\Delta_m}
 \{(Wq)\cdot x+\|x\|S(q)\}.
\]
The same equality holds at \(x=0\), with both sides zero. For each \(q\in\Delta_m\), the expression inside braces, multiplied by \(\beta\), is convex in \(x\): it is linear plus a nonnegative multiple of the norm, since \(S(q)\ge0\) and \(\beta>0\). A supremum of convex functions is convex. Directly from the definition, \(p_\theta(tx)=t p_\theta(x)\) for \(t\ge0\). Convexity and positive homogeneity imply subadditivity, so \(p_\theta\) is sublinear. Smoothness off the origin follows from smoothness of log-sum-exp and of \(x\mapsto x/\|x\|\) there.

We record the two body representations used below. Let \(p\) be a finite, continuous, positive-on-the-sphere sublinear function. Compactness of the sphere gives constants \(0<a\le b<\infty\) with \(a\|x\|\le p(x)\le b\|x\|\). Its sublevel set \(G=\{y:p(y)\le1\}\) is closed, convex, bounded, and contains a neighborhood of zero. Positive homogeneity gives \(g_G=p\).

Now suppose also that \(p\) is differentiable away from zero. Define
\[
 C=\{y\in\mathbb R^d:y\cdot u\le p(u)\text{ for every }u\in\mathbb R^d\}.
\]
The sublinear support representation gives \(h_C=p\); equivalently this follows by representing a finite sublinear function as the support function of its dominated linear functionals. The bounds above imply that \(C\) is compact and contains a ball about zero, so \(C\in\mathcal K\).

For a unit vector \(u\), differentiability and convexity imply
\(p(v)\ge p(u)+\nabla p(u)\cdot(v-u)\). Euler's identity for differentiable positive homogeneous functions gives \(\nabla p(u)\cdot u=p(u)\), so \(\nabla p(u)\cdot v\le p(v)\) for every \(v\). Thus \(\nabla p(u)\in C\) and \(\nabla p(u)\cdot u=p(u)\); it is the unique point of the exposed face of \(C\) in direction \(u\). For uniqueness, any point of that face is a subgradient of \(p\) at \(u\), and differentiability makes that subgradient unique. Every boundary point of a compact convex body has a supporting direction, so this also shows that \(\partial C=\{\nabla p(u):\|u\|=1\}\). Since zero is interior to \(C\), every point of \(C\) lies on a segment from zero to a boundary point, and consequently
\[
 C=\{0\}\cup\{t\nabla p(u):\|u\|=1,\ 0<t\le1\}
  =\{0\}\cup\{\|x\|\nabla p(x):0<\|x\|\le1\}.
\]
The last equality uses the degree-zero homogeneity of the gradient of a differentiable degree-one homogeneous function. This proves that the support-gradient image is a convex body with support function \(p\).

Fix \(K\in\mathcal K\) and \(\varepsilon>0\). Set \(r=\min_{\|u\|=1}h_K(u)>0\), which is positive since zero is interior to \(K\).

For the support representation, choose \(0<\delta<\min\{\varepsilon/3,r/2\}\). The standard polytope-approximation theorem for compact convex bodies gives a polytope \(P=\operatorname{conv}(w_1,\ldots,w_m)\) with \(d_H(K,P)<\delta\). Both are nonempty compact convex sets, so the support-function/Hausdorff identity gives \(\|h_K-h_P\|_{C(S^{d-1})}=d_H(K,P)<\delta\). In particular \(h_P(u)>r-\delta>0\) on the sphere. Choose \(\beta>0\) and columns of \(W\) equal to \(\beta^{-1}w_i\). For unit \(u\),
\[
 p_\theta(u)=\beta\log\sum_i\exp((w_i\cdot u)/\beta),\qquad
 0\le p_\theta(u)-h_P(u)\le\beta\log m.
\]
Take \(\beta\) small enough that \(\beta\log m<\varepsilon/3\) (when \(m=1\), the error is zero). Then \(p_\theta\) is positive on the sphere. The support-gradient representation just proved applies, and its support function is \(p_\theta\). Hence
\[
 d_H(K,\Omega_\theta^s)
 \le d_H(K,P)+d_H(P,\Omega_\theta^s)
 =d_H(K,P)+\|h_P-p_\theta\|_{C(S^{d-1})}
 <\delta+\varepsilon/3<\varepsilon.
\]

For the gauge representation, choose \(s>0\) with \(sB\subset K\). A finite \(\delta'\)-net of compact \(K\), together with the points \(\pm s e_j\) for a sufficiently small positive \(s\), has convex hull \(P\subset K\) containing a neighborhood of zero and satisfying \(d_H(K,P)<\varepsilon/3\): every point of \(K\) is within \(\delta'<\varepsilon/3\) of one of the net points in \(P\), and \(P\subset K\). Thus \(P\) is an inner polytope with zero in its interior. Its polar \(P^\circ=\{a:a\cdot y\le1\text{ for every }y\in P\}\) is a compact polytope. If \(a_1,\ldots,a_m\) are its vertices, the polar representation gives
\[
 P=\{y:a_i\cdot y\le1\text{ for all }i\},\qquad
 g_P(u)=\max_i a_i\cdot u.
\]
These facts apply because \(P\) is a full-dimensional polytope containing zero in its interior.

Choose \(\beta>0\) and columns of \(W\) equal to \(\beta^{-1}a_i\). The log-sum-exp estimate gives \(\|p_\theta-g_P\|_{C(S^{d-1})}\le\beta\log m\). Put \(\alpha=\min_{S^{d-1}}g_P>0\). Choose \(\eta>0\) so small that \(\eta<\alpha/2\) and \(2\eta/\alpha^2<\varepsilon/3\), and then choose \(\beta\) so that \(\beta\log m<\eta\) (if \(m=1\), the approximation error is zero). It follows that \(p_\theta\ge\alpha/2\) on the sphere. The gauge sublevel set is therefore in \(\mathcal K\), and homogeneity gives its radial function \(\rho_{\Omega_\theta^g}(u)=1/p_\theta(u)\); likewise \(\rho_P(u)=1/g_P(u)\). Thus
\[
 |\rho_{\Omega_\theta^g}(u)-\rho_P(u)|
 =\left|\frac1{p_\theta(u)}-\frac1{g_P(u)}\right|
 \le\frac{2\eta}{\alpha^2}.
\]
For any two convex bodies containing zero in their interiors, their Hausdorff distance is at most the supremum of the absolute difference of their radial functions: for a point outside the other body, the point on the same ray at that body's radial boundary gives distance no greater than the radial difference; points already inside have distance zero. Applying this in both directions yields \(d_H(P,\Omega_\theta^g)\le2\eta/\alpha^2<\varepsilon/3\). Consequently
\[
 d_H(K,\Omega_\theta^g)\le d_H(K,P)+d_H(P,\Omega_\theta^g)<2\varepsilon/3<\varepsilon.
\]
Both density claims follow.
