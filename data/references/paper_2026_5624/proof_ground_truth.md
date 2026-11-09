# Reference Proof

## Proof Structure

We derive the strategic-risk identity and establish existence of the benchmark minima. Support nesting gives the universal lower bound. Completing the covariance quadratic identifies the support-restriction term, including the empty support. On a nonempty support, we derive the generalized-ridge oracle equation, verify finite-parameter attainment along the ordinary-ridge path, and compare the two rules using the stated heterogeneity quantity and curvature constant. Finally, we combine the support and ridge terms and obtain a finite ridge rule for the exact tolerance consequence.

## Complete Proof

### step_001 — Strategic risk and benchmark existence

Write \(\varepsilon=Y-\beta_0^TX\). The assumptions and the definition of \(\beta_0\) imply
\[
 \mathbb E[\varepsilon]=0,\qquad
 \mathbb E[X\varepsilon]=\mathbb E[XY]-\Sigma\beta_0=0,
 \qquad \mathbb E[\varepsilon^2]=\tau^2<\infty.
\]
No independence or conditional-mean assumption on \(\varepsilon\) is needed.

The individual's objective has gradient \(\beta-Ca\) and negative-definite Hessian \(-C\), so its unique best response is \(a=C^{-1}\beta\). The deployed residual is therefore
\[
 \beta^T(X+C^{-1}\beta)+b-Y
 = (\beta-\beta_0)^TX+b+\beta^TC^{-1}\beta-\varepsilon.
\]
Expanding its square, centering eliminates the cross terms involving the deterministic shift, and \(\mathbb E[X\varepsilon]=0\) eliminates the remaining cross term. Hence
\[
 \mathcal R(\beta,b)
 = (\beta-\beta_0)^T\Sigma(\beta-\beta_0)
   +(b+\beta^TC^{-1}\beta)^2+\tau^2. \tag{1}
\]
All terms are finite under the stated second-moment assumptions.

Both nonconstant terms in (1) are nonnegative. Choosing \(\beta=\beta_0\) and \(b=-\beta_0^TC^{-1}\beta_0\) shows that \(\mathcal O=\tau^2\), with the minimum attained. For zero intercept, (1) is continuous and bounded below by
\[
 \lambda_{\min}(\Sigma)\|\beta-\beta_0\|_2^2+\tau^2.
\]
It is consequently coercive. On each closed coordinate subspace, a minimizing sequence is bounded and has a convergent subsequence whose limit attains the infimum by continuity. Thus \(\mathcal V\) and every \(\mathcal V(J)\) are attained, including the singleton feasible set \(\Theta(\varnothing)=\{0\}\).

### step_002 — Universal lower bound

For every support and every finite \(\lambda\ge0\), the defined ridge coefficient lies in \(\Theta(J)\) and has fitted intercept zero. Therefore
\[
 \mathcal R(\widehat\beta(J,\lambda),0)
 \ge\mathcal V(J)\ge\mathcal V.
\]
Subtracting \(\mathcal O\) proves the lower bound for all supports, including \(J=\varnothing\).

### step_003 — Exact support-restriction term

First suppose \(J\ne\varnothing\). Set \(R=[d]\setminus J\), \(A=\Sigma_{JJ}\), and \(m=m_J\). Restricting the equality \(\mathbb E[XY]=\Sigma\beta_0\) to the retained coordinates gives
\[
 m=\beta_{0,J}+A^{-1}\Sigma_{JR}\beta_{0,R}.
\]
For a vector with retained coordinates \(\eta\) and omitted coordinates zero, write \(z=\eta-\beta_{0,J}\). Block expansion gives
\[
 (\beta-\beta_0)^T\Sigma(\beta-\beta_0)
 =z^TAz-2z^T\Sigma_{JR}\beta_{0,R}
   +\beta_{0,R}^T\Sigma_{RR}\beta_{0,R}.
\]
Completing the square around \(z=A^{-1}\Sigma_{JR}\beta_{0,R}\) yields
\[
 (\beta-\beta_0)^T\Sigma(\beta-\beta_0)
 =p(J)+(\eta-m)^TA(\eta-m). \tag{2}
\]
When \(J=[d]\), the same identity reads \((\beta-\beta_0)^T\Sigma(\beta-\beta_0)=(\eta-m)^TA(\eta-m)\), with \(p([d])=0\) and \(m=\beta_0\).

