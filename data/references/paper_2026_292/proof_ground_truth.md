# Reference Proof

## Proof Structure

1. Establish feasibility after the first round and derive the local-to-global one-round inequality explicitly, including projection estimates, local drift, component telescoping, strong convexity, and endpoint averaging.
2. Apply the inequality at the bilevel solution for rounds starting at 2, bound the regularization contribution, and absorb the finite initial weighted objective value into the constant.
3. Apply Jensen to the prescribed full weighted average on the global domain. Because the initial point may be outside the constraint set, separately control the possible negative objective gap using a feasible tail average and bounded supporting subgradients.
4. Estimate the polynomial sums and combine the upper and lower bounds.

## Complete Proof

All parameters and problem data are fixed throughout the asymptotic argument. Constants below are independent of K. The client and component indices have their ordinary positive integer counting interpretation, so m>=S>=1.

### Existence and Feasibility

The stated Lipschitz bounds give continuity of F and H on X. Thus F attains its minimum on the nonempty compact set X. Its minimizer set is nonempty, compact, and convex. H attains a minimum there, and strong convexity makes that minimizer unique. This is x^star.

Each client performs at least one projected update. Therefore every first-round endpoint belongs to X, and convexity of X gives x_2 in X. Inductively, x_k and all local iterates in round k belong to X for k>=2. No such claim is made about x_1.

For completeness, the projection estimates used below follow directly from metric projection. If p=P_X(u), minimization of squared distance along each segment from p to z in X gives <u-p,z-p><=0. Expanding ||u-z||^2 then gives ||p-z||^2<=||u-z||^2. If p=P_X(u) and r=P_X(v), the two variational inequalities also give ||p-r||^2<=<u-v,p-r>, hence ||P_X(u)-P_X(v)||<=||u-v||.

### Explicit One-Round Inequality

Put
\[
A_1=C_f^2+\frac{2\lambda_1^2C_H^2}{m^2},\qquad
A_2=C_f+\frac{\lambda_1C_H}{m},\qquad
D=4m^3A_1+2m^2C_fA_2.
\]
The prescribed schedules have positive exponents, so lambda_k<=lambda_1. Fix k>=2 and z in X, and write
\[
V_k(z)=\|x_k-z\|^2,\qquad q_k=\frac{\lambda_k}{m},\qquad
\delta_{k,j}^i=x_{k,j}^i-x_k.
\]
Projection nonexpansiveness, with x_{k,j}^i in X, gives
\[
\|x_{k,j+1}^i-x_{k,j}^i\|
\le\gamma_k\|g_{k,j}^i+q_kH_k\|
\le\gamma_kA_2.
\]
Consequently,
\[
\|\delta_{k,j}^i\|\le(j-1)\gamma_kA_2\le j\gamma_kA_2,
\]
and, since j<=m,
\[
\|\delta_{k,j}^i\|^2
\le 2m^2\gamma_k^2(C_f^2+q_k^2C_H^2)
\le 2m^2\gamma_k^2A_1.\tag{1}
\]
The squared-distance projection estimate gives the correctly signed expansion
\[
\begin{aligned}
\|x_{k,j+1}^i-z\|^2
\le{}&\|x_{k,j}^i-z\|^2
-2\gamma_k\langle g_{k,j}^i,x_{k,j}^i-z\rangle\\
&-2\gamma_kq_k\langle H_k,x_{k,j}^i-z\rangle
+\gamma_k^2\|g_{k,j}^i+q_kH_k\|^2.
\end{aligned}\tag{2}
\]
Convexity and strong convexity give
\[
\langle g_{k,j}^i,x_{k,j}^i-z\rangle
\ge f_j^i(x_{k,j}^i)-f_j^i(z),
\]
\[
\langle H_k,x_k-z\rangle
\ge H(x_k)-H(z)+\frac{\mu_H}{2}V_k(z).
\]
Also,
\[
\|g_{k,j}^i+q_kH_k\|^2\le2C_f^2+2q_k^2C_H^2,
\]
\[
-2\gamma_kq_k\langle H_k,\delta_{k,j}^i\rangle
\le\|\delta_{k,j}^i\|^2+2\gamma_k^2q_k^2C_H^2,
\]
where the last inequality is a permissible weakening of 2ab<=a^2+b^2. Finally, the component Lipschitz bound yields
\[
2\gamma_k\big(f_j^i(x_k)-f_j^i(x_{k,j}^i)\big)
\le2j\gamma_k^2C_fA_2.
\]
Substituting these estimates and (1) into (2) gives
\[
\begin{aligned}
\|x_{k,j+1}^i-z\|^2
\le{}&\|x_{k,j}^i-z\|^2
-\frac{\gamma_k\lambda_k\mu_H}{m}V_k(z)
+2(m^2+1)\gamma_k^2A_1
+2j\gamma_k^2C_fA_2\\
&+2\gamma_k\left[
\left(f_j^i(z)+q_kH(z)\right)
-\left(f_j^i(x_k)+q_kH(x_k)\right)
\right].
\end{aligned}\tag{3}
\]
Sum (3) over j=1,...,I_i. The local squared distances telescope, x_{k,1}^i=x_k, and
\[
2(m^2+1)I_i\le4m^2I_i,\qquad
\sum_{j=1}^{I_i}j=\frac{I_i(I_i+1)}2\le m^2.
\]
Hence
\[
\begin{aligned}
\|x_k^i-z\|^2
\le{}&\left(1-\frac{I_i\gamma_k\lambda_k\mu_H}{m}\right)V_k(z)
+\gamma_k^2\left(4m^2I_iA_1+2m^2C_fA_2\right)\\
&+2\gamma_k\left[
\left(F_i(z)+\frac{I_i\lambda_k}{m}H(z)\right)
-\left(F_i(x_k)+\frac{I_i\lambda_k}{m}H(x_k)\right)
\right].
\end{aligned}\tag{4}
\]
Average (4) over clients and use convexity of the squared norm for the server average. Because sum_i I_i=m, this gives
\[
\begin{aligned}
V_{k+1}(z)
\le{}&\left(1-\frac{\gamma_k\lambda_k\mu_H}{S}\right)V_k(z)
+\gamma_k^2\left(\frac{4m^3}{S}A_1+2m^2C_fA_2\right)\\
&+\frac{2\gamma_k}{S}\left[(F+\lambda_kH)(z)-(F+\lambda_kH)(x_k)\right].
\end{aligned}\tag{5}
\]
Since V_k(z)>=0 and m>=S>=1, weakening the contraction and error terms yields
\[
V_{k+1}(z)
\le\left(1-\frac{\gamma_k\lambda_k\mu_H}{m}\right)V_k(z)
+D\gamma_k^2
+\frac{2\gamma_k}{S}\left[(F+\lambda_kH)(z)-(F+\lambda_kH)(x_k)\right].\tag{6}
\]
Neither the derivation nor this weakening requires a nonnegative contraction coefficient.

