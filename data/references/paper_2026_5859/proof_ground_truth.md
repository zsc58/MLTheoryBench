# Reference Proof

## Contract and obligations

All risks below average training noise conditional on the design. A filter is held fixed under that expectation, and comparator infima are taken afterward, pointwise in the design. The positive comparator comprises nonnegative ridge and ordinary gradient flow. The negative comparator comprises exactly the endpoints with \(0\leq\nu<\widehat\mu_{\min}^+\).

The proof must establish: (i) the simultaneous Gaussian localization event, including projected tail square mass; (ii) the exact conditional-risk decomposition; (iii) quantitative invariant-graph and localized-Duhamel bounds; (iv) the signed upper bound at the specified time; (v) the scalar-rescaling and both positive-class lower bounds; and (vi) the complete admissible-endpoint lower envelope and its optimization. All six obligations are derived below. Source support is theory_001–theory_004, theory_006, and theory_015–theory_021; the selected target is theory_009. No paper-specific lemma is used as an unproved black box.

Throughout, constants may depend on the fixed comparison bounds in the model, but not on n. Constants in Gaussian concentration and the tail-band width can be numerical. Write \(\lambda=\lambda_-\), \(w=w_k\), \(S=S_k\), \(\Theta=\Theta_H\), and \(\chi=\chi_{n,k}\) within this proof.

### Preliminary implications

The ordered spectrum gives \(S\leq\lambda_{k+1}T_k\leq\lambda_-na\), so \(V_{T,k}\) is bounded above. Since \(\Theta\) is bounded below, \(L\) is bounded below by a positive constant. Thus \(r_kL\to0\) implies \(r_k\to0\). Consequently \(\rho:=w/\lambda=O(r_k)\to0\), \(V_{T,k}\leq\sigma_\varepsilon^2\rho^2\to0\), and \(L\to\infty\). Also \(w^2\geq S/n\), so the restored assumption \(kw^2/S\to0\) implies \(k/n\to0\) and \(\chi\to0\). The exposure condition gives \(\rho L\to0\).

The tail dimension is eventually greater than n: if \(d=p-k\), then \(na=T_k\leq d\lambda_{k+1}\), hence \(d/n\geq a/\lambda_{k+1}\to\infty\). Thus the Gaussian tail Gram matrix, and hence the full sample Gram matrix, are positive definite almost surely for all sufficiently large n.

## 1. Conditional risk and scalar flow

Put \(F=\sum_i f_i\widehat v_i\widehat v_i^T\). The estimator decomposes as
\[
\widehat\beta_f=F\beta^*+\sum_i\frac{f_i}{n\widehat\mu_i}\widehat v_i\widehat v_i^TX^T\varepsilon.
\]
The noise coefficients have conditional mean zero and covariance
\[
\operatorname{Cov}\left(\frac{\widehat v_i^TX^T\varepsilon}{n\widehat\mu_i},\frac{\widehat v_j^TX^T\varepsilon}{n\widehat\mu_j}\mid X\right)
=\frac{\sigma_\varepsilon^2}{n\widehat\mu_i}\mathbf1\{i=j\}.
\]
Therefore
\[
R(f\mid X)=\|(F-I)\beta^*\|_\Sigma^2+
\frac{\sigma_\varepsilon^2}{n}\sum_i\frac{f_i^2}{\widehat\mu_i}\widehat v_i^T\Sigma\widehat v_i.
\]
This includes the null-space bias and uses only the stated conditional noise moments.

Solving the scalar shifted differential equation from zero gives
\[
f_{a,t}(\mu)=\mu\int_0^t e^{-(\mu-a)s}\,ds.
\]
At \(\mu=a\), its value is \(at\), so there is no singularity.

For later use, set
\[
K_H=X_HX_H^T/n,\quad K_T=X_TX_T^T/n,\quad K=K_H+K_T,\quad G_H=X_H^TX_H/n,
\]
\[
E_T=K_T-aI,\qquad K_{2,H}=X_H\Lambda_HX_H^T/n,\qquad K_{2,T}=X_T\Lambda_TX_T^T/n.
\]
For any real function h on the spectrum of K, the filter \(f(\mu)=\mu h(\mu)\) has estimator \(X^Th(K)y/n\). Splitting its conditional bias into population head and tail coordinates gives the exact identity
\[
\begin{aligned}
R(f\mid X)={}&\left\|\Lambda_H^{1/2}\left\{X_H^Th(K)X_H/n-I\right\}\beta_H^*\right\|^2\\
&+\frac1n(X_H\beta_H^*)^Th(K)K_{2,T}h(K)(X_H\beta_H^*)\\
&+\frac{\sigma_\varepsilon^2}{n}\operatorname{tr}\{(K_{2,H}+K_{2,T})h(K)^2\}.
\end{aligned}
\]

