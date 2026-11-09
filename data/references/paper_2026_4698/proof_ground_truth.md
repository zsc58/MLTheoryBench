# Reference Proof

## Proof Structure and Obligations

Fix one neuron and use its own maximal ideal-flow solution for the integrated theorem. We prove: (1) the exact Fourier reduction with the stated loss normalization; (2) positivity, conserved quantities, and the reduced domain; (3) preservation of magnitude and phase order by a cooperative comparison theorem; (4) a high-probability initial phase event; (5) a quantitative short-time ratio gap; and (6) threshold attainment before finite-time termination, followed by the stated time bound. The auxiliary source dependencies concerning approximation errors and trajectory symmetry are checked at the end. The auxiliary symmetry check concerns a standalone single-frequency solution on its own maximal interval, not a claim that every frequency crosses its turning point before the multi-frequency neuron terminates. No nonstandard external result is assumed.

## 1. Exact ideal dynamics

Suppress the neuron index. Write \(\bar\xi=p^{-1}\sum_j\xi[j]\). Differentiating the summed CE loss first, and then replacing each softmax probability by \(1/p\), gives
\[
\dot\xi[j]=\sum_x(\theta[x]+\theta[j-x])^2-\frac1p\sum_{x,y}(\theta[x]+\theta[y])^2,
\]
\[
\dot\theta[j]=4\sum_x(\xi[x+j]-\bar\xi)(\theta[x]+\theta[j]).
\]
All indices here are modulo \(p\). These equations involve only this neuron's parameters, so its solution can be considered on its own maximal interval, independently of other neurons' termination times.

For nonzero frequencies in the specified range, the elementary Fourier identities give
\[
\sum_x\cos(\omega_k(x+j)+\psi)\cos(\omega_kx+\phi)
=\frac p2\cos(\omega_kj+\psi-\phi),
\]
and the corresponding sums between different frequencies vanish. The convolution in the first equation similarly retains only equal frequencies; its constant part is removed by the uniform subtraction. Consequently
\[
\dot\xi[j]=p\sum_k\alpha_k^2\cos(\omega_kj+2\phi_k),\qquad
\dot\theta[j]=2p\sum_k\alpha_k\beta_k\cos(\omega_kj+\psi_k-\phi_k).
\]
Both constant coefficients have zero derivative and remain zero.

For each frequency, put \(A_k=\alpha_ke^{i\phi_k}\) and \(B_k=\beta_ke^{i\psi_k}\). Projection gives
\[
\dot A_k=2p\overline A_k B_k,\qquad \dot B_k=pA_k^2.
\]
These are autonomous polynomial equations in real and imaginary parts. They have unique local solutions, and a solution can terminate at a finite maximal time only if its Cartesian coefficients become unbounded. Radial and angular differentiation, initially valid because both magnitudes equal \(\kappa>0\), gives
\[
\dot\alpha_k=2p\alpha_k\beta_k\cos D_k,\quad
\dot\beta_k=p\alpha_k^2\cos D_k,
\]
\[
\dot\phi_k=-2p\beta_k\sin D_k,\quad
\dot\psi_k=p\frac{\alpha_k^2}{\beta_k}\sin D_k,\quad
\dot D_k=-p\left(4\beta_k+\frac{\alpha_k^2}{\beta_k}\right)\sin D_k,
\]
where \(D_k\) is a continuous lift of the phase difference whenever needed.

## 2. Invariants and shortest angles

Direct differentiation yields
\[
\frac d{dt}(\alpha_k^2-2\beta_k^2)=0,
\qquad \alpha_k^2-2\beta_k^2=-\kappa^2.
\]
In particular \(\beta_k\ge\kappa/\sqrt2\). On every compact subinterval of existence,
\(\alpha_k(t)=\kappa\exp(2p\int_0^t\beta_k\cos D_k\,ds)>0\), so actually \(\beta_k>\kappa/\sqrt2\), and the polar equations remain legitimate.

For the second invariant, let \(Q_k=\alpha_k^2\beta_k\). Then
\[
\dot Q_k=p\alpha_k^2(\alpha_k^2+4\beta_k^2)\cos D_k.
\]
Combining this with the equation for \(D_k\) gives
\[
\frac d{dt}(Q_k\sin D_k)=0,
\qquad
\alpha_k(t)^2\beta_k(t)\sin D_k(t)=\kappa^3\sin D_k(0).
\]
For nonstationary initial phase, this excludes crossing a multiple of \(\pi\) at a finite time of existence. The endpoint phases are stationary by their equation.

