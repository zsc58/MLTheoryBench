# Reference Proof

## Status and obligation audit

The recovery gap identified by F1 in revision 2 is genuine. This replacement closes it below, rather than treating feasibility, trace minimality, or a citation as a recovery theorem. The proof obligations are: uniform stable recovery; exploration-energy control; the causal comparator characterization; replay and transition accounting; rank-sensitive exploitation estimates; and balancing, including bounded remaining horizons. Each is established below.

Write \(n=T-m\), \(\delta_t=v_t-v_{t-1}\), and \(Z=(z_1,\ldots,z_m)\). After the design events have been constructed, expectations hold Z fixed unless stated otherwise. The probes and auxiliary feedback randomization are jointly independent of the minimizer process. The causal feedback and tie-breaking rules make the estimate measurable with respect to the exploration history. Future increments remain martingale differences after adjoining this history and the independent randomization. No conditional covariance upper bound is assumed.

## 1. Measurements and deterministic estimator reductions

The exploration observations satisfy
\[
\widetilde y_t=\tfrac12\langle A,z_tz_t^\top\rangle+\eta_t/\gamma^2.
\]
The true matrix is feasible for the public program. A minimizer exists: intersecting the feasible set with \(\{M\succeq0:\operatorname{tr}M\le\operatorname{tr}A\}\) gives a nonempty compact set. Every selected minimizer \(B=\widehat A\) satisfies
\[
B\succeq0,\qquad \operatorname{tr}B\le\operatorname{tr}A.
\]
The program uses the known noise cap, not the realized noise norm. Zero realized noise therefore does not, by itself, imply exact recovery.

Put \(q=\bar\eta/\gamma^2\) and \(H=B-A\). Feasibility and the triangle inequality give
\[
\begin{aligned}
\frac1m\sum_{t=1}^m|z_t^\top H z_t|
&\le\frac2m\sum_{t=1}^m\left(
\left|\widetilde y_t-\tfrac12z_t^\top Bz_t\right|
+\left|\widetilde y_t-\tfrac12z_t^\top Az_t\right|\right)\\
&\le4q.
\end{aligned}
\]
This is an upper bound on measured error; the probabilistic lower bound needed to use it is proved in Step 2.

Let P project orthogonally onto range(A), and write
\[
H_\perp=(I-P)H(I-P),\qquad H_{\mathcal T}=H-H_\perp.
\]
Then \(H_\perp=(I-P)B(I-P)\succeq0\), \(\operatorname{rank}(H_{\mathcal T})\le2r\), and these two components are Frobenius-orthogonal. Since \(\operatorname{tr}H\le0\),
\[
\operatorname{tr}H_\perp\le-\operatorname{tr}H_{\mathcal T}
\le\|H_{\mathcal T}\|_*.
\]
Consequently
\[
\|H\|_*\le2\|H_{\mathcal T}\|_*
\le2\sqrt{2r}\|H_{\mathcal T}\|_F
\le2\sqrt{2r}\|H\|_F.\tag{1}
\]
These deterministic conclusions hold for every admissible feedback vector and every selected minimizer.

## 2. Uniform Gaussian measurement lower bound

We prove that there are universal positive constants \(c,\kappa,c_*\) such that, if \(m\ge c_*rd\), then with probability at least \(1-e^{-cm}\),
\[
\frac1m\sum_{t=1}^m|z_t^\top H z_t|\ge\kappa\|H\|_F
\quad\text{for all symmetric }H\text{ satisfying }
\|H\|_*\le2\sqrt{2r}\|H\|_F.\tag{2}
\]
The event is uniform in H and depends only on the probes.

### 2.1 Gaussian moments and a uniform small-ball probability

