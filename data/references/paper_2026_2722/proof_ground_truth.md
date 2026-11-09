# Reference Proof

## Contract and Notation

Work on the unit-volume torus. All constants below depend only on the displayed parameters, the indicated upper bound for the potential norm, and, when specified, an upper bound for the initial density norm. They never require a positive lower bound for the evolving density.

Put
\[
\sigma=\rho-\pi,\quad H=\mathcal H(\rho\mid\pi),\quad X=\|\sigma\|_{\dot H^\gamma}^2,\quad a_0=(s-1)/\gamma.
\]
The functions \(\pi\) and \(\pi^{-1}\) belong to \(H^{\gamma+s}\), with controlled norms, and \(0<m\le\pi\le M_\pi\), because \(\gamma+s>d/2\), Sobolev embedding, and Sobolev composition apply to \(e^{\pm V}\). Define the vector distribution and velocity with reversed sign by
\[
 F=\nabla\sigma+\sigma\nabla V=\pi\nabla(\sigma/\pi),\qquad
 w=D^{-2s}F=\nabla D^{-2s}\sigma+D^{-2s}(\sigma\nabla V).
\]
Thus \(u=-w\) and \(\partial_t\sigma=\operatorname{div}(\pi w)+\operatorname{div}(\sigma w)\). The multiplier always removes the zero Fourier mode. For vector and tensor fields, Sobolev norms are the sums of the component norms.

## Analytic Background and Zero Modes

We use Fourier Sobolev interpolation, Sobolev embedding, the Sobolev algebra and composition estimates, Gronwall's inequality, and the following commutator bounds. These are the standard independent commutator estimates quoted in the source. If \(b>1\), then
\[
 \|[D^b,f]g\|_2\le C\bigl(\|\nabla f\|_\infty\|D^{b-1}g\|_2+\|D^bf\|_p\|g\|_q\bigr),\qquad 1/p+1/q=1/2.
\]
We use either \((p,q)=(2,\infty)\) or finite \(p,q\ge2\). We also use the order-one Lipschitz commutator estimate
\[
 \|[D,f]g\|_2\le C\|\nabla f\|_\infty\|g\|_2.
\]
All uses below have precisely these admissible exponents. They extend from smooth functions by regularization.

A needed homogeneous multiplier fact requires care with constants. If \(\alpha>d/2\), \(|b|\le\alpha\), and \(f\) has zero mean, then
\[
 \|gf\|_{\dot H^b}\le C\|f\|_{\dot H^b},\qquad g\in H^\alpha.
\]
This follows by inhomogeneous multiplication and the equivalence of the two norms on zero-mean inputs. If also \(g\ge\lambda>0\), the reverse bound holds. Indeed write \(gf=h+c\), with \(h\) of zero mean. The condition \(\int f=0\) gives
\[
 c=-\frac{\langle h,g^{-1}\rangle}{\int g^{-1}},\qquad
 |c|\le C\|h\|_{\dot H^b}.
\]
The last estimate is Sobolev duality, since \(g^{-1}\in H^\alpha\). Multiplication by \(g^{-1}\) in \(H^b\) now proves the reverse bound. In particular, no assertion that multiplication preserves zero mean is used.

We will also need, for a zero-mean smooth scalar or tensor field \(h\), the interpolation estimate
\[
 \|D^t h\|_{L^{2n/t}}\le C\|h\|_\infty^{1-t/n}\|D^nh\|_2^{t/n},\qquad 0<t<n.
 \tag{A}
\]
Here is a routine derivation of the particular estimate needed, rather than an invocation of an unspecified specialized interpolation theorem. Decompose into smooth dyadic Fourier blocks. The blocks of \(D^t h\) below scale \(2^J\) have pointwise sum bounded by \(C2^{Jt}\|h\|_\infty\). Write each higher block as an order \(t-n\) multiplier applied to a block of \(D^nh\); its kernel bound gives a pointwise bound by \(C2^{j(t-n)}\mathcal M(D^nh)\), where \(\mathcal M\) is the Hardy-Littlewood maximal operator. Summation and optimization in \(J\) give
\[
 |D^th|\le C\|h\|_\infty^{1-t/n}\mathcal M(D^nh)^{t/n}.
\]
The zero-mean condition removes the constant block; the finitely many lowest torus frequencies obey the same estimate. Integrating with exponent \(2n/t\), and using the standard \(L^2\) maximal inequality, proves (A). Finite-exponent Riesz transforms may be used to replace a full derivative by its component derivatives.

