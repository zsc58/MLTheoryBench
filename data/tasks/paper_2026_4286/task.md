# Problem

## Model and notation

Fix integers T>=W>=1 and p>=1, a confidence level delta in (0,1), and a quantile level tau in (0,1). Independent observations (X_t,Y_t), 1<=t<=T, satisfy

\[
Y_t=X_t^\top\beta^*+\varepsilon_t,
\qquad S=\operatorname{supp}(\beta^*),\qquad 1\le s_0=|S|\le s\le p.
\]

Let m be a nonnegative integer and set \(\bar s=s+m+s_0\). Write \(\beta_{\min}=\min_{k\in S}|\beta_k^*|>0\). The covariates are iid, mean zero, and sub-Gaussian: for a finite K,

\[
\sup_{\|u\|_2=1}\|u^\top X_t\|_{\psi_2}\le K,
\qquad \Sigma=\mathbb E[X_tX_t^\top],
\]

where \(\|Z\|_{\psi_2}=\inf\{a>0:\mathbb E\exp(Z^2/a^2)\le2\}\). Assume \(\Pr(\varepsilon_t\le0\mid X_t)=\tau\). The conditional noise distribution has a density satisfying, almost surely,

\[
f_{\varepsilon\mid X}(u\mid X_t)\ge m_0>0\quad (|u|\le b_0),
\qquad f_{\varepsilon\mid X}(u\mid X_t)\le M_1<\infty\quad(u\in\mathbb R),
\]

for a fixed \(b_0>0\). For a fixed \(m_1>0\), assume

\[
v^\top\Sigma v\ge m_1\|v\|_2^2
\quad\text{whenever }\|v\|_0\le\bar s.
\]

For \(W\le t\le T\), define

\[
\rho_\tau(u)=u(\tau-\mathbf1\{u<0\}),\qquad
Q_t(\beta)=\frac1W\sum_{i=t-W+1}^t\rho_\tau(Y_i-X_i^\top\beta),
\]

and use the subgradient selection

\[
\bar g_t(\beta)=-\frac1W\sum_{i=t-W+1}^tX_i\bigl(\tau-\mathbf1\{Y_i\le X_i^\top\beta\}\bigr).
\]

For an index set A, \(P_Av\) agrees with v on A and is zero elsewhere. The operator \(H_s\) retains the s largest-magnitude coordinates and sets the rest to zero, with a fixed rule for ties.

## Updates and local assumptions

Epochs \(\mathcal T_j=\{\tau_j,\ldots,\tau_{j+1}-1\}\), with positive integer lengths and \(W\le\tau_0<\cdots<\tau_N=T+1\), partition the post-burn-in update times. At the start of epoch j choose a candidate set satisfying

\[
\operatorname{supp}(\beta_{\tau_j})\subseteq A_j,
\qquad |A_j|\le s+m,
\]

and keep it fixed during that epoch. Candidate and step-size choices use only observations available when they are made. For positive step sizes, set

\[
d_t=P_{A_j}\bar g_t(\beta_t),\qquad
\widetilde\beta_{t+1}=\beta_t-\eta_t d_t.
\]

If \(t<\tau_{j+1}-1\), set \(\beta_{t+1}=\widetilde\beta_{t+1}\); at the endpoint set \(\beta_{\tau_{j+1}}=H_s(\widetilde\beta_{\tau_{j+1}})\). Write \(\Delta_t=\beta_t-\beta^*\) and \(B_j=\sum_{t\in\mathcal T_j}\eta_t\).

Fix positive finite constants \(C_\zeta,L_{\rm off},L_{\rm on},\mu,G\), a finite \(C_{\rm sc}\ge0\), constants \(0<R_{\rm in}<R\), and \(0<c_{\rm small}<c_{\rm large}\). Put

\[
\zeta=C_\zeta\sqrt{\frac{\log(pT/\delta)}{W}},\qquad
\Gamma_\zeta(c,S)=\{v:\|v_{S^c}-\beta^*_{S^c}\|_1\le c(\|v_S-\beta^*_S\|_1+\zeta)\}.
\]

Assume there is an event \(\mathcal E\), of probability at least \(1-\delta\), on which all of the following hold simultaneously.

1. With \(\widehat\Sigma_t=W^{-1}\sum_{i=t-W+1}^tX_iX_i^\top\), there is a fixed finite \(C_\infty\) such that

\[
\max_{W\le t\le T}\ \sup_{S\subseteq A,\ |A|\le\bar s}
\left(\|\widehat\Sigma_{t,S,A}\|_{\infty\to\infty}
+\|\widehat\Sigma_{t,S^c,A}\|_{\infty\to\infty}\right)\le C_\infty,
\]

