# Reference Proof

## Proof Structure

Establish the exact stochastic-policy Bellman error representation, derive the mean/transverse recursion, prove convexification invariance and the projected rate bound, identify the augmented-family JSR by its products, and lift the projected estimates to the full error.

## Complete Proof

### 1. Exact Bellman error representation

Fix any Q and write e=Q-Q^\star. For each state s, choose actions i maximizing Q(s,\cdot) and j maximizing Q^\star(s,\cdot), and put
\[
\delta_s=\max_b Q(s,b)-\max_b Q^\star(s,b).
\]
The maximizing properties give
\[
e(s,j)\le\delta_s\le e(s,i).
\]
If the endpoints differ, express \delta_s as their convex combination; if they coincide, either endpoint suffices. Thus there is a probability vector \mu_Q(\cdot\mid s) such that
\[
\delta_s=\sum_b\mu_Q(b\mid s)e(s,b).
\]
Doing this separately at every state defines a stochastic stationary policy. Subtracting the Bellman fixed-point equation yields
\[
F(Q)-Q^\star=A_{\mu_Q}(Q-Q^\star),\qquad F(Q)-Q=(A_{\mu_Q}-I)e.
\]
This is an algebraic existence statement for each Q, not an assumption that the algorithm observes Q^\star or samples this policy. Every A_\mu is nonnegative with row sums \gamma, so A_\mu\mathbf1=\gamma\mathbf1.

### 2. Exact deflated coordinates

Let
\[
e_k=Q_k-Q^\star,\quad z_k=\Pi_\perp e_k,\quad a_k=n^{-1}\mathbf1^Te_k.
\]
Then e_k=a_k\mathbf1+z_k and \mathbf1^Tz_k=0. Choose \mu_k from step 1 at Q_k. The error update is
\[
e_{k+1}=A_{\mu_k}e_k+\frac{\gamma}{1-\gamma}\bar r_k\mathbf1.
\]
Projection and A_{\mu_k}\mathbf1=\gamma\mathbf1 give
\[
z_{k+1}=\Pi_\perp A_{\mu_k}z_k=\bar A_{\mu_k}z_k.
\]
Write t_k=n^{-1}\mathbf1^TA_{\mu_k}z_k. The residual identity gives
\[
\bar r_k=(\gamma-1)a_k+t_k.
\]
Taking means in the error update therefore yields
\[
a_{k+1}=\gamma a_k+t_k+\frac{\gamma}{1-\gamma}\bigl((\gamma-1)a_k+t_k\bigr)
=\frac{t_k}{1-\gamma}=\ell_{\mu_k}z_k.
\]
Thus, on \mathbb R\oplus H,
\[
(a_{k+1},z_{k+1})=D_{\mu_k}(a_k,z_k).
\]
In particular, if z_0=0, both coordinates are zero after the first update and remain zero.

### 3. Stochastic-policy convexification

Let \Theta be the finite set of deterministic policies. For a stochastic policy \mu define
\[
\lambda_\pi=\prod_{s\in\mathcal S}\mu(\pi(s)\mid s),\qquad \pi\in\Theta.
\]
These coefficients are nonnegative, sum to one, and satisfy
\[
\sum_{\pi:\pi(s)=b}\lambda_\pi=\mu(b\mid s).
\]
The formula defining B_\mu then gives
\[
A_\mu=\sum_{\pi\in\Theta}\lambda_\pi A_\pi,\qquad
\bar A_\mu=\sum_{\pi\in\Theta}\lambda_\pi\bar A_\pi.
\]
Conversely, any convex combination of deterministic policies defines a stochastic policy by taking the same convex combination of their action probabilities, and the corresponding matrices have the same affine relation. Consequently
\[
\{\bar A_\mu:\mu\text{ stochastic}\}=\operatorname{co}\{\bar A_\pi:\pi\in\Theta\}.
\]
For completeness, a product of m convex combinations of a finite matrix family expands into a convex combination of length-m products from that family: the coefficients are products of the individual weights and sum to one. The triangle inequality bounds its norm by the maximum norm of the original length-m products. The reverse comparison follows from inclusion of the original family. Hence the two finite-length suprema are equal, and taking mth roots and limits proves convexification invariance. In particular, the stochastic projected family has JSR \bar\rho.

### 4. The projected rate is at most gamma

