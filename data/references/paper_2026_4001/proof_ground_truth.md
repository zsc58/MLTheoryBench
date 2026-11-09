# Reference Proof

## Proof Structure and Obligations

1. Identify the target risk as a target-domain conditional-loss functional and as a weighted source functional; center the displayed score.
2. Derive a positive lower bound for the true pooled labeled propensity, separately from the assumed estimated-denominator bound.
3. Obtain the exact normalized estimator decomposition on an event with probability tending to one.
4. Bound the population nuisance remainder by the stated product of errors.
5. Derive the conditional second-moment bound and control the empirical nuisance remainder using independent training.
6. Control normalization and apply the finite-variance iid central limit theorem and Slutsky's theorem.

## Complete Proof

Write P for integration under the pooled law and P_n for the empirical measure of the evaluation sample. When a function depends on the training sample, P integrates a fresh pooled observation while holding training fixed. All covariate norms are under P_X.

### 1. Identification and score centering

By iterated expectation, covariate shift, and selection on observables,
\[
\psi=E_T[E(L\mid X,R=0)]
=E_T[E(L\mid X,R=1)]
=E_T[E(L\mid X,R=1,D=1)]
=E_T[\mu(X)].
\]
Let w=dP_T/dP_S. The same assumptions and source positivity give
\[
E_S[DL\mid X]=\pi_S(X)\mu(X),\qquad
\psi=E_S[w(X)\mu(X)]
=E_S\left[w(X)\frac{D}{\pi_S(X)}L\right].
\]
These identities follow from the source's identification argument; they do not require an efficiency assertion. Nonnegativity permits the initial tower and change-of-measure operations, and the finite risk and stated moments provide the integrability needed below. In particular, the second moment condition and finite psi imply mu belongs to L2(P_X).

The score has mean zero. Indeed,
\[
E[RD(L-\mu(X))\mid X]=0,
\qquad E[(1-R)\mu(X)]=\rho E_T[\mu(X)]=\rho\psi.
\]
Thus P varphi=0. The finite score second moment makes the score integrable and yields
\[
P_n\varphi=O_p(n^{-1/2})
\]
by the variance formula for an iid sample mean and Chebyshev's inequality.

### 2. True and estimated overlap

The pooled covariate law is rho P_T+(1-rho)P_S. Since P_T is absolutely continuous with respect to P_S and w<=C,
\[
1-g(X)=\frac{1-\rho}{1-\rho+\rho w(X)}
\ge \frac{1-\rho}{1-\rho+\rho C}
\]
almost surely. Consequently
\[
\pi(X)=(1-g(X))\pi_S(X)\ge c,
\qquad c:=\frac{\epsilon(1-\rho)}{1-\rho+\rho C}>0.
\]
Let a=epsilon'/2>0, where epsilon' is the constant in the estimated-overlap assumption. We do not identify a or epsilon' with c.

Let A_n be the training-measurable event that inf_x hat pi(x)>=a, that 0<hat g(x)<1 for every x, and that all three nuisance-error L2 norms are finite. The assumptions imply P(A_n)->1. Let H_n={hatrho>=rho/2}; then P(H_n)->1. On A_n, |hat g/hat pi|<=a^{-1}.

### 3. Exact decomposition and exceptional samples

On A_n define
\[
B(Z)=RD\left[\frac{\hat g(X)}{\hat\pi(X)}(L-\hat\mu(X))
-\frac{g(X)}{\pi(X)}(L-\mu(X))\right]
+(1-R)(\hat\mu(X)-\mu(X)),
\]
and set B identically zero off A_n. This localization is only a private proof device. It makes B square-integrable conditional on every training realization, as shown below, without imposing global overlap on the fitted functions.

On A_n intersect H_n, the public estimator uses its displayed formula. Since P_n(1-R)=hatrho, algebra gives
\[
\hat\psi-\psi
=P_n\varphi+
\left(\frac{\rho}{\hat\rho}-1\right)P_n\varphi
+\frac{1}{\hat\rho}(P_n-P)B
+\frac{1}{\hat\rho}PB.
\]
The exceptional-case estimator convention is irrelevant on this event. Its complement has probability tending to zero. Accordingly, bounds proved on this event establish the required stochastic orders for the actual, everywhere-defined estimator. This uses only the elementary fact that for any random variables agreeing on an event of probability tending to one, the probability that their difference exceeds any positive, possibly n-dependent threshold tends to zero.

### 4. Population nuisance remainder

