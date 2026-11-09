# Reference Proof

## Audit scope and conventions

This proof establishes exactly the two iterate conclusions in the task. It does not assume consistency of the Fisher approximation, global positive definiteness of the Fisher operator, a Lipschitz Hessian, or a Fisher-consistency rate. The normalization throughout is \(\bar H_s=H_s/s\) for \(s\geq1\).

Write \(P_{s+1}=\bar H_{s+1}^{-1}\), \(h_s=\operatorname{grad}L(\theta^s)\), and \(v_{s+1}=-\tau_{s+1}P_{s+1}\widehat g_s\). The pre-score history is \(\mathcal G_s\), and \(\mathcal F_s\) additionally contains the score sample at step \(s+1\). Thus \(P_{s+1}\) is \(\mathcal F_s\)-measurable, the fresh gradient minibatch is conditionally unbiased given \(\mathcal F_s\), and the centered score outer product has conditional mean zero given \(\mathcal G_s\). These are different conditioning operations.

All eventual pathwise bounds below can be localized using deterministic bounds and starting indices, stopping at the first violation of an adapted bound, and then taking a countable union. In particular, no random constant in an almost-sure big-O bound is silently replaced by an integrable deterministic constant.

## 1. Geometric estimates used in the proof

Smoothness and the inverse function theorem imply, uniformly for bases in the compact iterate set and sufficiently small tangent vectors,
\[
d(x,R_x(v))\asymp\|v\|_x.
\]
The reverse displacement \(R_{R_x(v)}^{-1}(x)\) is likewise \(O(\|v\|_x)\), by smoothness of the chosen inverse branches near the diagonal.

Let \(\Gamma^R_{x,v}\) be parallel transport along \(t\mapsto R_x(tv)\). In local trivializations set
\[
A_x(v)=(\Gamma^R_{x,v})^{-1}DR_x(v).
\]
It is smooth, \(A_x(0)=I\), and \(DA_x(0)=0\). For the last assertion, the covariant second derivative of the map from the tangent vector space to the manifold is symmetric; the second-order retraction condition makes its value on \((u,u)\) zero, and polarization makes it zero on every pair. Differentiating after parallel trivialization gives the asserted first derivative.

The integral Taylor formula now gives
\[
A_x(v)-I=\int_0^1(1-t)D^2A_x(tv)[v,v]dt=O(\|v\|^2),
\]
uniformly on the compact local disk bundle. Consequently the singular values of \(DR_x(v)\) and its inverse are \(1+O(\|v\|^2)\). Applying the same argument to the exponential map, and to the transition between exponential and retraction coordinates, gives locally
\[
T_{x,y}^{-1}\Gamma_{x,y}=I+O(d(x,y)^2).
\]
Here the comparison is made in a sufficiently small normal neighborhood. Such a neighborhood suffices once the iterates converge. No global normal-neighborhood or triangle-holonomy hypothesis is used.

## 2. Descent, objective convergence, and squared steps

Let \(m_K=\min_K L\). Compactness and continuity imply that
\[
V_s=L(\theta^s)-m_K\geq0
\]
is bounded. Also \(W_s=L(\theta^s)-L(\theta^\star)\) is bounded in absolute value by a deterministic constant. The oracle assumptions and Jensen's inequality therefore give constants \(D_2,D_4<\infty\) such that
\[
\mathbb E[\|\widehat g_s\|^2\mid\mathcal F_s]\leq D_2,
\qquad
\mathbb E[\|\phi_{s+1}\|^4\mid\mathcal G_s]\leq D_4.
\]
Retraction smoothness, followed by conditioning on \(\mathcal F_s\), gives
\[
\mathbb E[V_{s+1}\mid\mathcal F_s]
\leq V_s-\tau_{s+1}\langle h_s,P_{s+1}h_s\rangle
 +\frac{L_0D_2}{2}\tau_{s+1}^2\|P_{s+1}\|^2.
\]
The positive definiteness of every \(H_s\) follows inductively from the transported positive-definite initialization and the positive-semidefinite score addition.

The step-size and spectral assumptions imply
\[
\sum_s\tau_{s+1}^2\|P_{s+1}\|^2<\infty\quad\text{a.s.},
\]
because \(2\alpha-2\beta>1\).

