# Reference Proof

## Proof Structure and Obligations

The obligations are: (1) oracle optimality and descent; (2) the exact momentum-error recursion and gradient-drift bound; (3) the weighted Schatten trace inequality, covariance-based block second moments, and mixed-norm aggregation; (4) the summed momentum-error estimate; and (5) telescoping and both parameter regimes. All are derived below. No specialized external result is assumed.

## Complete Proof

Write \(\|\cdot\|=\|\cdot\|_{w,p}\), \(\|\cdot\|_*=\|\cdot\|_{v,q}\), \(g_k=\nabla f(X_k)\), \(E_k=\bar G_k-g_k\), \(e_k=M_k-g_k\), and \(\sigma=\sigma_{v,q,B}\). Set \(r=1-\theta\). Empty sums are zero, and the zeroth power in geometric sums is one, including when \(r=0\).

Let \(\mathcal F_{-1}=\sigma(X_0)\) and \(\mathcal F_k=\sigma(X_0,\{\xi_{s,i}:0\le s\le k,1\le i\le B\})\). Measurability of the oracle selection implies that \(X_k\) is \(\mathcal F_{k-1}\)-measurable. Fresh independent samples and the estimator assumptions give
\[
\mathbb E[E_k\mid\mathcal F_{k-1}]=0,\qquad
\mathbb E[(E_k)_j(E_k)_j^T\mid\mathcal F_{k-1}]\preceq B^{-1}V_jV_j^T. \tag{1}
\]
Indeed, distinct within-batch centered summands have conditional cross moments zero; summing the remaining \(B\) covariance bounds and dividing by \(B^2\) gives (1). Blocks of a sample need not be independent.

### 1. Oracle identities and descent

The stated duality and symmetry of the unit ball imply, for every oracle selection \(Z=\Delta^b_{w,p}(M)\),
\[
\langle M,Z\rangle=-\|M\|_*,\qquad \|Z\|\le1.
\]
These statements hold also when \(M=0\); equality in the norm constraint is not required. Dual Holder follows either from this duality or by applying Schatten Holder blockwise and vector Holder to the weighted block norms.

Gradient Lipschitzness implies the upper model by integrating along a segment:
\[
\begin{aligned}
f(X+D)-f(X)-\langle\nabla f(X),D\rangle
&=\int_0^1\langle\nabla f(X+tD)-\nabla f(X),D\rangle\,dt\\
&\le\int_0^1t\|D\|^2\,dt=\tfrac12\|D\|^2.
\end{aligned}
\]
The integral is justified because the gradient is continuous. With \(D_k=X_{k+1}-X_k\), oracle feasibility gives \(\|D_k\|\le\eta\), and therefore
\[
\begin{aligned}
f(X_{k+1})
&\le f(X_k)+\langle M_k,D_k\rangle+\langle g_k-M_k,D_k\rangle+\tfrac12\eta^2\\
&\le f(X_k)-\eta\|M_k\|_*+\eta\|e_k\|_*+\tfrac12\eta^2\\
&\le f(X_k)-\eta\|g_k\|_*+2\eta\|e_k\|_*+\tfrac12\eta^2. \tag{2}
\end{aligned}
\]
The last line uses \(\|g_k\|_*\le\|M_k\|_*+\|e_k\|_*\).

### 2. Exact momentum expansion and drift

Since \(e_0=E_0\), the recursion for \(k\ge1\) is
\[
e_k=r e_{k-1}+\theta E_k+r(g_{k-1}-g_k).
\]
Induction gives
\[
e_k=r^kE_0+\theta\sum_{t=1}^k r^{k-t}E_t
       +\sum_{t=1}^k r^{k-t+1}(g_{t-1}-g_t). \tag{3}
\]
In particular, an expansion using differences \(g_t-g_k\) instead would also need the term \(r^k(g_0-g_k)\); it cannot be dropped.

Lipschitzness and oracle feasibility yield
\[
\|g_t-g_{t-1}\|_*\le\|X_t-X_{t-1}\|\le\eta.
\]
Thus the last sum in (3) has norm at most
\[
\eta\sum_{t=1}^k r^{k-t+1}\le\frac{\eta}{\theta}. \tag{4}
\]
This remains valid when \(\theta=1\), in which case the drift sum is zero.

