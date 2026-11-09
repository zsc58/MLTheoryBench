# Reference Proof

## Obligations and standard results

The proof must establish: (i) a uniform support estimate with the stated coefficient and failure probability; (ii) criticality of every exact factorization on the same event; and (iii) local growth with the specified factorization-dependent constant. The support event must not depend on corruption magnitudes or signs.

Write \(\ell=\log(mn)\), \(d_0=\min(m,n)\), and use \(K\) for numerical constants that may increase between estimates. The following standard independent results are used in the forms needed here.

1. **Bernstein inequality.** Independent centered real variables bounded in absolute value by \(b\), with total variance at most \(v\), satisfy
\[
\Pr\{|\textstyle\sum Z_i|>\sqrt{2vu}+(2b/3)u\}\le 2e^{-u},\qquad u>0.
\]
This is a permissible weaker-constant form of the source's Bernstein bound.
2. **Chaining functionals and mixed tails.** For admissible finite sets \(A_j\), with \(|A_0|=1\) and \(|A_j|\le 2^{2^j}\), define
\[
\gamma_\alpha(A,d)=\inf_{(A_j)}\sup_{a\in A}\sum_{j\ge0}2^{j/\alpha}d(a,A_j).
\]
For a separable process whose increments satisfy
\[
\Pr\{|Z_a-Z_b|>\sqrt u\,d_2(a,b)+u d_1(a,b)\}\le2e^{-u},
\]
the mixed-tail theorem bounds \(\sup_a|Z_a-Z_{a_0}|\), except on an event of probability \(e^{-u}\), by
\[
K\{\gamma_2(A,d_2)+\gamma_1(A,d_1)+\sqrt u\,\operatorname{diam}_{d_2}(A)+u\operatorname{diam}_{d_1}(A)\},\qquad u\ge1.
\]
3. **Entropy and Gaussian comparison.** Dudley's bound is
\[
\gamma_\alpha(A,d)\le K_\alpha\int_0^\infty [\log N(A,d,t)]^{1/\alpha}\,dt.
\]
For a centered separable Gaussian process with canonical metric \(d\), the majorizing-measure bound gives \(\gamma_2(A,d)\le K\mathbb E\sup_{a\in A}G_a\). Covering numbers may first be estimated with centers in the ambient normed space: selecting a point of the index set from each nonempty covering ball converts such a cover to an intrinsic cover with twice the radius.
4. **Local projection.** A smooth closed embedded submanifold of a finite-dimensional Euclidean space has, near each of its points, a single-valued continuous nearest-point projection. The displacement from a point to its projection is normal to the tangent space.
5. **Clarke calculus.** A finite maximum of continuously differentiable functions has Clarke subdifferential equal to the convex hull of the active gradients. In particular, this applies to an entrywise absolute-value sum of smooth residuals. Clarke criticality means that this subdifferential contains zero.

The applications below verify the hypotheses of these results. No paper-specific lemma is taken as an unproved input.

## 1. The restricted support estimate

### 1.1 A zero-anchored process and its metrics

Use the compact tangent-space unit ball
\[
\mathcal B=\{W\in T:\|W\|_1\le1\},\qquad
Z_W=\sum_{ij}(\delta_{ij}-p)|W_{ij}|.
\]
It contains zero, and \(Z_0=0\). Every sample path is continuous on this finite-dimensional compact set, so the process is separable and its supremum is measurable.

