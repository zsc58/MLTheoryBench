# Reference Proof

## Proof Structure

1. Establish existence of a continuous optimal target potential on the compact target support using the soft-transform semidual formulation.
2. Approximate that potential by centered members of the specified feature-pullback class and prove total-variation convergence of their Gibbs laws.
3. Transfer this convergence through heat smoothing, using Markov-kernel contraction and the ambient heat-kernel approximate-identity property.
4. Establish continuity of the projection–pullback map on the embedded graph, pass to the weak limit, and identify both marginals.

## Complete Proof

Write \(M=M_\Psi\), \(P=P_\Psi\), \(Q=Q_\Psi\), \(X=\operatorname{spt}P\), and \(K=\operatorname{spt}Q\). The embedding is continuous, so \(S=\Psi(\Gamma)\) is compact. Thus \(X\) and \(K\) are nonempty compact metric spaces, and \(c\) is continuous and bounded on \(X\times K\). Put \(C=\max_{X\times K}c\).

### 1. A continuous optimal potential

For \(g\in C(K)\), define
\[
T_Qg(x)=-\epsilon\log\int_K e^{(g(y)-c(x,y))/\epsilon}\,dQ(y),\qquad x\in X,
\]
and
\[
J(g)=\int_K g\,dQ+\int_X T_Qg\,dP.
\]
For \(f\in C(X)\), likewise define
\[
T_Pf(y)=-\epsilon\log\int_X e^{(f(x)-c(x,y))/\epsilon}\,dP(x).
\]
All these functions are finite and continuous, since the domains are compact and the integrands are continuous and strictly positive.

Consider the auxiliary functional
\[
D(f,g)=\int_X f\,dP+\int_K g\,dQ
-\epsilon\int_{X\times K}\left(e^{(f(x)+g(y)-c(x,y))/\epsilon}-1\right)dP(x)dQ(y).
\]
For fixed \(g\), its maximum over \(f\in C(X)\) is attained at \(f=T_Qg\). Indeed, at each \(x\), the relevant scalar expression is \(s-\epsilon A(x)e^{s/\epsilon}\), with \(A(x)>0\), and its maximum occurs at \(s=-\epsilon\log A(x)\). The analogous assertion holds for maximizing over \(g\) with \(f\) fixed. Also,
\[
D(T_Qg,g)=J(g).
\]
Consequently, if \(f=T_Qg\) and \(h=T_Pf\), then
\[
J(h)=D(T_Qh,h)\ge D(f,h)\ge D(f,g)=J(g).
\]

The integral comparison inside a soft transform gives
\[
|h(y)-h(y')|\le\sup_{x\in X}|c(x,y)-c(x,y')|.
\]
Hence these transformed potentials have oscillation at most \(C\) and a common modulus of continuity. Centering \(h\) by subtracting \(\int h\,dQ\) preserves \(J(h)\), its modulus of continuity, and its oscillation, and gives \(\|h\|_\infty\le C\).

The supremum of \(J\) over \(C(K)\) is finite. In fact, Jensen's inequality gives
\[
T_Qg(x)\le \int_K c(x,y)\,dQ(y)-\int_K g\,dQ,
\]
so \(J(g)\le\int c\,d(P\otimes Q)\); and \(J(0)\) is finite. Start with a maximizing sequence and apply the preceding two transforms and centering. The resulting sequence remains maximizing and is uniformly bounded and equicontinuous on \(K\).

We use the standard Arzelà–Ascoli theorem in its compact-metric-space form: a uniformly bounded equicontinuous sequence of continuous real functions has a uniformly convergent subsequence. Its hypotheses have just been checked. Thus a subsequence converges uniformly to a centered \(g^\star\in C(K)\). The integral comparison defining the transform also gives
\[
\|T_Qg-T_Q\widetilde g\|_\infty\le\|g-\widetilde g\|_\infty.
\]
Therefore \(J\) is continuous for uniform convergence, and \(g^\star\) maximizes \(J\) over \(C(K)\).

Set \(f^\star=T_Qg^\star\), and define
\[
R^\star(dx,dy)=e^{(f^\star(x)+g^\star(y)-c(x,y))/\epsilon}P(dx)Q(dy).
\]
Normalization gives its first marginal \(P\). For any \(b\in C(K)\), differentiation at zero of \(J(g^\star+s b)\) is justified by boundedness on the compact supports and gives
\[
0=\left.\frac{d}{ds}J(g^\star+s b)\right|_{s=0}
=\int_K b\,dQ-\int_{X\times K}b(y)\,dR^\star(x,y).
\]
Continuous functions determine Borel probability measures on a compact metric space, so the second marginal of \(R^\star\) is \(Q\).

To identify this coupling as the optimizer, note that its density with respect to \(P\otimes Q\) is bounded above and bounded away from zero. For every coupling \(\pi\in\Pi(P,Q)\) with finite relative entropy,
\[
\int c\,d\pi+\epsilon\operatorname{KL}(\pi\|P\otimes Q)
=J(g^\star)+\epsilon\operatorname{KL}(\pi\|R^\star).
\]
This follows by substituting the displayed logarithm of the density of \(R^\star\) and using the two marginal identities for \(\pi\). Couplings with infinite relative entropy have infinite objective and cannot improve on \(R^\star\). Nonnegativity of relative entropy, with equality only for identical probability measures, now shows that \(R^\star\) is the unique optimizer. In particular,
\[
R^\star=\pi^\star_{\epsilon,\Psi}.
\]

