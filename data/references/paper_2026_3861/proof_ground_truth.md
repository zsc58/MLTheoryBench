# Reference Proof

## Proof Structure and Obligations

1. Establish Borel measurability and almost-sure finiteness of conditional second moments, and independence of the conditional finite-moment domain from the reference point.
2. Establish finite, continuous, coercive conditional objectives and nonempty compact argmin sets.
3. Prove measurability of the value function and weak measurability of the argmin correspondence; obtain a Borel selector and extend it as a Borel map on the whole manifold.
4. Establish finiteness of the integrated value, the loss-disintegration identity on the defined domain, attainment, and the characterization of every minimizing Borel map.
5. Prove all four zero-defect equivalences, including both directions between deterministic kernels and map-induced couplings.

## Independent Results Used

The following are the relevant statements of the standard independent dependencies already indexed by the source.

- **Properness (theory_016):** A connected, complete, finite-dimensional Riemannian manifold has compact closed bounded subsets. Its geodesic metric is complete and separable, so it is a Polish space. In particular, a continuous real-valued function with bounded sublevel sets attains its minimum and has a compact minimizer set.
- **Measurable selection (theory_017):** Let \((S,\Sigma)\) be a measurable space and \(Y\) a Polish space. If a correspondence \(C\) has nonempty closed values in \(Y\) and is weakly measurable, meaning \(\{s:C(s)\cap U\ne\varnothing\}\in\Sigma\) for every open \(U\subseteq Y\), then it admits a \(\Sigma\)-to-Borel measurable selector. This is the Kuratowski–Ryll-Nardzewski theorem invoked by the source. Weak measurability in the present application is proved below, not inferred from compact values alone.
- **Disintegration (theory_020):** A probability measure on a product of Polish spaces admits a Borel probability kernel with respect to its first marginal, unique almost everywhere as a probability measure. Integration against the product measure equals iterated kernel integration for nonnegative Borel functions and bounded Borel functions. Integration of a nonnegative Borel function against a Borel kernel is measurable, including when the integrand also depends Borel measurably on the kernel parameter.

The domain used for selection is \((X_0,\mathcal B(X_0))\); it need not be Polish in its subspace topology. The codomain \(N\) is Polish. The source's optional uniqueness regimes are not used.

## Complete Proof

### Step 1: Conditional objectives and a Borel selector

For a reference point \(o\), define on all of \(N\)
\[
q_o(x):=\int_N d(o,y)^2\,\kappa_x(dy)\in[0,+\infty].
\]
The kernel property makes \(q_o\) Borel. Disintegration and the second marginal give
\[
\int_N q_o(x)\,\mu(dx)=\int_N d(o,y)^2\,\nu(dy)<\infty.
\]
Consequently, the specified set \(X_0=\{q_o<\infty\}\) is Borel and has full \(\mu\)-measure.

For another reference point \(o'\), the triangle inequality gives, for every \(x\),
\[
q_{o'}(x)\le 2d(o,o')^2+2q_o(x).
\]
Interchanging \(o\) and \(o'\) shows \(q_o(x)<\infty\) if and only if \(q_{o'}(x)<\infty\). Thus the two definitions of \(X_0\) actually agree exactly for the fixed kernel, which proves the requested almost-everywhere independence.

Fix \(x\in X_0\), and abbreviate \(q=q_o(x)\). For every \(z\in N\),
\[
d(z,y)^2\le 2d(z,o)^2+2d(o,y)^2,
\]
so \(\phi_x(z)\) is finite. If \(z_n\to z\), the numbers \(d(z_n,o)\) are bounded. The same inequality gives an integrable dominating function independent of \(n\), while continuity of distance gives pointwise convergence. Dominated convergence proves continuity of \(\phi_x\).

For coercivity, let \(r=d(z,o)\) and
\[
m:=\int_N d(o,y)\,\kappa_x(dy)\le q^{1/2}.
\]
The reverse triangle inequality gives \(d(z,y)\ge |r-d(o,y)|\), so
\[
2\phi_x(z)\ge\int_N(r-d(o,y))^2\,\kappa_x(dy)
=r^2-2rm+q.
\]
This tends to infinity as \(r\to\infty\). Thus the nonempty sublevel set \(\{z:\phi_x(z)\le\phi_x(o)\}\) is closed and bounded, hence compact by properness. Continuity on this set gives a global minimum, and \(A(x)\) is nonempty and compact. This argument also covers compact manifolds and the one-point case.

For fixed \(z\), \(x\mapsto\phi_x(z)\) is Borel on \(X_0\) by kernel integration. Fix a countable dense sequence \((p_j)\) in \(N\). Joint measurability can be checked directly: for each positive integer \(n\), choose \(p_{j_n(z)}\) to be the first sequence point within distance \(1/n\) of \(z\). Each \(j_n\) is Borel. Hence \((x,z)\mapsto\phi_x(p_{j_n(z)})\) is Borel, and continuity gives its pointwise convergence to \(\phi_x(z)\). The conditional objective is therefore jointly Borel on \(X_0\times N\).

Continuity also gives
\[
v(x)=\inf_j\phi_x(p_j).
\]
Thus \(v\) is Borel and finite on \(X_0\).

We next verify weak measurability of \(A\). Let \(\mathcal C\) be the countable family of closed balls with centers among the \(p_j\) and positive rational radii. Each \(C\in\mathcal C\) is nonempty and compact. Choose a countable dense sequence \((p_{C,k})\) in each such ball. Then
\[
v_C(x):=\min_{z\in C}\phi_x(z)=\inf_k\phi_x(p_{C,k})
\]
is a finite Borel function of \(x\); existence of the minimum follows from compactness and continuity.