For completeness, the displacement identity indexed by theory_006 follows from the same calculation. Let \(P_i=\widehat v_i\widehat v_i^T\), \(P=\sum_iP_i\), \(P_0=I-P\), and \(\delta_i=f_i-1\). Define \(H_{ij}=\beta^{*T}P_i\Sigma P_j\beta^*\), \(m_i=\beta^{*T}P_i\Sigma P_0\beta^*\), \(v_i=\sigma_\varepsilon^2\widehat v_i^T\Sigma\widehat v_i/(n\widehat\mu_i)\), \(D=\operatorname{diag}(v_i)\), \(Q=H+D\), and \(g=m-v\). Expansion yields \(R(f)-R(1)=\delta^TQ\delta-2g^T\delta\). If \(z\in\ker Q\), positivity gives \(z^THz=z^TDz=0\). With \(u=\sum_i z_iP_i\beta^*\), this implies \(\|u\|_\Sigma=0\), hence \(z^Tm=0\), while \(Dz=0\) implies \(z^Tv=0\). Thus \(g\in\operatorname{range}(Q)\), and completing the square gives the oracle centered at \(Q^\dagger g\). A one-coordinate perturbation has derivative \(-2(m_i-v_i)\). This identity is auxiliary, not a substitute for the comparator estimates below.

## 2. Gaussian localization

The following elementary concentration argument is the source derivation of theory_015. For deterministic nonnegative weights \(\alpha_j\) and independent standard normal \(g_j\), put \(A_2=\sum_j\alpha_j^2\) and \(\alpha_{\max}=\max_j\alpha_j\). The Gaussian moment-generating function gives
\[
\log\mathbb E\exp\left(\theta\sum_j\alpha_j(g_j^2-1)\right)
=\sum_j\left[-\theta\alpha_j-\tfrac12\log(1-2\theta\alpha_j)\right].
\]
Using \(-x-\log(1-x)\leq x^2/[2(1-x)]\) for \(0\leq x<1\), Chernoff optimization gives upper threshold \(2\sqrt{A_2x}+2\alpha_{\max}x\) with failure probability \(e^{-x}\). The negative-parameter calculation gives lower threshold \(2\sqrt{A_2x}\) with the same failure probability. Thus the two-sided failure probability at the larger threshold is at most \(2e^{-x}\).

For a symmetric matrix M and a 1/4-net of the unit sphere, \(\|M\|\leq2\max_u|u^TMu|\). Such a net in dimension q has at most \(9^q\) points, by the usual disjoint-ball volume bound. Apply the scalar inequality to each quadratic form and take a union bound. For independent standard Gaussian vectors \(z_j\in\mathbb R^n\),
\[
W_\alpha=\frac1n\sum_j\alpha_j(z_jz_j^T-I)
\]
satisfies
\[
\|W_\alpha\|\leq C\left\{\frac{\sqrt{A_2(n+s)}}n+\frac{\alpha_{\max}(n+s)}n\right\}
\]
except with probability \(2e^{-s}\). If U is an independent orthonormal q-frame, conditioning on U makes \(U^Tz_j\) independent standard Gaussian q-vectors. The same bound for \(U^TW_\alpha U\) replaces n+s inside the braces by q+s, while retaining the normalization n.

Let \(P_H\) project onto \(\operatorname{range}(X_H)\). Apply these inequalities as follows:

