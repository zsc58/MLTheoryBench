# Reference Proof

## Theorem-Critical Obligations

1. Verify the needed integrability and derive response sensitivity by differentiating the stationary equation for the same fixed selection map.
2. Calculate the trace normalization exactly and establish nonnegativity and integrability of the effective dimension.
3. State the standard-independent product Brascamp-Lieb inequality, check its hypotheses, and combine it with replace-one centering to prove prediction stability.
4. Derive the fresh-response/replace-one identity, expand square loss with the correct residual and sign, apply Cauchy-Schwarz with the sample-index normalization, and finish with Young's inequality.

All four obligations are closed below. The only external theorem used is the standard-independent variance inequality recorded as theory_017. No paper-specific cited sensitivity or stability result is assumed.

## Step 1: Integrability and Response Sensitivity

Write $h_j(y)=f_j(\theta_y)$. First, the response laws have finite second moments. Indeed, for any $a_i\in I_i$, the assumption $V_i''\ge\alpha$ implies
\[
V_i(z)\ge V_i(a_i)+V_i'(a_i)(z-a_i)+\frac\alpha2(z-a_i)^2\qquad(z\in I_i).
\]
Thus the noise density is bounded by a constant times an integrable Gaussian-shaped function on its support, including after multiplication by $z^2$. Since $f^*(x_i)$ is fixed and finite, $\mathbb E Y_i^2<\infty$.

The assumed $\mathbb E h_i(Y)^2<\infty$ and the inequality $(u-v)^2\le2u^2+2v^2$ imply
\[
\mathbb E\widehat L(\theta_Y)<\infty,\qquad
\mathbb E L(\theta_Y)<\infty.
\]
Also, $Y^{(i)}$ has the same law as $Y$, so $h_i(Y^{(i)})$ has a finite second moment. These facts justify the risk differences and square-loss expectations used below.

Define
\[
F(\theta,y)=\nabla_\theta\widehat L_{\lambda,y}(\theta)
=\frac1n\sum_{j=1}^n(f_j(\theta)-y_j)\nabla f_j(\theta)+\lambda\theta.
\]
At every selected point, $F(\theta_y,y)=0$ and
\[
D_\theta F(\theta_y,y)=H_y,
\qquad
\partial_{y_k}F(\theta_y,y)=-\frac1n\nabla f_k(\theta_y).
\]
The second parameter derivatives at the selected point and the $C^1$ selection justify differentiating this identity. Consequently,
\[
H_y\,\partial_{y_k}\theta_y=\frac1n\nabla f_k(\theta_y).
\]
Positive definiteness permits inversion, giving
\[
\partial_{y_k}\theta_y=\frac1n H_y^{-1}\nabla f_k(\theta_y),
\qquad
\partial_{y_k}h_j(y)=\frac1n\nabla f_j(\theta_y)^\top H_y^{-1}\nabla f_k(\theta_y). \tag{1}
\]
This calculation is local at each selected point; it does not require global continuous second differentiability of the predictor or a uniform lower bound on the eigenvalues of $H_y$.

## Step 2: Effective-Dimension Identity and Finiteness

At $Y$, put $g_j=\nabla f_j(\theta_Y)$. Differentiating the empirical objective in the parameter gives
\[
H_Y=\frac1n\sum_{j=1}^n\left[g_jg_j^\top+(f_j(\theta_Y)-Y_j)\nabla^2 f_j(\theta_Y)\right]+\lambda I_p
=G_Y+\Delta_Y+\lambda I_p.
\]
Because $H_Y^{-1}$ is symmetric, finite-dimensional trace algebra yields
\[
\begin{aligned}
\sum_{j=1}^n\|\nabla_y h_j(Y)\|_2^2
&=\frac1{n^2}\sum_{j,k=1}^n(g_j^\top H_Y^{-1}g_k)^2\\
&=\operatorname{tr}(H_Y^{-1}G_YH_Y^{-1}G_Y)\\
&=d_{\rm eff}(\theta_Y;\lambda). \tag{2}
\end{aligned}
\]
For example, the middle equality follows by writing each squared scalar as $\operatorname{tr}(H_Y^{-1}g_kg_k^\top H_Y^{-1}g_jg_j^\top)$ and then summing. No commutation of $H_Y$ and $G_Y$ is used.

Equation (2) proves $d_{\rm eff}\ge0$, even though $H_Y^{-1}G_Y$ need not be symmetric. The assumed response-gradient second moments, summed over the finite set of prediction indices, give
\[
D:=\mathbb E d_{\rm eff}(\theta_Y;\lambda)<\infty. \tag{3}
\]

## Step 3: Variance Control and Prediction Stability

Use the following standard-independent form of the product Brascamp-Lieb inequality, stated in the supplied source at L000395-L000396: for independent coordinates with densities proportional to $e^{-V_k}$ on interval supports, and a locally Lipschitz function $u$ with $\mathbb E u^2<\infty$ and square-integrable gradient,
\[
\operatorname{Var}(u(\xi))
\le\mathbb E\sum_{k=1}^n\frac{(\partial_{\xi_k}u(\xi))^2}{V_k''(\xi_k)}
\le\frac1\alpha\mathbb E\|\nabla_\xi u(\xi)\|_2^2. \tag{4}
\]
Here interval supports are convex, the potentials have the stipulated positive second derivatives, and the last right-hand side is finite. Local Lipschitz regularity and the stated function and gradient moments provide the required Sobolev integrability.