## 1. Entropy Dissipation and Coercivity

Define
\[
 I=\|F\|_{\dot H^{-s}}^2.
\]
Integration by parts in the continuity equation gives
\[
 H'=-\langle F,D^{-2s}F\rangle=-I.
 \tag{1}
\]
This identity does not require \(\rho>0\). It can be justified by smooth positive approximation, or by regularizing the entropy with \((\rho+\varepsilon)\log(\rho+\varepsilon)+\rho V\). The extra flux term, after integration by parts, is controlled on bounded time intervals by \(C\varepsilon(1+|\log\varepsilon|)\|\operatorname{div}u\|_1\), and vanishes. The Sobolev solution has a spatially Lipschitz velocity, as also verified in the continuation discussion below. Consequently the regularized transport identities and their limiting entropy identity are valid.

Apply the preceding positive multiplier equivalence first to the zero-mean vector field \(\nabla(\sigma/\pi)\), with multiplier \(\pi\) and order \(-s\), and then to the zero-mean function \(\sigma\), with multiplier \(\pi^{-1}\) and order \(1-s\). The available regularity \(\gamma+s\) exceeds all required orders. Therefore
\[
 I\asymp\|\nabla(\sigma/\pi)\|_{\dot H^{-s}}^2
 =\|\sigma/\pi\|_{\dot H^{1-s}}^2
 \asymp\|\sigma\|_{\dot H^{1-s}}^2.
 \tag{2}
\]

For \(\varphi(r)=r\log r-r+1\),
\[
 \frac{(r-1)^2}{2\max(r,1)}\le\varphi(r)\le(r-1)^2.
\]
Integration against \(\pi\) proves
\[
 H\le m^{-1}\|\sigma\|_2^2,
 \qquad
 H\ge(2\Lambda)^{-1}\|\sigma\|_2^2\quad\text{if }\rho,\pi\le\Lambda.
 \tag{3}
\]
These inequalities include zero densities by continuity. Interpolating between orders \(1-s\) and \(\gamma\), then using (2), gives
\[
 H\le C I^{\gamma/(\gamma+s-1)}X^{(s-1)/(\gamma+s-1)}.
\]
Thus, whenever \(X>0\),
\[
 I\ge c H^{1+a_0}X^{-a_0}.
 \tag{4}
\]
If \(X=0\), then \(\rho=\pi\), and uniqueness, or the nonnegative entropy identity, gives the stationary solution. All subsequent divisions are confined to nonstationary intervals.

## 2. High-Order Energy Estimate

Set
\[
 L=\|\nabla^2D^{-2s}\sigma\|_\infty+
       \|\nabla D^{-2s}(\sigma\nabla V)\|_\infty.
\]
In particular \(\|\nabla w\|_\infty\le L\). We derive
\[
 X'\le CLX-2m\|\sigma\|_{\dot H^{\gamma-s+1}}^2
       +C\|\sigma\|_{\dot H^{\gamma-s}}
          \|\sigma\|_{\dot H^{\gamma-s+1}}.
 \tag{5}
\]
For smooth solutions, half the energy derivative is the sum of
\[
 \mathrm{Lin}=\langle D^\gamma\operatorname{div}(\pi w),D^\gamma\sigma\rangle,
 \qquad
 \mathrm{Nonlin}=\langle D^\gamma\operatorname{div}(\sigma w),D^\gamma\sigma\rangle.
\]
Move derivatives between the two factors in the linear term. Its leading part is
\[
 -\int\pi|\nabla D^{\gamma-s}\sigma|^2
 \le-m\|\sigma\|_{\dot H^{\gamma-s+1}}^2.
\]
The remaining two terms are
\[
 -\langle[D^{\gamma+s},\pi]\nabla D^{-2s}\sigma,
                 \nabla D^{\gamma-s}\sigma\rangle
\]
and
\[
 -\langle D^{\gamma+s}(\pi D^{-2s}(\sigma\nabla V)),
                 \nabla D^{\gamma-s}\sigma\rangle.
\]
For the first, use the commutator estimate of order \(\gamma+s>1\). Both \(\|\nabla\pi\|_\infty\) and \(\|D^{\gamma+s}\pi\|_2\) are controlled, and
\[
 \|D^{\gamma+s-1}\nabla D^{-2s}\sigma\|_2
 \le C\|\sigma\|_{\dot H^{\gamma-s}},\qquad
 \|\nabla D^{-2s}\sigma\|_\infty
 \le C\|\sigma\|_{\dot H^{\gamma-s}},
\]
since \(\gamma+s-1>d/2\). For the second, homogeneous multiplication first by \(\pi\) and then by \(\nabla V\) gives
\[
 \|D^{\gamma+s}(\pi D^{-2s}(\sigma\nabla V))\|_2
 \le C\|\sigma\|_{\dot H^{\gamma-s}}.
\]
Here \(D^{-2s}(\sigma\nabla V)\) has zero mean, and \(\nabla V\in H^{\gamma+s-1}\) is an admissible multiplier at order \(\gamma-s\): indeed \(\gamma+s-1>d/2\) and \(\gamma+s-1\ge|\gamma-s|\), using \(\gamma>d/2\ge1/2\). This proves the claimed linear remainder bound.

