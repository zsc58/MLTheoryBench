# Reference Proof

## Proof Structure

Use a simultaneous self-normalized-noise event to obtain the regularized confidence ellipsoid. The policy's maximizing rule bounds instantaneous regret by a confidence width. Clipping by the mean-reward range, Cauchy--Schwarz, and the elliptical-potential inequality reduce cumulative regret to a determinant ratio. Bound that ratio by a continuous coordinate-mass relaxation, and then split its head and tail using the effective dimension.

## Complete Proof

Write \(x_t=x_{\pi_t}\), \(\mu(v)=x_v^\top\alpha^*\), and \(L=\log(1+T/\lambda)>0\). Since \(k=1\) satisfies the defining inequality, \(d\) exists and \(1\le d\le N\). Every \(V_t\) is positive definite.

### 1. Determinant reduction and effective dimension

For any \(0\le m\le T\), put
\[
S_m=\sum_{s=1}^m x_sx_s^\top,
\qquad b_i=(S_m)_{ii}=\sum_{s=1}^m x_{s,i}^2.
\]
Then \(b_i\ge0\) and
\[
\sum_i b_i=\sum_{s=1}^m\|x_s\|_2^2\le m\le T.
\]
We first justify the elementary inequality \(\det B\le\prod_i B_{ii}\) for a positive-definite matrix \(B\). It is equality in dimension one. In higher dimension write
\[
B=\begin{pmatrix}A&u\\u^\top&a\end{pmatrix}.
\]
Its principal block \(A\) is positive definite, and block elimination gives
\[
\det B=\det A\,(a-u^\top A^{-1}u)\le a\det A.
\]
Induction proves the inequality. Applying it to \(\Lambda+S_m\) gives
\[
\log\frac{\det(\Lambda+S_m)}{\det\Lambda}
\le\sum_{i=1}^N\log(1+b_i/\lambda_i)
\le\max_{a_i\ge0,\,\sum_i a_i\le T}
\sum_{i=1}^N\log(1+a_i/\lambda_i).
\]
The maximum exists because the feasible set is compact. For any feasible allocation, the first \(d\) terms contribute at most \(dL\), since \(a_i\le T\) and \(\lambda_i\ge\lambda\). If \(d<N\), maximality of \(d\) gives
\[
d\lambda_{d+1}>T/L.
\]
Consequently,
\[
\sum_{i>d}\log(1+a_i/\lambda_i)
\le\sum_{i>d}a_i/\lambda_i
\le T/\lambda_{d+1}<dL.
\]
If \(d=N\), there is no tail and no use of \(\lambda_{N+1}\). Thus, in all cases and for every \(1\le t\le T+1\),
\[
\log\frac{\det V_t}{\det\Lambda}\le2dL.
\]
This argument includes zero observations, zero coordinate masses, and repeated regularizer eigenvalues.

### 2. Simultaneous confidence event

We use the following standard self-normalized martingale inequality. For predictable vectors \(x_s\), adapted noises satisfying
\(\mathbb E[e^{\eta\epsilon_s}\mid\mathcal F_{s-1}]\le e^{\eta^2R^2/2}\), a fixed positive-definite regularizer \(\Lambda\), and \(\delta\in(0,1)\), define
\[
\xi_t=\sum_{s<t}x_s\epsilon_s,
\qquad V_t=\Lambda+\sum_{s<t}x_sx_s^\top.
\]
On one event of probability at least \(1-\delta\), simultaneously for all relevant times,
\[
\|\xi_t\|_{V_t^{-1}}^2
\le2R^2\log\frac{\det(V_t)^{1/2}}{\delta\det(\Lambda)^{1/2}}.
\]
This is the standard independent result indexed by theory_005. Its hypotheses hold: the features and regularizer are fixed, selected features are predictable, and the noises have the specified conditional moment-generating-function bound. No union bound over arms or rounds is needed. For \(R=0\), applying the moment-generating-function condition with \(\eta=1\) and \(\eta=-1\) gives \(\mathbb E[\cosh\epsilon_s]\le1\); hence \(\epsilon_s=0\) almost surely. The displayed event then holds with probability one.

