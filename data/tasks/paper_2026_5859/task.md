# Problem

## Setup

Let n tend to infinity. For each n, let k=k_n and p=p_n be integers with \(1\leq k<n\) and \(p\geq k+1\). Let the population covariance and signal be deterministic, with
\[
\Sigma=\operatorname{diag}(\lambda_1,\ldots,\lambda_p),\qquad
\lambda_1\geq\cdots\geq\lambda_p>0.
\]
Set \(\lambda_-:=\min_{j\leq k}\lambda_j\), \(\lambda_+:=\max_{j\leq k}\lambda_j\),
\[
T_k:=\sum_{j>k}\lambda_j,\qquad S_k:=\sum_{j>k}\lambda_j^2,\qquad a:=T_k/n,
\]
\[
\mathfrak r_k:=T_k/\lambda_{k+1},\qquad
\mathfrak R_k:=T_k^2/S_k,\qquad
r_k:=n/\mathfrak r_k+\sqrt{n/\mathfrak R_k},
\]
\[
w_k:=ar_k=\lambda_{k+1}+\sqrt{S_k/n},\qquad
\chi_{n,k}:=\sqrt{(k+\log n)/n}.
\]
Assume
\[
\lambda_+/\lambda_-=O(1),\qquad a\asymp\lambda_-,\qquad
\frac{kw_k^2}{S_k}\longrightarrow0,\qquad
r_kL\longrightarrow0,\qquad L\chi_{n,k}\longrightarrow0,
\]
where L is defined below.

Observe \(X=Z\Sigma^{1/2}\), where \(Z\in\mathbb R^{n\times p}\) has independent standard Gaussian entries, and
\[
y=X\beta^*+\varepsilon,\qquad
\mathbb E[\varepsilon\mid X]=0,\qquad
\operatorname{Cov}(\varepsilon\mid X)=\sigma_\varepsilon^2I_n.
\]
Assume \(\beta_j^*=0\) for \(j>k\). Put \(\Theta_j:=\lambda_j(\beta_j^*)^2\) and \(\Theta_H:=\sum_{j\leq k}\Theta_j\), and assume that \(\Theta_H\), \(\sigma_\varepsilon^2\), and their reciprocals are bounded uniformly in n.

Let \(\widehat\Sigma=X^TX/n\) have nonzero orthonormal eigenpairs \((\widehat\mu_i,\widehat v_i)\). For a spectral filter f define
\[
\widehat\beta_f:=\sum_i\frac{f(\widehat\mu_i)}{\widehat\mu_i}\widehat v_i\widehat v_i^T\frac{X^Ty}{n},
\]
with coefficients in the empirical null space equal to zero. Its conditional population excess risk is
\[
R(f\mid X):=\mathbb E\!\left[\left\|\Sigma^{1/2}(\widehat\beta_f-\beta^*)\right\|^2\,\middle|\,X\right].
\]
Filters are held fixed conditional on X in this expectation. Every infimum below is taken pointwise in X after this expectation, not over choices depending on the realized training noise.

For \(t\geq0\), define
\[
f_{a,t}(\mu):=\mu\int_0^t e^{-(\mu-a)s}\,ds,\qquad
R_{sign}(a,t):=R(f_{a,t}\mid X).
\]
Let
\[
R_{scale}^*:=\inf_{c\in\mathbb R}R(f\equiv c\mid X),
\]
where the constant filter is applied only to the nonzero empirical spectrum. Define
\[
f_\alpha^{ridge}(\mu):=\frac{\mu}{\mu+\alpha}\quad(\alpha\geq0),\qquad
f_t^{flow}(\mu):=1-e^{-t\mu}\quad(t\geq0),
\]
\[
R_+^*:=\min\left\{\inf_{\alpha\geq0}R(f_\alpha^{ridge}\mid X),\ 
\inf_{t\geq0}R(f_t^{flow}\mid X)\right\}.
\]
Let \(\widehat\mu_{min}^+\) be the smallest nonzero eigenvalue of \(\widehat\Sigma\), and set
\[
A_\nu(\mu):=\frac{\mu}{\mu-\nu},\qquad
R_{neg}^*:=\inf_{0\leq\nu<\widehat\mu_{min}^+}R(A_\nu\mid X).
\]

Put
\[
V_{T,k}:=\frac{\sigma_\varepsilon^2S_k}{n\lambda_-^2},\qquad
L:=\frac12\log(1+\Theta_H/V_{T,k}),\qquad
t_{fc}:=L/\lambda_-,
\]
\[
q_j:=\frac{\lambda_j}{\lambda_j+a},\qquad
\Delta_{shape}:=\inf_{c\in\mathbb R}\sum_{j=1}^k\Theta_j(1-cq_j)^2.
\]
The notation \(u_n\lesssim v_n\) means \(u_n\leq Cv_n\) with a constant independent of n; \(\gtrsim\) is the reverse comparison and \(\asymp\) means both. Unless specified to be numerical, constants may depend on the fixed bounds in the assumptions. All limits and deterministic little-o terms are as \(n\to\infty\).

## Task

Prove that, on events determined by X whose probabilities tend to one, the following inequalities hold simultaneously:
\[
R_{sign}(a,t_{fc})\lesssim\frac{\sigma_\varepsilon^2k}{n}+V_{T,k}(1+L^2)+\frac{\Theta_Hw_k^2}{\lambda_-^2},
\]
\[
R_{scale}^*\geq\Delta_{shape}-o(1)\Theta_H,\qquad
R_+^*\gtrsim\sum_{j=1}^k\Theta_j\left(\frac{a}{a+\lambda_j}\right)^2,
\]
and, for a numerical constant \(C_0>0\),
\[
R_{neg}^*\gtrsim\frac{\sigma_\varepsilon^2k}{n}+
\inf_{b\geq0}\left\{\frac{\Theta_Hb^2}{(b+\lambda_+)^2}
+\frac{\sigma_\varepsilon^2S_k}{n(b+C_0w_k)^2}\right\}.
\]
If
\[
b_k^*:=\left(\frac{\sigma_\varepsilon^2S_k\lambda_+^2}{n\Theta_H}\right)^{1/4}
\]
satisfies \(w_k=o(b_k^*)\), prove also that
\[
R_{neg}^*\gtrsim\frac{\sigma_\varepsilon^2k}{n}
+\frac{\sigma_\varepsilon\sqrt{\Theta_HS_k/n}}{\lambda_+}.
\]
In particular, if \(\Delta_{shape}\gtrsim\Theta_H\), show that \(R_{scale}^*\geq\Delta_{shape}/2\) with probability tending to one. Deduce polynomial improvement over any of the stated comparators whenever its lower bound is polynomially larger than the signed-flow upper bound: if their deterministic bounding expressions differ by at least a factor \(n^\delta\) for some fixed \(\delta>0\), the corresponding risk ratio is \(O(n^{-\delta})\) on the same high-probability events.
