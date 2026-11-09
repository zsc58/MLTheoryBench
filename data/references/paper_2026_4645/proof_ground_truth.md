# Reference Proof

## Proof Structure

Verify the density and logarithm domains, express the score difference of the two Boltzmann densities in terms of the PMF gradient error, and identify the relative Fisher divergence. Its finiteness verifies the remaining hypothesis for applying the stated logarithmic Sobolev inequality. Substitute to obtain the required bound.

## Complete Proof

### step_001 — Density domains and divergences

The positive finite normalizers make \(p_\eta\) and \(p^*\) probability densities. Since the potentials are real-valued and differentiable, both densities are strictly positive and differentiable on \(\mathbb R^d\). Their logarithms and log-density ratio are therefore defined and differentiable. Absolute continuity is stated in the task and also follows from positivity here.

Use the public definition
\[
D_{\mathrm{KL}}(p_\eta\|p^*)
=\int_{\mathbb R^d}p_\eta(R)\log\frac{p_\eta(R)}{p^*(R)}\,dR.
\]
This is well-defined as an extended integral: with \(f=p_\eta/p^*\), its negative part is bounded by \(\int p^*/e=1/e\), using \(t\log t\geq-1/e\). No separate integrability assumption on either potential is needed. Finiteness of KL will follow from LSI, rather than from absolute continuity alone.

Define the relative Fisher divergence by
\[
J(p_\eta\|p^*)
=\int_{\mathbb R^d}p_\eta(R)
\left\|\nabla_R\log\frac{p_\eta(R)}{p^*(R)}\right\|_2^2\,dR.
\]

### step_002 — Score difference

The normalizing constants do not depend on \(R\). Differentiating the logarithms of the Boltzmann densities gives
\[
\nabla_R\log p_\eta(R)=-\beta\nabla_R U_\eta(R),
\qquad
\nabla_R\log p^*(R)=-\beta\nabla_R U^*(R).
\]
Consequently,
\[
\nabla_R\log\frac{p_\eta(R)}{p^*(R)}
=-\beta\bigl(\nabla_R U_\eta(R)-\nabla_R U^*(R)\bigr).
\]

### step_003 — Relative Fisher divergence and finiteness

Squaring the norm and integrating under \(p_\eta\) yields
\[
J(p_\eta\|p^*)
=\beta^2\int_{\mathbb R^d}p_\eta(R)
\left\|\nabla_R U_\eta(R)-\nabla_R U^*(R)\right\|_2^2\,dR
=\beta^2\mathbb E_{R\sim p_\eta}
\left[\left\|\nabla_R U_\eta(R)-\nabla_R U^*(R)\right\|_2^2\right]
<\infty.
\]
The last assertion is precisely the stated gradient-error integrability assumption. It does not require either force separately to have a finite second moment.

### step_004 — Apply the stated LSI

The density \(q=p_\eta\) is normalized, strictly positive, differentiable, and absolutely continuous with respect to \(p^*\), by step_001. Its relative-score integral is finite by step_003. It therefore belongs to the explicitly specified test class in the public LSI assumption. Applying that assumption gives
\[
D_{\mathrm{KL}}(p_\eta\|p^*)\leq\frac{1}{2\rho}J(p_\eta\|p^*).
\]
In particular, KL is finite. LSI is an assumed inequality with its full relevant statement supplied in the task; no external proof of LSI or additional theorem is being invoked.

### step_005 — Conclude

Substitution of step_003 gives
\[
D_{\mathrm{KL}}(p_\eta\|p^*)\leq
\frac{\beta^2}{2\rho}\,
\mathbb E_{R\sim p_\eta}
\left[\left\|\nabla_R U_\eta(R)-\nabla_R U^*(R)\right\|_2^2\right],
\]
which is exactly the required inequality. No division by the error is used, so the zero-error case is included.

## Dependency and Obligation Audit

The five obligations above are closed explicitly. The source supplies the KL and relative Fisher definitions at L000355–L000360, the score calculation at L000361–L000363, the Fisher substitution at L000364–L000370, and the LSI application and conclusion at L000372–L000376. The density-domain checks and the extended-integral observation are routine local clarifications. The conditional projected-force identity and the force-matching objective are contextual, not premises of this proof. In particular, this proof does not identify an equilibrium-data training loss with the error integrated under the learned distribution. There are no unresolved theorem-critical proof obligations.
