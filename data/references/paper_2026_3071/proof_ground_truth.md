# Reference Proof

## Audited Standard Background

The following standard do-calculus results are used.

1. **Soundness.** For a finite recursive causal DAG, possibly containing latent endogenous vertices, the three do-calculus rules and probability identities are sound for the causal kernel-product law and for interventions that replace the selected kernels by point masses. A derivation terminating in observational quantities therefore supplies the queried interventional law whenever those quantities are evaluated in a way determined by the observational law.
2. **Nonparametric completeness.** For observed treatment and outcome sets, if an effect is not graphically identifiable by do-calculus in the unrestricted ordinary recursive causal-model class, there are two ordinary models with the same observed law and different queried interventional laws. Finite-state witnesses are available; latent state spaces and mechanisms are not externally restricted. Assigned finite treatment labels can be relabeled when specifying the witness.

These are the standard independent results invoked by the source. The finite graph, causal intervention semantics, unrestricted model class, and observational marginal required here are checked below. Latent queried vertices and degenerate cases are treated explicitly rather than being concealed in the external completeness invocation.

## Theorem-Critical Obligations

- The integrated mechanisms are measurable stochastic kernels, and the independent recursive construction has the stated DAG product law.
- The integrated mechanisms have the claimed conditional equivariance.
- Interventions have the required kernel-replacement semantics, including for coordinate-varying assignments.
- A sound do-calculus derivation uses the observed marginal, not an unavailable full endogenous joint law, and its conditional evaluations do not depend on arbitrary versions.
- Ordinary nonidentifiability witnesses belong to the full index-transform model class after lifting.
- Equal ordinary observed laws lift to equal entire structured observed laws, not merely equal one-coordinate marginals.
- A difference in the ordinary interventional laws survives at the actual assigned value of a selected coordinate.
- Latent queried vertices and empty cases do not invalidate the external theorem application.

## Kernel Construction and Equivariance

Write \(S_v=(X^v)^\Omega\), with its product sigma-algebra, and let \(N_v=\mu_v^\Omega\) be the product law of the noise field in \((E^v)^\Omega\). Measurability of \(f^v\) makes
\[
K_v(B\mid z)=\int 1_B(f^v(z,e))\,N_v(de)
\]
a stochastic kernel: it is a probability measure in \(B\) for fixed \(z\), and its value is measurable in \(z\) for fixed measurable \(B\).

Every index transform preserves \(N_v\). Indeed, any finite collection of transformed coordinates has the same product law as the corresponding original coordinates. Equality on finite cylinders gives equality of the product-space measures. Coordinate permutations and their inverses are measurable on the product sigma-algebra.

Consequently,
\[
\begin{aligned}
K_v(B\mid\phi z)
&=\int 1_B(f^v(\phi z,\phi e))\,N_v(de)\\
&=\int 1_B(\phi f^v(z,e))\,N_v(de)\\
&=K_v(\phi^{-1}B\mid z),
\end{aligned}
\]
where \(\phi^{-1}B=\{s:\phi s\in B\}\). This is conditional equivariance. The calculation verifies compatibility with the geometric definitions; a separate calculation of it is not necessary in an alternative proof that establishes the two requested identification claims directly.

Choose a topological ordering of the finite DAG. The exogenous field at a vertex is independent of the fields generating its predecessors. Integrating its mechanism therefore gives the kernel \(K_v\), and successive integration yields
\[
P(dx^V)=\prod_{v\in V}K_v(dx^v\mid x^{\mathrm{pa}(v)}).
\]
The observational input is precisely the \(O\)-marginal \(P_{\rm obs}=P^{x^O}\). No latent endogenous variable is thereby made observed.

Under \(do(x^A=a^*)\), the recursive construction sets the intervened fields to their assigned values and retains every other mechanism and noise law. Hence the intervened law is the same kernel product with each \(K_v\), \(v\in A\), replaced by \(\delta_{a^{*,v}}\). The assigned fields need not be invariant under the group; interventions are not required to preserve observational symmetry.

## Soundness

The preceding construction verifies the hypotheses of standard do-calculus soundness at the level of whole structured fields. In every mutilated graph used by a derivation, the corresponding causal kernel system has the required Markov and intervention semantics. The derivation is required to terminate in marginals and conditionals of \(P_{\rm obs}\), not of the unavailable full joint law.

For each observational conditional \(P_{\rm obs}(dz\mid w)\), a regular conditional kernel exists by the stated evaluation assumption. Any two versions agree for \(P_{\rm obs}^W\)-almost every \(w\). Every evaluation measure \(\nu\) in the functional is absolutely continuous with respect to \(P_{\rm obs}^W\), including a Dirac evaluation measure for a point evaluation. The versions therefore agree \(\nu\)-almost everywhere, at every relevant stage of integration. Nonzero-denominator requirements ensure that any conditional ratios used by the formula are defined. Thus the resulting expression is a functional of the observational measure itself.

