# Reference Proof

## Proof Structure

Establish positivity of the diagonal metrics and the directional descent estimate. Decompose the energy difference using the previous auxiliary point, derive the objective/momentum estimate explicitly, and bound the adaptive metric forcing coordinatewise. Apply directional descent again when replacing the uncorrected next energy by the auxiliary next energy. The parameter coupling makes the residual nonpositive, and iteration gives the product bound.

## Complete Proof

Write \(g_k=\nabla f(x_k)\), \(G_k=\operatorname{diag}(g_k)\), \(z_k=(x_k,y_k)\), and \(E_k=E(z_k^+,P_k)\).

### 1. Metric positivity and directional descent

The metric recursion gives
\[
P_{k+1}=\frac{P_k+\alpha_k\gamma_kP_k^{-1}G_{k+1}^2}{1+\alpha_k}.
\]
If \(P_k\) is positive diagonal, each diagonal entry of the numerator is strictly positive: its first summand is positive and its second summand is nonnegative. Thus induction from \(P_0\) proves that every \(P_k\) is positive diagonal. Together with the supplied \(P_{-1}\), all inverses and weighted norms used below are well defined.

Let \(P\) be positive diagonal, \(g=\nabla f(x)\), and \(x^+=x-\eta P^{-1}g\). The smoothness upper bound gives
\[
f(x^+)\le f(x)-\eta g^\top P^{-1}g
 +\frac{L\eta^2}{2}g^\top P^{-2}g.
\]
For \(g\ne0\), the denominator defining \(\bar\eta(P,g)\) is strictly positive. Whenever \(0<\eta\le\bar\eta(P,g)\), the last display implies
\[
f(x^+)\le f(x)-\frac{\eta}{2}\|g\|_{P^{-1}}^2.
\tag{1}
\]
In particular, this applies to the prescribed equality choice. If \(g=0\), then \(x^+=x\) and (1) holds for every positive \(\eta\), without evaluating the quotient.

### 2. The exact decomposition and objective/momentum bound

Fix \(k\ge0\), and abbreviate \(\alpha=\alpha_k\), \(h=g_{k+1}\), and \(Q=h^\top P_k^{-1}h\ge0\). Define
\[
\begin{aligned}
I_1&=E(z_{k+1}^+,P_{k+1})-E(z_{k+1},P_{k+1}),\\
I_2&=E(z_{k+1},P_{k+1})-E(z_{k+1},P_k),\\
I_3&=E(z_{k+1},P_k)-E(z_k^+,P_k).
\end{aligned}
\]
These definitions give \(E_{k+1}-E_k=I_1+I_2+I_3\).

Using \(\eta_k=\alpha_k\beta_k\), the x-update yields
\[
x_{k+1}-x_k^+=\alpha(y_k-x_{k+1}).
\tag{2}
\]
Set \(\Delta y=y_{k+1}-y_k=-\alpha P_k^{-1}h\). The definition of \(D_f\) and the quadratic identity for the momentum energy give the exact expansion
\[
\begin{aligned}
I_3={}&\langle h,x_{k+1}-x_k^+\rangle-D_f(x_k^+,x_{k+1})\\
&+\langle P_k(y_{k+1}-x^*),\Delta y\rangle
-\frac12\|\Delta y\|_{P_k}^2\\
={}&-\alpha\langle h,x_{k+1}-x^*\rangle
+\alpha\langle h,y_k-y_{k+1}\rangle\\
&-D_f(x_k^+,x_{k+1})-\frac12\|\Delta y\|_{P_k}^2.
\end{aligned}
\tag{3}
\]
Convexity implies
\[
\langle h,x_{k+1}-x^*\rangle\ge f(x_{k+1})-f(x^*),
\qquad D_f(x_k^+,x_{k+1})\ge0.
\]
Also, expanding the nonnegative square
\(\|y_k-y_{k+1}-\alpha P_k^{-1}h\|_{P_k}^2\) gives
\[
\alpha\langle h,y_k-y_{k+1}\rangle
\le\frac{\alpha^2}{2}Q+\frac12\|y_k-y_{k+1}\|_{P_k}^2.
\]
Substitution into (3) cancels the squared momentum increment and proves
\[
I_3\le-\alpha\bigl(f(x_{k+1})-f(x^*)\bigr)+\frac{\alpha^2}{2}Q.
\tag{4}
\]

### 3. Auxiliary descent and adaptive metric forcing

Applying (1) at \(x_{k+1}\), with metric \(P_k\), gives
\[
I_1\le-\frac{\eta_{k+1}}2Q.
\tag{5}
\]
This also holds when \(h=0\).

Put \(v=y_{k+1}-x^*\). The metric update gives
\[
I_2=\frac12v^\top(P_{k+1}-P_k)v
=-\frac\alpha2v^\top P_{k+1}v
+\frac{\alpha\gamma_k}{2}v^\top P_k^{-1}G_{k+1}^2v.
\]
Writing \(p_{k,i}=(P_k)_{ii}>0\) and using \(\|v\|_\infty\le R\), we obtain
\[
v^\top P_k^{-1}G_{k+1}^2v
=\sum_{i=1}^d\frac{v_i^2h_i^2}{p_{k,i}}
\le R^2\sum_{i=1}^d\frac{h_i^2}{p_{k,i}}=R^2Q.
\tag{6}
\]
Combining (4), (5), and (6) therefore yields
\[
E_{k+1}-E_k
\le-\alpha E(z_{k+1},P_{k+1})
+\frac{\alpha^2+\alpha\gamma_kR^2-\eta_{k+1}}2Q.
\tag{7}
\]
The uncorrected and auxiliary energies in this display have the same momentum term. Consequently (1) also gives
\[
E(z_{k+1},P_{k+1})\ge E_{k+1}+\frac{\eta_{k+1}}2Q.
\]
Because \(\alpha>0\), inserting this lower bound in the negative energy term of (7) proves
\[
E_{k+1}-E_k
\le-\alpha E_{k+1}
+\frac{\alpha^2+\alpha\gamma_kR^2-\eta_{k+1}(1+\alpha)}2Q.
\tag{8}
\]
Equivalently, the residual is \(\tfrac12h^\top M_{k+1}h\), where
\[
M_{k+1}=\bigl(\alpha_k^2+\alpha_k\gamma_kR^2
-\eta_{k+1}(1+\alpha_k)\bigr)P_k^{-1}.
\]
Here the expression is a quadratic form; no norm with a negative metric is needed.

### 4. Cancellation and iteration

The parameter identities give \(\gamma_kR^2=\alpha_k\) and \(\eta_k=2\alpha_k^2\). The consistency assumption therefore implies
\[
\alpha_k^2+\alpha_k\gamma_kR^2-\eta_{k+1}(1+\alpha_k)
=2\alpha_k^2-\eta_{k+1}(1+\alpha_k)\le0.
\]
Since \(Q\ge0\), (8) yields
\[
(1+\alpha_k)E_{k+1}\le E_k.
\]
All factors \(1+\alpha_k\) are positive. Iterating from index \(0\) through index \(k\) proves
\[
E(z_{k+1}^+,P_{k+1})
\le E(z_0^+,P_0)\prod_{j=0}^k(1+\alpha_j)^{-1}.
\]
Every step remains valid for zero gradients, including an identically constant objective. The assumption uses a positive bound R, not necessarily the smallest bound, so a trajectory with zero momentum distance creates no division by zero.