For any such supported vector,
\[
 \beta^TC^{-1}\beta=\eta^T(C^{-1})_{JJ}\eta.
\]
In particular, the relevant matrix is the principal block of the full inverse cost matrix, not the inverse of the retained cost block. Substituting into (1) and minimizing gives
\[
 \mathcal V(J)=\tau^2+p(J)+g(J). \tag{3}
\]
For the empty support, the only coefficient vector is zero. Applying (1) directly gives
\[
 \mathcal V(\varnothing)=\mathbb E[Y^2]
 =\tau^2+\beta_0^T\Sigma\beta_0
 =\tau^2+p(\varnothing)+g(\varnothing).
\]
Thus (3) holds for every support. For full support it gives \(\mathcal V=\tau^2+g([d])\), and subtraction yields
\[
 \mathcal V(J)-\mathcal V
 =p(J)-[g([d])-g(J)] \tag{4}
\]
for every \(J\subseteq[d]\).

### step_004 — Fixed-support ridge approximation and attainment

Fix a nonempty support. Retain \(A\) and \(m\) above and define
\[
 K=(C^{-1})_{JJ},\quad
 u=A^{1/2}\eta,\quad v=A^{1/2}m,\quad
 Q=A^{-1/2}KA^{-1/2},\quad D=A^{-1}.
\]
The matrices \(A,K,Q,D\) are symmetric positive definite. After subtracting \(\tau^2+p(J)\), the support risk is
\[
 f(u)=\|u-v\|_2^2+(u^TQu)^2. \tag{5}
\]
It is continuous and satisfies \(f(u)\ge\|u-v\|_2^2\), so it is coercive and attains a minimum. Differentiation gives
\[
 \nabla f(u)=2(u-v)+4(u^TQu)Qu,
\]
\[
 \nabla^2f(u)=2I+8Quu^TQ+4(u^TQu)Q\succeq2I.
\]
The minimizer \(u_*\) is therefore unique. Its first-order equation is
\[
 (I+\alpha Q)u_*=v,
 \qquad \alpha=2u_*^TQu_*\ge0. \tag{6}
\]
This derives, rather than assumes, the generalized-ridge representation.

Let \(u_\lambda=A^{1/2}\widehat\beta_J(J,\lambda)\). The population ridge formula gives
\[
 (I+\lambda D)u_\lambda=v. \tag{7}
\]
The eigenvalues of each inverse \((I+\alpha Q)^{-1}\) and \((I+\lambda D)^{-1}\) lie in \((0,1]\). Writing \(r=\|v\|_2\) and \(q=\|Q\|_{\rm op}\), it follows that
\[
 \|u_*\|_2\le r,\qquad \|u_\lambda\|_2\le r,
 \qquad \alpha\le2q r^2.
\]

#### Finite-parameter attainment of the ridge minimum

The function \(F(\lambda)=f(u_\lambda)\) is continuous on \([0,\infty)\). If \(v=0\), then \(u_\lambda=0\) for every \(\lambda\), and its minimum is attained at every parameter.

If \(v\ne0\), equation (7) implies
\[
 u_\lambda\longrightarrow0,
 \qquad \lambda u_\lambda\longrightarrow D^{-1}v=Av
 \quad\text{as }\lambda\longrightarrow\infty.
\]
Expanding (5) at zero gives
\[
 F(\lambda)-\|v\|_2^2
 =-2v^Tu_\lambda+\|u_\lambda\|_2^2+(u_\lambda^TQu_\lambda)^2.
\]
Since \(\lambda u_\lambda\) converges, multiplying this equality by \(\lambda\) yields
\[
 \lambda\bigl(F(\lambda)-\|v\|_2^2\bigr)
 \longrightarrow -2v^TAv<0.
\]
The quadratic and quartic terms tend to zero after this multiplication. Thus some finite \(\lambda_0\) satisfies \(F(\lambda_0)<\|v\|_2^2\), whereas \(F(\lambda)\to\|v\|_2^2\). For all sufficiently large \(M\), every \(\lambda>M\) has \(F(\lambda)>F(\lambda_0)\). A continuous function attains its minimum on the compact interval \([0,M]\), which is consequently its global minimum on \([0,\infty)\). This proves finite-\(\lambda\) attainment without adjoining an infinite ridge parameter.