Reflection \(D\mapsto-D\) leaves the magnitude dynamics unchanged. Hence the shortest angle \(\delta_k\in[0,\pi]\) satisfies
\[
\dot\beta_k=p(2\beta_k^2-\kappa^2)\cos\delta_k,
\qquad
\dot\delta_k=-p\left(6\beta_k-\frac{\kappa^2}{\beta_k}\right)\sin\delta_k.
\tag{1}
\]
Thus \(\delta_k\) is nonincreasing, and remains in \((0,\pi)\) at every finite time when initialized there. The random initialization has all angles in this interior almost surely.

## 3. Comparison and the winning frequency

Use coordinates \(x_1=-\beta\), \(x_2=\delta\). Equation (1) has vector field
\[
f_1=-p(2x_1^2-\kappa^2)\cos x_2,
\qquad f_2=p(6x_1-\kappa^2/x_1)\sin x_2.
\]
On the open, order-convex domain
\(x_1<-\kappa/\sqrt2\), \(0<x_2<\pi\), it is continuously differentiable and
\[
\partial_{x_2}f_1=p(2x_1^2-\kappa^2)\sin x_2\ge0,
\qquad
\partial_{x_1}f_2=p(6+\kappa^2/x_1^2)\sin x_2\ge0.
\]
The standard cooperative ODE comparison principle states that a continuously differentiable vector field with nonnegative off-diagonal derivatives on an order-convex domain preserves coordinatewise order between solutions throughout their common existence interval. Its hypotheses have just been verified; the solutions stay in the domain by Section 2.

Therefore, if \(\sigma\) orders the initial angles increasingly, then
\[
\beta_{\sigma(1)}(t)\ge\cdots\ge\beta_{\sigma(K)}(t),
\qquad
\delta_{\sigma(1)}(t)\le\cdots\le\delta_{\sigma(K)}(t).
\tag{2}
\]
This holds on the fixed neuron's maximal interval. Write \(\star=\sigma(1)\) and \(\sharp=\sigma(2)\). Comparison with the runner-up controls every competitor. The endpoint cases, though null under initialization, also follow directly from (1) or by continuity.

## 4. Initial phase event

The independent uniform coefficient directions give independent uniform phases modulo \(2\pi\). Conditional on each input phase, subtracting the independent uniform output phase makes \(D_k(0)\) uniform modulo \(2\pi\). Thus the \(\delta_k(0)\) are iid uniform on \([0,\pi]\).

Let their order statistics be \(U_{(1)},U_{(2)},\ldots\), and set
\[
s=\pi p^{-(c+1)},\quad a=2c\pi\frac{\log p}{p},\quad
G=2p^{-2(c+1)},\quad d_p=1-2c^2\pi^2(\log p/p)^2.
\]
For fixed \(c\in(0,1)\) and sufficiently large \(p\), consider
\[
E=\{s\le U_{(1)}\le a,\ U_{(2)}-U_{(1)}\ge s,\ U_{(2)}<\pi/2\}.
\]
The minimum and first spacing obey
\[
\Pr(U_{(1)}<s)=1-(1-s/\pi)^K\le Ks/\pi,
\]
\[
\Pr(U_{(2)}-U_{(1)}<s)=1-(1-s/\pi)^K\le Ks/\pi.
\]
For the spacing identity, the ordered sample has constant density on \(0<u_1<\cdots<u_K<\pi\); subtracting \(s\) from coordinates \(u_2,\ldots,u_K\) maps the event \(u_2-u_1\ge s\) to an ordered simplex of side length \(\pi-s\), giving the stated volume ratio.

Also
\[
\Pr(U_{(1)}>a)=(1-a/\pi)^K
\le p^{-c}\exp(c\log p/p)\le2p^{-c},
\]
and
\[
\Pr(U_{(2)}\ge\pi/2)=(K+1)2^{-K}=O(p^{-c}).
\]
Hence \(\Pr(E^c)\le C_0p^{-c}\) for a universal constant and sufficiently large \(p\), which implies the requested polylogarithmic probability bound.

On \(E\), \(\cos U_{(1)}\ge1-a^2/2=d_p\). For \(u=U_{(1)}\), \(v=U_{(2)}<\pi/2\), the identity for a cosine difference and \(\sin z\ge2z/\pi\) on \([0,\pi/2]\) give
\[
\cos u-\cos v
=2\sin\frac{u+v}{2}\sin\frac{v-u}{2}
\ge\frac{2(v^2-u^2)}{\pi^2}\ge G.
\tag{3}
\]
Here \(u\ge s\) and \(v-u\ge s\). Both winner and runner-up remain below \(\pi/2\), so their magnitudes are nondecreasing and at least \(\kappa\); the winner's cosine remains at least \(d_p\).

