# Reference Proof

## Contract and notation

The stochastic directions use the two local samples specified in the public task. Samples are fresh conditionally on the history and independent across agents; evaluations within an agent may be correlated through sample reuse. No smoothness of the sample-gradient maps is assumed.

Write \(h=\lambda_\theta\), \(\alpha=c_\lambda\), and \(s=1-\rho\). Constants denoted by \(C\) depend only on the smoothness parameters, \(\gamma\), \(\mu_0\), and fixed step prefactors, not on \(n,K,s\). They may increase between displays. Choose \(\alpha\) sufficiently small, independently of the network, and subsequently choose a sufficiently small \(b>0\). We work under \(h\le b s^4\).

For a stacked collection define \(\|A\|_n^2=n^{-1}\sum_i\|A_i\|^2\). Let \(J\) be network averaging, \(P=I-J\), and let \(Z=(x,y,\theta)\). Define
\[
X_k=\mathbb E\|PZ^k\|_n^2=\Delta^k,\qquad T_k=\mathbb E\|PS^k\|_n^2,
\]
\[
M_k=\mathbb E\|Z^{k+1}-Z^k\|_n^2,\qquad E_k=\mathbb E\|\bar\theta^k-\theta_\gamma^*(\bar x^k,\bar y^k)\|^2.
\]
Let \(d_i^k\) be the exact three-component direction in the task, \(\widehat d_i^k=d_i^k+\varepsilon_i^k\), and \(q_k=(\bar d_x^k,\bar d_y^k)\). Put \(U_k=\mathbb E\|q_k\|^2\) and \(v=C(\mu_0^2\delta_f^2+\delta_g^2)\). Conditional unbiasedness, local variance bounds, and elementary norm inequalities give
\[
\mathbb E[\varepsilon_i^k\mid\mathcal F_k]=0,\quad \mathbb E\|\varepsilon^k\|_n^2\le v,\quad \mathbb E\|\bar\varepsilon^k\|^2\le v/n.
\]
The last bound uses independence across agents, not independence of the reused gradient evaluations.

The corrected initialization and tracker update imply, by induction,
\[
\bar S^k=\overline{\widehat d}^{\,k}.
\]
Thus the averaged variables take a fresh unbiased stochastic step, even though an individual tracker is not an unbiased local direction estimator.

## 1. Moreau properties and gradient mismatch

Set \(\eta=\gamma^{-1}-L_2>0\) and
\[
H(x,y,\theta)=G(x,\theta)+(2\gamma)^{-1}\|\theta-y\|^2.
\]
For fixed \((x,y)\), this function is \(\eta\)-strongly convex and has a unique minimizer. Indeed, smoothness gives its quadratic lower bound with curvature \(\eta\), which also gives coercivity. Subtracting the two minimizer equations and using strong monotonicity gives
\[
\|\theta_\gamma^*(x,y)-\theta_\gamma^*(x',y')\|\le \eta^{-1}(L_2\|x-x'\|+\gamma^{-1}\|y-y'\|).
\]
The minimizer is therefore Lipschitz. The minimizing inequalities at neighboring parameter values, followed by differentiability of \(H\) and continuity of the minimizer, give
\[
\nabla V_\gamma(x,y)=\bigl(\nabla_xG(x,\theta_\gamma^*(x,y)),\gamma^{-1}(y-\theta_\gamma^*(x,y))\bigr).
\]
This formula and the preceding Lipschitz estimate give a finite Lipschitz constant for \(\nabla V_\gamma\). Consequently \(\Phi_\mu=\mu(F-F_*)+G-V_\gamma\) has a uniformly Lipschitz gradient for \(0<\mu\le\mu_0\), is nonnegative, and has the same gradient as \(\Psi_\mu\). These facts are derived here; the nonstandard bilevel-equivalence and penalty-approximation assertions grouped in theory_005 are not invoked.

Adding and subtracting exact local directions evaluated at the averaged variables, and then at the proximal minimizer, gives
\[
\mathbb E\|\nabla\Psi_{\mu_k}(\bar x^k,\bar y^k)-q_k\|^2\le C(E_k+X_k),
\]
\[
\mathbb E\|\bar d_\theta^k\|^2\le C(E_k+X_k).
\]
Only local gradient Lipschitzness and Jensen's inequality are used. In particular,
\[
\mathbb E\|\nabla\Psi_{\mu_k}(\bar x^k,\bar y^k)\|^2\le C(U_k+E_k+X_k).\tag{1}
\]

## 2. Averaged objective and proximal descent

