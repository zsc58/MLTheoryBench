# Reference Proof

## Proof Structure

Establish the iterate displacement identity and polar alignment, control the population-gradient drift and stochastic EMA error separately, telescope the smoothness inequality, and tune the resulting bound. For the log-free specialization, remove harmonic drift from both the descent and tracking calculations. Treat zero initial gap using admissible positive steps rather than an unattained zero-step optimizer.

## Complete Proof

Write
\[
g_t=\nabla f(Y_t),\qquad S_t=Z_t-Y_t,\qquad \alpha=1-\mu\in(0,1],\qquad h_T=\log(eT).
\]
All parameters in a run are deterministic. The conditional oracle hypotheses do not require independent batches: the martingale-difference property with respect to the stated history is sufficient.

### 1. Geometry, displacement, and well-defined expectations

Since \(X_0=Z_0\) and each update of \(X_t\) is a convex combination of \(X_t\) and \(Z_{t+1}\), the centered-ball assumption implies
\[
\|X_t\|_F,\|Y_t\|_F\le D/2,
\qquad
\|Y_t-W_\star\|_F,\|Z_t-W_\star\|_F\le D.
\]
Consequently,
\[
\|S_t\|_F\le2D,\qquad \|g_t\|_F\le LD. \tag{1}
\]
The first bound is deliberately loose, matching the requested constants.

The defining recursions give
\[
S_t=\beta(Z_t-X_t),\qquad
S_{t+1}=\frac{t}{t+1}(S_t-\beta\eta P_t).
\]
Using \(Y_t=Z_t-S_t\), it follows that
\[
d_t:=Y_{t+1}-Y_t
=\frac{S_t}{t+1}-\eta a_tP_t,
\qquad
a_t=1-\beta+\frac{\beta}{t+1}\in[1-\beta,1]. \tag{2}
\]

For the supported polar factor, its nonzero singular values are one, so
\[
\|P_t\|_{\rm op}\le1,\qquad \|P_t\|_F\le\sqrt r,
\qquad \langle M_t,P_t\rangle=\|M_t\|_*.
\]
These statements also hold when \(M_t=0\). Here \(\|\cdot\|_{\rm op}\) is the induced Euclidean operator norm and the inner product is the Frobenius inner product. The supported polar map is measurable; for example, it is the pointwise limit, as \(\varepsilon\downarrow0\), of the continuous maps \(M\mapsto M(M^\top M+\varepsilon I)^{-1/2}\). Thus the stated history indeed contains the previously constructed iterates.

For any matrix \(H\), Cauchy--Schwarz applied to its at most \(r\) singular values gives
\[
\|H\|_*\le\sqrt r\|H\|_F.
\]
If \(H=\sum_j s_j u_jv_j^\top\), then
\[
|\langle H,Q\rangle|
\le\sum_j s_j|u_j^\top Qv_j|
\le\|H\|_*\|Q\|_{\rm op}.
\]
This verifies the operator--nuclear duality inequality needed below, including its hypotheses, directly from the SVD.

Frobenius smoothness implies the descent inequality
\[
f(A+H)\le f(A)+\langle\nabla f(A),H\rangle+\frac L2\|H\|_F^2. \tag{3}
\]
Indeed, integrate \(\langle\nabla f(A+sH)-\nabla f(A),H\rangle\) over \(s\in[0,1]\) and bound it by \(Ls\|H\|_F^2\). In particular, taking \(A=W_\star\) shows
\[
0\le f(Y_t)-f_\star\le LD^2/2.
\]
Hence the function values and gradients used in expectations are integrable. The variance hypothesis and (1) also give \(\mathbb E\|G_t\|_F^2\le2L^2D^2+2\sigma^2/B\), so the moment calculations below are justified.

### 2. Polar alignment

Decomposition, duality, and the reverse triangle inequality give
\[
\begin{aligned}
\langle g_t,P_t\rangle
&=\|M_t\|_*+\langle g_t-M_t,P_t\rangle\\
&\ge\|M_t\|_*-\|g_t-M_t\|_*\\
&\ge\|g_t\|_*-2\|g_t-M_t\|_*.
\end{aligned} \tag{4}
\]

