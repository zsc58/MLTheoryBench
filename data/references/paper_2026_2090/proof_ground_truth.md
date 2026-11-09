# Reference Proof

## Proof Structure

Check that both perturbed evaluations are defined and that the relevant expectations have an unambiguous meaning. For either perturbation regime, perfect prediction makes the unperturbed quadratic loss zero, so the importance is the expected squared prediction change. The definitions of the unrestricted and conditional total indices then identify the two expectations, each with a factor of two.

## Complete Proof

Fix $j$. Let $\widetilde X_j$ denote either perturbation draw and write $\widetilde X=(\widetilde X_j,X_{-j})$, with the replacement in coordinate $j$. Both vectors take values in the product domain of the fixed measurable, real-valued predictor $g$. Thus their predictions and their squared difference are measurable and finite pointwise, and the squared difference has a well-defined expectation in $[0,+\infty]$.

Since $Y=g(X)$ almost surely and the loss is $\ell(y,a)=(y-a)^2$, we have
\[
\ell(Y,g(X))=(g(X)-g(X))^2=0
\]
almost surely. Therefore, by the definition of population permutation importance,
\[
\nu_j=\mathbb E\!\left[\ell(Y,g(\widetilde X))-\ell(Y,g(X))\right]
=\mathbb E\!\left[(g(X)-g(\widetilde X_j,X_{-j}))^2\right].
\]
There is no subtraction of two infinite quantities: the baseline loss is zero. This also agrees with the source's difference of expected losses.

For unrestricted marginal resampling, $\widetilde X_j^{\,\mathrm{ind}}$ is independent of $X$ with the marginal law of $X_j$. Hence its joint law with $X$ is the product of that marginal law and the original joint feature law, exactly the sampling law in the unrestricted index definition. By definition,
\[
\tau'_j=\frac12\,\mathbb E\!\left[(g(X)-g(\widetilde X_j^{\,\mathrm{ind}},X_{-j}))^2\right].
\]
Substitution gives
\[
\nu_j^{\mathrm{ind}}
=\mathbb E\!\left[(g(X)-g(\widetilde X_j^{\,\mathrm{ind}},X_{-j}))^2\right]
=2\tau'_j.
\]
This equality remains valid if the common expectation is infinite. Square integrability under the original joint feature law is not used to assert square integrability under marginal resampling.

For conditional resampling, $\widetilde X_j^{\,\mathrm{cond}}$ is conditionally independent of $X_j$ given $X_{-j}$ and has conditional law $X_j\mid X_{-j}$. Thus, given the original vector, the replacement is a fresh draw from the conditional law determined by $X_{-j}$. This is exactly the sampling law in the dependent-feature index definition. By definition,
\[
\tau_j=\frac12\,\mathbb E\!\left[(g(X)-g(\widetilde X_j^{\,\mathrm{cond}},X_{-j}))^2\right].
\]
Consequently,
\[
\nu_j^{\mathrm{cond}}
=\mathbb E\!\left[(g(X)-g(\widetilde X_j^{\,\mathrm{cond}},X_{-j}))^2\right]
=2\tau_j.
\]

For completeness, this conditional expectation is finite under the stated square-integrability assumption. For every nonnegative measurable function $h$, conditioning on $X_{-j}$ and using the specified conditional law gives
\[
\mathbb E[h(\widetilde X_j^{\,\mathrm{cond}},X_{-j})]
=\mathbb E\!\left[\int h(t,X_{-j})\,\mathbb P(X_j\in dt\mid X_{-j})\right]
=\mathbb E[h(X)].
\]
Taking $h=g^2$ and using $(a-b)^2\leq 2a^2+2b^2$ yields
\[
\mathbb E[(g(X)-g(\widetilde X_j^{\,\mathrm{cond}},X_{-j}))^2]
\leq 4\mathbb E[g(X)^2]<\infty.
\]
The two target identities require no division by a variance and therefore include constant predictors and degenerate feature laws. These identities establish all parts of the theorem.