### 2. Neural-potential recovery

Because \(\phi:K\to\mathbb R^n\) is continuous and injective and \(K\) is compact, it is a homeomorphism onto the compact, hence closed, set \(A=\phi(K)\). Thus \(g^\star\circ\phi^{-1}\) is continuous on \(A\).

We use the standard continuous-extension theorem: a bounded continuous real function on a closed subset of a metric space extends to a continuous real function on the whole space. Here the subset is the compact set \(A\subset\mathbb R^n\), so its hypotheses hold. Let \(G\in C(\mathbb R^n,\mathbb R)\) be such an extension. Density of \(\mathcal F\) in the topology of uniform convergence on compact sets allows us to choose \(a_m\in\mathcal F\) with
\[
\sup_{z\in A}|a_m(z)-G(z)|\le \frac1m.
\]
Define
\[
g_m=a_m\circ\phi-\int_K a_m\circ\phi\,dQ.
\]
Since \(g^\star\) is centered,
\[
\delta_m:=\|g_m-g^\star\|_{\infty,K}\le\frac2m.
\]
The soft-transform bound gives \(\|T_Qg_m-f^\star\|_{\infty,X}\le\delta_m\). Writing \(\pi_m=\pi^\epsilon_{g_m,\Psi}\), comparison of its density with that of \(\pi^\star_{\epsilon,\Psi}\) yields
\[
e^{-2\delta_m/\epsilon}\le
\frac{d\pi_m}{d\pi^\star_{\epsilon,\Psi}}(x,y)
\le e^{2\delta_m/\epsilon}
\]
almost everywhere. Therefore \(\|\pi_m-\pi^\star_{\epsilon,\Psi}\|_{\mathrm{TV}}\to0\), under either conventional normalization of total variation. This proves the neural recovery conclusion without invoking the specialized external recovery theorem.

### 3. Heat smoothing and the joint limit

Write \(\pi^\star=\pi^\star_{\epsilon,\Psi}\), and let \(L_t\) be the Markov kernel on \(M\times M\) that keeps the first coordinate fixed and applies \(H_t\) to the second. Set
\[
\eta_{m,t}=\pi_mL_t,\qquad \eta_t^\star=\pi^\star L_t.
\]
A Markov kernel contracts total variation: for any measurable event \(B\), its probability after applying the kernel is the integral of a measurable function taking values in \([0,1]\), namely \(L_t(\cdot,B)\). Taking the corresponding supremum gives
\[
\|\eta_{m,t}-\eta_t^\star\|_{\mathrm{TV}}
\le\|\pi_m-\pi^\star\|_{\mathrm{TV}}.
\]

The heat kernels on Euclidean space and a flat torus satisfy \(H_t(y,\cdot)\Rightarrow\delta_y\) as \(t\downarrow0\). These are precisely the ambient geometries in the task. For bounded continuous \(h\) on \(M\times M\), it follows for every \((x,y)\) that
\[
\int h(x,z)H_t(y,dz)\longrightarrow h(x,y).
\]
The integrands are bounded by \(\|h\|_\infty\), so dominated convergence gives \(\eta_t^\star\Rightarrow\pi^\star\). Together with total-variation contraction, this proves
\[
\eta_{k,1/k}\Rightarrow\pi^\star.
\]
Thus one can take \(m_k=k\) and \(t_k=1/k\); no additional rate-dependent diagonal selection is necessary.

### 4. Projection, pullback, and marginals

The continuous injective map \(\Psi\) from a compact space to the Hausdorff space \(M\) has a continuous inverse on \(S\). Fix \(v\in S\) and an ambient sequence \(z_j\to v\). If \(w_j=\operatorname{proj}_S(z_j)\), then nearest-point optimality and the triangle inequality give
\[
d(w_j,v)\le d(w_j,z_j)+d(z_j,v)
\le2d(z_j,v)\longrightarrow0.
\]
This holds regardless of ties. Thus the selected projection, and hence \(\rho\), is continuous at every point of \(S\). The map \(R=\rho\times\rho\) is measurable and continuous at every point of \(S\times S\).

Both marginals of \(\pi^\star\) are concentrated on \(S\), so
\[
\pi^\star((M\times M)\setminus(S\times S))
\le P(M\setminus S)+Q(M\setminus S)=0.
\]
We apply the standard mapping theorem for weak convergence: if probability measures on metric spaces converge weakly and a measurable map is continuous outside a set of zero limiting measure, their image measures converge weakly. The preceding facts verify its hypotheses and yield
\[
\widehat\pi_{g_k,1/k}=R_\#\eta_{k,1/k}
\Rightarrow R_\#\pi^\star
=(\Psi^{-1},\Psi^{-1})_\#\pi^\star
=\pi^\star_{\epsilon,\Gamma}.
\]
The equality uses that projection is the identity on \(S\).

Finally, the first marginal of this limiting law is
\[
(\Psi^{-1})_\#P_\Psi
=(\Psi^{-1}\circ\Psi)_\#P_\Gamma=P_\Gamma,
\]
and its second marginal is likewise \(Q_\Gamma\). It is a probability law on \(\Gamma\times\Gamma\), and therefore belongs to \(\Pi(P_\Gamma,Q_\Gamma)\).
