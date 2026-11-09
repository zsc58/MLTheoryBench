# Reference Proof

## Proof Structure

Compute the one-neuron tangent space after removing its scaling direction, identify the full differential image with the sum of the atom tangent spaces, and apply Terracini's lemma at the assumed generic configuration. Non-defectivity gives the identifiable dimension. Finally, use local submersion coordinates to integrate all redundant parameter directions and compute the RLCT of the regular identifiable loss.

## Complete Proof

Write \(\theta^*\) for the specified parameter point, \(y^*=\Phi(\theta^*)\), and \(x_j=v_j\otimes w_jw_j^\top\). All parameters and tangent spaces below are evaluated at this point unless indicated otherwise. Let
\[
N=K(p+d),\qquad r=\dim S_K.
\]

### 1. The One-Neuron Tangent Space and Dimension

For one neuron, differentiation of \(g(v,w)=v\otimes ww^\top\) gives
\[
Dg(\delta v,\delta w)=\delta v\otimes ww^\top+v\otimes(\delta w\,w^\top+w\,\delta w^\top).
\]
Write \(\delta w=u+c w\), with \(u\perp w\), and set \(\beta=\delta v+2cv\). Then
\[
Dg(\delta v,\delta w)=\beta\otimes ww^\top+v\otimes(uw^\top+wu^\top).
\]
Conversely, every pair \((\beta,u)\), with \(u\perp w\), is obtained by taking \(\delta v=\beta\) and \(\delta w=u\). The infinitesimal scaling direction \((\delta v,\delta w)=(-2cv,cw)\) lies in the kernel, consistently with the exact symmetry \((v,w)\mapsto(a^{-2}v,aw)\), \(a\ne0\).

To justify that this differential image is the full atom tangent space, choose coordinates \(i,k\) with \(w_i\ne0\) and \(v_k\ne0\). Normalize \(w_i=1\) by replacing \(w\) with \(w/w_i\) and \(v\) with \(w_i^2v\). If the atom has matrix components \(Q_a=v_a ww^\top\), the normalized parameters are recovered near this atom by
\[
v_a=(Q_a)_{ii},\qquad w_l=\frac{(Q_k)_{li}}{(Q_k)_{ii}}.
\]
The denominator is nonzero locally. These analytic inverse formulas show that the normalized parametrisation is a local chart of the nonzero atom cone. Therefore
\[
T_xA=\{\beta\otimes ww^\top+v\otimes(uw^\top+wu^\top):\beta\in\mathbb R^p,\ u\perp w\}.
\]

This space has dimension \(p+d-1\). Indeed, \(\beta\mapsto\beta\otimes ww^\top\) is injective, so its image has dimension \(p\). The map \(u\mapsto v\otimes(uw^\top+wu^\top)\) on \(w^\perp\) is injective: since \(v\ne0\), vanishing implies \(uw^\top+wu^\top=0\), and multiplication by \(w\) gives \(\|w\|^2u=0\). Its image thus has dimension \(d-1\). Finally,
\[
\langle uw^\top+wu^\top,ww^\top\rangle_F=0
\]
for \(u\perp w\). Contracting any equality between the two tensor summands against \(ww^\top\) shows that their intersection is zero.

### 2. The Network Differential and Secant Dimension

The neuron perturbations can be chosen independently, so
\[
\operatorname{Im}D\Phi_{\theta^*}=\sum_{j=1}^K T_{x_j}A.
\]
Removing the individual scaling directions does not change this image. It does not assert that scaling accounts for every redundancy of the whole network.

The standard independent geometric result used here is Terracini's lemma in its affine-cone form: for generic constituent points \(x_1,\ldots,x_K\) on an atom cone and a generic smooth sum \(y\) on its affine Kth secant cone,
\[
T_yS_K=\sum_{j=1}^K T_{x_j}A.
\]
The public hypotheses give nonzero atoms, algebraic genericity and general position of the constituent choices, and a generic smooth point \(y^*\). Thus the lemma applies, and
\[
\operatorname{Im}D\Phi_{\theta^*}=T_{y^*}S_K,\qquad \operatorname{rank}D\Phi_{\theta^*}=r.
\]
Smoothness ensures that this tangent dimension equals the affine dimension of \(S_K\).

There are \(d(d+1)/2\) independent entries in a symmetric \(d\times d\) matrix. Therefore the ambient coefficient space has dimension \(p d(d+1)/2\). The one-neuron dimension is \(p+d-1\), and the assumed non-defectivity gives
\[
r=\min\{K(p+d-1),\ p d(d+1)/2\}.
\]

### 3. Local Fibres and the LLC

The loss is the finite analytic excess KL
\[
\mathcal K(\vartheta)=D(\vartheta)-D(\theta^*)
=\widetilde D(\Phi(\vartheta))-\widetilde D(y^*).
\]
The induced map into the local smooth identifiable manifold \(M\) is a submersion. The local analytic submersion theorem gives coordinates \((z,t)\in\mathbb R^r\times\mathbb R^{N-r}\), centered at \(\theta^*\), and coordinates on \(M\), centered at \(y^*\), in which this map is \((z,t)\mapsto z\). Consequently \(\mathcal K\) is independent of \(t\).

Regularity at the minimum gives
\[
\widetilde D(z)-\widetilde D(0)=\tfrac12z^\top H z+O(\|z\|^3),\qquad H\succ0.
\]
Hence, on a sufficiently small neighborhood, there are constants \(0<c<C<\infty\) with
\[
c\|z\|^2\le\mathcal K(z,t)\le C\|z\|^2.
\]
The prior times the absolute Jacobian of the local coordinate change is positive and continuous. On a smaller closed product box it is bounded above and below by positive constants.

For completeness, the standard co-area result underlying this reduction states that for a \(C^1\) submersion \(\phi:X\to Y\) and nonnegative measurable \(h\),
\[
\int_X h\,dV_X=\int_Y\left(\int_{\phi^{-1}(y)}\frac{h}{J_\phi}\,dV_{\mathrm{fibre}}\right)dV_Y.
\]
Here the localized fibres are restricted to the chosen neighborhood, the submersion Jacobian is positive, and the integrands used for integrability tests are nonnegative measurable functions. In the product coordinates above, this is simply Fubini. Integration over a fixed small \(t\)-box gives a bounded positive weight in \(z\). If \(N-r=0\), this fibre factor is absent, with the same conclusion.

For a real exponent \(a>0\), the localized integral of \(\mathcal K^{-a}\) is therefore finite exactly when
\[
\int_{\|z\|<\epsilon}\|z\|^{-2a}\,dz
\]
is finite. Polar coordinates reduce this integral to a positive constant times
\[
\int_0^\epsilon \rho^{r-1-2a}\,d\rho,
\]
which is finite exactly for \(a<r/2\), and diverges at \(a=r/2\). Thus the local RLCT, equivalently the positive integrability threshold or minus the largest local zeta pole, is \(r/2\). This argument explicitly handles all local fibre directions and does not infer pole locations merely from comparability of complex-valued zeta integrals.

Combining this with the dimension calculation yields
\[
\boxed{\lambda=\frac12\min\{K(p+d-1),\ p d(d+1)/2\}.}
\]

## Obligation Closure

The atom chart, scaling reduction, one-atom dimension, differential-image equality, identifiable dimension, fibre integration, and quadratic integrability calculation are explicitly derived above. Terracini's lemma and the local submersion/co-area results are standard independent results whose relevant statements and hypotheses are specified. There is no unresolved paper-specific dependency. The argument includes \(d=1\), \(p=1\), \(K=1\), and equality of the two dimension branches.
