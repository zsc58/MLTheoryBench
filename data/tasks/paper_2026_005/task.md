# Problem

## Setup

Fix a context \(x_{<t}\), a finite nonempty vocabulary \(\mathcal V\), an integer \(d\ge1\), and a radius \(r>0\). Use the Euclidean norm on \(\mathbb R^d\). Let \(p_\eta(\cdot\mid x_{<t})\), \(\eta\in\mathbb R^d\), be a regular exponential-family conditional distribution on \(\mathcal V\), expressed in its natural parameter:
\[
p_\eta(v\mid x_{<t})=h(v\mid x_{<t})\exp\{\eta^{\mathsf T}T(v\mid x_{<t})-A(\eta\mid x_{<t})\}.
\]
Here \(h\ge0\) is not identically zero, \(T(v\mid x_{<t})\in\mathbb R^d\), and \(A\) is the log-partition function. Logarithms and scores inside expectations are evaluated on the common support \(\{v\in\mathcal V:h(v\mid x_{<t})>0\}\).

Let \(\eta_{\mathrm{ref}}\) be a fixed reference parameter and write \(q_{\mathrm{ref}}=p_{\eta_{\mathrm{ref}}}\). Assume \(A\) is three-times continuously differentiable on a neighborhood containing the radius-\(r\) ball around \(\eta_{\mathrm{ref}}\), with its third derivative bounded there by a finite constant \(M\) in the multilinear operator norm induced by the Euclidean norm. For \(\|\eta-\eta_{\mathrm{ref}}\|<r\), set \(\delta=\eta-\eta_{\mathrm{ref}}\).

Define the reference natural-parameter score and per-token empirical Fisher matrix by
\[
s_{\mathrm{ref}}(v)=\left.\nabla_\eta\log p_\eta(v\mid x_{<t})\right|_{\eta=\eta_{\mathrm{ref}}},
\qquad
F_{\mathrm{ref}}=\mathbb E_{v\sim q_{\mathrm{ref}}}\!\left[s_{\mathrm{ref}}(v)s_{\mathrm{ref}}(v)^{\mathsf T}\right].
\]
Assume \(F_{\mathrm{ref}}\) is positive definite, and denote its extreme eigenvalues by \(0<\lambda_{\min}(F_{\mathrm{ref}})\le\lambda_{\max}(F_{\mathrm{ref}})\). Let
\[
D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})=\mathbb E_{v\sim p_\eta}\left[\log\frac{p_\eta(v\mid x_{<t})}{q_{\mathrm{ref}}(v\mid x_{<t})}\right].
\]

## Task

Prove that there is a constant \(C\), depending only on the stated local regularity bound, such that for every \(\|\delta\|<r\),
\[
D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})=\tfrac12\delta^{\mathsf T}F_{\mathrm{ref}}\delta+R_3(\delta),\qquad |R_3(\delta)|\le C\|\delta\|^3,
\]
and consequently
\[
\tfrac12\lambda_{\min}(F_{\mathrm{ref}})\|\delta\|^2-C\|\delta\|^3
\le D_{\mathrm{KL}}(p_\eta\|q_{\mathrm{ref}})
\le \tfrac12\lambda_{\max}(F_{\mathrm{ref}})\|\delta\|^2+C\|\delta\|^3.
\]
Moreover, for nonzero \(\delta\), the coefficient of \(\|\delta\|^2\) in the displayed leading quadratic term equals \(\tfrac12\lambda_{\max}(F_{\mathrm{ref}})\) if and only if \(\delta\) lies in the eigenspace associated with \(\lambda_{\max}(F_{\mathrm{ref}})\) (equivalently, is parallel to a dominant eigenvector when that eigenvalue is simple).
