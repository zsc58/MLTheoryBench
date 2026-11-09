# Reference Proof

## Proof Structure

First derive the exact energy-dissipation identity directly from the metric, kinetic energy, and equation of motion. Integrating this identity gives a common cubic dissipation integral. A lower bound on that integral before the kinetic-energy hitting time yields the stopping-time estimate. An upper bound using monotonicity of the total energy converts the same integral into Riemannian arc length; state convergence then identifies the limiting energy loss.

## Complete Proof

Write $v=\dot x(t)$, $g=\nabla F(x(t))$, and

$$q=g^T v,\qquad r=v^T\nabla^2F(x(t))v.$$

Since $A=I_d+gg^T$, the kinetic energy can be written as

$$K=\frac12\bigl(v^Tv+q^2\bigr).$$

Differentiation along the trajectory gives

$$\dot K=v^T\ddot x+q\bigl(r+g^T\ddot x\bigr)
=v^TA\ddot x+qr.$$

The equation of motion implies

$$A\ddot x=-(r+c)g-\lambda\sqrt K\,Av.$$

Consequently,

$$\dot K=-(r+c)q-\lambda\sqrt K\,v^TAv+qr
=-cq-2\lambda K^{3/2}.$$

On the other hand, $\dot U=cq$. Therefore

$$\boxed{\dot E(t)=-2\lambda K(t)^{3/2}.}$$

In particular, $E$ is nonincreasing. Because $z_*$ is a global minimizer, $U\ge 0$, and hence

$$0\le K(t)\le E(t)\le E(t_0).$$

Integrating the boxed identity over $[t_0,s]$ yields

$$E(t_0)-E(s)=2\lambda\int_{t_0}^sK(t)^{3/2}\,dt. \tag{1}$$

Fix $\varepsilon>0$. If $K(t_0)\le\varepsilon$, then $\tau_\varepsilon=t_0$ and the desired bound is immediate. Suppose instead that $K(t_0)>\varepsilon$. For every $s<\tau_\varepsilon$, the definition of the first hitting time and continuity of $K$ give $K(t)>\varepsilon$ on $[t_0,s]$. Thus (1) and $E(s)\ge0$ imply

$$2\lambda\varepsilon^{3/2}(s-t_0)
\le 2\lambda\int_{t_0}^sK(t)^{3/2}\,dt
\le E(t_0). \tag{2}$$

If $\tau_\varepsilon=\infty$, inequality (2) would hold for arbitrarily large finite $s$, which is impossible. Hence the hitting time is finite. Letting $s\uparrow\tau_\varepsilon$ in (2) gives

$$\tau_\varepsilon\le t_0+\frac{E(t_0)}{2\lambda\varepsilon^{3/2}}.$$

It remains to prove the length estimate. From $K(t)\le E(t_0)$ and (1), for every finite $s>t_0$,

$$
\begin{aligned}
E(t_0)-E(s)
&=2\lambda\int_{t_0}^sK(t)\sqrt{K(t)}\,dt\\
&\le 2\lambda E(t_0)\int_{t_0}^s\sqrt{K(t)}\,dt.
\end{aligned}
$$

The graph metric and the definition of $K$ give

$$\left\|\frac{d}{dt}\iota(x(t))\right\|^2
=\dot x(t)^TA(x(t))\dot x(t)=2K(t).$$

Therefore the partial arc length $\ell_s$ satisfies

$$\ell_s=\sqrt2\int_{t_0}^s\sqrt{K(t)}\,dt,$$

and hence

$$E(t_0)-E(s)\le\sqrt2\lambda E(t_0)\ell_s. \tag{3}$$

By the assumed state convergence and continuity of $F$ and $A$,

$$K(t)\longrightarrow0,
\qquad
E(t)\longrightarrow c\bigl(F(z_\infty)-F(z_*)\bigr).$$

Moreover, $\ell_s$ increases to the full length $\ell$, possibly $+\infty$. Letting $s\to\infty$ in (3) therefore gives

$$
\begin{aligned}
K(t_0)+c\bigl(F(x(t_0))-F(z_\infty)\bigr)
&=E(t_0)-c\bigl(F(z_\infty)-F(z_*)\bigr)\\
&\le\sqrt2\lambda E(t_0)\ell,
\end{aligned}
$$

which is the claimed division-free length bound. It remains valid when $E(t_0)=0$; when $E(t_0)>0$, division gives the stated ratio form.
