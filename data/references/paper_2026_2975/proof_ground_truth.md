# Reference Proof

## Proof Structure

1. Apply the standard Novikov-Girsanov theorem on a weak representation of the guided sampler. Verify that the initial distribution is unchanged and that the resulting uncontrolled path law is the specified prior.
2. Verify that the stochastic exponential is measurable with respect to the state trajectory, so it is the path-space Radon-Nikodym derivative, even for singular covariance.
3. Combine that derivative with the terminal likelihood and posterior tilt to obtain the weighted-expectation identity and its endpoint specialization.
4. Apply the iid law of large numbers separately to the weighted numerator and denominator, including the zero-denominator convention.

## Complete Proof

Fix the observed data and use the notation of the public task. Write \(a_s=\Sigma_s^{1/2}\) and \(g_s(x)=\nabla_xG_s(x)\). Realize the guided process on a filtered probability space \((\Omega,\mathcal F,(\mathcal F_s),\mathsf Q)\), with Brownian motion \(W^G\), initial law \(\mu\), and state-path law \(Q_t\). Thus
\[
dX_s^G=\bigl(b_s(X_s^G,X_t^G)+\Sigma_sg_s(X_s^G)\bigr)\,ds+a_s\,dW_s^G,
\qquad u_s=a_sg_s(X_s^G).
\]
The control is progressively measurable. The public Novikov assumption, which is a state-path expectation, is the same assumption under this representation. In particular, \(\int_t^{t+1}\|u_s\|^2ds<\infty\) almost surely.

The standard Novikov-Girsanov theorem states that
\[
L_s=\exp\left(-\int_t^su_r\cdot dW_r^G-\frac12\int_t^s\|u_r\|^2dr\right)
\]
is a positive martingale with \(L_t=1\), and that under \(d\overline{\mathsf P}=L_{t+1}\,d\mathsf Q\), the process
\[
\overline W_s-\overline W_t=W_s^G-W_t^G+\int_t^su_r\,dr
\]
is Brownian. These hypotheses have just been verified. Since \(E_{\mathsf Q}[L_{t+1}\mid\mathcal F_t]=1\), changing measure preserves the initial distribution \(\mu\). Because \(a_su_s=\Sigma_sg_s(X_s^G)\), substitution gives
\[
dX_s^G=b_s(X_s^G,X_t^G)\,ds+a_s\,d\overline W_s.
\]
The uncontrolled equation has a unique law for initial distribution \(\mu\); hence the state-path law under \(\overline{\mathsf P}\) is \(P_t\).

We next justify passage from the representation-space density to the state-path density. Define the guided state martingale part
\[
M_s=X_s^G-X_t^G-\int_t^s\bigl(b_r(X_r^G,X_t^G)+\Sigma_rg_r(X_r^G)\bigr)\,dr.
\]
This is a functional of the state trajectory, and \(dM_s=a_s\,dW_s^G\). Its quadratic covariation is \(d\langle M\rangle_s=\Sigma_s\,ds\). Consequently,
\[
\int_t^{t+1}g_s(X_s^G)^\top\Sigma_sg_s(X_s^G)\,ds
=\int_t^{t+1}\|u_s\|^2ds<\infty
\]
almost surely, so the stochastic integral against \(M\) exists. By associativity of stochastic integration and symmetry of \(a_s\),
\[
\int_t^{t+1}g_s(X_s^G)\cdot dM_s
=\int_t^{t+1}a_sg_s(X_s^G)\cdot dW_s^G
=\int_t^{t+1}u_s\cdot dW_s^G.
\]
The integral against \(M\) is measurable with respect to the completed state-path sigma-field: it is obtained as a probability limit of measurable elementary stochastic integrals, with an almost surely convergent subsequence giving a measurable version. Thus \(L_{t+1}\) has a state-path-measurable version, say \(r(X^G)\). This argument does not require invertibility of \(\Sigma_s\).

For every bounded measurable path functional \(F\), the law identification above yields
\[
E_{P_t}[F]=E_{\overline{\mathsf P}}[F(X^G)]
=E_{\mathsf Q}[L_{t+1}F(X^G)]
=E_{Q_t}[rF].
\]
Therefore \(P_t\ll Q_t\) and \(R=r\), \(Q_t\)-almost surely. In particular, the stochastic exponential has the correct direction, from the guided law to the prior. Its positivity also gives equivalence, although only absolute continuity is needed below. In a general weak representation without the source's control structure, the pushforward density would instead be the conditional expectation of \(L_{t+1}\) given the state path; identifying it directly with \(L_{t+1}\) would require a separate justification.

Now let \(\Phi\) be bounded and measurable. Since \(0<Z_{t+1}<\infty\),
\[
E_{P_t}[\ell_{t+1}(X_{t+1})|\Phi(X)|]
\leq \|\Phi\|_\infty Z_{t+1}<\infty.
\]
Using the Radon-Nikodym identity first for nonnegative functions establishes the corresponding absolute integrability under \(Q_t\). Thus change of measure applies to the signed functional as well, giving
\[
\begin{aligned}
E_{Q_t}[w_{t+1}(X^G)\Phi(X^G)]
&=E_{Q_t}[\ell_{t+1}(X_{t+1}^G)R(X^G)\Phi(X^G)]\\
&=E_{P_t}[\ell_{t+1}(X_{t+1})\Phi(X)]\\
&=Z_{t+1}E_{P_{t+1}}[\Phi(X)].
\end{aligned}
\]
The last equality is precisely the defining posterior tilt. Taking \(\Phi(X)=\varphi(X_{t+1})\) proves the endpoint identity. Taking \(\Phi=1\) gives \(E_{Q_t}[w_{t+1}]=Z_{t+1}\).

For an iid sequence of guided paths, let
\[
A_N=\frac1N\sum_{i=1}^Nw_i\varphi(X_{t+1}^{G,(i)}),
\qquad B_N=\frac1N\sum_{i=1}^Nw_i.
\]
The variables \(w_i\) are nonnegative and integrable, with mean \(Z_{t+1}>0\), and
\[
E[|w_i\varphi(X_{t+1}^{G,(i)})|]
\leq\|\varphi\|_\infty Z_{t+1}<\infty.
\]
The iid law of large numbers for integrable real random variables therefore gives, in probability,
\[
A_N\longrightarrow Z_{t+1}E_{P_{t+1}}[\varphi(X_{t+1})],
\qquad B_N\longrightarrow Z_{t+1}.
\]
In particular,
\[
\Pr(B_N=0)\leq\Pr(|B_N-Z_{t+1}|\geq Z_{t+1}/2)\longrightarrow0.
\]
On the event \(B_N>Z_{t+1}/2\), division is continuous at the limiting pair, and the estimator is \(A_N/B_N\). The complementary event has probability tending to zero, so defining the estimator to be zero when its denominator vanishes does not affect the limit. Hence
\[
\widehat\pi_{t+1}^N(\varphi)\longrightarrow
E_{P_{t+1}}[\varphi(X_{t+1})]
\quad\text{in probability}.
\]

## Obligation Audit

All theorem-critical obligations are closed above. The external inputs are the explicitly stated standard Novikov-Girsanov theorem and the iid law of large numbers for integrable random variables. The state-path density identification, initial-law preservation, normalization, absolute integrability, and zero-denominator argument are explicitly supplied. No specialized paper-dependent proof obligation remains unresolved.
