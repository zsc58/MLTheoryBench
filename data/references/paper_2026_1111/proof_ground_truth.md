# Reference Proof

Let \(\mathcal Q\), \(p^*\), \(\Delta^*\), \(P_0\), and the epoch policy have the meanings in the task. Classical finite-state average-reward theory under weak communication gives a state-independent gain \(\alpha_p\). The chosen unichain policy has gain \(\alpha^*\), and its Poisson equation has a solution \(v^*\), unique up to a shift. Write \(b=|v^*|_{\rm span}\) and \(\bar r(x)=\sum_a\Delta^*(a\mid x)r(x,a)\).

**Testing.** While \(\Delta^*\) runs, fix an epoch start \(m\) and condition on its starting history. Under the null the subsequent state transitions have matrix \(P_0\). On paths using only positive \(P_0\) edges, each fixed-\(Q\) likelihood product is a nonnegative supermartingale: its conditional multiplicative expectation is \(\sum_{y:P_0(y\mid x)>0}Q(y\mid x)\leq1\). Integration over the prior preserves this property and gives initial value one. A zero-\(P_0\) edge has null probability zero. Bounded stopping followed by monotone convergence, equivalently Ville's inequality, therefore gives conditional probability at most \(\rho\) of rejection at any time in the epoch.

For completeness, the expected-delay argument is uniform over initial states. Fix an alternative matrix \(P\) with \(P|_{C_0}\ne P_0|_{C_0}\). Every closed class \(C\) of \(P\) has stationary-weighted divergence \(I_C(P\Vert P_0)>0\): if it were zero, the two full transition rows would agree on \(C\), making \(C\) closed under \(P_0\); the unique closed class \(C_0\) would be contained in \(C\), contradicting the difference on \(C_0\). A class with an edge positive under \(P\) and zero under \(P_0\) yields rejection upon traversing that edge. Finite-state hitting and return times give a finite expected time to do so, including the time to enter \(C\).

For a class with \(0<I_C<\infty\), put \(\epsilon=I_C/2\). Full support of the positive-parameter product Dirichlet prior gives \(c=\nu\{Q:Q(y\mid x)\geq e^{-\epsilon}P(y\mid x)\text{ for all }x,y\}>0\). Until a zero-\(P_0\) edge has already caused rejection, \(\Lambda_{m,m+n}\geq c\exp(S_n)\), where \(S_n\) sums \(\log(P/P_0)-\epsilon\) along the \(n\) observed transitions. Thus crossing \(\beta=\log(1/(\rho c))\) forces rejection. After entry into \(C\), split the finite chain into return cycles to a reference state. Their lengths and log-likelihood increments are iid; finite-state return times have exponential tails, the increments are integrable, and their expected increment is \(I_C/2\) times the expected cycle length, hence positive. For sufficiently small \(t>0\), the negative exponential moment of an increment is less than one. Applying the exponential bound to the cycle counter gives expected cycles to cross a level \(\beta-y\) bounded by \(K_C(1+(\beta-y)_+)\). Wald's identity then gives the same-order expected elapsed time. The expected entrance time is finite and the pre-entrance log-likelihood, on paths without an earlier zero edge, is bounded below by minus a constant times that entrance time. Summing over the finitely many possible closed classes proves
\[
 \sup_{x\in S}\mathbb E_x^P\tau_{0,\rho}\leq K_P(1+\log(1/\rho)). \tag{1}
\]
All constants here may depend on \(P,P_0,\nu\), but not on \(x,m,\rho\). A zero edge encountered earlier only shortens rejection time. This establishes the testing obligations without taking a paper-specific test theorem as an unexplained premise.

**Kernels with \(P=p_{\Delta^*}=P_0\).** This case includes \(p^*\), but may include other kernels: the test observes only transitions generated while \(\Delta^*\) runs. Under any such \(p\), the Poisson equation and the conditional action law make
\[
 v^*(X_n)+\sum_{t<n}(r(X_t,A_t)-\alpha^*)
\]
a martingale throughout each \(\Delta^*\) period. Optional stopping at any bounded end of such a period gives expected excess reward \(\mathbb E[v^*(X_{\rm start})-v^*(X_{\rm end})]\). Join \(\Delta^*\) periods across epoch boundaries whenever no RL segment intervenes. The joined periods are separated only by rejections that actually start RL, including a rejection at the last action time of an epoch. For any horizon \(T\), telescoping the potential across these periods bounds their combined expected excess below by \(-b(1+\mathbb EN_T)\), where \(N_T\) is the number of such rejections before \(T\). Conditional type-I control gives \(\mathbb EN_T\leq\sum_{j\geq1}\rho_j\). Each RL step has \(r-\alpha^*\geq-1\), and expected RL steps are at most \(\sum_{j\geq1}L_j\rho_j\). These statements include a horizon inside an epoch. Consequently, for every \(T\),
\[
 \mathbb E_{\mu}^{\pi^*,p}\sum_{t<T}(r_t-\alpha^*)
 \geq-b\left(1+\sum_{j\geq1}2^{-\zeta j}\right)
       -\sum_{j\geq1}2^{-(\zeta-1)j}
 =-\frac{2^\zeta}{2^\zeta-1}b-\frac1{2^{\zeta-1}-1}. \tag{2}
\]
The conditional calculation is valid even if earlier epochs used RL, because the test restarts and, up to rejection, the current epoch follows \(\Delta^*\).

**Distinguishable kernels.** For \(p\ne p^*\), uniqueness gives \(d_p=\alpha_p-\alpha^*>0\). The assumed RL property for the fixed reward and every starting state implies that, for some finite \(T_0=T_0(p,r)\), a fresh RL run of any integer length \(h\geq0\) from any state has expected excess reward at least \(d_ph/2-2T_0\). Indeed the asymptotic inequality holds beyond a state-specific threshold; take the maximum over the finite state set and use \(r-\alpha^*\geq-1\) for shorter runs.

Suppose \(P=p_{\Delta^*}\) differs from \(P_0\) on \(C_0\). Conditional on each epoch-start history, coupling its testing phase to a continued \(\Delta^*\) run and using (1) bounds the expected testing length in epoch \(j\), even when truncated by the epoch or horizon, by \(K_P(1+\zeta j\log2)\). Testing steps have excess at least \(-1\). Conditional on the rejection history, the restarted RL phase is a fresh run from the rejection state, so the preceding RL bound applies to its remaining, possibly zero, length. Summing over all epochs intersecting \([0,T)\), with \(J=O(\log(T+2))\), yields
\[
 \mathbb E_{\mu}^{\pi^*,p}\sum_{t<T}(r_t-\alpha^*)
 \geq \frac{d_p}{2}T
 -(1+d_p/2)K_P\sum_{j=1}^{J}(1+\zeta j\log2)-2T_0J
 =\frac{d_p}{2}T-O_p((\log(T+2))^2). \tag{3}
\]
Thus this kernel has transient value \(+\infty\) and lower average reward strictly greater than \(\alpha^*\). Under identifiability, every \(p\ne p^*\) not covered by (2) is distinguishable. Under irreducibility, \(C_0=S\), so \(P\ne P_0\) is distinguishable. Hence (2) and (3) cover all \(p\in\mathcal P\), proving the claimed transient bound and a lower average reward of at least \(\alpha^*\) for each kernel. Finally, no policy can have robust lower average reward exceeding \(\alpha_{p^*}=\alpha^*\), by the classical optimal-gain bound at \(p^*\). This proves robust optimality.
