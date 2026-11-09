# Reference Proof

## Proof Structure

Fix a coordinate and collect every term in the energy that depends on it. The log-amplitude interaction produces the power \(2\alpha_d-2\), the diagonal quadratic term produces Gaussian radial decay, and the remaining complex terms form one linear field. Completing the square identifies the normalized planar conditional. Conditioning on the radius gives the von Mises law, while polar integration with the Jacobian gives the radial density.

## Complete Proof

Fix \(d\) and \(x_{-d}\), and write \(x_d=r e^{i\theta}\). We first collect the terms in \(-\mathcal E(x)\) that depend on \(x_d\).

Because \(Q\) is Hermitian, \(Q_{dd}=-2\beta_d\), and
\[
g_d=Q_{-d,d}^{H}x_{-d}+h_d,
\]
the complex quadratic and linear terms contribute
\[
-\beta_d|x_d|^2+\operatorname{Re}(\overline{g_d}x_d).
\]
Indeed, the factor \(1/2\) in the quadratic form combines the two conjugate cross terms into one real part.

Let \(\ell=\log|x|\). Since \(A\) is symmetric with zero diagonal, its terms involving \(\ell_d=\log r\) contribute
\[
\bigl(A_{-d,d}^{T}\log|x_{-d}|+\eta_d\bigr)\log r
=(2\alpha_d-2)\log r.
\]
All remaining terms are constant in \(x_d\). Hence the coordinate-conditional kernel with respect to planar Lebesgue measure is
\[
|x_d|^{2\alpha_d-2}
\exp\!\left(-\beta_d|x_d|^2+
\operatorname{Re}(\overline{g_d}x_d)\right).
\tag{1}
\]
The assumptions \(\beta_d>0\) and \(\alpha_d>0\) ensure integrability at infinity and at the origin, respectively.

Set
\[
m_d=\frac{g_d}{2\beta_d},\qquad s_d^2=\frac1{\beta_d}.
\]
Completing the square gives
\[
-\beta_d|x_d|^2+
\operatorname{Re}(\overline{g_d}x_d)
=-\frac{|x_d-m_d|^2}{s_d^2}
+\frac{|g_d|^2}{4\beta_d}.
\]
The last term is independent of \(x_d\), so (1) has the kernel of \(q_{\alpha_d,m_d,s_d^2}\).

It remains to verify the stated normalization. Put \(\nu=|m_d|\) and rotate polar coordinates so that \(m_d\) has phase zero. Using
\[
\int_{-\pi}^{\pi}e^{t\cos\vartheta}\,d\vartheta=2\pi I_0(t),
\]
we obtain
\[
\begin{aligned}
&\int_{\mathbb C}|z|^{2\alpha_d-2}
 e^{-|z-m_d|^2/s_d^2}\,dz\\
&=2\pi e^{-\nu^2/s_d^2}
  \int_0^\infty r^{2\alpha_d-1}e^{-r^2/s_d^2}
  I_0\!\left(\frac{2\nu r}{s_d^2}\right)dr.
\end{aligned}
\]
Expanding \(I_0\) in its nonnegative power series and integrating term by term gives
\[
\int_0^\infty r^{2\alpha_d-1}e^{-r^2/s_d^2}
 I_0\!\left(\frac{2\nu r}{s_d^2}\right)dr
=\frac{(s_d^2)^{\alpha_d}\Gamma(\alpha_d)}2
{}_1F_1\!\left(\alpha_d;1;\frac{\nu^2}{s_d^2}\right).
\]
Kummer's transformation and
\(L_{\alpha_d-1}(t)={}_1F_1(1-\alpha_d;1;t)\) imply
\[
{}_1F_1\!\left(\alpha_d;1;\frac{\nu^2}{s_d^2}\right)
=e^{\nu^2/s_d^2}L_{\alpha_d-1}\!\left(-\frac{\nu^2}{s_d^2}\right).
\]
Thus the planar integral is
\[
\pi(s_d^2)^{\alpha_d}\Gamma(\alpha_d)
L_{\alpha_d-1}\!\left(-\frac{|m_d|^2}{s_d^2}\right),
\]
which proves
\[
x_d\mid x_{-d}\sim q_{\alpha_d,m_d,s_d^2}.
\]

For the phase conditional, write \(g_d=a_de^{i\phi_d}\) and \(x_d=re^{i\theta}\). For fixed \(r\), all phase-independent factors in (1) cancel, leaving
\[
p(\theta\mid R_d=r,x_{-d})
=\frac{e^{a_dr\cos(\theta-\phi_d)}}{2\pi I_0(a_dr)}.
\]
This is the claimed von Mises density. When \(a_d=0\), it is uniform, so the arbitrary choice of \(\phi_d\) is immaterial.

Finally, the density of \(R_d\) with respect to \(dr\) is obtained from the normalized planar density using the polar Jacobian \(r\):
\[
p(r\mid x_{-d})
=r\int_{-\pi}^{\pi}q_{\alpha_d,m_d,s_d^2}(re^{i\theta})\,d\theta.
\]
Writing \(\nu_d=|m_d|\) and applying the angular Bessel identity gives
\[
p(r\mid x_{-d})=
\frac{2r^{2\alpha_d-1}e^{-(r^2+\nu_d^2)/s_d^2}
I_0(2\nu_dr/s_d^2)}
{(s_d^2)^{\alpha_d}\Gamma(\alpha_d)
L_{\alpha_d-1}(-\nu_d^2/s_d^2)},
\qquad r>0.
\]
This proves the asserted magnitude formula and completes the proof.
