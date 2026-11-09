# Reference Proof

## Proof Structure

The proof establishes the exact evolution of the worker average, conditional noise and local-drift estimates, a contraction for worker disagreement, its accumulated bound, and a one-round smoothness descent inequality. Telescoping the descent inequality then gives the stated rate.

## Conditioning and Integrability

Define

$$
I_t=\{i:H_i>t\},\qquad m_t=|I_t|,
\qquad \mathcal A_r=\sigma(x_1^r,\ldots,x_n^r),
\qquad \mathbb E_r[\cdot]=\mathbb E[\cdot\mid\mathcal A_r].
$$

All sums over local time without an explicit range run from $0$ to $H_{\max}-1$. Use the within-round filtration

$$
\mathcal F_{r,t}=\sigma\!\left(
\{x_i^r\}_{i=1}^n,
\{\theta_{i,s}^r,\xi_{i,s}^r:i\in I_s,\ 0\le s<t\},
\{\theta_{i,t}^r:i\in I_t\}
\right).
$$

The local trajectories are measurable functions of their starting points and the previously used samples. Therefore $\mathcal A_r\subseteq\mathcal F_{r,t}$, and the fresh samples at time $t$ are independent of $\mathcal F_{r,t}$ and of each other. The public oracle assumptions, which hold at every evaluation point, consequently give

$$
\mathbb E[g_i(\theta_{i,t}^r,\xi_{i,t}^r)\mid\mathcal F_{r,t}]
=\nabla f(\theta_{i,t}^r),
$$

$$
\mathbb E[\|g_i(\theta_{i,t}^r,\xi_{i,t}^r)-\nabla f(\theta_{i,t}^r)\|^2\mid\mathcal F_{r,t}]
\le\sigma^2,
\qquad
\mathbb E[\|g_i(\theta_{i,t}^r,\xi_{i,t}^r)\|^2\mid\mathcal F_{r,t}]
\le G^2.
$$

Conditional on this filtration, the active workers' noises are independent and mean zero. The current mask does not enter any within-round local update. Thus it is independent jointly of the starting worker states and the current-round trajectories, even though it is sampled at the beginning of the round.

All finite-horizon iterates are square-integrable: start from the fixed initialization, apply the conditional second-moment bound to each fresh gradient, and use that the updates are finite sums and that coordinate projections have operator norm at most one. Smoothness gives

$$
|f(x)|\le |f(0)|+\|\nabla f(0)\|\,\|x\|+\frac L2\|x\|^2,
\qquad
\|\nabla f(x)\|\le\|\nabla f(0)\|+L\|x\|.
$$

Hence all objective expectations and gradient second moments below are finite. No additional moment assumption on the iterates is required.

## 1. Exact Evolution of the Worker Average

Write $P_r=P_{S_r}$ and define

$$
\bar z^r=\frac1n\sum_i z_i^r,
\qquad
\bar g_t^r=\frac1n\sum_{i\in I_t}g_i(\theta_{i,t}^r,\xi_{i,t}^r),
\qquad
G_r=\sum_t\bar g_t^r.
$$

Averaging the merge and using linearity gives

$$
\bar x^{r+1}
=\bar z^r+P_r\left(\bar y^r-\frac1n\sum_i y_i^r\right)
=\bar z^r.
$$

Telescoping the local updates gives

$$
z_i^r=x_i^r-\eta\sum_{t=0}^{H_i-1}g_i(\theta_{i,t}^r,\xi_{i,t}^r).
$$

Averaging and regrouping by local time therefore yields

$$
\bar x^{r+1}=\bar x^r-\eta G_r. \tag{2}
$$

## 2. Conditional Noise and Local-Drift Estimates

Let

$$
\epsilon_{i,t}^r=g_i(\theta_{i,t}^r,\xi_{i,t}^r)-\nabla f(\theta_{i,t}^r),
\qquad
\bar\epsilon_t^r=\frac1n\sum_{i\in I_t}\epsilon_{i,t}^r.
$$

Conditional independence and zero means eliminate same-time cross terms, so

