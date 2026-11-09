# Reference Proof

## Proof Structure

Represent each latent Gaussian as an affine function of a standard normal variable and center every individual error. Absorb the resulting constants and scales into the latent coefficients and biases. Couple the resulting equations to prove observational equality. For positive observational laws, identifiability gives the requested query equality directly. For possibly singular laws, complete the same structural-recursion argument after intervention; this avoids applying the positivity-based identification definition outside its domain.

## Complete Proof

### step_001: Construct the standardized model

Fix a model in class \(\mathcal G\), including its graph \(G=(V\mathbin{\dot\cup}K,E)\). All means, coefficients, and biases are finite real numbers, and \(s_k,\tau_i\geq 0\). Choose mutually independent variables
\[
U_k\sim N(0,1)\quad(k\in K),\qquad
\varepsilon_i\sim N(0,\tau_i^2)\quad(i\in V).
\]
Define
\[
\widetilde U'_k=m_k+s_kU_k,
\qquad
\widetilde\varepsilon'_i=r_i+\varepsilon_i.
\]
Their joint law is exactly the original exogenous law: each component has the required Gaussian distribution, and separate affine transformations preserve independence. If \(s_k=0\), the first expression is the constant \(m_k\); if \(\tau_i=0\), the corresponding centered error is zero. Thus no division by a variance is required.

Set
\[
\gamma_{ki}=\gamma'_{ki}s_k,
\qquad
\mu_i=\mu'_i+r_i+\sum_{k\in L(i)}\gamma'_{ki}m_k,
\]
and retain every observed-parent coefficient \(\beta_{ji}\). Define the new model by
\[
X_i=\sum_{j\in\operatorname{pa}^{o}_G(i)}\beta_{ji}X_j
+\sum_{k\in L(i)}\gamma_{ki}U_k+\mu_i+\varepsilon_i.
\]
These equations use precisely the same specified observed and latent parent lists. In particular, if a latent variance is zero, its new coefficient is zero within the same graphical specification. The claim concerns that specification, not a minimal graph obtained by deleting zero coefficients. The latent variables are independent standard normals; the errors are centered independent Gaussians with diagonal covariance; and the two families are independent. Hence this is a model in \(\mathcal C\) on the required graph.

### step_002: Verify observational equality

On the same probability space, generate a copy \(\widetilde X\) of the original model using \(\widetilde U'\) and \(\widetilde\varepsilon'\). For every node, substitution gives the identity
\[
\sum_{k\in L(i)}\gamma'_{ki}\widetilde U'_k
+\mu'_i+\widetilde\varepsilon'_i
=
\sum_{k\in L(i)}\gamma_{ki}U_k+\mu_i+\varepsilon_i.
\]
Choose a topological order of the observed vertices. For a vertex with no observed parents, this identity gives equality of its two generated values. Inductively, if the observed parents agree, their linear contributions agree as well, and the displayed identity gives equality at the current vertex. Thus \(\widetilde X=X\) almost surely. Since \(\widetilde X\) has the original model's law, the observational laws coincide.

### step_003: Verify the intervention conclusion, including singular laws

If the common observational law admits an everywhere positive Lebesgue density, the two models meet the hypotheses in the public definition of identifiability: they have the same complete graph and the same positive observational law. Therefore every identifiable intervention query has equal values in the two models.

The theorem also permits models whose observational law is singular. Equality of such laws alone does not authorize the preceding use of identifiability. Instead, use the already constructed coupling. Fix arbitrary disjoint \(Y,Z\subseteq V\) and arbitrary \(z\in\mathbb R^Z\). In both coupled models replace the equations for \(Z\) by the same constants \(z\). Traverse the same topological order. At an intervened vertex, the two values agree because both equal the assigned constant. At every other vertex, the exogenous-contribution identity from step_002 is unchanged, and equality of preceding parent values implies equality at that vertex. Consequently, the intervened vectors, and in particular their \(Y\)-coordinates, are equal almost surely. Their probability laws are therefore equal.

This last argument applies whether or not the observational law is positive, and in particular proves the requested equality for every identifiable query in all allowed cases. It is a property of the constructed pair, not a claim about arbitrary observationally equivalent singular models. The standardized model was fixed in step_001 independently of \(Y,Z,z\), so a single model satisfies all the required conclusions. Empty sums have value zero; with \(Z=\varnothing\) the argument reduces to observational equality, and with \(Y=\varnothing\) both laws are the unique law on \(\mathbb R^{\varnothing}\).

## Obligation Closure

The affine representation is verified directly, including zero variances. Independence and class membership follow from the product construction. Graph preservation follows from retention of the specified parent lists. Observational equality and intervention equality are proved by finite topological induction. Identification is invoked only with its positive-law hypothesis verified. No specialized external theorem or unresolved proof obligation is used.