Apply (4) to $u(\xi)=h_i(f^*(x_1)+\xi_1,\ldots,f^*(x_n)+\xi_n)$. Translation preserves local Lipschitz regularity and the response derivatives. The task's moment assumptions verify the remaining hypotheses. By (1),
\[
\operatorname{Var}(h_i(Y))
\le\frac1{\alpha n^2}\mathbb E\sum_{k=1}^n(g_i^\top H_Y^{-1}g_k)^2. \tag{5}
\]

For fixed $i$, the variables $h_i(Y)$ and $h_i(Y^{(i)})$ have the same marginal law because the same deterministic selection map is used and $Y^{(i)}$ has the law of $Y$. Let $m_i=\mathbb E h_i(Y)$. Then
\[
\begin{aligned}
\mathbb E[(h_i(Y)-h_i(Y^{(i)}))^2]
&\le2\mathbb E[(h_i(Y)-m_i)^2]+2\mathbb E[(h_i(Y^{(i)})-m_i)^2]\\
&=4\operatorname{Var}(h_i(Y)). \tag{6}
\end{aligned}
\]
This argument does not claim unconditional independence of the two predictions.

Define
\[
S:=\frac1n\sum_{i=1}^n\mathbb E[(h_i(Y)-h_i(Y^{(i)}))^2].
\]
Combining (5), (6), and (2),
\[
S\le\frac4{\alpha n^3}\mathbb E\sum_{i,k=1}^n(g_i^\top H_Y^{-1}g_k)^2
=\frac{4D}{\alpha n}. \tag{7}
\]
This is the requested prediction-stability bound.

## Step 4: Exact Generalization Calculation and Young's Inequality

For every $i$, independence of the response coordinates and independence of $Y_i'$ from the entire training vector give
\[
(Y^{(i)},Y_i)\overset{d}{=}(Y,Y_i'). \tag{8}
\]
Indeed, conditional on the unchanged coordinates, $Y_i$ and $Y_i'$ are independent copies with the same coordinate law and may be interchanged. Identical laws across different indices are not required.

Let $\ell(a,y)=\tfrac12(a-y)^2$. From the definition of $L$ and (8),
\[
\begin{aligned}
\mathbb E[L(\theta_Y)-\widehat L(\theta_Y)]
&=\frac1n\sum_{i=1}^n\mathbb E[\ell(h_i(Y),Y_i')-\ell(h_i(Y),Y_i)]\\
&=\frac1n\sum_{i=1}^n\mathbb E[\ell(h_i(Y^{(i)}),Y_i)-\ell(h_i(Y),Y_i)]. \tag{9}
\end{aligned}
\]
All expectations are finite by Step 1. Thus the replace-one identity is derived here rather than left as an external proof obligation.

Set
\[
b_i=h_i(Y),\qquad a_i=h_i(Y^{(i)}),\qquad r_i=b_i-Y_i,\qquad \delta_i=a_i-b_i,
\]
and let $A=\mathbb E\widehat L(\theta_Y)$. The exact quadratic expansion is
\[
\ell(a_i,Y_i)-\ell(b_i,Y_i)=r_i\delta_i+\frac12\delta_i^2.
\]
Consequently, (9) becomes
\[
\mathbb E[L(\theta_Y)-\widehat L(\theta_Y)]
=\frac1n\sum_{i=1}^n\mathbb E[r_i\delta_i]+\frac S2. \tag{10}
\]
Cauchy-Schwarz first in probability and then over the sample index gives
\[
\begin{aligned}
\frac1n\sum_i\mathbb E[r_i\delta_i]
&\le\frac1n\sum_i\sqrt{\mathbb E r_i^2\,\mathbb E\delta_i^2}\\
&\le\sqrt{\left(\frac1n\sum_i\mathbb E r_i^2\right)
\left(\frac1n\sum_i\mathbb E\delta_i^2\right)}\\
&=\sqrt{2AS}. \tag{11}
\end{aligned}
\]
In particular, this calculation requires no independence between a residual and its prediction change.

Substituting (7) into (10)-(11) yields
\[
\mathbb E[L(\theta_Y)-\widehat L(\theta_Y)]
\le\sqrt{\frac{8AD}{\alpha n}}+\frac{2D}{\alpha n},
\]
which is the stated square-root generalization bound.

Finally, put $q=D/(\alpha n)\ge0$. For each $\eta>0$, Young's inequality gives
\[
\sqrt{8Aq}=2\sqrt{A\,(2q)}\le\eta A+\frac{2q}{\eta}.
\]
Adding $2q$ proves
\[
\mathbb E[L(\theta_Y)-\widehat L(\theta_Y)]
\le\eta\,\mathbb E\widehat L(\theta_Y)
+\left(2+\frac2\eta\right)\frac{\mathbb E d_{\rm eff}(\theta_Y;\lambda)}{\alpha n}.
\]
No step divides by the training loss or effective dimension, so their zero cases are included. The argument also includes $n=1$, singular $G_Y$, and $\lambda=0$ whenever the selected Hessians satisfy the stated positive-definiteness assumption.

## Source Closure

The response derivative is recovered directly from theory_003 and L000297-L000303. The trace and stability calculations follow theory_004, theory_005, and the standard-independent theory_017, with its hypotheses verified above. The complete square-loss calculation is recovered from theory_006 and L000331-L000355. The fresh-response definitions are recorded in the completed theory_001. There are no unresolved private ground-truth obligations.
