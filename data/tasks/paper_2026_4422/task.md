# Problem

## Setup

Let \(d,T\) be positive integers. Let \(A\in\mathbb R^{d\times d}\) be a fixed unknown positive semidefinite matrix of rank \(1\le r\le d\), and let \(\sigma_+>0\) be its smallest positive eigenvalue. The learner is supplied with \(r,\sigma_+,T\), and a noise-cap parameter \(\bar\eta>0\), but not with A.

Let \((v_t)_{t=0}^T\) be an integrable \(\mathbb R^d\)-valued martingale for its natural filtration \(\mathcal F_t=\sigma(v_0,\ldots,v_t)\). Write \(\delta_t=v_t-v_{t-1}\). Assume the increments have finite second moments and
\[
\mathbb E[\delta_t\delta_t^\top]\preceq\Sigma,\qquad 1\le t\le T,
\]
for a fixed finite positive semidefinite matrix \(\Sigma\). This is an unconditional second-moment bound; independence of the increments is not assumed.

The initial minimizer \(v_0\) is observed, and \(x_0=v_0\). At round t the learner observes \(v_t\), chooses \(x_t\in\mathbb R^d\), and then receives
\[
y_t=\tfrac12(x_t-v_t)^\top A(x_t-v_t)+\eta_t,
\qquad |\eta_t|\le\bar\eta.
\]
The feedback noise may be random or adversarial but is causal. Explicitly, it may be any measurable function of A, the minimizers observed through t, the learner's actions and probes through t, the previous feedback, and auxiliary random variables \(U_1,\ldots,U_t\). The sequence \((U_t)\) is independent of the entire minimizer process and the exploration probes. Neither future minimizers nor future probes are available to this function.

For an action sequence define
\[
\operatorname{Cost}_T(x)=\sum_{t=1}^T\left[
\tfrac12(x_t-v_t)^\top A(x_t-v_t)
+\tfrac12\|x_t-x_{t-1}\|_2^2\right].
\]
Let
\[
J_T^*(A)=\inf_\pi\mathbb E[\operatorname{Cost}_T(x^\pi)],
\]
where the infimum is over measurable causal policies with knowledge of A, initial state \(v_0\), and access at time t to \(v_0,\ldots,v_t\). Independent randomization is permitted, but future minimizers are not available.

## Algorithm

Let \(c_1\) be a positive integer constant, set \(m=c_1rd\), and suppose \(m<T\). Put
\[
\gamma^2=\begin{cases}
\sqrt{\bar\eta}\max\{(T-m)^{2/3},2/\sigma_+\},&r<d,\\
\sqrt{\bar\eta}\max\{(T-m)^{1/2},2/\sigma_+\},&r=d,
\end{cases}
\]
and take \(\gamma>0\).

For \(1\le t\le m\), draw independent probes \(z_t\sim N(0,I_d)\), independent of the entire minimizer process and the auxiliary feedback randomization. The learner accesses \(z_t\) only at its exploration round. Play
\[
x_t=v_t+\gamma z_t,\qquad \widetilde y_t=y_t/\gamma^2.
\]
After round m, choose a measurable minimizer
\[
\widehat A\in\operatorname*{argmin}_{M\succeq0}\operatorname{tr}(M)
\quad\text{subject to}\quad
\sum_{t=1}^m\left|\widetilde y_t-\tfrac12\langle M,z_tz_t^\top\rangle\right|
\le m\bar\eta/\gamma^2,
\]
where \(\langle M,N\rangle=\operatorname{tr}(M^\top N)\). Any measurable tie-breaking rule based only on the observations and probes available through m is allowed.

Set \(\widehat C_{T+1}=I_d\) and compute, backwards for \(t=T,\ldots,1\),
\[
\widehat C_t^{-1}=2I_d+\widehat A-\widehat C_{t+1}.
\]
Using the already observed minimizers, compute auxiliary states
\[
w_0=v_0,\qquad
w_t=\widehat C_t w_{t-1}+(I_d-\widehat C_t)v_t,
\quad 1\le t\le m.
\]
These auxiliary states do not replace the actions actually played during exploration. Play
\[
x_{m+1}=\widehat C_{m+1}w_m+(I_d-\widehat C_{m+1})v_{m+1},
\]
and then, for \(t=m+2,\ldots,T\), play
\[
x_t=\widehat C_t x_{t-1}+(I_d-\widehat C_t)v_t.
\]
In particular, the switching cost at round \(m+1\) is measured from the actual exploration action \(x_m\).

Write \(Z=(z_1,\ldots,z_m)\). The random performance quantity in the claim is
\[
\operatorname{Regret}_T(Z)
=\mathbb E[\operatorname{Cost}_T(x)\mid Z]-J_T^*(A).
\]
Thus the cost expectation averages over the minimizer process and feedback randomization, while the probability in the claim is over Z. Conditioning in this definition does not give a policy access to future observations or future probes.

## Task

Prove that there exist universal constants \(c_1\in\mathbb N\) and \(C_0>0\) such that the algorithm above has the following property. There are positive constants \(\alpha_1,\alpha_2,\beta_1,\beta_2\), depending only on \(\bar\eta\), the positive spectrum of A, \(\Sigma\), and d, for which, for every horizon with \(m<T\), every minimizer process satisfying the stated assumptions, and every admissible feedback-noise rule,
\[
\mathbb P_Z\!\left\{
\operatorname{Regret}_T(Z)\le
\begin{cases}
\alpha_1(T-c_1rd)^{2/3}+\alpha_2,&r<d,\\
\beta_1(T-c_1d^2)^{1/2}+\beta_2,&r=d
\end{cases}
\right\}\ge1-\exp(-C_0m).
\]
The coefficient constants must not depend on T or on additional distributional features of the minimizer process or feedback noise.