- Tail weights \(\lambda_j\), dimension n, and \(s=n\) give \(\|E_T\|\leq Cw\).
- Conditional on the independent head frame, dimension k and \(s=3\log n\) give
\[
\|P_HE_TP_H\|\leq C\left\{\frac{\sqrt{S(k+\log n)}}n+\frac{\lambda_{k+1}(k+\log n)}n\right\}\leq Cw\chi.
\]
Also \(\|P_HE_TP_H^\perp\|\leq Cw\).
- Applying the scalar-net argument to \(Z_H^TZ_H/n\), with n unit weights and a k-dimensional net, gives
\[
\|\Lambda_H^{-1/2}G_H\Lambda_H^{-1/2}-I\|\leq C\chi.
\]
- Tail weights \(\lambda_j^2\) give
\[
\|K_{2,T}\|\leq C\left\{S/n+\lambda_{k+1}^2+\sqrt{\textstyle\sum_{j>k}\lambda_j^4/n}\right\}\leq Cw^2,
\]
since \(\sum\lambda_j^4\leq\lambda_{k+1}^2S\).

Moreover, \(\operatorname{tr}K_{2,T}\) has mean S and variance \(2\sum\lambda_j^4/n\leq2S^2/n\). Chebyshev with relative tolerance \(n^{-1/4}\) therefore gives \(\operatorname{tr}K_{2,T}=(1+o(1))S\) on an event of probability tending to one.

We use the standard independent rank-k interlacing fact: if B is symmetric and C is positive semidefinite of rank at most k, adding C moves no eigenvalue downward and moves at most k eigenvalues above an interval containing the entire spectrum of B. Its hypotheses hold for \(B=K_T\) and \(C=K_H\). Consequently at least n-k eigenvalues of K lie in \([a-Cw,a+Cw]\), and none lies below this interval. If \(P_B\) is the spectral projector onto this band, then
\[
\operatorname{tr}(P_BK_{2,T})\geq\operatorname{tr}K_{2,T}-k\|K_{2,T}\|\geq cS,
\]
because \(kw^2=o(S)\). This is precisely where the restored source assumption is used.

Intersecting the preceding events gives a single event \(\mathcal E_n\) of probability tending to one. On it, all displayed estimates hold, \(\|K\|\leq C\lambda_+\), \(\|K_{2,H}\|\leq C\lambda_+^2\), and \(\operatorname{tr}K_{2,H}\asymp k\lambda_-^2\). The latter statements follow from \(K_{2,H}=X_H\Lambda_HX_H^T/n\), the head Gram bound, and the bounded head condition number. No Marchenko-Pastur lower-edge theorem is needed for this general-tail chain.

## 3. Quantitative invariant-graph estimate

Here is the source construction underlying theory_017. Let
\[
A_0=\begin{pmatrix}H&0\\0&0\end{pmatrix},\qquad
A=A_0+E=\begin{pmatrix}H_1&B\\B^T&C_T\end{pmatrix},
\]
where \(\operatorname{spec}(H)\subset[g,G]\), \(G/g\leq\kappa\), \(\delta=\|E\|\leq c_\kappa g\), \(H_1=H+E_{HH}\), and \(b=\|B\|\). Take \(c_\kappa\) small enough that \(H_1\succeq3gI/4\), \(\lambda_{\max}(C_T)\leq g/4\), and the gap \(\Delta\geq g/2\).

The Sylvester map \(\mathcal S(Z)=ZH_1-C_TZ\) has inverse
\[
\mathcal S^{-1}(Y)=\int_0^\infty e^{sC_T}Ye^{-sH_1}\,ds,
\qquad \|\mathcal S^{-1}\|\leq\Delta^{-1}.
\]
Convergence follows from the gap, and differentiating the integrand verifies the inverse. The graph of Z is invariant exactly when
\[
\mathcal S(Z)=B^T-ZBZ.
\]
On \(\|Z\|\leq2b/\Delta\), the map \(\Phi(Z)=\mathcal S^{-1}(B^T-ZBZ)\) maps the ball into itself and has Lipschitz constant at most \(4b^2/\Delta^2<1\). The contraction theorem therefore constructs Z with \(\|Z\|\leq Cb/g\). If b=0, use Z=0 directly.

