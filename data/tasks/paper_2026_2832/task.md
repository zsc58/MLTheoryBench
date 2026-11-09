# Problem

## Setup

Let \(D\geq1\), \(1\leq d_i\leq D\), and \(0<t_0<T<\infty\). For domains \(i=1,2\), let \(X_0=A_iZ_i+\varepsilon_i\), where \(A_i\in\mathbb R^{D\times d_i}\) has orthonormal columns, \(Z_i\in\mathbb R^{d_i}\), and \(\varepsilon_i\sim N(0,\sigma_i^2I_D)\) is independent of \(Z_i\), with \(\sigma_i>0\). Let \(X_t=\alpha(t)X_0+\sqrt{h(t)}\xi\), where \(\xi\sim N(0,I_D)\) is independent of \(X_0\), \(\alpha(t)=e^{-t/2}\), and \(h(t)=1-e^{-t}\). Write \(p_{i,t}\) for the density of \(X_t\) in domain \(i\), and \(\tilde h_i(t)=\alpha(t)^2\sigma_i^2+h(t)\).

In the target domain, let \(Y_t=A_2^TX_t\), let \(p^{\rm LD}_{2,t}\) denote its density, and put
\[
g_2(y,t)=h(t)\nabla\log p^{\rm LD}_{2,t}(y)+y,\quad
\mu_2(t)=\lambda_{\min}E[g_2(Y_t,t)g_2(Y_t,t)^T],\quad
\lambda_{g,2}^{\max}(t)=\lambda_{\max}E[g_2(Y_t,t)g_2(Y_t,t)^T],\quad
M_{Y,2}(t)=E[Y_tY_t^T].
\]
Fix \(V_1\in\mathbb R^{D\times d_1}\) with orthonormal columns, independently of the target training observations. Set \(B=V_1^TA_2\), \(r=\min(d_1,d_2)\), and let \(0\leq\theta_1\leq\cdots\leq\theta_r\leq\pi/2\) be determined by the singular values \(\sigma_j(B)=\cos\theta_j\). Write \(B^\dagger\) for the Moore-Penrose pseudoinverse.

Assume the target latent variable has a positive twice continuously differentiable density \(p_{2,z}\), and that there are constants \(B_2,C_{1,2},C_{2,2}>0\) for which
\[
p_{2,z}(z)\leq(2\pi)^{-d_2/2}C_{1,2}e^{-C_{2,2}\|z\|^2/2}\qquad(\|z\|\geq B_2).
\]
Assume also that \(f_2^*(y,t)=\tilde h_2(t)\nabla\log p^{\rm LD}_{2,t}(y)+y\) is uniformly \(\beta_2\)-Lipschitz in \(y\) for \(t\in[0,T]\). Let \(L_g\) be a finite uniform Lipschitz constant for \(g_2(\cdot,t)\) on \([t_0,T]\); for example, \(L_g=\beta_2+1\) is admissible.

For a measurable core \(f:\mathbb R^{d_1}\times[t_0,T]\to\mathbb R^{d_1}\), define \(s_{V_1,f}(x,t)=h(t)^{-1}[V_1f(V_1^Tx,t)-x]\) and
\[
L_2(s)=\frac1{T-t_0}\int_{t_0}^T E\|s(X_t,t)-\nabla\log p_{2,t}(X_t)\|^2dt.
\]
Let \(B_{\rm str}(V_1)=\inf_{f\text{ measurable}}L_2(s_{V_1,f})\). Let \(F_{\rm ReLU}\) consist of maps \(f:\mathbb R^{d_1}\times[t_0,T]\to\mathbb R^{d_1}\) represented by depth-\(L\) ReLU networks of width at most \(M\), at most \(J\) nonzero parameters, weights and biases bounded entrywise by \(\kappa\), uniform output norm at most \(K\), and spatial and time Lipschitz constants at most \(\gamma\) and \(\gamma_t\), respectively. Its architecture parameters are fixed independently of the target training observations. Put \(B_{\rm freeze}(V_1)=\inf_{f\in F_{\rm ReLU}}L_2(s_{V_1,f})\).

For the approximation level \(\epsilon>0\), require the selected architecture to satisfy the following capacity condition, with \(C_T=(T/(1-e^{-T}))^2\):
\[
\inf_{f\in F_{\rm ReLU}}\frac1{T-t_0}\int_{t_0}^T\frac{E\|f(V_1^TX_t,t)-B g_2(B^\dagger V_1^TX_t,t)\|^2}{h(t)^2}\,dt
\leq \frac{C_T(d_1+1)\epsilon^2}{t_0(T-t_0)}.
\]

