# Reference Proof

For clarity, all feedback policies are fixed maps, E averages over innovations at a fixed initial state, and E_0 averages over the independent initial state. The compact-action finite-horizon Bellman and measurable-minimum result used here says that a jointly continuous one-step cost-plus-expected-continuation function on R^d x A, with A compact, has a Borel minimizing selector; backward induction gives an optimal Markov policy. Its hypotheses hold here: g is Lipschitz, the coefficients and costs are continuous in state and action, Gaussian first moments and uniform linear growth make each continuation expectation finite and jointly continuous, and induction preserves continuity. Thus V_0 is measurable and finite, and the source's randomized-value representation is valid. In particular, for every alpha in G^N, V_0(x)<=tilde J(0,x,alpha), and all expectations below are well-defined.

Write bar alpha=bar alpha^epsilon. Because hat alpha is admissible, hat V_0(xi)-V_0(xi)>=0 almost surely. Crucially, use eta-suboptimality before choosing a comparison policy. Epsilon-optimality gives

E_0|hat V_0(xi)-V_0(xi)| <= inf_{alpha in hat G_L^N} E_0[tilde J(0,xi,alpha)-tilde J(0,xi,bar alpha)]+epsilon+eta
<= inf_{alpha in hat G_L^N}(E_0|tilde J(0,xi,alpha)-tilde J(0,xi,bar alpha)|^2)^(1/2)+epsilon+eta.

Fix an arbitrary alpha in hat G_L^N. At a fixed initial state x, couple its Euler trajectory Y_j and the reference trajectory X_j with the same innovations. Put D_j=Y_j-X_j and q_j=|alpha_j(X_j)-bar alpha_j(X_j)|. Inserting alpha_j(X_j) and using the Lipschitz bounds gives |delta b_j|<=([b]_1+L[b]_2)|D_j|+[b]_2 q_j and |delta sigma_j|<=([sigma]_1+L[sigma]_2)|D_j|+[sigma]_2 q_j. Conditional centering and unit covariance of Z_{j+1}, followed by tau<=T, imply

E[|D_{j+1}|^2 | Z_1,...,Z_j] <= (1+C_{T,L} tau)|D_j|^2+C_{T,L} tau q_j^2.

Since D_0=0, discrete Gronwall yields

max_{0<=j<=N} E|D_j|^2 <= C_{T,L} tau sum_{j=0}^{N-1} E q_j^2.                                                    (1)

No regularity of bar alpha is used. Also, the running-cost difference at step j is bounded by ([f]_1+L[f]_2)|D_j|+[f]_2 q_j. Jensen's inequality for the innovation expectation, Cauchy–Schwarz for the time sum, and the Lipschitz property of g give

|tilde J(0,x,alpha)-tilde J(0,x,bar alpha)|^2
<= (4T^2([f]_1+L[f]_2)^2+2[g]^2) max_j E|D_j|^2+4T[f]_2^2 tau sum_j E q_j^2
<= C_{T,L} tau sum_j E q_j^2.                                                            (2)

These bounds hold conditionally for each realization x=xi(omega_0), so they may be integrated with E_0.

The source's moment estimate can be verified with constants uniform in N. For an arbitrary measurable feedback and deterministic x, uniform linear growth bounds both coefficients by K(1+|state|). Decompose X_j-x into the accumulated drift and the martingale sum of sigma(t_i,X_i,alpha_i(X_i))sqrt(tau)Z_{i+1}. Cauchy–Schwarz bounds the expected squared maximum of the drift by t_j times the sum of tau-weighted expected squared drifts. The discrete L2 maximal inequality for a square-integrable martingale, E max_{i<=j}|M_i|^2<=4E|M_j|^2, bounds its martingale counterpart by four times the sum of tau-weighted expected squared Frobenius norms; the predictable Gaussian increments verify its hypotheses. With Gamma_j=E max_{i<=j}|X_i-x|^2 and E|X_i|^2<=2|x|^2+2Gamma_i, this gives Gamma_j<=C_T tau sum_{i<j}(1+|x|^2+Gamma_i). Discrete Gronwall therefore proves

E max_{0<=j<=N}|X_j-x|^2 <= C_T(1+|x|^2).                                                   (3)

In particular, this calculation uses the coefficient 8([b]_1^2 T+4[sigma]_1^2), rather than the incorrect coefficient in the source's intermediate displayed bound.

For |x|<=R, M>R, and each j, exit from the closed ball B_M implies |X_j-x|>=M-R. Applying Markov's inequality to (3), including when R=0, gives

E_0[max_j P_Z(X_{t_j}^{xi,bar alpha} notin B_M | xi)] <= C_T(1+E_0|xi|^2)/(M-R)^2,           (4)

where P_Z denotes probability over the innovations with xi held fixed. For each comparison policy, q_j^2 is at most sup_{z in B_M}|alpha_j(z)-bar alpha_j(z)|^2 on B_M and at most diam(A)^2 outside it. Consequently, (2)–(4) yield

E_0|tilde J(0,xi,alpha)-tilde J(0,xi,bar alpha)|^2
<= C_{T,L}[tau sum_j sup_{z in B_M}|alpha_j(z)-bar alpha_j(z)|^2+T diam(A)^2(1+E_0|xi|^2)/(M-R)^2].

The comparison class is the Cartesian product hat G_L^N. Since N is finite and its coordinates can be selected independently, the infimum of its sum of nonnegative squared supremum errors equals the sum of the coordinatewise infima, whether or not individual infima are attained. Those infima are d_{infty,B_M}^2(bar alpha_j,hat G_L). Insert this result into the earlier comparison inequality, use sqrt(u+v)<=sqrt(u)+sqrt(v), and enlarge C_{T,L} to absorb factors depending on T. This gives the claimed estimate with the stipulated constant dependencies. The calculation nowhere divides by sigma or assumes a transition density, so it also covers degenerate and deterministic dynamics.