For the nonlinear term, algebra and self-adjointness give the exact decomposition
\[
 \mathrm{Nonlin}
 =-\langle wD^\gamma\sigma,\nabla D^\gamma\sigma\rangle
  +\langle[D,w]D^\gamma\sigma,\nabla D^{\gamma-1}\sigma\rangle
  -\langle[D^{\gamma+1},w]\sigma,\nabla D^{\gamma-1}\sigma\rangle.
\]
The first term is bounded by \(CLX\) after integration by parts. The order-one Lipschitz commutator bounds the second by \(CLX\). For the last, the order \(\gamma+1>1\) commutator bound gives
\[
 C\bigl(LX^{1/2}+\|\sigma\|_p\|D^{\gamma+1}w\|_q\bigr)X^{1/2}.
\]
Write \(a=2s-2>0\), \(n=\gamma+a\), \(p=2n/a\), and \(q=2n/\gamma\). Both exponents are finite and greater than two, and \(1/p+1/q=1/2\). Apply (A) to \(h=D^{-a}\sigma\), with derivative order \(a\), and to \(h=\nabla w\), with derivative order \(\gamma\). With
\[
 A=\|\nabla^2D^{-2s}\sigma\|_\infty,\qquad B=\|\nabla w\|_\infty,
\]
this yields
\[
 \|\sigma\|_p\le C A^{\gamma/n}X^{a/(2n)},\qquad
 \|D^{\gamma+1}w\|_q\le C B^{a/n}X^{\gamma/(2n)}.
\]
For the first estimate, \(D^{-a}\sigma=-\Delta D^{-2s}\sigma\), so its infinity norm is bounded by the Hessian norm. For the second, finite-exponent Riesz transforms are bounded, and
\[
 \|D^n\nabla w\|_2=\|F\|_{\dot H^{\gamma-1}}\le C X^{1/2}.
\]
The last inequality follows from \(F=\nabla\sigma+\sigma\nabla V\) and the multiplier bound at order \(\gamma-1\), whose hypotheses again follow from \(\gamma>1/2\) and \(s>1\). Weighted Young's inequality now gives
\[
 \|\sigma\|_p\|D^{\gamma+1}w\|_q
 \le C(A+B)X^{1/2}\le CLX^{1/2}.
\]
This proves (5), including the fractional range \(1/2<\gamma<1\).

Let \(b=\gamma-s+1\) and \(\ell=1-s\), so \(b-\ell=\gamma>0\). Frequency splitting gives, for every \(\varepsilon>0\),
\[
 \|\sigma\|_{\dot H^{b-1}}\|\sigma\|_{\dot H^b}
 \le\varepsilon\|\sigma\|_{\dot H^b}^2+C_\varepsilon\|\sigma\|_{\dot H^\ell}^2.
\]
To see this uniformly in the permitted range of \(\gamma\), first bound the square of the order \(b-1\) norm by an arbitrarily small multiple of the square of the order \(b\) norm plus a fixed multiple of the order \(\ell\) norm, splitting at a large frequency, and then use Young's inequality. This also covers \(b-1\le\ell\). Absorb the high-order term in (5) and use (2). For a fixed data-dependent constant \(C_E\),
\[
 X'\le C_E L X+C_E I.
 \tag{6}
\]
The additive \(I\) term must not be discarded or included without justification in \(LX\).

