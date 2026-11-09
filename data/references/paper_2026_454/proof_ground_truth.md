# Reference Proof

## Proof Structure

First verify that the base joint and its data marginal are probability densities and that exceptional density-version values do not affect the weight. Expand the second moment on the positive conditional-density set. For interior temperatures, apply Holder's inequality with beta-dependent conjugate exponents for prior-almost every parameter. Handle both endpoints directly and conclude finite variance.

## Complete Proof

Write \(\Pi(d\theta)=\pi(\theta)\,d\theta\). All integrands used for normalization are nonnegative and measurable. Tonelli's theorem, which permits exchanging integrals of nonnegative measurable functions on these sigma-finite reference spaces, gives
\[
\int_{\mathcal X}p_X(x)\,dx
=\int_\Theta\pi(\theta)\left(\int_{\mathcal X}r(x\mid\theta)\,dx\right)d\theta
=1.
\]
The same calculation shows that \(P_0\) has total mass one and has data marginal \(p_X\).

For \(\Pi\)-almost every \(\theta\), the conditional density \(r(\cdot\mid\theta)\) is finite almost everywhere in \(x\). The conditional probability of the sets where it is zero or infinite is zero. Integrating over \(\Pi\) shows that
\[
0<r(x\mid\theta)<\infty\qquad P_0\text{-almost surely}.
\]
Also, \(p_X\) is finite almost everywhere with respect to the data reference measure because it integrates to one. Its infinite-value set consequently has probability zero under its own density and hence under the data marginal of \(P_0\). Thus the displayed weight ratio is finite and defined \(P_0\)-almost surely. Assigning zero on exceptional sets where it is undefined does not affect any moment. Throughout, statements involving density versions and integrals are interpreted up to the appropriate null sets.

For \(\beta\in(1/2,1)\), put
\[
a=2\beta-1,\qquad b=2-2\beta.
\]
Then \(a,b\in(0,1)\) and \(a+b=1\). Expanding the squared weight on \(\{r(x\mid\theta)>0\}\) gives
\[
\mathbb E_{P_0}[w_\beta^2]
=\int_\Theta\pi(\theta)\int_{\mathcal X}
 r(x\mid\theta)^a p_X(x)^b\,dx\,d\theta.
\]
The integrand vanishes where \(r=0\), since \(a>0\); density-version exceptions do not change the integrals. Nonnegativity justifies the iterated integration without assuming the desired second moment is already finite.

Holder's inequality states that for \(u,v>1\) with \(1/u+1/v=1\),
\[
\int |fg|\leq
\left(\int |f|^u\right)^{1/u}
\left(\int |g|^v\right)^{1/v}.
\]
Choose \(u=1/a\) and \(v=1/b\). These exponents satisfy its hypotheses. For \(\Pi\)-almost every \(\theta\), apply the inequality to \(f(x)=r(x\mid\theta)^a\) and \(g(x)=p_X(x)^b\). Their required powers integrate to one, so
\[
\int_{\mathcal X}r(x\mid\theta)^a p_X(x)^b\,dx
\leq
\left(\int_{\mathcal X}r(x\mid\theta)\,dx\right)^a
\left(\int_{\mathcal X}p_X(x)\,dx\right)^b
=1.
\]
Integration against the probability measure \(\Pi\) yields \(\mathbb E_{P_0}[w_\beta^2]\leq1\).

At \(\beta=1\), the weight is one \(P_0\)-almost surely, so \(\mathbb E_{P_0}[w_1^2]=1\).

At \(\beta=1/2\), cancellation must retain the positive conditional-density set. Therefore
\[
\mathbb E_{P_0}[w_{1/2}^2]
=\int_\Theta\pi(\theta)\int_{\mathcal X}
\mathbf 1_{\{r(x\mid\theta)>0\}}p_X(x)\,dx\,d\theta
\leq\int_\Theta\pi(\theta)\,d\theta=1.
\]
The equality is understood up to the density-version null sets already addressed. It does not assert that every conditional support has full marginal probability.

We have proved the bound for every \(\beta\in[1/2,1]\). Since \(w_\beta\geq0\) and \(2w_\beta\leq1+w_\beta^2\), its first moment is finite. Consequently
\[
\operatorname{Var}_{P_0}(w_\beta)
=\mathbb E_{P_0}[w_\beta^2]
 -\bigl(\mathbb E_{P_0}[w_\beta]\bigr)^2
\leq1<\infty.
\]
This conclusion concerns the importance weights only, not an unspecified SNIS estimator with an arbitrary test function or loss.