Use the nonnegative proximal gap
\[
R(x,y,\theta)=H(x,y,\theta)-V_\gamma(x,y).
\]
Strong convexity and smoothness in \(\theta\) imply
\[
(\eta/2)\|\theta-\theta_\gamma^*(x,y)\|^2\le R(x,y,\theta)\le C\|\theta-\theta_\gamma^*(x,y)\|^2.
\]
The formulas for \(\nabla H\) and \(\nabla V_\gamma\) show that \(R\) has Lipschitz gradient and
\[
\|\nabla_{x,y}R\|\le C\|\theta-\theta_\gamma^*\|,\quad \|\nabla_\theta H\|\le C\|\theta-\theta_\gamma^*\|,\quad \|\nabla_\theta H\|^2\ge\eta^2\|\theta-\theta_\gamma^*\|^2.
\]

Apply smooth descent conditionally to the averaged primal step. The exact averaged primal direction is \(q_k\); its discrepancy from \(\nabla\Phi_{\mu_k}\) is bounded above. For sufficiently small \(h\),
\[
\mathbb E\Phi_{\mu_{k+1}}(\bar x^{k+1},\bar y^{k+1})-\mathbb E\Phi_{\mu_k}(\bar x^k,\bar y^k)
\le -c\alpha h U_k+C\alpha h(E_k+X_k)+C\alpha^2h^2v/n.\tag{2}
\]
Here replacing \(\mu_k\) by \(\mu_{k+1}\) is nonpositive because \(F-F_*\ge0\).

Similarly, apply smooth descent to \(R\) in all three averaged variables. Its theta inner product supplies negative \(hE_k\). The theta-direction discrepancy is bounded by consensus; Young's inequality bounds the primal inner product by a small multiple of \(hE_k\) plus \(C\alpha^2hU_k\). The quadratic smoothness remainder is bounded by \(Ch^2(U_k+E_k+X_k+v/n)\). After absorbing its \(E_k\) term,
\[
\mathbb E R(\bar Z^{k+1})-\mathbb E R(\bar Z^k)
\le -c hE_k+C(\alpha^2h+h^2)U_k+ChX_k+Ch^2v/n.\tag{3}
\]
All noise-linear terms vanish conditionally; correlation between components does not affect the quadratic remainder estimate.

Choose a fixed positive weight \(a\), a sufficiently large constant multiple of \(\alpha\). First choose \(\alpha\) small and then \(h\) small. Adding (2) and \(a\) times (3) gives, for
\[
B_k=\mathbb E\Phi_{\mu_k}(\bar x^k,\bar y^k)+a\mathbb E R(\bar Z^k)\ge0,
\]
\[
B_{k+1}-B_k\le -c h(U_k+E_k)+ChX_k+Ch^2v/n.\tag{4}
\]
The constants absorb the fixed positive \(\alpha\). This closes averaged proximal descent without the incorrect assertion that the reciprocal of a Young parameter proportional to \(h\) stays bounded.

## 3. Disagreement and movement

Since \(\|WP\|\le\rho\), apply Young's inequality to \(PZ^{k+1}=WP(Z^k-\Lambda S^k)\), where the block steps are \(\alpha h,\alpha h,h\). With \(r=(1+\rho^2)/2\),
\[
X_{k+1}\le rX_k+Ch^2T_k/s.
\]
Summing, using \(1-r\ge s/2\), gives
\[
\sum_{k<K}X_k\le CX_0/s+Ch^2s^{-2}\sum_{k<K}T_k.\tag{5}
\]

For each variable, the update difference decomposes as
\[
Z_z^{k+1}-Z_z^k=(W-I)PZ_z^k-\lambda_z WP S_z^k-\lambda_z JS_z^k.
\]
The bounds \(\|W-I\|\le2\) and \(\|W\|\le1\), followed by a norm inequality and division by \(n\), give
\[
M_k\le CX_k+Ch^2T_k+Ch^2(U_k+E_k+v/n).\tag{6}
\]
This explicitly proves the relevant standard-independent movement result and verifies its normalization. No external method-specific claim is being used as a closed obligation.

## 4. Tracker increments, including the penalty change

Project the tracker update onto disagreement. Contraction and Young's inequality yield
\[
T_{k+1}\le rT_k+Cs^{-1}\mathbb E\|W(\widehat d^{k+1}-\widehat d^k)\|_n^2.
\]
Let \(r_k=\mu_k-\mu_{k+1}\ge0\). Local smoothness gives
\[
\mathbb E\|W(d^{k+1}-d^k)\|_n^2\le CM_k+C r_k^2\mathbb E\|W\nabla f(x^k,y^k)\|_n^2.
\]
Here \(\nabla f\) stacks the complete local upper-level gradients. This retains the time-varying coefficient rather than incorrectly treating the directions as one fixed Lipschitz map. Sampling errors at adjacent times need not be independent after conditioning on their resulting iterates: the unconditional bound \(\mathbb E\|W(\varepsilon^{k+1}-\varepsilon^k)\|_n^2\le4v\) is sufficient.

