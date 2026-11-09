# Reference Proof

## Proof Structure

1. Restrict the divergence to unit-speed geodesics. Symmetry and the induced-metric normalization cancel the cubic Taylor coefficient, giving a local fourth-order comparison with squared geodesic distance.
2. Use compactness and strongly convex normal neighborhoods to make the comparison uniform on the manifold, then extend it to all pairs.
3. Analyze the normalized kernel integral in normal coordinates. Radial scaling and cancellation of odd terms give the second-order bias expansion; the quartic comparison controls replacement of the divergence by the quadratic radial model.
4. Apply Hoeffding's inequality to the empirical summands, use the bandwidth condition for summability, and invoke Borel-Cantelli. Combine the almost-sure empirical-to-mean limit with the bias expansion and the Laplacian product rule.

## Complete Proof

Let \(d=d_g\). Fix a unit-speed, length-minimizing geodesic segment \(\gamma\) in a sufficiently small normal neighborhood, and put
\[
F(s,t)=D(\gamma(s),\gamma(t)).
\]
The function \(F\) is smooth there, symmetric, nonnegative, and vanishes on the diagonal. Since \(\gamma\) has unit speed and \(g_p=\tfrac12\operatorname{Hess}_p(D(p,\cdot))\),
\[
\partial_t^2F(s,s)=2
\]
for every \(s\). Differentiating the diagonal identity and using symmetry gives
\(\partial_t^3F(s,s)=0\). Hence Taylor's theorem gives
\[
|D(\gamma(0),\gamma(t))-t^2|\le C_{\gamma}t^4
\]
for sufficiently small \(t\).

By compactness, finitely many strongly convex normal neighborhoods cover \(M\). On the associated compact subset of the unit tangent bundle, the relevant fourth derivatives of
\[
(q,v,t)\longmapsto D(q,\exp_q(tv))
\]
are uniformly bounded. Thus there are \(r_0,C_0>0\) such that
\[
 |D(p,q)-d(p,q)^2|\le C_0d(p,q)^4\qquad(d(p,q)\le r_0).
\]
On the compact set \(\{(p,q):d(p,q)\ge r_0\}\), continuity and boundedness of \(D\) and \(d^2\), together with \(d^4\ge r_0^4\), yield the same inequality after increasing the constant. This proves the first assertion.

For the integral calculation, define the normalized operator
\[
G_\varepsilon q(p)=\frac1{\varepsilon^{m/2}}\int_M h(D(p,y)/\varepsilon)q(y)\,dV_g(y).
\]
The decay assumptions make \(m_0\) and \(m_2\) finite. Fix a normal-ball radius smaller than the injectivity radius and the radius on which \(D\) is smooth. By compactness and positivity of \(D\) away from the diagonal, the contribution of its complement to \(G_\varepsilon q(p)\) is exponentially small, uniformly in \(p\).

Inside the normal ball, write \(y=\exp_p(v)\). The fourth-order comparison gives
\[
D(p,\exp_p(v))=\|v\|^2+O(\|v\|^4).
\]
Taylor-expand \(q(\exp_p(v))\), the Riemannian volume density, and \(h\), then scale \(v=\sqrt\varepsilon\,u\). Odd monomials integrate to zero by radial symmetry, and
\[
\int_{\mathbb R^m}u_i u_jh(\|u\|^2)\,du=m_2\delta_{ij}.
\]
The curvature and quartic-divergence terms multiply \(q(p)\) and can be collected into a bounded smooth function \(\omega\). Therefore, uniformly in \(p\),
\[
G_\varepsilon q(p)=m_0q(p)+\frac{\varepsilon m_2}{2}
\bigl(\omega(p)q(p)-\Delta_gq(p)\bigr)+R_\varepsilon(q,p),
\]
where \(|R_\varepsilon(q,p)|\le C\varepsilon^{3/2}\) for \(q\in C^3(M)\), and the remainder is \(O(\varepsilon^2)\) for \(q\in C^4(M)\). Here \(\Delta_g\) uses the stated nonnegative convention, so
\[
\Delta_g(ab)=a\Delta_gb+b\Delta_ga-2g(\nabla_ga,\nabla_gb).
\]

Let \(Y_1,\ldots,Y_N\) be the iid samples with density \(P\), and, for fixed \(x\), define
\[
Z_j=h(D(x,Y_j)/\varepsilon_N)\,[f(x)-f(Y_j)].
\]
These variables are iid and uniformly bounded. Hoeffding's inequality gives, for every fixed \(t>0\),
\[
\Pr\left(\left|\sum_{j=1}^NZ_j-N\mathbb EZ_1\right|>tN\varepsilon_N^{m/2+1}\right)
\le 2\exp\{-c_tN\varepsilon_N^{m+2}\}.
\]
The lower bandwidth bound makes the right-hand side summable in \(N\). Borel-Cantelli, followed by a countable sequence of \(t\downarrow0\), gives almost surely
\[
\frac{\mathcal L^{(\varepsilon_N,N)}f(x)-N\mathbb EZ_1}
{N\varepsilon_N^{m/2+1}}\longrightarrow0.
\]

By the normalized definition of \(G_\varepsilon\),
\[
\mathbb EZ_1
=\varepsilon_N^{m/2}\bigl[f(x)G_{\varepsilon_N}P(x)-G_{\varepsilon_N}(fP)(x)\bigr].
\]
Insert the preceding expansion for \(P\) and \(fP\). The \(m_0\) and \(\omega\) terms cancel, and the product rule gives
\[
\frac{\mathbb EZ_1}{\varepsilon_N^{m/2+1}}
\longrightarrow \frac{m_2}{2}\left[P(x)\Delta_gf(x)-2g_x(\nabla_gf(x),\nabla_gP(x))\right].
\]
Combining this deterministic limit with the almost-sure concentration proves the asserted convergence. If \(P\equiv1/\operatorname{vol}_g(M)\), its gradient vanishes and the limit reduces to
\[
\frac{m_2}{2\operatorname{vol}_g(M)}\Delta_gf(x).
\]