### Telescoping and the Initial Round

For k>=2, let G_k=F(x_k)-F(x^star). Feasibility gives G_k>=0. Taking z=x^star in (6), discarding the nonpositive term -(gamma_k lambda_k mu_H/m)V_k(x^star), and using H(x^star)-H(x_k)<=2C_H gives
\[
\gamma_kG_k
\le\frac S2\left(V_k(x^star)-V_{k+1}(x^star)\right)
+\frac S2D\gamma_k^2+2C_H\gamma_k\lambda_k.\tag{7}
\]
The first round is well-defined, and its endpoint lies in X. The value G_1 is finite because the functions are real-valued on R^n, but G_1 need not be nonnegative.

Since 2a=1+epsilon>1, sum_{k=2}^infinity gamma_k^2 is finite. Set
\[
M=\frac S2V_2(x^star)
+\frac S2D\sum_{k=2}^{\infty}\gamma_k^2
+\max\{\gamma_1G_1,0\}.
\]
Summing (7) from 2 through K, using V_{K+1}>=0, and adding gamma_1G_1 gives, for every K>=2,
\[
\sum_{k=1}^K\gamma_k\big(F(x_k)-F(x^star)\big)
\le M+2C_H\sum_{k=1}^K\gamma_k\lambda_k.\tag{8}
\]

### The Prescribed Average and Its Possible Negative Gap

Write W_K=sum_{k=1}^K gamma_k. F is convex on all of R^n, so Jensen applies to the prescribed average even if it is outside X:
\[
F(\bar x_K)-F(x^star)
\le\frac{M+2C_H\sum_{k=1}^K\gamma_k\lambda_k}{W_K}.\tag{9}
\]
It would be incorrect to assert that bar x_K belongs to X solely by convexity of X, because x_1 may be outside X.

To control the possible negative part, define for K>=2
\[
y_K=\frac{\sum_{k=2}^K\gamma_kx_k}{W_K-\gamma_1}\in X,
\qquad
\tau_K=\frac{\gamma_1}{W_K}.
\]
Then
\[
\bar x_K=\tau_Kx_1+(1-\tau_K)y_K.
\]
Compactness gives the finite number R=max_{y in X}||x_1-y||. At y_K choose component subgradients h_j^i in partial f_j^i(y_K) with ||h_j^i||<=B_f, as permitted by the stated bounds on X. Summing their supporting inequalities gives
\[
\begin{aligned}
F(\bar x_K)
&\ge F(y_K)+\left\langle\sum_{i,j}h_j^i,\bar x_K-y_K\right\rangle\\
&\ge F(x^star)-mB_f\tau_K\|x_1-y_K\|\\
&\ge F(x^star)-\frac{mB_fR\gamma_1}{W_K}.
\end{aligned}\tag{10}
\]
Thus (9) and (10) provide a two-sided bound, without modifying the initial point or the averaging rule.

### Polynomial Sums

The exponents satisfy
\[
0<a<1,\qquad b>0,\qquad 2a>1,\qquad
a+b=1-\frac\varepsilon2<1,\qquad
1-a-b=\frac\varepsilon2>0.
\]
For any fixed p in (0,1), comparison with the integral of t^{-p} gives sum_{k=1}^K k^{-p}=Theta(K^{1-p}). Applying this with p=a and p=a+b yields
\[
W_K=\Theta(K^{1-a}),\qquad
\sum_{k=1}^K\gamma_k\lambda_k=O(K^{1-a-b}).
\]
Consequently, (9) gives
\[
F(\bar x_K)-F(x^star)
\le O(K^{-(1-a)})+O(K^{-b})=O(K^{-b}),
\]
while (10) bounds its negative part by O(K^{-(1-a)}). Because 1-a>b, that negative part is o(K^{-b}). Combining the two bounds proves
\[
\left|F(\bar x_K)-F(x^star)\right|=O(K^{-b})
=O\!\left(K^{-(1/2-\varepsilon)}\right).
\]
This proves the stated target. The prescribed initial product restriction is satisfied throughout; the rate argument does not need an additional nonnegativity restriction on the contraction coefficient.
