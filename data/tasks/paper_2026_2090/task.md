# Problem

## Setup

Let $d\geq 1$ be an integer and let $X=(X_1,\ldots,X_d)$ be a real random feature vector. For each $i$, let $\mathcal X_i$ be the marginal support of $X_i$, and put $\mathcal X=\prod_{i=1}^d\mathcal X_i$. Let $g:\mathcal X\to\mathbb R$ be a fixed measurable predictor with $\mathbb E[g(X)^2]<\infty$. Assume a perfect predictor, $Y=g(X)$ almost surely, and use the quadratic loss $\ell(y,a)=(y-a)^2$. Fix $j\in\{1,\ldots,d\}$. Write $X_{-j}$ for the vector with coordinate $j$ removed, and write $g(t,X_{-j})$ for evaluation after replacing coordinate $j$ by $t$.

For an independent perturbation, let $\widetilde X_j^{\,\mathrm{ind}}$ be independent of $X$ and distributed as $X_j$. For a conditional perturbation, let $\widetilde X_j^{\,\mathrm{cond}}$ be conditionally independent of $X_j$ given $X_{-j}$ and have conditional law $X_j\mid X_{-j}$. Define population permutation importance under either perturbation by
\[
\nu_j^{\bullet}=\mathbb E\left[\ell\bigl(Y,g(\widetilde X_j^{\,\bullet},X_{-j})\bigr)-\ell\bigl(Y,g(X)\bigr)\right],
\]
where $\bullet\in\{\mathrm{ind},\mathrm{cond}\}$. Define the unrestricted and dependent-feature total indices by
\[
\tau'_j=\frac12\mathbb E\left[(g(X)-g(\widetilde X_j^{\,\mathrm{ind}},X_{-j}))^2\right],
\qquad
\tau_j=\frac12\mathbb E\left[(g(X)-g(\widetilde X_j^{\,\mathrm{cond}},X_{-j}))^2\right].
\]
These quantities and the equalities below are interpreted in $[0,+\infty]$, with $2(+\infty)=+\infty$.

## Task

Prove the integrated theorem that, under these assumptions,
\[
\nu_j^{\mathrm{ind}}=\mathbb E\left[(g(X)-g(\widetilde X_j^{\,\mathrm{ind}},X_{-j}))^2\right]=2\tau'_j,
\]
and
\[
\nu_j^{\mathrm{cond}}=\mathbb E\left[(g(X)-g(\widetilde X_j^{\,\mathrm{cond}},X_{-j}))^2\right]=2\tau_j.
\]
