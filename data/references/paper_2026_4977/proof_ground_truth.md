# Reference Proof

## Proof Structure

The proof follows row-normalization geometry, weight-decay control, smoothness descent, stochastic momentum tracking, and telescoping. Care is needed because a trajectory-defined approximation error is random. We first derive deterministic geometry bounds for the specified NS5 polynomial, prove the epsilon-zero stationarity bound for both methods, and then compare its constants with the requested constants. This does not assume a deterministic uniform spectral gap or condition the oracle on a realized approximation error.

All arguments below are elementary consequences of the supplied definitions. The cited external approximation result and scalar recursion result are not used as unproved obligations.

## 1. Exact-polar geometry

Write $R=P_r(M)$ and let $D=\operatorname{diag}(d_1,\ldots,d_m)$, where $d_i=\|M_{i,:}\|_2$. Then $M=DR$. The case $M=0$ is immediate. Otherwise let $R=U\Sigma V^\top$, $Q=UV^\top$, and $H=(RR^\top)^{1/2}=U\Sigma U^\top$. Thus $QR^\top=H$ and
\[
\langle M,Q\rangle_F=\operatorname{tr}(DH)=\sum_i d_iH_{ii}.
\]
For every $i$ with $d_i>0$, row normalization gives $(RR^\top)_{ii}=1$. Since $H^2\preceq\|H\|_2H$,
\[
1\le\|R\|_2H_{ii}.
\]
Also $\|R\|_2\le\|R\|_F\le\sqrt m$ and $\sum_i d_i\ge\|M\|_F$. Therefore
\[
\langle M,Q\rangle_F\ge\frac{\|M\|_F}{\sqrt m},\qquad
\|Q\|_F^2=\operatorname{rank}(R)\le n.
\]
Zero rows contribute zero throughout.

## 2. NS5 geometry and the approximation dependency

For a nonzero input $A=U\Sigma V^\top$, substitution into the polynomial iteration proves by induction that
\[
Y^{(k)}(A)=U\operatorname{diag}(s_i^{(k)})V^\top,
\quad s_i^{(0)}=\frac{\sigma_i(A)}{\max\{1,\|A\|_F\}},
\]
where
\[
s_i^{(k+1)}=\phi(s_i^{(k)}),\qquad
\phi(s)=\frac{15}{8}s-\frac54s^3+\frac38s^5.
\]
For $0\le s\le1$,
\[
\phi(s)-s=\frac{s(1-s^2)(7-3s^2)}8\ge0,\qquad
\phi'(s)=\frac{15}{8}(1-s^2)^2\ge0,\qquad \phi(1)=1.
\]
Consequently every nonzero singular direction satisfies
\[
0<s_i^{(0)}\le s_i^{(k)}\le1.
\]
In particular, $\|\operatorname{NS5}(A)\|_F\le\sqrt{\operatorname{rank}(A)}$, and the output has the same compact polar factor as $A$. The zero-input case gives zero at every step.

For completeness, the particular approximation estimate used in the selected source dependency also follows directly. Set $e=1-s^2$. An expansion gives
\[
1-\phi(s)^2=\frac{e^3(40+15e+9e^2)}{64}\le e^3\qquad(0\le e\le1).
\]
For a nonzero input, all initial residuals lie in $[0,1)$; for a zero input use residual zero on its zero-dimensional range. Thus the maximum range-restricted residual after five steps is at most $\delta_0^{3^5}$, where $\delta_0$ is the initial maximum. It follows that
\[
\|\operatorname{NS5}(A)-\operatorname{Orth}(A)\|_2
\le1-\sqrt{1-\delta_0^{3^5}}\le\delta_0^{3^5}<1.
\]
Taking a maximum over a finite trajectory proves the stated finite-trajectory estimate. This is a realization-wise fact, not the assertion of an automatic deterministic upper bound strictly below one over all sample paths.

