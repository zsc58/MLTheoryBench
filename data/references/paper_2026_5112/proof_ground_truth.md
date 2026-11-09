# Reference Proof

## Proof Structure

We establish the fixed-bin calibration reduction, pointwise softmax-margin inequalities, the clean-to-robust comparison, and logit-Hessian spectral control. These yield both population bounds. Strictly positive sample margins then identify empirical ECE with mean true-class misconfidence and give the two-sided empirical bounds and curvature coupling. All expectations and zero-Jacobian cases are handled explicitly.

## Complete Proof

### 1. Calibration reduction

Fix a parameter. Finite logits imply that each softmax probability is positive and that the maximum probability lies in $(0,1]$. Thus the prescribed interval bins contain every population or sample confidence. The confidence and the tie-resolved predicted label are measurable. Write $Z=A-C$, so $|Z|\le1$ and all binwise expectations used here are integrable. For each positive-probability bin,
\[
\Pr(C\in B_r)\left|\mathbb E[Z\mid C\in B_r]\right|
=\left|\mathbb E[Z\mathbf1_{\{C\in B_r\}}]\right|
\le\mathbb E[|Z|\mathbf1_{\{C\in B_r\}}].
\]
Zero-probability bins contribute nothing. Summing over the bins gives
\[
\operatorname{ECE}_M(\theta;\pi)\le\mathbb E|A-C|.
\]
Likewise, with $Z_i=\mathbf1\{\hat y_i=y_i\}-\hat p_i$, the triangle inequality in each nonempty empirical bin gives
\[
\operatorname{ECE}_M(\theta;D)
\le\sum_{r:n_r>0}\frac1n\sum_{i:\hat p_i\in B_r}|Z_i|
=\frac1n\sum_{i=1}^n|Z_i|.
\]

For a point $(x,y)$, suppress the parameter and input notation. If $\hat y=y$, then
\[
|\mathbf1\{\hat y=y\}-\hat p|=1-p_y.
\]
If $\hat y\ne y$, then
\[
|\mathbf1\{\hat y=y\}-\hat p|=p_{\hat y}
\le\sum_{j\ne y}p_j=1-p_y.
\]
This remains valid at tied logits. Consequently,
\[
|\mathbf1\{\hat y=y\}-\hat p|\le1-p_y.\tag{1}
\]

### 2. Softmax-margin bounds

For $m=z_y-\max_{j\ne y}z_j$, let
\[
S=\sum_{j\ne y}e^{z_j-z_y}.
\]
The softmax definition yields $1-p_y=S/(1+S)$. Each summand is at most $e^{-m}$, and one summand equals $e^{-m}$ because $K\ge2$ and a maximizing competitor exists. Hence
\[
e^{-m}\le S\le(K-1)e^{-m}.
\]
It follows that
\[
1-p_y\le S\le(K-1)e^{-m},\tag{2}
\]
and
\[
1-p_y=\frac{S}{1+S}
\ge\frac{e^{-m}}{1+S}
\ge\frac{e^{-m}}{1+(K-1)e^{-m}}.\tag{3}
\]
For $m\ge0$, the last denominator is at most $K$, so
\[
\frac1K e^{-m}\le1-p_y\le(K-1)e^{-m}.\tag{4}
\]

### 3. Clean-to-robust comparison

The support-neighborhood condition makes every logit evaluation in the robust infimum meaningful. Since $\delta=0$ is feasible,
\[
m_{\epsilon,\theta}(x,y)\le m_\theta(x,y),\qquad
 e^{-m_\theta(x,y)}\le e^{-m_{\epsilon,\theta}(x,y)}.\tag{5}
\]
The comparison also holds when the infimum is $-\infty$. The robust random variable is measurable by the setup, and the clean exponential is measurable because the clean margin is a finite combination of measurable functions. Monotonicity of nonnegative integrals therefore gives
\[
\mathbb E e^{-m_\theta(X,Y)}\le Q(\theta;\pi)
\]
as an extended-real inequality. No finiteness of either exponential moment and no input-Lipschitz condition is needed.