Put delta=hat mu-mu. On A_n, conditional centering of the residual gives
\[
PB=E\left[\left(g-\hat g\frac{\pi}{\hat\pi}\right)\delta\right].
\]
Use
\[
g-\hat g\frac{\pi}{\hat\pi}
=(g-\hat g)+\hat g\frac{\hat\pi-\pi}{\hat\pi}.
\]
Cauchy--Schwarz and the bounds on hat g and hat pi yield
\[
|PB|\le \|\delta\|_2
\left(\|\hat g-g\|_2+a^{-1}\|\hat\pi-\pi\|_2\right)
=o_p(n^{-1/2}).
\]
Off A_n, PB=0. On H_n, 1/hatrho<=2/rho, so the corresponding normalized remainder is also o_p(n^{-1/2}). The bound is an outcome-error norm times a sum of propensity-error norms, not a product of all three errors.

### 5. Empirical nuisance remainder

On A_n put q=hat g/hat pi-g/pi. The two distinct denominator bounds give
\[
|q|\le a^{-1}|\hat g-g|+(ac)^{-1}|\hat\pi-\pi|,
\]
so
\[
\|q\|_2\le a^{-1}\|\hat g-g\|_2+(ac)^{-1}\|\hat\pi-\pi\|_2=o_p(1)
\]
on A_n. Rewriting B gives
\[
B=RDq(L-\mu)-RD\frac{\hat g}{\hat\pi}\delta+(1-R)\delta.
\]
Therefore, using (u+v)^2<=2u^2+2v^2,
\[
PB^2\le 2E[RDq^2(L-\mu)^2]
+2(1+a^{-1})^2\|\delta\|_2^2.
\]
The conditional moment assumption implies
\[
E[RDq^2(L-\mu)^2]
=E\left[q(X)^2\pi(X)E[(L-\mu(X))^2\mid X,R=1,D=1]\right]
\le M\|q\|_2^2.
\]
Thus PB^2=o_p(1), and it is finite on A_n. Off A_n it is zero by definition. This verifies conditional square integrability and uses all three nuisance consistencies.

Let T_n denote the training sample. Independence gives
\[
E[(P_n-P)B\mid T_n]=0,\qquad
\operatorname{Var}(\sqrt n(P_n-P)B\mid T_n)\le PB^2.
\]
For any t>0, conditional Chebyshev yields
\[
P\bigl(|\sqrt n(P_n-P)B|>t\bigr)
\le E\left[\min\{1,PB^2/t^2\}\right]\longrightarrow0.
\]
For completeness, a bounded nonnegative quantity U_n<=1 converging to zero in probability satisfies E[U_n]<=eta+P(U_n>eta) for every eta>0; this proves the last limit. Hence (P_n-P)B=o_p(n^{-1/2}), and normalization by hatrho on H_n preserves this order. We condition only on training, not on H_n or on a combined event involving evaluation observations.

### 6. Normalization and the limit theorem

Because hatrho is an average of iid Bernoulli(rho) indicators,
\[
E[(\hat\rho-\rho)^2]=\frac{\rho(1-\rho)}n,
\qquad \hat\rho-\rho=O_p(n^{-1/2}).
\]
On H_n,
\[
\left|\frac{\rho}{\hat\rho}-1\right|
\le \frac2\rho|\hat\rho-\rho|.
\]
Together with P_n varphi=O_p(n^{-1/2}), this makes the normalization remainder O_p(n^{-1})=o_p(n^{-1/2}). Combining all remainders on A_n intersect H_n and then using its probability limit gives
\[
\hat\psi-\psi=P_n\varphi+o_p(n^{-1/2})
=\frac1n\sum_{i=1}^n\varphi(Z_i;P)+o_p(n^{-1/2}).
\]
The ordinary iid finite-variance CLT states that the centered sample mean of iid real random variables with variance V<infinity, multiplied by sqrt(n), converges in distribution to N(0,V). Here its hypotheses hold because the evaluation observations are iid, the true score is a fixed measurable function, P varphi=0, and P varphi^2<infinity. If V=0, the centered score is zero almost surely and the same conclusion is the point mass at zero. Thus
\[
\frac1{\sqrt n}\sum_{i=1}^n\varphi(Z_i;P)
\Rightarrow N(0,\operatorname{Var}_P\varphi).
\]
Slutsky's theorem, in its form that adding an o_p(1) term preserves convergence in distribution, applies to the scaled remainder and proves
\[
\sqrt n(\hat\psi-\psi)\Rightarrow
N(0,\operatorname{Var}_P\{\varphi(Z;P)\}).
\]

All six obligations are closed. Only elementary conditioning, change of measure, Cauchy--Schwarz, Chebyshev, the iid finite-variance CLT, and Slutsky are used; no specialized external efficiency theorem is needed.
