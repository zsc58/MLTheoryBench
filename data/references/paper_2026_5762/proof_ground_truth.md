# Reference Proof

Throughout, put \(d=|\mathcal E|\), \(m=k(n-k)\), and \(H=\{z:\sum_i z_i=0\}\). Constants may depend on the fixed instance, model, \(n,k,R,\alpha,\gamma,\lambda\), and a stated polynomial-tail exponent, but not on the horizon or risk level. Analyze the infinite continuation of the procedure in which updates are performed even when a stopping test succeeds. For each risk level its first successful test has exactly the law of the specified stopping time. This allows all allocation and estimation bounds below to be independent of \(\delta\).

The theorem-critical obligations are: deterministic sampling discrepancy; estimator concentration and boundary stabilization; bounded unbiased score estimates; deterministic and stochastic regret bounds despite changing boundary sets; transfer to empirical information; mixture control of erroneous stopping; uniform likelihood-to-information comparison; summable stopping tails; and the matching lower bound. They are derived below.

## 1. Tracking and estimation

Write \(P_e(t)=\sum_{s=1}^t\widetilde w_{s,e}\). The repaired sampling rule chooses a maximizer of \(P_e(t)-N_e(t-1)\). To prove its discrepancy bound, put \(a_e(t)=N_e(t)-P_e(t)\). Immediately before the count increment, the coordinates \(a_e(t-1)-\widetilde w_{t,e}\) sum to \(-1\); the chosen coordinate is a minimum, hence is at most \(-1/d\). Inductively, every coordinate of \(a(t)\) is at most \(1\): an unchosen coordinate can only decrease, and the chosen coordinate becomes at most \(1-1/d\). Since the coordinates sum to zero, each is at least \(-(d-1)\). For \(d\ge2\), this proves
\[
\max_e|N_e(t)-P_e(t)|\le d-1. \tag{1}
\]
For \(d=1\), the discrepancy is identically zero, so (1) also holds. Consequently
\[
N_{\min}(t)\ge d^{-1}\sum_{s=1}^t s^{-\gamma}-(d-1),
\qquad
\left\|\frac{N(t)}t-\frac1t\sum_{s=1}^t w_s\right\|_1
\le d\left(\frac{d-1}{t}+\frac1t\sum_{s=1}^t s^{-\gamma}\right). \tag{2}
\]
Integral comparison gives \(N_{\min}(t)\ge c t^{1-\gamma}\) for all sufficiently large deterministic \(t\), and the second bound is \(O(t^{-1}+t^{-\gamma})\).

