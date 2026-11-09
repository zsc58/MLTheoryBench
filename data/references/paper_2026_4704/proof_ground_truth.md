# Reference Proof

## Theorem-Critical Obligations

1. Verify normalization and moment domains, and prove existence and uniqueness of a radial KL minimizer without incorrectly treating the finite-second-moment class as globally weakly closed.
2. Identify the optimizer by spherical averaging and justify the stationary calculation without assuming an unknown minimizer is already positive.
3. Establish the full spatial Hessian bounds, including the origin.
4. Establish almost-everywhere uniqueness, the continuous radial representative, sufficient classical regularity on positive radii, and the two-sided first-derivative bounds.
5. Derive the correctly normalized radial change-of-variables equation, prove the required half-line mode-moment estimates, retain all conditioning-parameter factors, and close the second-derivative estimate with a universal constant.

The proof below closes all five obligations. Its only substantial external inputs are the two standard independent transport results recorded as theory_001 and theory_007:

- **Brenier's theorem, relevant form.** For an absolutely continuous source probability measure with finite second moment and a target probability measure with finite second moment, the quadratic-cost optimal map exists, is unique up to source-almost-everywhere equality, and is the gradient of a convex potential.
- **Caffarelli contraction, relevant Gaussian form.** If a target probability density on $\mathbb R^d$ has a $C^2$ potential $U$ satisfying $\ell I\preceq\nabla^2U\preceq LI$ with $0<\ell\le L<\infty$, its Brenier map from the standard Gaussian is $\ell^{-1/2}$-Lipschitz, and the reverse optimal map is $\sqrt L$-Lipschitz. Thus the forward map has Jacobian eigenvalues between $L^{-1/2}$ and $\ell^{-1/2}$ wherever differentiable. These are the two-sided bounds explicitly invoked in the supplied source at L000356-L000362.

All hypotheses of these inputs are verified below. The mode-moment estimate is derived directly rather than left as an additional cited obligation.

## 1. Normalization, Domains, Existence, and Uniqueness

Write $U(r)=\bar V(r)$ and $U(x)=U(\|x\|)$. Since $\nabla V(0)=0$, integration of the Hessian bounds along line segments gives
$$V(0)+\frac\ell2\|x\|^2\le V(x)\le V(0)+\frac L2\|x\|^2.$$
Averaging over the sphere gives the same inequalities for $U$. Consequently $Z$ and $Z_*$ are finite and strictly positive, and
$$\nu(dx):=Z_*^{-1}e^{-U(x)}\,dx$$
is a radial probability measure with finite second moment. Also $|V(x)-U(x)|\le (L-\ell)\|x\|^2/2$, so $\mathrm{KL}(\nu\|\pi)$ is finite.

For completeness, finite KL under these assumptions already implies a finite second moment, even if that moment was not imposed on the competing measure. Let $c=\ell/4$ and
$$M=\int e^{c\|x\|^2}\,d\pi(x)<\infty.$$
For $h_n(x)=c\min\{\|x\|^2,n\}$, compare $\mu$ with the probability measure proportional to $e^{h_n}\pi$. Nonnegativity of relative entropy gives
$$\int h_n\,d\mu\le\mathrm{KL}(\mu\|\pi)+\log\int e^{h_n}\,d\pi\le\mathrm{KL}(\mu\|\pi)+\log M.$$
Monotone convergence proves
$$c\int\|x\|^2\,d\mu\le\mathrm{KL}(\mu\|\pi)+\log M.$$
Thus restricting the source's radial probability class to finite-second-moment measures does not discard any finite-objective competitor. It also supplies the moment control needed if one uses the source's compactness route; global weak closedness of the finite-second-moment class itself is not needed or asserted here.

