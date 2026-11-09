# Reference Proof

## Proof structure and obligations

The proof reduces the activation to ReLU hinges, canonicalizes the realized function on its domain, isolates individual kinks to bound canonical coefficients, derives weight-independent uniform entropy, proves a finite-class noisy-fitting estimate, and balances entropy against concentration after Gaussian localization. The following proof closes each of these obligations. All nets used in the probabilistic argument are fixed independently of the observed sample.

Write \(r=(K-1)m\) and \(M=r+1\). Since \(|y|\le1\),
\[
0<\sigma^2=\mathbb E\operatorname{Var}(y\mid x)\le\mathbb E y^2\le1.
\]
Constants denoted by \(C,c\) are positive absolute constants and may change between occurrences.

## 1. Reduction to ReLU hinges

If \(K=1\), the activation is affine, so every network in the public class is affine and requires no hinges. Otherwise \(K\ge2\). Let \(\tau_1<\cdots<\tau_{K-1}\) be the breakpoints and \(s_0,\ldots,s_{K-1}\) the successive slopes. Then
\[
\phi(t)=\phi(\tau_1)+s_0(t-\tau_1)
 +\sum_{k=1}^{K-1}(s_k-s_{k-1})(t-\tau_k)_+.
\]
Indeed, both sides agree at \(\tau_1\), are continuous, and have the same slope on each interval between successive breakpoints. Substitution into each hidden unit and absorption of the affine residuals into the skip connection gives an affine function plus at most \(r\) ReLU hinges, identically on \(\mathbb R^d\).

## 2. Domain-wise canonicalization

A unit with zero input weight is constant. For every other unit, positive homogeneity normalizes its direction to a unit vector. The identity
\[
(-z)_+=(z)_+-z
\]
permits orientation reversal, with the difference absorbed into the affine term.

On \(B_2\), a normalized hinge with threshold \(t\ge2\) vanishes, and one with \(t\le-2\) is affine. On the sphere, orient each hinge so that \(t\ge0\), and discard those with \(t\ge1\). Choose a consistent orientation for coincident hyperplanes, including hyperplanes through the origin, merge their coefficients, and delete zero combined coefficients. Consequently, on the relevant domain,
\[
f(x)=\langle v,x\rangle+c+
 \sum_{j=1}^{r_0}\alpha_j(\langle u_j,x\rangle-t_j)_+,
\qquad r_0\le r,
\]
where \(\|u_j\|=1\), the remaining coefficients are nonzero, the kink hyperplanes are pairwise distinct, and
\[
t_j\in(-2,2)\quad\text{on }B_2,
\qquad t_j\in[0,1)\quad\text{on }\mathbb S^{d-1}.
\]
These identities are required only on the stated domain; no control of the original parameters has been imposed.

## 3. Rigidity of individual kinks

Suppose \(\operatorname{Lip}_D(f)\le L\).

### Ball

For a fixed kink hyperplane \(H_j\), its intersection with the interior of \(B_2\) is a nonempty relatively open disk. Each other distinct hyperplane intersects it in a set of relative measure zero. Choose \(x_*\) in this disk and on no other kink. In a neighborhood of \(x_*\), every other summand is affine. The restriction along \(x_*+su_j\) therefore has one-sided slopes \(\beta\) and \(\beta+\alpha_j\). Both belong to \([-L,L]\), so
\[
|\alpha_j|\le2L.
\]

### Sphere