### 3. Dimension-free mixed-norm second moments

First prove the weighted trace inequality. For a real matrix \(A\), a symmetric positive definite matrix \(\Lambda\), and \(1\le q<2\),
\[
\|A\|_{S_q}^2\le\|\Lambda\|_{S_{q/(2-q)}}\operatorname{Tr}(AA^T\Lambda^{-1}). \tag{5}
\]
Diagonalize \(\Lambda\) and rotate the rows of \(A\), which changes neither its singular values nor the relevant trace. It suffices to consider \(\Lambda=\operatorname{diag}(\lambda_i)\), with \(\lambda_i>0\). Put \(T=AA^T\) and \(a=q/2\). If \(T=U\operatorname{diag}(\mu_\ell)U^T\), then scalar concavity and \(\sum_\ell U_{i\ell}^2=1\) give
\[
T_{ii}^{a}=\Big(\sum_\ell U_{i\ell}^2\mu_\ell\Big)^a
\ge\sum_\ell U_{i\ell}^2\mu_\ell^a.
\]
Summing over \(i\) proves \(\operatorname{Tr}(T^a)\le\sum_iT_{ii}^a\). Holder with exponents \(1/(1-a)\) and \(1/a\) then gives
\[
\|A\|_{S_q}^{q}
\le\sum_i\lambda_i^a(T_{ii}/\lambda_i)^a
\le\Big(\sum_i\lambda_i^{a/(1-a)}\Big)^{1-a}
    \Big(\sum_iT_{ii}/\lambda_i\Big)^a.
\]
Raising to \(1/a=2/q\) proves (5). For \(q=2\), the corresponding inequality follows from
\(I\preceq\|\Lambda\|_{S_\infty}\Lambda^{-1}\) by taking its trace against \(AA^T\). This proves the endpoint as well.

Now let \(a_t\) be any finite deterministic scalar sequence and put \(S=\sum_t a_tE_t\), \(c=B^{-1}\sum_t a_t^2\), and \(C_j=V_jV_j^T\). For \(s<t\), conditional centering in (1) and measurability of \(E_s\) imply
\(\mathbb E[(E_t)_j(E_s)_j^T]=0\), and likewise for its transpose. Consequently
\[
\mathbb E[S_jS_j^T]\preceq cC_j. \tag{6}
\]
All these products are integrable because (1) bounds the Frobenius second moments.

If \(q_j<2\), use (5) with
\[
\Lambda_{j,\varepsilon}=(C_j+\varepsilon I)^{1-q_j/2},\qquad \varepsilon>0.
\]
Since \(C_j\preceq C_j+\varepsilon I\), (6) gives
\[
\begin{aligned}
\mathbb E\|S_j\|_{S_{q_j}}^2
&\le c\|\Lambda_{j,\varepsilon}\|_{S_{q_j/(2-q_j)}}
       \operatorname{Tr}(C_j\Lambda_{j,\varepsilon}^{-1})\\
&\le c\left[\operatorname{Tr}(C_j+\varepsilon I)^{q_j/2}\right]^{2/q_j}.
\end{aligned}
\]
Taking the finite-dimensional spectral limit \(\varepsilon\downarrow0\) yields
\[
\mathbb E\|S_j\|_{S_{q_j}}^2\le c\|V_j\|_{S_{q_j}}^2. \tag{7}
\]
For \(q_j=2\), take the trace of (6) directly to obtain (7). This separate endpoint argument avoids any zero-to-zero-power expression. Singular or zero \(V_j\) cause no difficulty.

For nonnegative random variables \(Z_j=L_j^{-1/2}\|S_j\|_{S_{q_j}}\), Minkowski in \(L_{2/\beta}\), whose exponent is at least one, gives
\[
\begin{aligned}
\mathbb E\|S\|_*^2
&=\mathbb E\left(\sum_j Z_j^\beta\right)^{2/\beta}\\
&\le\left[\sum_j(\mathbb E Z_j^2)^{\beta/2}\right]^{2/\beta}\\
&\le\sigma^2\sum_t a_t^2. \tag{8}
\end{aligned}
\]
The required moments are finite by (7); the case \(\beta=2\) is simply linearity of expectation. No cross-block independence enters this calculation.

