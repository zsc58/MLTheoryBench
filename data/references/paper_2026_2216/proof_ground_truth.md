# Reference Proof

## Proof Structure

1. Prove that the small tube is contained in the optimal-greedy-policy set and is invariant under the Bellman operator.
2. Derive an exact stochastic-policy representation of the Bellman error, project away the constant direction, and identify the projected norm with distance to the affine set.
3. Derive the projection-product identity and bound the projected joint spectral radius by the discount factor.
4. Construct a common Lyapunov norm from uniform deterministic product bounds and extend its contraction to stochastic-policy matrices.
5. Obtain the exponential estimate with a constant independent of the initialization.
6. Deduce finite-time tube entrance and permanent optimal greedy-policy identification.

## Complete Proof

### 1. Tube inclusion and invariance

For any two state-action functions U and V, the inequality
\[
\left|\max_a U(s,a)-\max_a V(s,a)\right|\leq\max_a|U(s,a)-V(s,a)|
\]
and the nonnegative transition probabilities with row sums one imply
\[
\|\mathcal BU-\mathcal BV\|_\infty\leq\gamma\|U-V\|_\infty.
\]
Also, directly from the fixed-point equation and the definition of the Bellman operator,
\[
\mathcal B(Q^*+\alpha\mathbf1)=Q^*+\gamma\alpha\mathbf1.
\]

Fix 0<delta<Delta/2, written mathematically as \(0<\delta<\Delta/2\). For any Q, the function \(\alpha\mapsto\|Q-Q^*-\alpha\mathbf1\|_\infty\) is continuous and tends to infinity as \(|\alpha|\to\infty\). Its minimum is therefore attained. If \(Q\in T_\delta\), choose a minimizing alpha so that
\[
Q=Q^*+\alpha\mathbf1+h,\qquad\|h\|_\infty\leq\delta.
\]
For any state with a nonoptimal action and any \(b\notin\Phi^*(s)\),
\[
\max_{a\in\Phi^*(s)}Q(s,a)-Q(s,b)
\geq\Delta_s-2\delta\geq\Delta-2\delta>0.
\]
At every other state all actions are optimal. Thus every greedy action belongs to \(\Phi^*(s)\), regardless of ties among optimal actions, and \(T_\delta\subseteq X^*\).

Writing \(Y=Q^*+\alpha\mathbf1\), the shift identity and Lipschitz estimate give
\[
\operatorname{dist}_\infty(\mathcal BQ,X_1)
\leq\|\mathcal BQ-\mathcal BY\|_\infty
\leq\gamma\|Q-Y\|_\infty\leq\gamma\delta.
\]
Consequently,
\[
\mathcal B(T_\delta)\subseteq T_{\gamma\delta}\subseteq T_\delta.
\]

### 2. Exact error representation and projection

Let \(e_k=Q_k-Q^*\), and for each state define
\[
d_k(s)=\max_a Q_k(s,a)-\max_a Q^*(s,a).
\]
The pointwise bounds on \(e_k(s,a)\) imply
\[
\min_a e_k(s,a)\leq d_k(s)\leq\max_a e_k(s,a).
\]
Every number in this interval is a convex combination of the finitely many action errors. Thus there are nonnegative numbers \(\mu_k(a\mid s)\), summing to one over a at each state, such that
\[
d_k(s)=\sum_a\mu_k(a\mid s)e_k(s,a).
\]
For any such stochastic policy mu, define its linear action-selection operator by
\[
(\Pi^\mu x)(s)=\sum_a\mu(a\mid s)x(s,a),
\qquad A_\mu=\gamma P\Pi^\mu.
\]
Subtracting the fixed-point equation from the Bellman update gives the exact recursion
\[
e_{k+1}=\gamma P d_k=A_{\mu_k}e_k.
\]
The policies \(\mu_k\) are auxiliary representations, not policies executed by the iteration, and need not equal its greedy policies.

Every \(P\Pi^\mu\) is row-stochastic, so \(A_\mu\mathbf1=\gamma\mathbf1\). Put
\[
\alpha_k=\frac1m\mathbf1^\top e_k,\qquad z_k=\Pi_\perp e_k,
\qquad e_k=\alpha_k\mathbf1+z_k.
\]
Projection annihilates the constant component and yields
\[
z_{k+1}=\Pi_\perp A_{\mu_k}z_k
=\Pi_\perp A_{\mu_k}\Pi_\perp z_k
=:\bar A_{\mu_k}z_k.
\]
Orthogonal projection onto \(\mathbf1^\perp\) also gives
\[
\operatorname{dist}_2(Q_k,X_1)=\|z_k\|_2.
\]

### 3. Projected products and the JSR upper bound

For each deterministic mode, \((I-\Pi_\perp)x\) is a constant vector and \(A_i\mathbf1=\gamma\mathbf1\). Hence
\[
\Pi_\perp A_i(I-\Pi_\perp)=0,
\qquad \Pi_\perp A_i=\Pi_\perp A_i\Pi_\perp=\bar A_i.
\]
Induction on the positive integer j now proves
\[
\bar A_{i_j}\cdots\bar A_{i_1}
=\Pi_\perp A_{i_j}\cdots A_{i_1}.
\]
Indeed, multiplying the length-j identity on the left by \(\bar A_i\) and using \(\Pi_\perp A_i\Pi_\perp=\Pi_\perp A_i\) gives the length-(j+1) identity.

