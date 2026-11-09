# Reference Proof

Let \(P_2=A_2A_2^T\), \(P_1=V_1V_1^T\), \(Y_t=A_2^TX_t\), \(U_t=(I-P_2)X_t\), and \(\rho(t)=\alpha(t)^2\sigma_2^2/\tilde h_2(t)\). Gaussian factorization gives independence of \(Y_t\) and \(U_t\), with \(U_t\sim N(0,\tilde h_2(t)(I-P_2))\), and
\[
G_t(x):=h(t)\nabla\log p_{2,t}(x)+x=A_2g_2(A_2^Tx,t)+\rho(t)(I-P_2)x.
\]
Thus the frozen-score error is \(h(t)^{-1}[V_1f(V_1^TX_t,t)-G_t(X_t)]\).

## Structural converse

Orthogonally project this error onto \(\operatorname{col}(V_1)^\perp\). Independence and \(E[U_t]=0\) remove the signal/noise cross term. For every measurable core its time-\(t\) risk is at least
\[
h(t)^{-2}\{\operatorname{Tr}[A_2^T(I-P_1)A_2 E(g_2g_2^T)]+\rho(t)^2\tilde h_2(t)\operatorname{Tr}[(I-P_1)(I-P_2)]\}.
\]
The first trace is at least \(\mu_2(t)(d_2-\sum_{j=1}^r\cos^2\theta_j)\); the projector trace is \(D-d_1-d_2+\sum_{j=1}^r\cos^2\theta_j\). Integrate this pointwise bound before taking the infimum over time-dependent measurable cores. Inclusion of the ReLU class gives its lower bound.

## Comparator

Use \(f_{\rm comp}(z,t)=Bg_2(B^\dagger z,t)\). Put \(Z_t=V_1^TX_t=BY_t+V_1^TU_t\). The squared normalized error splits orthogonally into an output-side part \(O_t\) and an in-space part \(I_t\). Independence gives
\[
O_t\leq\lambda_{g,2}^{\max}(t)(d_2-\|B\|_F^2)+\rho(t)^2\tilde h_2(t)(D-d_1-d_2+\|B\|_F^2).
\]
Since \(Y_t-B^\dagger Z_t=(I-B^\dagger B)Y_t-B^\dagger V_1^TU_t\), Lipschitzness and \(\|u+v\|^2\leq2\|u\|^2+2\|v\|^2\) give
\[
I_t\leq2\|B\|_{\rm op}^2L_g^2\{\operatorname{Tr}[(I-B^\dagger B)M_{Y,2}(t)]+\tilde h_2(t)\operatorname{Tr}[B^\dagger V_1^T(I-P_2)V_1(B^\dagger)^T]\}+2\rho(t)^2\tilde h_2(t)(d_1-\|B\|_F^2).
\]
The pseudoinverse trace is \(\sum_{j=1}^r\tan^2\theta_j\) in either full-rank case. For full column rank, \(B^\dagger B=I_{d_2}\), so the information-loss trace is zero and \(d_2-\|B\|_F^2=\sum_{j=1}^{d_2}\sin^2\theta_j\). For full row rank, retain the information-loss trace and use \(d_2-\|B\|_F^2=d_2-\sum_{j=1}^{d_1}\cos^2\theta_j\). Combining the two noise traces gives \(\rho(t)^2\tilde h_2(t)(D+d_1-d_2-\|B\|_F^2)\). Divide by \(h(t)^2\) and integrate to obtain \(L_2(s_{\rm comp})\leq U\).

## ReLU transfer and approximation obligation

The architecture-capacity premise bounds the infimum of the weighted squared error relative to \(f_{\rm comp}\) by \(A_\epsilon:=C_T(d_1+1)\epsilon^2/[t_0(T-t_0)]\). Add and subtract \(s_{\rm comp}\), apply \(\|u+v\|^2\leq(1+\eta)\|u\|^2+(1+1/\eta)\|v\|^2\), and infimize to get \(B_{\rm freeze}(V_1)\leq(1+\eta)U+(1+1/\eta)A_\epsilon\).

A fixed comparison core attaining the approximation infimum can be chosen independently of the sample. Indeed, pad the finite-width architecture to a fixed finite parameter space. The parameter bounds make that space compact; sparsity, global output, and Lipschitz constraints are closed under parameter convergence. The objective is continuous there by dominated convergence: network outputs are bounded, the comparator has at most linear growth under the stated Lipschitz and tail assumptions, and \(t_0>0\). Denote its frozen score by \(\bar s_\epsilon\).

