# Reference Proof

## Audited background and obligations

We use the finite-dimensional implicit function theorem: for a C^r equation E(x,y)=0, r>=1, an invertible y-derivative at a zero gives a unique local C^r solution y=f(x), and every nearby zero lies on its graph. Its derivative follows by differentiating E(x,f(x))=0. This is the standard independent result recorded as theory_018.

The obligations are: establish the stationary-value definitions and exact critical-point correspondence; identify the mixed coefficient with the normalized eigenvalue crossing speed; prove the exhaustive transcritical classification and its remainder; prove the exhaustive symmetric classification at the stated finite regularity; and establish reduced stability and the full index change. All are proved below.

## 1. Coordinates and stationary values

Use the normalized branch-centered chart in the task, and write its pulled-back objective as ell(a,w,mu), w in N. All derivatives here are ordinary coordinate derivatives of this scalar function; we do not treat arbitrary chart components of the Riemannian gradient as a Euclidean gradient.

At the origin, D_w ell=0 and C_0=D^2_{ww}ell is invertible, because the chart identifies N with the nonsingular Hessian complement. The implicit function theorem therefore gives a unique local C^{k-1} function w_*(a,mu) satisfying D_w ell=0. Since the distinguished branch is critical, uniqueness gives w_*(0,mu)=0.

Define phi(a,mu)=ell(a,w_*(a,mu),mu). The chain rule gives

phi_a=ell_a(a,w_*,mu),    phi_mu=ell_mu(a,w_*,mu),

because D_w ell=0 on the graph. Both right-hand sides are C^{k-1}, so phi is C^k. Set g=phi_a, which is C^{k-1}. A point is critical for L exactly when all coordinate derivatives of ell vanish. The transverse derivatives already vanish on the graph, so nearby critical points correspond exactly to zeros of g. Also g(0,mu)=0.

## 2. Coefficients and crossing speed

Along the trivial branch, write the coordinate Hessian in blocks as

A(mu) = [[d(mu), b(mu)^T], [b(mu), C(mu)]].

Here d=ell_aa, b=ell_wa, and C=ell_ww, evaluated at (0,0,mu). At mu=0, d(0)=0, b(0)=0, and C(0) is invertible. Differentiating the transverse equation gives w_{*,a}(0,mu)=-C(mu)^{-1}b(mu). Hence

g_a(0,mu)=d(mu)-b(mu)^T C(mu)^{-1}b(mu).

In particular, g_a(0,0)=0 and g_{a mu}(0,0)=d'(0).

We verify d'(0)=alpha. Choose a smooth orthonormal frame along the critical branch. In this frame let B(mu) be the Riemannian Hessian and let z(mu) be the coordinate a-vector. Criticality implies d(mu)=z(mu)^T B(mu)z(mu). Chart normalization gives z(0)=v_0, and B(0)v_0=0, so d'(0)=v_0^T B'(0)v_0.

For completeness, the simple eigenpair is differentiable: apply the IFT to B(mu)e-rho e=0 together with (||e||^2-1)/2=0 at (mu,e,rho)=(0,v_0,0). The derivative in (e,rho) maps (delta e,delta rho) to (B(0)delta e-delta rho v_0, <v_0,delta e>), and is invertible by the kernel/complement splitting. Differentiating the eigenpair equation and pairing with v_0 gives rho'(0)=v_0^T B'(0)v_0. Thus g_{a mu}(0,0)=alpha.

By the definitions in the task, g_{aa}(0,0)=beta and g_{aaa}(0,0)=gamma.

## 3. Generic branch

Since g(0,mu)=0, define

h(a,mu)=integral_0^1 g_a(ta,mu) dt.

Then g(a,mu)=a h(a,mu), h is C^{k-2}, and

h(0,0)=0,    h_mu(0,0)=alpha,    h_a(0,0)=beta/2.