Put \(\rho_j=\sqrt{1-t_j^2}>0\). The kink set \(H_j\cap\mathbb S^{d-1}\) is a positive-radius \((d-2)\)-sphere. For \(d\ge3\), it affinely spans \(H_j\); its intersection with any other distinct hyperplane is a lower-dimensional sphere, a point, or the empty set. Such finitely many intersections cannot cover it. Choose \(x_*\) outside all other kinks and set
\[
\xi=\frac{u_j-t_jx_*}{\rho_j}.
\]
Then \(\|\xi\|=1\), \(\langle\xi,x_*\rangle=0\), and \(\langle u_j,\xi\rangle=\rho_j\). Along the unit-speed great circle
\[
\gamma(s)=\cos(s)x_*+\sin(s)\xi,
\]
the selected preactivation crosses zero with derivative \(\rho_j\). All other summands are differentiable there, so the derivative jump of \(f\circ\gamma\) is \(\alpha_j\rho_j\). Since
\(\|\gamma(s)-\gamma(s')\|\le|s-s'|\), this restriction is \(L\)-Lipschitz. Its one-sided derivatives lie in \([-L,L]\), yielding
\[
|\alpha_j|\sqrt{1-t_j^2}\le2L.
\]
This isolation argument supplies bounds on the canonical coefficients without any bound on the original weights.

## 4. Value and affine-parameter bounds

If the empirical error is at most \(\sigma^2-\varepsilon\le1\) and all samples lie in \(D\), some sample has \(|f(x_i)-y_i|\le1\), hence \(|f(x_i)|\le2\). Thus
\[
\|f\|_{\infty,D}\le2+L\operatorname{diam}(D)\le B_0:=2+4L.
\]

More generally, consider any canonical realization satisfying this uniform bound and \(\operatorname{Lip}_D(f)\le L\). On the ball, at an interior point off all hyperplanes,
\[
\nabla f=v+\sum_{j\text{ active}}\alpha_j u_j,
\qquad \|\nabla f\|\le L.
\]
The coefficient bounds and evaluation at zero imply
\[
\|v\|\le L(1+2r_0),
\qquad |c|\le B_0+4Lr_0.
\]

On the sphere, rotational symmetry gives \(\mathbb Ex=0\), \(\mathbb Exx^\top=I_d/d\), and
\[
\mathbb E[(\langle u,x\rangle-t)_+x]=\lambda(t)u,
\quad
\lambda(t)=\mathbb E[(\langle u,x\rangle-t)_+\langle u,x\rangle].
\]
For \(t\in[0,1)\), \(0\le\lambda(t)\le1-t\). Spherical rigidity therefore gives both
\[
|\alpha_j|\lambda(t_j)\le2L,
\qquad |\alpha_j|(1-t_j)\le2L.
\]
Taking \(\mathbb E[f(x)x]\) in the canonical representation, and then evaluating that representation at any sphere point, yields
\[
\|v\|\le d(B_0+2Lr_0),
\qquad |c|\le B_0+\|v\|+2Lr_0.
\]
These arguments apply to every finite hinge budget, including zero hinges.

## 5. Weight-independent uniform entropy

For \(L>0\), let \(\mathcal A_{M,L}\) consist of restrictions to \(D\) of affine-plus-ReLU realizations with at most \(M\) hinges, Lipschitz constant at most \(L\), and uniform norm at most \(B_0=2+4L\). The preceding arguments put this class inside the canonical parameter superclass with the corresponding coefficient and affine bounds, with the hinge count replaced by \(M\).

We prove that, for \(0<\eta<4+8L\), this superclass has an external uniform \(\eta\)-cover satisfying
\[
\log N\le C Md\log\!\left(\frac{CMd(2+L)}{\eta}\right).
\tag{1}
\]
We use the standard-independent volumetric bounds indexed by theory_026: a radius-\(A\) Euclidean ball in \(\mathbb R^d\) has an \(h\)-net of size at most \((1+2A/h)^d\), and the unit sphere has an \(h\)-net of size at most \((1+2/h)^d\). An interval of length \(A\) admits a mesh with at most \(2+A/h\) points and approximation error at most \(h\). The parameter ranges below verify the hypotheses of these bounds.

### Ball covering

For a single ridge, with both coefficients in \([-2L,2L]\),
\[
\|\alpha(\langle u,\cdot\rangle-t)_+
 -\alpha'(\langle u',\cdot\rangle-t')_+\|_{\infty,B_2}
\le4|\alpha-\alpha'|+2L(2\|u-u'\|+|t-t'|).
\]
Use coefficient mesh \(\eta/(32M)\), threshold mesh \(\eta/(32LM)\), and direction-net radius \(\eta/(64LM)\). Their total error is at most \(\eta/(4M)\) per ridge. Each scalar grid has at most \(2+CLM/\eta\) points, and the direction net has at most \((1+CLM/\eta)^d\) points.

The affine ranges satisfy \(\|v\|,|c|\le CMd(2+L)\). Approximate \(v\) within \(\eta/16\) and \(c\) within \(\eta/8\); their combined function error on \(B_2\) is at most \(\eta/4\). Multiplying these grid sizes and summing over the possible hinge counts \(0,\ldots,M\) proves (1). Indeed, the number of scalar parameter coordinates is \(O(Md)\), and every logarithmic grid factor is bounded by a constant times \(\log(CMd(2+L)/\eta)\).

### Spherical covering

Bulk hinges with \(t\le1/2\) satisfy \(|\alpha|\le3L\), so the preceding sensitivity and grid argument applies after adjusting absolute constants.

For a cap hinge with \(t>1/2\), write \(\gamma=\sqrt{1-t}\). Then
\[
|\alpha|\le\frac{2L}{\gamma},
\qquad
\|\alpha(\langle u,\cdot\rangle-t)_+\|_\infty
=|\alpha|\gamma^2\le2L\gamma.
\tag{2}
\]
Delete hinges with \(\gamma\le\gamma_{\min}:=\eta/(64LM)\). Their total uniform contribution is at most \(\eta/32\). If \(\gamma_{\min}\ge1/\sqrt2\), no cap hinge survives.

Otherwise divide the surviving \(\gamma\)-range into dyadic bins with lower endpoints \(a\ge\gamma_{\min}\). In a bin \(a\le\gamma\le2a\), the coefficient magnitude is at most \(2L/a\), the unscaled hinge has norm at most \(4a^2\), and the threshold interval has length at most \(3a^2\). Use meshes
\[
h_\alpha=\frac{\eta}{128Ma^2},
\qquad h_t=\frac{\eta a}{64LM},
\qquad h_u=\frac{\eta a}{128LM}.
\]
Choose coefficient-grid centers within \([-2L/a,2L/a]\), threshold centers within the bin's threshold interval, and direction centers on the unit sphere. The sensitivity inequality gives error at most
\[
4a^2h_\alpha+\frac{2L}{a}(h_t+h_u)
=\frac{5\eta}{64M}<\frac{\eta}{8M}.
\]
The two scalar grid sizes are each at most \(2+CLMa/\eta\). The direction-net size is at most
\[
\left(1+\frac{CLM}{\eta a}\right)^d
\le\left(1+C(LM/\eta)^2\right)^d,
\]
because \(a\ge\eta/(64LM)\). Thus every bin has logarithmic cardinality at most \(C(d+2)\log(2+LM/\eta)\). The number of bins is at most \(C\log(2+LM/\eta)\); enumerating bulk, bin, or deleted status for each of at most \(M\) hinges adds at most \(CM\log(2+LM/\eta)\) to the logarithmic count.

The spherical affine bounds again give ranges \(\|v\|,|c|\le CMd(2+L)\). Their grids contribute at most \(C(d+1)\log(CMd(2+L)/\eta)\). The total approximation error, including deletion and affine approximation, is less than \(\eta\), proving (1). Centers need not satisfy the original threshold-dependent coefficient constraint: this is an external cover. The scale restriction on \(\eta\) allows the absolute constant in the logarithm to make its argument at least \(e\).

### Internal net

Take an external \(\eta/2\)-cover of the superclass. Greedily choose points in \(\mathcal A_{M,L}\) with pairwise distances strictly greater than \(\eta\). Each covering ball contains at most one chosen point, so the procedure stops after finitely many choices. At termination every member of \(\mathcal A_{M,L}\) is within \(\eta\) of a chosen point. This produces an internal net \(\mathcal S\subset\mathcal A_{M,L}\) with
\[
\log|\mathcal S|\le CMd\log\!\left(\frac{CMd(2+L)}{\eta}\right).
\tag{3}
\]

## 6. Concentration tools

Define
\[
\|Z\|_{\psi_2}=\inf\{s>0:\mathbb E\exp(Z^2/s^2)\le2\}.
\]
The standard-independent sphere and Gaussian concentration results indexed by theory_027 have the following relevant forms. On the sphere of radius \(\sqrt d\), a bounded \(b\)-Lipschitz function has centered \(\psi_2\)-norm at most \(Cb\), uniformly for \(d\ge2\). The same statement holds under the standard Gaussian law on \(\mathbb R^d\). Applying these statements to \(z\mapsto q(z/\sqrt d)\) gives an absolute \(\kappa\ge1\) such that, for both input laws and every bounded Lipschitz function on the support,
\[
\|q(x)-\mathbb Eq(x)\|_{\psi_2}
\le\frac{\kappa\operatorname{Lip}(q)}{\sqrt d}.
\tag{4}
\]
The spherical model has \(d\ge3\), and the Gaussian dimension hypothesis in particular ensures a positive admissible dimension.

We also use these standard-independent forms of theory_032:

- For iid variables in an interval of length \(b\), either one-sided deviation of their empirical average by \(t>0\) has probability at most \(\exp(-2nt^2/b^2)\); the two-sided bound has an additional factor two.
- If independent centered variables have \(\psi_2\)-norm at most \(b>0\), then \(\mathbb P(n^{-1}\sum_i V_i\ge t)\le\exp(-cnt^2/b^2)\).
- If \(X\sim\chi_d^2\), then \(\mathbb P(X\ge4d)\le\exp(-(3-\log4)d/2)\le e^{-d/2}\).

Every use below verifies boundedness or the required norm bound and independence.

## 7. Finite-class noisy-fitting bound

Let \(\mathcal Q\) be a deterministic finite collection of \([-1,1]\)-valued functions on the input support, each with Lipschitz constant at most \(L>0\). For \(0<a\le\sigma^2\), we prove
\[
\mathbb P\!\left\{\exists q\in\mathcal Q:
\frac1n\sum_i(q(x_i)-y_i)^2\le\sigma^2-a\right\}
\le4e^{-na^2/512}
+|\mathcal Q|\exp\!\left[-c_2na^2
\max\!\left\{1,\frac d{\kappa^2L^2}\right\}\right]
\tag{5}
\]
for an absolute \(c_2>0\).

Set \(g(x)=\mathbb E[y\mid x]\) and \(z=y-g(x)\). Then \(|g|\le1\), \(|z|\le2\), \(\mathbb E[z\mid x]=0\), and \(\mathbb Ez^2=\sigma^2\). Write \(P_n\) for the sample average. The variables \(z_i^2\in[0,4]\) and \(z_i g(x_i)\in[-2,2]\) are iid, with means \(\sigma^2\) and zero respectively. Hoeffding gives, outside an event of probability at most \(2e^{-na^2/288}\),
\[
P_nz^2\ge\sigma^2-a/6,
\qquad P_n(zg)\ge-a/6.
\]
On this common event, a fitting function satisfies
\[
\sigma^2-a\ge P_n(q-g-z)^2
=P_n(q-g)^2-2P_n(zq)+2P_n(zg)+P_nz^2
\ge-2P_n(zq)+\sigma^2-a/2.
\]
Consequently \(P_n(zq)\ge a/4\).

For each fixed \(q\), decompose
\[
P_n(zq)=P_nW+(\mathbb Eq)P_nz,
\qquad W_i=z_i(q(x_i)-\mathbb Eq).
\]
The \(W_i\) are iid and centered, because \(\mathbb E[z_i\mid x_i]=0\). They obey \(|W_i|\le4\), and (4), together with \(|z_i|\le2\), gives
\[
\|W_i\|_{\psi_2}\le C\min\{1,\kappa L/\sqrt d\}.
\]
The independent sub-Gaussian sum bound therefore yields
\[
\mathbb P(P_nW\ge a/8)
\le\exp\!\left[-c_2na^2\max\{1,d/(\kappa^2L^2)\}\right].
\]
For the mean term, \(|\mathbb Eq|\le1\) implies that the event \((\mathbb Eq)P_nz\ge a/8\) for any member of the class is contained in \(\{|P_nz|\ge a/8\}\). Thus this term is controlled uniformly, without a class-cardinality factor, by \(2e^{-na^2/512}\). Union-bound only the centered terms over \(\mathcal Q\), and add the noise-decomposition failure probability. Since \(288<512\), the resulting bound is (5). This argument allows arbitrary dependence between the label and its input.

## 8. Localization, net reduction, and final balance

Choose constants later and put
\[
\ell=\log(C_0Mnd/\varepsilon),
\qquad
L_*=c_0\varepsilon\sqrt{\frac n{M\ell}}.
\tag{6}
\]
Take \(C_0\ge e\), so \(\ell\ge1\) and \(L_*>0\).

### Localization and extension

In the Gaussian case, \(d\|x_i\|^2\sim\chi_d^2\). Hence the chi-square bound and the stated dimension condition imply
\[
\mathbb P(E_{\rm loc}^c)
\le ne^{-d/2}\le\delta/8,
\qquad E_{\rm loc}=\{x_i\in B_2\text{ for all }i\}.
\tag{7}
\]
On the sphere, let \(E_{\rm loc}\) be the sure event.

Let \(\pi\) be Euclidean projection onto \(B_2\) in the Gaussian case, and the identity on the sphere otherwise. Projection is nonexpansive: if \(p=\pi(x)\), then \(\langle x-p,z-p\rangle\le0\) for all \(z\in B_2\), as follows by differentiating squared distance along the segment from \(p\) to \(z\). Applying this inequality to \(p=\pi(x)\) and \(q=\pi(x')\) gives \(\|p-q\|^2\le\langle x-x',p-q\rangle\), hence \(\|p-q\|\le\|x-x'\|\).

If a fitting network has \(\operatorname{Lip}_D(f)\le L_*\), then on \(E_{\rm loc}\) the value bound places \(f|_D\) in \(\mathcal A_{M,L_*}\). This also covers affine networks and networks whose actual Lipschitz constant is zero.

### Deterministic net reduction

Fix an internal \(\eta\)-net \(\mathcal S\) of this class with \(\eta=\varepsilon/32\). Its existence and size follow from (3); the required scale condition holds because \(\varepsilon\le1\). Form the deterministic finite class
\[
\mathcal Q=\{\operatorname{clip}\circ h\circ\pi:h\in\mathcal S\}.
\]
Its functions are defined on the full input support, are \([-1,1]\)-valued, and have Lipschitz constant at most \(L_*\).

For a putative fitting \(f\), choose \(h\in\mathcal S\) within \(\eta\) on \(D\). Clipping is nonexpansive and cannot increase squared loss against labels in \([-1,1]\). Moreover, for \(a,b,y\in[-1,1]\),
\[
|(a-y)^2-(b-y)^2|=|a-b|\,|a+b-2y|\le4|a-b|.
\]
On \(E_{\rm loc}\), the corresponding member of \(\mathcal Q\) therefore has empirical error at most
\[
\sigma^2-\varepsilon+4\eta\le\sigma^2-\varepsilon/2.
\]
This is an event inclusion, not conditioning the concentration estimate on localization. In particular the original iid law remains available when applying (5).

### Entropy and probability budget

Write \(E=\log|\mathcal S|\). For \(c_0\le1\), (6) gives \(L_*\le\varepsilon\sqrt n\le\sqrt n\). Consequently \(2+L_*\le3\sqrt n\). Taking \(C_0\) sufficiently large in comparison with the absolute constants in (3) gives
\[
E\le C_E Md\ell
\tag{8}
\]
for an absolute \(C_E\).

Apply (5) with \(a=\varepsilon/2\) and \(L=L_*\). Define
\[
T=n\varepsilon^2,
\qquad H=\max\{1,d/(\kappa^2L_*^2)\}.
\]
The fitting event for the finite class has probability at most
\[
4e^{-T/2048}+\exp(E-c_2TH/4).
\tag{9}
\]
Choose \(c_0\) so small that
\[
c_0^2\le\frac{c_2}{8\kappa^2C_E}.
\tag{10}
\]
If \(L_*\le\sqrt d/\kappa\), substitution of (6) gives
\[
TH=\frac{Md\ell}{\kappa^2c_0^2},
\qquad E\le c_2TH/8.
\]
If \(L_*>\sqrt d/\kappa\), the case hypothesis instead gives
\[
Md\ell<\kappa^2c_0^2T,
\]
so (8) and (10) again imply \(E\le c_2TH/8\), now with \(H=1\). Thus both regimes leave a residual exponent:
\[
E-c_2TH/4\le-c_2TH/8\le-c_2T/8.
\tag{11}
\]
Finally enlarge \(C_0\), if necessary, so that \(C_0\ge2048\) and \(C_0\ge8/c_2\), as well as the previous absolute requirements. The sample-size hypothesis makes the first term of (9) at most \(\delta/2\), and (11) makes its second term at most \(\delta/4\). Adding (7) gives total failure probability at most \(\delta/8+\delta/2+\delta/4<\delta\).

Outside this failure event no fitting network has Lipschitz constant at most \(L_*\). Therefore every fitting network satisfies, in particular,
\[
\operatorname{Lip}_D(f)\ge
c_0\varepsilon\sqrt{\frac{n}{M\log(C_0Mnd/\varepsilon)}}.
\]
The finite-net good event is measurable and implies the simultaneous conclusion for every network, including sample-dependent choices of parameters. No weight restriction, label-input independence, additional sample-size condition, or saturation cap has been introduced.