We prove existence and uniqueness directly using the same spherical averaging that underlies the source's variational calculation. If $\mu$ is radial and has finite KL to $\pi$, then it has a radial Lebesgue density, and $V$ and $U$ are integrable under $\mu$. Polar coordinates give
$$\int V\,d\mu=\int U\,d\mu.$$
Moreover,
$$\log\frac{d\nu}{d\pi}=V-U+\log Z-\log Z_*.$$
This logarithmic density ratio is integrable under $\mu$, so the relative-entropy change-of-reference identity is legitimate and yields
$$\mathrm{KL}(\mu\|\pi)=\mathrm{KL}(\mu\|\nu)+\log Z-\log Z_*.$$
It applies to $\mu=\nu$ as well, giving
$$\mathrm{KL}(\nu\|\pi)=\log Z-\log Z_*.$$
Therefore
$$\mathrm{KL}(\mu\|\pi)-\mathrm{KL}(\nu\|\pi)=\mathrm{KL}(\mu\|\nu)\ge0.$$
Nonnegativity and its equality condition follow by integrating $t\log t-t+1\ge0$ against the reference probability measure. Equality holds exactly when $\mu=\nu$. Competitors of infinite KL cannot improve on $\nu$.

Hence a unique minimizer exists and equals $\nu$. This also establishes the asserted density formula globally, rather than merely identifying a possible stationary point. Alternatively, once existence is established, uniqueness follows from strict convexity of relative entropy and convexity of the radial class.

## 2. Stationary Characterization

Here is the source's first-variation calculation with its normalization and positivity issue made explicit. For a positive radial density $q$, consider bounded, compactly supported radial variations
$$q_t(x)=q(x)(1+t\eta(x)),\qquad \int q\eta\,dx=0,$$
for sufficiently small $|t|$. Whenever $q$ has finite KL, the preceding moment bounds and the relative-entropy integrability ensure that these localized variations are legitimate. Differentiating and using spherical averaging gives
$$\left.\frac{d}{dt}\mathrm{KL}(q_t\,dx\|\pi)\right|_{t=0}=\int q(x)\eta(x)\bigl(\log q(x)+U(x)\bigr)\,dx.$$
The normalization constraint removes the additional constant from differentiating $q\log q$. Vanishing for all such normalized radial variations implies
$$\log q(r)+U(r)=\text{constant}$$
almost everywhere, and normalization gives $q=Z_*^{-1}e^{-U}$.

Section 1 already proves that this positive density is the global minimizer and excludes minimizers with vanishing density on positive-measure sets. Thus the first variation is not being used to assume positivity or to infer global optimality without justification.

## 3. Conditioning of the Averaged Potential