The requested perturbation geometry follows as in the source. If $\|\operatorname{NS5}(R)-\operatorname{Orth}(R)\|_2\le\varepsilon<1$, the common singular-vector representation implies $s_i^{(5)}\in[1-\varepsilon,1+\varepsilon]$. Hence
\[
\operatorname{NS5}(R)R^\top\succeq(1-\varepsilon)H,
\]
and the trace argument in Section 1 yields
\[
\langle M,\operatorname{NS5}(R)\rangle_F\ge\frac{1-\varepsilon}{\sqrt m}\|M\|_F,
\qquad\|\operatorname{NS5}(R)\|_F\le(1+\varepsilon)\sqrt n.
\]
Norm closeness alone, without the common singular-vector representation, would not justify this alignment step.

We additionally need deterministic bounds before taking expectations. Let $k$ be the number of nonzero rows of the nonzero row-normalized matrix $R$. Then $\|R\|_F=\sqrt k$, so its internal scaling is exactly $\sqrt k$. Since $s_i^{(5)}\ge\sigma_i(R)/\sqrt k$,
\[
\operatorname{NS5}(R)R^\top
=U\operatorname{diag}(s_i^{(5)}\sigma_i(R))U^\top
\succeq\frac{RR^\top}{\sqrt k}.
\]
Taking the trace against the same nonnegative diagonal matrix $D$ gives
\[
\langle M,\operatorname{NS5}(R)\rangle_F
\ge\frac{\operatorname{tr}(DRR^\top)}{\sqrt k}
=\frac{\sum_i d_i}{\sqrt k}
\ge\frac{\|M\|_F}{\sqrt m}.
\]
Thus, for both methods and every realization,
\[
\boxed{\langle M_t,O_t\rangle_F\ge\frac{\|M_t\|_F}{\sqrt m},\qquad\|O_t\|_F\le\sqrt n.}
\]
This additional estimate uses the same diagonal-trace proof mechanism and only the elementary scalar inequalities for the explicitly specified polynomial.

## 3. Weight decay and finite moments

Fix the horizon and set the deterministic quantities
\[
c_0=\frac1{\sqrt m}+\sqrt n,\qquad d_0=a\sqrt n+\rho,\qquad\kappa_0=\frac a{\sqrt m}-\rho.
\]
Because $\varepsilon\ge0$, the task's hypotheses imply $\kappa_0>0$ and
\[
\lambda_t\le\lambda_0t^{-1/4},\qquad
\lambda_0:=\frac{\rho}{\|X_1\|_F+4a\sqrt n}.
\]
The parameters here are fixed inputs, not functions of future samples. Moreover,
\[
0\le\eta_t\lambda_t\le\lambda_0t^{-1},\qquad
\lambda_0<\frac1{4\sqrt{mn}}\le1.
\]
Using the deterministic norm bound from Section 2,
\[
\|X_{t+1}\|_F
\le(1-\eta_t\lambda_t)\|X_t\|_F+a\eta_t\sqrt n
\le\|X_t\|_F+a\sqrt n\,t^{-3/4}.
\]
Induction and $\sum_{s=1}^{t-1}s^{-3/4}\le4t^{1/4}$ give
\[
\|X_t\|_F\le\|X_1\|_F+4a\sqrt n\,t^{1/4}.
\]
Therefore
\[
\lambda_t\|X_t\|_F
\le\lambda_0\bigl(\|X_1\|_Ft^{-1/4}+4a\sqrt n\bigr)\le\rho,
\]
\[
\|aO_t+\lambda_tX_t\|_F\le d_0,\qquad
\|X_{t+1}-X_t\|_F\le d_0\eta_t.
\]
The schedule $t^{-3/4}$ is not summable. The relevant iterate bound grows as $t^{1/4}$, and the weight-decay product is bounded by $\rho$, not by $\rho t^{-1/4}$.

At any finite horizon these bounds put the iterates in a deterministic bounded set. Smoothness bounds their true gradients and objective values there. The oracle variance bound then gives finite second moments for the stochastic gradients and momentum. Thus the expectations and conditional expansions below are well defined. Row normalization and the polynomial map are measurable; the compact polar map, including its value at zero, is also measurable, for example as the pointwise limit of $A(A^\top A+uI)^{-1/2}$ as $u\downarrow0$.

