# Reference Proof

## Proof Structure

We first make the density well-defined and show that its Laguerre normalizer is strictly positive. We then verify normalization by polar coordinates, the modified-Bessel angular identity, a nonnegative series expansion, and gamma integrals. Polar marginalization gives the amplitude law and its specializations. Finally, the change of variables x=r^2 yields the power density; expanding I_0 and regrouping each term as a gamma density gives the normalized mixture.

## Complete Proof

Throughout, write q=|\mu|^2/\sigma^2 and interpret \(\sigma^{2a}\) as \((\sigma^2)^a\). Since a>0 and q\ge 0, Kummer's power-series identity gives
\[
\mathcal L_{a-1}(-q)=\exp(-q)\sum_{k=0}^{\infty}\frac{(a)_kq^k}{(k!)^2}>0.
\]
Thus the displayed density is nonnegative and well-defined away from z=0; the separately assigned value at z=0 does not affect any integral.

Write z=re^{i\theta}, \mu=\nu e^{i\phi}, with \nu=|\mu| and, when \nu=0, choose any value of \phi. The identity
\[
|z-\mu|^2=r^2+\nu^2-2\nu r\cos(\theta-\phi)
\]
and the planar Jacobian dA=r\,dr\,d\theta give, for r>0,
\[
p_{R,\Theta}(r,\theta)=\frac{r^{2a-1}e^{-(r^2+\nu^2)/\sigma^2}e^{(2\nu r/\sigma^2)\cos(\theta-\phi)}}{\pi(\sigma^2)^a\Gamma(a)\,\mathcal L_{a-1}(-q)}.
\]
Using
\[
\int_{-\pi}^{\pi}e^{t\cos u}\,du=2\pi I_0(t),
\]
integration over theta gives
\[
f_R(r)=\frac{2r^{2a-1}e^{-(r^2+\nu^2)/\sigma^2}I_0(2\nu r/\sigma^2)}{(\sigma^2)^a\Gamma(a)\,\mathcal L_{a-1}(-q)},\qquad r>0.
\]

To verify normalization directly, expand the nonnegative series
\[
I_0(2\nu r/\sigma^2)=\sum_{k=0}^{\infty}\frac{(\nu^2r^2/\sigma^4)^k}{(k!)^2}.
\]
Tonelli's theorem permits termwise integration. With
\[
\int_0^\infty r^{2a+2k-1}e^{-r^2/\sigma^2}\,dr
=\frac12(\sigma^2)^{a+k}\Gamma(a+k),
\]
the integral of p over the plane is
\[
\frac{e^{-q}}{\Gamma(a)\,\mathcal L_{a-1}(-q)}
\sum_{k=0}^{\infty}\frac{\Gamma(a+k)q^k}{(k!)^2}
=\frac{e^{-q}}{\mathcal L_{a-1}(-q)}
\sum_{k=0}^{\infty}\frac{(a)_kq^k}{(k!)^2}
=\frac{\mathcal L_{a-1}(-q)}{\mathcal L_{a-1}(-q)}=1,
\]
where the last equality uses the Kummer-series identity stated above. This proves \(\int_{\mathbb C}p\,dA=1\).

If a=1, then \((0)_0=1\) and \((0)_k=0\) for every k\ge1, so
\[
\mathcal L_0(-q)=1.
\]
Consequently the amplitude formula becomes
\[
f_R(r)=\frac{2r}{\sigma^2}e^{-(r^2+\nu^2)/\sigma^2}I_0(2\nu r/\sigma^2),
\]
which is the Rice density. If \nu=0, set a=m>0 and \(\sigma^2=\Omega/m\) with \Omega>0. Since \(I_0(0)=1\),
\[
f_R(r)=\frac{2m^m}{\Gamma(m)\Omega^m}r^{2m-1}e^{-mr^2/\Omega},
\]
which is the Nakagami-m density. The cases m=1 and \(m=\tfrac12\) are respectively the Rayleigh and one-sided normal laws.

Set X=R^2, \(\beta=1/\sigma^2\), and \(\lambda=\beta\nu^2\). Since \(dr=dx/(2\sqrt{x})\), the amplitude formula and
\[
\mathcal L_{a-1}(-\lambda)=e^{-\lambda}\mathcal L_{-a}(\lambda)
\]
give
\[
f_X(x)=\frac{\beta^a x^{a-1}e^{-\beta x}I_0(2\sqrt{\beta\lambda x})}{\Gamma(a)\,\mathcal L_{-a}(\lambda)},\qquad x>0.
\]
For \lambda=0, \(I_0(0)=1\) and \(\mathcal L_{-a}(0)=1\), so this is the Gamma(a, rate beta) density.

For general \lambda\ge0, expand
\[
I_0(2\sqrt{\beta\lambda x})=\sum_{n=0}^{\infty}\frac{(\beta\lambda x)^n}{(n!)^2}.
\]
Using \(\Gamma(a+n)=\Gamma(a)(a)_n\), regrouping gives
\[
f_X(x)=\sum_{n=0}^{\infty}w_ng_{a+n,\beta}(x),
\qquad
w_n=\frac{(a)_n\lambda^n}{(n!)^2\mathcal L_{-a}(\lambda)},
\]
where, for k>0,
\[
g_{k,\beta}(x)=\frac{\beta^kx^{k-1}e^{-\beta x}}{\Gamma(k)}.
\]
All weights are nonnegative. Finally, by the defining series of \(\mathcal L_{-a}\),
\[
\sum_{n=0}^{\infty}w_n
=\frac{\sum_{n=0}^{\infty}(a)_n\lambda^n/(n!)^2}{\mathcal L_{-a}(\lambda)}=1.
\]
This also includes the \lambda=0 case, where w_0=1 and all other weights vanish.