### 4. Sum of momentum errors

Applying (8) to the single term \(E_0\) and using Cauchy-Schwarz gives \(\mathbb E\|E_0\|_*\le\sigma\). For \(k\ge1\), use coefficients \(a_t=r^{k-t}\), \(1\le t\le k\). Since
\[
\sum_{t=1}^k r^{2(k-t)}\le\frac{1}{1-r^2}
=\frac{1}{\theta(2-\theta)}\le\frac1\theta,
\]
(8) gives
\[
\mathbb E\left\|\theta\sum_{t=1}^k r^{k-t}E_t\right\|_*\le\sqrt\theta\,\sigma.
\]
Combining this with (3)-(4), for all \(k\ge0\),
\[
\mathbb E\|e_k\|_*\le r^k\sigma+\sqrt\theta\,\sigma+\frac\eta\theta.
\]
At \(k=0\) this is a valid upper bound even though the actual noise-sum and drift contributions are absent. Summing and using \(\sum_{k=0}^{K-1}r^k\le1/\theta\) yields
\[
\sum_{k=0}^{K-1}\mathbb E\|e_k\|_*
\le\frac\sigma\theta+K\sqrt\theta\,\sigma+\frac{K\eta}\theta. \tag{9}
\]

### 5. Telescoping and parameter regimes

For every fixed finite horizon, oracle feasibility gives \(\|X_k-X_0\|\le k\eta\). Therefore all iterates lie in a deterministic compact set, on which \(f\) and its continuous gradient are bounded. Together with (8)-(9), this justifies the expectations in the following telescoping calculation. From (2), the lower bound on \(f\), and (9),
\[
\begin{aligned}
\frac1K\sum_{k=0}^{K-1}\mathbb E\|g_k\|_*
&\le\frac{\Delta_f}{\eta K}+\frac\eta2
 +\frac{2\sigma}{\theta K}+2\sqrt\theta\,\sigma+\frac{2\eta}\theta\\
&\le\frac{\Delta_f}{\eta K}
 +\frac{2\sigma}{\theta K}+2\sqrt\theta\,\sigma+\frac{3\eta}\theta,
\end{aligned}
\]
where \(\eta/2+2\eta/\theta\le3\eta/\theta\) because \(0<\theta\le1\). Put \(h=\sqrt{\Delta_f/K}>0\). With \(\eta=h\sqrt\theta\), this becomes
\[
\frac1K\sum_{k=0}^{K-1}\mathbb E\|g_k\|_*
\le\frac{4h}{\sqrt\theta}+2\sqrt\theta\,\sigma
 +\frac{2\sigma}{\theta K}. \tag{10}
\]
If \(\theta=1\), its definition implies \(\sigma\le h\), including \(\sigma=0\). Since \(K\ge1\), (10) is at most \(4h+2h+2h/K\le8h\).

If \(\theta<1\), then \(\sigma>h>0\) and \(\theta=h/\sigma\). Substituting into (10) gives
\[
6\sqrt{\sigma h}+\frac{2\sigma^2}{hK}
=6\sqrt\sigma\left(\frac{\Delta_f}{K}\right)^{1/4}
 +\frac{2\sigma^2}{\sqrt{\Delta_f K}}.
\]
Adding the nonnegative unused term in each regime proves
\[
\frac1K\sum_{k=0}^{K-1}\mathbb E\|\nabla f(X_k)\|_{v,q}
\le6\sqrt{\sigma_{v,q,B}}\left(\frac{\Delta_f}{K}\right)^{1/4}
 +8\sqrt{\frac{\Delta_f}{K}}
 +\frac{2\sigma_{v,q,B}^2}{\sqrt{\Delta_f K}}.
\]
All constants are independent of the matrix dimensions. Every listed proof obligation is closed.
