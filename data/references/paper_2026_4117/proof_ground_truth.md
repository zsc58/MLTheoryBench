# Reference Proof

## Proof Structure

Parameter containment and optimism reduce regret to directional supports. Minimum-volume enclosing ellipsoids of regularized error sets bound those supports by directional widths. Explicit enclosing ellipsoids for half-space cuts yield a telescoping volume decrease. Fresh boundary-visiting noise and a martingale calculation control truncated large widths. Finally, a direct bound on the supports removes truncation without requiring a uniform bound on MVEE widths.

## Complete Proof

Fix the deterministic values of $\delta,\mu,\xi$ in the task. All assertions below are on the probability-one event where the finitely many noise and context bounds hold. If $L=0$, every reward mean and every regret increment is zero, so the result is immediate. Hence assume $L>0$.

### 1. Parameter containment and support reduction

The true parameter satisfies every observed constraint because
\[
|r_{t,a_t}-\theta_*^\top X_{t,a_t}|=|\eta_t|\le\eta_{\max}.
\]
Thus $\theta_*\in\Theta_t$ for every $t$, including $t=0$. The uncertainty sets are nonempty compact convex sets, so each finite-arm maximization attains its maximum.

Write $x_t=X_{t,a_t}$, $x_t^*=X_{t,a_t^*}$, and $\Gamma_t=\Theta_t-\theta_*$. Optimism gives
\[
\theta_*^\top x_t^*-\theta_*^\top x_t
\le(\theta_t-\theta_*)^\top x_t
\le h_t,
\qquad h_t:=\sup_{\gamma\in\Gamma_{t-1}}x_t^\top\gamma.
\]
Consequently $R(T)\le\sum_t h_t$. Since $0\in\Gamma_t$ and $\Gamma_t\subseteq[-2S,2S]^d$,
\[
0\le h_t\le 2SL\sqrt d. \tag{1}
\]
The exact error-set update is
\[
\Gamma_t=\Gamma_{t-1}\cap\{-b_t\le x_t^\top\gamma\le b'_t\},
\quad b_t=\eta_{\max}-\eta_t,\quad b'_t=\eta_{\max}+\eta_t.
\]

### 2. Regularized ellipsoids and their potential

Let $B_2^d$ be the Euclidean unit ball and define $K_t=\Gamma_t+\mu B_2^d$. These are compact convex bodies containing $\mu B_2^d$. Use the standard minimum-volume enclosing ellipsoid existence-and-uniqueness theorem: every compact convex set with nonempty interior has a unique minimum-volume enclosing ellipsoid. Its hypotheses hold here because $\mu>0$. Write that ellipsoid as
\[
E_t=\{c_t+B_t^{1/2}y:\|y\|_2\le1\},\qquad B_t\succ0,
\]
and put $\Phi_t=\log\operatorname{Vol}(E_t)$ and $W_t=2\sqrt{x_t^\top B_{t-1}x_t}$.

These quantities have the required measurability. One elementary justification is to relax the finitely many defining inequalities of $\Gamma_t$ by $1/n$, including its box constraints. The resulting compact sets decrease to $\Gamma_t$; their support functions are measurable, as suprema over rational points in their interiors, and converge to the support function of $\Gamma_t$. Adding $\mu B_2^d$ preserves this measurability. The MVEE depends continuously on a compact convex body in the Hausdorff metric when the bodies contain a common positive-radius ball and have a common finite outer bound. To see this, every enclosing ellipsoid has each semiaxis at least the inner radius; the volume upper bound supplied by the outer ball then bounds its other semiaxes and its center. Subsequence compactness, enclosure in the limit, and comparison with arbitrarily small dilations of a candidate limiting ellipsoid show that any subsequential limit is minimizing. Uniqueness identifies the limit. This establishes the needed measurable dependence. In particular, $c_{t-1},B_{t-1},x_t,W_t$ are $\mathcal F_{t-1}$-measurable.

Set $\alpha_t=x_t^\top c_{t-1}$ and $\rho_t=\sqrt{x_t^\top B_{t-1}x_t}$. The extreme projections of $E_{t-1}$ are $\alpha_t\pm\rho_t$. Since $0\in E_{t-1}$, $|\alpha_t|\le\rho_t$, and hence
\[
h_t\le\alpha_t+\rho_t\le2\rho_t=W_t. \tag{2}
\]

Let $A=2S\sqrt d+\mu$. The initial set satisfies
\[
K_0=([-S,S]^d-\theta_*)+\mu B_2^d\subseteq A B_2^d,
\]
whereas $K_T\supseteq\mu B_2^d$. Comparing enclosing volumes gives
\[
\Phi_0-\Phi_T\le d\log(A/\mu). \tag{3}
\]
Also $K_t\subseteq K_{t-1}$, so their minimum enclosing volumes are nonincreasing. This is volume monotonicity, not containment or directional-width monotonicity of the ellipsoids.

### 3. Explicit half-space volume estimate

Consider $E=\{c+B^{1/2}y:\|y\|_2\le1\}$ and $H=\{\gamma:x^\top\gamma\le u\}$ with $x\ne0$. Put $r=\sqrt{x^\top Bx}$ and $q=(u-x^\top c)/r$. The affine transformation $y=B^{-1/2}(\gamma-c)$ followed by a rotation of the unit vector $B^{1/2}x/r$ to $e_1$ transforms $E\cap H$ into the truncated unit ball $\{\|y\|_2\le1,y_1\le q\}$.

For $-1<q<1/d$, define
\[
m=\frac{dq-1}{d+1},\qquad a=\frac{d(1+q)}{d+1},\qquad b^2=\frac{d^2(1-q^2)}{d^2-1}.
\]
The ellipsoid centered at $me_1$, with axial radius $a$ and orthogonal radius $b$, encloses this truncated ball. Indeed, for $-1\le s\le q$,
\[
1-\left(\frac{(s-m)^2}{a^2}+\frac{1-s^2}{b^2}\right)
=\frac{2(d+1)(q-s)(1+s)(1-dq)}{d^2(1-q)(1+q)^2}\ge0.
\]
Its volume ratio to the unit ball is
\[
R_d(q)=\frac{d(1+q)}{d+1}\left(\frac{d^2(1-q^2)}{d^2-1}\right)^{(d-1)/2}.
\]
Thus a minimum enclosing ellipsoid of $E\cap H$ has volume at most $R_d(q)\operatorname{Vol}(E)$. No claim of exact optimality of the constructed ellipsoid is needed.

Since
\[
\frac{d}{dq}\log R_d(q)=\frac{1-dq}{1-q^2}>0\quad(-1<q<1/d),
\]
a cut with $q\le\xi/d$ decreases log minimum enclosing volume by at least $\Omega:=-\log R_d(\xi/d)$. Moreover,
\[
\begin{aligned}
\Omega&=\log\frac{d+1}{d+\xi}-\frac{d-1}{2}\log\frac{d^2-\xi^2}{d^2-1}\\
&\ge\frac{1-\xi}{d+1}-\frac{d-1}{2}\frac{1-\xi^2}{d^2-1}
=\frac{(1-\xi)^2}{2(d+1)}.
\end{aligned} \tag{4}
\]
Here the two estimates are $-\log(1-z)\ge z$ for $0\le z<1$ and $\log(1+z)\le z$ for $z>-1$.

### 4. Regularized cuts and the pathwise count

For $x_t\ne0$ define
\[
q_t^+=\frac{b'_t+\mu L-\alpha_t}{\rho_t},\qquad
q_t^-=\frac{b_t+\mu L+\alpha_t}{\rho_t},
\qquad I_t=\mathbf1\{q_t^+\le\xi/d\text{ or }q_t^-\le\xi/d\}.
\]
If $x_t=0$, set $I_t=0$; then $h_t=W_t=0$ and no normalized offset is needed.

Every $z\in K_t$ can be written as $\gamma+v$ with $\gamma\in\Gamma_t$ and $\|v\|_2\le\mu$. Therefore
\[
x_t^\top z\le b'_t+\mu L,\qquad -x_t^\top z\le b_t+\mu L.
\]
Thus $K_t$ is contained in $E_{t-1}$ intersected with either relaxed half-space. Each such intersection contains the full-dimensional set $K_t$, so its normalized offset is strictly greater than $-1$. The preceding cut estimate applies whenever $I_t=1$. On all other rounds volume monotonicity applies. Consequently
\[
\Phi_{t-1}-\Phi_t\ge\Omega I_t,
\qquad
\sum_{t=1}^T I_t\le\frac{d}{\Omega}\log(A/\mu). \tag{5}
\]
This includes the first round.

### 5. Boundary probabilities and concentration

Define
\[
w_\mu=\frac{4d\mu L}{\xi}>0,\qquad w_\xi=\frac{4d\epsilon_0}{\xi},\qquad
j_t=\mathbf1\{W_t\ge w_\mu\}I_t,\qquad p_t=\mathbb E[j_t\mid\mathcal F_{t-1}].
\]
On a large-width round, $x_t\ne0$. The events defining $I_t$ are respectively
\[
\eta_t\le-\eta_{\max}+u_t,
\qquad \eta_t\ge\eta_{\max}-v_t,
\]
where
\[
u_t=\alpha_t+\frac{\xi\rho_t}{d}-\mu L,
\qquad v_t=\frac{\xi\rho_t}{d}-\alpha_t-\mu L.
\]
Their sum satisfies
\[
u_t+v_t=\frac{\xi W_t}{d}-2\mu L\ge\frac{\xi W_t}{2d}.
\]
Hence at least one of $u_t,v_t$ is at least $\xi W_t/(4d)$. These thresholds and the choice of which one is larger are predictable. Independence of $\eta_t$ from $\mathcal F_{t-1}$ and the appropriate boundary assumption, applied at $\min\{\epsilon_0,\xi W_t/(4d)\}$, give
\[
p_t\ge\mathbf1\{W_t\ge w_\mu\}c_0\min\{\epsilon_0,\xi W_t/(4d)\}. \tag{6}
\]

For completeness, here is the required concentration argument. For any adapted indicators $j_t$ and their predictable means $p_t$, put $P_T=\sum_t p_t$ and $J_T=\sum_t j_t$. The conditional Bernoulli formula gives
\[
\mathbb E[\exp(3p_t/8-3j_t/4)\mid\mathcal F_{t-1}]
=e^{3p_t/8}(1-p_t+p_t e^{-3/4})
\le\exp\{p_t(3/8+e^{-3/4}-1)\}\le1.
\]
For the last inequality, $e^{3/4}\ge1+3/4>8/5$, so $e^{-3/4}<5/8$. Products of these factors form a nonnegative supermartingale starting at one. Markov's inequality therefore yields, with probability at least $1-\delta$,
\[
\frac38 P_T-\frac34 J_T\le\log(1/\delta),
\qquad P_T\le2J_T+\frac83\log(1/\delta). \tag{7}
\]
Since $J_T\le\sum_t I_t$, equations (5)--(7), multiplied by $4d/(c_0\xi)$, give on that same event
\[
\sum_{t:W_t\ge w_\mu}\min\{W_t,w_\xi\}
\le\frac{8d^2}{c_0\xi\Omega}\log(A/\mu)
+\frac{32d}{3c_0\xi}\log(1/\delta). \tag{8}
\]

### 6. Remove truncation from supports and conclude

Put $M=2LA=2L(2S\sqrt d+\mu)$. Equations (1)--(2) imply $h_t\le\min\{W_t,M\}$. For every $W\ge0$,
\[
\min\{W,M\}\le\left(1+\frac{M}{w_\xi}\right)\min\{W,w_\xi\}. \tag{9}
\]
If $W\le w_\xi$, the right side is at least $W$; if $W>w_\xi$, it is $w_\xi+M$, at least $M$.

Small-width rounds contribute at most $Tw_\mu$ to the support sum. Apply (9) and then (8) on all other rounds. Since $M/w_\xi=\xi L(2S\sqrt d+\mu)/(2d\epsilon_0)$, this proves
\[
R(T)\le\frac{4d\mu LT}{\xi}
+\left(1+\frac{\xi L(2S\sqrt d+\mu)}{2d\epsilon_0}\right)
\left[\frac{8d^2}{c_0\xi\Omega}\log\frac{2S\sqrt d+\mu}{\mu}
+\frac{32d}{3c_0\xi}\log\frac1\delta\right].
\]
Substitute (4) to obtain exactly the requested expression. Only one probability-$1-\delta$ event was used. The proof also covers $S=0$ and $\eta_{\max}=0$; neither introduces a division by zero.

## Audit Note

Containment of $K_t$ in a ball does not justify containment of its MVEE in that ball. Accordingly, this proof does not assert the source's uniform bound on $W_t$ or its stronger cumulative untruncated-width claim. Those assertions are unnecessary: the direct parameter-box bound on $h_t$ closes every obligation of the frozen regret theorem with the same constants.