### 4. Logit-Hessian spectral control

For a probability vector $p$, put $H=\operatorname{diag}(p)-pp^\top$. This matrix is real symmetric. If $u\in\mathbb R^K$ and $\bar u=\sum_jp_ju_j$, then
\[
u^\top Hu=\sum_jp_ju_j^2-\bar u^2
=\sum_jp_j(u_j-\bar u)^2\ge0.
\]
Thus $H$ is positive semidefinite. Its diagonal entries and absolute off-diagonal row sums satisfy
\[
H_{ii}=p_i(1-p_i),\qquad
R_i:=\sum_{j\ne i}|H_{ij}|=p_i(1-p_i).
\]
To verify the needed row bound directly, take a nonzero real eigenvector $w$ for an eigenvalue $\lambda$ and choose an index $i$ for which $|w_i|=\max_j|w_j|>0$. The eigenvector equation gives
\[
|\lambda-H_{ii}|\,|w_i|
=\left|\sum_{j\ne i}H_{ij}w_j\right|
\le R_i|w_i|.
\]
Therefore $\lambda\le H_{ii}+R_i=2p_i(1-p_i)$, and
\[
\lambda_{\max}(H)\le2\max_i p_i(1-p_i).
\]
Choose $k$ with $p_k=p_{\max}$. For $i=k$, $p_i(1-p_i)\le1-p_{\max}$. For $i\ne k$, $p_i\le1-p_{\max}$, so again $p_i(1-p_i)\le1-p_{\max}$. Hence
\[
0\le\lambda_{\max}(H_z(p))\le2(1-p_{\max})\le2(1-p_y).\tag{6}
\]
This supplies the spectral estimate with its hypotheses and derivation, rather than leaving it to an unstated application of a named theorem.

### 5. Population conclusions and matrix expectations

Combining the calibration reduction, (1), (2), and (5) yields
\[
\operatorname{ECE}_M(\theta;\pi)
\le\mathbb E(1-p_\theta(X)_Y)
\le(K-1)\mathbb E e^{-m_\theta(X,Y)}
\le(K-1)Q(\theta;\pi).
\]
All comparisons are valid for infinite nonnegative moments.

For curvature, let
\[
G(X)=J_\theta(X)^\top H_z(p_\theta(X))J_\theta(X).
\]
It is a measurable symmetric positive-semidefinite matrix. For a symmetric matrix, orthonormal diagonalization gives the variational formula $\lambda_{\max}(H)=\sup_{\|v\|_2=1}v^\top Hv$. In particular, for positive-semidefinite $H$ and any compatible $J$,
\[
v^\top J^\top HJv
\le\lambda_{\max}(H)\|Jv\|_2^2
\le\lambda_{\max}(H)\|J\|_{\mathrm{op}}^2
\quad(\|v\|_2=1).
\]
Taking the supremum proves
\[
\lambda_{\max}(J^\top HJ)\le\|J\|_{\mathrm{op}}^2\lambda_{\max}(H).\tag{7}
\]
Under the assumed Jacobian bound, (6)–(7) imply $\|G(X)\|_{\mathrm{op}}\le2C_J^2$ almost surely. Every entry of $G(X)$ is consequently absolutely integrable, so the population Gauss–Newton matrix exists and is symmetric positive semidefinite. Its random top eigenvalue is also measurable and integrable. For every deterministic unit vector $v$,
\[
v^\top\mathbb E[G(X)]v
=\mathbb E[v^\top G(X)v]
\le\mathbb E\lambda_{\max}(G(X)).
\]
Taking the supremum over $v$ gives
\[
\lambda_{\max}(\mathbb E G)\le\mathbb E\lambda_{\max}(G).\tag{8}
\]
For $C_J>0$, (6)–(8), followed by (2) and (5), now give
\[
\begin{aligned}
\lambda_{\max}(H_{\mathrm{GN}}(\theta;\pi))
&\le2C_J^2\mathbb E(1-p_\theta(X)_Y)\\
&\le2C_J^2(K-1)\mathbb E e^{-m_\theta(X,Y)}\\
&\le2C_J^2(K-1)Q(\theta;\pi).
\end{aligned}
\]
If an exponential moment is infinite, the relevant upper bound is simply an extended-real upper bound. If $C_J=0$, the norm assumption gives $J_\theta(X)=0$ almost surely, hence $H_{\mathrm{GN}}(\theta;\pi)=0$. The displayed population inequalities then hold under the stated nonnegative-product convention, including when a moment is infinite.

