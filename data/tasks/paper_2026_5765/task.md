# Problem

## Setup

Let $m,n,d_0,q$ be positive integers, let $d\ge2$ be an integer, and let $\gamma>0$. Let $\mathcal X=\mathbb R^{d_0}$, equipped with a sigma-algebra $\mathcal A$. Write $S^{d-1}$ for the Euclidean unit sphere in $\mathbb R^d$, equipped with its Borel sigma-algebra, and let $\mathcal M$ be the set of measurable maps $f:(\mathcal X,\mathcal A)\to S^{d-1}$. For real numbers $s,t$, write $s\wedge t=\min\{s,t\}$.

For a tuple $z=(x,x^+,x_1^-,\ldots,x_m^-)\in\mathcal X^{m+2}$ and $f\in\mathcal M$, define

$$
\ell_\gamma(f;z)=\log\left(\frac1m+\frac1m\sum_{j=1}^m
\exp\left(\frac{\langle f(x),f(x_j^-)-f(x^+)\rangle}{\gamma}\right)\right).
$$

Fix $\theta_0\in\mathbb R^q$, $r>0$, and

$$
\Theta=\{\theta\in\mathbb R^q:\|\theta-\theta_0\|_2\le r\}.
$$

Suppose $\mathcal F=\{f_\theta:\theta\in\Theta\}\subseteq\mathcal M$ and, for some finite $L_0\ge0$,

$$
\|f_\theta(u)-f_{\theta'}(u)\|_2
\le L_0\|u\|_2\|\theta-\theta'\|_2
$$

for all $u\in\mathcal X$ and $\theta,\theta'\in\Theta$.

For realized tuples $z_i=(x_i,x_i^+,x_{i1}^-,\ldots,x_{im}^-)$, set

$$
B_\gamma=
\left(\frac1n\sum_{i=1}^n\|x_i\|_2^2\right)^{1/2}
+\left(\frac1n\sum_{i=1}^n\|x_i^+\|_2^2\right)^{1/2}
+\left(\frac1{nm}\sum_{i=1}^n\sum_{j=1}^m
\|x_{ij}^-\|_2^{\,2/(1\wedge\gamma)}\right)^{(1\wedge\gamma)/2}.
$$

Let $\sigma_1,\ldots,\sigma_n$ be independent Rademacher signs, each taking the values $-1$ and $1$ with probability $1/2$, and define the conditional empirical Rademacher complexity

$$
\mathfrak R_n=
\mathbb E_\sigma\left[
\sup_{f\in\mathcal F}\frac1n\sum_{i=1}^n\sigma_i\ell_\gamma(f;z_i)
\right].
$$

## Task

Prove the following integrated theorem.

1. For every $z=(x,x^+,x_1^-,\ldots,x_m^-)$, every $f,g\in\mathcal M$, and every $\beta\ge1$,

$$
\begin{aligned}
|\ell_\gamma(f;z)-\ell_\gamma(g;z)|
&\le \frac4\gamma\|f(x)-g(x)\|_2
+\frac1\gamma\|f(x^+)-g(x^+)\|_2\\
&\quad+\frac3\gamma e^{2/(\beta\gamma)}
\left(\frac1m\sum_{j=1}^m
\|f(x_j^-)-g(x_j^-)\|_2^\beta\right)^{1/\beta}.
\end{aligned}
$$

2. For every realized sample $z_1,\ldots,z_n$, if $a=erB_\gamma L_0$, then

$$
\mathfrak R_n\le
\frac{96}{\gamma}\sqrt{\frac qn}
\min\left\{
 a\sqrt{\log 3+1},
 \sqrt{\log(1+2a)+1}
\right\}.
$$
