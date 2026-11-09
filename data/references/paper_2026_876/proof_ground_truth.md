# Reference Proof

## Proof Structure

Work on the positive support of the base distribution. Differentiate the sum of a differentiable convex function of the temperature-scaled coordinates. The derivative is a covariance of two similarly ordered quantities and is therefore nonnegative. An explicit convex approximation extends the argument to every convex test function in the definition. Then apply Schur-concavity and verify the Shannon entropy consequence, including boundary coordinates.

## Complete Proof

### 1. Domain, normalization, and support

Write the coordinates of $\pi$ as $p_i$ and set $S=\{i:p_i>0\}$. Since $\sum_i p_i=1$, the set $S$ is nonempty. For every $\beta>0$,
\[
Z(\beta)=\sum_{j\in S}p_j^\beta>0,
\qquad q_i(\beta)=\frac{p_i^\beta}{Z(\beta)}\quad(i\in S).
\]
Set $q_i(\beta)=0$ outside $S$. Thus $q(\beta)=\pi_\beta$ is a probability vector. Coordinates outside $S$ contribute the same constant $\phi(0)$ to each convex-function sum.

The original finite-logit setting is included: if $p_i=e^{z_i}/\sum_j e^{z_j}$, cancellation of the common factor $(\sum_j e^{z_j})^{-\beta}$ gives $q_i(\beta)=e^{\beta z_i}/\sum_j e^{\beta z_j}$. No finite logits are required for the full-simplex power definition.

### 2. Derivative and covariance identity

For $i\in S$, put $\ell_i=\log p_i$ and $\mu(\beta)=\sum_{j\in S}q_j(\beta)\ell_j$. Differentiating the finite sums gives
\[
q_i'(\beta)=q_i(\beta)\bigl(\ell_i-\mu(\beta)\bigr).
\]
Let $\phi:\mathbb R\to\mathbb R$ be differentiable and convex. Then
\[
\begin{aligned}
\frac{d}{d\beta}\sum_{i\in S}\phi(q_i(\beta))
&=\sum_{i\in S}q_i\phi'(q_i)\ell_i
-\left(\sum_{i\in S}q_i\phi'(q_i)\right)
 \left(\sum_{i\in S}q_i\ell_i\right)\\
&=\frac12\sum_{i,j\in S}q_iq_j
\bigl(\phi'(q_i)-\phi'(q_j)\bigr)(\ell_i-\ell_j).
\end{aligned}
\]
The second equality follows by expanding the double sum and using $\sum_{i\in S}q_i=1$.

For positive $\beta$, the order of $q_i=e^{\beta\ell_i}/Z(\beta)$ is the order of $\ell_i$. Also, convexity makes $\phi'$ nondecreasing. Consequently each summand in the last display is nonnegative. The derivative is therefore nonnegative for every $\beta>0$, and the mean value theorem yields
\[
\sum_i\phi(q_i(\beta_1))\leq\sum_i\phi(q_i(\beta_2))
\quad\text{whenever }0<\beta_1<\beta_2.
\]
The constant contributions from indices outside $S$ have been restored here.

### 3. Arbitrary convex test functions

Now let $\phi:\mathbb R\to\mathbb R$ be any finite convex function. Such a function is continuous: on each compact interval, the convex secant-slope inequalities bound slopes using values at enclosing points. In particular, $\phi$ is uniformly continuous on $[-1,2]$.

For $0<\varepsilon<1$, define
\[
\phi_\varepsilon(t)=\frac{1}{2\varepsilon}
\int_{-\varepsilon}^{\varepsilon}\phi(t+s)\,ds.
\]
Integrating the convexity inequality for each translate shows that $\phi_\varepsilon$ is convex. Continuity and the fundamental theorem of calculus give
\[
\phi_\varepsilon'(t)=
\frac{\phi(t+\varepsilon)-\phi(t-\varepsilon)}{2\varepsilon},
\]
so it is differentiable. Moreover,
\[
\sup_{t\in[0,1]}|\phi_\varepsilon(t)-\phi(t)|
\leq \sup_{\substack{t\in[0,1]\\ |s|\leq\varepsilon}}
|\phi(t+s)-\phi(t)|\longrightarrow0.
\]
Apply the inequality from the preceding section to $\phi_\varepsilon$ and pass to the limit in the finite sums. This proves
\[
\sum_i\phi(q_i(\beta_1))\leq\sum_i\phi(q_i(\beta_2))
\]
for every convex $\phi:\mathbb R\to\mathbb R$. By the public definition,
\[
\pi_{\beta_1}\prec\pi_{\beta_2}.
\]

### 4. Schur-concave functionals and Shannon entropy

For any symmetric Schur-concave $U$, its defining implication immediately gives
\[
U(\pi_{\beta_1})\geq U(\pi_{\beta_2}).
\]
To justify the Shannon specialization directly with the global-domain test functions used in the definition, for $\varepsilon>0$ define
\[
g_\varepsilon(t)=
\begin{cases}
(t+\varepsilon)\log(t+\varepsilon),&t\geq0,\\
\varepsilon\log\varepsilon+(1+\log\varepsilon)t,&t<0.
\end{cases}
\]
The two pieces agree in value and derivative at zero. The derivative is constant on the negative half-line and increasing on the positive half-line, so $g_\varepsilon$ is a finite convex function on $\mathbb R$.

For any $x,y\in\Delta_K$ with $x\prec y$, apply the definition to $g_\varepsilon$ and let $\varepsilon\downarrow0$. At each nonnegative coordinate, $g_\varepsilon(t)\to t\log t$, with limit zero at $t=0$. Hence
\[
\sum_i x_i\log x_i\leq\sum_i y_i\log y_i,
\qquad H(x)\geq H(y).
\]
Entropy is invariant under coordinate permutations, so it is symmetric Schur-concave. Applying this implication to the proved temperature ordering gives
\[
H(\pi_{\beta_1})\geq H(\pi_{\beta_2}).
\]

All arguments allow ties and zero coordinates. If $K=1$ or the positive support has one element, the derivative double sum vanishes and the conclusions hold with equality. Equal positive coordinates likewise cause no difficulty.

## Source and Proof Audit Notes

The source's displayed convex-function definition and temperature ordering are retained. Its explanatory entropy inequality at L000231 has the wrong sign; the correct direction above agrees with its decreasing-entropy conclusion at L000241. This local source repair is recorded under theory_005.

The original approximation sentence was too broad: a finite convex function defined only on a closed interval can have an endpoint discontinuity and need not admit uniform approximation by continuous functions. Section 3 uses exactly the public domain assumption $\phi:\mathbb R\to\mathbb R$ and supplies the required approximation explicitly.

The external majorization result indexed by theory_014 is attribution, not an invoked proof premise. Sections 1–4 independently close normalization, differentiation, the covariance identity and sign, arbitrary-convex-function coverage, majorization, and both requested consequences. There are no unresolved proof obligations.