Set \(C_Z=(I+Z^TZ)^{-1/2}\), \(D_Z=(I+ZZ^T)^{-1/2}\), and
\[
Q=\begin{pmatrix}C_Z&-Z^TD_Z\\ZC_Z&D_Z\end{pmatrix}.
\]
The identities \(D_ZZ=ZC_Z\) and \(C_ZZ^T=Z^TD_Z\), obtained by singular-value decomposition, show that Q is orthogonal. Invariance and self-adjointness give
\[
Q^TAQ=\operatorname{diag}(\widetilde H,\widetilde C_T).
\]
In particular,
\[
\widetilde H=C_Z(H_1+BZ+Z^TB^T+Z^TC_TZ)C_Z,
\]
\[
\widetilde C_T=D_Z(C_T-ZB-B^TZ^T+ZH_1Z^T)D_Z.
\]
Since \(\|C_Z-I\|+\|D_Z-I\|\leq C\|Z\|^2\), these formulas imply
\[
\|\widetilde H-H_1\|+\|\widetilde C_T-C_T\|\leq C_\kappa b^2/g,
\quad \widetilde H\succeq gI/2,
\quad \widetilde C_T\succeq-C_\kappa\delta I.
\]

Write \(h_t(A)=\int_0^t e^{-sA}\,ds\). The exact head compression is
\[
Ph_t(A)P=C_Zh_t(\widetilde H)C_Z+Z^TD_Zh_t(\widetilde C_T)D_ZZ.
\]
For positive matrices with eigenvalues at least g/2, differentiating a product of exponentials gives the Duhamel identity and the estimate
\[
\|e^{-sU}-e^{-sV}\|\leq s e^{-gs/2}\|U-V\|.
\]
Integration bounds the difference of their h-functions by \(4\|U-V\|/g^2\). Apply this to \((\widetilde H,H_1)\) and \((H_1,H)\). The rotation error is \(O(b^2/g^3)\), while the lower-block term is at most \(C b^2t e^{C_\kappa\delta t}/g^2\). Thus, with \(\epsilon_H=\|E_{HH}\|\),
\[
\|P\{h_t(A)-h_t(A_0)\}P\|
\leq C_\kappa\left\{\frac{\epsilon_H}{g^2}+\frac{b^2}{g^3}(1+gt e^{C_\kappa\delta t})\right\}.
\]
Finally \(Q^TP|_{\operatorname{range}(P)}=(C_Z,-D_ZZ)^T\), so
\[
\|h_t(A)P\|\leq\frac{C_\kappa}{g}\{1+bt e^{C_\kappa\delta t}\}.
\]
This supplies both the quadratic leave-and-return bound and the noncontractive exposure estimate, without importing a specialized perturbation theorem.

## 4. Signed-flow upper bound

On \(\mathcal E_n\), apply the preceding result with \(A_0=K_H\), \(E=E_T\), and \(P=P_H\). The nonzero spectrum of \(K_H\) equals that of \(G_H\), so \(g\geq\lambda_-(1-C\chi)\), \(G/g\) is bounded, \(\delta\leq Cw=o(g)\), \(\epsilon_H\leq Cw\chi\), and \(b\leq Cw\). At any deterministic time with \(wt=o(1)\), all hypotheses are satisfied.

Let \(h=h_{a,t}(K)=\int_0^t e^{-s(K-aI)}ds\). Intertwining the powers, or using singular-value decomposition of \(X_H\), gives
\[
X_H^Th_{a,t}(K_H+aI)X_H/n=I-e^{-tG_H}.
\]
Multiplying the compression estimate by \(X_H/\sqrt n\) on both sides yields head-map error at most
\[
\delta_H(t)\leq C\left\{\rho\chi+\rho^2(1+\lambda_-t e^{Cwt})\right\}.
\]
Norm equivalence under the bounded condition number then bounds head bias by
\[
C\Theta\{e^{-2(1-C\chi)\lambda_-t}+\delta_H(t)^2\}.
\]
The exposure estimate gives \(\|hP_H\|\leq C/\lambda_-\). Consequently the tail-signal term in the exact decomposition is at most \(C\Theta w^2/\lambda_-^2\). Since \(K_{2,H}\) is supported on the head sample subspace and has trace at most \(Ck\lambda_+^2\), head variance is at most \(C\sigma_\varepsilon^2 k/n\).

The smallest eigenvalue of \(K-aI\) is at least \(-Cw\), so \(\|h\|\leq t e^{Cwt}\). Hence tail variance is at most
\[
C\frac{\sigma_\varepsilon^2S}{n}t^2e^{Cwt},
\]
where C absorbs the harmless factor from squaring the exponential. Combining these estimates proves the full intermediate bound of theory_018.

