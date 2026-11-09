# Reference Proof

## Scope and standard background

All matrix norms below are spectral norms. Put
\[
S=\Gamma_\infty(A),\qquad g=\|S\|\ge1,\qquad a=1+\|B\|^2\bar u.
\]
The common policy kernels are used in every converse experiment. Their unconditional covariance sequences need not agree across experiments.

We use the following standard independent quadratic-form inequality, not a specialized system-identification theorem. If the coordinates of \(\xi\) are independent and centered, with \(\|\xi_j\|_{\psi_2}\le K\), and \(D\) is a deterministic symmetric matrix, then
\[
\Pr\{|\xi^TD\xi-\mathbb E\xi^TD\xi|>z\}
\le2\exp\left[-c\min\left\{\frac{z^2}{K^4\|D\|_F^2},\frac{z}{K^2\|D\|}\right\}\right].
\]
This is the standard independent-coordinate Hanson–Wright inequality. Every application below explicitly identifies the independent coordinates, deterministic matrix, and its norms. We also use the elementary facts that a Euclidean unit sphere has a \(1/4\)-net of size at most \(9^d\), that such a net controls a symmetric quadratic-form norm within a factor two, and that two such nets control a rectangular bilinear-form norm within a universal factor. These follow from the usual disjoint-ball volume argument and approximation of unit vectors. Data processing, joint convexity of relative entropy, and the variational characterization of symmetric eigenvalues are used in their ordinary finite-dimensional forms.

## 1. Covariances, likelihoods, and the stationary objective

Fresh Gaussian noise and conditional centering give, in each parameter experiment,
\[
\Sigma_{s+1}=A\Sigma_sA^T+BU_sB^T+I,\qquad \Sigma_0=0.
\]
Indeed, \(\mathbb E[x_su_s^T]=\mathbb E[x_s\mathbb E[u_s^T\mid\mathcal F_s]]=0\), and the current noise is independent of the history and current input. Consequently
\[
G_t(A):=\sum_{s=1}^{t-1}\Sigma_s
=\sum_{s=1}^{t-1}\left[\Gamma_s(A)+\Xi_s(A,\{U_k\})\right]
\succeq(t-1)I.
\]

