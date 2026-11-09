# Problem

## Setup

Let \(n_x,n_u\) be positive integers and let \(0\le\bar u<\infty\). Matrix norms \(\|\cdot\|\) are spectral norms, vector norms are Euclidean norms, and \(I_d\) denotes the \(d\)-dimensional identity. Consider the unknown stable linear system
\[
x_{t+1}=Ax_t+Bu_t+w_t,\qquad x_0=0,
\]
where \(A\in\mathbb R^{n_x\times n_x}\) has spectral radius less than one, \(B\in\mathbb R^{n_x\times n_u}\) is known, and the process noises are independent \(N(0,I_{n_x})\) draws. States and inputs are observed. Inputs are chosen before the current process noise is drawn; that noise is independent of the observed history and current input.

### Converse experiment

The converse uses a single trajectory without resets. Set
\[
\mathcal F_t=\sigma(x_0,\ldots,x_t,u_0,\ldots,u_{t-1}).
\]
A procedure consists of an \(\mathcal F_t\)-measurable estimator \(\widehat A_t\) and history-measurable conditional input densities. The same estimator functions and policy kernels are used under every system parameter; they do not receive the unknown matrix. The policy is centered and power-constrained in each parameter experiment under consideration:
\[
\mathbb E[u_t\mid\mathcal F_t]=0,
\qquad \mathbb E\|u_t\|^2\le\bar u.
\]
Expectations and probabilities are taken under the specified system parameter. In the experiment at \(A\), write \(U_t=\mathbb E_A[u_tu_t^\top]\).