For each deterministic policy, A_\pi\mathbf1=\gamma\mathbf1 implies
\[
\Pi_\perp A_\pi(I-\Pi_\perp)=0,
\qquad \Pi_\perp A_\pi\Pi_\perp=\Pi_\perp A_\pi.
\]
Induction therefore gives, for m\ge1,
\[
\bar A_{\pi_{m-1}}\cdots\bar A_{\pi_0}
=\Pi_\perp A_{\pi_{m-1}}\cdots A_{\pi_0}\Pi_\perp
\]
when the projected factors are represented on the ambient space. Since \|A_\pi\|_\infty=\gamma, the ambient product on the right has infinity norm at most
\[
\|\Pi_\perp\|_\infty^2\gamma^m.
\]
Its restriction to H consequently has Euclidean operator norm at most
\[
\sqrt n\,\|\Pi_\perp\|_\infty^2\gamma^m,
\]
using \|x\|_\infty\le\|x\|_2 and \|x\|_2\le\sqrt n\|x\|_\infty. Taking maximum norms over words and then mth roots proves \bar\rho\le\gamma. If H=\{0\}, every projected operator has norm zero and the conclusion holds directly.

### 5. Uniform product estimates and augmented JSR

Let M_m be the supremum of Euclidean norms of length-m products from the stochastic projected family for m\ge1, and set M_0=1 as a bound for the empty product. The families are bounded: row stochasticity gives \|A_\mu\|_2\le\gamma\sqrt n, and projection cannot increase the Euclidean norm. By the JSR definition and step 3,
\[
\lim_{m\to\infty}M_m^{1/m}=\bar\rho.
\]
Thus for every q>\bar\rho there is an integer N\ge1 such that M_m\le q^m for m\ge N. Taking
\[
c_q=\max\left\{1,\max_{0\le m<N}M_mq^{-m}\right\}
\]
gives M_m\le c_qq^m for all m\ge0.

The nonnegative ambient row vector \mathbf1^TA_\mu has total mass \gamma n. Its restriction to H has norm no greater than its ambient Euclidean norm, so
\[
\|\ell_\mu|_H\|_2\le\frac{\|\mathbf1^TA_\mu\|_2}{n(1-\gamma)}
\le\frac{\|\mathbf1^TA_\mu\|_1}{n(1-\gamma)}
=\frac{\gamma}{1-\gamma}=:L.
\]
For a word \mu_0,\ldots,\mu_{m-1}, put P_j=\bar A_{\mu_{j-1}}\cdots\bar A_{\mu_0}, with P_0=I_H. Direct multiplication gives, for m\ge1,
\[
D_{\mu_{m-1}}\cdots D_{\mu_0}
=\begin{bmatrix}0&\ell_{\mu_{m-1}}P_{m-1}\\0&P_m\end{bmatrix}.
\]
The Euclidean product norm on \mathbb R\oplus H is at least \|P_m\|_2, by applying the product to inputs (0,z). It is at most
\[
L\|P_{m-1}\|_2+\|P_m\|_2
\le c_q(L+q)q^{m-1}.
\]
Taking suprema and mth roots proves
\[
\bar\rho\le\rho_{\rm def}\le q.
\]
Letting q decrease to \bar\rho gives \rho_{\rm def}=\bar\rho\le\gamma. This also covers \bar\rho=0 by using every q>0. When H=\{0\}, D_\mu is the zero operator on its scalar coordinate, and the same conclusion holds directly.

### 6. Full-error estimate and asymptotic rate

Fix \varepsilon\in(0,1-\bar\rho), and set \beta=\bar\rho+\varepsilon\in(0,1). The uniform bound in step 5 applies to every stochastic-policy word, including the policies selected along any actual trajectory. Hence
\[
\|z_m\|_2\le c_\beta\beta^m\|z_0\|_2\qquad(m\ge0).
\]
For k\ge1, the scalar recursion gives
\[
|a_k|\le L\|z_{k-1}\|_2\le Lc_\beta\beta^{k-1}\|z_0\|_2.
\]
Therefore
\[
\|e_k\|_2\le\sqrt n|a_k|+\|z_k\|_2
\le c_\beta(\sqrt nL+\beta)\beta^{k-1}\|z_0\|_2.
\]
The positive constant C_\beta=c_\beta(\sqrt nL+\beta) depends only on the fixed matrix family, dimension, discount, and \beta, and is independent of Q_0 and k. This proves the requested estimate with z_0=\Pi_\perp(Q_0-Q^\star).

If z_0=0, step 2 gives e_k=0 for all k\ge1, including the case n=1. Otherwise taking kth roots gives
\[
\limsup_{k\to\infty}\|e_k\|_2^{1/k}\le\beta.
\]
This holds for every permitted \varepsilon, so letting \varepsilon\downarrow0 gives the bound by \bar\rho, including when \bar\rho=0. The bound is strictly below \gamma whenever \bar\rho<\gamma.

## Proof-Obligation Closure

All theorem-critical obligations are derived above. Steps 1–2 recover the source's exact representation and cancellation calculations; steps 3–5 explicitly establish the finite-family convexification argument, projected bound, uniform product estimate, and the relevant triangular-family JSR identity; step 6 proves the full-error and limit statements. No specialized external result is used as an unproved substitute for these obligations.