$$
\mathbb E[\|\bar\epsilon_t^r\|^2\mid\mathcal F_{r,t}]
=\frac1{n^2}\sum_{i\in I_t}\mathbb E[\|\epsilon_{i,t}^r\|^2\mid\mathcal F_{r,t}]
\le\frac{m_t\sigma^2}{n^2}.
$$

Since

$$
\sum_t m_t=\sum_iH_i=n\bar H,
$$

the tower property gives

$$
\sum_t\mathbb E_r\|\bar\epsilon_t^r\|^2\le\frac{\bar H\sigma^2}{n}.
$$

For $s<t$, the earlier noise $\bar\epsilon_s^r$ is $\mathcal F_{r,t}$-measurable. Thus

$$
\mathbb E_r\langle\bar\epsilon_s^r,\bar\epsilon_t^r\rangle
=\mathbb E_r\left\langle\bar\epsilon_s^r,
\mathbb E[\bar\epsilon_t^r\mid\mathcal F_{r,t}]\right\rangle=0.
$$

Expanding the square consequently proves the round-conditioned bound

$$
\mathbb E_r\left\|\sum_t\bar\epsilon_t^r\right\|^2
=\sum_t\mathbb E_r\|\bar\epsilon_t^r\|^2
\le\frac{\bar H\sigma^2}{n}. \tag{3}
$$

For $0\le t\le H_i$, telescoping and Cauchy–Schwarz give

$$
\|\theta_{i,t}^r-x_i^r\|^2
\le\eta^2t\sum_{s=0}^{t-1}\|g_i(\theta_{i,s}^r,\xi_{i,s}^r)\|^2.
$$

The tower property applies because $\mathcal A_r\subseteq\mathcal F_{r,s}$. Therefore

$$
\mathbb E_r\|\theta_{i,t}^r-x_i^r\|^2\le\eta^2t^2G^2,
\qquad
\sum_i\sum_{t=0}^{H_i-1}\mathbb E_r\|\theta_{i,t}^r-x_i^r\|^2
\le\eta^2G^2\Phi_H. \tag{4}
$$

Define

$$
u_i^r=y_i^r-x_i^r,
\qquad v_i^r=z_i^r-y_i^r,
\qquad \bar u^r=\frac1n\sum_i u_i^r,
\qquad \bar v^r=\frac1n\sum_i v_i^r.
$$

The corresponding telescoped sums contain $T_i$ and $O_i$ gradients, respectively. The same calculation gives

$$
\mathbb E_r\|u_i^r\|^2\le\eta^2T_i^2G^2,
\qquad
\mathbb E_r\|v_i^r\|^2\le\eta^2O_i^2G^2.
$$

These formulas also cover $O_i=0$, when the overlap increment is zero. For any worker vectors $h_i$ with average $\bar h$,

$$
\sum_i\|h_i-\bar h\|^2=\sum_i\|h_i\|^2-n\|\bar h\|^2
\le\sum_i\|h_i\|^2.
$$

Consequently,

$$
\mathbb E_r\sum_i\|u_i^r-\bar u^r\|^2\le\eta^2G^2S_T,
\qquad
\mathbb E_r\sum_i\|v_i^r-\bar v^r\|^2\le\eta^2G^2S_O. \tag{5}
$$

## 3. Contractive Disagreement Recursion

Define

$$
X_r=\sum_i\|x_i^r-\bar x^r\|^2,
\quad Y_r=\sum_i\|y_i^r-\bar y^r\|^2,
\quad U_r=\sum_i\|u_i^r-\bar u^r\|^2,
\quad V_r=\sum_i\|v_i^r-\bar v^r\|^2.
$$

The merge and the exact-average identity imply

$$
x_i^{r+1}-\bar x^{r+1}
=(I-P_r)(y_i^r-\bar y^r)+(v_i^r-\bar v^r). \tag{6}
$$

For fixed vectors $h,k$, each coordinate is omitted by the uniform mask with probability $q$, and hence

$$
\mathbb E_{S_r}\|(I-P_r)h+k\|^2
=q\|h\|^2+2q\langle h,k\rangle+\|k\|^2
=q\|h+k\|^2+p\|k\|^2.
$$

Using $2\langle h,k\rangle\le b\|h\|^2+b^{-1}\|k\|^2$ gives

