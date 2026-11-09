# Problem

## Setup

Let \(T,M\) be positive integers, and let \(B_y,B_z,R\in[0,\infty)\). At each round \(t=1,\ldots,T\), a vector of causal base forecasts \(z_t\in\mathbb R^M\) is available before the outcome \(y_t\in\mathbb R\) is revealed. Here causal means that the forecasts use only information available before observing \(y_t\), including previously revealed outcomes and current-period inputs already available, without access to unrevealed outcomes. The aggregate prediction is issued before observing \(y_t\), and the states and cumulative regrets are updated afterward.

Assume \(|y_t|\le B_y\). Set \(\widetilde z_t=(z_t^\top,1)^\top\in\mathbb R^d\), where \(d=M+1\), and assume \(\|\widetilde z_t\|_2\le B_z\). Let \(H=\{h_1,\ldots,h_K\}\subset[2,\infty)\) be a nonempty finite set with \(K=|H|\), let \(\delta>0\), and set \(\gamma_h=1-1/h\).

For every \(h\in H\), define
\[
A^{(h)}_0=\delta I_d,\quad b^{(h)}_0=0,\quad v^{(h)}_1=0,
\]
\[
A^{(h)}_t=\gamma_hA^{(h)}_{t-1}+\widetilde z_t\widetilde z_t^\top,\quad
b^{(h)}_t=\gamma_hb^{(h)}_{t-1}+y_t\widetilde z_t,\quad
v^{(h)}_{t+1}=(A^{(h)}_t)^{-1}b^{(h)}_t
\qquad (t=1,\ldots,T).
\]
The idealized scale prediction is \(a_t^{(h)}=\widetilde z_t^\top v_t^{(h)}\). Assume \(\|v_t^{(h)}\|_2\le R\) for every \(t=1,\ldots,T\) and \(h\in H\).

Let \(f_{t,j}=z_{t,j}\) for \(j=1,\ldots,M\) denote the raw base forecasts. Fix \(B\in[0,\infty)\) such that \(|y_t|\le B\) for every \(t\), and define
\[
\operatorname{clip}_B(a)=\max\{-B,\min\{a,B\}\}.
\]
The pool consists of the clipped raw forecasts and clipped scale predictions:
\[
\widetilde y_{t,j}=\operatorname{clip}_B(f_{t,j})\quad(1\le j\le M),\qquad
\widetilde y_{t,M+k}=\operatorname{clip}_B(a_t^{(h_k)})\quad(1\le k\le K).
\]
Set \(N=M+K\), define \([x]_+=\max\{x,0\}\), and use
\[
\widehat y_t=\sum_{j=1}^Np_{t,j}\widetilde y_{t,j},\qquad
r_{t,j}=2(\widehat y_t-y_t)(\widehat y_t-\widetilde y_{t,j}),
\]
\[
R_{t-1,j}=\sum_{s=1}^{t-1}r_{s,j},\qquad
p_{t,j}=\frac{[R_{t-1,j}]_+}{\sum_{i=1}^N[R_{t-1,i}]_+},
\]
with \(p_{t,j}=1/N\) when the denominator is zero.

For a scalar sequence \(a\), let \(L_T(a)=\sum_{t=1}^T(a_t-y_t)^2\). For a comparator path \(u_{1:T}\in(\mathbb R^d)^T\), let
\[
L_T(u_{1:T})=\sum_{t=1}^T(\widetilde z_t^\top u_t-y_t)^2,\qquad
P_T(u_{1:T})=\sum_{t=2}^T\|u_t-u_{t-1}\|_2,
\]
and assume \(\|u_t\|_2\le R\) for all \(t=1,\ldots,T\). Define \(D=B_y+B_zR\) and, for \(h\in H\),
\[
\Psi_h(T,P)=\delta R^2+D^2d\log(1+B_z^2h/\delta)+\frac{2D^2dT}{h}+4R(\delta+B_z^2h)P.
\]

## Task

Prove that there is a universal constant \(C>0\) such that
\[
L_T(\widehat y)\le \min\!\left\{\min_{1\le j\le M}L_T(\widetilde y_{\cdot,j}),\; L_T(u_{1:T})+\min_{h\in H}\Psi_h\bigl(T,P_T(u_{1:T})\bigr)\right\}+CB^2\sqrt{T(M+K)}
\]
for every admissible forecast and outcome sequence and every comparator path satisfying the stated bound. Here \(\widetilde y_{\cdot,j}\) denotes the corresponding clipped raw sequence in the first minimum.
