# Problem

## Setup

Let \(V\) and \(K\) be disjoint finite sets indexing observed and latent variables, respectively. Let \(G=(V\mathbin{\dot\cup}K,E)\) be a directed acyclic graph whose edges are either between observed vertices or from latent vertices to observed vertices. For \(i\in V\), write
\[
\operatorname{pa}^{o}_G(i)=\{j\in V:(j,i)\in E\},
\qquad
L(i)=\{k\in K:(k,i)\in E\}.
\]
The graph specifies permitted parent arguments; coefficients on specified edges may be zero. Having the same graph means having these same observed and latent parent lists, not merely the same observed directed edges.

An SCM on this graph has real latent variables \((U_k)_{k\in K}\), real individual errors \((\varepsilon_i)_{i\in V}\), and one real observed variable \(X_i\) for each \(i\in V\). All latent variables and individual errors are mutually independent. Each structural equation is a Borel-measurable function of the listed observed parents, listed latent parents, and that variable's individual error. The individual errors are implicit in the graphical specification.

A **general Gaussian linear SCM** (class \(\mathcal G\)) on \(G\) has
\[
U'_k\sim N(m_k,s_k^2),\qquad
\varepsilon'_i\sim N(r_i,\tau_i^2),
\]
and structural equations
\[
X_i=\sum_{j\in\operatorname{pa}^{o}_G(i)}\beta_{ji}X_j
+\sum_{k\in L(i)}\gamma'_{ki}U'_k+\mu'_i+\varepsilon'_i.
\]
The entire family \((U'_k)_{k\in K},(\varepsilon'_i)_{i\in V}\) is mutually independent. All means, coefficients, and biases are finite real numbers, and \(s_k,\tau_i\) are finite nonnegative real numbers. We allow \(N(a,0)\), meaning the point mass at \(a\).

A **standardized-exogenous Gaussian linear SCM** (class \(\mathcal C\)) on \(G\) has mutually independent \(U_k\sim N(0,1)\) and centered Gaussian individual errors \(\varepsilon_i\), with the two families independent of one another. Its equations have the same linear form and the same parent lists, with arbitrary finite real coefficients and biases. The error variances are arbitrary finite nonnegative numbers, so their covariance matrix is diagonal.

For disjoint \(Y,Z\subseteq V\) and \(z\in\mathbb R^Z\), define the intervention law
\[
Q^M_{Y,Z}(z)=\mathcal L_M\bigl(X_Y\mid\operatorname{do}(X_Z=z)\bigr)
\]
by deleting the structural equations for vertices in \(Z\) and substituting \(X_Z=z\) in the remaining equations. This is a probability measure on \(\mathbb R^Y\); notation such as \(P(y\mid\operatorname{do}(z))\) denotes this law rather than the probability of a singleton.

The intervention query \(Q_{Y,Z}\) is **identifiable from \(G\)** if every pair of SCMs on this graphical specification, not necessarily linear or Gaussian, that have the same observational law admitting an everywhere strictly positive Lebesgue density on \(\mathbb R^V\) satisfies
\[
Q^{M_1}_{Y,Z}(z)=Q^{M_2}_{Y,Z}(z)
\quad\text{for every }z\in\mathbb R^Z.
\]
This positivity condition specifies the comparison domain in the definition of identifiability; it is not imposed on every model in \(\mathcal G\) or \(\mathcal C\).

Empty sums equal zero, and \(\mathbb R^{\varnothing}\) is a singleton with its usual probability measure.

## Task

Prove the following integrated theorem.

For every model \(M'\) in class \(\mathcal G\) on \(G\), there exists a model \(M\) in class \(\mathcal C\) on the same graph such that their observational distributions on \(X\) are equal. Moreover, this same model \(M\) satisfies
\[
Q^{M'}_{Y,Z}(z)=Q^M_{Y,Z}(z)
\]
for every disjoint \(Y,Z\subseteq V\), every intervention query \(Q_{Y,Z}\) identifiable from \(G\), and every \(z\in\mathbb R^Z\).