### 3. Stochastic EMA error

Define
\[
C_0=g_0,\qquad C_t=\mu C_{t-1}+\alpha g_t\quad(t\ge1),\qquad E_t=C_t-M_t.
\]
Then \(E_0=g_0-G_0\), and for \(t\ge1\),
\[
E_t=\mu E_{t-1}+\alpha(g_t-G_t).
\]
The matrix \(E_{t-1}\) is \(\mathcal F_t\)-measurable, while \(\mathbb E[g_t-G_t\mid\mathcal F_t]=0\). Thus the conditional cross term vanishes and
\[
\mathbb E[\|E_t\|_F^2\mid\mathcal F_t]
\le\mu^2\|E_{t-1}\|_F^2+\alpha^2\frac{\sigma^2}{B}.
\]
Starting from \(\mathbb E\|E_0\|_F^2\le\sigma^2/B\), iteration yields
\[
\mathbb E\|E_t\|_F^2
\le\frac{\sigma^2}{B}\left(\mu^{2t}+\alpha^2\sum_{j=0}^{t-1}\mu^{2j}\right)
=\frac{\sigma^2}{B}\left(\mu^{2t}+\frac{\alpha}{1+\mu}(1-\mu^{2t})\right).
\]
For \(t=0\), the sum is empty and \(\mu^0=1\), including when \(\mu=0\). Taking square roots and using Jensen's inequality gives
\[
\mathbb E\|E_t\|_F
\le\frac{\sigma}{\sqrt B}\left(\mu^t+\sqrt{\frac{\alpha}{2-\alpha}}\right).
\]
Since \(\sum_{t=0}^{T-1}\mu^t\le1/\alpha\),
\[
\frac1T\sum_{t=0}^{T-1}\mathbb E\|E_t\|_*
\le\sqrt r\left[\frac{\sigma}{\alpha T\sqrt B}
+\sqrt{\frac{\alpha}{2-\alpha}}\frac{\sigma}{\sqrt B}\right]. \tag{5}
\]

### 4. Population-gradient drift and tracking

Let \(A_t=\|g_t-C_t\|_*\), so \(A_0=0\). For \(t\ge1\),
\[
A_t\le\mu\|g_t-g_{t-1}\|_*+\mu A_{t-1}.
\]
By (1), (2), and smoothness,
\[
\|g_t-g_{t-1}\|_*
\le\sqrt rL\|Y_t-Y_{t-1}\|_F
\le\frac{2\sqrt rLD}{t}+Lr\eta.
\]
Write the last upper bound as \(b_t\). Unrolling the recursion and reversing the finite sums gives
\[
\begin{aligned}
\frac1T\sum_{t=0}^{T-1}A_t
&\le\frac{\mu}{T}\sum_{s=1}^{T-1}b_s\sum_{t=s}^{T-1}\mu^{t-s}\\
&\le\frac{\mu}{\alpha T}\sum_{s=1}^{T-1}\left(\frac{2\sqrt rLD}{s}+Lr\eta\right)\\
&\le\frac{\mu Lr\eta}{\alpha}
+\frac{2\mu\sqrt rLDh_T}{\alpha T}.
\end{aligned}
\]
This also holds for \(T=1\), when the sums over \(s\) are empty. Since \(g_t-M_t=(g_t-C_t)+E_t\), (5) implies
\[
\frac1T\sum_{t=0}^{T-1}\mathbb E\|g_t-M_t\|_*
\le\frac{\mu Lr\eta}{\alpha}
+\frac{2\mu\sqrt rLDh_T}{\alpha T}
+\sqrt r\left[\frac{\sigma}{\alpha T\sqrt B}
+\sqrt{\frac{\alpha}{2-\alpha}}\frac{\sigma}{\sqrt B}\right]. \tag{6}
\]

### 5. Descent and the explicit finite-time bound

