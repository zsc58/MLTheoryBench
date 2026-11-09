# Reference Proof

## Contract and proof obligations

Use the recorded-history filtration \(\mathcal F_t=H_t\). Fresh context/potential-outcome draws are independent of \(\mathcal F_{t-1}\), and action selection is unconfounded conditional on \((\mathcal F_{t-1},X_t)\). The obligations are: a weighted uniform law; target-Jacobian convergence and local derivative control; a normalized score CLT; existence of data-measurable bounded approximate roots at the required residual rate; consistency and linearization of every such root; the joint limit; and sandwich consistency.

The only specialized external result used is the following standard-independent martingale triangular-array CLT. A square-integrable scalar array \(\xi_{T,t}\), adapted within each row and having zero conditional means, satisfies \(\sum_t\xi_{T,t}\Rightarrow N(0,v)\) if its summed predictable variances converge in probability to a finite deterministic \(v\), and for every \(\varepsilon>0\), \(\sum_t E[\xi_{T,t}^2 1\{|\xi_{T,t}|>\varepsilon\}\mid\mathcal F_{t-1}]\to_p0\). Its hypotheses are checked below. Zero-variance projections also follow directly from the second-moment calculations. No matrix concentration or martingale strong-law statement from the ancillary Appendix D record is needed.

## 1. Weighted uniform law and derivative control

Fix an arm and suppress its subscript when convenient. Write \(W_t=1\{A_t=a\}/\pi_t(a)\), \(g_t(\theta)=g(X_t,Y_t(a);\theta)\), and \(m(\theta)=E g_t(\theta)\). Weighted quantities involving potential outcomes equal observable quantities whenever their indicator is nonzero. Unconfoundedness and the fresh-draw model give, for any integrable measurable function \(f\),
\[
E[W_t f(X_t,Y_t(a))\mid\mathcal F_{t-1}]=E f(X,Y(a)).
\]
If \(f\) is square-integrable, conditioning first on history and context gives
\[
E\|W_t f(X_t,Y_t(a))\|^2\le \pi_{\min,t}^{-1}E\|f(X,Y(a))\|^2.
\]
Centered weighted terms are martingale differences. For distinct times their inner-product expectations vanish by iterated conditioning. Consequently
\[
E\left\|T^{-1}\sum_{t\le T}(W_t f_t-Ef_t)\right\|^2
\le T^{-2}\sum_{t\le T}\pi_{\min,t}^{-1}E\|f_t\|^2.
\]

