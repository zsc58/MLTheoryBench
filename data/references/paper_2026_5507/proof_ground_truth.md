# Reference Proof

## Proof Structure

1. Derive the equality of the positive and negative coefficient masses and verify the predictor decomposition.
2. Establish uniform upper and lower eigenvalue bounds for each Gaussian-kernel Hessian.
3. Aggregate these bounds to obtain the inclusive convexity threshold, common strong-convexity modulus, and global gradient-Lipschitz bound.
4. Verify existence and feasibility of exact updates, incorporate the constraint through its indicator, and derive constrained DCA descent using finite strong-convexity constants.

## Complete Proof

### Coefficients and decomposition

Complementarity and nonnegativity imply that \(\alpha_i^*=0\) on \(S_+\) and \(\alpha_i=0\) on \(S_-\). In particular, if \(\Delta_i=0\), then both coefficients vanish. Splitting the zero-sum constraint over the two sets gives
\[
\sum_{i\in S_+}\alpha_i=\sum_{i\in S_-}\alpha_i^*=:m.
\]
Consequently, the public total-weight definition gives \(C_\alpha=2m>0\). Expanding the definitions of the two components yields
\[
G(x)=\frac{C_\alpha\rho}{2}\|x\|^2-\sum_{i\in S_-}\alpha_i^*\phi_i(x),\qquad
H(x)=\frac{C_\alpha\rho}{2}\|x\|^2-\sum_{i\in S_+}\alpha_i\phi_i(x).
\]
Their difference is
\[
\widehat f(x)=\sum_{i\in S_+}\alpha_i\phi_i(x)-\sum_{i\in S_-}\alpha_i^*\phi_i(x)
=\sum_{i=1}^n(\alpha_i-\alpha_i^*)\phi_i(x).
\]
Thus this is the bias-free predictor. All sums are finite, and both components are smooth and finite-valued on \(\mathbb R^d\).

### Gaussian Hessian bounds

Fix \(i\), put \(r=x-z_i\), and differentiate:
\[
\nabla^2\phi_i(x)=\phi_i(x)(4\gamma^2rr^\top-2\gamma I).
\]
For any unit vector \(v\),
\[
v^\top\nabla^2\phi_i(x)v
=\phi_i(x)(4\gamma^2\langle r,v\rangle^2-2\gamma).
\]
Since \(0<\phi_i(x)\le1\) and the squared inner product is nonnegative, this is at least \(-2\gamma\). By Cauchy-Schwarz, its upper bound is \(\psi(\|r\|^2)\), where
\[
\psi(u)=e^{-\gamma u}(4\gamma^2u-2\gamma),\qquad u\ge0.
\]
Its derivative is
\[
\psi'(u)=2\gamma^2(3-2\gamma u)e^{-\gamma u}.
\]
Therefore \(\psi\) increases up to \(u=3/(2\gamma)\) and decreases thereafter. Its maximum is \(4\gamma e^{-3/2}\). The Rayleigh-quotient bounds consequently give, for every \(x\),
\[
-2\gamma I\preceq\nabla^2\phi_i(x)\preceq4\gamma e^{-3/2}I.
\]

### Aggregation, convexity, and smoothness

The component Hessians are
\[
\nabla^2G=C_\alpha\rho I-\sum_{i\in S_-}\alpha_i^*\nabla^2\phi_i,\qquad
\nabla^2H=C_\alpha\rho I-\sum_{i\in S_+}\alpha_i\nabla^2\phi_i.
\]
Each weighted kernel sum has nonnegative weights with total mass \(m=C_\alpha/2\). The upper kernel bound thus implies
\[
\nabla^2G,\nabla^2H\succeq
(C_\alpha\rho-4\gamma e^{-3/2}m)I
=C_\alpha(\rho-2\gamma e^{-3/2})I.
\]
At \(\rho\ge2\gamma e^{-3/2}\), both Hessians are positive semidefinite. In particular, \(G\) is convex; subtracting the linear term in each subproblem preserves convexity, and its feasible set is convex. This proves the first claim, including the equality endpoint. Convexity of the individual \(h_i\) is not needed.

