# Problem

## Setup

Fix a finite horizon \(N\ge 1\), tolerance \(\epsilon>0\), coefficient \(a\in(0,1)\), initial value \(z_0\in\mathbb R\), and real inputs \(X_1,\ldots,X_N\). Define
\[
z_t=a z_{t-1}+(1-a)X_t,
\qquad 1\le t\le N,
\]
and, for each \(\gamma>0\), define the time-warped trajectory
\[
\widetilde z_t=a^\gamma\widetilde z_{t-1}+(1-a^\gamma)X_t,
\qquad \widetilde z_0=z_0.
\]

Let \(\sigma(u)=1/(1+e^{-u})\) and \(\operatorname{logit}(v)=\ln(v/(1-v))\) for \(v\in(0,1)\). A one-unit linear-activation LSTM is defined by
\[
f_t=\sigma(W_fX_t+U_fh_{t-1}+b_f),\quad
 i_t=\sigma(W_iX_t+U_ih_{t-1}+b_i),\quad
 o_t=\sigma(W_oX_t+U_oh_{t-1}+b_o),
\]
\[
g_t=W_gX_t+U_gh_{t-1}+b_g,\qquad
c_t=f_tc_{t-1}+i_tg_t,\qquad h_t=o_tc_t,
\]
with \(c_0=z_0\) and any fixed \(h_0\).

## Task

Prove that there exists a single base parameter setting \(\theta\) such that
\[
\max_{1\le t\le N}|z_t-h_t|<\epsilon,
\]
and, simultaneously for every \(\gamma>0\), replacing only its forget- and input-gate biases by
\[
 b_f\leftarrow\operatorname{logit}(a^\gamma),\qquad
 b_i\leftarrow\operatorname{logit}(1-a^\gamma)
\]
produces a setting \(\theta_\gamma\) satisfying
\[
\max_{1\le t\le N}|\widetilde z_t-h_t^{(\gamma)}|<\epsilon.
\]
All other weights, recurrent weights, biases, and the initial state remain unchanged.