We use the following almost-supermartingale theorem: if nonnegative adapted sequences satisfy
\(\mathbb E[X_{s+1}\mid\mathcal A_s]\leq(1+a_s)X_s+b_s-c_s\), then on the event \(\sum a_s+\sum b_s<\infty\), \(X_s\) has a finite almost-sure limit and \(\sum c_s<\infty\). This is the standard independent result recorded as theory_011. Here \(X_s=V_s\), \(a_s=0\), the displayed noise coefficient is \(b_s\), and \(c_s=\tau_{s+1}\langle h_s,P_{s+1}h_s\rangle\). All are nonnegative and adapted, and the preceding calculation verifies summability. Therefore
\[
W_s\text{ converges finitely},\qquad
\sum_s\tau_{s+1}\lambda_{\min}(P_{s+1})\|h_s\|^2<\infty
\quad\text{a.s.}
\]
This argument does not require \(W_s\geq0\).

Furthermore,
\[
\mathbb E[\|v_{s+1}\|^2\mid\mathcal F_s]
\leq D_2\tau_{s+1}^2\|P_{s+1}\|^2.
\]
Apply the same theorem to \(X_s=\|v_s\|^2\), with \(c_s=X_s\) and the right-hand side above as \(b_s\). Localization handles any initially unbounded moments of the preconditioner. It follows that
\[
\sum_s\|v_{s+1}\|^2<\infty\quad\text{a.s.}
\]

## 3. Spectral control

Put \(S_s=T_{s,s-1}^{-1}\), so the correctly normalized recursion is
\[
\bar H_{s+1}=\frac{s}{s+1}S_s\bar H_sS_s^*
 +\frac1{s+1}\phi_{s+1}\otimes\phi_{s+1},\qquad s\geq1.
\]
For \(0\leq k\leq s\), let \(A_{s,k}\) be the composite inverse backward transport from \(T_{\theta^k}M\) to \(T_{\theta^s}M\), with \(A_{s,s}=I\). Iterating the unnormalized update gives
\[
\bar H_{s+1}=\frac1{s+1}A_{s,0}H_0A_{s,0}^*
 +\frac1{s+1}\sum_{k=0}^s A_{s,k}(\phi_{k+1}\otimes\phi_{k+1})A_{s,k}^*.
\]
Define
\[
R_{s+1}=\frac1{s+1}\sum_{k=0}^s A_{s,k}I_F(\theta^k)A_{s,k}^*,
\qquad M_{s+1}=\bar H_{s+1}-R_{s+1}.
\]
These transported summands are not asserted to be a martingale array. Instead use the one-step recursion
\[
M_{s+1}=\frac{s}{s+1}S_sM_sS_s^*
 +\frac1{s+1}Z_{s+1},
\qquad Z_{s+1}=\phi_{s+1}\otimes\phi_{s+1}-I_F(\theta^s).
\]
Both \(S_s\) and \(M_s\) are \(\mathcal G_s\)-measurable; \(\mathbb E[Z_{s+1}\mid\mathcal G_s]=0\), and \(\mathbb E[\|Z_{s+1}\|_{\rm HS}^2\mid\mathcal G_s]\leq4D_4\).

The geometric estimates and squared-step summability imply
\[
\|S_s\|^4\leq1+a_s,\qquad a_s\geq0,\qquad \sum_s a_s<\infty\quad\text{a.s.}
\]
The finitely many initial terms can be included in \(a_s\). Thus, writing \(X_s=\|M_s\|_{\rm HS}^2\),
\[
\mathbb E[X_{s+1}\mid\mathcal G_s]
\leq(1+a_s)X_s-
\left(1-\frac{s^2}{(s+1)^2}\right)X_s+rac{4D_4}{(s+1)^2}.
\]
Robbins-Siegmund shows that \(X_s\) converges and that its product with the displayed harmonic-order coefficient is summable. Since that coefficient has divergent sum, the limit must be zero. Hence \(M_s\to0\) almost surely.

Products of the transport singular-value bounds show that, almost surely,
\[
\sup_{s\geq k\geq0}\|A_{s,k}\|<\infty,
\]
and the largest and smallest singular values of \(A_{s,k}\) tend uniformly to one as \(k\to\infty\), uniformly in \(s\geq k\). Indeed the logarithms of the upper and lower product bounds are controlled by \(C\sum_{j>k}\|v_j\|^2\); finitely many earlier invertible transports cause no problem.

The score fourth-moment bound gives
\[
\|I_F(\theta^k)\|_{\rm HS}^2\leq D_4.
\]
Consequently \(R_s\) is bounded above in operator norm, and so is \(\bar H_s=R_s+M_s\). Therefore
\[
\liminf_s\lambda_{\min}(P_s)>0\quad\text{a.s.}
\]
This is the only spectral conclusion needed globally.