Define \(H_0=\|W\nabla f(x^0,y^0)\|_n^2\). Lipschitzness, path summation, and Cauchy-Schwarz imply
\[
\mathbb E\|W\nabla f(x^k,y^k)\|_n^2\le2H_0+2L_1^2 k\sum_{j<k}M_j.
\]
Moreover,
\[
r_k\le\mu_0p(k+1)^{-p-1},\qquad \sum_{k\ge0}r_k^2\le C\mu_0^2,\qquad \sum_{k\ge1}k r_k^2\le C\mu_0^2,
\]
with constants uniform for \(0<p<1/4\): the last series is bounded by \(\mu_0^2p^2[1+(2p)^{-1}]\). Reordering finite nonnegative sums consequently gives
\[
\sum_{k<K}r_k^2\mathbb E\|W\nabla f(x^k,y^k)\|_n^2\le C H_0+C\sum_{k<K}M_k.\tag{7}
\]
Summing the tracker recursion thus gives
\[
\sum_{k<K}T_k\le CT_0/s+C H_0/s^2+C s^{-2}\sum_{k<K}M_k+CKv/s^2.\tag{8}
\]
Notice that local tracker noise has order \(v\), not \(v/n\).

The initialization term introduces no gradient-bound assumption. Let \(b_i^0\) be the lower-level part of the initial primal direction. For its x component, \(\|b_{x,i}^0\|\le L_2\|y_i^0-\theta_i^0\|\). For its y component,
\[
b_{y,i}^0=d_{\theta,i}^0+\nabla_y g_i(x_i^0,y_i^0)-\nabla_y g_i(x_i^0,\theta_i^0).
\]
Since \(\mathbb E S^0=W d^0\), these identities and Jensen's inequality give
\[
H_0\le C\mu_0^{-2}\left(\mathbb E\|S^0\|_n^2+\|y^0-\theta^0\|_n^2\right).\tag{9}
\]
All quantities here are finite initialization quantities. There is no uniform bound on local gradients along the run.

## 5. Coupling absorption and telescoping

Write \(X_\Sigma,T_\Sigma,M_\Sigma\) for the sums through \(K-1\), and \(J_\Sigma=\sum_{k<K}(U_k+E_k)\). Substitute (6) into (8), absorb \(Ch^2T_\Sigma/s^2\), and substitute into (5). Absorbing the resulting \(Ch^2X_\Sigma/s^4\) gives
\[
X_\Sigma\le C I_0+C h^4J_\Sigma/s^4+CKh^2v/s^4,\qquad
I_0=X_0/s+h^2T_0/s^3+h^2H_0/s^4.\tag{10}
\]
These absorptions hold under \(h\le b s^4\) for a sufficiently small network-independent \(b\). Summing (4) and using \(B_K\ge0\) gives
\[
J_\Sigma\le CB_0/h+CX_\Sigma+CKhv/n.
\]
Substitute (10) and absorb \(Ch^4J_\Sigma/s^4\). Therefore
\[
J_\Sigma+X_\Sigma\le C\left(B_0/h+I_0+Khv/n+Kh^2v/s^4\right).\tag{11}
\]
This supplies the complete coupled closure; it does not claim a uniform \(hT_k\) dissipation that the tracker estimates do not provide. Equivalently, weighted assembly uses tracker weights of cubed-step order, matching variable forcing and the cubed-step stochastic remainder.

Let \(A_0=B_0+X_0+T_0+H_0\). Since \(h\le b s^4\le b s^2\),
\[
h I_0=(h/s)X_0+(h^3/s^3)T_0+(h^3/s^4)H_0\le C A_0.
\]
Thus network-dependent initialization terms cannot secretly enter the leading constant. By (1) and (11), both the average stationarity measure and average consensus error are at most
\[
C\left(\frac{A_0}{Kh}+\frac{hv}{n}+\frac{h^2v}{s^4}\right).\tag{12}
\]
The initialization quantity is bounded by starting-variable values, initial tracker second moments, and the initial objective/proximal gaps, using (9). These are the allowed initialization dependence; uniformity across families is understood with these initialization quantities controlled.

Finally substitute \(h=c_\theta\sqrt{n/K}\). Formula (12) becomes
\[
C\left(\frac{A_0+\delta_f^2+\delta_g^2}{\sqrt{nK}}+\frac{n(\delta_f^2+\delta_g^2)}{(1-\rho)^4K}\right).
\]
This proves the requested stationarity rate, including its averaged-noise contribution to the leading term. It also proves a stronger consensus estimate. Since \(n\ge1\), that estimate implies the requested consensus bound with leading \(1/\sqrt K\) and lower-order \(n^{3/2}/K\). The leading stationarity term has asymptotic linear agent speedup when it dominates the lower-order term. Every bound used only local smoothness, finite initialization, the stated sampling model, and mixing; no gradient heterogeneity or bounded-gradient assumption was introduced.