## 3. Integrated Lipschitz Estimate

Suppose \(X\le M\) on an interval. Set
\[
 r=\max\{2-2s+\gamma/2+d/4,\ 1-s\},\qquad
 \theta=\frac{r+s-1}{\gamma+s-1}.
\]
The strict assumptions on \(\gamma\) give \(1-s\le r<\gamma\), \(r+2s-2>d/2\), and \(0\le\theta<1\). Sobolev embedding and multiplication by \(\nabla V\) at order \(r\) show
\[
 L\le C\|\sigma\|_{\dot H^r}
 \le C I^{(1-\theta)/2}M^{\theta/2}.
\]
For the drift term, the map \(\nabla D^{-2s}\) gains \(2s-1\) derivatives; its output is therefore also in a Sobolev space embedded into \(L^\infty\). The multiplier hypotheses hold because \(|r|\le\gamma+s-1\).

Use (4) to estimate the negative power in
\(I^{(1-\theta)/2}=I I^{-(1+\theta)/2}\). On positive-entropy intervals,
\[
 L\le C_M I H^{-(1+\theta)(1+a_0)/2}
   =-\frac{C_M}{b_*}(H^{b_*})',
\]
where
\[
 b_*=1-\frac{(1+\theta)(1+a_0)}2
 =\min\left\{\frac{2\gamma-d}{8\gamma},\frac{\gamma-s+1}{2\gamma}\right\}>0.
\]
Consequently
\[
 \int_0^tL(\tau)\,d\tau\le C_M H_0^{b_*}.
 \tag{7}
\]
The dependence on \(M\) can be bounded using any fixed upper bound on \(M\); the powers of \(M\) in this derivation are nonnegative. If entropy reaches zero, the solution is stationary thereafter, and the estimate follows by taking limits up to that time.

## 4. Corrected Bootstrap and Entropy Rate

By (3) and the zero-mean Poincare inequality there is a constant \(c_E\), depending only on the potential bound and the fixed parameters, such that
\[
 H_0\le c_E X_0.
\]
If \(X_0=0\), the solution is stationary. Otherwise choose
\[
 A_*=4(1+C_Ec_E),\qquad M=A_*X_0.
\]
There is a positive upper bound \(\overline M\) for \(M\) depending only on \(d,s,\gamma,\|V\|_{H^{\gamma+s}},\|\bar\rho\|_{H^\gamma}\). Bootstrap up to the first exit from \(X<M\). On that interval, (6), (1), (7), and Gronwall give
\[
 X(t)\le\left(X_0+C_E\int_0^tI\right)
              \exp\left(C_E\int_0^tL\right)
 \le (1+C_Ec_E)X_0\exp(C_E C_{\overline M}H_0^{b_*}).
\]
Choose \(\delta>0\), with only the stated dependencies, so the exponential is at most two when \(H_0\le\delta\). Then \(X(t)\le M/2<M\), a strict improvement that rules out a first exit.

On the same interval, (1) and (4) imply
\[
 H'\le-c\overline M^{-a_0}H^{1+a_0}.
\]
Integration gives
\[
 H_t\le\left(H_0^{-a_0}+t/C\right)^{-1/a_0},
 \tag{8}
\]
where one can choose \(C=\overline M^{a_0}/(a_0c)\), enlarging it if needed.

## 5. Sobolev Solution Justification and Continuation

The local solution is part of the problem's hypotheses; its continuation need not be taken on faith from the paper-specific citation. Here are the relevant local estimates. For \(q=\gamma\) and \(q=\gamma-1\), the linear velocity map satisfies
\[
 \|u[f]\|_{H^{q+2s-1}}\le C\|f\|_{H^q},\qquad
 u[f]=-D^{-2s}(\nabla f+f\nabla V).
\]
These follow from Fourier multipliers and Sobolev multiplication; for both values of \(q\), \(\nabla V\) has the required multiplier regularity. In particular, a bounded \(H^\gamma\) density gives a bounded \(H^{\gamma+1}\) velocity, and hence a spatially Lipschitz velocity, because \(2s-1>1\) and \(\gamma>d/2\).