Now set \(t=L/\lambda_-\). We have \(wt=\rho L=o(1)\) and
\[
\Theta e^{-2L}=\frac{\Theta V_{T,k}}{\Theta+V_{T,k}}\leq V_{T,k}.
\]
Since \(L\chi\to0\), the empirical head residual is at most \((1+o(1))V_{T,k}\), up to the fixed norm-equivalence constant. Moreover,
\[
\delta_H(t)\leq C\{\rho\chi+\rho^2(1+L)\},\qquad
\delta_H(t)^2\leq C\rho^2\{\chi^2+\rho^2(1+L^2)\}=o(\rho^2).
\]
Tail variance is at most \(C V_{T,k}L^2\). This proves
\[
R_{sign}(a,t_{fc})\lesssim\frac{\sigma_\varepsilon^2k}{n}+V_{T,k}(1+L^2)+\Theta_H\frac{w_k^2}{\lambda_-^2}.
\]

## 5. Scalar rescaling and positive comparators

The matrix inversion identity gives
\[
M_{rid}=X_H^TK^{-1}X_H/n=C(I+C)^{-1},\qquad C=X_H^TK_T^{-1}X_H/n.
\]
This identity follows by multiplying the Woodbury formula for \((K_T+X_HX_H^T/n)^{-1}\); both \(K_T\) and \(I+C\) are positive definite. On \(\mathcal E_n\), the resolvent identity gives
\[
\|K_T^{-1}-a^{-1}I\|\leq Cw/a^2,
\quad C=\Lambda_H/a+O(\rho+\chi)
\]
in operator norm. Since \(C(I+C)^{-1}=I-(I+C)^{-1}\), another resolvent identity yields
\[
M_{rid}=Q_0+O(\rho+\chi),\qquad Q_0=\operatorname{diag}(q_j).
\]
All q_j are bounded away from zero and one by fixed constants.

For bounded c, head bias therefore equals
\[
\|\Lambda_H^{1/2}(cM_{rid}-I)\beta_H^*\|^2
=\sum_j\Theta_j(1-cq_j)^2+O(\rho+\chi)\Theta,
\]
uniformly over that bounded interval. To justify the infimum over all real c, note that
\(\|\Lambda_H^{1/2}M_{rid}\beta_H^*\|\geq c_1\sqrt\Theta\)
for a fixed \(c_1>0\). The reverse triangle inequality gives head bias at least \((|c|c_1-1)^2\Theta\) whenever \(|c|c_1\geq1\). Outside a sufficiently large fixed interval this exceeds \(\Theta\), whereas \(\Delta_{shape}\leq\Theta\) by choosing c=0. Nonnegative tail bias and variance can be discarded, proving
\[
R_{scale}^*\geq\Delta_{shape}-o(1)\Theta_H.
\]

For nonnegative ridge, \(h_+(x)=1/(x+\alpha)\), \(\alpha\geq0\); for ordinary gradient flow, \(h_+(x)=(1-e^{-tx})/x\), \(t\geq0\). Both satisfy \(0\leq h_+(x)\leq1/x\) for x>0. Functional calculus and congruence yield
\[
0\preceq M_+:=X_H^Th_+(K)X_H/n\preceq M_{rid},\qquad I-M_+\succeq c_0I.
\]
For \(\beta=\beta_H^*\), directional Cauchy-Schwarz implies
\[
\|(I-M_+)\beta\|\,\|\beta\|\geq\beta^T(I-M_+)\beta\geq c_0\|\beta\|^2.
\]
Thus head bias is at least \(\lambda_-c_0^2\|\beta\|^2\geq c\Theta_H\). Since \(a/(a+\lambda_j)\asymp1\) uniformly, this proves the desired lower bound for the infimum over both positive classes. No squared Loewner-order assertion or substitution of population eigenvalues into an empirical filter is needed.

## 6. Stable negative endpoints

