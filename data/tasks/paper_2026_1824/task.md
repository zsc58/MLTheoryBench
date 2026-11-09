# Problem

## Setup

Let M be a finite-dimensional Riemannian manifold, let I be an open interval containing 0, and let L:M x I -> R be C^k, where k>=4. Let bar{x}(mu) be a smooth branch of critical points. Write H_mu for the Riemannian Hessian of L at bar{x}(mu). Assume

\[
\ker H_0=\operatorname{span}\{v_0\},\qquad \|v_0\|=1,
\]

and that H_0 is invertible on N=v_0^perp. Let rho(mu) be the simple Hessian eigenvalue issuing from rho(0)=0, and assume

\[
\alpha:=\rho'(0)\ne0.
\]

Fix a smooth branch-centered local coordinate family Psi_mu from a neighborhood of 0 in T_{bar{x}(0)}M to M, with Psi_mu(0)=bar{x}(mu) and D Psi_0(0) the identity. Write its coordinates as a v_0+w, with w in N, and put

\[
\ell(a,w,\mu)=L\bigl(\Psi_\mu(a v_0+w),\mu\bigr).
\]

The following definitions specify the coefficient normalizations and the meaning of the reduced direction. Let w_*(a,mu) denote the local solution through w_*(0,0)=0 of

\[
D_w\ell(a,w_*(a,\mu),\mu)=0,
\]

and let

\[
\phi(a,\mu)=\ell(a,w_*(a,\mu),\mu),\qquad
\beta=\partial_a^3\phi(0,0),\qquad
\gamma=\partial_a^4\phi(0,0).
\]

The local existence, uniqueness, and differentiability needed for these definitions are to be justified in the proof. A minimum or maximum in the reduced direction means a local minimum or maximum of a -> phi(a,mu) at fixed mu.

Consider separately:

- **Generic case:** beta != 0.
- **Symmetric case:** phi(-a,mu)=phi(a,mu) for all sufficiently small (a,mu), and gamma != 0.

The Morse index of a nondegenerate critical point is the number of negative Hessian eigenvalues, counted with multiplicity. Here supercritical means that the nontrivial branches are reduced minima on the side where the trivial branch is unstable in the reduced direction; subcritical means that they are reduced maxima on the side where the trivial branch is stable in that direction.

## Task

Prove the following local classification, including the well-definedness of the quantities introduced above.

In the generic case, the nearby critical set consists exactly of the trivial branch bar{x}(mu) and a unique nontrivial branch crossing it at mu=0. The nontrivial branch is at least C^{k-2}, and its kernel coordinate satisfies

\[
a(\mu)=-\frac{2\alpha}{\beta}\mu+O(\mu^2).
\]

In the symmetric case, the nearby critical set consists of the trivial branch and, on the side where -6alpha mu/gamma>0, exactly two nontrivial branches with opposite kernel coordinates a_-(mu)=-a_+(mu). As mu tends to zero on that side,

\[
a_\pm(\mu)^2=-\frac{6\alpha}{\gamma}\mu+o(|\mu|).
\]

There are no nearby nontrivial critical points on the opposite side or at mu=0. Show that gamma>0 gives the supercritical case, with the bifurcating branches strict minima in the reduced direction, whereas gamma<0 gives the subcritical case, with strict maxima there.

Finally, in both cases show that the Morse index of the trivial branch changes by exactly one between sufficiently small negative and positive parameters.
