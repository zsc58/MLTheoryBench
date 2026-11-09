# Problem

## Setup

Let \(Z\) be a finite-dimensional Euclidean representation space and \(H\) a finite-dimensional Euclidean head-output space. Fix \(z\in Z\), and let \(U\subseteq\mathbb R^m\) be an open neighborhood of \(0\). Let \(h:Z\to H\) be \(C^1\) near \(z\), and let a continuous-augmentation map \(A:Z\times U\to Z\) be \(C^1\) near \((z,0)\), with \(A(z,0)=z\).

Define the augmentation-tangent space at \(z\) by
\[
V_{\mathrm{aug}}(z)
=\operatorname{span}\left\{\left.\frac{d}{dt}\right|_{t=0} A(z,\alpha(t)):
\alpha(0)=0,\ \alpha(t)\in U\right\},
\]
where the span ranges over differentiable parameter curves defined on an interval about \(0\). Write \(J_h=D h(z)\) and define the pullback metric \(G(z)=J_h^\top J_h\).

Assume exact local invariance: for every \(\xi\in U\) sufficiently close to \(0\),
\[
h(A(z,\xi))=h(z).
\]

For the local information model, define the augmentation sensitivities
\[
S_z=D_\xi A(z,0),
\qquad
S_h=\left.D_\xi\bigl[h(A(z,\xi))\bigr]\right|_{\xi=0}.
\]
Use the normalized local additive-isotropic-observation-noise approximation in which the Fisher information matrices with respect to the continuous augmentation parameter \(\xi\), evaluated at \(\xi=0\), are
\[
I_z=S_z^\top S_z,
\qquad
I_h=S_h^\top S_h.
\]
For the information-rank claim, assume \(\dim V_{\mathrm{aug}}(z)>0\).

## Task

Prove that exact local invariance forces
\[
V_{\mathrm{aug}}(z)\subseteq\ker J_h,
\]
and hence the pullback metric \(G(z)\) is singular on every nonzero augmentation direction. Prove moreover that the head information has the rank deficit
\[
\operatorname{rank}(I_h)
\le \operatorname{rank}(I_z)-\dim V_{\mathrm{aug}}(z).
\]