Fix any \(0\leq\nu<\widehat\mu_{\min}^+\) and put \(D_\nu=K-\nu I\succ0\), \(d=|a-\nu|\), and \(\mathcal D=\sigma_\varepsilon^2S/n\). On the tail-band projector,
\[
D_\nu^{-2}\succeq\frac{P_B}{(d+Cw)^2}.
\]
Taking its trace against positive semidefinite \(K_{2,T}\) gives
\[
V_T(\nu)\geq\frac{c\mathcal D}{(d+Cw)^2}.
\]
Choose a numerical constant \(C_0>0\), fixed large enough relative to the numerical band constants, and define
\[
F(b)=\Theta\frac{b^2}{(b+\lambda_+)^2}+\frac{\mathcal D}{(b+C_0w)^2},\qquad b\geq0.
\]
This b is a variable of a deterministic envelope, not a replacement definition of the estimator domain.

If \(\nu>a\), the existence of at least one tail-band eigenvalue and admissibility imply \(0<\nu-a<Cw\). If \(\nu\leq a\) but \(b=a-\nu\leq Mw\), for a fixed sufficiently large numerical M, again \(d=O(w)\). In either case,
\[
V_T(\nu)\geq c\mathcal D/w^2\geq c'F(0)\geq c'\inf_{b\geq0}F(b).
\]
Thus no head-bias lower bound is needed near or above the floor.

In the remaining case \(b=a-\nu\geq Mw\), choose M so that \(\|E_T\|\leq b/2\). Then \(B_\nu=K_T-\nu I=bI+E_T\succeq bI/2\), and
\[
C_\nu=X_H^TB_\nu^{-1}X_H/n\succeq0,\qquad\|C_\nu\|\leq C\lambda_+/b.
\]
The same matrix inversion identity gives head map \(C_\nu(I+C_\nu)^{-1}\). Its residual is \((I+C_\nu)^{-1}\beta_H^*\), so head bias is at least
\[
\frac{\lambda_-\|\beta_H^*\|^2}{(1+\|C_\nu\|)^2}
\geq c\Theta\frac{b^2}{(b+\lambda_+)^2}.
\]
Together with the tail-variance estimate, this is at least \(cF(b)\), and hence at least \(c\inf F\).

Finally, the head-noise floor holds uniformly over the entire source endpoint class. Because \(\nu\geq0\) and \(D_\nu\succ0\), all its eigenvalues are at most \(\|K\|\), so
\[
D_\nu^{-2}\succeq\|K\|^{-2}I,
\qquad
\frac{\sigma_\varepsilon^2}{n}\operatorname{tr}(K_{2,H}D_\nu^{-2})
\geq\frac{\sigma_\varepsilon^2\operatorname{tr}K_{2,H}}{n\|K\|^2}
\geq c\frac{\sigma_\varepsilon^2k}{n}.
\]
This is a separate nonnegative component of risk from the tail variance and head bias used above. Adding it and taking the infimum over admissible nu proves the full endpoint envelope.

Let \(b^*=(\mathcal D\lambda_+^2/\Theta)^{1/4}\). Since \(S/(n\lambda_+^2)\to0\) and the signal and noise scales are bounded above and below, \(b^*/\lambda_+\to0\). Assume \(w=o(b^*)\). For \(0\leq b\leq b^*\),
\[
F(b)\geq\frac{\mathcal D}{(b^*+C_0w)^2}\geq c\frac{\sqrt{\Theta\mathcal D}}{\lambda_+}.
\]
For \(b\geq b^*\), monotonicity of \(b/(b+\lambda_+)\) gives
\[
F(b)\geq\Theta\frac{(b^*)^2}{(b^*+\lambda_+)^2}\geq c\frac{\sqrt{\Theta\mathcal D}}{\lambda_+}.
\]
This proves the simplified endpoint lower bound without assuming that the infimum is attained at the balancing value.

## 7. Final comparison

All bounds hold on the same event \(\mathcal E_n\), whose probability tends to one; the comparator estimates are uniform over their entire stated parameter sets. If \(\Delta_{shape}\geq c\Theta_H\) eventually, the deterministic vanishing remainder in the rescaling bound is eventually at most \(\Delta_{shape}/2\). Hence \(R_{scale}^*\geq\Delta_{shape}/2\). Whenever any stated comparator lower bound is at least a factor \(n^\delta\), for fixed \(\delta>0\), larger than the signed upper bound, division gives the corresponding \(O(n^{-\delta})\) risk ratio on this same event. There are no unresolved reference-proof obligations.