#### Heterogeneity comparison

In the present notation,
\[
 h(J)=\inf_{\gamma\ge0}\|Q-\gamma D\|_{\rm op}.
\]
The function inside the infimum is continuous, and the reverse triangle inequality gives
\[
 \|Q-\gamma D\|_{\rm op}
 \ge\gamma\|D\|_{\rm op}-\|Q\|_{\rm op}
 \longrightarrow\infty.
\]
It therefore attains its infimum at a finite \(\gamma_*\ge0\).

Subtracting (6) from (7) in a common left-hand operator gives
\[
 (I+\lambda D)(u_\lambda-u_*)=(\alpha Q-\lambda D)u_*.
\]
For any \(\gamma\ge0\), take \(\lambda=\alpha\gamma\). The inverse on the left has operator norm at most one, so
\[
 \|u_{\alpha\gamma}-u_*\|_2
 \le\alpha\|Q-\gamma D\|_{\rm op}\|u_*\|_2.
\]
In particular, the finite choice \(\bar\lambda=\alpha\gamma_*\) satisfies
\[
 \|u_{\bar\lambda}-u_*\|_2
 \le\alpha h(J)\|u_*\|_2. \tag{8}
\]
Using the preceding bounds on \(\alpha\) and \(\|u_*\|_2\) gives
\[
 \|u_{\bar\lambda}-u_*\|_2^2
 \le4q^2r^6h(J)^2. \tag{9}
\]
No division by \(\alpha\), \(r\), or \(h(J)\) is used. If \(v=0\), the oracle and all ridge points are zero. If \(h(J)=0\), (8) gives exact equality of the oracle and the ridge point at the finite parameter \(\bar\lambda\).

#### Curvature and objective excess

For every \(u\), the displayed Hessian satisfies
\[
 \|\nabla^2f(u)\|_{\rm op}
 \le2+8\|Qu\|_2^2+4(u^TQu)\|Q\|_{\rm op}
 \le2+12q^2\|u\|_2^2.
\]
Both endpoints of the segment between \(u_*\) and any \(u_\lambda\) have norm at most \(r\); the whole segment has that property. On this segment the Hessian norm is at most
\[
 2+12q^2r^2=2A_C(J).
\]
Let \(w=u_\lambda-u_*\). Because \(\nabla f(u_*)=0\), integrating the second derivative along the segment gives
\[
 f(u_\lambda)-f(u_*)
 =\int_0^1(1-t)w^T\nabla^2f(u_*+tw)w\,dt
 \le A_C(J)\|w\|_2^2.
\]
Apply this at \(\bar\lambda\) and use (9). The result is
\[
 f(u_{\bar\lambda})-f(u_*)
 \le4A_C(J)q^2r^6h(J)^2=B_C(J)h(J)^2.
\]
Returning to the support risk, using oracle minimality and the already-proved attainment of the ridge minimum, yields
\[
 0\le\min_{\lambda\ge0}\mathcal R(\widehat\beta(J,\lambda),0)-\mathcal V(J)
 \le B_C(J)h(J)^2. \tag{10}
\]
For \(J=\varnothing\), every ridge coefficient is zero and its risk is exactly \(\mathcal V(\varnothing)\). Thus (10) also holds there, with both sides of the excess bound equal to zero and with an attained minimum.

### step_005 — Integrated upper bound and consequences

For every support, adding (4) and (10) gives
\[
 \min_{\lambda\ge0}\mathcal R(\widehat\beta(J,\lambda),0)-\mathcal V
 \le p(J)-[g([d])-g(J)]+B_C(J)h(J)^2.
\]
For the empty support this is an equality. For every nonempty support the preceding comparison also supplies a finite parameter witnessing the upper bound directly.

If the right-hand side is at most \(\epsilon\), a finite minimizing parameter, or the finite witness just constructed, gives a ridge rule supported on \(J\) with risk at most \(\mathcal V+\epsilon\). Since
\[
 \mathcal V+\epsilon
 =\mathcal O+(\mathcal V-\mathcal O)+\epsilon,
\]
the second consequence follows. The argument also covers \(\tau^2=0\), zero full or restricted signal, the full and empty supports, and zero heterogeneity. All theorem-critical proof obligations are closed; no specialized external result is assumed.
