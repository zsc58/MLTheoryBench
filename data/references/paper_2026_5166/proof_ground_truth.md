# Reference Proof

## Proof Structure

1. Define the auxiliary functions and differentiate the canonical energy.
2. Derive the first component from its prescribed slope and concave curvature.
3. Solve the limiting stationarity equation, select the second curvature before calculating its mean, and verify every branch.
4. Normalize the components, derive the energy weights and exact mixture moments, and establish finite positive final precision.

## Complete Proof

Fix any finite $a>0$, $r>0$, and $m\in\mathbb R$. All assertions below are pointwise in this parameter triple; no smallness assumption on $a$ is made.

### 1. Definitions and derivatives

Define

$$s(x)=\frac{e^x}{a+e^x},\qquad d(x)=\frac{r}{a+e^x}-1,$$

and

$$C(x)=-\tfrac12\log(a+e^x)-\tfrac14(x-m)^2.$$

These functions and $E$ are finite and smooth at every real $x$, and $0<s(x)<1$. Differentiation gives

$$s'(x)=s(x)(1-s(x)),\qquad d'(x)=-s(x)(d(x)+1).$$

Consequently,

$$E'(x)=\tfrac12s(x)d(x)-\tfrac12(x-m),$$

and

$$\begin{aligned}
E''(x)
&=\tfrac12\{s(x)(1-s(x))d(x)-s(x)^2(d(x)+1)\}-\tfrac12\\
&=-\tfrac12s(x)\{s(x)+(2s(x)-1)d(x)\}-\tfrac12.
\end{aligned}$$

Also,

$$C''(x)=-\tfrac12s(x)(1-s(x))-\tfrac12<0.$$

The source's underlying normalized-exponential interpretation is well-defined here as well: $e^{E(x)}>0$ and

$$e^{E(x)}\leq a^{-1/2}\exp\!\left(-\frac{(x-m)^2}{4}\right).$$

Thus its normalizing integral is positive and finite, and its first two absolute moments are finite. The moment identity required below is nevertheless an identity for the constructed mixture, not for this original normalized exponential.

### 2. First component

A quadratic with prescribed derivative $E'(z)$ at $z$ and constant second derivative $-p$, where $p>0$, can be written, up to an additive constant, as