The source also advertises an explicit construction meeting the capacity premise. Conditional on its compact-box ReLU construction, the comparator has spatial Lipschitz constant at most \(\|B\|_{\rm op}\|B^\dagger\|_{\rm op}(\beta_2+1)\). Its finite compact-box time modulus, bounded value at zero, and the target tail bound permit a box for which squared approximation error is at most \(d_1\epsilon^2\) inside and \(\epsilon^2\) outside, uniformly in time. Since \(h(t)\geq(1-e^{-T})t/T\), its weighted error is at most \(A_\epsilon\). The supplied source does not prove the specialized network construction or verify its simultaneous architecture constraints. This architecture-existence step remains open here; it is not a completed rubric step.

## Finite sample: denoising and truncation

Let \(H_t=-(X_t-\alpha(t)X_0)/h(t)\). Gaussian differentiation gives \(E[H_t\mid X_t]=\nabla\log p_{2,t}(X_t)\). Conditional orthogonality yields \(\mathcal R_2(s):=E_{X_0}\ell_2(X_0;s)=L_2(s)+E_2\), where \(E_2=(T-t_0)^{-1}\int E\|H_t-E(H_t\mid X_t)\|^2dt\). Since \(E\|H_t\|^2=D/h(t)\),
\[
0\leq E_2\leq\frac D{T-t_0}\log\frac{e^T-1}{e^{t_0}-1}.
\]

Here are the needed truncation estimates. Write \(z=Z_2\), \(Y=A_2^TX_0=z+\sigma_2G_{d_2}\), and \(Q=(I-P_2)X_0=\sigma_2G_{D-d_2}\), with the Gaussian vectors independent of \(z\) and of each other. Thus \(Y\) and \(Q\) are independent. The displayed density bound, by integration outside a ball, gives for \(r\geq B_2\)
\[
P(\|z\|>r)\leq C_{1,2}C_{2,2}^{-d_2/2}P(\|G_{d_2}\|>\sqrt{C_{2,2}}r).
\]
For \(k\geq1\), Gaussian norm concentration gives \(P(\|G_k\|>\sqrt{k}+\sqrt{2v})\leq e^{-v}\). Applying this bound to \(z\), \(\sigma_2G_{d_2}\), and \(Q\), then using \(\|Y\|\leq\|z\|+\sigma_2\|G_{d_2}\|\), shows that sufficiently large \(C_z,C_\perp\), depending only on the stated tail constants and Gaussian constants, make each of \(P(\|Y\|>R_z)\) and \(P(\|Q\|>R_\perp)\) at most \(\delta/(8N_2)\). The prefactor \(C_{1,2}C_{2,2}^{-d_2/2}\) is absorbed by increasing the coefficient of \(\sqrt{d_2}\) in \(R_z\). If \(D=d_2\), \(Q=0\) and its bounds hold trivially. Hence \(P(X_0\notin\mathcal T)\leq\delta/(4N_2)\), and a union bound makes every training observation lie in \(\mathcal T\) with probability at least \(1-\delta/4\).

