# Reference Proof

## Proof Structure

Use finite-dimensional transport duality and complementary slackness to identify transported target points with active affine pieces of a max-affine convex potential. In the discrete case, averaging the active-piece subgradient inequalities gives the same inequality for each indexed barycentric value. In the semi-discrete case, every selected active target satisfies a subgradient inequality at every point. Summing these inequalities in the appropriate cyclic direction gives both conclusions.

## Complete Proof

Write \(c(x,y)=\tfrac12\|x-y\|^2\). For a finite cyclic list, expansion of this cost gives
\[
\sum_t c(x_t,w_t)-\sum_t c(x_t,w_{t+1})
=-\sum_t\langle x_t,w_t\rangle+\sum_t\langle x_t,w_{t+1}\rangle,
\]
because the source and target squared-norm terms cancel separately. Thus the task's inner-product convention agrees with the squared-cost convention.

The semi-discrete objective is a finite real number for every \(g\in\mathbb R^m\). Indeed, its integrand is bounded below by \(-\max_l g_l\) and above by
\[
c(x,v_1)-g_1\leq \|x\|^2+\|v_1\|^2+|g_1|.
\]
Both bounds are integrable under the stated second-moment assumption. The objective's maximizer is stipulated; proving semi-discrete dual attainment is not an additional target.

For a finite convex function \(H\), the notation \(w\in\partial H(x)\) means
\[
H(z)\geq H(x)+\langle w,z-x\rangle\qquad\text{for every }z\in\mathbb R^d.
\]
We will establish this inequality directly for both constructions.

### Discrete Construction

The finite transport feasible set is nonempty: \(Q_{ij}=1/(nm)\) has the required marginals. It is closed and bounded, all costs are finite, and its objective therefore has a finite attained minimum.

The standard finite-dimensional transportation LP duality result used here states that this minimum equals the attained maximum
\[
\max_{f\in\mathbb R^n,\,h\in\mathbb R^m}
\left\{\frac1n\sum_i f_i+\frac1m\sum_j h_j:
 f_i+h_j\leq c(x_i,y_j)\text{ for all }i,j\right\}.
\]
Its hypotheses are precisely the finite real cost matrix, nonempty primal feasible set, and finite optimum verified above. Choose an optimal dual pair \((f,h)\). Equality of primal and dual values gives
\[
0=\sum_{i,j}Q^*_{ij}\bigl(c(x_i,y_j)-f_i-h_j\bigr).
\]
Every summand is nonnegative. Consequently,
\[
Q^*_{ij}>0\quad\Longrightarrow\quad f_i+h_j=c(x_i,y_j).
\]
This explicitly derives complementary slackness for the supplied optimizer.

Define
\[
\Phi(x)=\max_{1\leq j\leq m}
\left\{\langle x,y_j\rangle-\tfrac12\|y_j\|^2+h_j\right\}.
\]
A finite maximum of finite affine functions is finite, proper, and convex. Expanding the dual inequalities yields
\[
\langle x_i,y_j\rangle-\tfrac12\|y_j\|^2+h_j
\leq \tfrac12\|x_i\|^2-f_i,
\]
with equality whenever \(Q^*_{ij}>0\). Each row has positive total mass \(1/n\), hence at least one positive entry. It follows that every active target \(y_j\) indexes an affine piece attaining \(\Phi(x_i)\).

For such an active target and every \(z\), comparison with its affine piece gives
\[
\Phi(z)\geq\Phi(x_i)+\langle y_j,z-x_i\rangle.
\]
Multiply these inequalities by \(nQ^*_{ij}\) and sum over active targets. These coefficients are nonnegative and sum to one, so
\[
\Phi(z)\geq\Phi(x_i)+\left\langle n\sum_jQ^*_{ij}y_j,z-x_i\right\rangle
=\Phi(x_i)+\langle t_i,z-x_i\rangle.
\]
Thus \(t_i\in\partial\Phi(x_i)\) for every row \(i\). This conclusion is about the indexed relation \(\{(x_i,t_i)\}\); it does not require different rows at the same source location to have the same barycenter.

### Semi-Discrete Construction

Define
\[
\Psi(x)=\max_{1\leq j\leq m}
\left\{\langle x,v_j\rangle-\tfrac12\|v_j\|^2+g_j\right\}.
\]
Again this is a finite, proper convex function. Expanding the squared distances shows that \(x\in C_j(g)\) if and only if the \(j\)-th affine term attains this maximum. Hence, whenever \(x\in C_j(g)\), for every \(z\),
\[
\Psi(z)\geq\Psi(x)+\langle v_j,z-x\rangle.
\]
At every \(x\), the selection condition supplies an index \(j\) with \(S_g(x)=v_j\) and \(x\in C_j(g)\). Therefore
\[
\Psi(z)\geq\Psi(x)+\langle S_g(x),z-x\rangle
\qquad\text{for all }x,z\in\mathbb R^d.
\]
In particular, \(S_g(x)\in\partial\Psi(x)\) everywhere, not merely almost everywhere. This also covers boundary ties and repeated target points. The cells are closed and cover \(\mathbb R^d\), since a minimum of finitely many real numbers is attained. A smallest-active-index rule is a measurable selection, and any other stipulated measurable active-target selection satisfies the same pointwise inequality. Neither optimality of \(g\) nor an assertion that \(S_g\) pushes \(\mu\) to \(\nu\) is needed for this step.

### Exact Cyclic Inequality

Let \((x_t,w_t)_{t=1}^{\ell}\) be any cyclic list satisfying \(w_t\in\partial H(x_t)\), and put \(x_0=x_\ell\). Apply the subgradient inequality at \(x_t\) to the preceding point:
\[
H(x_{t-1})\geq H(x_t)+\langle w_t,x_{t-1}-x_t\rangle.
\]
Summing cancels all function values and gives
\[
\sum_{t=1}^{\ell}\langle x_t,w_t\rangle
\geq\sum_{t=1}^{\ell}\langle x_{t-1},w_t\rangle
=\sum_{t=1}^{\ell}\langle x_t,w_{t+1}\rangle,
\qquad w_{\ell+1}=w_1.
\]
This is exactly the convention in the task. Apply it first to the indexed discrete relation with \(H=\Phi\), and then to the full graph of \(S_g\) with \(H=\Psi\). Both graphs are cyclically monotone.

## Obligation Closure

The finite objective and discrete feasibility checks are explicit. The only invoked independent theorem is finite-dimensional transportation LP duality, whose relevant statement and hypotheses are given above. Complementary slackness, both subgradient inclusions, barycentric preservation, and cyclic monotonicity are explicitly derived. The semi-discrete optimizer is a stipulated object, not an unproved existence conclusion. No nonstandard dependency or unresolved theorem-critical obligation remains.