Each full product \(A_{i_j}\cdots A_{i_1}\) is \(\gamma^j\) times a row-stochastic matrix. Its infinity operator norm is therefore \(\gamma^j\), and
\[
\|\bar A_{i_j}\cdots\bar A_{i_1}\|_\infty
\leq\|\Pi_\perp\|_\infty\gamma^j.
\]
For an m-by-m matrix D, \(\|D\|_{2\to2}\leq\sqrt m\|D\|_\infty\), as follows from the corresponding vector norm inequalities. Taking maxima over words, jth roots, and limits in the displayed product bound proves
\[
0\leq\bar\rho\leq\gamma<1.
\]

### 4. Common norm and stochastic-policy extension

Fix \(\varepsilon\in(0,1-\bar\rho)\), put \(\beta=\bar\rho+\varepsilon\), and choose \(\eta\) with \(\bar\rho<\eta<\beta\). For j at least one, let
\[
G_j=\max_{i_1,\ldots,i_j}\|\bar A_{i_j}\cdots\bar A_{i_1}\|_{2\to2},
\qquad G_0=1.
\]
By the JSR definition, there is an integer \(J\geq1\) such that \(G_j\leq\eta^j\) for every \(j\geq J\). Set
\[
C=\max\bigl(\{1\}\cup\{\eta^{-j}G_j:0\leq j<J\}\bigr).
\]
Then \(G_j\leq C\eta^j\) for all \(j\geq0\).

For \(x\in W:=\mathbf1^\perp\), define
\[
h_0(x)=\|x\|_2,\qquad
h_j(x)=\max_{i_1,\ldots,i_j}\|\bar A_{i_j}\cdots\bar A_{i_1}x\|_2\quad(j\geq1),
\]
and
\[
p(x)=\left(\sum_{j=0}^\infty\beta^{-2j}h_j(x)^2\right)^{1/2}.
\]
The product bound gives
\[
\|x\|_2\leq p(x)\leq L\|x\|_2,
\qquad L=\frac{C}{\sqrt{1-(\eta/\beta)^2}}<\infty.
\]
Each \(h_j\) is a seminorm: absolute homogeneity is immediate, and the triangle inequality follows by applying the Euclidean triangle inequality to each product and then taking the maximum. The finite partial sums defining p satisfy the triangle inequality by the Euclidean triangle inequality for the vector of weighted seminorms. Passing to the finite limit proves the triangle inequality for p. Absolute homogeneity follows termwise, and positive definiteness follows from \(h_0(x)=\|x\|_2\). Thus p is a norm on W.

For every deterministic mode i, \(h_j(\bar A_i x)\leq h_{j+1}(x)\). Consequently,
\[
p(\bar A_i x)^2
\leq\sum_{j=0}^\infty\beta^{-2j}h_{j+1}(x)^2
=\beta^2\bigl(p(x)^2-\|x\|_2^2\bigr)
\leq\beta^2p(x)^2.
\]

For a stochastic policy mu, assign each deterministic policy pi the weight
\[
w_\pi=\prod_{s\in S}\mu(\pi(s)\mid s).
\]
These weights are nonnegative and sum to one by expanding the product of the statewise probability sums. Moreover,
\[
\sum_{\pi:\pi(s)=a}w_\pi=\mu(a\mid s).
\]
It follows row by row that
\[
\Pi^\mu=\sum_\pi w_\pi\Pi^\pi,
\qquad \bar A_\mu=\sum_\pi w_\pi\bar A_\pi.
\]
The norm triangle inequality and deterministic contraction therefore give
\[
p(\bar A_\mu x)
\leq\sum_\pi w_\pi p(\bar A_\pi x)
\leq\beta p(x).
\]

### 5. Uniform exponential distance estimate

Applying this contraction to the exact projected recursion yields
\[
p(z_k)\leq\beta^k p(z_0).
\]
Combining this with the explicit norm bounds gives
\[
\|z_k\|_2\leq L\beta^k\|z_0\|_2.
\]
The distance identity proves the required estimate with \(c_\varepsilon=L\). This constant depends on the fixed matrix family and epsilon, not on the initialization or k. The estimate includes k=0 and \(z_0=0\), without any division by the initial distance.

### 6. Finite entrance and permanent identification

Fix \(0<\delta<\Delta/2\). If \(z_0=0\), then \(Q_0\in X_1\subseteq T_\delta\), so K=0 is valid by tube invariance. Otherwise, since \(0<\beta<1\), choose an integer K such that
\[
c_\varepsilon\beta^K\|z_0\|_2<\delta.
\]
The particular point \(Q^*+\alpha_K\mathbf1\in X_1\) gives
\[
\operatorname{dist}_\infty(Q_K,X_1)
\leq\|z_K\|_\infty\leq\|z_K\|_2<\delta.
\]
Thus \(Q_K\in T_\delta\), and tube invariance gives \(Q_k\in T_\delta\subseteq X^*\) for every \(k\geq K\). The tie-broken greedy actions are therefore optimal at all states from time K onward. This conclusion uses tube entrance; it does not require or assert invariance of X* itself.
