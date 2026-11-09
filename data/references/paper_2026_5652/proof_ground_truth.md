# Reference Proof

## Proof Structure and Obligations

The proof closes six obligations: (1) the mean alignment, curvature, and well-definedness of the constants; (2) the Poisson solution estimates and adapted martingale decomposition; (3) unconditional concentration for localized scalar noise and its remainder; (4) the radius bootstrap, including the exit iterate; (5) the telescoping, additive, and multiplicative residual bounds; and (6) the energy bound, convexity, and a single all-time probability event. All paper-specific estimates are derived below. The only non-elementary concentration result used is the explicitly stated standard independent Euclidean martingale maximal inequality.

## Step 001: Mean Dynamics, Curvature, and Degenerate Cases

Write $e_t=w_t-w_*$ and $g(w,z)=b_z-A_zw$. Since $\pi$ is stationary and $P$ is irreducible, all entries of $\pi$ are positive: from any state with positive stationary mass, a positive-probability path reaches every other state, and stationarity applied along that path gives positive mass there. Full column rank therefore gives $X^TDX\succ0$, and $d\geq1$ gives $L>0$.

Let $(r_P)_s=\sum_{s'}P(s,s')r(s,s')$. Direct expansion gives

$$
A=X^TD(I-\gamma P)X,\qquad b=X^TDr_P.
$$

For every state-vector $v$, stationarity and stochasticity give

$$
v^TL_{\rm Dir}v=\frac12\sum_{i,j}\pi_iP(i,j)(v_i-v_j)^2\geq0.
$$

Consequently,

$$
\frac{A+A^T}{2}=(1-\gamma)X^TDX+\gamma X^TL_{\rm Dir}X\succeq\omega I.
$$

This proves nonsingularity of $A$ and uniqueness of $w_*$. For $e=w-w_*$,

$$
e^TAe=V(w)\geq\omega\|e\|^2,\qquad \bar g(w):=\mathbb E_{\pi_Z}g(w,Z)=-Ae.
$$

In particular, $\langle\bar g(w),e\rangle=-V(w)\leq0$, and $V$ is a convex quadratic.

Define

$$
\xi(z)=b_z-A_zw_*,\qquad \Delta(z)=A-A_z,\qquad \zeta(z)=b_z-b.
$$

Then $\pi_Z(\xi)=0$, $\pi_Z(\Delta)=0$, and

$$
g(w,z)=-Ae+\xi(z)+\Delta(z)e,
\qquad g(w,z)-\bar g(w)=\Delta(z)w+\zeta(z).
$$

The elementary bounds are

$$
\|A_z\|_{\rm op}\leq2L^2,\quad
\|A\|_{\rm op}\leq2L^2,\quad
\|\Delta(z)\|_{\rm op}\leq4L^2,\quad
\|\zeta(z)\|\leq2BL,
$$

$$
\|g(w,z)\|\leq BL+2L^2\|w\|,
\qquad \|\xi(z)\|\leq BL+2L^2\|w_*\|.
$$

The assumptions imply $0<Q<\infty$, $H=Q/(c^2m^2L^4)<\infty$, and $S_T>0$ for every finite $T\geq1$. Also $c^2-A_1c-A_2>0$ and $\kappa>2$.

If $R_0=0$, then $B=0$ and $w_0=w_*=0$. Every update and both target bounds are zero, so the conclusion holds surely. Henceforth suppose $R_0>0$, and put

$$
R=\kappa R_0,\qquad \Lambda=\sqrt{2\log(8/\delta)}.
$$

Then $\|w_*\|\leq R$, $B\leq LR$, and $\|w_0\|\leq2R_0<R$.

## Step 002: Poisson Estimates and the Martingale Decomposition

Let $K=P_Z$. For any centered bounded scalar- or Euclidean-vector-valued function $h$ on $\mathcal Z$, total variation and the mixing assumption give

$$
\|K^kh\|_\infty\leq8\,2^{-k/m}\|h\|_\infty.
$$

Thus

$$
\mathcal Uh=\sum_{k=0}^{\infty}K^kh
$$

converges absolutely and uniformly. Telescoping proves $(I-K)\mathcal Uh=h$. To verify the constant, set $x=1/m\in(0,1]$. Concavity of $1-2^{-x}$ on $[0,1]$ gives $1-2^{-x}\geq x/2$. Therefore

$$
\|\mathcal Uh\|_\infty\leq\frac8{1-2^{-1/m}}\|h\|_\infty\leq16m\|h\|_\infty.
$$

The same bound applies to differences of centered forcings, since this specified solution operator is linear.

For the scalar forcing and multiplicative forcing, respectively, define

$$
h_w(z)=\langle\Delta(z)w+\zeta(z),w-w_*\rangle,
\qquad q_w(z)=\Delta(z)(w-w_*).
$$

Both are centered under $\pi_Z$. If $\|w\|,\|v\|\leq R$, the bounds from Step 001 yield

$$
\|h_w\|_\infty\leq(2BL+4L^2R)\,2R\leq12L^2R^2.
$$

Expanding the difference rather than assuming a Lipschitz estimate gives

$$
h_w(z)-h_v(z)
=\langle\Delta(z)w+\zeta(z),w-v\rangle
 +\langle\Delta(z)(w-v),v-w_*\rangle.
$$

Hence

$$
\|h_w-h_v\|_\infty
\leq(2BL+4L^2\|w\|+4L^2\|v-w_*\|)\|w-v\|
\leq14L^2R\|w-v\|.
$$

Writing $u_w=\mathcal Uh_w$, we obtain

$$
\|u_w\|_\infty\leq192mL^2R^2,
\qquad \|u_w-u_v\|_\infty\leq224mL^2R\|w-v\|. \tag{P1}
$$

Likewise, with $v_w=\mathcal Uq_w$,

$$
\|v_w\|_\infty\leq64mL^2\|w-w_*\|\leq128mL^2R,
\qquad \|v_w-v_v\|_\infty\leq64mL^2\|w-v\|. \tag{P2}
$$

For the fixed additive forcing, let $u^\xi=\mathcal U\xi$. Then

$$
\|u^\xi\|_\infty\leq U_\xi:=16m(BL+2L^2\|w_*\|). \tag{P3}
$$

These explicitly specified families are measurable in their parameters; the displayed local Lipschitz bounds also establish this directly.

Let $\mathcal F_t=\sigma(Z_0,\ldots,Z_t)$. Fixed initialization and deterministic stepsizes make $w_t$ measurable with respect to $\mathcal F_{t-1}$ for $t\geq1$, and in particular with respect to $\mathcal F_t$. Suppose $U_t$ is an $\mathcal F_t$-measurable function on $\mathcal Z$ and $\beta_t$ is an $\mathcal F_t$-measurable weight. The Markov property, with the random function frozen conditional on $\mathcal F_t$, gives

$$
\mathbb E[U_t(Z_{t+1})\mid\mathcal F_t]=(KU_t)(Z_t).
$$

Thus, whenever the increments are integrable,

$$
M_T=\sum_{t=0}^{T-1}\beta_t\{U_t(Z_{t+1})-(KU_t)(Z_t)\},\qquad M_0=0,
$$

is a martingale. If $h_t=(I-K)U_t$, adding and subtracting $U_t(Z_{t+1})$ gives

$$
\sum_{t=0}^{T-1}\beta_th_t(Z_t)=M_T+\mathcal R_T,
\qquad
\mathcal R_T=\sum_{t=0}^{T-1}\beta_t\{U_t(Z_t)-U_t(Z_{t+1})\}.
$$

Reindexing the two sums gives the exact identity

$$
\begin{aligned}
\mathcal R_T={}&\beta_0U_0(Z_0)-\beta_TU_T(Z_T)\\
&-\sum_{t=1}^T(\beta_{t-1}-\beta_t)U_{t-1}(Z_t)
-\sum_{t=1}^T\beta_t\{U_{t-1}(Z_t)-U_t(Z_t)\}. \tag{SBP}
\end{aligned}
$$

We use the following standard independent maximal inequality, supplied in the source as the Euclidean specialization of Pinelis' inequality: if a Euclidean-valued martingale starts at zero and has increments $D_{t+1}$ satisfying deterministic bounds $\|D_{t+1}\|\leq b_t$ almost surely, with $0<b_*^2:=\sum_{t\geq0}b_t^2<\infty$, then

$$
\mathbb P\left\{\sup_{T\geq0}\|M_T\|\geq r\right\}
\leq2\exp\left(-\frac{r^2}{2b_*^2}\right).
$$

In the scalar case use the absolute value. If all increment bounds are zero, the martingale is identically zero and no concentration theorem is needed. In particular, deterministic bounds $b_t=C\alpha_t$ yield, with failure probability at most $\delta/4$, the simultaneous bound $\sup_T\|M_T\|\leq C\sqrt H\Lambda$. Below, adaptedness, zero initialization, and these deterministic increment envelopes are checked before each application. No concentration argument conditions on the future event of bounded iterates.

## Step 003: Localized Scalar Noise and Remainder

Define

$$
\tau=\inf\{t\geq0:\|w_t\|>R\},\qquad
\widetilde w_t=w_{t\wedge\tau},\qquad
\beta_t=\alpha_t\mathbf1\{t<\tau\}.
$$

The stopping time and weights are adapted, $\tau\geq1$, and $\beta_t$ is nonnegative and nonincreasing. Importantly, $\widetilde w_\tau=w_\tau$ if $\tau<\infty$: the exit iterate is retained, not projected or discarded. The stopped recursion is exactly

$$
\widetilde w_{t+1}=\widetilde w_t+\beta_tg(\widetilde w_t,Z_t).
$$

Only when $\beta_t>0$ do we assert $\|\widetilde w_t\|\leq R$ and consequently

$$
\|g(\widetilde w_t,Z_t)\|\leq3L^2R. \tag{A}
$$

This suffices to give, for every $T$,

$$
G_T:=\sum_{t<T}\beta_t^2\|g(\widetilde w_t,Z_t)\|^2\leq9L^4R^2H. \tag{B}
$$

Apply the preceding decomposition with $U_t=u_{\widetilde w_t}$ and $h_t=h_{\widetilde w_t}$. The weighted increment satisfies the deterministic bound

$$
\left|\beta_t\{U_t(Z_{t+1})-(KU_t)(Z_t)\}\right|
\leq384mL^2R^2\alpha_t.
$$

Indeed, if $\beta_t>0$ this follows from (P1), and otherwise the increment vanishes. Integrability and the martingale property therefore hold. The maximal inequality gives an event $\mathcal E_s$ of probability at least $1-\delta/4$ on which

$$
\sup_T|M_T|\leq384mL^2R^2\sqrt H\Lambda. \tag{C}
$$

We now bound every term of (SBP). A nonzero endpoint coefficient multiplies a Poisson solution at an iterate still in the ball, so the two endpoints together have absolute value at most $384\alpha_0mL^2R^2$. A nonzero difference $\beta_{t-1}-\beta_t$ implies $\beta_{t-1}>0$. Since

$$
\sum_{t=1}^T(\beta_{t-1}-\beta_t)=\beta_0-\beta_T\leq\alpha_0,
$$

the step-difference sum is at most $192\alpha_0mL^2R^2$.

For the last sum in (SBP), only indices with $\beta_t>0$ matter. At such indices both $\widetilde w_{t-1}$ and $\widetilde w_t$ are in the ball. By (A) and (P1),

$$
\|U_t-U_{t-1}\|_\infty
\leq224mL^2R\|\widetilde w_t-\widetilde w_{t-1}\|
\leq672mL^4R^2\beta_{t-1}.
$$

Also $\sum_{t=1}^T\beta_t\beta_{t-1}\leq\sum_{t=1}^T\alpha_{t-1}^2\leq H$. Consequently,

$$
|\mathcal R_T|\leq576\alpha_0mL^2R^2+672mL^4R^2H. \tag{D}
$$

This estimate includes the drop to zero at the stopping time; it never assumes that the exit iterate lies in the ball.

Define the stopped bias

$$
\widetilde B_T=2\sum_{t<T}\beta_th_{\widetilde w_t}(Z_t)=2M_T+2\mathcal R_T.
$$

Equations (B)-(D) imply, on $\mathcal E_s$ and for every $T$,

$$
G_T+\widetilde B_T
\leq R^2\left[768mL^2\sqrt H\Lambda+1152\alpha_0mL^2+(1344m+9)L^4H\right]. \tag{E}
$$

## Step 004: Radius Bootstrap and Removal of Stopping

Let $\widetilde e_t=\widetilde w_t-w_*$. Expanding the exact stopped recursion gives

$$
\|\widetilde e_T\|^2
=\|e_0\|^2+G_T-2\sum_{t<T}\beta_tV(\widetilde w_t)+\widetilde B_T.
$$

Dropping the nonpositive drift and using (E), on $\mathcal E_s$,

$$
\sup_T\|\widetilde e_T\|^2
\leq\|e_0\|^2+R^2\left[768mL^2\sqrt H\Lambda+1152\alpha_0mL^2+(1344m+9)L^4H\right].
$$

Using $\|\widetilde w_T\|^2\leq2\|\widetilde e_T\|^2+2\|w_*\|^2$, $R=\kappa R_0$, and the stepsize definitions gives

$$
\begin{aligned}
\sup_T\|\widetilde w_T\|^2
\leq R_0^2\bigg[4
&+\frac{1536\kappa^2\sqrt Q\Lambda}{c}
+\frac{2304\kappa^2a_0}{c}\\
&+\frac{\kappa^2Q}{c^2}\left(\frac{2688}{m}+\frac{18}{m^2}\right)\bigg]
\leq R_0^2\left[4+\frac{A_1\kappa^2}{c}+\frac{A_2\kappa^2}{c^2}\right].
\end{aligned}
$$

Here $a_0\leq1$ and $m\geq1$ give the last inequality. By the definition of $\kappa$,

$$
4+\kappa^2\left(\frac{A_1}{c}+\frac{A_2}{c^2}\right)=\kappa^2.
$$

Therefore $\sup_T\|\widetilde w_T\|\leq R$ on $\mathcal E_s$. If $\tau<\infty$ on this event, evaluating this bound at $T=\tau$ gives $\|w_\tau\|=\|\widetilde w_\tau\|\leq R$, contradicting the strict inequality in the definition of $\tau$. This is a discrete first-exit contradiction and requires no continuity argument.

Thus $\mathcal E_s\subseteq\mathcal E_R$, where

$$
\mathcal E_R=\{\sup_{t\geq0}\|w_t\|\leq R\},\qquad
\mathbb P(\mathcal E_R)\geq1-\delta/4.
$$

On $\mathcal E_R$, the stopped and original processes coincide for every time.

## Step 005: Averaged Residual and the Fast Bound

Rearrange the original recursion as

$$
Ae_t=\frac{e_t-e_{t+1}}{\alpha_t}+\xi(Z_t)+\Delta(Z_t)e_t.
$$

Writing $\bar e_T=\bar w_T-w_*$, weighted summation yields

$$
A\bar e_T=I_{1,T}+I_{2,T}+I_{3,T},
$$

where

$$
I_{1,T}=\frac{e_0-e_T}{S_T},\qquad
I_{2,T}=\frac1{S_T}\sum_{t<T}\alpha_t\xi(Z_t),\qquad
I_{3,T}=\frac1{S_T}\sum_{t<T}\alpha_t\Delta(Z_t)e_t.
$$

On $\mathcal E_R$, cancellation of $w_*$ gives

$$
\|I_{1,T}\|=\frac{\|w_0-w_T\|}{S_T}\leq\frac{2R}{S_T}.
$$

For the additive term apply the decomposition with $U_t=u^\xi$ and $\beta_t=\alpha_t$. Its martingale starts at zero and has deterministic increment bounds $2U_\xi\alpha_t$. The endpoint and step-difference terms in (SBP) total at most $3\alpha_0U_\xi$, and the solution-difference term is zero. Thus there is an event $\mathcal E_2$, with probability at least $1-\delta/4$, on which for all $T$,

$$
\|I_{2,T}\|\leq\frac{U_\xi(2\sqrt H\Lambda+3\alpha_0)}{S_T}.
$$

If $U_\xi=0$, the same conclusion holds deterministically. Since $B\leq LR$ and $\|w_*\|\leq R$, this implies

$$
\|I_{2,T}\|\leq\frac{48mL^2R(2\sqrt H\Lambda+3\alpha_0)}{S_T}. \tag{F}
$$

For the multiplicative term first control the genuinely localized quantity

$$
\widetilde I_{3,T}=\frac1{S_T}\sum_{t<T}\beta_t\Delta(Z_t)(\widetilde w_t-w_*).
$$

Use $U_t=v_{\widetilde w_t}$ in the decomposition. On active indices (P2) gives $\|U_t\|_\infty\leq128mL^2R$, so the weighted martingale increments have deterministic bounds $256mL^2R\alpha_t$. The martingale is adapted and starts at zero. Its maximal bound, with failure probability at most $\delta/4$, is $256mL^2R\sqrt H\Lambda$.

For the remainder, the two endpoints and the step-difference sum contribute at most $3\alpha_0(128mL^2R)=384\alpha_0mL^2R$. Whenever $\beta_t>0$, (P2) and (A) give

$$
\|U_t-U_{t-1}\|_\infty
\leq64mL^2\|\widetilde w_t-\widetilde w_{t-1}\|
\leq192mL^4R\beta_{t-1}.
$$

Thus the last remainder contributes at most $192mL^4RH$. The coefficient is $64\cdot3=192$; the previously recorded source correction applies to both successive occurrences of 92 in that calculation.

There is therefore an event $\mathcal E_3$ of probability at least $1-\delta/4$ on which, simultaneously for all $T$,

$$
\|\widetilde I_{3,T}\|
\leq\frac{256mL^2R\sqrt H\Lambda+384\alpha_0mL^2R+192mL^4RH}{S_T}. \tag{G}
$$

On $\mathcal E_R$, $\widetilde I_{3,T}=I_{3,T}$. Combining (F), (G), and the telescoping bound, on $\mathcal E_R\cap\mathcal E_2\cap\mathcal E_3$,

$$
\begin{aligned}
\|A\bar e_T\|
&\leq\frac{R}{S_T}\left[2+(144+384)\alpha_0mL^2+(96+256)mL^2\sqrt H\Lambda+192mL^4H\right]\\
&=\frac{C_{\rm fast}}{S_T}.
\end{aligned}
$$

If $\bar e_T=0$, the fast bound is immediate. Otherwise, curvature and Cauchy-Schwarz give

$$
\omega\|\bar e_T\|^2\leq\bar e_T^TA\bar e_T\leq\|A\bar e_T\|\|\bar e_T\|,
$$

so $\|\bar e_T\|\leq\|A\bar e_T\|/\omega$ and

$$
V(\bar w_T)=\bar e_T^TA\bar e_T
\leq\frac{\|A\bar e_T\|^2}{\omega}
\leq\frac{C_{\rm fast}^2}{\omega S_T^2}. \tag{H}
$$

## Step 006: Energy, Robust Bound, and the Common Event

Set $\mathcal E_4=\mathcal E_s$, using the scalar-noise event already constructed, and define

$$
\mathcal E=\mathcal E_R\cap\mathcal E_2\cap\mathcal E_3\cap\mathcal E_4.
$$

Each listed event has failure probability at most $\delta/4$, so a union bound gives $\mathbb P(\mathcal E)\geq1-\delta$. The events need not be independent or distinct; in particular the scalar concentration event can serve both stability and energy control.

On $\mathcal E$, stopping is inactive. Define $B_T=2\sum_{t<T}\alpha_th_{w_t}(Z_t)$. The exact squared-error identity gives

$$
2\sum_{t<T}\alpha_tV(w_t)
=\|e_0\|^2-\|e_T\|^2+\sum_{t<T}\alpha_t^2\|g(w_t,Z_t)\|^2+B_T.
$$

Use $\|e_0\|\leq R_0\leq R$, discard $-\|e_T\|^2$, and apply (E). Dividing by two yields

$$
\sum_{t<T}\alpha_tV(w_t)
\leq R^2\left[\frac12+384mL^2\sqrt H\Lambda+576\alpha_0mL^2+(672m+4.5)L^4H\right]
=C_{\rm robust}.
$$

The averaging weights are positive and sum to one. Convexity of $V$ therefore gives, for every $T\geq1$ on the same event,

$$
V(\bar w_T)\leq\frac1{S_T}\sum_{t<T}\alpha_tV(w_t)
\leq\frac{C_{\rm robust}}{S_T}. \tag{I}
$$

Stability, (H), and (I) establish exactly the requested simultaneous conclusion. The proof does not require $\sum_ta_t=\infty$, stationary initialization, reversibility, bounded original iterates as an assumption, or any condition on the stepsizes involving $\omega$. All concentration events control every time simultaneously, so no union over horizons is needed.