Every point of an open set \(U\subseteq N\) belongs to a ball \(C\in\mathcal C\) contained in \(U\). Therefore
\[
\{x\in X_0:A(x)\cap U\ne\varnothing\}
=
\bigcup_{\substack{C\in\mathcal C\\ C\subseteq U}}
\{x\in X_0:v_C(x)=v(x)\}.
\]
For the reverse inclusion, equality of the two values produces an actual minimizer in \(C\), because the minimum defining \(v_C\) is attained. The displayed union is countable and Borel. Thus \(A\) is weakly measurable with nonempty closed values in the Polish space \(N\), verifying every hypothesis of the stated selection theorem.

Obtain a Borel selector on \(X_0\), and define it to equal the fixed point \(o\) on \(N\setminus X_0\). Since \(X_0\) is Borel, this defines a Borel map \(b:N\to N\) satisfying \(b(x)\in A(x)\) for every \(x\in X_0\).

### Step 2: Finite attained value and all minimizers

Pointwise comparison with the reference point gives
\[
0\le v(x)\le\phi_x(o)=\frac12q_o(x),\qquad x\in X_0.
\]
Consequently,
\[
0\le D(\gamma)\le\frac12\int_N d(o,y)^2\,\nu(dy)<\infty.
\]
This is the finite-value part of theory_019, explicitly derived here. Its separate assertion about the second moment of the selected pushforward is not needed for the public task.

Let \(T:N\to N\) be any Borel map. The function \((x,y)\mapsto d(T(x),y)^2\) is nonnegative Borel. Disintegration, followed by removal of a \(\mu\)-null set, gives
\[
L_\gamma(T)
=\int_N\left(\frac12\int_Nd(T(x),y)^2\,\kappa_x(dy)\right)\mu(dx)
=\int_{X_0}\phi_x(T(x))\,\mu(dx).
\]
These are extended nonnegative integrals. In particular, this identity never evaluates the public object \(\phi_x\) outside its defined domain.

Pointwise minimality implies \(L_\gamma(T)\ge D(\gamma)\). For the Borel selector \(b\), pointwise equality holds on \(X_0\), so
\[
L_\gamma(b)=D(\gamma).
\]
Thus the infimum over all Borel maps is attained and equals \(D(\gamma)\).

For an arbitrary Borel \(T\), the function
\[
e_T(x):=\phi_x(T(x))-v(x),\qquad x\in X_0,
\]
is Borel, finite-valued, and nonnegative. By additivity of nonnegative integrals,
\[
L_\gamma(T)=D(\gamma)+\int_{X_0}e_T(x)\,\mu(dx).
\]
Since \(D(\gamma)<\infty\), equality \(L_\gamma(T)=D(\gamma)\) holds exactly when \(e_T=0\) almost everywhere. This is precisely \(T(x)\in A(x)\) for \(\mu\)-almost every \(x\). The reasoning permits \(L_\gamma(T)=+\infty\) and imposes no extra moment or pushforward restriction on competing maps.

### Step 3: The four zero-defect formulations

Because \(v\) is nonnegative and measurable on a full-measure set,
\[
D(\gamma)=0
\quad\Longleftrightarrow\quad
v(x)=0\text{ for \(\mu\)-almost every }x.
\]
If the latter holds, the selector constructed above satisfies
\[
0=\phi_x(b(x))=\frac12\int_Nd(b(x),y)^2\,\kappa_x(dy)
\]
for almost every \(x\). A nonnegative function with zero integral vanishes almost everywhere. Distance vanishes exactly on the diagonal, so \(\kappa_x(\{b(x)\})=1\), equivalently \(\kappa_x=\delta_{b(x)}\), for almost every \(x\).

More generally, suppose \(\kappa_x=\delta_{T(x)}\) almost everywhere for some Borel \(T\). For every bounded Borel \(h:N\times N\to\mathbb R\), disintegration gives
\[
\int h(x,y)\,\gamma(dx,dy)
=\int_N\left(\int_Nh(x,y)\,\kappa_x(dy)\right)\mu(dx)
=\int_N h(x,T(x))\,\mu(dx).
\]
Taking indicators of Borel sets identifies the measures and proves \(\gamma=(\mathrm{id},T)_\#\mu\).

Conversely, suppose \(\gamma=(\mathrm{id},T)_\#\mu\) for some Borel \(T\). The map \(x\mapsto\delta_{T(x)}\) is a Borel probability kernel, since its value on a Borel set \(E\) is \(\mathbf 1_E(T(x))\). The pushforward integration identity shows that this kernel is a disintegration of \(\gamma\) with respect to \(\mu\). Uniqueness of disintegration on the Polish space \(N\) therefore yields
\[
\kappa_x=\delta_{T(x)}
\]
for almost every \(x\). On the common full-measure set contained in \(X_0\),
\[
\phi_x(z)=\frac12d(z,T(x))^2,
\]
whose minimum is zero, attained uniquely at \(T(x)\). Hence \(v=0\) almost everywhere and \(D(\gamma)=0\). This also proves the converse implication between the kernel and pushforward formulations, completing every equivalence.

## Source and Obligation Closure

Step 1 follows the conditional existence and selection development at source.html L000385–L000416, with the weak-measurability verification and basepoint comparison written out. Step 2 uses the finite-value estimate at L000422–L000425 and the variational argument at L000434–L000445. Step 3 follows L000446–L000460. All theorem-critical obligations listed above are explicitly derived or discharged by a stated standard independent result whose hypotheses are checked. No unresolved private proof obligation remains.