Let \(\Theta=\{\theta:\|\theta\|\le R_\theta\}\). At every point of a fixed finite \(\eta\)-net of \(\Theta\), the preceding bound and the first propensity-rate condition give \(G_T(\theta)-m(\theta)\to_p0\). The gradient envelope gives
\[
\|g_t(\theta)-g_t(\theta')\|\le\phi_a(X_t,Y_t(a))\|\theta-\theta'\|.
\]
The random Lipschitz constant \(L_T=T^{-1}\sum_tW_t\phi_a(X_t,Y_t(a))\) has expectation \(E\phi_a\le\sqrt{M'_2}\), so it is uniformly tight. The population Lipschitz constant is at most \(E\phi_a\). Thus
\[
\sup_{\Theta}\|G_T-m\|\le \max_{\text{net}}\|G_T-m\|+\eta(L_T+E\phi_a).
\]
For any tolerance, first make the tightness tail small, then choose \(\eta\) small, then let \(T\to\infty\). This proves the uniform law. Continuity makes the displayed suprema measurable through a countable dense subset.

Each entry of \(\nabla g_t(\theta^*)\) is bounded in absolute value by \(\phi_a\). Applying the same martingale variance calculation entrywise yields
\[
\dot G_T(\theta^*)\to_p J.
\]
Set \(B_T=T^{-1}\sum_tW_t\Phi_a(X_t,Y_t(a))\). It is nonnegative with \(EB_T=E\Phi_a<\infty\), hence \(B_T=O_p(1)\). Each component Hessian of \(G_T\), throughout the prescribed neighborhood, has operator norm at most \(B_T\). In particular, its component gradient is \(B_T\)-Lipschitz there. Taylor remainders in vector norm are at most \(\sqrt d\,B_T\|\delta\|^2/2\) along a segment in that neighborhood. These mean-value bounds require twice differentiability and the envelope, not continuity of second derivatives. Dominated differentiation using \(\phi_a\) also identifies the population derivative at the target as \(J\).

## 2. Score normalization and predictable covariance

Let \(Z_t=W_tg_t(\theta^*)\) and \(M_a(x)=E[g_t(\theta^*)g_t(\theta^*)^\top\mid X_t=x]\). Then \(E[Z_t\mid\mathcal F_{t-1}]=0\), \(\|M_a(x)\|_{\rm op}\le M_2\), and \(E[\|g_t(\theta^*)\|^2\mid X_t]\le dM_2\). In particular \(\bar I_a\) is finite and positive semidefinite.

The predictable covariance sum of \(S_{a,T}^{-1}\sum_tZ_t\) is
\[
V_{a,T}=S_{a,T}^{-2}\sum_t E[\pi_t(a)^{-1}M_a(X_t)\mid\mathcal F_{t-1}].
\]
It is essential to retain the outer expectation over the current context. Given history and context, the score mean generally does not vanish, so the unintegrated second moment is not itself the conditional covariance needed by this martingale CLT.

Put \(q_{T,t}=r_{a,t}^{-1}/S_{a,T}^2\) and \(e_t=E|r_{a,t}/\pi_t(a)-\rho(a,X_t)|\). The weights are nonnegative, sum to one, and tend to zero for each fixed \(t\), because \(S_{a,T}\to\infty\). Fresh contexts and deterministic \(\rho\) give
\[
V_{a,T}-\bar I_a
=\sum_tq_{T,t}E[(r_{a,t}/\pi_t(a)-\rho(a,X_t))M_a(X_t)\mid\mathcal F_{t-1}],
\]
so
\[
E\|V_{a,T}-\bar I_a\|_{\rm op}\le M_2\sum_tq_{T,t}e_t\longrightarrow0.
\]
Indeed, for any \(\delta>0\), choose a fixed index after which \(e_t\le\delta\). The finite initial weighted sum vanishes and the remaining sum is at most \(\delta\). Each initial \(e_t\) is finite by the deterministic propensity lower bound. This proves the needed weighted-averaging assertion without any additional regularity of the rate sequence.

For any fixed \(c\in\mathbb R^d\),
\[
E[(c^\top Z_t)^4\mid\mathcal F_{t-1}]
\le \|c\|^4M_4\pi_{\min,t}^{-3}.
\]
Therefore, for every \(\varepsilon>0\), the conditional Lindeberg sum for \(c^\top Z_t/S_{a,T}\) is at most
\[
\frac{\|c\|^4M_4}{\varepsilon^2 S_{a,T}^4}\sum_t\pi_{\min,t}^{-3}\longrightarrow0.
\]
Square integrability, adaptedness, zero conditional means, and predictable variance convergence have all been verified. The martingale CLT and Cramer-Wold yield
\[
U_{a,T}:=S_{a,T}^{-1}\sum_t Z_t=b_{a,T}G_{a,T}(\theta_a^*)\Rightarrow N(0,\bar I_a).
\]
For a zero-variance projection, \(E[(c^\top U_{a,T})^2]=c^\top EV_{a,T}c\to0\), which proves the degenerate case directly. Also \(U_{a,T}=O_p(1)\), independently of any estimator construction.

## 3. Measurable approximate roots and consistency

Consider the comparison point \(\widetilde\theta_T=\theta^*-J^{-1}G_T(\theta^*)\). Since \(b_TG_T(\theta^*)=O_p(1)\) and \(b_T\to\infty\), its displacement is \(O_p(b_T^{-1})\). It lies inside \(\Theta\) and the local Hessian neighborhood with probability tending to one. On this event the Taylor bound gives
\[
G_T(\widetilde\theta_T)
=[I-\dot G_T(\theta^*)J^{-1}]G_T(\theta^*)
+O_p(b_T^{-2})=o_p(b_T^{-1}).
\]
The comparison point need not be a statistical procedure: it is only used to bound the empirical minimum.

To obtain an estimator depending only on recorded data, enumerate a fixed countable dense subset \((v_j)\) of \(\Theta\). Set \(h_T=\inf_j\|G_T(v_j)\|\) and choose the first index \(j\) such that
\[
\|G_T(v_j)\|\le h_T+(Tb_T)^{-1}.
\]
The index exists and is measurable. By continuity, \(h_T=\min_{\theta\in\Theta}\|G_T(\theta)\|\). On the event that the comparison point lies in the ball, the selected residual is bounded by \(\|G_T(\widetilde\theta_T)\|+(Tb_T)^{-1}\). The complementary event has probability tending to zero, so the selected bounded sequence has residual \(o_p(b_T^{-1})\) globally. This proves existence without giving an estimator access to unknown population quantities.

For any bounded approximate-root sequence, its residual tends to zero because \(b_T\to\infty\). For each \(\varepsilon>0\), let \(\delta_\varepsilon=\inf_{\|\theta-\theta^*\|>\varepsilon}\|m(\theta)\|>0\). On \(\{\|\hat\theta-\theta^*\|>\varepsilon\}\),
\[
\delta_\varepsilon\le\sup_{\Theta}\|G_T-m\|+\|G_T(\hat\theta)\|.
\]
The right side tends to zero in probability. Hence every such sequence is consistent.

## 4. Linearization and joint normality

For each component, the scalar mean-value theorem along the segment joining \(\theta^*\) and \(\hat\theta\) produces a row of a matrix \(A_T\) such that
\[
G_T(\hat\theta)-G_T(\theta^*)=A_T(\hat\theta-\theta^*).
\]
On an event with probability tending to one, the segment lies in the local neighborhood and
\[
\|A_T-\dot G_T(\theta^*)\|_{\rm op}\le\sqrt d\,B_T\|\hat\theta-\theta^*\|=o_p(1).
\]
Thus \(A_T\to_pJ\), and it is invertible with probability tending to one. Multiplication by \(b_T\) and the approximate-root residual give
\[
b_T(\hat\theta-\theta^*)=-J^{-1}U_{a,T}+o_p(1).
\]
This proves the single-arm limit and its rate without assuming that rate in order to control the remainder.

For the joint score limit, fix deterministic block vectors \(c_a\) and define
\[
\xi_{T,t}=\sum_{a=1}^K c_a^\top Z_{a,t}/S_{a,T}.
\]
These are scalar martingale differences. Distinct-arm products vanish pointwise, so their total predictable variance is \(\sum_a c_a^\top V_{a,T}c_a\), converging to \(\sum_a c_a^\top\bar I_ac_a\). At each time at most one arm term is nonzero, and hence
\[
\sum_tE[\xi_{T,t}^4\mid\mathcal F_{t-1}]
\le M_4\sum_a\|c_a\|^4 S_{a,T}^{-4}\sum_t\pi_{\min,t}^{-3}\longrightarrow0.
\]
This verifies joint Lindeberg. The martingale CLT and Cramer-Wold give the block-diagonal joint score limit. Stacking the finitely many linearizations and applying Slutsky yields the asserted \(D_T\)-normalized estimator limit.

## 5. Sandwich consistency

The derivative-substitution bound from Section 1 and consistency give
\[
\|\widehat J_{a,T}-\dot G_{a,T}(\theta_a^*)\|_{\rm op}
\le\sqrt d\,B_T\|\hat\theta_a-\theta_a^*\|=o_p(1)
\]
on an event with probability tending to one. Thus \(\widehat J_{a,T}\to_pJ_a\).

For the true-parameter meat, define \(Q_T=S_{a,T}^{-2}\sum_tZ_{a,t}Z_{a,t}^\top\). Matrix-entry martingale orthogonality, summed in Frobenius norm, gives
\[
E\|Q_T-V_{a,T}\|_F^2
\le S_{a,T}^{-4}\sum_tE\|Z_{a,t}Z_{a,t}^\top\|_F^2
\le M_4 S_{a,T}^{-4}\sum_t\pi_{\min,t}^{-3}\longrightarrow0.
\]
Together with Section 2 this proves \(Q_T\to_p\bar I_a\).

To justify parameter substitution, let \(\Delta_T=\|\hat\theta_a-\theta_a^*\|\), \(g_t^*=g_t(\theta_a^*)\), and \(\phi_t=\phi_a(X_t,Y_t(a))\). Both parameters lie in the convex ball, so \(\|g_t(\hat\theta_a)-g_t^*\|\le\phi_t\Delta_T\) pointwise. Expanding the two outer products yields
\[
\|\widehat I_{a,T}-Q_T\|_{\rm op}\le2\Delta_T C_T+\Delta_T^2 F_T,
\]
where
\[
C_T=S_{a,T}^{-2}\sum_t\frac{1\{A_t=a\}}{\pi_t(a)^2}\|g_t^*\|\phi_t,
\qquad F_T=S_{a,T}^{-2}\sum_t\frac{1\{A_t=a\}}{\pi_t(a)^2}\phi_t^2.
\]
Conditional Cauchy-Schwarz gives \(E[\|g_t^*\|\phi_t\mid X_t]\le\sqrt{dM_2M'_2}\). Also
\[
L_{a,T}:=S_{a,T}^{-2}\sum_tE[\pi_t(a)^{-1}]
=\sum_tq_{T,t}E[r_{a,t}/\pi_t(a)]\longrightarrow E\rho(a,X),
\]
by the same early/late weighted split. Hence \(EC_T\le\sqrt{dM_2M'_2}L_{a,T}=O(1)\) and \(EF_T\le M'_2L_{a,T}=O(1)\). Markov gives \(C_T,F_T=O_p(1)\). Since \(\Delta_T=o_p(1)\), the substitution error vanishes and \(\widehat I_{a,T}\to_p\bar I_a\).

Finally, nonsingularity of \(J_a\) implies \(P(\widehat J_{a,T}\text{ singular})\to0\), and inversion is continuous near \(J_a\). Therefore the sandwich estimator, with its specified value on the singular event, converges in probability to \(J_a^{-1}\bar I_aJ_a^{-\top}\). No positive-definiteness assumption on \(\bar I_a\) is needed.

## Source-local repairs and closure

The source sandwich calculation is used with the trace factor \(d\), the limit \(E\rho(a,X)\), and a fourth moment in the centered quadratic bound; see the repair record for theory_007. The Jacobian bilinear calculation retains both test vectors, and componentwise Hessian bounds avoid the source's insufficient tensor factor; see theory_021. All listed proof obligations are explicitly closed. There are no unresolved nonstandard dependencies or private GT gaps.