where \(\|\cdot\|_{\infty\to\infty}\) is the maximum absolute row-sum norm.

2. At every epoch start,

\[
\|\Delta_{\tau_j,S^c}\|_1\le c_{\rm small}(\|\Delta_{\tau_j,S}\|_1+\zeta),
\qquad \|\Delta_{\tau_j}\|_2\le R_{\rm in}.
\]

3. The local direction controls have the following precise meaning: at any update time t, if \(\beta_t\in\Gamma_\zeta(c_{\rm large},S)\) and \(\|\Delta_t\|_2\le R\), then

\[
\|d_{t,S^c}\|_1\le L_{\rm off}(\|\Delta_{t,S}\|_1+\zeta),
\qquad
\|d_{t,S}\|_1\le L_{\rm on}(\|\Delta_{t,S}\|_1+\zeta).
\]

These are hypotheses on \(\mathcal E\), not additional conclusions to be established from the distributional assumptions. The constants may depend on the working sparsity and candidate size as well as the fixed local distributional parameters; they are uniform over the stated times.

4. For every epoch and update time,

\[
\eta_tL_{\rm on}\le\frac12,
\qquad
B_j\le\min\left\{
\frac{c_{\rm large}-c_{\rm small}}{2(L_{\rm off}+c_{\rm large}L_{\rm on})},
\frac{R-R_{\rm in}}{(L_{\rm off}+L_{\rm on})(\sqrt{s_0}R+\zeta)}
\right\}.
\]

5. The candidate sets cover S, and endpoint thresholding preserves it:

\[
S\subseteq A_j,
\qquad
S\subseteq\operatorname{supp}\bigl(H_s(\widetilde\beta_{\tau_{j+1}})\bigr).
\]

6. At every post-burn-in update time,

\[
\langle\bar g_t(\beta_t)-\bar g_t(\beta^*),\Delta_t\rangle
\ge\mu\|\Delta_t\|_2^2,
\]

\[
-2\eta_t\langle\bar g_t(\beta^*),\Delta_t\rangle
\le\frac\mu2\eta_t\|\Delta_t\|_2^2+C_{\rm sc}\eta_t^2,
\qquad \|d_t\|_2\le G.
\]

All constants in these event assumptions are uniform over the indicated times. They may depend on the fixed local parameters, window size, and sparse/candidate dimensions; no independence between an iterate and its overlapping data window is assumed.

## Claims

Prove the following on \(\mathcal E\).

**Invariance.** Every iterate \(\beta_t\), every provisional update \(\widetilde\beta_{t+1}\), and every thresholded epoch endpoint belongs to \(\Gamma_\zeta(c_{\rm large},S)\) and has Euclidean error at most R.

**Epoch contraction.** There is a constant C, depending only on \(C_{\rm sc}\) and G and not on the epoch or its length, such that

\[
\|\Delta_{\tau_{j+1}}\|_2^2
\le e^{-\mu B_j}\|\Delta_{\tau_j}\|_2^2
+C\sum_{t\in\mathcal T_j}\eta_t^2.
\]

If the Phase I epochs satisfy \(B_j\ge B_{\min}>0\), prove the norm bound

\[
\|\Delta_{\tau_{j+1}}\|_2
\le e^{-\mu B_{\min}/2}\|\Delta_{\tau_j}\|_2
+\sqrt C\left(\sum_{t\in\mathcal T_j}\eta_t^2\right)^{1/2}.
\]

In particular, if a fixed \(q\in(e^{-\mu B_{\min}},1)\) satisfies

\[
C\sum_{t\in\mathcal T_j}\eta_t^2
\le(q-e^{-\mu B_{\min}})\|\Delta_{\tau_j}\|_2^2
\]

throughout those epochs, conclude geometric squared-error contraction with factor q.

**Refinement.** Let \(T_0+1\) be an epoch start at which Phase II begins. Suppose, for \(T_0+1\le t\le T\),

\[
\eta_t=\frac1{c_{\rm eff}(t+b_2)},\qquad 0<c_{\rm eff}\le\mu,
\]

where \(b_2\ge1\) and the explicit step-size and epoch budgets above continue to hold. Prove that, for \(T_0+1\le t\le T+1\),

\[
\|\Delta_t\|_2^2\le C'\frac{\log(t+b_2)}{t+b_2},
\]

where C' is independent of t and may depend on \(C_{\rm sc},G,c_{\rm eff},R,T_0,b_2\). Thus the squared-error rate is \(O(\log(t)/t)\), and the norm-error rate is \(O(\sqrt{\log(t)/t})\), with these parameters held fixed.