$$
\mathbb E_{S_r}\|(I-P_r)h+k\|^2
\le q(1+b)\|h\|^2+C_O\|k\|^2.
$$

To keep the conditioning nested, let

$$
\mathcal B_r=\sigma\bigl(\{x_i^r,y_i^r,z_i^r\}_{i=1}^n\bigr).
$$

The current mask is independent of $\mathcal B_r$, and $\mathcal A_r\subseteq\mathcal B_r$. Applying the mask calculation to (6) and summing over workers yields

$$
\mathbb E[X_{r+1}\mid\mathcal B_r]\le q(1+b)Y_r+C_OV_r.
$$

Since

$$
y_i^r-\bar y^r=(x_i^r-\bar x^r)+(u_i^r-\bar u^r),
$$

Young's inequality with parameter $a>0$ gives

$$
Y_r\le(1+a)X_r+(1+a^{-1})U_r.
$$

Combining the last two bounds gives

$$
\mathbb E[X_{r+1}\mid\mathcal B_r]\le\rho X_r+C_TU_r+C_OV_r.
$$

Now condition on $\mathcal A_r$ and apply (5). The tower property is valid for these nested sigma-fields, and we obtain

$$
\mathbb E_r X_{r+1}
\le\rho X_r+\eta^2G^2(C_TS_T+C_OS_O). \tag{7}
$$

## 4. Accumulated Disagreement

Let $\delta_r=\mathbb E X_r$ and $C=\eta^2G^2(C_TS_T+C_OS_O)$. Common initialization gives $\delta_0=0$, and taking full expectation in (7) gives

$$
\delta_{r+1}\le\rho\delta_r+C.
$$

Induction yields

$$
\delta_r\le C\sum_{j=0}^{r-1}\rho^j\le\frac{C}{1-\rho},
$$

where the sum is zero when $r=0$. Here $0\le\rho<1$. Thus

$$
\sum_{r=0}^{R-1}\mathbb E X_r
\le\frac{R\eta^2G^2(C_TS_T+C_OS_O)}{1-\rho}. \tag{8}
$$

## 5. One-Round Descent

Let $a_r=\nabla f(\bar x^r)$. Smoothness and (2) imply

$$
f(\bar x^{r+1})
\le f(\bar x^r)-\eta\langle a_r,G_r\rangle
+\frac{L\eta^2}{2}\|G_r\|^2. \tag{9}
$$

First observe from (4) that

$$
\begin{aligned}
\sum_i\sum_{t=0}^{H_i-1}\mathbb E_r\|\theta_{i,t}^r-\bar x^r\|^2
&\le 2\sum_iH_i\|x_i^r-\bar x^r\|^2
+2\sum_i\sum_{t=0}^{H_i-1}\mathbb E_r\|\theta_{i,t}^r-x_i^r\|^2\\
&\le2H_{\max}X_r+2\eta^2G^2\Phi_H.
\end{aligned} \tag{10}
$$

Conditional unbiasedness and the tower property give

$$
\mathbb E_r\langle a_r,G_r\rangle
=\frac1n\sum_i\sum_{t=0}^{H_i-1}
\mathbb E_r\langle a_r,\nabla f(\theta_{i,t}^r)\rangle.
$$

For any vectors $h,k$,

$$
\langle h,k\rangle
=\tfrac12\|h\|^2+\tfrac12\|k\|^2-\tfrac12\|h-k\|^2
\ge\tfrac12\|h\|^2-\tfrac12\|h-k\|^2.
$$

Using this inequality, smoothness, the identity $\sum_iH_i=n\bar H$, and (10), we obtain

$$
\mathbb E_r\langle a_r,G_r\rangle
\ge\frac{\bar H}{2}\|a_r\|^2
-\frac{L^2H_{\max}}nX_r
-\frac{L^2\eta^2G^2}{n}\Phi_H. \tag{11}
$$

For the quadratic term, define

$$
d_t^r=\frac1n\sum_{i\in I_t}\nabla f(\theta_{i,t}^r),
\qquad
G_r=\sum_td_t^r+\sum_t\bar\epsilon_t^r.
$$