## 4. Descent

Let $g_t=\nabla f(X_t)$, $S_t=g_t-M_t$, and $h_t=t^{-1/2}$. By the geometry above,
\[
\langle g_t,O_t\rangle_F
\ge\frac{\|M_t\|_F}{\sqrt m}-\sqrt n\|S_t\|_F
\ge\frac{\|g_t\|_F}{\sqrt m}-c_0\|S_t\|_F.
\]
Smoothness and $\lambda_t\|X_t\|_F\le\rho$ imply
\[
f(X_{t+1})\le f(X_t)-\kappa_0\eta_t\|g_t\|_F
+ac_0\eta_t\|S_t\|_F+\frac L2d_0^2\eta_t^2.
\]
Young's inequality gives
\[
ac_0\eta_t\|S_t\|_F
\le\frac{ah_{t+1}}{2L}\|S_t\|_F^2
+\frac{aL}{2}c_0^2\frac{\eta_t^2}{h_{t+1}}.
\]
Accordingly,
\[
f(X_{t+1})\le f(X_t)-\kappa_0\eta_t\|g_t\|_F
+\frac{ah_{t+1}}{2L}\|S_t\|_F^2
+\frac{aL}{2}c_0^2\frac{\eta_t^2}{h_{t+1}}
+\frac L2d_0^2\eta_t^2.
\]
All coefficients used at this stage are deterministic.

## 5. Tracking recursion and accumulated error

Let $\mathcal F_t=\sigma(\xi_1,\ldots,\xi_t)$ and
\[
\zeta_{t+1}=\nabla f(X_{t+1};\xi_{t+1})-g_{t+1}.
\]
The point $X_{t+1}$ is $\mathcal F_t$-measurable and is formed before drawing $\xi_{t+1}$. Fresh sampling gives
\[
\mathbb E[\zeta_{t+1}\mid\mathcal F_t]=0,\qquad
\mathbb E[\|\zeta_{t+1}\|_F^2\mid\mathcal F_t]\le\sigma^2.
\]
The corrected update at $X_{t+1}$ gives
\[
M_{t+1}-g_{t+1}
=\beta_{t+1}\bigl(M_t-g_t+g_t-g_{t+1}\bigr)+h_{t+1}\zeta_{t+1}.
\]
Taking conditional expectation of the squared norm removes the noise cross term. Applying Young's inequality with parameter $h_{t+1}/\beta_{t+1}$, which is positive for $t\ge1$, and then smoothness yields, for $E_t=\mathbb E\|S_t\|_F^2$,
\[
E_{t+1}\le\beta_{t+1}E_t
+\frac{\beta_{t+1}^2}{h_{t+1}}L^2\eta_t^2\mathbb E\|aO_t+\lambda_tX_t\|_F^2
+h_{t+1}^2\sigma^2.
\]
The expectation around the squared update norm is essential in this unconditional statement. Bounding it by $d_0^2$, and using
\[
\frac{\eta_t^2}{h_{t+1}}=\frac{\sqrt{t+1}}{t^{3/2}}\le\frac{2\sqrt2}{t+1}=2\sqrt2h_{t+1}^2,
\]
gives
\[
E_{t+1}\le(1-h_{t+1})E_t+B_0h_{t+1}^2,
\qquad B_0=2\sqrt2L^2d_0^2+\sigma^2.
\]
Also $E_1\le\sigma^2$ from the initialization.

The scalar lemma is elementary: if $E_{t+1}\le(1-\alpha_{t+1})E_t+A_{t+1}$, then $E_t-E_{t+1}+A_{t+1}\ge\alpha_{t+1}E_t$. For $\alpha_t=t^{-p}$ with $0<p\le1$,
\[
\frac{\alpha_t}{\alpha_{t+1}}=\left(\frac{t+1}{t}\right)^p\le2,
\]
so $\alpha_tE_t\le2(E_t-E_{t+1}+A_{t+1})$. Applying this with $p=1/2$ and summing yields
\[
\sum_{t=1}^T h_{t+1}E_t
\le\sum_{t=1}^T h_tE_t
\le2E_1+2B_0\sum_{t=1}^T\frac1{t+1}
\le2\sigma^2+2B_0(1+\ln T).
\]
There is no extra factor of $1/L$ in this accumulated-error estimate, and its logarithmic coefficient includes $\sigma^2$.