Differentiation under the spherical integral is valid because $V$ is $C^2$ and the sphere is compact. For $r\ge0$,
$$U'(r)=\int_{S^{d-1}}\langle\nabla V(r\theta),\theta\rangle\,d\sigma(\theta),$$
$$U''(r)=\int_{S^{d-1}}\theta^T\nabla^2V(r\theta)\theta\,d\sigma(\theta).$$
Thus $U'(0)=0$ and
$$\ell\le U''(r)\le L.$$
For $r>0$, integration gives
$$\ell\le\frac{U'(r)}r\le L.$$
Writing $e=x/\|x\|$, the spatial Hessian at $x\ne0$ is
$$\nabla^2U(x)=U''(r)ee^T+\frac{U'(r)}r(I-ee^T),\qquad r=\|x\|.$$
Its radial and tangential eigenvalues therefore lie in $[\ell,L]$.

There is no missing origin case. Spherical symmetry gives
$$U''(0)=\frac1d\operatorname{tr}(\nabla^2V(0)).$$
As $r\downarrow0$, both $U''(r)$ and $U'(r)/r$ converge to this same number. The radial gradient and Hessian formulas consequently extend continuously to the origin, with
$$\nabla U(0)=0,\qquad \nabla^2U(0)=U''(0)I.$$
Hence $U$ is $C^2$ on $\mathbb R^d$ and satisfies
$$\ell I\preceq\nabla^2U(x)\preceq LI\qquad(x\in\mathbb R^d).$$
The optimizer has exactly the required conditioning bounds.

## 4. The Optimal Radial Representative and Its First Derivative

The Gaussian source is absolutely continuous and has finite second moment, and Section 1 establishes the target's finite second moment. Brenier's theorem therefore applies.

Both measures are invariant under every orthogonal transformation. If $T=\nabla\varphi$ is optimal and $Q$ is orthogonal, then $Q^TT(Qx)$ is another admissible map with the same cost. Uniqueness gives equality almost everywhere. The convex potential can be taken finite on $\mathbb R^d$, since its domain has full Lebesgue measure and is convex. The convex potentials $\varphi(Qx)$ and $\varphi(x)$ have the same gradient almost everywhere and therefore differ by a constant; normalizing at the origin makes this constant zero. Thus $\varphi$ is radial. A radial convex potential has a nonnegative, nondecreasing radial derivative, so its transport map has a radial monotone profile almost everywhere.

To specify the representative and justify classical differentiation, let
$$A_\rho=\int_0^\infty r^{d-1}e^{-r^2/2}\,dr,\qquad A_*=\int_0^\infty s^{d-1}e^{-U(s)}\,ds,$$
and define the two radius densities on $(0,\infty)$ by
$$f_\rho(r)=A_\rho^{-1}r^{d-1}e^{-r^2/2},\qquad f_*(s)=A_*^{-1}s^{d-1}e^{-U(s)}.$$
Let $G$ and $H$ be their cumulative distribution functions. Monotonicity and transport of the radius laws identify the profile almost everywhere with
$$\Psi(r)=H^{-1}(G(r)),\qquad r>0.$$
Both densities are positive and $C^2$ on $(0,\infty)$. The inverse function theorem therefore makes this representative at least $C^2$ there, with positive derivative. It extends continuously by $\Psi(0)=0$, is strictly increasing, and tends to infinity. Hence setting $T(0)=0$ gives a continuous radial representative of the optimal map. No third derivative of $V$ is required.

Section 3 verifies the target Hessian assumptions for the Gaussian form of Caffarelli contraction stated above; the Gaussian potential has Hessian $I$. The forward and reverse Lipschitz bounds hold for the continuous representatives. Restricting the maps to a common ray gives, for $r,t\ge0$,
$$\frac{|r-t|}{\sqrt L}\le|\Psi(r)-\Psi(t)|\le\frac{|r-t|}{\sqrt\ell}.$$
Taking derivatives at positive radii yields
$$\frac1{\sqrt L}\le\Psi'(r)\le\frac1{\sqrt\ell}\qquad(r>0).$$
Taking $t=0$ also gives
$$\frac r{\sqrt L}\le\Psi(r)\le\frac r{\sqrt\ell}.$$

## 5. Second-Derivative Estimate

### Correct change of variables

Differentiating $G(r)=H(\Psi(r))$ gives the normalized mass identity
$$f_\rho(r)=f_*(\Psi(r))\Psi'(r).$$
Define
$$F_\rho(r)=\frac{r^2}{2}-(d-1)\log r,\qquad F_*(s)=U(s)-(d-1)\log s.$$
The mass identity is equivalently
$$F_\rho(r)=F_*(\Psi(r))-\log\Psi'(r)+\log\frac{A_*}{A_\rho}.$$
Consequently,
$$\frac{\Psi''(r)}{\Psi'(r)}=F_*'(\Psi(r))\Psi'(r)-F_\rho'(r).$$

### Modes and parameter-dependent derivative estimates

Let $a=\sqrt{d-1}$, the unique minimizer of $F_\rho$. Since $d\ge2$,
$$F_*''(s)=U''(s)+\frac{d-1}{s^2}\ge\ell,$$
while $F_*'(s)$ tends to $-\infty$ at zero and to $+\infty$ at infinity. Thus $F_*$ has a unique interior minimizer $b>0$, characterized by
$$U'(b)=\frac{d-1}{b}.$$
The bound $U'(b)\le Lb$ implies
$$b^2\ge\frac{d-1}{L}.$$
Using the second derivatives and integrating from the corresponding modes gives
$$|F_\rho'(r)|\le\left(1+\frac{d-1}{\min\{r,a\}^2}\right)|r-a|\le2\left(1+\frac d{r^2}\right)|r-a|,$$
$$|F_*'(s)|\le\left(L+\frac{d-1}{\min\{s,b\}^2}\right)|s-b|\le2\left(L+\frac d{s^2}\right)|s-b|.$$
The factor $L$ in the second estimate is essential. No normalization such as $L\le1$ or $L\ge1$ is assumed.

### Mode-moment estimate on the half-line

For either of the radius densities $p(s)=A^{-1}e^{-F(s)}$, let $m>0$ be its mode, and suppose $F''\ge\alpha>0$. Here the two pairs are $(F,m,\alpha)=(F_\rho,a,1)$ and $(F_*,b,\ell)$.

Strong convexity and $F'(m)=0$ give
$$\alpha(s-m)^2\le(s-m)F'(s).$$
Because $d\ge2$, the density is $O(s^{d-1})$ at zero, so $(s-m)p(s)\to0$ there. Quadratic growth of the underlying potential makes the same boundary term vanish at infinity. The integral below is also absolutely convergent: near zero its possible singularity is of order $s^{d-2}$, and at infinity it is controlled by a Gaussian tail. Since $p'=-F'p$, integration by parts yields
$$\mathbb E[(S-m)F'(S)]=-\int_0^\infty(s-m)p'(s)\,ds=1.$$
It follows that
$$\mathbb E(S-m)^2\le\frac1\alpha.$$
In particular, if $R$ has density $f_\rho$ and $S=\Psi(R)$ has density $f_*$, then
$$\mathbb E|R-a|\le1,\qquad\mathbb E|S-b|\le\frac1{\sqrt\ell}.$$
The Lipschitz estimate from Section 4 now gives
$$|\Psi(a)-b|\le\mathbb E|\Psi(a)-\Psi(R)|+\mathbb E|\Psi(R)-b|\le\frac2{\sqrt\ell}.$$
Therefore, with $\delta=|r-a|$,
$$|\Psi(r)-b|\le\frac{\delta+2}{\sqrt\ell}.$$
This proves the source's auxiliary mode estimate without an unresolved external concentration claim.

### Closing the bound

Set $B(r)=1+d/r^2$. From $\Psi(r)\ge r/\sqrt L$,
$$L+\frac d{\Psi(r)^2}\le L B(r).$$
Substitution into the differentiated mass identity gives
$$\frac{|\Psi''(r)|}{\Psi'(r)}\le2B(r)\delta+2\Psi'(r)L B(r)\frac{\delta+2}{\sqrt\ell}\le2B(r)\bigl[\delta+\kappa(\delta+2)\bigr].$$
Since $\kappa\ge1$ and $\Psi'\le\ell^{-1/2}$,
$$|\Psi''(r)|\le\frac{4\kappa}{\sqrt\ell}B(r)(1+|r-\sqrt{d-1}|).$$
Finally, $0<\sqrt d-\sqrt{d-1}<1$, so
$$1+|r-\sqrt{d-1}|\le2(1+|r-\sqrt d|).$$
Thus
$$|\Psi''(r)|\le8\frac{\kappa}{\sqrt\ell}\left(1+\frac d{r^2}\right)\left(1+|r-\sqrt d|\right)\qquad(r>0).$$
This establishes the requested conclusion with the universal choice $C=8$.

## Source-Local Repair and Closure

At source L000355, strict monotonicity must refer to $\Psi$, not to $\psi(r)=\Psi(r)/r$. The latter need not be strictly monotone, including for an isotropic Gaussian target. The proof uses only strict increase of $\Psi$ and the stated bounds on $\psi$; no monotonicity of $\psi$ is used. This notation repair is recorded under theory_008 and in provenance.applied_source_repairs.

All theorem-critical obligations are closed. In particular, the proof covers $d=2$, arbitrary positive conditioning scales, the origin for the averaged spatial potential, and all positive radii for the transport derivatives. There is no unresolved private ground-truth obligation.