## 5. Quantitative initial growth

Work on \(E\). Equation (1) gives \(\dot\beta_k\le2p\beta_k^2\). Integrating the reciprocal inequality yields
\[
\beta_k(t)\le\frac{\kappa}{1-2p\kappa t}\le2\kappa
\quad\text{for }0\le t\le\frac1{4p\kappa}.
\]
This also guarantees existence through that interval: the invariant bounds \(\alpha_k\), and bounded Cartesian coefficients permit continuation.

Let
\[
t_1=\frac{G}{48p\kappa}.
\]
For sufficiently large \(p\), \(G\le1\), so the preceding bound applies. For either of the two leading frequencies,
\[
0\le\frac d{dt}\cos\delta_k
=p(6\beta_k-\kappa^2/\beta_k)\sin^2\delta_k\le12p\kappa.
\]
Consequently, throughout \([0,t_1]\), the cosine gap is at least \(G-24p\kappa t\ge G/2\).

Put \(\rho=\beta_\star/\beta_\sharp\), \(L=\log\rho\), and \(h(b)=2b-\kappa^2/b\). By (2),
\[
\dot L=p\{[h(\beta_\star)-h(\beta_\sharp)]\cos\delta_\star
+h(\beta_\sharp)(\cos\delta_\star-\cos\delta_\sharp)\}.
\tag{4}
\]
Both terms are nonnegative, and \(h(\beta_\sharp)\ge\kappa\). Therefore
\[
L(t_1)\ge p\kappa\frac G2t_1=\frac{G^2}{96}.
\]
For \(q=1-1/\rho=1-e^{-L}\), this implies
\[
q(t_1)\ge1-e^{-G^2/96}\ge\frac{G^2}{192}
=\frac1{48}p^{-4(c+1)}.
\tag{5}
\]
Moreover \(t_1\le C\pi^2p^{-(2c+3)}/\kappa\), as required for the first stage.

## 6. Existence of the hitting time and final bound

It is necessary to prove the threshold is attained before the ideal solution terminates. Let \(b=\beta_\star\), \(v=\beta_\sharp\), and
\[
w=\frac1v-\frac1b.
\]
By (5), \(w(t_1)>0\). Define \(A(z)=2-\kappa^2/z^2\), which is nonnegative and increasing on \([\kappa/\sqrt2,\infty)\). Equation (1) and (2) give
\[
\dot w=p\{A(b)\cos\delta_\star-A(v)\cos\delta_\sharp\}
=p\{[A(b)-A(v)]\cos\delta_\star
+A(v)(\cos\delta_\star-\cos\delta_\sharp)\}\ge0.
\]
Thus \(v(t)\le1/w(t_1)\) for all later times of existence. Every other competitor is bounded by \(v\).

The winner is increasing and satisfies
\[
\dot b\ge pd_p(2b^2-\kappa^2)\ge pd_p b^2,
\]
since \(b\ge\kappa\). The fixed neuron's maximal time \(T_m\) is therefore finite, with \(T_m\le1/(p\kappa d_p)\). At a finite maximal time some Cartesian coefficient must become unbounded. The invariant and (2) show that boundedness of \(b\) would bound all coefficients, so \(b(t)\to\infty\) as \(t\uparrow T_m\). The competitors remain bounded by the reciprocal-gap estimate. Consequently
\[
\frac{\beta_\sharp(t)}{\beta_\star(t)}\longrightarrow0,
\qquad q(t)\longrightarrow1.
\]
Continuity now proves that every threshold \(\epsilon\in(0,1)\) is attained at a time strictly below \(T_m\).

