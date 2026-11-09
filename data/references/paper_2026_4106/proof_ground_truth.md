# Reference Proof

## Proof Structure

1. Verify the reweighted probability law, normalized push-forward, and measurability of the displayed losses.
2. Derive decision-risk equivalence using positive-scale invariance and loss homogeneity.
3. Derive the squared-loss change-of-variables identity, including infinite-risk predictors.
4. Characterize every weighted-spherical Bayes minimizer by conditional quadratic completion.
5. Prove conditional and global decision optimality, including zero conditional means.

## Complete Proof

### 1. Well-defined laws and risks

Write $r(y)=\|y\|$. Since $r(Y)>0$ almost surely and is integrable, $C=\mathbb E_P r(Y)$ belongs to $(0,\infty)$. The nonnegative density $r/C$ integrates to one, so it defines a probability law $\widetilde Q$. The map $T(x,y)=(x,y/r(y))$ is Borel measurable on the stated domain, and its push-forward $Q$ is a probability law with $\|Z\|=1$ almost surely.

The measurable oracle and predictors make both losses measurable. Oracle optimality and boundedness of $S$ imply
\[
0\leq \ell_{\rm dec}(u,y)\leq 2B_S\|y\|.
\]
Thus decision risks under $P$ and $Q$ are finite for every predictor. The weighted-spherical and squared losses are nonnegative and therefore always have well-defined extended expectations.

For any nonnegative Borel function $h$, the definitions give
\[
\int h(x,z)\,dQ(x,z)
=\frac1C\int r(y)h\!\left(x,\frac{y}{r(y)}\right)\,dP(x,y).
\]
Indeed, this equality follows first for indicator functions from the push-forward and density definitions, then for nonnegative simple functions by linearity, and then for general nonnegative functions by increasing simple approximation. Hence it applies without an integrability assumption on $h$.

### 2. Decision-risk identity

For $c\in\mathbb R^d$, let $W(c)=\arg\min_{w\in S}c^\top w$. Compactness and continuity make this a nonempty compact set. For $\alpha>0$, the inequalities defining $W(c)$ are equivalent to those defining $W(\alpha c)$, so these two sets agree. Since the tie-breaking rule depends only on this set,
\[
w^*(\alpha c)=w^*(c),\qquad c\in\mathbb R^d,\quad\alpha>0.
\]
This statement includes $c=0$. Consequently,
\[
\ell_{\rm dec}(u,\alpha y)
=\alpha y^\top w^*(u)-\alpha y^\top w^*(\alpha y)
=\alpha\ell_{\rm dec}(u,y).
\]
Applying the integration identity from Step 1 gives
\[
\begin{aligned}
\mathbb E_Q[\ell_{\rm dec}(f(X),Z)]
&=\frac1C\mathbb E_P\!\left[r(Y)\ell_{\rm dec}\!\left(f(X),\frac{Y}{r(Y)}\right)\right]\\
&=\frac1C\mathbb E_P[\ell_{\rm dec}(f(X),Y)]
=\frac1C R_P^{\rm dec}(f).
\end{aligned}
\]
Because $C>0$, the decision-risk minimizers under $P$ and $Q$ coincide.

### 3. Squared-loss identity

Apply the same integration identity to $h(x,z)=\|f(x)-z\|^2$. It yields
\[
\mathbb E_Q\|f(X)-Z\|^2
=\frac1C\mathbb E_P\!\left[r(Y)\left\|f(X)-\frac{Y}{r(Y)}\right\|^2\right]
=\frac1C R_P^{\rm ws}(f).
\]
This equality holds in $[0,\infty]$, including when both sides are infinite. Minimizing the weighted-spherical risk under $P$ is therefore equivalent to minimizing squared prediction risk under $Q$.

### 4. Every surrogate Bayes minimizer