For \(\rho>2\gamma e^{-3/2}\), let \(\mu=C_\alpha(\rho-2\gamma e^{-3/2})>0\). The functions \(G-\frac\mu2\|\cdot\|^2\) and \(H-\frac\mu2\|\cdot\|^2\) have positive semidefinite Hessians and hence are convex. Thus both components are \(\mu\)-strongly convex, and \(\sigma(G),\sigma(H)\ge\mu\).

The lower kernel bound similarly implies
\[
\nabla^2G,\nabla^2H\preceq
(C_\alpha\rho+2\gamma m)I=C_\alpha(\rho+\gamma)I=:LI.
\]
Together with positive semidefiniteness, this bounds the operator norms of both Hessians by \(L\). For \(J=G\) or \(J=H\), and any \(a,b\in\mathbb R^d\),
\[
\nabla J(b)-\nabla J(a)=\int_0^1\nabla^2J(a+\theta(b-a))(b-a)\,d\theta.
\]
Taking norms gives \(\|\nabla J(b)-\nabla J(a)\|\le L\|b-a\|\). This proves global gradient Lipschitz continuity with the asserted constant.

### Exact constrained descent

The set \(\Omega\) is nonempty and compact. For every current iterate, the subproblem objective is continuous, so its minimum on \(\Omega\) is attained. Starting from \(x^{(0)}\in\Omega\), all iterates are therefore well-defined and feasible. Under the strict parameter inequality each subproblem is also strongly convex and has a unique minimizer, although uniqueness is not required for the following argument.

Define \(\chi_\Omega(x)=0\) on \(\Omega\) and \(+\infty\) otherwise, and let \(\widetilde G=G+\chi_\Omega\). This is proper closed convex and \(\mu\)-strongly convex, since
\[
\widetilde G-\tfrac\mu2\|\cdot\|^2
=(G-\tfrac\mu2\|\cdot\|^2)+\chi_\Omega
\]
is convex. The update is exact minimization of \(\widetilde G-\langle\nabla H(x^{(t)}),\cdot\rangle\).

Here is an explicit finite-modulus proof of the relevant exact-DCA descent principle. Write \(u=x^{(t)}\), \(v=x^{(t+1)}\), and \(s=\nabla H(u)\). For any \(w\in\Omega\), the segment \(v+\theta(w-v)\), \(0\le\theta\le1\), is feasible. Exact minimality at \(v\) implies that the right derivative at \(\theta=0\) of the subproblem objective along this segment is nonnegative. Hence
\[
\langle\nabla G(v)-s,w-v\rangle\ge0.
\]
Taking \(w=u\) and using strong convexity of \(G\) gives
\[
G(u)\ge G(v)+\langle\nabla G(v),u-v\rangle+\tfrac\mu2\|u-v\|^2
\ge G(v)+\langle s,u-v\rangle+\tfrac\mu2\|u-v\|^2.
\]
Strong convexity of \(H\) gives the complementary inequality
\[
H(v)\ge H(u)+\langle s,v-u\rangle+\tfrac\mu2\|v-u\|^2.
\]
Adding these inequalities cancels the inner products and proves
\[
(G-H)(u)-(G-H)(v)\ge\mu\|v-u\|^2.
\]
This is precisely the required descent inequality, since both iterates are feasible and the indicator vanishes at them.

This argument uses only finite admissible moduli, not the supremal value \(\sigma(\widetilde G)\). For a singleton \(\Omega\), that supremum can be \(+\infty\), but the displayed argument still applies and the step is zero. No nonempty-interior assumption or additional constraint qualification is needed. Repeated training locations and cancellation of the predictor also require no exception. All theorem-critical obligations are closed without an unproved specialized external dependency.
