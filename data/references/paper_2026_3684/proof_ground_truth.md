# Reference Proof

## Proof Structure and Obligations

The proof must establish: (1) exact Gaussian prediction and conditioning, including the common covariance factor across columns; (2) the cross-key contraction-replenishment identity and its bounds; (3) convergence of the scalar repeated-key iteration for an arbitrary finite preceding history; (4) decay of the parallel-to-orthogonal cross-covariance and the resulting limiting uncertainty increment; (5) the scalar gain limits; and (6) the eventual warped-probe angle limit, together with the exact finite-time angle identity in the separate from-initialization experiment. All six obligations are closed below. No paper-specific result is assumed without derivation.

## Complete Proof

### Gaussian filtering and well-definedness

The initial vectorized state is Gaussian with covariance I_m tensor p_0 I_D. The controls k_t are fixed, and the process and observation innovations are independent as specified in the task. Thus prediction and conditioning preserve Gaussianity.

The standard-independent conditioning identity used here is the following: if Y is Gaussian with covariance Q and Z=HY+epsilon, where epsilon is independent Gaussian noise with positive-definite covariance R, then

Cov(Y|Z)=Q-QH^T(HQH^T+R)^{-1}HQ.

For completeness, the centered residual Y-E[Y]-QH^T(HQH^T+R)^{-1}(Z-E[Z]) is jointly Gaussian with Z and has zero cross-covariance with Z. It is therefore independent of Z, and its covariance is the displayed matrix. This also proves the formula for a positive-semidefinite, possibly degenerate Q. In the present task R=r^2 I_m is positive definite.

For one column, independent additive process noise gives
\[
\bar P_t=P_{t-1}+\ell^2 I_D.
\]
The conditioning formula with observation direction k_t gives
\[
P_t=\bar P_t-\frac{\bar P_t k_t k_t^T\bar P_t}{r^2+k_t^T\bar P_t k_t}.
\]
In the full vectorized model, the observation matrix is I_m tensor k_t^T, the process covariance is I_m tensor ell^2 I_D, and the observation covariance is r^2 I_m. Substitution into the same formula preserves I_m tensor P_t. Hence the posterior columns are conditionally independent and share P_t, although their posterior means can differ.

Every P_t is positive semidefinite because it is a covariance. Since ell>0, every predicted covariance bar P_t is positive definite. Consequently all directional predicted variances for unit keys are positive, all denominators and correlation normalizations in the task are defined, and w_t is nonzero. The case p_0=0 causes no difficulty: the initial Gaussian may be degenerate, but the first prediction is positive definite.

### Exact cross-key balance

For a step with k_t=k_A, evaluating the update along k_B and subtracting the preceding posterior variance gives
\[
\begin{aligned}
\Delta_{B,t}
&=k_B^T\bar P_t k_B-k_B^TP_{t-1}k_B
 -\frac{(k_B^T\bar P_t k_A)^2}{r^2+k_A^T\bar P_t k_A}\\
&=\ell^2-\frac{(k_B^T\bar P_t k_A)^2}{r^2+\bar\sigma_{A,t}^2}.
\end{aligned}
\]
The definition of rho_{bar P_t} gives the equivalent normalized expression in the task. Cauchy-Schwarz for the positive-semidefinite quadratic form yields
\[
(k_B^T\bar P_t k_A)^2\leq
\bar\sigma_{A,t}^2\bar\sigma_{B,t}^2.
\]
Thus the subtracted contraction is nonnegative and is at most
\[
\bar\sigma_{B,t}^2\frac{\bar\sigma_{A,t}^2}{r^2+\bar\sigma_{A,t}^2}
\leq\bar\sigma_{B,t}^2.
\]

### Eventual repeated-key iteration

Suppose k_t=k_A for every t>=N, where N>=1 is fixed. The preceding history need not consist of k_A writes. Put x_t=k_A^T bar P_t k_A. Projecting the covariance update and the next prediction onto k_A gives, for t>=N,
\[
x_{t+1}=f(x_t),\qquad
f(x)=\ell^2+\frac{r^2x}{r^2+x}.
\]
A fixed point solves
\[
x^2-\ell^2x-r^2\ell^2=0.
\]
Its unique positive root is
\[
x_* =\frac{\ell^2+\sqrt{\ell^4+4r^2\ell^2}}2.
\]
Both x_t and x_* are at least ell^2. For nonnegative x,y,
\[
f(x)-f(y)=\frac{r^4(x-y)}{(r^2+x)(r^2+y)}.
\]
Writing q=r^2/(r^2+ell^2)<1, it follows that
\[
|x_{t+1}-x_*|\leq q^2|x_t-x_*|.
\]
Therefore x_t converges to x_* geometrically. The fixed-point identity also gives
\[
\frac{x_*^2}{r^2+x_*}=\ell^2.
\]

