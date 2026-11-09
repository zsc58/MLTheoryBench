# Reference Proof

## Proof Structure and Obligations

1. Handle the zero-step case and derive a quantified descent inequality from oracle feasibility, strong convexity, and smoothness.
2. Telescope that inequality to obtain the stated average and minimum bounds. Under summable oracle errors, establish square-summability and hence convergence of individual gaps to zero.
3. In the separate exact squared-loss regime, derive residual monotonicity and the correct consecutive-update identity directly from the orthogonal-projector properties.
4. Establish the contraction factor and its geometric consequences, including the endpoint kappa=0.

All obligations are proved below; no specialized external result is required.

## Complete Proof

Write delta_t=f_{t+1}-f_t. Vector norms are Euclidean and matrix norms are their induced operator norms.

### General inexact regime

If eta=0, every delta_t is zero, so all the general-regime conclusions hold. Now assume eta>0.

Since theta=0 is feasible in the oracle minimization,
\[
V(f_t+h_t)\le V(f_t)+\varepsilon_t.
\]
Strong convexity on the full-update segment gives
\[
V(f_t+h_t)\ge V(f_t)+\langle\nabla V(f_t),h_t\rangle+\frac m2\|h_t\|^2.
\]
Consequently,
\[
\langle\nabla V(f_t),h_t\rangle\le\varepsilon_t-\frac m2\|h_t\|^2.
\]
Smoothness on the actual-update segment yields
\[
\begin{aligned}
V(f_{t+1})
&\le V(f_t)+\eta\langle\nabla V(f_t),h_t\rangle+\frac{L\eta^2}{2}\|h_t\|^2\\
&\le V(f_t)+\eta\varepsilon_t-\frac{\eta(m-L\eta)}2\|h_t\|^2.
\end{aligned}
\]
Since delta_t=eta h_t and eta<=m/(2L),
\[
\frac{m}{4\eta}\|\delta_t\|^2
\le V(f_t)-V(f_{t+1})+\eta\varepsilon_t. \tag{1}
\]
Summing and using V(f_T)>=0 gives, for every integer T>=1,
\[
\sum_{t=0}^{T-1}\|\delta_t\|^2
\le\frac{4\eta}{m}\left(V(f_0)+\eta\sum_{t=0}^{T-1}\varepsilon_t\right). \tag{2}
\]
Cauchy–Schwarz now gives
\[
\begin{aligned}
\min_{0\le t<T}\|\delta_t\|
&\le\frac1T\sum_{t=0}^{T-1}\|\delta_t\|\\
&\le\sqrt{\frac1T\sum_{t=0}^{T-1}\|\delta_t\|^2}\\
&\le\sqrt{\frac{4\eta}{mT}\left(V(f_0)+\eta\sum_{t=0}^{T-1}\varepsilon_t\right)}.
\end{aligned}
\]
If E:=sum_{t=0}^infinity epsilon_t is finite, the average and minimum are bounded by C/sqrt(T), where C=sqrt((4 eta/m)(V(f_0)+eta E)) is independent of T. Moreover, (2) bounds every partial sum of the nonnegative series sum_t ||delta_t||^2 by C^2. Thus that series converges and ||delta_t|| tends to zero. This last conclusion is an individual-gap convergence statement, not an individual-gap O(t^{-1/2}) rate.

### Exact squared-loss regime

This part uses its own stepsize assumption 0<eta<=1, not the general regime's more restrictive bound. Put r_t=y-f_t and A_t=A(f_t). Then
\[
\delta_t=\eta A_t r_t,\qquad r_{t+1}=(I-\eta A_t)r_t.
\]
The Moore–Penrose identities give A_t^T=A_t and A_t^2=A_t. In particular, A_t r_t and (I-A_t)r_t are orthogonal. Therefore
\[
\begin{aligned}
\|r_{t+1}\|^2
&=\|(I-A_t)r_t\|^2+(1-\eta)^2\|A_t r_t\|^2\\
&=\|r_t\|^2-\eta(2-\eta)\|A_t r_t\|^2\\
&\le\|r_t\|^2.
\end{aligned}
\]
It follows inductively that ||r_t||<=||r_0|| for every t.

Idempotence also gives
\[
\eta A_t r_{t+1}
=\eta A_t(I-\eta A_t)r_t
=(1-\eta)\delta_t.
\]
Adding and subtracting eta A_t r_{t+1} in the next update proves the correct identity
\[
\begin{aligned}
\delta_{t+1}
&=\eta A_{t+1}r_{t+1}\\
&=(1-\eta)\delta_t+\eta(A_{t+1}-A_t)r_{t+1}. \tag{3}
\end{aligned}
\]
Equivalently, the last term is eta(A_{t+1}-A_t)(I-eta A_t)r_t. It cannot generally be replaced by eta(A_{t+1}-A_t)r_t.

Since 1-eta>=0, the triangle inequality, the assumed Lipschitz bound, and residual monotonicity imply
\[
\begin{aligned}
\|\delta_{t+1}\|
&\le(1-\eta)\|\delta_t\|+\eta\|A_{t+1}-A_t\|\,\|r_{t+1}\|\\
&\le\left(1-\eta+\eta L_A\|r_0\|\right)\|\delta_t\|\\
&=\kappa\|\delta_t\|.
\end{aligned}
\]
Reindexing gives the requested inequality for every t>=1.

Here kappa>=0. If 0<kappa<1, induction yields ||delta_t||<=kappa^t||delta_0||. For integers s>t,
\[
\|f_s-f_t\|\le\sum_{j=t}^{s-1}\|\delta_j\|
\le\frac{\kappa^t}{1-\kappa}\|\delta_0\|.
\]
Thus f_t is Cauchy in R^n, converges to some f_infinity, and satisfies
\[
\|f_\infty-f_t\|\le\frac{\kappa^t}{1-\kappa}\|\delta_0\|.
\]
If kappa=0, the recurrence gives delta_t=0 for every t>=1, so f_t=f_1 for every t>=1. This is finite termination and covers the remaining geometric-convergence endpoint. Zero initial residuals, zero initial updates, and zero-rank projectors require no division and are included in these arguments.