For \(W,W'\in\mathcal B\), the summands of \(Z_W-Z_{W'}\) are independent and centered. They are bounded by \(\|W-W'\|_\infty\), and their total variance is at most
\[
p\sum_{ij}(|W_{ij}|-|W'_{ij}|)^2\le p\|W-W'\|_F^2.
\]
Bernstein therefore verifies the mixed-tail hypothesis with
\[
d_2(W,W')=\sqrt{2p}\|W-W'\|_F,
\qquad d_1(W,W')=\tfrac23\|W-W'\|_\infty.
\]

### 1.2 Projector and diameter estimates

Let \(P_U=UU^T\), \(P_V=VV^T\). The Frobenius orthogonal projector onto \(T\) is
\[
P_T(A)=P_UA+AP_V-P_UAP_V.
\]
Indeed, its complement is \(A\mapsto(I-P_U)A(I-P_V)\), the orthogonal projector onto \(T^\perp\).

For coordinate matrices \(E_{ij}\), put \(a_i=\|U_{i,:}\|_2^2\), \(b_j=\|V_{j,:}\|_2^2\), and \(q=\mu r(1/m+1/n)\). Direct substitution gives
\[
\|P_TE_{ij}\|_F^2=\langle E_{ij},P_TE_{ij}\rangle=a_i+b_j-a_ib_j\le q.
\]
Since \(P_T\) is an orthogonal projector,
\[
|\langle E_{ij},P_TE_{kl}\rangle|
=|\langle P_TE_{ij},P_TE_{kl}\rangle|\le q.
\]
Expanding \(W=P_TW=\sum W_{ij}P_TE_{ij}\), for \(W\in\mathcal B\), yields
\[
\|W\|_F\le\sqrt q,\qquad \|W\|_\infty\le q.
\]
Thus the unscaled Frobenius and infinity diameters are at most \(2\sqrt q\) and \(2q\), respectively.

### 1.3 The Gaussian contribution

Let \(G\) have independent standard Gaussian entries and set \(G_W=\langle G,W\rangle\). This is a centered continuous Gaussian process with canonical metric \(\|W-W'\|_F\). Furthermore,
\[
\sup_{W\in\mathcal B}\langle G,W\rangle\le\|G\|_\infty.
\]
For \(N=mn\) and \(t>0\), the Gaussian moment-generating function and the sum over both signs give
\[
\mathbb E\max_{ij}|G_{ij}|\le\frac{\log(2N)}t+\frac t2.
\]
Minimizing over \(t\) proves \(\mathbb E\|G\|_\infty\le\sqrt{2\log(2mn)}\). Majorizing measures consequently gives
\[
\gamma_2(\mathcal B,\|\cdot\|_F)\le K\sqrt\ell,
\qquad \gamma_2(\mathcal B,d_2)\le K\sqrt{p\ell}.
\]

### 1.4 Row covers and the entropy integral

Set
\[
a=\sqrt{\mu r/n},\qquad b=\sqrt{\mu r/m}.
\]
For \(W\in\mathcal B\), define
\[
H=WV,\qquad K_0=W^TU,\qquad Z=U^TWV.
\]
The tangent-projector identity gives
\[
W=HV^T+UK_0^T-UZV^T.
\]
The entrywise triangle inequality and incoherence imply
\[
\sum_i\|H_{i,:}\|_2\le a,
\qquad \sum_j\|(K_0)_{j,:}\|_2\le b,
\qquad \|Z\|_F\le ab.
\]
For example, the first bound follows from
\(\sum_i\|\sum_jW_{ij}V_{j,:}\|_2\le a\sum_{ij}|W_{ij}|\).
The last follows by writing \(Z=\sum_{ij}W_{ij}U_{i,:}^TV_{j,:}\).
These are row-sum norms, not induced 2-to-1 operator norms.

Let \(\mathcal H(a)\) denote the row-sum ball in \(\mathbb R^{m\times r}\), equipped with the row-maximum metric
\(d_{\rm row}(H,H')=\max_i\|H_{i,:}-H'_{i,:}\|_2\).
Use \(N_{\rm ext}\) for covers whose centers may lie in the ambient space. A Euclidean ball of radius \(a\) in \(\mathbb R^r\) admits a \(t\)-cover with at most \((1+2a/t)^r\) points, by the disjoint-ball volume argument. Covering all rows therefore gives
\[
\log N_{\rm ext}(\mathcal H(a),d_{\rm row},t)
\le mr\log(1+2a/t).
\]
For \(0<t<a\), let \(s=\min\{m,\lfloor a/t\rfloor\}\). At most \(s\) rows of a member of \(\mathcal H(a)\) have norm greater than \(t\). Pad their support to cardinality \(s\), cover those row balls, and replace the other rows by zero. This proves the second bound
\[
\log N_{\rm ext}(\mathcal H(a),d_{\rm row},t)
\le s\log(em/s)+rs\log(1+2a/t).
\]
The support-selection term is retained. For \(t\ge a\), the center zero covers the entire set.

Split the entropy integral at \(a/m\). On \((0,a/m)\), the volume estimate and \(\log(1+2a/t)\le\log(3a/t)\) give
\[
\int_0^{a/m}\log N_{\rm ext}(t)\,dt
\le ar[\log(3m)+1].
\]
On \((a/m,a)\), use \(s\le a/t\) and \(\log(em/s)\le\log(em)\) to obtain
\[
\begin{aligned}
\int_{a/m}^{a}\log N_{\rm ext}(t)\,dt
&\le a\log(em)\log m
+ar\left(\tfrac12\log^2m+\log3\log m\right).
\end{aligned}
\]
Since \(r\ge1\), altogether
\[
I_H:=\int_0^\infty\log N_{\rm ext}(\mathcal H(a),d_{\rm row},t)\,dt
\le K ar\log^2(em).
\]
The same argument for \(\mathcal K(b)\subset\mathbb R^{n\times r}\) gives
\(I_K\le Kbr\log^2(en)\).

For \(\mathcal Z=\{Z:\|Z\|_F\le ab\}\), Frobenius covers are also operator-norm covers. A volume bound in dimension \(r^2\) gives
\[
I_Z:=\int_0^\infty\log N_{\rm ext}(\mathcal Z,\|\cdot\|_{\rm op},t)\,dt
\le r^2\int_0^{ab}\log(1+2ab/t)\,dt
\le Kr^2ab.
\]
Reconstruct net points as \(H'V^T+UK'^T-UZ'V^T\). Their approximation error is bounded by
\[
a\,d_{\rm row}(H,H')+b\,d_{\rm row}(K_0,K')+ab\|Z-Z'\|_{\rm op}.
\]
Product covers, a change of integration variable, and recentering into \(\mathcal B\) therefore give
\[
\begin{aligned}
\int_0^\infty\log N(\mathcal B,\|\cdot\|_\infty,t)\,dt
&\le K(aI_H+bI_K+abI_Z)\\
&\le K\left[\mu r^2\ell^2(1/m+1/n)+\frac{\mu^2r^4}{mn}\right].
\end{aligned}
\]
Here \(\log(em),\log(en)\le K\ell\) because \(m,n\ge2\). Define \(B=\mu r^2\ell^2/d_0\). Since \(mn\ge d_0^2\),
\[
\frac{\mu^2r^4}{mn}\le\left(\frac{\mu r^2}{d_0}\right)^2=\frac{B^2}{\ell^4}.
\]
The assumed rank bound gives \(B\le c^2\). Taking \(c\le1\), this term is bounded by a universal multiple of \(B\). Dudley's inequality now proves
\[
\gamma_1(\mathcal B,d_1)\le KB.
\]
In particular the entropy integral is finite, as required in the chaining application.

### 1.5 Tail bound, mean, and margin

Apply the mixed-tail theorem with anchor zero and \(u=r\ell^2\ge1\). Except on an event of probability \(e^{-r\ell^2}\),
\[
\sup_{W\in\mathcal B}|Z_W|
\le K\left[\sqrt{p\ell}+B+\sqrt{pqu}+qu\right].
\]
Since \(q\le2\mu r/d_0\) and \(p\le1\),
\[
\sqrt{pqu}\le K r\ell\sqrt{\mu/d_0},\qquad qu\le KB.
\]
For \(\|W\|_1=1\),
\(\|P_\Omega W\|_1=p+Z_W\), and \(p\le\sqrt{p\ell}\) because \(\ell>1\). Homogeneity, including the separate trivial case \(W=0\), proves the first displayed support bound with a universal coefficient \(C_1\) and a positive universal probability constant \(C_2\) (the above argument permits \(C_2=1\)).

The parameter restrictions imply
\[
\sqrt{p\ell}\le\sqrt c,\qquad B\le c^2,
\qquad r\ell\sqrt{\mu/d_0}\le c.
\]
Choose \(c>0\) sufficiently small that \(C_1(\sqrt c+c^2+c)\le1/4\). We may then take the common deterministic margin \(\varepsilon=1/2\). More generally any smaller positive margin satisfying the required inequality works. This choice does not depend on the factorization or corruption values.

## 2. Certificate and criticality

Fix a support realization on the event just established and fix any values of the nonzero corruption entries. Define the compact convex set
\[
\Xi=\{\Lambda:P_\Omega\Lambda=P_\Omega\operatorname{sign}(-S),\ 
\|P_{\Omega^c}\Lambda\|_\infty\le1-\varepsilon\}.
\]
Its image \(\mathcal D=\{(\Lambda V,\Lambda^TU):\Lambda\in\Xi\}\) is compact and convex. For arbitrary \(H,K\), put \(W=HV^T+UK^T\). The support function of \(\mathcal D\) obeys
\[
\begin{aligned}
\sup_{\Lambda\in\Xi}\langle\Lambda,W\rangle
&\ge(1-\varepsilon)\|P_{\Omega^c}W\|_1-\|P_\Omega W\|_1\\
&=(1-\varepsilon)\|W\|_1-(2-\varepsilon)\|P_\Omega W\|_1\\
&\ge\tfrac12\varepsilon(1-\varepsilon)\|W\|_1\ge0.
\end{aligned}
\]
If zero were outside \(\mathcal D\), finite-dimensional strict separation would give a direction with negative support function. Thus there exists \(\Lambda\in\Xi\) with
\(\Lambda V=0\) and \(\Lambda^TU=0\).

For any \((X_*,Y_*)\in\mathcal L\), rank and the product identity imply \(\operatorname{col}(X_*)=\operatorname{col}(U)\) and \(\operatorname{col}(Y_*)=\operatorname{col}(V)\). Hence \(\Lambda Y_*=0\) and \(\Lambda^TX_*=0\).

To verify the Clarke formula, write the objective as the finite maximum
\[
f(X,Y)=\max_{Q\in\{-1,1\}^{m\times n}}\langle Q,XY^T-M\rangle.
\]
Each function in this maximum is smooth; the convex hull of the active sign matrices is exactly the entrywise set \(\operatorname{sign}(XY^T-M)\). The finite-maximum rule consequently gives
\[
\partial f(X,Y)=\{(\Lambda Y,\Lambda^TX):\Lambda\in\operatorname{sign}(XY^T-M)\}.
\]
Our certificate therefore proves \(0\in\partial f(X_*,Y_*)\) simultaneously for every true factorization.

## 3. Sharp local growth with the stated constant

Fix \((X_*,Y_*)\in\mathcal L\), and put
\(\sigma_* =\min\{\sigma_r(X_*),\sigma_r(Y_*)\}>0\).
Every true factorization can be written uniquely as
\[
(X_*R,Y_*R^{-T}),\qquad R\in\mathrm{GL}(r).
\]
This parametrization is smooth and has smooth inverse \(R=X_*^\dagger X\) on its image; its derivative is injective. Moreover, \(\mathcal L=\{(X,Y):XY^T=L\}\) is closed because \(k=r=\operatorname{rank}(L)\) makes the rank conditions automatic. Thus \(\mathcal L\) is a smooth closed embedded manifold, and the local projection theorem applies.

For \((X,Y)\) sufficiently close to \((X_*,Y_*)\), let \((X^\sharp,Y^\sharp)\) be its nearest point in \(\mathcal L\), and set
\[
H=X-X^\sharp,\quad K=Y-Y^\sharp,\quad
 d=\sqrt{\|H\|_F^2+\|K\|_F^2}=d((X,Y),\mathcal L).
\]
The tangent space to \(\mathcal L\) at the projection consists of
\((X^\sharp A,-Y^\sharp A^T)\). Normality therefore gives, for every \(A\),
\[
0=\langle H,X^\sharp A\rangle-\langle K,Y^\sharp A^T\rangle
=\langle (X^\sharp)^TH-K^TY^\sharp,A\rangle,
\]
so
\[
(X^\sharp)^TH=K^TY^\sharp.
\]
Expand the product perturbation as
\[
XY^T-L=\Delta_1+\Delta_2,
\quad \Delta_1=X^\sharp K^T+H(Y^\sharp)^T\in T,
\quad \Delta_2=HK^T.
\]

For any matrix \(\Delta\), convexity of the supported absolute values and the certificate bounds give
\[
\begin{aligned}
\|\Delta-S\|_1-\|S\|_1
&\ge\|P_{\Omega^c}\Delta\|_1+
\langle P_\Omega\Lambda,P_\Omega\Delta\rangle\\
&\ge\varepsilon\|P_{\Omega^c}\Delta\|_1+\langle\Lambda,\Delta\rangle.
\end{aligned}
\]
The certificate annihilates \(\Delta_1\). Applying the restricted estimate to \(\Delta_1\) gives
\(\|P_{\Omega^c}\Delta_1\|_1\ge(1+\varepsilon)\|\Delta_1\|_1/2\).
For the quadratic term, split the support and complement:
\[
\langle\Lambda,\Delta_2\rangle
-\varepsilon\|P_{\Omega^c}\Delta_2\|_1
\ge-\|P_\Omega\Delta_2\|_1-\|P_{\Omega^c}\Delta_2\|_1
=-\|\Delta_2\|_1.
\]
Consequently,
\[
f(X,Y)-f(X_*,Y_*)\ge\frac\varepsilon2\|\Delta_1\|_1-\|\Delta_2\|_1.
\]
No sign-preservation condition on the supported residual is needed.

Let \(A_0=(X^\sharp)^TH=K^TY^\sharp\). The cross term in the Frobenius expansion is
\[
\langle X^\sharp K^T,H(Y^\sharp)^T\rangle
=\operatorname{tr}((Y^\sharp)^TK(X^\sharp)^TH)
=\operatorname{tr}(A_0^TA_0)\ge0.
\]
Writing \(\sigma_\sharp=\min\{\sigma_r(X^\sharp),\sigma_r(Y^\sharp)\}\), full column rank yields
\[
\|\Delta_1\|_1\ge\|\Delta_1\|_F
\ge\left(\sigma_r(X^\sharp)^2\|K\|_F^2+
\sigma_r(Y^\sharp)^2\|H\|_F^2\right)^{1/2}
\ge\sigma_\sharp d.
\]
Continuity of projection and singular values permits shrinking the neighborhood so that \(\sigma_\sharp\ge\sigma_*/2\). Also,
\[
\|\Delta_2\|_1\le\sqrt{mn}\|HK^T\|_F
\le\sqrt{mn}\|H\|_F\|K\|_F
\le\tfrac12\sqrt{mn}\,d^2.
\]
Choose \(\rho>0\) so that the closed product-space ball of radius \(\rho\) about \((X_*,Y_*)\) lies in this neighborhood and
\(\rho\le\varepsilon\sigma_*/(4\sqrt{mn})\).
Because \(d\le\|(X,Y)-(X_*,Y_*)\|_{\rm prod}\le\rho\),
\[
f(X,Y)-f(X_*,Y_*)
\ge\frac{\varepsilon\sigma_*}{4}d-\frac{\sqrt{mn}}2d^2
\ge\frac{\varepsilon\sigma_*}{8}d.
\]
This includes \(d=0\). The factorization was arbitrary, so the same support event gives the asserted conclusion for every member of \(\mathcal L\), with its own radius. The argument also covers the positive-probability event \(\Omega=\varnothing\); no nonzero-corruption assumption is used.