For the local theorem also assume \(\theta^s\to\theta^\star\) and \(I_F(\theta^\star)\succ0\). There is a positive lower bound for \(I_F(\theta^s)\) eventually. To verify this without adding Fisher continuity, use a smooth orthonormal frame near \(\theta^\star\). If such a bound failed, choose a subsequence of unit vectors attaining the smallest eigenvalues and a further subsequence converging in this frame to a unit vector \(u\). Smoothness of the likelihood and metric gives pointwise convergence of
\(q_{\theta^s}(y)\langle\phi(y;\theta^s),u_s\rangle^2\).
Fatou's lemma then gives a limiting lower bound at least
\(\langle u,I_F(\theta^\star)u\rangle>0\), a contradiction. The common-measure likelihood and measurability hypotheses in the task justify this application.

Apply this lower bound to the sufficiently late terms of \(R_{s+1}\), together with the uniform lower singular-value bound for tail transports. Those terms occupy a fraction tending to one of the average; all other terms are nonnegative. Thus \(R_s\) has a strictly positive eventual lower eigenvalue. Since \(M_s\to0\), the same is true of \(\bar H_s\). We have proved, locally,
\[
0<mI\preceq P_s\preceq MI<\infty
\]
eventually almost surely, with pathwise constants. This does not assert that \(P_s\) converges.

## 4. Global stationarity and the convex case

The global spectral bound and Section 2 give
\[
\sum_s\tau_{s+1}\|h_s\|^2<\infty\quad\text{a.s.}
\]
Let \(b_s=\min_{0\leq k\leq s}\|h_k\|^2\). Then
\[
b_s\sum_{k=\lfloor s/2\rfloor}^s\tau_{k+1}
\leq\sum_{k=\lfloor s/2\rfloor}^s\tau_{k+1}\|h_k\|^2\longrightarrow0.
\]
The sum on the left is comparable to \(s^{1-\alpha}\). This proves the required little-o statement.

In the geodesically strictly convex case the stationary point is the unique minimizer. The convexity inequality along a connecting minimizing geodesic gives
\[
0\leq W_s\leq\|h_s\|d(\theta^s,\theta^\star).
\]
The distance is uniformly bounded on the compact iterate set. Hence \(\sum_s\tau_{s+1}W_s^2<\infty\). Since \(W_s\) converges and \(\sum_s\tau_s=\infty\), its limit is zero. Every accumulation point in \(K\) is therefore a minimizer by continuity of \(L\); uniqueness and compactness imply \(\theta^s\to\theta^\star\). The stated bounded-level-set hypothesis is compatible with this argument, although compact containment already supplies the boundedness used here.

## 5. A proved adaptive linear-noise estimate

We need the following finite-dimensional fact. Suppose \(\tau_n\asymp n^{-\alpha}\), \(0<\alpha<1\), and \(C_{n+1}\) is measurable before a martingale difference \(\epsilon_{n+1}\) is drawn. Suppose
\[
cI\preceq C_{n+1}\preceq CI,
\qquad
\mathbb E[\|\epsilon_{n+1}\|^p\mid\mathcal F_n]\leq D,
\qquad p>2/\alpha.
\]
Then the recursion
\[
Z_{n+1}=(I-\tau_{n+1}C_{n+1})Z_n+\tau_{n+1}\epsilon_{n+1}
\]
satisfies \(Z_n=O(\sqrt{\log n/n^\alpha})\) almost surely. The conclusion also holds for eventual pathwise bounds, by localization.

Here is a derivation, including the issue of adaptive products. Set
\(t_n=n^{\alpha/2}/\sqrt{\log n}\) for \(n\geq3\), and center the truncated noise:
\[
\epsilon'_{n+1}=\epsilon_{n+1}{\bf1}_{\{\|\epsilon_{n+1}\|\leq t_n\}}
-\mathbb E[\epsilon_{n+1}{\bf1}_{\{\|\epsilon_{n+1}\|\leq t_n\}}\mid\mathcal F_n].
\]
Markov's inequality gives a summable series of probabilities for \(\|\epsilon_{n+1}\|>t_n\), since \(\alpha p/2>1\). Hence these events occur only finitely often. The centering correction has norm at most \(Dt_n^{1-p}\).