Factor the joint trajectory density into policy kernels and Gaussian transition densities. The policy factors cancel because the same kernels are used in both experiments. Thus
\[
D(P_A^t\|P_{A'}^t)
=\frac12\operatorname{tr}\left((A-A')^T(A-A')G_t(A)\right).
\]
The omitted \(s=0\) contribution is zero because \(x_0=0\). This identity also holds with the parameters reversed, in which case the information matrix is \(G_t(A')\).

For completeness, the elementary two-point argument uses perturbations of norm strictly greater than \(2\varepsilon\), so that the closed success balls are disjoint. Data processing gives the binary-testing lower bound; letting the perturbation norm decrease to \(2\varepsilon\) gives the source's bound involving \(\log(1/(3\delta))\). The dimension-sensitive proof below does not rely on that bound being positive near \(\delta=1/2\).

The feasible covariance set is compact. Its stationary Gramian is continuous in \(U\), so an optimizer exists. For stable \(A\), the convergent series \(P_U=\sum_{k\ge0}A^k(I+BUB^T)(A^k)^T\) satisfies the Lyapunov equation. Uniqueness follows by iterating the homogeneous equation for a difference and using \(A^k\to0\). This proves the stated SDP characterization. Also
\[
I\preceq P_U\preceq aS,\qquad 1\le J_A^*\le ag.
\]

## 2. Perturbation bound, including the boundary case

Here the two systems are compared using the same deterministic sequence of feasible input covariances. Let \(T=A+\Delta\), \(d=\|\Delta\|\le g^{-3/2}/4\). Since
\[
ASA^T=S-I,\qquad \|A\|\le\sqrt{g-1},
\]
put
\[
e=2dg\sqrt{g-1}+d^2g\le\frac9{16}.
\]
Expanding \(TST^T\) gives
\[
TST^T\preceq S-(1-e)I.
\]
Conjugation by \(S^{-1/2}\) shows that \(T\) is stable. Summing the last inequality after conjugating by powers of \(T\) gives
\[
\Gamma_\infty(T)\preceq\frac{S}{1-e}.
\]

Let \(P_s\) be the unperturbed finite covariance, with driving covariance \(Q_s=I+BU_sB^T\preceq aI\). Then \(0\preceq P_s\preceq aS\). If \(\widetilde P_s\) uses \(T\) and the same \(Q_s\), the difference satisfies
\[
\widetilde P_{s+1}-P_{s+1}
=T(\widetilde P_s-P_s)T^T+R_s,
\quad
R_s=\Delta P_sA^T+AP_s\Delta^T+\Delta P_s\Delta^T.
\]
The norm bound on \(P_s\) gives \(-aeI\preceq R_s\preceq aeI\). Iterating therefore yields
\[
\|\widetilde P_s-P_s\|
\le ae\|\Gamma_s(T)\|
\le\frac{aeg}{1-e}
\le\frac{36}{7}adg^{5/2}
\le32adg^3.
\]
This proves the required uniform perturbation bound and stability, without the problematic intermediate factorization in the source. It also covers \(g=1\); in that case \(S=I\) implies \(A=0\).

The matrix-power result cited in the source has also been recovered. If \(\rho>0\) and \(\tau=\sup_{k\ge0}\|A^k\|\rho^{-k}<\infty\), let \(b=\rho+\tau\|\Delta\|\). The telescoping identity
\[
T^k=A^k+\sum_{j=0}^{k-1}A^{k-1-j}\Delta T^j
\]
and induction imply \(\|T^k\|\le\tau b^k\). Substitution into the same identity gives \(\|T^k-A^k\|\le k\tau^2\|\Delta\|b^{k-1}\). Thus this dependency is closed, although the direct Lyapunov estimate above is more convenient at the boundary.

## 3. Dimension-sensitive converse

Fix \(t=\tau_A\), and let \(u\) be a unit eigenvector for \(\lambda=\lambda_{\min}(G_t(A))\). First construct an all-dimensions packing. For \(d=n_x\), a greedy binary code in \(\{-1,1\}^d\) with Hamming distance greater than \(d/8\) has cardinality
\[
N\ge\frac{2^d}{\sum_{j=0}^{\lfloor d/8\rfloor}\binom dj}
\ge\exp(c_0d),\qquad c_0=\log2-H(1/8)>0,
\]
where \(H(p)=-p\log p-(1-p)\log(1-p)\). The binomial bound follows by comparing the lower binomial tail to the expansion of \((p+(1-p))^d\) at \(p=1/8\). Normalize these sign vectors to obtain unit vectors \(v_i\). Their distances exceed \(1/\sqrt2\). In particular, \(N\ge2\) even when \(d=1\).

Set
\[
r=3\sqrt2\varepsilon,\qquad A_i=A+r v_i u^T.
\]
Each perturbation has spectral and Frobenius norm \(r\); pairwise distances exceed \(3\varepsilon\), and
\[
\operatorname{tr}((A_i-A)^T(A_i-A)G_t(A))=r^2\lambda.
\]
The alternatives belong to the local ball. The small-accuracy hypothesis gives \(rg^3<1/4\), hence \(r\le g^{-3/2}/4\); the perturbation result also makes all these alternatives stable.

Let \(E_i=\{\|\widehat A_t-A_i\|\le\varepsilon\}\). These events are pairwise disjoint and their union is disjoint from success at \(A\). Therefore
\[
p:=N^{-1}\sum_iP_{A_i}(E_i)\ge1-\delta,
\qquad q:=P_A(\cup_iE_i)/N\le\delta/N.
\]
For each \(i\), data processing gives \(D(P_{A_i}\|P_A)\ge\mathrm{kl}(P_{A_i}(E_i),P_A(E_i))\). Averaging and using joint convexity proves directly
\[
N^{-1}\sum_iD(P_{A_i}\|P_A)\ge\mathrm{kl}(p,q).
\]
Thus the specialized inherited testing proposition is not being assumed.

Since \(p>1/2\) and \(q<1/4\), monotonicity gives
\[
\mathrm{kl}(p,q)\ge\mathrm{kl}(1/2,q)
=\frac12\log\frac1{4q(1-q)}
\ge\frac1{32}\log\frac1q
\ge\frac1{32}[\log N+\log(1/\delta)].
\]
For example, the penultimate inequality follows by considering \(q\le1/16\) and \(1/16\le q\le1/4\) separately. This corrects the unjustified coefficient-one bound in the source and is uniform as \(\delta\uparrow1/2\).

It remains essential not to equate adaptive input covariances across parameter experiments. Under alternative \(A_i\), the power constraint instead gives directly
\[
G_t(A_i)\preceq a\sum_{s=1}^{t-1}\Gamma_s(A_i).
\]
Apply the perturbation bound with zero excitation, and use \(\sum_s\Gamma_s(A)\preceq G_t(A)\). Then
\[
u^TG_t(A_i)u
\le a[\lambda+32rg^3(t-1)]
\le9a\lambda,
\]
where \(G_t(A)\succeq(t-1)I\) and \(rg^3<1/4\) were used. The reversed Gaussian KL identity now gives
\[
D(P_{A_i}^t\|P_A^t)
=\tfrac12r^2u^TG_t(A_i)u
\le81a\varepsilon^2\lambda.
\]
Combining the last bounds proves
\[
\lambda_{\min}(G_{\tau_A}(A))
\ge\frac{c[n_x+\log(1/\delta)]}{a\varepsilon^2}
\]
for a universal \(c>0\). If \(t\le1\), the KL identity would make all these trajectory laws indistinguishable, contradicting the positive testing lower bound, so division by \(t-1\) below is legitimate.

For the stationary reduction, set \(\overline U=(t-1)^{-1}\sum_{s=0}^{t-2}U_s\), which is feasible. Reordering the finite covariance sums and extending positive semidefinite summands to infinite time gives
\[
G_t(A)\preceq(t-1)\Gamma_\infty(A)+\sum_{s=0}^{t-2}\Xi_\infty(A,U_s)
=(t-1)[\Gamma_\infty(A)+\Xi_\infty(A,\overline U)].
\]
Hence \(\lambda_{\min}(G_t(A))\le(t-1)J_A^*\). This is an aggregate, averaged-covariance argument, not a claim that one fixed optimizer dominates every instantaneous covariance in Loewner order. The stated converse follows.

## 4. Fixed-covariance least squares

Consider a zero-start phase of length \(h\ge2\) with fixed covariance \(U\). Write
\[
X=[x_1,\ldots,x_{h-1}]^T,\quad W=[w_1,\ldots,w_{h-1}]^T,
\quad H=\mathbb E[X^TX]=\sum_{s=1}^{h-1}[\Gamma_s(A)+\Xi_s(A,U)],\quad M=H^{-1/2}.
\]
Let \(L=\|\Gamma_{U,h}\|\). The fresh phase inputs and noises make the stacked vector \(\xi=(\eta_0^T,\ldots,\eta_{h-2}^T)^T\) have independent centered coordinates, variance one, and coordinate \(\psi_2\)-norm at most \(K\). Moreover \(\operatorname{vec}(X^T)=\Gamma_{U,h}\xi\).

For every unit vector \(v\), write \(XMv=T_v\xi\). Then
\[
\|T_v\|_F^2=\mathbb E\|XMv\|^2=1,
\qquad \|T_v\|^2\le\|M\|^2L^2=:R.
\]
Thus \(D_v=T_v^TT_v\) has \(\|D_v\|\le R\) and \(\|D_v\|_F^2\le R\). Applying the stated quadratic-form inequality on a \(1/4\)-net proves
\[
\Pr\{\|MX^TXM-I\|>1/2\}\le q/2
\]
provided
\[
\lambda_{\min}(H)\ge C K^4L^2[n_x+\log(1/q)].
\]
All independence conditions also hold conditionally in the second phase, because its entire input law is fixed by the first-phase history and uses fresh randomness.

We must also control the score, not merely the design. For deterministic unit vectors \(b,c\), let
\[
Z_{b,c}=\sum_{s=1}^{h-1}(b^Tw_s)(x_s^TMc),\qquad
V_c=\sum_{s=1}^{h-1}(x_s^TMc)^2.
\]
The coefficients \(x_s^TMc\) are predictable, and \(b^Tw_s\) is conditionally standard Gaussian. Iterated conditional Gaussian moment generating functions imply
\(\mathbb E\exp(\theta Z_{b,c}-\theta^2V_c/2)=1\).
Consequently
\[
\Pr\{|Z_{b,c}|>z,\ V_c\le3/2\}\le2e^{-z^2/3}.
\]
On the design event, \(V_c\le3/2\) for every unit \(c\). Two finite nets and a union bound therefore give
\[
\|W^TXM\|\le C_0\sqrt{n_x+\log(1/q)}
\]
except on an additional event of probability at most \(q/2\).

On the design event, \(X^TX\) is invertible. The LSE error identity is therefore valid in the form
\[
\widehat A-A=W^TX(X^TX)^{-1}
=W^TXM\,(MX^TXM)^{-1}M,
\]
which yields
\[
\|\widehat A-A\|\le\frac{2C_0\sqrt{n_x+\log(1/q)}}{\sqrt{\lambda_{\min}(H)}}.
\]
Away from this event, the general minimum-norm pseudoinverse formula includes the bias term \(-A(I-X^TX(X^TX)^\dagger)\); no false full-rank identity is used there.

A variance-one random variable has a \(\psi_2\)-norm bounded below by a universal positive constant. Thus one sufficiently large universal \(c'\) makes \(C=c'K^4\) cover both the design and score bounds. We have proved exactly the fixed-covariance requirement in the task.

Finally, the convolution triangle inequality gives
\[
L\le\sum_{k=0}^{h-2}\|A^kQ_U^{1/2}\|
\le\sqrt a\sum_{k\ge0}\|A^k\|,
\]
so \(L^2\le\bar\gamma\).

## 5. Objective sensitivity

For a feasible fixed \(U\), pass to the limit in the perturbation bound and use the eigenvalue variational principle to obtain
\[
|J_A(U)-J_{A+\Delta}(U)|\le32a\|\Delta\|g^3.
\]
Insert and subtract the objectives at \(A+\Delta\), evaluated at its optimizer and at an optimizer for \(A\). The middle difference is nonpositive by optimality. Hence
\[
J_A^*-J_A(U^*(A+\Delta))\le64a\|\Delta\|g^3.
\]
This needs neither uniqueness nor continuity of the optimizer selection.

## 6. Initialization, reset, and exact horizon terms

The initialization assumption implies that its requirement set is nonempty. The fixed-covariance bound with \(U_0=(\bar u/n_u)I\), \(h=t_0\), and \(q=\delta/2\) gives an event \(E_0\) of probability at least \(1-\delta/2\) on which
\[
\|\widehat A^{(1)}_{t_0}-A\|\le\varepsilon_{t_0}\le g^{-3/2}/4.
\]
By the perturbation stability result the raw preliminary estimate is already stable on \(E_0\). Thus the projection is not applied there, and
\[
J_A^*-J_A(\widehat U)\le64ag^3\varepsilon_{t_0}.
\]
No nonexpansiveness of the projection is asserted or required.

Put \(\gamma=1-1/g\in[0,1)\). From \(ASA^T=S-I\), conjugation by \(S^{-1/2}\) gives
\[
\|A^k\|\le\sqrt g\,\gamma^{k/2}\quad(k\ge0),
\]
with the \(k=0\) factor interpreted as one and with \(A=0\) when \(g=1\).

For a feasible \(U\), define \(H_s(U)=\Gamma_s(A)+\Xi_s(A,U)\), \(P_U=H_\infty(U)\), and \(b=t-1\). There are three finite-horizon losses:
\[
\|P_U-H_b(U)\|\le ag^2\gamma^b,
\]
\[
\left\|bH_b(U)-\sum_{s=1}^{b}H_s(U)\right\|
\le a\sum_{k\ge0}k\|A^k\|^2
\le ag^2(g-1),
\]
\[
\left\|\sum_{s=b-t_0+1}^{b}H_s(U)\right\|\le ag^2t_0.
\]
The first two estimates follow by summing geometric series; the last follows from \(\|H_s(U)\|\le ag\le ag^2\). For \(g=1\), the first two losses are zero directly.

Any horizon satisfying the theorem's inequality necessarily has \(t\ge t_0+2\): otherwise \((t-1)J_A^*\le t_0ag\le t_0ag^2\), already no larger than the initialization-removal term, whereas the concentration term is strictly positive. Thus the post-reset design sum has at least one term.

Combining the three losses with objective sensitivity, on \(E_0\), gives
\[
\begin{aligned}
&(t-1)J_A^*-\lambda_{\min}\left(\sum_{s=1}^{t-t_0-1}H_s(\widehat U)\right)\\
&\quad\le g^2\left[64ag(t-1)\varepsilon_{t_0}+at_0+a(t-1)\gamma^{t-1}+a(g-1)\right].
\end{aligned}
\]
This is precisely the correction in the public inequality, since \(C_1=64ag\) and \(C_2=a\).

Therefore that inequality implies, for each first-phase history in \(E_0\),
\[
\lambda_{\min}\left(\sum_{s=1}^{t-t_0-1}H_s(\widehat U)\right)
\ge C\max\{\varepsilon^{-2},\bar\gamma\}[\log(2/\delta)+n_x].
\]
After conditioning on that complete history, \(\widehat U\) is fixed, the state is reset to zero, and all hypotheses of the fixed-covariance bound hold. Its failure probability is at most \(\delta/2\), uniformly over those histories. Integration and addition of \(P(E_0^c)\) give total failure probability at most \(\delta\).

During initialization, \(\mathbb E\|u_t\|^2=\operatorname{tr}(U_0)=\bar u\). Afterwards,
\[
\mathbb E\|u_t\|^2=\mathbb E\operatorname{tr}(\widehat U)\le\bar u.
\]
This also covers \(\bar u=0\) and singular optimized covariances. With a zero budget the density-requiring converse policy class is empty, so its universal assertion is vacuous; the upper-bound experiment remains well-defined.

All theorem-critical obligations are closed. The sufficient horizon inequality remains implicit; the proof does not claim it is satisfiable for every initialization meeting only the stated perturbation-radius condition.