For \(\varepsilon>0\) and \(\delta\in(0,1)\), a procedure is \((\varepsilon,\delta)\)-locally stable at \(A\) if there is a finite deterministic integer \(\tau\ge1\) such that, for every integer \(t\ge\tau\),
\[
\inf_{\substack{A'\in\mathbb R^{n_x\times n_x}\\\|A'-A\|\le6\sqrt2\,\varepsilon}}
\mathbb P_{A'}(\|\widehat A_t-A'\|\le\varepsilon)\ge1-\delta.
\]
The parameter experiments in this definition use the same dynamics and policy, whether or not \(A'\) is stable. Let \(\tau_A\) be the smallest such time.

### Covariance objective

For integers \(s\ge1\) and a fixed covariance \(U\succeq0\), define
\[
\Gamma_s(A)=\sum_{k=0}^{s-1}A^k(A^k)^\top,
\qquad
\Xi_s(A,U)=\sum_{k=0}^{s-1}A^{s-1-k}BU B^\top(A^{s-1-k})^\top.
\]
Let \(\Gamma_\infty(A)\) and \(\Xi_\infty(A,U)\) be their infinite-horizon limits. Set
\[
J_A(U)=\lambda_{\min}(\Gamma_\infty(A)+\Xi_\infty(A,U)),
\qquad
J_A^*=\max_{U\succeq0,\ \operatorname{tr}U\le\bar u}J_A(U),
\]
and let \(U^*(A)\) denote a measurably selected optimizer. Equivalently, \(J_A^*\) is the optimum of the semidefinite program maximizing \(\lambda\) over symmetric \(U,P\) and real \(\lambda\), subject to
\[
P-APA^\top-I-BUB^\top=0,
\qquad P\succeq\lambda I,
\qquad U\succeq0,\quad\operatorname{tr}U\le\bar u.
\]

### Initialization requirement and two-phase procedure

For a feasible covariance \(U\), put \(Q_U=BUB^\top+I_{n_x}\). For an integer horizon \(h\ge2\), let \(\Gamma_{U,h}\) be the block matrix with \(h-1\) block rows and columns, each block of size \(n_x\times n_x\), whose blocks are
\[
(\Gamma_{U,h})_{ij}=
\begin{cases}
A^{i-j}Q_U^{1/2},&1\le j\le i\le h-1,\\
0,&i<j.
\end{cases}
\]
Fix \(K>0\) and write \(C=c'K^4\), where \(c'>0\) is the universal constant whose existence is asserted below. At horizon \(h\), accuracy \(r>0\), and failure level \(q\in(0,1)\), define the fixed-covariance requirement to be
\[
\lambda_{\min}\left(\sum_{s=1}^{h-1}[\Gamma_s(A)+\Xi_s(A,U)]\right)
\ge C\max\{r^{-2},\|\Gamma_{U,h}\|^2\}\,[\log(1/q)+n_x].
\]
Set \(U_0=(\bar u/n_u)I_{n_u}\). Given \(\delta\in(0,1)\) and an integer \(t_0\ge2\), let \(\varepsilon_{t_0}\) be the smallest positive \(r\) satisfying this requirement for \(h=t_0\), \(U=U_0\), and \(q=\delta/2\). If no such \(r\) exists, set \(\varepsilon_{t_0}=+\infty\).

The achievability experiment permits the following reset and uses this two-phase procedure:

- In phase one, draw mutually independent centered inputs with covariance \(U_0\), independently of the process noises, for times \(0,\ldots,t_0-1\). Compute the minimum-Frobenius-norm least-squares minimizer
\[
\widehat A^{(1)}_{t_0}\in\arg\min_{A'}\sum_{s=0}^{t_0-1}\|x_{s+1}-A'x_s-Bu_s\|^2.
\]
If this matrix is stable, set \(\widetilde A_{t_0}=\widehat A^{(1)}_{t_0}\). Otherwise use a fixed measurable projection rule returning a stable matrix, and call its result \(\widetilde A_{t_0}\). Solve the displayed SDP at \(\widetilde A_{t_0}\) to select \(\widehat U=U^*(\widetilde A_{t_0})\).
- Let \(\mathcal H_0\) denote the sigma-algebra of all first-phase observations, including the terminal state before resetting. Reset \(x_{t_0}=0\). Conditional on \(\mathcal H_0\), phase-two inputs are mutually independent centered draws with covariance \(\widehat U\), independent of the phase-two process noises. For \(t>t_0\), compute the minimum-Frobenius-norm LSE using only
\[
\sum_{s=t_0}^{t-1}\|x_{s+1}-A'x_s-Bu_s\|^2.
\]
Denote this estimate by \(\widehat A_t\); at \(t=t_0\), use the preliminary estimate.

For a scalar random variable \(Z\), use
\[
\|Z\|_{\psi_2}=\inf\{a>0:\mathbb E\exp(Z^2/a^2)\le2\}.
\]
Assume that \(Q_{U_0}^{-1/2}(Bu_s+w_s)\) has independent coordinates, each of \(\psi_2\)-norm at most \(K\), during phase one. During phase two, impose the same condition on \(Q_{\widehat U}^{-1/2}(Bu_s+w_s)\) under the conditional law given \(\mathcal H_0\), almost surely. No absolute-continuity requirement is imposed on the achievability input law; singular feasible covariances are allowed.

## Task

Prove that universal constants \(c,c'>0\) can be chosen so that the following statements hold, with \(C=c'K^4\) in the initialization requirement and upper bound.

1. **Converse.** Every centered, power-constrained \((\varepsilon,\delta)\)-locally stable procedure, for \(\delta\in(0,1/2)\) and
\[
0<\varepsilon<\|\Gamma_\infty(A)\|^{-3}/(12\sqrt2),
\]
satisfies
\[
\tau_A-1\ge
\frac{c\,[n_x+\log(1/\delta)]}
{(1+\|B\|^2\bar u)\,\varepsilon^2\,J_A^*}.
\]

2. **Achievability.** For every \(\varepsilon>0\), \(\delta\in(0,1)\), and deterministic initialization horizon \(t_0\ge2\) such that
\[
\varepsilon_{t_0}\le\|\Gamma_\infty(A)\|^{-3/2}/4,
\]
the two-phase procedure obeys \(\mathbb P_A(\|\widehat A_t-A\|>\varepsilon)\le\delta\) for every integer \(t\ge t_0\) satisfying
\[
\begin{aligned}
t\ge{}&1+\frac{C}{J_A^*}\max\{\varepsilon^{-2},\bar\gamma\}\,[\log(2/\delta)+n_x]\\
&+\frac{\|\Gamma_\infty(A)\|^2}{J_A^*}\Big[C_1(t-1)\varepsilon_{t_0}+C_2t_0+C_2(t-1)(1-\|\Gamma_\infty(A)\|^{-1})^{t-1}\\
&\hspace{40mm}+C_2(\|\Gamma_\infty(A)\|-1)\Big],
\end{aligned}
\]
where
\[
\bar\gamma=(1+\|B\|^2\bar u)\left(\sum_{k=0}^{\infty}\|A^k\|\right)^2,
\quad C=c'K^4,
\quad C_1=64(1+\|B\|^2\bar u)\|\Gamma_\infty(A)\|,
\quad C_2=1+\|B\|^2\bar u.
\]
In addition, the procedure satisfies \(\mathbb E_A\|u_t\|^2\le\bar u\) at every time.