Apply (3) with the displacement (2). Its linear drift term is bounded by \(2LD^2/(t+1)\). If \(e_t=\|g_t-M_t\|_*\), (4) and the two bounds on \(a_t\) give
\[
-\eta a_t\langle g_t,P_t\rangle
\le-\eta a_t\|g_t\|_*+2\eta a_te_t
\le-\eta(1-\beta)\|g_t\|_*+2\eta e_t.
\]
This step does not assume that \(\langle g_t,P_t\rangle\) is nonnegative. Also,
\[
\|d_t\|_F\le\frac{2D}{t+1}+\eta\sqrt r.
\]
Expanding its squared upper bound in (3) therefore yields
\[
\begin{aligned}
\eta(1-\beta)\|g_t\|_*
\le{}& f(Y_t)-f(Y_{t+1})
+\frac{2LD^2}{t+1}+\frac{2LD^2}{(t+1)^2}\\
&+\frac{2\eta\sqrt rLD}{t+1}
+\frac{Lr\eta^2}{2}+2\eta e_t.
\end{aligned} \tag{7}
\]
Sum from \(t=0\) to \(T-1\), take expectations, and use the deterministic initial gap and \(f(Y_T)\ge f_\star\). The scalar bounds
\[
\sum_{k=1}^T\frac1k\le1+\log T=h_T,
\qquad
\sum_{k=1}^T\frac1{k^2}\le\sum_{k=1}^{\infty}\frac1{k^2}=\frac{\pi^2}{6}
\]
apply for every integer \(T\ge1\). Dividing by \((1-\beta)T\eta\) and inserting (6) proves
\[
\begin{aligned}
\frac1T\sum_{t=0}^{T-1}\mathbb E\|\nabla f(Y_t)\|_*
\le{}&\frac{\Delta+2LD^2(h_T+\pi^2/6)}{(1-\beta)T\eta}
+\frac{Lr\eta}{2(1-\beta)}
+\frac{2\mu Lr\eta}{(1-\beta)(1-\mu)}\\
&+\frac{2\sqrt rLDh_T}{(1-\beta)T}\left(1+\frac{2\mu}{1-\mu}\right)
+\frac{2\sqrt r\sigma}{(1-\beta)\sqrt B}\sqrt{\frac{1-\mu}{1+\mu}}\\
&+\frac{2\sqrt r\sigma}{(1-\beta)(1-\mu)T\sqrt B}.
\end{aligned} \tag{8}
\]

### 6. Rates for fixed beta

Let \(R_T=T^{-1}\sum_{t<T}\mathbb E\|g_t\|_*\) for the run with horizon \(T\), and put
\[
K_T=\Delta+2LD^2(h_T+\pi^2/6).
\]
Because \(L,D>0\) and the problem data are fixed, \(K_T>0\) for all \(T\ge1\) and \(K_T=\Theta(h_T)\) as \(T\to\infty\). Equation (8) becomes
\[
R_T\le\frac1{1-\beta}\left[
\frac{K_T}{T\eta}
+\frac{Lr(4-3\alpha)}{2\alpha}\eta
+\frac{2\sqrt rLDh_T}{T}\frac{2-\alpha}{\alpha}
+\frac{2\sqrt r\sigma}{\sqrt B}\sqrt{\frac{\alpha}{2-\alpha}}
+\frac{2\sqrt r\sigma}{\alpha T\sqrt B}\right]. \tag{9}
\]
For fixed \(\alpha\in(0,1]\), the optimizer of the two \(\eta\)-dependent terms is
\[
\eta_T^\star(\alpha)=\sqrt{\frac{2K_T\alpha}{LrT(4-3\alpha)}}>0,
\]
and their sum at this choice is
\[
\sqrt{\frac{2K_TLr}{T}\frac{4-3\alpha}{\alpha}}. \tag{10}
\]

If \(\sigma>0\), choose
\[
\alpha_T=\min\left\{1,\ 2\sqrt{\frac{K_TLB}{\sigma^2T}}\right\},
\qquad \mu_T=1-\alpha_T,
\qquad \eta_T=\eta_T^\star(\alpha_T).
\]
These choices are admissible for every \(T\ge1\). For sufficiently large \(T\), \(\alpha_T=\Theta(\sqrt{h_T/T})\). The optimized expression (10) and the stationary EMA-noise term are each \(O((h_T/T)^{1/4})\). The harmonic tracking term is \(O(h_T/(T\alpha_T))=O(\sqrt{h_T/T})\), and the initialization-noise term is \(O(1/(T\alpha_T))=O((Th_T)^{-1/2})\). Both are of smaller order. Thus
\[
R_T=O((\log T/T)^{1/4}).
\]