### 6. Interpolating empirical conclusions

Because $n\ge1$ and every logit is finite, all sample margins are finite and their minimum is defined. If $\gamma>0$, the true class is the unique logit maximizer at every sample. Thus $\hat y_i=y_i$, $\hat p_i=p_\theta(x_i)_{y_i}$, and every nonempty bin has accuracy one. Since $c_r\le1$,
\[
\begin{aligned}
\operatorname{ECE}_M(\theta;D)
&=\sum_{r:n_r>0}\frac{n_r}{n}(1-c_r)\\
&=\frac1n\sum_{i=1}^n(1-\hat p_i)
=\frac1n\sum_{i=1}^n(1-p_\theta(x_i)_{y_i}).
\end{aligned}\tag{9}
\]
This identity is independent of the prescribed bin edges. Applying (4) termwise yields
\[
\frac1KQ_D(\theta)\le\operatorname{ECE}_M(\theta;D)\le(K-1)Q_D(\theta).
\]
Since each margin is at least $\gamma$, each exponential is at most $e^{-\gamma}$, and consequently
\[
Q_D(\theta)\le e^{-\gamma}.
\]
These prove the full empirical sandwich.

Let $J_i=J_\theta(x_i)$ and $H_i=H_z(p_\theta(x_i))$. The finite-average version of the unit-vector argument in (8), together with (7), gives
\[
\lambda_{\max}\left(\frac1n\sum_iJ_i^\top H_iJ_i\right)
\le\frac1n\sum_i\lambda_{\max}(J_i^\top H_iJ_i)
\le\frac1n\sum_i\|J_i\|_{\mathrm{op}}^2\lambda_{\max}(H_i).
\]
Using the sample Jacobian bound, (6), and (2), we obtain
\[
\lambda_{\max}(H_{\mathrm{GN}}(\theta;D))
\le\frac{2C_J^2}{n}\sum_i(1-p_\theta(x_i)_{y_i})
\le2C_J^2(K-1)Q_D(\theta).
\]
The already established lower ECE bound gives $Q_D(\theta)\le K\operatorname{ECE}_M(\theta;D)$, hence
\[
\lambda_{\max}(H_{\mathrm{GN}}(\theta;D))
\le2C_J^2(K-1)Q_D(\theta)
\le2C_J^2K(K-1)\operatorname{ECE}_M(\theta;D).
\]
When $C_J>0$, division of the resulting curvature–ECE inequality by $2C_J^2K(K-1)>0$ gives the stated lower bound on ECE. When $C_J=0$, all sample Jacobians and the empirical Gauss–Newton matrix vanish; the undivided bounds hold, and no divided assertion is made.

## Obligation Closure

The fixed-bin reduction, pointwise calibration gap, both softmax-margin bounds, robust comparison, logit spectral estimate, Jacobian composition estimate, matrix integrability, expectation comparison, empirical ECE identity, minimum-margin bound, and curvature coupling have each been derived above. Infinite population moments, zero Jacobian bounds, zero-probability and empty bins, and ties in the population case are covered. No theorem-critical external or specialized dependency remains unresolved.