Cauchy–Schwarz and $m_t\le n$ give the pathwise estimate

$$
\begin{aligned}
\|d_t^r\|^2
&\le\frac{m_t}{n^2}\sum_{i\in I_t}\|\nabla f(\theta_{i,t}^r)\|^2\\
&\le\frac1n\sum_{i\in I_t}\|\nabla f(\theta_{i,t}^r)\|^2\\
&\le\frac{2m_t}{n}\|a_r\|^2
+\frac{2L^2}{n}\sum_{i\in I_t}\|\theta_{i,t}^r-\bar x^r\|^2.
\end{aligned}
$$

Applying $\|\sum_t d_t^r\|^2\le H_{\max}\sum_t\|d_t^r\|^2$, conditioning on $\mathcal A_r$, and using (10) yields

$$
\mathbb E_r\left\|\sum_td_t^r\right\|^2
\le2H_{\max}\bar H\|a_r\|^2
+\frac{4L^2H_{\max}}n
\bigl(H_{\max}X_r+\eta^2G^2\Phi_H\bigr).
$$

The gradient sum and noise sum need not be independent. Instead use $\|h+k\|^2\le2\|h\|^2+2\|k\|^2$, together with (3), to get

$$
\mathbb E_r\|G_r\|^2
\le4H_{\max}\bar H\|a_r\|^2
+\frac{8L^2H_{\max}}n
\bigl(H_{\max}X_r+\eta^2G^2\Phi_H\bigr)
+\frac{2\bar H\sigma^2}{n}. \tag{12}
$$

Conditioning (9) on $\mathcal A_r$ and substituting (11) and (12) gives

$$
\begin{aligned}
\mathbb E_r f(\bar x^{r+1})
\le{}&f(\bar x^r)
-\eta\bigl(\bar H/2-2L\eta\bar H H_{\max}\bigr)\|a_r\|^2\\
&+\eta\frac{L^2H_{\max}}n(1+4L\eta H_{\max})X_r
+\frac{L\eta^2\bar H\sigma^2}{n}\\
&+\frac{L^2\eta^3G^2\Phi_H}{n}(1+4L\eta H_{\max}).
\end{aligned} \tag{13}
$$

## 6. Telescoping and Final Constants

The stepsize condition gives

$$
\bar H/2-2L\eta\bar H H_{\max}\ge\bar H/4,
\qquad
1+4L\eta H_{\max}\le3/2.
$$

Take full expectations in (13), rearrange, and sum over $r=0,\ldots,R-1$. The objective terms telescope, and $f(\bar x^R)\ge f_*$, so

$$
\begin{aligned}
\frac{\eta\bar H}{4}\sum_{r=0}^{R-1}\mathbb E\|\nabla f(\bar x^r)\|^2
\le{}&f(x^0)-f_*
+\frac{3\eta L^2H_{\max}}{2n}\sum_{r=0}^{R-1}\mathbb E X_r\\
&+\frac{RL\eta^2\bar H\sigma^2}{n}
+\frac{3RL^2\eta^3G^2\Phi_H}{2n}.
\end{aligned}
$$

Apply (8) and divide by $R\eta\bar H/4>0$. This gives

$$
\frac1R\sum_{r=0}^{R-1}\mathbb E\|\nabla f(\bar x^r)\|^2
\le
\frac{4(f(x^0)-f_*)}{\eta\bar H R}
+\frac{4L\eta\sigma^2}{n}
+\frac{6L^2\eta^2G^2\Phi_H}{n\bar H}
+\frac{6L^2\eta^2G^2H_{\max}}{n\bar H}
\frac{C_TS_T+C_OS_O}{1-\rho}.
$$

All denominators are positive: $n\ge1$, $H_i\ge1$, $\eta>0$, $R\ge1$, and $1-\rho>0$. The proof requires no division by $q$, $S_O$, $\Phi_H$, $\sigma^2$, or the initial objective gap. Thus it includes $K=d$, $\zeta=0$, $H_{\max}=1$, $\sigma^2=0$, and zero initial gap. For $n=1$ the disagreement is identically zero, and the same upper bound remains valid. This completes every proof obligation for the stated theorem.
