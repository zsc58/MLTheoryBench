# Problem

## Setup

Let \(D=(V,E)\) be a known finite directed acyclic graph, and fix a known observed vertex set \(O\subseteq V\). Vertices in \(V\setminus O\) are latent. Write \(\mathrm{pa}(v)\) for the parents of \(v\).

Let \(\Omega\) be a common index set. A known group \((G,\cdot)\) acts on \(\Omega\) by bijections. Its action on every indexed field is the index transform
\[
(\phi x)_\omega=x_{\phi^{-1}(\omega)}.
\]
The identity acts trivially, and composition agrees with the group product. Every group element acts in this way, including on the noise fields.

For a model specification, choose measurable coordinate state spaces \(X^v\) and noise spaces \(E^v\), with probability laws \(\mu_v\) on \(E^v\). Equip all field spaces and finite products of field spaces with their product sigma-algebras. The endogenous field at vertex \(v\) is
\[
x^v=(x^v_\omega)_{\omega\in\Omega}\in(X^v)^\Omega.
\]
Its exogenous field \(\varepsilon^v\in(E^v)^\Omega\) has product law \(\mu_v^\Omega\). The exogenous fields are mutually independent.

A map is equivariant when \(f(\phi z)=\phi f(z)\). A geometric structural causal model has measurable mechanisms
\[
f^v:\left(\prod_{u\in\mathrm{pa}(v)}(X^u)^\Omega\right)\times(E^v)^\Omega\longrightarrow(X^v)^\Omega
\]
and recursive equations
\[
x^v=f^v(x^{\mathrm{pa}(v)},\varepsilon^v),
\]
with
\[
f^v(\phi x^{\mathrm{pa}(v)},\phi\varepsilon^v)
=\phi f^v(x^{\mathrm{pa}(v)},\varepsilon^v)
\]
for every \(\phi\in G\). The associated geometric causal graphical model has kernels
\[
K_v(B\mid z)=\int 1_B(f^v(z,e))\,\mu_v^\Omega(de)
\]
for measurable \(B\subseteq(X^v)^\Omega\), and joint law given by their DAG product. Its observational distribution is the marginal
\[
P_{\rm obs}=P^{x^O}.
\]
The observational distribution is supplied as a probability measure; the task does not concern estimating it from a realization.

For disjoint vertex sets \(A,Y\subseteq V\) and an assigned field
\[
a^*\in\prod_{v\in A}(X^v)^\Omega,
\]
the intervention \(do(x^A=a^*)\) replaces the mechanisms at vertices in \(A\) by the assigned values. Equivalently, it replaces their kernels by point masses and leaves all other mechanisms unchanged. The assignment may vary across coordinates. Denote the resulting outcome law by
\[
Q_{a^*}=P(x^Y\in\cdot\mid do(x^A=a^*)).
\]

Here the **whole model class** for identification is the unrestricted nonparametric class for the fixed graph, observed set, index set, and index action: coordinate and noise state spaces are not externally cardinality-restricted, and all measurable mechanisms and noise laws satisfying the preceding definitions are allowed. A functional is understood as a type-compatible family as these state spaces and assigned values vary. It may depend on the known graph, observed set, action, state-space specification, and assigned value, but not on unknown mechanisms or noise laws except through \(P_{\rm obs}\). Uniform identification requires the same such family to give \(Q_{a^*}\) throughout this whole class; it does not mean identification only at one observational law or within an additionally restricted family.

For evaluation of an identification formula, impose the following conditional-existence and support convention. Each observational conditional \(P_{\rm obs}(dz\mid w)\) used in the formula has a regular conditional probability kernel. Every measure \(\nu\) against which its conditioning argument \(w\) is evaluated is absolutely continuous with respect to the corresponding observational conditioning marginal \(P_{\rm obs}^W\). This includes \(\nu=\delta_w\) for a point evaluation, and applies for almost every outer integration argument when the formula has nested integrations. Conditional ratios, if used, have nonzero denominators at their evaluated arguments. These evaluation conditions apply to the soundness formula; they do not restrict the whole model class in the completeness assertion.

## Task

Prove the following integrated theorem.

**Soundness.** Whenever a valid do-calculus derivation on \(D\) identifies the effect using the observed vertices \(O\), its observational functional \(\psi_{a^*}\), evaluated under the stated conditional-existence and support conditions, satisfies
\[
Q_{a^*}=\psi_{a^*}(P_{\rm obs}).
\]

**Completeness.** For the index-transform actions specified above, if the interventional distribution is uniformly identifiable over the whole model class as any functional of the observational distribution, then a do-calculus derivation identifying it from \(P_{\rm obs}\) exists.