### Cross-covariance decay and limiting increment

Let Pi=I_D-k_A k_A^T and c_t=Pi bar P_t k_A. Then c_t is perpendicular to k_A and
\[
\bar P_t k_A=x_t k_A+c_t.
\]
The update gives
\[
P_t k_A=\frac{r^2}{r^2+x_t}(x_t k_A+c_t).
\]
The next prediction adds ell^2 k_A to this vector, so
\[
c_{t+1}=\frac{r^2}{r^2+x_t}c_t.
\]
Since x_t>=ell^2,
\[
\|c_t\|\leq q^{t-N}\|c_N\|\longrightarrow0.
\]
For every unit k_B, including rho=1 and rho=-1,
\[
k_B^T\bar P_t k_A=\rho x_t+k_B^Tc_t\longrightarrow\rho x_*.
\]
Using the exact balance and the fixed-point identity,
\[
\Delta_{B,t}\longrightarrow
\ell^2-\frac{\rho^2x_*^2}{r^2+x_*}
=(1-\rho^2)\ell^2.
\]
This is strictly positive when |rho|<1 and is zero for the two collinear cases.

### Scalar gain and parameter limits

Continuity gives
\[
g_t=\frac{x_t}{r^2+x_t}\longrightarrow
 g_*=\frac{x_*}{r^2+x_*}.
\]
Let a=ell/r and s=x_*/r^2. Then
\[
s=\frac{a^2+\sqrt{a^4+4a^2}}2
=\frac{a^2+a\sqrt{a^2+4}}2,
\qquad g_*=\frac{s}{1+s}.
\]
As a tends to zero, s/a tends to 1 and s tends to zero, hence g_*/a tends to 1. Thus g_*~ell/r. As a tends to infinity, s tends to infinity, hence g_* tends to 1.

### Eventual warped-probe angle

Assume |rho|<1 and put b=sqrt(1-rho^2) and e=e_perp, so k_B=rho k_A+b e. We must not assume c_t=0 after an arbitrary preceding history.

Let H_t be the restriction of Pi bar P_t Pi to the orthogonal complement of k_A. In the orthogonal decomposition into k_A and its complement, bar P_t has blocks x_t, c_t, and H_t. Restricting the covariance update and subsequent prediction to the orthogonal complement gives
\[
H_{t+1}=H_t+\ell^2 I_{k_A^\perp}
-\frac{c_t c_t^T}{r^2+x_t}.
\]
The norm of the last term is at most
\[
\frac{\|c_N\|^2 q^{2(t-N)}}{r^2+\ell^2},
\]
so its sum over t>=N converges. Consequently
\[
H_t=H_N+(t-N)\ell^2 I_{k_A^\perp}
-\sum_{j=N}^{t-1}\frac{c_jc_j^T}{r^2+x_j},
\qquad
\frac{H_t}{t}\longrightarrow\ell^2 I_{k_A^\perp}
\]
in operator norm.

The warped probe satisfies
\[
w_t=\bar P_t k_B
=(\rho x_t+b e^Tc_t)k_A+\rho c_t+b H_t e.
\]
Since x_t is bounded and c_t tends to zero,
\[
\frac{w_t}{t}\longrightarrow b\ell^2 e.
\]
This limit is nonzero. Because k_B is unit and k_B^T e=b,
\[
\cos\angle(w_t,k_B)
=\frac{k_B^Tw_t}{\|w_t\|}
\longrightarrow b=\sqrt{1-\rho^2}.
\]
This proves the angle limit under the full eventual-history contract, without exact finite-time diagonalization.

### Exact angle identity from initialization

Now consider the additional experiment in which k_t=k_A for every t>=1. Since P_0=p_0 I_D, induction in the covariance update shows that the cross block c_t is exactly zero and that the orthogonal predicted covariance is (p_0+t ell^2) times the identity. In particular,
\[
\bar P_t k_A=x_t k_A,\qquad
\bar P_t e_\perp=z_t e_\perp,
\qquad z_t=p_0+t\ell^2.
\]
Hence
\[
w_t=\rho x_t k_A+\sqrt{1-\rho^2}\,z_t e_\perp.
\]
Taking its inner product with k_B and its norm yields the exact identity
\[
\cos\angle(w_t,k_B)=
\frac{\rho^2x_t+(1-\rho^2)z_t}
{\sqrt{\rho^2x_t^2+(1-\rho^2)z_t^2}}.
\]
Here x_t tends to x_* and z_t tends to infinity, so the identity also gives the same angular limit directly. At rho=0 its value and limit are both 1. No residual-direction angle assertion is made for |rho|=1; in those cases k_B=+k_A or -k_A and w_t=x_t k_B, so their angle is zero.
