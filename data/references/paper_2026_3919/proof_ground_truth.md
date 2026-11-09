# Reference Proof

## Proof Structure

Reduce excess risk to disagreement with the Bayes rule. Establish the required pointwise k-nearest-neighbour posterior tail directly from the lower-mass and Holder assumptions. Split disagreement into a small-margin event and a posterior-estimation event, then choose the threshold that balances the two exponents.

## Complete Proof

Write
\[
s=d/v,\qquad q=2+s,\qquad
 a=\min\{C_d(2\lambda)^{-d/v},1\}.
\]
Thus \(0<a\leq1\). All test observations below are independent of the training sample.

### step_001: Excess risk and threshold disagreement

Conditioning on the test input, for every measurable classifier \(h\),
\[
R(h)-R(h_*)
=\mathbb E_X\left[|2\eta(X)-1|\mathbf1\{h(X)\ne h_*(X)\}\right]
\leq\Pr_X\{h(X)\ne h_*(X)\}. \tag{1}
\]
The same identity applies for each fixed training sample.

Let \(M(x)=|\eta(x)-1/2|\). For a classifier obtained by thresholding an estimate at \(1/2\), disagreement implies
\[
|\widehat\eta(x)-\eta(x)|\geq M(x).
\]
Indeed, if \(\eta(x)\geq1/2\), disagreement requires \(\widehat\eta(x)<1/2\); if \(\eta(x)<1/2\), disagreement requires \(\widehat\eta(x)\geq1/2\). The comparison need not be strict in the second case. Nevertheless, for every \(t>0\),
\[
\{\widehat h(X)\ne h_*(X)\}
\subseteq
\{M(X)\leq t\}\cup
\{|\widehat\eta(X)-\eta(X)|>t\}. \tag{2}
\]
This is the only threshold implication needed below.

### step_002: A complete pointwise posterior-tail derivation

Fix \(0<t\leq1\), \(n\geq2\), and a query \(x\). Put
\[
r=(t/(2\lambda))^{1/v},\qquad
m=an t^s,\qquad k=\lfloor m/2\rfloor.
\]
Suppose \(m\geq4\). Then
\[
1\leq k\leq n,\qquad m/4\leq k\leq m/2.
\]
This choice depends only on \(n,t\) and the displayed parameters, not on \(x\) or the sample.

The mass \(p_x=P_X(B(x,r))\) satisfies
\[
p_x\geq\min\{C_d(2\lambda)^{-d/v}t^s,1\}\geq at^s.
\]
The number \(B_x\) of training inputs in this ball is binomial with parameters \(n,p_x\). Since \(k\leq m/2\leq np_x/2\), an exponential-moment calculation gives
\[
\begin{aligned}
\Pr_S\{B_x<k\}
&\leq\Pr_S\{B_x<np_x/2\}\\
&\leq\exp\bigl((\log2)np_x/2\bigr)\mathbb E[2^{-B_x}]\\
&=\exp\bigl((\log2)np_x/2\bigr)(1-p_x/2)^n\\
&\leq\exp\bigl(-np_x(1-\log2)/2\bigr)\\
&\leq\exp(-np_x/8)
\leq\exp(-m/8). \tag{3}
\end{aligned}
\]
Here \(1-u\leq e^{-u}\) and \(\log2\leq3/4\) justify the last estimates.

Condition on all training inputs. The selected indices are then fixed because nearest-neighbour selection uses inputs and sample indices only. The selected labels are conditionally independent Bernoulli variables, with conditional means \(\eta(X_i)\). Let \(\mu_x\) be the average of these \(k\) conditional means.