The normal equations give
\[
\widehat\alpha_t-\alpha^*
=-V_t^{-1}\Lambda\alpha^*+V_t^{-1}\xi_t.
\]
Since \(V_t\succeq\Lambda\), we have \(V_t^{-1}\preceq\Lambda^{-1}\): this follows by conjugating with \(\Lambda^{-1/2}\), inverting a positive-definite matrix whose eigenvalues are at least one, and conjugating back. Therefore
\[
\|\Lambda\alpha^*\|_{V_t^{-1}}^2
=(\alpha^*)^\top\Lambda V_t^{-1}\Lambda\alpha^*
\le(\alpha^*)^\top\Lambda\alpha^*\le C^2.
\]
Cauchy--Schwarz now implies, simultaneously for every vector \(x\) and every decision time,
\[
|x^\top(\widehat\alpha_t-\alpha^*)|
\le\|x\|_{V_t^{-1}}
\left[R\sqrt{\log\frac{\det V_t}{\det\Lambda}+2\log(1/\delta)}+C\right].
\]
By the determinant estimate, the bracket is at most
\[
R\sqrt{2dL+2\log(1/\delta)}+C
\le2R\sqrt{dL+2\log(1/\delta)}+C=c.
\]
The final comparison uses \(R\ge0\).

### 3. Optimism and width aggregation

Work on this confidence event. Choose \(v^*\in\arg\max_v\mu(v)\) and write \(w_t=\|x_t\|_{V_t^{-1}}\). Confidence and the maximizing rule imply
\[
\mu(v^*)
\le x_{v^*}^\top\widehat\alpha_t+c\|x_{v^*}\|_{V_t^{-1}}
\le x_t^\top\widehat\alpha_t+cw_t
\le\mu(\pi_t)+2cw_t.
\]
All means lie in \([-1,1]\), so the instantaneous regret is also at most two. Since \(c\ge0\),
\[
\mu(v^*)-\mu(\pi_t)
\le\min(2,2cw_t)
\le(2c+2)\min(1,w_t).
\]
Cauchy--Schwarz yields
\[
R_T\le(2c+2)\sqrt{T\sum_{t=1}^T\min(1,w_t^2)}.
\]
For completeness, the determinant identity for a rank-one update gives
\[
\det V_{t+1}=\det V_t\,(1+w_t^2).
\]
For \(u\ge0\), \(\min(1,u)\le2\log(1+u)\): on \([0,1]\), integrate \((1+u)^{-1}\ge1/2\), and for \(u\ge1\) use \(2\log2\ge1\). Summing the determinant identities therefore proves the elliptical-potential estimate
\[
\sum_{t=1}^T\min(1,w_t^2)
\le2\log\frac{\det V_{T+1}}{\det\Lambda}
\le4dL.
\]
Consequently,
\[
R_T\le(2c+2)\sqrt{4dTL}
=\bigl[4R\sqrt{dL+2\log(1/\delta)}+2C+2\bigr]\sqrt{4dTL}.
\]
The confidence event has probability at least \(1-\delta\), proving the stated result.

## Source-Repair Note

The single-update identity \(\det(A+xx^\top)=\det A(1+x^\top A^{-1}x)\) does imply that a single update is maximized in a smallest-eigenvalue direction. It does not imply that a jointly optimal collection of updates consists of coordinate vectors. The source's stronger assertion is false: for \(\Lambda=\operatorname{diag}(1,2)\), the two unit vectors \((\sqrt3/2,1/2)\) and \((\sqrt3/2,-1/2)\) give determinant \(25/4\), whereas axis-aligned pairs give at most \(6\). The proof above uses the valid continuous diagonal relaxation instead. This repairs the proof of the required determinant bound without changing the regret theorem or assuming that the relaxed allocation is realizable by axis-aligned observations.