First take symmetric H with \(\|H\|_F=1\). Orthogonal diagonalization and Gaussian rotational invariance give
\[
X=z^\top Hz=\tau+Y,\qquad
\tau=\operatorname{tr}H,\qquad
Y=\sum_i\lambda_i(g_i^2-1),\qquad \sum_i\lambda_i^2=1,
\]
where the \(g_i\) are independent standard normals. Gaussian moments give
\[
\mathbb EX^2=\tau^2+2,
\qquad
\mathbb EY^4=12\Big(\sum_i\lambda_i^2\Big)^2+48\sum_i\lambda_i^4\le60.
\]
Using \((a+b)^4\le8(a^4+b^4)\),
\[
\mathbb EX^4\le8\tau^4+480\le120(\tau^2+2)^2.
\]
For any nonnegative W, Cauchy–Schwarz applied on \(\{W\ge\theta\mathbb EW\}\) gives
\[
\mathbb P(W\ge\theta\mathbb EW)
\ge(1-\theta)^2\frac{(\mathbb EW)^2}{\mathbb EW^2},\qquad 0<\theta<1.
\]
Apply this with \(W=X^2\) and \(\theta=1/2\). Since \(\mathbb EX^2/2\ge1\),
\[
\mathbb P(|z^\top Hz|\ge1)\ge p_0:=1/480.\tag{3}
\]

Let \(\phi:\mathbb R\to[0,1]\) be zero when \(|s|\le1/2\), equal to \(2|s|-1\) when \(1/2<|s|<1\), and equal to 1 when \(|s|\ge1\). It is 2-Lipschitz, \(\phi(0)=0\), and \(\phi(s)\le2|s|\). Equation (3) implies
\[
\mathbb E\phi(z^\top Hz)\ge p_0
\quad\text{whenever }\|H\|_F=1.\tag{4}
\]

### 2.2 Standard independent probability tools used below

We use the following general results, not a specialized matrix-recovery theorem.

1. **Symmetrization.** For independent identically distributed observations, a measurable uniformly bounded function class \(\mathcal G\), and independent Rademacher signs \(\xi_i\),
\[
\mathbb E\sup_{g\in\mathcal G}\left|\frac1m\sum_i g(z_i)-\mathbb Eg(z)\right|
\le2\mathbb E\sup_{g\in\mathcal G}\left|\frac1m\sum_i\xi_i g(z_i)\right|.
\]
2. **Scalar Rademacher contraction.** If \(\phi(0)=0\) and \(\phi\) is L-Lipschitz, then for any bounded set \(\mathcal V\subset\mathbb R^m\),
\[
\mathbb E_\xi\sup_{a\in\mathcal V}\left|\sum_i\xi_i\phi(a_i)\right|
\le2L\mathbb E_\xi\sup_{a\in\mathcal V}\left|\sum_i\xi_i a_i\right|.
\]
3. **Bounded differences.** If a measurable function of independent observations changes by at most \(b_i\) when observation i is replaced, then
\[
\mathbb P(F>\mathbb EF+t)\le\exp\left(-\frac{2t^2}{\sum_i b_i^2}\right).
\]

Here the matrix index set used below is compact in a finite-dimensional space, and the indexed functions are continuous in the matrix argument. The suprema are therefore measurable and may equivalently be taken over a countable dense set. The functions \(\phi(z^\top Hz)\) lie in \([0,1]\). Thus symmetrization applies, contraction applies conditionally on the realized probes, and bounded differences applies with \(b_i=1/m\).

### 2.3 Expected norm of a signed Gaussian covariance matrix

Let
\[
S_m=\frac1m\sum_{i=1}^m\xi_i z_i z_i^\top,
\]
with independent Rademacher signs, independent of the probes. We show
\[
\mathbb E\|S_m\|_{\rm op}\le C\left(\sqrt{\frac dm}+\frac dm\right)\tag{5}
\]
for a universal C.

