# Reference Proof

## Proof Structure

First derive the softmax gradient and forward-KL objective directly. Parameterize the affine constraint by its tangent null space and apply first-order optimality to obtain the dual displacement. Then expand the KL sum using the fixed partition and factorization. The binary factor is the concept law appearing in the probe, so its divergence from the initial binary law is constant on the constraint. The remaining objective is exactly the off-target KL, up to a fixed additive term.

## Complete Proof

### 1. Softmax gradient and objective

The output set is finite and nonempty. Every softmax probability is positive, and differentiation of the finite sum gives
\[
\nabla A(\lambda)=\frac{\sum_{y\in\mathcal Y}e^{\lambda^\top\gamma_y}\gamma_y}{\sum_{y\in\mathcal Y}e^{\lambda^\top\gamma_y}}=\sum_{y\in\mathcal Y}P_\lambda(y)\gamma_y.
\]
Write \(\phi_0=\phi(\lambda_0)\). Since
\[
\log\frac{P_{\lambda_0}(y)}{P_\lambda(y)}=(\lambda_0-\lambda)^\top\gamma_y-A(\lambda_0)+A(\lambda),
\]
summing against \(P_{\lambda_0}\) yields
\[
F(\lambda):=D_{\rm KL}(P_{\lambda_0}\|P_\lambda)=A(\lambda)-A(\lambda_0)-\phi_0^\top(\lambda-\lambda_0).
\]
Consequently \(\nabla F(\lambda)=\phi(\lambda)-\phi_0\). Strict convexity and an inverse dual-coordinate map are not needed.

### 2. Dual displacement at every constrained minimizer

Choose \(c_0\in\Lambda_W(c)\), and let \(v_1,\ldots,v_k\) be a basis of \(\ker(\beta_W^\top)\), where \(k\) is its dimension. The constraint is exactly
\[
\lambda(\alpha)=c_0+\sum_{j=1}^k\alpha_jv_j,\qquad \alpha\in\mathbb R^k.
\]
For any constrained minimizer \(\hat\lambda=\lambda(\hat\alpha)\), differentiability and unconstrained first-order optimality in \(\alpha\) give
\[
0=\frac{\partial}{\partial\alpha_j}F(\lambda(\alpha))\bigg|_{\hat\alpha}=(\phi(\hat\lambda)-\phi_0)^\top v_j,\qquad 1\leq j\leq k.
\]
Thus \(u:=\phi(\hat\lambda)-\phi_0\) is orthogonal to \(\ker(\beta_W^\top)\).

If \(\beta_W=0\), nonemptiness of the constraint implies \(c=0\), and the kernel is all of \(\mathbb R^d\). Hence \(u=0\), and the conclusion holds with \(t=0\). If \(\beta_W\ne0\), set \(t=(\beta_W^\top u)/(\beta_W^\top\beta_W)\). Then \(r=u-t\beta_W\) belongs to the kernel. Both \(u\) and \(\beta_W\) are orthogonal to that kernel, so \(r\) is also orthogonal to it. In particular \(r^\top r=0\), and \(u=t\beta_W\). Therefore
\[
\phi(\hat\lambda)=\phi(\lambda_0)+t\beta_W.
\]
If \(k=0\), the stationarity equations form an empty list, and the same argument applies.

### 3. Factorized KL decomposition

For every parameter under consideration, the probe gives a strictly positive binary law: both \(P_\lambda^W(1)\) and \(P_\lambda^W(0)\) lie in \((0,1)\). The factorization and normalization of this binary law imply
\[
P_\lambda^Z(z_i)=\sum_{w=0}^1P_\lambda(y_i^w),\qquad P_\lambda^Z(z_y)=P_\lambda(y)\quad(y\in N_W).
\]
Thus the off-target factor is uniquely determined and strictly positive on every element of \(Z_W\). All KL terms below are finite. If there are no pairs, only the neutral formula is needed.

For brevity, write \(q_0=P_{\lambda_0}^W\), \(q=P_\lambda^W\), \(p_0=P_{\lambda_0}^Z\), and \(p=P_\lambda^Z\). The disjoint, exhaustive partition gives
\[
\begin{aligned}
F(\lambda)
&=\sum_{i=1}^{n_W}\sum_{w=0}^1q_0(w)p_0(z_i)\log\frac{q_0(w)p_0(z_i)}{q(w)p(z_i)}
 +\sum_{y\in N_W}p_0(z_y)\log\frac{p_0(z_y)}{p(z_y)}\\
&=\left(\sum_{i=1}^{n_W}p_0(z_i)\right)\sum_{w=0}^1q_0(w)\log\frac{q_0(w)}{q(w)}
 +\sum_{i=1}^{n_W}p_0(z_i)\log\frac{p_0(z_i)}{p(z_i)}
 +\sum_{y\in N_W}p_0(z_y)\log\frac{p_0(z_y)}{p(z_y)}\\
&=m_0D_{\rm KL}(P_{\lambda_0}^W\|P_\lambda^W)+D_{\rm KL}(P_{\lambda_0}^Z\|P_\lambda^Z),
\end{aligned}
\]
where \(m_0=\sum_{i=1}^{n_W}P_{\lambda_0}^Z(z_i)\). The second equality uses \(\sum_wq_0(w)=1\). Empty sums are zero, so this identity includes an empty pair collection or an empty neutral set.

### 4. Reduction to off-target minimization

By definition, \(P_\lambda^W\) is the same concept law used in the logistic probe. For every \(\lambda\in\Lambda_W(c)\),
\[
P_\lambda^W(1)=\sigma(c+b_W),\qquad P_\lambda^W(0)=1-\sigma(c+b_W).
\]
Hence \(m_0D_{\rm KL}(P_{\lambda_0}^W\|P_\lambda^W)\) is a finite constant on the constraint. For any two feasible parameters, the difference of their full KL objectives therefore equals the difference of their off-target KL objectives. The two objectives have exactly the same constrained minimizers. In particular, every constrained minimizer of the full KL minimizes
\[
D_{\rm KL}(P_{\lambda_0}^Z\|P_\lambda^Z).
\]
Finally, every feasible parameter has target probability \(\sigma(c+b_W)\). When this differs from \(P_{\lambda_0}(W=1)\), every constrained minimizer changes that probability while attaining the stated off-target minimum. No claim of zero off-target divergence, uniqueness, or a prescribed sign of \(t\) is needed.