If \(\sigma=0\), choose \(\mu_T=0\), so \(\alpha_T=1\), and
\[
\eta_T=\sqrt{\frac{2K_T}{LrT}}.
\]
Then (9) gives
\[
R_T\le\frac1{1-\beta}\left[\sqrt{\frac{2LrK_T}{T}}+\frac{2\sqrt rLDh_T}{T}\right]
=O(\sqrt{\log T/T}).
\]
These arguments also cover \(\Delta=0\), since \(K_T\) remains strictly positive.

### 7. Log-free rates and the zero-gap boundary

When \(\beta=0\), \(Y_t=Z_t\), \(S_t=0\), and \(Y_{t+1}-Y_t=-\eta P_t\). In the tracking calculation, this gives
\[
\|g_t-g_{t-1}\|_*\le Lr\eta,
\]
so the harmonic term in (6) is absent. In the descent calculation, (7) has none of its three terms involving \((t+1)^{-1}\) or \((t+1)^{-2}\). Telescoping these two sharpened calculations yields
\[
R_T\le\frac{\Delta}{T\eta}
+\frac{Lr(4-3\alpha)}{2\alpha}\eta
+\frac{2\sqrt r\sigma}{\sqrt B}\sqrt{\frac{\alpha}{2-\alpha}}
+\frac{2\sqrt r\sigma}{\alpha T\sqrt B}. \tag{11}
\]

Suppose first that \(\Delta>0\). For \(\sigma>0\), choose
\[
\alpha_T=\min\left\{1,\ 2\sqrt{\frac{\Delta LB}{\sigma^2T}}\right\},
\qquad \mu_T=1-\alpha_T,
\qquad \eta_T=\sqrt{\frac{2\Delta\alpha_T}{LrT(4-3\alpha_T)}}.
\]
Now \(\alpha_T=\Theta(T^{-1/2})\). The first two terms together and the stationary noise term in (11) are \(O(T^{-1/4})\), while the last term is \(O(T^{-1/2})\). Hence \(R_T=O(T^{-1/4})\). For \(\sigma=0\), first choose \(\mu_T=0\) and then \(\eta_T=\sqrt{2\Delta/(LrT)}\). Equation (11) gives
\[
R_T\le\sqrt{\frac{2Lr\Delta}{T}}=O(T^{-1/2}).
\]

It remains to treat \(\Delta=0\), without allowing a zero step or \(\mu_T=1\). If \(\sigma>0\), set
\[
\alpha_T=T^{-1/2},\qquad \mu_T=1-T^{-1/2},\qquad \eta_T=T^{-3/4}.
\]
The descent-gap term in (11) is zero, \(4-3\alpha_T\le4\), and \(2-\alpha_T\ge1\). Therefore
\[
R_T\le\left(2Lr+\frac{2\sqrt r\sigma}{\sqrt B}\right)T^{-1/4}
+\frac{2\sqrt r\sigma}{\sqrt B}T^{-1/2}
=O(T^{-1/4}).
\]
If \(\Delta=0\) and \(\sigma=0\), set \(\mu_T=0\) and \(\eta_T=T^{-1/2}\). Equation (11) gives
\[
R_T\le\frac{Lr}{2}T^{-1/2}.
\]
All these parameter choices satisfy \(\mu_T\in[0,1)\) and \(\eta_T>0\), including at \(T=1\). The rate assertions are conditional on the stated boundedness assumptions with horizon-independent constants; the tuning calculation does not prove those assumptions for the unprojected dynamics.

## Source-Local Repair Note

The source's positive-gap optimizers are retained where \(\Delta>0\). Its missing \(\Delta=0\) case is closed by the explicit positive-step choices above, using only its existing reduced bound. A noisy run need not remain optimal merely because its initial gap is zero. No positive-gap assumption is added to the public task, and no theorem-critical obligation remains unresolved.