Applying soundness to the finite derivation gives
\[
Q_{a^*}:=P(x^Y\in\cdot\mid do(x^A=a^*))
=\psi_{a^*}(P_{\rm obs}).
\]
This claim is evaluated where the formula's stated support conditions hold. Those conditions do not define or shrink the model class in the converse.

## Completeness: Elementary Cases

If \(Y=\varnothing\), the target is the unit probability measure on the empty product. If \(\Omega=\varnothing\), every structured field likewise has a single possible value. Probability normalization identifies the target in either case, providing a derivation with no nontrivial do-calculus step.

Suppose henceforth that \(\Omega\ne\varnothing\) and \(Y\ne\varnothing\). The completeness claim is graph-level identification over the unrestricted class, so finite binary coordinate-state choices and arbitrary finite latent state spaces are available as test specifications. It does not assert completeness for an externally restricted family at one particular observational distribution.

If \(Y\) contains a latent vertex \(h\notin O\), take two ordinary binary models making \(h\) constantly 0 and constantly 1 respectively. Make all other vertices constant and have all descendants ignore \(h\). The observed laws agree and the \(h\)-component of the queried interventional laws differs, since \(A\cap Y=\varnothing\). Their coordinatewise lifts, as constructed below, show that the full query cannot be uniformly identifiable. Thus a uniformly identifiable query with nonempty outcome has \(Y\subseteq O\).

Now consider a latent intervention vertex \(h\in A\setminus O\). Delete incoming arrows to all vertices in \(A\). If a directed path from \(h\) to an outcome remains, it has no interior vertex in \(A\). Construct two binary ordinary models in which \(h\) is observationally constant at the value opposite its intervention value. In one model, make the first path vertex constantly 0. In the other, let it indicate that its path parent has the intervention value. Subsequent path vertices copy that binary signal. All remaining mechanisms may ignore their parents and be constant. Observationally, the signal is 0 in both models, so every observed variable has the same joint law. Under the intervention, the signal reaches an outcome and its law differs. All other interventions can be ignored by these mechanisms. Lifting this pair again contradicts uniform identifiability.

Consequently, if the query is uniformly identifiable, no latent intervention has such a surviving path. In that case no latent intervention has a path to \(Y\) after incoming arrows to \(A\cap O\) alone are removed: any such path would have a last latent intervention vertex and would give a surviving path from that vertex. Since intervened vertices have no incoming arrows and there is no directed path to \(Y\), the third do-calculus rule removes the latent interventions. This reduces the query to the observed intervention set \(A\cap O\).

If this set is empty, the reduced target is an observational marginal. Otherwise both the reduced treatment and outcome sets are observed, as required by the standard completeness result.

## Completeness: Lifting Ordinary Witnesses

Consider an ordinary recursive model on the same full DAG, written
\[
Z^v=g^v(Z^{\mathrm{pa}(v)},U^v),
\]
with mutually independent exogenous variables. Use independent copies \(U^v_\omega\) across both vertices and indices, and define
\[
f^v(z,e)_\omega
=g^v((z^u_\omega)_{u\in\mathrm{pa}(v)},e_\omega).
\]
Each output coordinate is measurable, so this defines a measurable map into the product space. For every index bijection,
\[
f^v(\phi z,\phi e)_\omega
=g^v((z^u_{\phi^{-1}\omega})_u,e_{\phi^{-1}\omega})
=(\phi f^v(z,e))_\omega.
\]
The construction is therefore a member of the geometric model class for the given index action, with the required iid-coordinate and independent-field noise laws.

For each finite \(F\subseteq\Omega\), the vectors \((x^V_\omega)_{\omega\in F}\) are independent copies of the full ordinary endogenous vector. In particular, if \(R\) is the ordinary observed law, the structured observed law on \(F\) is \(R^{\otimes F}\). Two ordinary models with the same observed law therefore have equal structured observed laws on every finite cylinder. These cylinders generate the product sigma-algebra, so their full \(P_{\rm obs}\) measures agree, even when \(\Omega\) is uncountable.

After \(do(x^A=a^*)\), recursion at coordinate \(\omega\) is exactly the ordinary recursion after \(do(Z^A=a^*_\omega)\). Thus its outcome marginal is the ordinary interventional law at that coordinate's assigned value. This does not require \(a^*\) to be constant.

If the reduced observed-treatment/observed-outcome query were not derivable by do-calculus, standard completeness would give two ordinary models with equal observed laws and different interventional laws at a specified treatment value. Choose \(\omega_0\in\Omega\) and specify or relabel that witness at \(a^*_{\omega_0}\). The unrestricted state-space and mechanism class admits this specification. The two geometric lifts have equal entire observed laws, but their intervened outcome marginals at \(\omega_0\) differ. Hence their full intervened outcome laws differ.

No functional of \(P_{\rm obs}\) can identify the query throughout the full class in the presence of this pair. Therefore uniform identifiability implies that the reduced query has a do-calculus derivation. Combining that derivation with the removal of causally irrelevant latent interventions gives a derivation for the original query.

All obligations listed above are closed. The only imported theorem-critical results are the explicitly stated standard independent soundness and ordinary nonparametric completeness results.