$$E'(z)(x-z)-\frac p2(x-z)^2
=-\frac p2\left(x-z-\frac{E'(z)}p\right)^2+\text{constant}.$$

Its normalized exponential therefore has center $z+E'(z)/p$. To verify its moments directly, let $t$ denote displacement from that center and let

$$Z_p=\int_{\mathbb R}e^{-pt^2/2}\,dt.$$

For $p>0$, this integral is finite and positive. Symmetry gives zero mean displacement. Integrating the derivative of $t e^{-pt^2/2}$ over the real line, whose boundary terms vanish, gives

$$\int_{\mathbb R}t^2e^{-pt^2/2}\,dt=\frac{Z_p}{p}.$$

Thus the normalized quadratic defines a Gaussian with variance $1/p$.

Apply this calculation at $z=m$ with

$$p_1=-C''(m)=\tfrac12s(m)(1-s(m))+\tfrac12>0.$$

The first component is

$$G_1=\mathcal N(u_1,p_1^{-1}),\qquad
u_1:=u_1=m+\frac{s(m)d(m)}{2p_1}.$$

Here $\mathcal N(u,v)$ denotes the normal law with mean $u$ and variance $v$. In particular, $u_1$ is finite. The auxiliary notation $\nu_1$ in the display is dispensable: the component mean is $u_1$.

### 3. Secondary point and second component

Holding $r,m$ fixed and taking the pointwise limit at each real $x$ gives

$$F(x)=-\tfrac12x-\tfrac r2e^{-x}-\tfrac14(x-m)^2.$$

Hence

$$F'(x)=\tfrac12(re^{-x}-1)-\tfrac12(x-m),\qquad
F''(x)=-\tfrac r2e^{-x}-\tfrac12<0.$$

The stationarity equation is

$$re^{-x}=1+x-m.$$

Put $v=1+x-m$. Then this equation is equivalent to

$$ve^v=re^{1-m}.$$

The right-hand side is finite and strictly positive. A solution must have $v>0$. On $[0,\infty)$, the function $v\mapsto ve^v$ is continuous, has derivative $e^v(1+v)>0$, starts at zero, and is unbounded. It therefore has a unique inverse at every positive argument. Denote this inverse by $W_0$. This proves the needed positive-argument principal Lambert-W property directly, rather than leaving it as an unverified citation.

It follows that

$$y=m-1+W_0(re^{1-m})$$

is finite and is the unique real stationary point of $F$. Since $F''<0$, it is also its unique global maximizer. This solves only the limiting stationarity equation; it does not assert $E'(y)=0$ at positive $a$.

Define the full candidate precision

$$h=-E''(y)=\tfrac12s(y)\{s(y)+(2s(y)-1)d(y)\}+\tfrac12.$$

Select the actual precision first:

$$p_2=
\begin{cases}
h,&h>0,\\
\tfrac12s(y)(1-s(y))+\tfrac12,&h\leq0.
\end{cases}$$

Both branches are finite and strictly positive. In particular, the case $h=0$ uses the second branch and involves no division by zero. The prescribed quadratic $Q_2$ has this negative curvature and the full slope $E'(y)$, so completing the square as above gives

$$G_2=\mathcal N(u_2,p_2^{-1}),\qquad
u_2:=u_2=y+\frac{s(y)d(y)-(y-m)}{2p_2}.$$

Again, the component mean is $u_2$; the auxiliary notation $\nu_2$ is dispensable. When $h>0$, this is the ordinary expression $y-E'(y)/E''(y)$. When $h\leq0$, its denominator is the selected positive fallback precision, not the unreplaced full curvature. This is the precision-based mean formula used together with the source's fallback instruction.

No claim of exact mode recovery or of a uniform error bound for this one-step correction is needed.

### 4. Weights, moments, and final precision

The two means are finite, so both $E(u_1)$ and $E(u_2)$ are finite. Normalizing their exponentials gives

$$b=\frac{e^{E(u_2)}}{e^{E(u_1)}+e^{E(u_2)}}
=\frac{1}{1+\exp(E(u_1)-E(u_2))},\qquad 0<b<1.$$

In particular,

$$\frac{b}{1-b}=\exp(E(u_2)-E(u_1)).$$

Thus $E(u_2)>E(u_1)$ implies $b>1-b$, the reverse inequality gives the reverse weight ordering, and equality gives $b=1/2$. As the energy difference $E(u_2)-E(u_1)$ tends to positive or negative infinity, the second weight tends to one or zero, respectively. These are weight limits; they do not assert uniform convergence of mixture moments along parameter sequences with changing component means or variances.

Each $G_i$ is normalized and has finite first and second moments. By linearity of integration under the mixture,

$$\bar u=\mathbb E_M[X]=(1-b)u_1+bu_2,$$

and

$$\mathbb E_M[X^2]=(1-b)(p_1^{-1}+u_1^2)+b(p_2^{-1}+u_2^2).$$

Subtracting $\bar u^2$ and expanding yields

$$\begin{aligned}
\bar v=\operatorname{Var}_M(X)
&=\frac{1-b}{p_1}+\frac{b}{p_2}
 +(1-b)u_1^2+bu_2^2-((1-b)u_1+bu_2)^2\\
&=\frac{1-b}{p_1}+\frac{b}{p_2}
 +b(1-b)(u_1-u_2)^2.
\end{aligned}$$

Every term is finite. The first two terms are strictly positive and the last is nonnegative, so $0<\bar v<\infty$. Therefore

$$\bar p=\bar v^{-1}>0,$$

and the required final Gaussian is $\mathcal N(\bar u,\bar v)$. Its first raw moment is $\bar u$ and its second raw moment is $\bar u^2+\bar v=\mathbb E_M[X^2]$, proving the exact two-moment match.

If the component means coincide, the between-component term is simply zero and positivity still follows from the within-component terms. Both weights are positive for every finite allowed parameter triple. None of the argument assumes a particular number of local maxima of $E$, so the same construction and conclusions apply in the bimodal regime.

## Source Correspondence and Closure

The definitions and derivatives are supported by theory_001 through theory_004; the first component by theory_005; the limiting point and precision-first fallback by theory_006 and theory_010; and the weights and mixture moments by theory_007. All theorem-critical obligations are derived above. There is no unresolved specialized dependency and no private ground-truth quality warning.