The same Gaussian-norm bound applies at every radius above the chosen thresholds. Integrating it using
\[
E[W^2\mathbf1_{\{W>R\}}]=R^2P(W>R)+2\int_R^\infty uP(W>u)\,du
\]
for \(W=\|Y\|,\|Q\|\), with the constants in the radii enlarged to absorb the integral, gives
\[
E[\|Y\|^2\mathbf1_{\{\|Y\|>R_z\}}]\leq C R_z^2\frac\delta{N_2},\qquad
E[\|Q\|^2\mathbf1_{\{\|Q\|>R_\perp\}}]\leq C R_\perp^2\frac\delta{N_2}.
\]
Independence controls the cross terms: \(E[\|Y\|^2\mathbf1_{\{\|Q\|>R_\perp\}}]=E\|Y\|^2P(\|Q\|>R_\perp)\leq C R_z^2\delta/N_2\), since the same norm bounds give \(E\|Y\|^2\leq C R_z^2\). Likewise \(E[\|Q\|^2\mathbf1_{\{\|Y\|>R_z\}}]\leq C R_\perp^2\delta/N_2\). Using \(\mathcal T^c\subseteq\{\|Y\|>R_z\}\cup\{\|Q\|>R_\perp\}\) and \(\|X_0\|^2=\|Y\|^2+\|Q\|^2\), we obtain
\[
E[(K^2+\|X_0\|^2)\mathbf1_{\mathcal T^c}(X_0)]\leq C(K^2+R_z^2+R_\perp^2)\frac\delta{N_2}.
\]
For any frozen score, direct subtraction gives
\[
H_t-s_{V_1,f}(X_t,t)=\frac{\alpha(t)X_0-V_1f(V_1^TX_t,t)}{h(t)}.
\]
The output bound \(\|f\|\leq K\) and \(\int_{t_0}^T h(t)^{-2}dt\leq C_T/t_0\) therefore give \(\ell_2(x;s)\leq C C_T(K^2+\|x\|^2)/[t_0(T-t_0)]\). It follows that the truncated loss is between zero and \(B_u=C C_T(K^2+R_z^2+R_\perp^2)/[t_0(T-t_0)]\), while uniformly over the class the population loss discarded outside \(\mathcal T\) is at most \(C C_T(K^2+R_z^2+R_\perp^2)\delta/[N_2t_0(T-t_0)]\). On the all-observations-in-\(\mathcal T\) event, the truncated and original empirical losses agree for every score.

## Finite sample: concentration and specialization

For completeness, if \(0\leq W\leq B_u\), then \(EW^2\leq B_u EW\). Bernstein's exponential-moment bound consequently gives deviations of the empirical mean from its expectation of at most \(\sqrt{2B_u(EW)u/N_2}+C B_u u/N_2\), with failure probability \(e^{-u}\) on either side. Young's inequality absorbs the square-root term against \(aEW\). Thus, for \(0<a<1\), each of \([EW-(1+a)\overline W]_+\) and \([\overline W-(1+a)EW]_+\) is at most \(C(1+1/a)B_u u/N_2\). Apply the first inequality to an \(\iota\)-net of the truncated loss class. Its sup-norm approximation adds at most \((2+a)\iota\). Apply the second inequality to the fixed \(\bar s_\epsilon\). Union bounds give the statistical term involving \(\log N_2(\iota)+\log(8/\delta)\), with total concentration failure probability at most \(\delta/2\).

The empirical-minimizer comparison, two one-sided deviations, truncation, and \(\mathcal R_2=L_2+E_2\) give
\[
L_2(\widehat s_{\rm freeze})\leq\mathrm{TruncErr}+\mathrm{StatErr}+(1+a)^2L_2(\bar s_\epsilon)+(2a+a^2)E_2.
\]
Insert \(L_2(\bar s_\epsilon)\leq(1+\eta)U+(1+1/\eta)A_\epsilon\) and the preceding estimates. The truncation event and two concentration events have total failure probability at most \(3\delta/4<\delta\). This proves the full explicit bound in the public task.

To state the requested specialization, write \(q=N_2t_0(T-t_0)\) and \(S=K^2+R_z^2+R_\perp^2\). At \(\eta=1\) and \(\iota=q^{-1}\), the bound is
\[
L_2(\widehat s_{\rm freeze})\leq C C_T\frac{S\delta}{q}+\frac{2+a}{q}+C C_T(1+1/a)\frac{S[\log N_2(q^{-1})+\log(8/\delta)]}{q}+2(1+a)^2U+2(1+a)^2\frac{C_T(d_1+1)\epsilon^2}{t_0(T-t_0)}+(2a+a^2)E_2.
\]
For \(0<\epsilon<1\), setting \(a=\epsilon^2\) gives explicitly
\[
L_2(\widehat s_{\rm freeze})\leq C C_T\frac{S\delta}{q}+\frac{2+\epsilon^2}{q}+C C_T(1+\epsilon^{-2})\frac{S[\log N_2(q^{-1})+\log(8/\delta)]}{q}+2(1+\epsilon^2)^2U+2(1+\epsilon^2)^2\frac{C_T(d_1+1)\epsilon^2}{t_0(T-t_0)}+(2\epsilon^2+\epsilon^4)E_2.
\]
Neither specialization discards the covering-scale term or the factors introduced by the one-sided comparison.