For any fixed unit vector u, \(u^\top S_mu\) is an average of independent variables distributed as \(\xi g^2\). Their moment-generating function is
\[
f(t)=\mathbb Ee^{t\xi g^2}
=\tfrac12\big[(1-2t)^{-1/2}+(1+2t)^{-1/2}\big].
\]
On \(|t|\le1/4\), \(f(0)=1\), \(f'(0)=0\), and \(f''(t)\le3\cdot2^{5/2}<17\). Taylor's theorem yields \(f(t)\le1+9t^2\le e^{16t^2}\). Chernoff's inequality, using \(t=\min\{s/32,1/4\}\) for the positive tail and the symmetric choice for the negative tail, gives
\[
\mathbb P(|u^\top S_mu|>s)
\le2\exp[-c' m\min\{s^2,s\}]
\]
for a universal \(c'>0\).

A maximal separated-set volume argument gives a \(1/4\)-net \(\mathcal N\) of the unit sphere with \(|\mathcal N|\le9^d\). For a symmetric matrix S, approximation of a unit vector maximizing \(|u^\top Su|\) gives
\[
\|S\|_{\rm op}\le2\max_{u\in\mathcal N}|u^\top Su|.
\]
The union bound therefore implies, after increasing a universal constant,
\[
\mathbb P\left\{\|S_m\|_{\rm op}>
C\left[\sqrt{\frac{d+t}{m}}+\frac{d+t}{m}\right]\right\}
\le2e^{-t},\qquad t\ge0.
\]
Integrating this tail proves (5). This calculation verifies the particular matrix-norm estimate used in the empirical-process bound, rather than invoking a specialized covariance result.

### 2.4 Uniform empirical bound on the cone

Set \(L_r=2\sqrt{2r}\) and
\[
\mathcal S_r=\{H=H^\top:\|H\|_F=1,\ \|H\|_*\le L_r\}.
\]
Define
\[
D=\sup_{H\in\mathcal S_r}\left|
\frac1m\sum_{i=1}^m\phi(z_i^\top Hz_i)
-\mathbb E\phi(z^\top Hz)\right|.
\]
The stated symmetrization and contraction inequalities, followed by nuclear/operator norm duality, give
\[
\begin{aligned}
\mathbb ED
&\le8\mathbb E\sup_{H\in\mathcal S_r}
\left|\left\langle H,\frac1m\sum_i\xi_i z_i z_i^\top\right\rangle\right|\\
&\le8L_r\mathbb E\|S_m\|_{\rm op}\\
&\le C'\sqrt r\left(\sqrt{\frac dm}+\frac dm\right).
\end{aligned}
\]
For \(m\ge c_*rd\), choosing the universal \(c_*\) sufficiently large makes the last expression at most \(p_0/4\): the two terms are bounded by universal multiples of \(c_*^{-1/2}\) and \(c_*^{-1}\), respectively.

Replacing one probe changes D by at most \(1/m\). Bounded differences with \(t=p_0/4\) gives
\[
\mathbb P(D>p_0/2)\le\exp(-mp_0^2/8).
\]
On the complementary event, (4) gives simultaneously for all \(H\in\mathcal S_r\)
\[
\frac1m\sum_i\phi(z_i^\top Hz_i)\ge p_0/2.
\]
Since \(\phi(s)\le2|s|\), the empirical absolute quadratic measurement average is at least \(p_0/4\). Homogeneity, with the zero matrix treated separately, proves (2) with \(\kappa=p_0/4\) and \(c=p_0^2/8\).

### 2.5 Stable recovery and the joint design event

Apply (2) to the error H from Step 1. Equations (1) and (2) give
\[
\|B-A\|_F\le4q/\kappa,
\qquad
\|B-A\|_*\le\frac{8\sqrt{2r}}\kappa q
\le K_d\bar\eta/\gamma^2,
\quad K_d:=\frac{8\sqrt{2d}}\kappa.
\]
Thus the previously unclosed recovery obligation is established. The design event is uniform over H in the cone, so it controls every admissible feedback realization and every trace minimizer, including those selected using the exploration history. No independence between the estimate and that history is required.

Also use
\[
E_{\rm energy}=\left\{\sum_{t=1}^m\|z_t\|^2\le4md\right\}.
\]
The sum is chi-squared with \(md\) degrees of freedom. Its exponential moment at \(1/4\) is \(2^{md/2}\), so
\[
\mathbb P(E_{\rm energy}^c)
\le\exp[-(1-\tfrac12\log2)md].
\]
Choose a universal positive integer \(c_1\ge c_*\), enlarged if necessary so that the sum of the two failure bounds is at most \(e^{-C_0m}\) for a universal \(C_0>0\), using \(m=c_1rd\ge c_1\). Denote the intersection event by E. Everything below holds on E. Set
\[
\varepsilon=K_d\bar\eta/\gamma^2.
\]
This is a deterministic error upper bound, not an additional hypothesis of the task.

## 3. Optimal comparator and quadratic identities

For a PSD matrix M define \(C_{T+1}(M)=I\),
\[
C_t(M)^{-1}=2I+M-C_{t+1}(M),\qquad H_t(M)=I-C_t(M).
\]
Backward induction gives \(0\prec C_t(M)\preceq I\), and also \(C_t(M)\preceq(I+M)^{-1}\). These matrices are functions of M and commute with M and with one another.

For the true matrix A, completion of the square gives, for any action x and previous state u,
\[
\begin{aligned}
&\tfrac12\|x-v\|_A^2+\tfrac12\|x-u\|^2
 +\tfrac12\|x-v\|_{H_{t+1}(A)}^2\\
&=\tfrac12\|u-v\|_{H_t(A)}^2
 +\tfrac12\|x-[C_t(A)u+(I-C_t(A))v]\|_{C_t(A)^{-1}}^2.
\end{aligned}
\]
Here \(\|q\|_D^2=q^\top Dq\); if D is indefinite this notation denotes a quadratic form, not a norm.

Taking expectations and telescoping uses martingale orthogonality. Starting at \(x_0=v_0\), every finite-cost causal policy has expected cost
\[
\frac12\sum_{t=1}^T\mathbb E[\delta_t^\top H_t(A)\delta_t]
+\frac12\sum_{t=1}^T\mathbb E\|x_t-[C_t(A)x_{t-1}+(I-C_t(A))v_t]\|_{C_t(A)^{-1}}^2.
\]
Finite cost makes the requisite tracking errors square-integrable: the increments of x have finite second moments, and \(x_t-v_t\) is their finite sum minus the finite sum of the \(\delta_j\). Thus the cross-term calculations are justified even though only integrability of \(v_0\) was assumed.

The true-matrix interpolation policy makes the second sum zero and has finite cost. It therefore attains the comparator infimum. This directly closes the optimal-policy obligation, including history-dependent increment variances and independently randomized causal policies.

For an estimated matrix B fixed at the beginning of a suffix, the corresponding quadratic identity for its interpolation policy contains the additional stage term
\[
\tfrac12\|x_{t-1}-v_t\|_{C_t(B)(A-B)C_t(B)}^2.
\]
For a suffix beginning after round m with tracking error h, its expected cost is
\[
\begin{aligned}
&\tfrac12\mathbb E[h^\top(I-C_{m+1}(B))h]
+\tfrac12\sum_{s=m+1}^T\mathbb E[\delta_s^\top(I-C_s(B))\delta_s]\\
&\quad+\tfrac12\sum_{s=m+1}^T\mathbb E\|x_{s-1}-v_s\|_{C_s(B)(A-B)C_s(B)}^2.
\end{aligned}
\]
For the learned B, condition first on the exploration history and then average. The estimate and its coefficient sequence are fixed under that conditioning. The initial quadratic is retained.

## 4. Exploration, replay, and the actual transition

Set \(z_0=0\). Conditional on Z, independence and \(\mathbb E\delta_t=0\) give exploration cost
\[
\frac12\sum_{t=1}^m\mathbb E\|\delta_t\|^2
+\frac{\gamma^2}{2}\sum_{t=1}^m z_t^\top A z_t
+\frac{\gamma^2}{2}\sum_{t=1}^m\|z_t-z_{t-1}\|^2.
\]
On \(E_{\rm energy}\) this is at most \(K(1+\gamma^2)\), where K depends only on the allowed fixed parameters. Here and below K may increase from line to line. Since \(m=c_1rd\) and \(r\le d\), its dependence on the fixed exploration length is permitted.

Let \(w_0=v_0\), and replay the B-policy through round m. Contraction gives the pathwise bound
\[
\|w_m-v_m\|\le\sum_{j=1}^m\|\delta_j\|,
\qquad
\mathbb E\|w_m-v_m\|^2\le m^2\operatorname{tr}\Sigma.
\]
This holds even though B depends on the exploration history. Continue the replay policy through the suffix; the public algorithm uses exactly these suffix actions. Its first suffix switching cost is, however, measured from the actual \(x_m=v_m+\gamma z_m\).

Put \(a=w_{m+1}-w_m\), \(b=w_m-x_m\). The switching-cost difference is
\[
a^\top b+\|b\|^2/2\le\|a\|^2/2+\|b\|^2,
\]
and
\[
\|a\|\le\|w_m-v_m\|+\|\delta_{m+1}\|,
\qquad
\|b\|\le\|w_m-v_m\|+\gamma\|z_m\|.
\]
Its expected upper bound is therefore \(K(1+\gamma^2)\) on E. The suffix initial quadratic is at most \(m^2\operatorname{tr}\Sigma/2\). The early part of the comparator cost is nonnegative and may be dropped in an upper bound.

Thus total regret is bounded by \(K(1+\gamma^2)\), the suffix coefficient-difference term, and the suffix propagated matrix-error term. For singular A the whole-space bound is \(C_t(A)\preceq I\), not \(I/(1+\sigma_+)\).

## 5. Coefficient-difference term

Let \(c_t(a)\) denote the scalar recursion with terminal value 1. Backward induction and reversal of Loewner order under inversion give
\[
M\preceq N\quad\Longrightarrow\quad C_t(M)\succeq C_t(N).
\]
Since \(B\preceq A+\varepsilon I\),
\[
C_t(A)-C_t(B)\preceq C_t(A)-C_t(A+\varepsilon I).
\]
For \(a>0\), the scalar inverse identity gives
\[
0\le c_t(a)-c_t(a+\varepsilon)
\le(1+a)^{-1}[c_{t+1}(a)-c_{t+1}(a+\varepsilon)+\varepsilon]
\le\varepsilon/a.
\]
The last inequality follows by backward iteration from a zero terminal difference.

For \(a=0\), \(c_t(0)=1\). The nonnegative fixed point
\[
\ell(b)=\frac{b+2-\sqrt{b^2+4b}}2
\]
is a lower bound on \(c_t(b)\), by backward induction from the terminal value 1. Moreover
\[
1-\ell(b)=\frac{\sqrt{b^2+4b}-b}{2}\le\sqrt b.
\]
Consequently the coefficient-difference contribution is at most
\[
K(\varepsilon+\sqrt\varepsilon)n\operatorname{tr}\Sigma
\quad(r<d),
\qquad
K\varepsilon n\operatorname{tr}\Sigma\quad(r=d).
\]
These are pointwise upper bounds in B. After averaging over the exploration history, the unconditional second-moment bound suffices. No conditional covariance bound or invalid substitution into an indefinite quadratic form is needed.

## 6. Propagated matrix error

Assume temporarily \(\varepsilon\le\min\{1,\sigma_+/2\}\), and put \(\rho=(1+\sigma_+/2)^{-1}<1\).

### Singular case

Split the eigenspaces of B into its largest r eigenvalues and the remaining eigenvalues. Weyl's inequality and \(\|A-B\|_{\rm op}\le\varepsilon\) give high eigenvalues at least \(\sigma_+/2\) and low eigenvalues at most \(\varepsilon\). Products of k estimated coefficients have norm at most \(\rho^k\) on the high subspace and at most 1 on the low subspace.

Let \(\Pi\) project onto range(A). For a unit low eigenvector p of B with eigenvalue b,
\[
(A-bI)\Pi p=\Pi(A-B)p,
\qquad
\|\Pi p\|\le\frac{\varepsilon}{\sigma_+-\varepsilon}.
\]
Summing squared overlaps over an orthonormal low-subspace basis bounds the norm of the low-low compression of A by
\[
\frac{d\|A\|_{\rm op}\varepsilon^2}{(\sigma_+-\varepsilon)^2}.
\]
The low-low compression of \(A-B\) is bounded above by that of A, because B is PSD. Its high-high and cross blocks have norm at most \(\varepsilon\).

For a product G of k estimated coefficients, split a test vector into its high and low components. The high-high term is bounded by \(\varepsilon\rho^{2k}\) times the squared norm of the high component, the cross term by \(2\varepsilon\rho^k\) times the product of the two component norms, and the low-low term by a fixed multiple of \(\varepsilon^2\) times the squared norm of the low component. Hence
\[
G(A-B)G\preceq K(\varepsilon^2+\varepsilon\rho^k)I.\tag{6}
\]
This uses only the required subspace overlap, not a comparison of complete eigenbases.

Condition on the exploration history. Expand the suffix tracking error into its propagated initial error \(h=w_m-v_m\) and the future martingale increments. The matrices in this expansion are fixed under that conditioning, and all cross terms have zero conditional expectation. Apply (6) to each diagonal term, then average over the history. Summing geometric series and counting the nondecaying terms gives
\[
K\operatorname{tr}\Sigma(\varepsilon^2n^2+\varepsilon n)
+K\mathbb E\|h\|^2(\varepsilon^2n+\varepsilon).
\]
The initial second moment is bounded in Step 4. Combining with Step 5 and using \(\varepsilon\le1\),
\[
\operatorname{Regret}_T(Z)
\le K[1+\gamma^2+\varepsilon^2n^2+\sqrt\varepsilon n+\varepsilon n]
\quad(r<d).\tag{7}
\]

### Full-rank case

All estimated coefficient products contract, and directly
\[
\|G(A-B)G\|_{\rm op}\le\varepsilon\rho^{2k}.
\]
The same martingale expansion and geometric summation give
\[
K\varepsilon\big(n\operatorname{tr}\Sigma+\mathbb E\|h\|^2\big)
\]
for the propagated-error contribution. Therefore
\[
\operatorname{Regret}_T(Z)\le K[1+\gamma^2+\varepsilon n]
\quad(r=d).\tag{8}
\]

## 7. Balancing and bounded remaining horizons

With p equal to \(2/3\) or \(1/2\) as appropriate,
\[
\gamma^2=\sqrt{\bar\eta}\max\{n^p,2/\sigma_+\},
\qquad
\varepsilon\le K_d\sqrt{\bar\eta}\,n^{-p}.
\]
The factor \(\sqrt{\bar\eta}\) is retained. There is a finite threshold N, depending only on the allowed fixed parameters, such that \(n\ge N\) ensures \(\varepsilon\le\min\{1,\sigma_+/2\}\).

For \(r<d\), substitution into (7) gives
\[
\gamma^2=O(n^{2/3}+1),\quad
\varepsilon^2n^2=O(n^{2/3}),\quad
\sqrt\varepsilon n=O(n^{2/3}),\quad
\varepsilon n=O(n^{1/3}).
\]
For \(r=d\), (8) gives \(\gamma^2=O(n^{1/2}+1)\) and \(\varepsilon n=O(n^{1/2})\).

For \(1\le n<N\), no perturbative estimate is required. Contraction of the replay and its continuation gives
\[
\|w_t-v_t\|\le\sum_{j=1}^t\|\delta_j\|,
\qquad
\mathbb E\Big(\sum_{j=1}^t\|\delta_j\|\Big)^2
\le t^2\operatorname{tr}\Sigma.
\]
Thus suffix hitting and switching costs are bounded by a fixed polynomial in the bounded horizon \(m+N\). Exploration and the actual transition are controlled by Step 4. The prescribed gamma is bounded in this range, and comparator cost is nonnegative. These finitely bounded remaining-horizon cases are absorbed into the additive constant, without changing gamma or restricting the public regime.

On E the claimed bounds follow with coefficient constants depending only on \(\bar\eta\), the positive spectrum of A, \(\Sigma\), and d. Step 2 gives \(\mathbb P_Z(E)\ge1-e^{-C_0m}\) with universal \(c_1,C_0\). Uniformity of the recovery event over error matrices, together with the pointwise and moment bounds in the remaining steps, gives the asserted uniformity over admissible processes, feedback rules, and measurable estimator selections. All theorem-critical obligations are closed.