## 6. Summation and conversion to the requested average

The remaining scalar sums satisfy
\[
\sum_{t=1}^T\frac{\eta_t^2}{h_{t+1}}
\le\sqrt2\sum_{t=1}^T\frac1t\le2(1+\ln T),\qquad
\sum_{t=1}^T\eta_t^2=\sum_{t=1}^Tt^{-3/2}\le3.
\]
Take expectations in the descent inequality and sum. Using $f(X_{T+1})\ge f^*$ gives
\[
\kappa_0\sum_{t=1}^T\eta_t\mathbb E\|g_t\|_F
\le f(X_1)-f^*+C_{1,\rho}^{(0)}(1+\ln T)+C_{2,\rho}^{(0)},
\]
where
\[
C_{1,\rho}^{(0)}=\frac aL\left(2\sqrt2L^2d_0^2+\sigma^2\right)+aLc_0^2,
\qquad C_{2,\rho}^{(0)}=\frac{a\sigma^2}{L}+\frac{3L}{2}d_0^2.
\]
For every $t\le T$, $\eta_t\ge T^{-3/4}$. Since the gradient norms are nonnegative,
\[
T^{-3/4}\sum_{t=1}^T\mathbb E\|g_t\|_F
\le\sum_{t=1}^T\eta_t\mathbb E\|g_t\|_F.
\]
Thus both methods satisfy the deterministic bound
\[
\frac1T\sum_{t=1}^T\mathbb E\|g_t\|_F
\le\frac{f(X_1)-f^*+C_{1,\rho}^{(0)}(1+\ln T)+C_{2,\rho}^{(0)}}{\kappa_0T^{1/4}}.
\]
A bound on $\sum_t\eta_t$ alone would not justify this conversion to an unweighted average.

## 7. Requested constants and random-error interpretation

For any allowed value of $\varepsilon\ge0$,
\[
c=c_0+\varepsilon\left(\sqrt n-\frac1{\sqrt m}\right)\ge c_0,\qquad
d=d_0+a\varepsilon\sqrt n\ge d_0,
\]
\[
0<\kappa=\kappa_0-\frac{a\varepsilon}{\sqrt m}\le\kappa_0.
\]
Therefore $C_{1,\rho}\ge C_{1,\rho}^{(0)}$ and $C_{2,\rho}\ge C_{2,\rho}^{(0)}$. The objective gap is nonnegative. Comparing the nonnegative numerators and positive denominators proves exactly
\[
\frac1T\sum_{t=1}^T\mathbb E\|\nabla f(X_t)\|_F
\le\frac{f(X_1)-f^*+C_{1,\rho}(1+\ln T)+C_{2,\rho}}{\kappa T^{1/4}}.
\]
If $\varepsilon=\varepsilon_{\mathrm{ns},T}$ is random, this final comparison is made pointwise on the probability-one event where the task's parameter conditions hold. No random coefficient has been extracted from an expectation, and no conditioning on $\varepsilon$ has been performed. The exact-polar case is $\varepsilon=0$; the same reasoning covers any permitted deterministic NS5 error bound.

## Audit Closure

Closed obligations are: zero and rank-deficient matrix cases; exact and NS5 alignment; NS5 scalar stability and the selected approximation estimate; correct information timing; weight-decay and step bounds; finite moments; smoothness descent; the unconditional tracking recursion; initialization; the scalar telescoping inequality; schedule sums; conversion to the unweighted average; and comparison with deterministic or trajectory-dependent requested constants. No specialized external theorem remains an unproved dependency and no GT quality warning is needed.