The standard linear transport energy estimate, together with the \(H^\gamma\) algebra estimate applied to \(\rho\operatorname{div}u\), gives on bounded norm sets
\[
 \left|\frac d{dt}\|\rho\|_{H^\gamma}^2\right|
 \le C(1+\|\rho\|_{H^\gamma})\|\rho\|_{H^\gamma}^2.
\]
It gives a local existence interval of length bounded below in terms of an upper bound for \(\|\rho\|_{H^\gamma}\). For completeness, regularize the velocity and solve successive linear transport equations; this estimate bounds the iterates on a common interval. For two iterates or solutions, their difference \(\eta\) has forcing \(-\operatorname{div}(\rho_2(u_1-u_2))\). The velocity estimate at \(q=\gamma-1\), the algebra property, and the transport estimate at order \(\gamma-1\) give
\[
 \|\operatorname{div}(\rho_2(u_1-u_2))\|_{H^{\gamma-1}}
 \le C_R\|\eta\|_{H^{\gamma-1}},
\]
when both densities have \(H^\gamma\) norm at most \(R\). The corresponding transport coefficients are controlled in \(H^{\gamma+1}\); this regularity is sufficient also when \(\gamma-1<0\), since \(\gamma>1/2\). The difference estimate gives convergence on a shorter common interval and uniqueness. Standard regularization of the energy estimate supplies strong \(H^\gamma\) continuity. Positivity and unit mass follow from the characteristic transport formula and the divergence form of the equation. These arguments establish a lifespan depending only on the norm bound and the fixed data.

They also justify the preceding a priori calculations by smoothing and passage to the limit: products and velocities converge in lower Sobolev orders, the entropy converges under uniform boundedness of the densities, and the dissipative norm is continuous in a sufficiently low Sobolev topology. Thus the energy inequalities and entropy identity apply to the stated Sobolev solution.

The bootstrap bounds \(\|\rho_t\|_{H^\gamma}\) uniformly up to any putative finite maximal time. Restarting the local construction sufficiently near that time, with the uniform lifespan just obtained, extends the solution beyond it. Therefore the maximal time is infinite, and (8) holds for every \(t\ge0\).

## 6. Sobolev Decay and Endpoints

The uniform \(H^\gamma\) bound and \(\gamma>d/2\) give a uniform upper bound \(\Lambda\) on \(\rho_t\) and \(\pi\), with the permitted dependence. Equation (3) therefore gives \(\|\sigma_t\|_2^2\le2\Lambda H_t\). For \(0\le\beta\le\gamma\), interpolation and the bootstrap bound yield
\[
 \|\sigma_t\|_{\dot H^\beta}^2
 \le \|\sigma_t\|_2^{2(1-\beta/\gamma)}X_t^{\beta/\gamma}
 \le C_\beta X_0^{\beta/\gamma}H_t^{1-\beta/\gamma}.
\]
Substitute (8) to obtain
\[
 \|\rho_t-\pi\|_{\dot H^\beta}^2
 \le C_\beta\|\bar\rho-\pi\|_{\dot H^\gamma}^{2\beta/\gamma}
 \left(H_0^{-(s-1)/\gamma}+t/C\right)^{-(\gamma-\beta)/(s-1)}.
\]
The endpoint \(\beta=0\) is the entropy-to-\(L^2\) estimate, and \(\beta=\gamma\) is the uniform high-order bound. The stationary case was already separated, so neither endpoint requires evaluating an indeterminate expression.

## Source Repair Ledger

The source's additive dissipation remainder is retained. Its bootstrap threshold \(2X_0\) is replaced by \(A_*X_0\), with a fixed data-dependent \(A_*\), to make the final strict inequality uniform under the claimed constant dependencies. This is a local proof repair of theory_002; no theorem assumption or conclusion is changed. All theorem-critical obligations above are closed.