For finite-sample training, observe \(N_2\geq1\) independent initial target observations \(x_1,\ldots,x_{N_2}\), each distributed as \(X_0\). Conditional noising in the following loss means the Gaussian channel above, independently specified for each \(x\); its expectation and time integral are part of the loss, not extra sampled training pairs:
\[
\ell_2(x;s)=\frac1{T-t_0}\int_{t_0}^T E_{X_t\mid X_0=x}\left\|s(X_t,t)+\frac{X_t-\alpha(t)x}{h(t)}\right\|^2dt,\qquad
\widehat R_{N_2}(s)=\frac1{N_2}\sum_{n=1}^{N_2}\ell_2(x_n;s).
\]
Let \(\widehat s_{\rm freeze}\) be any minimizer of \(\widehat R_{N_2}\) over scores induced by \(F_{\rm ReLU}\). For \(\delta\in(0,1)\), set
\[
R_z=C_z(1+\sigma_2)\left(\sqrt{d_2}+\sqrt{\log(8N_2/\delta)}\right),\qquad
R_\perp=C_\perp\sigma_2\left(\sqrt{D-d_2}+\sqrt{\log(8N_2/\delta)}\right),
\]
where \(C_z,C_\perp\) are sufficiently large constants determined by the displayed latent tail bound and Gaussian concentration. Define \(\mathcal T=\{x:\|A_2^Tx\|\leq R_z,\ \|(I-A_2A_2^T)x\|\leq R_\perp\}\). For \(\iota>0\), let \(N_2(\iota)\) be the \(\iota\)-covering number in the sup norm on \(\mathbb R^D\) of \(\{x\mapsto\ell_2(x;s)\mathbf1_{\mathcal T}(x):s=s_{V_1,f},\ f\in F_{\rm ReLU}\}\), and assume it is finite. Let \(E_2\) be the score-independent nonnegative constant defined by \(E_{X_0}\ell_2(X_0;s)=L_2(s)+E_2\). It satisfies
\[
E_2\leq\frac D{T-t_0}\log\frac{e^T-1}{e^{t_0}-1}.
\]

## Task

Prove the integrated frozen-reuse theorem. The unavoidable risk satisfies
\[
B_{\rm str}(V_1)\geq\frac1{T-t_0}\int_{t_0}^T\left[\frac{\mu_2(t)}{h(t)^2}\left(d_2-\sum_{j=1}^r\cos^2\theta_j\right)+\frac{\alpha(t)^4\sigma_2^4}{h(t)^2\tilde h_2(t)}\left(D-d_1-d_2+\sum_{j=1}^r\cos^2\theta_j\right)\right]dt,
\]
and the same lower bound holds for \(B_{\rm freeze}(V_1)\).

If \(d_1\geq d_2\) and \(B\) has full column rank, define \(U\) as the time average of
\[
\frac{\lambda_{g,2}^{\max}(t)}{h(t)^2}\sum_{j=1}^{d_2}\sin^2\theta_j
+\frac{2\|B\|_{\rm op}^2\tilde h_2(t)L_g^2}{h(t)^2}\sum_{j=1}^{d_2}\tan^2\theta_j
+\frac{\alpha(t)^4\sigma_2^4}{h(t)^2\tilde h_2(t)}\left(D+d_1-d_2-\sum_{j=1}^{d_2}\cos^2\theta_j\right).
\]
If \(d_1<d_2\) and \(B\) has full row rank, instead define \(U\) as the time average of
\[
\frac{\lambda_{g,2}^{\max}(t)}{h(t)^2}\left(d_2-\sum_{j=1}^{d_1}\cos^2\theta_j\right)
+\frac{2\|B\|_{\rm op}^2L_g^2}{h(t)^2}\operatorname{Tr}[(I_{d_2}-B^\dagger B)M_{Y,2}(t)]
+\frac{2\|B\|_{\rm op}^2\tilde h_2(t)L_g^2}{h(t)^2}\sum_{j=1}^{d_1}\tan^2\theta_j
+\frac{\alpha(t)^4\sigma_2^4}{h(t)^2\tilde h_2(t)}\left(D+d_1-d_2-\sum_{j=1}^{d_1}\cos^2\theta_j\right).
\]
Here and below, the time average of \(q(t)\) means \((T-t_0)^{-1}\int_{t_0}^Tq(t)dt\). In either full-rank case, show that for every \(\eta>0\),
\[
B_{\rm freeze}(V_1)\leq(1+\eta)U+(1+1/\eta)\frac{C_T(d_1+1)\epsilon^2}{t_0(T-t_0)}.
\]
Finally, for every \(a\in(0,1)\) and \(\iota>0\), prove that with probability at least \(1-\delta\),
\[
\begin{aligned}
L_2(\widehat s_{\rm freeze})\leq{}&C C_T\frac{(K^2+R_z^2+R_\perp^2)\delta}{N_2t_0(T-t_0)}+(2+a)\iota\\
&+C C_T(1+1/a)\frac{(K^2+R_z^2+R_\perp^2)[\log N_2(\iota)+\log(8/\delta)]}{N_2t_0(T-t_0)}\\
&+(1+a)^2(1+\eta)U
 +(1+a)^2(1+1/\eta)\frac{C_T(d_1+1)\epsilon^2}{t_0(T-t_0)}+(2a+a^2)E_2,
\end{aligned}
\]
where \(C\) is an absolute constant. State the bound after setting \(\eta=1\) and \(\iota=[N_2t_0(T-t_0)]^{-1}\). When \(0<\epsilon<1\), also state its specialization \(a=\epsilon^2\).