Choose measurable versions
\[
m(x)=\mathbb E_P[Y\mid X=x],\qquad a(x)=\mathbb E_P[r(Y)\mid X=x].
\]
These exist because the variables are integrable and take values in finite-dimensional Euclidean spaces. We have $a(X)\leq B_y$ almost surely. To verify strict positivity, let $A=\{a(X)=0\}$. Then
\[
\mathbb E_P[r(Y)\mathbf 1_A]=\mathbb E_P[a(X)\mathbf 1_A]=0.
\]
Since $r(Y)>0$ almost surely, $P(A)=0$. Conditional Jensen's inequality gives $\|m(X)\|\leq a(X)$ almost surely.

Define $f_0(x)=m(x)/a(x)$ on the full-measure set where $a(x)>0$ and $\|m(x)\|\leq a(x)$, and define $f_0(x)=0$ elsewhere. This is measurable and satisfies $\|f_0(X)\|\leq1$ almost surely. In particular, $R_P^{\rm ws}(f_0)\leq4C<\infty$.

Consider any predictor $f$ with finite weighted-spherical risk. The bound
\[
r(Y)\|f(X)\|^2
\leq 2r(Y)\left\|f(X)-\frac{Y}{r(Y)}\right\|^2+2r(Y)
\]
shows that $r(Y)\|f(X)\|^2$ is integrable. Also
\[
\mathbb E_P|Y^\top f(X)|
\leq\mathbb E_P[r(Y)\|f(X)\|]
\leq \sqrt{C\,\mathbb E_P[r(Y)\|f(X)\|^2]}<\infty.
\]
Thus the following conditional expansion and integration are legitimate:
\[
\begin{aligned}
\mathbb E_P[\ell_{\rm ws}(f(X),Y)\mid X]
&=a(X)\|f(X)\|^2-2f(X)^\top m(X)+a(X)\\
&=a(X)\|f(X)-f_0(X)\|^2+a(X)-\frac{\|m(X)\|^2}{a(X)}
\quad\text{almost surely}.
\end{aligned}
\]
The final two terms together lie between zero and $a(X)$. Applying this formula to $f_0$ and subtracting the integrated expressions yields
\[
R_P^{\rm ws}(f)-R_P^{\rm ws}(f_0)
=\mathbb E_P[a(X)\|f(X)-f_0(X)\|^2]\geq0.
\]
Predictors with infinite risk cannot improve on $f_0$. Hence $f_0$ is a global Bayes minimizer. Conversely, every global Bayes minimizer has finite risk and equality in this display. Positivity of $a(X)$ implies that it equals $f_0(X)$ almost surely. This proves the required characterization for every minimizer, not merely existence of one.

### 5. Decision optimality

Let $f^*$ be any surrogate Bayes minimizer. By Step 4,
\[
f^*(X)=\frac{m(X)}{a(X)}\quad\text{almost surely}.
\]
The multiplier $1/a(X)$ is strictly positive. Step 2 therefore gives
\[
w^*(f^*(X))=w^*(m(X))\quad\text{almost surely}.
\]
This reasoning already includes $m(X)=0$: both oracle arguments are then zero. Equivalently, on this event every feasible decision minimizes the identically zero conditional cost.

For an arbitrary measurable predictor $g$, boundedness of the decisions and integrability of $Y$ justify
\[
\mathbb E_P[\ell_{\rm dec}(g(X),Y)\mid X]
=m(X)^\top w^*(g(X))
-\mathbb E_P[Y^\top w^*(Y)\mid X].
\]
The second term is independent of $g$, whereas oracle optimality gives
\[
m(X)^\top w^*(g(X))\geq m(X)^\top w^*(m(X)).
\]
Thus $f^*$ minimizes conditional decision risk almost surely. Integration proves that it minimizes global decision risk over all measurable predictors.

For completeness, the stated equivalence between global and conditional optimality follows from the same comparison. The measurable predictor $x\mapsto m(x)$ attains the conditional minimum. For any predictor, its decision risk minus that attained minimum is the expectation of the nonnegative, integrable conditional cost gap. The expectation is zero if and only if that gap is zero almost surely. This proves the equivalence and completes every obligation of the theorem.