When beta is nonzero, the IFT solves h=0 uniquely as a=A(mu), with A of class C^{k-2}. Since k>=4, A is C^2. Differentiating gives A'(0)=-2alpha/beta, and Taylor's theorem yields

A(mu)=-(2alpha/beta)mu+O(mu^2).

The nonzero slope ensures A(mu) is nonzero for sufficiently small nonzero mu. Every zero of g has either a=0 or h=0; consequently the trivial branch and this branch exhaust the local critical set. Their distinct tangents give the claimed crossing.

## 4. Symmetric branches without an unjustified squared-variable IFT

In the symmetric case phi is even in a, so g is odd and h is even. In particular beta=0. Since h is C^{k-2}, it is at least C^2, and differentiating its integral definition gives

h_mu(0,0)=alpha,    h_a(0,0)=0,    h_{aa}(0,0)=gamma/3.

Apply the IFT using h_mu(0,0) != 0. Its complete local zero set is mu=m(a), where m is C^{k-2}. Evenness and uniqueness imply m(-a)=m(a). Differentiating h(a,m(a))=0 once and twice at zero gives

m(0)=m'(0)=0,    m''(0)=-gamma/(3alpha).

Therefore

m(a)=-gamma a^2/(6alpha)+o(a^2),

m'(a)=-gamma a/(3alpha)+o(a).

Since alpha and gamma are nonzero, m is strictly monotone on a sufficiently small positive half-interval. Its image is a one-sided parameter interval with sign -gamma/alpha. Every sufficiently small nonzero mu on that side has exactly one positive solution and, by evenness, exactly one negative solution. There are no nonzero solutions on the opposite side or at mu=0, after the neighborhood is reduced. Inverting the first expansion gives

a_+(mu)^2=a_-(mu)^2=-(6alpha/gamma)mu+o(|mu|).

Also a_-(mu)=-a_+(mu). These are smooth in the available finite-regularity sense on their open existence side; the combined curve is parameterized by a through mu=m(a). No differentiability of a square-root graph at mu=0 is asserted. Exact critical-point correspondence lifts them to the stated critical branches.

## 5. Stability and Morse index

On the trivial branch,

phi_{aa}(0,mu)=g_a(0,mu)=alpha mu+o(|mu|).

On a nontrivial symmetric branch, h=0 and therefore g_a=a h_a. Evenness gives h_a(0,mu)=0. Continuity of h_{aa} gives

h_a(a,mu)=a integral_0^1 h_{aa}(ta,mu) dt=(gamma/3)a+o(|a|)

as (a,mu) tends to zero. Consequently, on the nontrivial branches,

phi_{aa}=g_a=(gamma/3)a^2+o(a^2)=-2alpha mu+o(|mu|).

Its sign is gamma. Thus gamma>0 gives strict reduced minima on the side where the trivial reduced direction is unstable; gamma<0 gives strict reduced maxima on the side where the trivial reduced direction is stable. These are respectively the supercritical and subcritical alternatives under the task's convention.

Finally, at any nearby critical point the transverse Hessian block C remains invertible. Its number q of negative eigenvalues is constant locally. If the full coordinate Hessian has blocks d,b,C, differentiating the transverse stationarity equation gives phi_{aa}=d-b^T C^{-1}b. Its quadratic form is

(w+C^{-1}b a)^T C(w+C^{-1}b a)+(d-b^T C^{-1}b)a^2.

The displayed invertible change of variables shows directly that its index is q plus one when phi_{aa}<0 and q when phi_{aa}>0. Coordinate changes preserve the inertia of the Hessian at a critical point. On the trivial branch alpha mu+o(|mu|) has opposite signs on the two sides, so the full Morse index changes by exactly one. This argument applies in both cases. It also confirms that reduced minima need not be full minima when q>0.

If dim M=1, N is the zero-dimensional space: the transverse equation is vacuous, q=0, and the same proof applies with empty transverse blocks. No unresolved proof obligation remains.