Partition the large indices into deterministic consecutive blocks starting at \(a_j\), of lengths \(\lceil a_j^\alpha\rceil\). On one such block beginning at \(a\), the increments \(\tau_{n+1}\epsilon'_{n+1}\) are bounded by
\(C a^{-\alpha/2}/\sqrt{\log a}\), and the sum of their conditional second moments is at most \(Ca^{-\alpha}\).

For completeness, a scalar martingale with increments bounded in absolute value by \(b\) and total conditional variance at most \(V\) satisfies
\[
\Pr\!\left(\max_k|S_k|\geq x\right)
\leq2\exp\!\left(-\frac{x^2}{2(V+bx/3)}\right).
\]
Indeed, expanding the conditional exponential and using the zero conditional mean and \(|D|^r\leq b^{r-2}D^2\) gives
\(\mathbb E[e^{\lambda D}\mid\mathcal F]\leq\exp(\lambda^2\mathbb E[D^2\mid\mathcal F]/(2(1-\lambda b/3)))\) for \(0<\lambda b<3\). Multiplication gives an exponential supermartingale; stopping at the first crossing and optimizing \(\lambda\) proves the one-sided bound. Apply it to both signs. Applying this coordinatewise proves the finite-dimensional version with changed constants.

Take \(x=A\sqrt{\log a/a^\alpha}\). For sufficiently large fixed \(A\), the resulting probabilities are summable over the blocks. Thus the maximal partial sum of the centered weighted noise on every sufficiently late block is
\(O(\sqrt{\log a/a^\alpha})\) almost surely. The total weighted centering correction on that block is
\(O(t_a^{1-p})=o(\sqrt{\log a/a^\alpha})\). The finitely many truncation exceptions affect only finitely many blocks. Therefore the same maximal partial-sum bound holds for the original weighted noise.

Write \(J_i=I-\tau_iC_i\). Eventually \(\|J_i\|\leq1-c\tau_i\) and \(\|I-J_i\|\leq C\tau_i\). For a terminal index \(l\) in a block beginning at \(a\), variation of constants gives a sum of the weighted noise with coefficients \(\Phi_{l,i+1}=J_l\cdots J_{i+2}\). These coefficients can depend on that noise, so they are not used as martingale coefficients. Instead, pathwise summation by parts bounds the sum by
\[
\left(1+C\sum_{i=a}^{l-1}\tau_{i+1}\right)
\max_{a\leq k\leq l}\left\|\sum_{i=a}^{k-1}\tau_{i+1}\epsilon_{i+1}\right\|.
\]
To see this, the terminal coefficient is the identity and each consecutive coefficient difference has norm at most \(C\tau_{i+1}\), because all remaining products have norm at most one. The block sum of step sizes is uniformly bounded, so this expression has the required order.

Across a full block the homogeneous product norm is at most a fixed \(\rho<1\), since its sum of step sizes is bounded below. Consequently
\[
\|Z_{a_{j+1}}\|\leq\rho\|Z_{a_j}\|+C\sqrt{\log a_j/a_j^\alpha}.
\]
Successive values of the displayed rate have ratio tending to one. Geometric iteration proves the bound at block endpoints, and the partial-block estimate proves it everywhere. This proves the adaptive linear-noise estimate without assuming independence or predictability of future product factors.

## 6. The local chart recursion

Assume the additional local hypotheses. Let
\[
\Delta_s=R_{\theta^\star}^{-1}(\theta^s),\qquad
A=\operatorname{Hess}L(\theta^\star),\qquad z_s=A^{1/2}\Delta_s.
\]
All calculations below are eventually inside a fixed sufficiently small coordinate neighborhood. Smooth cutoff extensions of the chart maps outside a smaller neighborhood, followed by localization, justify conditional estimates without conditioning on a future event of remaining in that neighborhood.

For \(F_\theta(v)=R_{\theta^\star}^{-1}(R_\theta(v))\), the integral Taylor formula gives
\[
\Delta_{s+1}=\Delta_s+T_{\star,s}^{-1}v_{s+1}+\rho_{s+1},
\qquad \|\rho_{s+1}\|\leq C\|v_{s+1}\|^2.
\]
Let \(\Gamma_{\star,s}\) denote local geodesic parallel transport and set
\[
\widetilde P_{s+1}=\Gamma_{\star,s}^{-1}P_{s+1}\Gamma_{\star,s}.
\]
Section 3 bounds its eigenvalues above and below. The geometric comparison and differentiability of the gradient give
\[
T_{\star,s}^{-1}\Gamma_{\star,s}=I+O(\|\Delta_s\|^2),
\qquad
\Gamma_{\star,s}^{-1}h_s=A\Delta_s+o(\|\Delta_s\|).
\]
The second remainder is little-o, not necessarily quadratic.

Keep the complete chart differential in the noise coefficient. The recursion can then be written
\[
z_{s+1}=(I-\tau_{s+1}C_{s+1})z_s
 +\tau_{s+1}\epsilon_{s+1}+\tau_{s+1}e_s+r_{s+1},
\]
where
\[
C_{s+1}=A^{1/2}\widetilde P_{s+1}A^{1/2},
\qquad
\epsilon_{s+1}=-A^{1/2}T_{\star,s}^{-1}P_{s+1}(\widehat g_s-h_s).
\]
The remaining deterministic drift error satisfies \(\|e_s\|\leq a_s\|z_s\|\) with \(a_s\to0\), and \(r_{s+1}=A^{1/2}\rho_{s+1}\) satisfies
\[
\mathbb E[\|r_{s+1}\|\mid\mathcal F_s]\leq C\tau_{s+1}^2.
\]
These statements follow respectively from the preceding two expansions and the conditional second-moment bound together with the local spectral bound.

The matrices \(C_{s+1}\) are symmetric positive definite with eventual uniform spectral bounds. Thus \(I-\tau_{s+1}C_{s+1}\) is contractive. Equivalently, the original linearization is contractive in the fixed Hessian norm, not necessarily in the baseline norm.

Set \(p=2+2\eta>2/\alpha\). Compactness bounds the right-hand side of the oracle higher-moment assumption. Jensen's inequality, bounded local coordinate maps and preconditioners, and the fresh-sampling law give
\[
\mathbb E[\epsilon_{s+1}\mid\mathcal F_s]=0,
\qquad
\mathbb E[\|\epsilon_{s+1}\|^p\mid\mathcal F_s]\leq C
\]
after localization. All hypotheses of Section 5 have now been checked.

## 7. Absorption and the stated rate

Let \(Z_s\) solve the linear recursion with the matrices \(C_{s+1}\) and noise \(\epsilon_{s+1}\), starting at a sufficiently late fixed index. Section 5 gives
\[
\|Z_s\|=O(b_s),\qquad b_s=\sqrt{\log s/s^\alpha}\quad\text{a.s.}
\]
For \(E_s=z_s-Z_s\), contractivity gives eventually
\[
\|E_{s+1}\|\leq(1-c\tau_{s+1})\|E_s\|
 +\tau_{s+1}a_s(\|E_s\|+\|Z_s\|)+\|r_{s+1}\|.
\]
Since \(a_s\to0\), absorb its coefficient of \(\|E_s\|\) and obtain, for some \(c_0>0\),
\[
\|E_{s+1}\|\leq(1-c_0\tau_{s+1})\|E_s\|
 +C\tau_{s+1}b_s+\|r_{s+1}\|.
\]
The scalar convolution of \(\tau_{s+1}b_s\) with these contraction factors is \(O(b_s)\). One direct verification uses \(b_{s+1}/b_s=1+O(1/s)\) and \(s^{-1}=o(\tau_s)\): a sufficiently large multiple of \(b_s\) is eventually a supersolution. The homogeneous term decays stretched-exponentially.

It remains to bound the scalar recursion
\[
U_{s+1}=(1-c_0\tau_{s+1})U_s+\|r_{s+1}\|,\qquad U_N=0.
\]
Fix the \(\delta>0\) in the requested conclusion and define
\[
h_s=\frac{s^{2\alpha-1}}{(\log s)^{2+\delta/2}}.
\]
The ratio \(h_{s+1}/h_s=1+O(1/s)\). Hence
\[
\mathbb E[h_{s+1}U_{s+1}\mid\mathcal F_s]
\leq h_sU_s+\frac{C}{s(\log s)^{2+\delta/2}}
\]
eventually: the coefficient \((h_{s+1}/h_s)(1-c_0\tau_{s+1})\) is at most one. The final series is summable. Robbins-Siegmund gives
\[
U_s=O\!\left(\frac{(\log s)^{2+\delta/2}}{s^{2\alpha-1}}\right)\quad\text{a.s.}
\]
It follows that
\[
\|z_s\|=O\!\left(\sqrt{\frac{\log s}{s^\alpha}}+
\frac{(\log s)^{2+\delta/2}}{s^{2\alpha-1}}\right)\quad\text{a.s.}
\]
Local equivalence of the Hessian norm, the retraction-coordinate norm, and Riemannian distance yields
\[
d(\theta^s,\theta^\star)^2
=O\!\left(\max\left\{\frac{\log s}{s^\alpha},
\frac{(\log s)^{4+\delta}}{s^{4\alpha-2}}\right\}\right)\quad\text{a.s.}
\]
The assertion holds for each \(\delta>0\); if a common probability-one event is desired, intersect the events for a countable sequence of positive exponents decreasing to zero and use monotonicity. Finally, when \(\alpha>2/3\), the positive power gap \(4\alpha-2-\alpha\) dominates the logarithmic factor, giving \(O(\log s/s^\alpha)\).

All theorem-critical obligations are closed. The source's specialized stochastic-rate citation is not an unresolved dependency of this proof.