For the quantitative estimate, \(h'(b)=2+\kappa^2/b^2\ge2\). Dropping the second term of (4) gives
\[
\dot L\ge2pd_p(\beta_\star-\beta_\sharp)
\ge2p\kappa d_p(\rho-1),
\qquad
\dot q=\rho^{-1}\dot L\ge2p\kappa d_pq.
\]
If the threshold has already been reached by \(t_1\), there is nothing further to prove. Otherwise integration up to the now-established hitting time gives
\[
t_{m,\epsilon}\le t_1+
\frac{[\log((1-\epsilon)/q(t_1))]_+}{2p\kappa d_p}.
\]
Using (5), and enlarging a universal constant, this is at most
\[
C\left[\frac{\pi^2}{\kappa}p^{-(2c+3)}+
\frac{(c+1)\log p+\log(1/(1-\epsilon))}{p\kappa d_p}\right].
\]
The positive logarithm in the stated bound is a permissible relaxation; it is not the exact threshold logarithm. Equation (2) gives the same dominance threshold for every competitor. The event \(E\) depends only on the fixed neuron's initial phases and has the required probability; no simultaneous probability statement over all neurons is used.

## Auxiliary source-dependency checks

### Approximation error normalization

Although the theorem concerns the exact ideal model, its source decomposition can be checked directly. With \(P_\tau(x,y)=\operatorname{softmax}(f(x,y))_\tau\), the full theta-gradient residual is
\[
\operatorname{Err}^{(2)}_{m,j}=4\sum_{x,\tau}(P_\tau(x,j)-1/p)\xi_m[\tau](\theta_m[x]+\theta_m[j]).
\]
The factor 4 comes from the two symmetric input positions and the derivative of the quadratic activation. If \(\Delta\) bounds the logit spread, comparison with the largest and smallest logits gives \(|P_\tau-1/p|\le p^{-1}(e^\Delta-1)\). Here \(\Delta\le8M\|\xi\|_\infty\|\theta\|_\infty^2\). Taking absolute values termwise gives the error bounds \(4p\|\theta_m\|_\infty^2(e^\Delta-1)\) and \(8p\|\xi_m\|_\infty\|\theta_m\|_\infty(e^\Delta-1)\). Thus the source's common bound remains valid after correcting the residual definition.

### Trajectory symmetry

This auxiliary lemma concerns the standalone single-frequency reduced system. Fix initial data \(\widehat\beta(0)=\kappa\) and \(\widehat\delta(0)=\delta_0\in(\pi/2,\pi)\). Let \((\widehat\beta,\widehat\delta)\) solve (1) on its own maximal interval \([0,\widehat T)\), without stopping it when another frequency terminates. Autonomy and uniqueness ensure that a frequency in the multi-frequency neuron agrees with this standalone solution on their shared interval.

Before the first \(\pi/2\) crossing, the invariant and monotonicity give
\[
\frac{\kappa}{\sqrt2}\le\widehat\beta\le\kappa,
\qquad \frac\pi2\le\widehat\delta\le\delta_0.
\]
This rectangle is a compact subset of the smooth vector field's domain \(\beta>0\). Therefore the standalone solution cannot terminate at a finite time while it remains in the rectangle: boundedness and smoothness permit continuation. Also, on this segment,
\[
-\dot{\widehat\delta}
=p(6\widehat\beta-\kappa^2/\widehat\beta)\sin\widehat\delta
\ge2\sqrt2p\kappa\sin\delta_0>0.
\]
If no crossing occurred, continuation and integration of this inequality would force \(\widehat\delta<\pi/2\) after a finite time, a contradiction. Thus the standalone crossing time \(t_c\) is finite, with
\[
t_c\le\frac{\delta_0-\pi/2}{2\sqrt2p\kappa\sin\delta_0}.
\]
The compact-domain continuation also ensures that the solution exists at \(t_c\) and locally beyond it.

For \(0\le s\le t_c\), define
\[
\beta_R(s)=\widehat\beta(t_c-s),\qquad
\delta_R(s)=\pi-\widehat\delta(t_c-s).
\]
Direct differentiation in (1), using \(\cos(\pi-u)=-\cos u\) and \(\sin(\pi-u)=\sin u\), shows that this reflected reverse path solves the same smooth two-dimensional ODE and starts from \((\widehat\beta(t_c),\pi/2)\). Uniqueness identifies it with the standalone forward solution from \(t_c\), and the explicitly defined path supplies continuation through \(2t_c\). Consequently, for \(0<\Delta t<t_c\),
\[
\widehat\beta(t_c-\Delta t)=\widehat\beta(t_c+\Delta t),\qquad
\widehat\delta(t_c-\Delta t)+\widehat\delta(t_c+\Delta t)=\pi.
\]
These identities transfer to a multi-frequency neuron's trajectory only when both evaluation times are in \([0,T_m)\). The standalone crossing may occur after \(T_m\); no crossing within the neuron's interval is asserted or needed in Sections 1–6. One must not instead invoke local Lipschitz continuity of the eliminated scalar square-root field at its turning point: that field is generally only square-root regular there.

All listed obligations are closed.