For completeness, if \(Z\) is a Bernoulli variable, then
\[
\mathbb E\exp(u(Z-\mathbb EZ))\leq\exp(u^2/8),\qquad u\in\mathbb R.
\]
To verify this, let \(\phi(u)=\log\mathbb E\exp(u(Z-\mathbb EZ))\). We have \(\phi(0)=\phi'(0)=0\), and \(\phi''(u)\) is the variance of a Bernoulli variable under exponential tilting, hence is at most \(1/4\). Integrating this second-derivative bound gives \(\phi(u)\leq u^2/8\), including the deterministic Bernoulli cases.

Multiplying these conditional moment bounds and applying the exponential Markov inequality, with \(u=4\epsilon\), proves each one-sided bound \(\exp(-2k\epsilon^2)\) for deviation of the selected-label average by more than \(\epsilon\). Therefore
\[
\Pr_S\left\{|\widehat\eta_{n,k}(x)-\mu_x|>t/2\mid X_1,\ldots,X_n\right\}
\leq2\exp(-kt^2/2). \tag{4}
\]

On \(\{B_x\geq k\}\), all selected inputs have distance at most \(r\) from \(x\). Holder smoothness consequently gives
\[
|\mu_x-\eta(x)|\leq\lambda r^v=t/2.
\]
Combining (3) and (4), and using \(k\geq m/4\) and \(t\leq1\), yields
\[
\begin{aligned}
\Pr_S\{|\widehat\eta_{n,k}(x)-\eta(x)|>t\}
&\leq e^{-m/8}+2e^{-kt^2/2}\\
&\leq3\exp(-an t^q/8)\\
&\leq2n\exp(-c_0nt^q),\qquad c_0=a/8. \tag{5}
\end{aligned}
\]
The last inequality uses \(n\geq2\). The bound is independent of the fixed query \(x\), so it also bounds the supremum of these pointwise probabilities and, by integration, the joint independent-query probability.

Choose
\[
A_0\geq\frac{4}{a\log2}.
\]
For \(n\geq2\), the requirement \(nt^q\geq A_0\log n\) implies
\[
m=an t^s\geq an t^q\geq4.
\]
It therefore guarantees every admissibility condition used in (5). This proves the required posterior tail without invoking the source's specialized uniform regression theorem. The finite-VC assumption remains part of the source contract but is not needed for this pointwise derivation.

### step_003: Margin splitting and exponent balancing

Average (1) over \(S\), apply (2), integrate (5) over the independent test input, and use (EB). Whenever the preceding admissibility conditions hold,
\[
\mathbb E_S[R(\widehat h_{n,k})-R(h_*)]
\leq\alpha\exp(-\gamma t^{-\beta})
+2n\exp(-c_0nt^q). \tag{6}
\]
Set
\[
t=n^{-1/(\beta+q)}.
\]
Then \(0<t\leq1\), and
\[
t^{-\beta}=nt^q=n^{\beta/(\beta+q)}.
\]
Thus this choice balances the two powers in the exponents.

### step_004: Integer k, sample-size conditions, and the final bound

Define, for every positive integer \(n\),
\[
k_n=\max\left\{1,\left\lfloor\frac a2 n^{(\beta+2)/(\beta+q)}\right\rfloor\right\}.
\]
Because \((\beta+2)/(\beta+q)<1\) and \(a\leq1\), this is an integer in \(\{1,\ldots,n\}\), and
\[
k_n=O\left(n^{(\beta+2)/(\beta+q)}\right).
\]
For the eligible sample sizes below, the maximum with 1 is unnecessary, so this is precisely the choice used in step_002.

Take
\[
A\geq\max\{A_0,2/c_0\},\qquad N=2.
\]
If \(n\geq N\) and
\[
n\geq(A\log n)^{1+q/\beta},
\]
then, writing \(z=n^{\beta/(\beta+q)}\), we obtain
\[
z\geq A\log n\geq A_0\log n,
\qquad \log n\leq(c_0/2)z.
\]
The first inequality establishes posterior-tail admissibility. The second absorbs the prefactor:
\[
2n e^{-c_0z}\leq2e^{-(c_0/2)z}.
\]
Apply (6) with the balanced threshold and take
\[
c=\min\{\gamma,c_0/2\}>0.
\]
It follows that
\[
\mathbb E_S[R(\widehat h_{n,k_n})-R(h_*)]
\leq(2+\alpha)\exp\left(-c n^{\beta/(\beta+q)}\right).
\]
Every constant and the entire deterministic sequence \((k_n)\) depend only on the displayed parameters. All theorem-critical obligations are closed; the specialized uniform regression citation is not used as a proved result.