Define
\[
\Xi_e(t)=\sum_{s\le t}\mathbf1\{A_s=e\}\{T(Y_s)-\psi'(x_e^Tv)\}.
\]
For each real \(a\), the conditional sub-Gaussian assumption makes
\(\exp\{a\Xi_e(t)-\sigma_{\rm sg}^2a^2N_e(t)/2\}\) a nonnegative supermartingale. For each integer \(j\in\{1,\ldots,t\}\), use \(a=\sqrt{2u}/(\sigma_{\rm sg}\sqrt j)\), and separately its negative, on the event \(N_e(t)=j\). Markov's inequality and a union bound over \(j\) yield
\[
\Pr\{\Xi_e(t)^2/N_e(t)\ge2\sigma_{\rm sg}^2u,\ N_e(t)>0\}\le2t e^{-u}.
\]
Thus, simultaneously over all edges, with probability at least \(1-\varepsilon\),
\[
\Xi_e(t)^2/N_e(t)\le2\sigma_{\rm sg}^2\log(2td/\varepsilon). \tag{3}
\]

For \(h=\widehat v_t-v\), likelihood optimality and the exponential-family KL identity imply
\[
0\le\ell_t(v+h)-\ell_t(v)
=\sum_e(x_e^Th)\Xi_e(t)-\sum_eN_e(t)d_e(v,v+h).
\]
The curvature lower bound gives \(d_e(v,v+h)\ge\underline a(x_e^Th)^2/2\). Weighted Cauchy--Schwarz therefore gives
\[
h^TL_th\le\frac4{\underline a^2}\sum_e\frac{\Xi_e(t)^2}{N_e(t)}.
\]
On \(H\), the complete-graph identity \(\sum_e x_ex_e^T=nI-\mathbf1\mathbf1^T\) implies \(h^TL_th\ge nN_{\min}(t)\|h\|_2^2\). Combining this with (3), after a deterministic warm-up,
\[
\Pr\left\{\|\widehat v_t-v\|_2>
\frac{2\sigma_{\rm sg}}{\underline a}
\sqrt{\frac{n\log(2td/\varepsilon)}{N_{\min}(t)}}\right\}\le\varepsilon. \tag{4}
\]
Taking \(\varepsilon=t^{-2}\), summability and (2) prove almost-sure consistency. If \(\Delta=v_{(k)}-v_{(k+1)}>0\), error at most \(\Delta/4\) in sup norm makes every true crossing difference positive. Hence \(S(\widehat v_t)=S(v)\) and all oriented boundary constraints stabilize almost surely.

The MLE exists by continuity on compact \(\mathcal K\). Its lexicographic selection is measurable: the criterion depends measurably on finitely many counts and sufficient-statistic sums, and successive coordinate minimization on the compact maximizing set gives a measurable compact-argmax selection. The projection used in each update is unique, as established next.

## 2. Oracle geometry and score estimates

The exponential-family identity is
\[
d(\xi,\zeta)=\psi(\zeta)-\psi(\xi)-\psi'(\xi)(\zeta-\xi).
\]
On the bounded parameter interval, \(0\le d_e(a,z)\le D\) for some finite \(D\), for example \(D=8\bar\sigma^2R^2\). For a fixed inversion halfspace, the infimum defining \(g\) is attained, continuous in \(w\), and concave in \(w\), since it is the minimum over a fixed compact set of functions linear in \(w\). Moreover, for a minimizer \(z^*\),
\[
g(w';a)\le D_{w'}(a,z^*)=g(w;a)+\sum_e(w'_e-w_e)d_e(a,z^*). \tag{5}
\]
Thus these divergences give the needed supergradient directly, without any differentiability assumption at disconnected allocations.

Every actual \(w_t\) has full support. The Hessian in the projected parameter is
\(\sum_e w_{t,e}\psi''(x_e^Tz)x_ex_e^T\), positive definite on \(H\). Hence the projection is unique. The inversion set is nonempty because it contains zero. Compactness and strict convexity also give measurable dependence of this projection on its inputs.

Fix the true boundary and its orientations. For these fixed constraint sets, differentiating the divergence in its first scalar parameter gives \(\partial_\xi d(\xi,\zeta)=\psi''(\xi)(\xi-\zeta)\). Therefore, with \(L=4R\bar\sigma^2\sqrt2\),
\[
|g_{ij}(w;a)-g_{ij}(w;a')|\le L\|a-a'\|_2,
\qquad
|F_a(w,q)-F_{a'}(w,q)|\le L\|a-a'\|_2. \tag{6}
\]
Here the notation for varying \(a\) uses the same fixed true inversion sets; it does not change domains with \(a\). It agrees with the actual game whenever the estimated top set is correct.

Let \(\mathcal I(w;v)=\min_{(i,j)\in\mathcal C(v)}g_{ij}(w;v)\). Minimizing the linear expression in \(q\) gives precisely this minimum. Thus \(\mathcal I^*(v)=\max_w\mathcal I(w;v)\), and the maximum exists by compactness and continuity. Also
\[
|\mathcal I(w;v)-\mathcal I(w';v)|\le D\|w-w'\|_1. \tag{7}
\]
Uniform allocation gives
\(\mathcal I^*(v)\ge\underline a\Delta^2/(2d)>0\): every inversion changes its crossing edge's natural parameter by at least \(\Delta\).

Let \(\mathcal H_t\) be the history after \(Y_t\) and the current iterates are formed but before \(J_t\). Conditional on \(\mathcal H_t\), uniform selection of one of the \(m\) current boundary pairs makes the primal score mean the \(q_t\)-weighted supergradient in (5). Its dual score mean is the vector of projected divergences. Both estimated score vectors have sup norm at most \(G=mD\). On a correct-boundary round, these are the first-order quantities for the fixed true-boundary game. The dual coordinates here are unordered edges, even though the current constraint is conveniently labeled by an ordered pair.

## 3. Regret with a changing estimated boundary

First establish the deterministic exponential-weights bound. For bounded gains \(a_t\in[-G,G]^D\), initial distribution \(p_1\) with full support, cumulative gains \(A_t\), and positive nonincreasing rates \(\eta_t\), let
\[
p_t\propto p_1\exp(\eta_t A_{t-1}),\qquad
\Phi_t=\eta_t^{-1}\log\sum_jp_{1,j}e^{\eta_t A_{t,j}}.
\]
Set \(\Phi_0=0\). Jensen's inequality shows that \(\eta^{-1}\log\sum_jp_{1,j}e^{\eta A_j}\) is nondecreasing in \(\eta>0\). For a variable in \([-G,G]\), the second derivative of its log moment-generating function is a tilted variance at most \(G^2\); integrating twice gives the exponential-moment bound with remainder \(\eta^2G^2/2\). Consequently
\[
\Phi_t-\Phi_{t-1}\le\langle p_t,a_t\rangle+\eta_tG^2/2.
\]
Nonnegativity of relative entropy gives \(\langle p,A_T\rangle\le\Phi_T+\operatorname{KL}(p\|p_1)/\eta_T\). Summing yields
\[
\sup_p\sum_{t=1}^T\langle a_t,p-p_t\rangle
\le\frac{\max_j\log(1/p_{1,j})}{\eta_T}
+\frac{G^2}{2}\sum_{t=1}^T\eta_t. \tag{8}
\]
Removing the first \(b-1\) terms costs at most \(2G(b-1)\). Losses are handled by taking negative gains.

There is an important fixed-domain bookkeeping issue for the dual player. Let \(B\subseteq\mathcal E\) be the unordered true boundary. Define a shadow dual sequence for every time by restricting the actual cumulative dual edge scores to \(B\) and normalizing their exponential weights there. Its initial distribution is uniform on \(B\). This sequence follows (8) on the fixed simplex \(\Delta_B\), even before the actual estimated boundary is correct. On every round with \(S(\widehat v_t)=S(v)\), it equals the actual dual iterate, after identifying the oriented pair with its unordered edge. Thus on a correct window \([b,T]\), the actual dual linearized regret is bounded by (8) for this shadow sequence plus the initial-segment cost. The primal bound applies directly to its actual full-horizon score sequence.

One must not condition martingale concentration on correctness of an entire future window. Instead let \(C_t=\mathbf1\{S(\widehat v_t)=S(v)\}\), which is \(\mathcal H_t\)-measurable. Multiply each centered estimated-score coordinate by \(C_t\), defining the product as zero on incorrect rounds. These products have conditional mean zero and magnitude at most \(2G\). Their inner products with \(w_t\), or with the shadow dual iterate, have the same properties. For any such increment \(X_t\), the same bounded-variable calculation used above gives
\(\mathbb E[e^{aX_t}\mid\mathcal H_t]\le e^{2a^2G^2}\). Iteration and Markov's inequality give a tail at most \(\exp[-x^2/(8G^2T)]\) for its sum. A coordinate union bound and the predictable-inner-product bound control the supremum over each simplex. On a correct window the masked sums equal the required score-noise sums.

Combining these facts with (5) and linearity in the dual variable proves, jointly with correctness of \([b,T]\), that both estimated-game regrets are at most
\[
C\left(T^\alpha+\sum_{s=1}^T s^{-\alpha}+b+\sqrt{T\log(C/\varepsilon)}\right) \tag{9}
\]
except on an event of probability at most \(\varepsilon\). This is a joint good-window bound, not a conditional concentration assertion.

Fix \(p>1\) and take \(b=\lceil T^{1/4}\rceil\). Apply (4) for every \(s\in[b,T]\) with failure probability \(T^{-(p+3)}\). For all sufficiently large deterministic \(T\), their joint event makes the whole window correct and gives
\[
\|\widehat v_s-v\|_2\le C_p\sqrt{\log T}\,s^{-(1-\gamma)/2}.
\]
The event fails with probability at most \(T^{-(p+2)}\). Its average error on the window is at most \(C_pT^{-(1-\gamma)/2}\sqrt{\log T}\), by integral comparison. Equation (6) adds at most twice the sum of these errors to each player's true-game regret.

Let \(T'=T-b+1\), and let \(w^\circ,q^\circ\) be the window averages. Linearity in \(q\), concavity in \(w\), and cancellation of the played payoffs give
\[
\sup_w F_v(w,q^\circ)-\inf_qF_v(w^\circ,q)
\le\frac{\operatorname{Reg}_w^v+\operatorname{Reg}_q^v}{T'}.
\]
The first term is at least \(\mathcal I^*(v)\), since \(F_v(w,q^\circ)\ge\min_qF_v(w,q)\) for every \(w\). Hence the regret bound lower-bounds \(\mathcal I(w^\circ;v)\). Replacing the window average by the full average costs at most \(2D(b-1)/T\), by (7); replacing the latter by \(N(T)/T\) uses (2). Choosing the confidence in (9) of polynomial order and combining the events gives, for every \(p>1\), constants \(C_p,T_p\) such that
\[
\Pr_v\{\mathcal I(N(T)/T;v)<\mathcal I^*(v)-r_T\}\le T^{-p},\qquad T\ge T_p, \tag{10}
\]
where one can take
\[
r_T=C_p\left(T^{\alpha-1}+T^{-\alpha}+\sqrt{\frac{\log T}{T}}
+T^{-(1-\gamma)/2}\sqrt{\log T}+T^{-\gamma}+T^{-3/4}+T^{-1}\right).
\]
All terms vanish for the stated exponents. Summability and the deterministic upper bound \(\mathcal I(N(T)/T;v)\le\mathcal I^*(v)\) prove almost-sure convergence to the oracle value.

## 4. Risk control

For every fixed \(z\in H\), including those outside \(\mathcal K\), the globally defined exponential family makes \(\exp\{\ell_t(z)-\ell_t(v)\}\) a mean-one likelihood-ratio martingale in the complete algorithm history. Algorithm randomization has the same conditional law under both parameters and contributes no likelihood factor. Integrating against a centered Gaussian of precision \(\lambda\) on \(H\) preserves the martingale property by nonnegative integration. Call the resulting process \(M_t\), with \(M_0=1\).

Choose an orthonormal basis matrix \(U\) of \(H\), and put
\[
f_t(a)=\ell_t(Ua)-\lambda\|a\|_2^2/2,
\qquad Q_t=\lambda I_{n-1}+\bar\sigma^2U^TL_tU.
\]
Global curvature gives \(-\nabla^2f_t\preceq Q_t\) everywhere. The function \(f_t\) is strongly concave and coercive: concavity bounds \(\ell_t(Ua)\) above by an affine function, and the negative quadratic dominates. Thus it has a maximizer \(a_t^\lambda\) with zero gradient. Taylor's inequality gives
\[
f_t(a)\ge f_t(a_t^\lambda)-\tfrac12(a-a_t^\lambda)^TQ_t(a-a_t^\lambda).
\]
Integrating this Gaussian lower envelope and using \(f_t(a_t^\lambda)\ge f_t(U^T\widehat v_t)\) yields
\[
M_t\ge\exp\left\{\ell_t(\widehat v_t)-\ell_t(v)
-\frac\lambda2\|\widehat v_t\|_2^2
-\frac12\log\det\left(I_n+\frac{\bar\sigma^2}{\lambda}L_t\right)\right\}. \tag{11}
\]
The determinant on \(H\) equals the displayed determinant because \(L_t\mathbf1=0\). This argument explains why the source's global, rather than merely local, curvature assumption is necessary for this proof.

At an incorrect finite stop, choose \(i\in S(\widehat v_t)\setminus S(v)\) and \(j\in S(v)\setminus S(\widehat v_t)\). Then \(v_i<v_j\), so the true parameter is feasible in that declared inversion set. Therefore
\(b(t,\delta)\le Z_{ij}(t)\le\ell_t(\widehat v_t)-\ell_t(v)\), and (11) gives \(M_t\ge1/\delta\). A nonnegative mean-one martingale satisfies \(\Pr(\sup_tM_t\ge c)\le1/c\): stop at its first crossing before a deterministic horizon, use its expectation bound, and let the horizon grow. Consequently the probability of an incorrect finite stop is at most \(\delta\).

## 5. GLR convergence and finite stopping

Set
\[
V_t=\sum_{s\le t}x_{A_s}\{T(Y_s)-\psi'(x_{A_s}^Tv)\},
\qquad \Delta_t=\sup_{z\in\mathcal K}|z^TV_t|/t.
\]
Each coordinate of \(V_t\) is a sum of conditionally centered \(\sigma_{\rm sg}^2\)-sub-Gaussian increments. Exponential Markov bounds, optimized in their parameter and union-bounded over coordinates and signs, give
\[
\Pr\left\{\Delta_t>R\sigma_{\rm sg}n
\sqrt{\frac{2\log(2n/\varepsilon)}t}\right\}\le\varepsilon. \tag{12}
\]
In particular \(\Delta_t\to0\) almost surely.

Define
\[
\bar L_t(z)=-\ell_t(z)/t,\qquad
L_t^{\rm pop}(z)=t^{-1}\sum_{s\le t}
\{\psi(x_{A_s}^Tz)-(x_{A_s}^Tz)\psi'(x_{A_s}^Tv)\}.
\]
Then \(\sup_z|\bar L_t(z)-L_t^{\rm pop}(z)|=\Delta_t\), and
\[
L_t^{\rm pop}(z)-L_t^{\rm pop}(v)=D_{N(t)/t}(v,z).
\]
When the estimated top set is correct, expressing the normalized GLR as the difference of two minima and bounding each minimum's perturbation by \(\Delta_t\) gives
\[
\left|Z_{ij}(t)/t-g_{ij}(N(t)/t;v)\right|\le2\Delta_t. \tag{13}
\]
Stabilization, (10), and (12) therefore imply
\[
\frac1t\min_{(i,j)\in\mathcal C(\widehat v_t)}Z_{ij}(t)
\longrightarrow\mathcal I^*(v)>0\quad\text{almost surely}. \tag{14}
\]
Meanwhile, \(\|\widehat v_t\|_2^2\le nR^2\), \(\operatorname{rank}(L_t)\le n-1\), and \(\|L_t\|_{\rm op}\le2t\), so
\[
b(t,\delta)\le B(t,\delta):=\log(1/\delta)+\lambda nR^2/2
+\frac{n-1}{2}\log(1+2\bar\sigma^2t/\lambda). \tag{15}
\]
For fixed \(\delta\), this is \(o(t)\). Equation (14) proves almost-sure finite stopping. Combined with the preceding risk bound, this establishes both fixed-confidence claims. These arguments actually apply to every positive-gap parameter in \(\mathcal K\), including its relative boundary.

## 6. Expected stopping time and lower bound

Fix \(\epsilon>0\), put \(I=\mathcal I^*(v)\), and set
\[
t_\delta=\left\lceil(1+\epsilon)\log(1/\delta)/I\right\rceil,
\qquad c=\epsilon I/[2(1+\epsilon)].
\]
The function \(B(t,\delta)/t\) is decreasing for \(t>0\), since each of its constant-over-\(t\) and \(\log(1+at)/t\) terms is decreasing. For sufficiently small \(\delta\), (15) gives \(b(t,\delta)/t\le I-c\) for every \(t\ge t_\delta\).

Choose any \(p>1\). Equations (4), (10), and (12) imply that, for all \(t\) beyond a fixed deterministic \(t_*\), except on an event of probability at most \(3t^{-(p+2)}\), the boundary is correct, \(\Delta_t\le c/4\), and \(\mathcal I(N(t)/t;v)\ge I-c/2\). Equation (13) then gives the minimum normalized GLR at least \(I-c\). Non-stopping is the strict failure event, so
\[
\Pr_v(\tau_\delta>t)
\le\Pr_v\left\{\min Z_{ij}(t)/t<I-c\right\}
\le3t^{-(p+2)},\qquad t\ge\max(t_\delta,t_*). \tag{16}
\]
No inclusion involving the non-strict event at \(I-c\) is needed. With \(T_\delta=\max(t_\delta,t_*)\), tail summation gives
\[
\mathbb E_v\tau_\delta\le T_\delta+3\sum_{t\ge T_\delta}t^{-(p+2)}.
\]
Dividing by \(\log(1/\delta)\), then sending \(\delta\downarrow0\) and \(\epsilon\downarrow0\), proves the upper bound \(1/I\). The same bounds also give finite expectation for every fixed \(\delta\), by choosing a sufficiently large deterministic threshold-crossing time in (15).

For completeness, the model-specific lower-bound application can be checked directly. Fix \(\delta<1/2\) and any positive-gap alternative \(z\in\mathcal K\) with \(S(z)\ne S(v)\). Let \(E\) be the event that the output equals \(S(v)\). Uniform correctness just proved gives \(\Pr_v(E)\ge1-\delta\) and \(\Pr_z(E)\le\delta\). The stopped likelihood ratio has expected log value
\[
\sum_e\mathbb E_vN_e(\tau_\delta)d_e(v,z).
\]
Indeed, the log-likelihood increments equal their predictable KL means plus a centered term with bounded conditional variance; finite expected stopping time permits stopping and passage to the limit in this centered sum. The sampling and auxiliary-randomization kernels are identical under both parameters and cancel from the ratio. Partitioning the stopped experiment into \(E\) and its complement and applying nonnegativity of relative entropy within each part shows that this expected log ratio is at least the binary relative entropy of the two event probabilities, hence at least \(\operatorname{kl}(1-\delta,\delta)\).

The closure of positive-gap alternatives with a different top set is exactly the union of the inversion sets used in the task. To check the nontrivial direction, take a point in one inversion set and mix it with an interior centered vector with distinct coordinates that strictly reverses that pair. Arbitrarily small mixture weights, avoiding finitely many coordinate-equality values, produce interior positive-gap alternatives with a different top set. Continuity of KL therefore allows the infimum over these genuine alternatives to be replaced by the minimum over the closed inversion sets.

Set \(w_e=\mathbb E_vN_e(\tau_\delta)/\mathbb E_v\tau_\delta\). This is a probability distribution. Taking the alternative infimum gives
\[
\mathbb E_v\tau_\delta\,\mathcal I^*(v)
\ge\mathbb E_v\tau_\delta\,\mathcal I(w;v)
\ge\operatorname{kl}(1-\delta,\delta).
\]
Since \(\operatorname{kl}(1-\delta,\delta)/\log(1/\delta)\to1\), the matching liminf follows. Together with the upper bound, this proves the claimed limit. All listed proof obligations are closed.
