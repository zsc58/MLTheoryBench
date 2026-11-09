# Reference Proof

## Proof Structure

First establish that the replace-one assumptions imply integrability of the function. Construct its Doob martingale differences and obtain deterministic bounds on their conditional second and pth moments. Truncate those differences, control both the large-increment event and the centering bias, and retain the factor introduced by centering in the pth-moment estimate. Prove the finite-moment exponential estimate and apply it conditionally. Finally, evaluate the Chernoff bound in all four relevant regimes. Some regimes give a Gaussian bound and the others give an additional polynomial contribution; both contributions are needed for the stated conclusion.

## Complete Proof

### Step 1: Well-definedness and the martingale decomposition

If an empty indexing family is allowed, the function of the empty tuple is constant and the conclusion is immediate. Otherwise let n>=1. Write \(\mathbf X=(X_1,\ldots,X_n)\) and \(\mathbf X'=(X_1',\ldots,X_n')\). Replace the coordinates successively. Each mixed vector has the same product distribution as the original vector, so the assumed almost-sure replace-one inequality applies at each of these finitely many replacements. Thus
\[
|f(\mathbf X)-f(\mathbf X')|\leq\sum_{i=1}^n H_i(X_i,X_i')\quad\text{a.s.}
\]
Consequently,
\[
\mathbb E|f(\mathbf X)-f(\mathbf X')|^p\leq n^{p-1}A_p<\infty.
\]
The vectors \(\mathbf X\) and \(\mathbf X'\) are independent with the same product law. Applying Fubini to this nonnegative integrable function shows that there is a deterministic vector \(a\in\mathcal X^n\) such that
\[
\mathbb E|f(\mathbf X)-f(a)|^p<\infty.
\]
Since f is real-valued, f(a) is finite. The inequality \(|u+v|^p\leq2^{p-1}(|u|^p+|v|^p)\) now implies \(f(\mathbf X)\in L_p\), in particular \(\mathbb E|f(\mathbf X)|<\infty\). Also all second moments of the envelopes are finite because p>=2.

Set \(F_i=\sigma(X_1,\ldots,X_i)\), with \(F_0\) trivial, and define
\[
M_i=\mathbb E[f(\mathbf X)\mid F_i],\qquad D_i=M_i-M_{i-1},\qquad S=f(\mathbf X)-\mathbb Ef(\mathbf X).
\]
Then \(\mathbb E[D_i\mid F_{i-1}]=0\) and \(S=\sum_iD_i\). If \(g=f(\mathbf X)\) and \(g_i=f(X_1,\ldots,X_i',\ldots,X_n)\), independence gives
\[
\mathbb E[g_i\mid F_i]=\mathbb E[g\mid F_{i-1}],\qquad D_i=\mathbb E[g-g_i\mid F_i].
\]
All conditional expectations used here are now justified by integrability.

### Step 2: Deterministic conditional moment bounds and the zero case

For \(r\in\{2,p\}\), put
\[
h_{i,r}=\mathbb E[H_i(X_i,X_i')^r].
\]
Conditional Jensen and the tower property give
\[
\begin{aligned}
\mathbb E[|D_i|^r\mid F_{i-1}]
&\leq\mathbb E[|g-g_i|^r\mid F_{i-1}]\\
&\leq\mathbb E[H_i(X_i,X_i')^r\mid F_{i-1}]
=h_{i,r}\quad\text{a.s.}
\end{aligned}
\]
The final equality uses the independence of the pair \((X_i,X_i')\) from \(F_{i-1}\), together with the deterministic coordinate-pair dependence of H_i. Hence \(\sum_i\mathbb E|D_i|^r\leq A_r\).

If \(A_2=0\), every D_i vanishes almost surely, so S=0 almost surely. Every H_i also vanishes almost surely, hence \(A_p=0\), and the stated zero-denominator convention gives the desired conclusion. In what follows assume \(A_2>0\); this also implies \(A_p>0\).

### Step 3: Truncation, centering, and exceptional events

Fix z>0 and set
\[
y=\frac{pz}{4(p+2)},\qquad T_i=D_i\mathbf1_{\{|D_i|\leq y\}},\qquad \mu_i=\mathbb E[T_i\mid F_{i-1}],\qquad U_i=T_i-\mu_i.
\]
Write \(V=\sum_iU_i\) and \(B=A_p/y^p\). The U_i are F_i-measurable martingale differences. Since \(|T_i|\leq y\) and \(|\mu_i|\leq y\), they satisfy \(|U_i|\leq2y\).

Using the conditional mean-zero property of D_i,
\[
\mu_i=-\mathbb E[D_i\mathbf1_{\{|D_i|>y\}}\mid F_{i-1}],
\]
so
\[
|\mu_i|\leq y^{1-p}\mathbb E[|D_i|^p\mid F_{i-1}]\leq y^{1-p}h_{i,p}.
\]
Thus \(\sum_i|\mu_i|\leq A_p/y^{p-1}\) almost surely, with a deterministic right-hand side.

The conditional second moment obeys
\[
\mathbb E[U_i^2\mid F_{i-1}]
=\mathbb E[T_i^2\mid F_{i-1}]-\mu_i^2
\leq h_{i,2}.
\]
For the pth moment, centering must be accounted for:
\[
\begin{aligned}
\mathbb E[|U_i|^p\mid F_{i-1}]
&\leq2^{p-1}\bigl(\mathbb E[|T_i|^p\mid F_{i-1}]+|\mu_i|^p\bigr)\\
&\leq2^p\mathbb E[|T_i|^p\mid F_{i-1}]
\leq2^ph_{i,p}.
\end{aligned}
\]
Here the second inequality is conditional Jensen.

Let \(E_y=\{\max_i|D_i|>y\}\). Markov's inequality and the union bound give \(\mathbb P(E_y)\leq B\). Outside E_y, \(S=\sum_iT_i=V+\sum_i\mu_i\). Therefore
\[
\begin{aligned}
\mathbb P(|S|>z)
&\leq B+\mathbb P(|V|>z/2)+\mathbb P\left(\left|\sum_i\mu_i\right|>z/2\right)\\
&\leq B+\mathbb P(|V|>z/2)+\mathbf1_{\{A_p/y^{p-1}>z/2\}}\\
&\leq\left(1+\frac{2y}{z}\right)B+\mathbb P(|V|>z/2).
\end{aligned}
\]
The indicator in the second line is deterministic. This argument counts the common exceptional event only once.

### Step 4: A proved exponential estimate and its conditional iteration

We first establish the auxiliary estimate used below. Let W be a real random variable satisfying W<=b almost surely, where b>0, with \(\mathbb E|W|^p<\infty\). For t>0 define \(R_t(u)=e^{tu}-1-tu\). If \(u\leq p/t\), Taylor's formula gives
\[
R_t(u)=t^2u^2\int_0^1(1-s)e^{stu}\,ds\leq\frac{e^pt^2u^2}{2},
\]
because \(stu\leq\max\{tu,0\}\leq p\). This explicitly includes negative u.

For \(u>p/t\), the function \(R_t(u)/u^p\) is increasing. Indeed,
\[
\frac{d}{du}\left(\frac{e^{tu}-1-tu}{u^p}\right)
=\frac{(tu-p)e^{tu}+(p-1)tu+p}{u^{p+1}}>0.
\]
Consequently, on \(p/t<u\leq b\),
\[
R_t(u)\leq\frac{e^{tb}-1-tb}{b^p}|u|^p.
\]
This region is empty when \(t\leq p/b\). Combining the two regions and taking expectations yields
\[
\mathbb E e^{tW}\leq1+t\mathbb EW+\frac{e^pt^2}{2}\mathbb EW^2
+\frac{e^{tb}-1-tb}{b^p}\mathbb E|W|^p\mathbf1_{\{t>p/b\}}.
\]
Applying \(\log a\leq a-1\) also gives the corresponding logarithmic inequality. Since the underlying bounds are pointwise, the same expectation inequality holds conditionally on a sigma-field; no regular conditional distribution assumption on the underlying measurable space is needed.

Apply this conditional inequality to \(W=U_i\) and \(W=-U_i\), with b=2y. Their conditional means are zero, and Step 3 verifies all moment and boundedness hypotheses. The factor \(2^p\) in the pth-moment bound cancels the corresponding factor in \((2y)^p\), giving
\[
\mathbb E[e^{\pm tU_i}\mid F_{i-1}]
\leq1+\frac{e^pt^2}{2}h_{i,2}
+\frac{e^{2ty}-1-2ty}{y^p}h_{i,p}\mathbf1_{\{t>p/(2y)\}}.
\]
The right-hand side is deterministic. Iterating conditional expectations, using the F_{i-1}-measurability of the preceding partial sum and \(1+a\leq e^a\), proves
\[
\mathbb E e^{\pm tV}
\leq\exp\left\{\frac{e^pt^2}{2}A_2+B(e^{2ty}-1-2ty)\mathbf1_{\{t>p/(2y)\}}\right\}.
\]
Set
\[
v=e^pA_2,\qquad k=\frac{p}{2y},\qquad
\Psi(t)=\frac{vt^2}{2}-\frac{zt}{2}+B(e^{2yt}-1-2yt)\mathbf1_{\{t>k\}},\qquad
I=\inf_{t>0}e^{\Psi(t)}.
\]
Markov's inequality applied to the positive random variables \(e^{tV}\) and \(e^{-tV}\) gives, for every t>0,
\[
\mathbb P(|V|>z/2)\leq2e^{\Psi(t)},
\]
and hence \(\mathbb P(|V|>z/2)\leq2I\).

### Step 5: All Chernoff regimes and the final constants

Define
\[
\alpha=\frac{2}{p+2},\qquad\gamma=\frac{p}{p+2}.
\]
Thus \(\alpha+\gamma=1\), \(\gamma=p\alpha/2\), and \(y=\gamma z/4\). Put
\[
h_1(t)=\frac{vt^2}{2}-\frac{\alpha zt}{2},\qquad
h_2(t)=B(e^{2yt}-1-2yt)-\frac{\gamma zt}{2},
\]
and
\[
t_1=\frac{\alpha z}{2v},\qquad
t_2=\frac{1}{2y}\log\left(1+\frac{\gamma z}{4yB}\right),\qquad
G=\exp\left(-\frac{\alpha^2z^2}{8v}\right).
\]
These are finite positive quantities. The function h_1 is minimized at t_1. Since
\[
h_2'(t)=2yB(e^{2yt}-1)-\frac{\gamma z}{2},
\]
h_2 decreases on [0,t_2], is minimized at t_2, and satisfies h_2(0)=0.

There are four exhaustive cases, including all equalities at the cutoffs.

1. If \(t_1\leq k\), the pth-moment term in \(\Psi(t_1)\) is absent, and
\[
\Psi(t_1)=h_1(t_1)-\frac{\gamma zt_1}{2}
\leq-\frac{\alpha^2z^2}{8v}.
\]
Thus I<=G.

2. If \(k<t_1\leq t_2\), then h_2(t_1)<=0, and
\[
\Psi(t_1)=h_1(t_1)+h_2(t_1)\leq-\frac{\alpha^2z^2}{8v}.
\]
Again I<=G.

3. If \(k<t_2<t_1\), use \(vt_2\leq vt_1=\alpha z/2\), discard the nonpositive term \(-2yt_2B\), and use \(B(e^{2yt_2}-1)=\gamma z/(4y)\). This gives
\[
\begin{aligned}
\Psi(t_2)
&\leq\frac{\gamma z}{4y}-\frac{\alpha zt_2}{4}-\frac{\gamma zt_2}{2}\\
&\leq\left(\gamma-\frac{p\alpha}{2}\right)\frac{z}{4y}-\frac{\gamma zt_2}{2}
=-\frac{\gamma zt_2}{2}.
\end{aligned}
\]
The second inequality uses \(t_2>k=p/(2y)\).

4. If \(t_2\leq k<t_1\), choose t=k. The strict cutoff in \(\Psi\) makes the pth-moment term vanish at this point. Since \(vk\leq vt_1=\alpha z/2\),
\[
\Psi(k)=\frac{vk^2}{2}-\frac{zk}{2}
\leq-\frac{\gamma zk}{2}-\frac{\alpha zk}{4}
\leq-\frac{\gamma zt_2}{2}.
\]

In the last two cases, \(\gamma z/(4y)=1\) implies
\[
I\leq e^{-\gamma zt_2/2}
=\left(1+\frac1B\right)^{-1}
=\frac{B}{1+B}\leq B.
\]
Therefore in every case \(I\leq G+B\). In particular, this is not a Gaussian-only bound on the truncated sum.

Combining Steps 3 and 4 now yields
\[
\begin{aligned}
\mathbb P(|S|>z)
&\leq\left(1+\frac{2y}{z}\right)B+2I\\
&\leq\left(3+\frac{\gamma}{2}\right)B+2G\\
&\leq4B+2G.
\end{aligned}
\]
Finally,
\[
B=\left(\frac{4(p+2)}p\right)^p\frac{A_p}{z^p},\qquad
G=\exp\left(-\frac{z^2}{2(p+2)^2e^pA_2}\right).
\]
Substitution is exactly the claimed bound. The argument covers p=2 as well as every real p>2; the zero case was handled in Step 2.

## Source Alignment and Proof Closure

The conditional moment estimates, truncation, and four-regime optimization follow the selected source chain. The proof explicitly corrects the negative-argument Taylor inference at L000364, puts the random bias event inside a probability before replacing it with a deterministic bound at L000424, uses h_2(0)=0 at L000462, and preserves the correct equality/inequality relations at L000475 and L000491-L000492. The source's pth-moment denominator in L000432-L000437 is y^p, not (2y)^p after substituting the centered-moment bound. Its large-tilt regimes contribute the polynomial term retained here. All five critical obligations are closed by the displayed derivations; no specialized external theorem or unresolved proof obligation is used.
