# Problem

## Setup

Fix integers $N\ge 2$ and $1\le n<N$. There are $N$ finite-population units with outcomes $Y_1,\ldots,Y_N\in\mathbb R$ and observed proxy predictions $\hat Y_1,\ldots,\hat Y_N\in\mathbb R$. Let
\[
\theta_\star=\frac1N\sum_{i=1}^N Y_i.
\]
A label sample $L$ is drawn uniformly without replacement from all subsets of size $n$; proxy values are available for every unit. For any finite-population variable $Z$, write
\[
E_N[Z]=\frac1N\sum_i Z_i,\quad \operatorname{Var}_N(Z)=E_N[(Z-E_NZ)^2],\quad \operatorname{Cov}_N(Z,W)=E_N[(Z-E_NZ)(W-E_NW)].
\]
For variables $Z,W$ with positive finite-population variances, define $\rho_N(Z,W)=\operatorname{Cov}_N(Z,W)/\sqrt{\operatorname{Var}_N(Z)\operatorname{Var}_N(W)}$; set $\rho_N(Z,W)=0$ if either variance is zero. Set $S_Y^2=\operatorname{Var}_N(Y)>0$ and assume $\operatorname{Var}_N(\hat Y)>0$. For a fixed measurable recalibration $\phi$ on the finite support of $\hat Y$ and a fixed $\lambda\in\mathbb R$, define $s_i=\phi(\hat Y_i)$ and
\[
\hat\theta_\lambda(\phi)=\frac1n\sum_{i\in L}Y_i+\lambda\left(\frac1N\sum_{i=1}^N s_i-\frac1n\sum_{i\in L}s_i\right).
\]
Let $\lambda^*(\phi)$ minimize its sampling variance over $\lambda\in\mathbb R$, and let $V^*(\phi)=\operatorname{Var}(\hat\theta_{\lambda^*(\phi)}(\phi))$. Use the convention $\lambda^*(\phi)=0$ and $V^*(\phi)=D S_Y^2$ when $\operatorname{Var}_N(s)=0$, where
\[
D=\frac{N-n}{n(N-1)},
\]
and define correlations involving a zero-variance variable as zero. Let $m(z)=E_N[Y\mid \hat Y=z]$ on the finite proxy support, and define
\[
R^2_{Y\sim\hat Y}=\frac{\operatorname{Var}_N(m(\hat Y))}{S_Y^2}.
\]

## Task

Prove the integrated theorem below. The infimum over all measurable recalibrations satisfies
\[
\inf_\phi V^*(\phi)=D S_Y^2\left(1-R^2_{Y\sim\hat Y}\right),
\]
and it is attained by $\phi^*(z)=m(z)$ (under the stated convention). For the identity recalibration $\phi_{\mathrm{id}}(z)=z$,
\[
V^*(\phi_{\mathrm{id}})=D S_Y^2\left[1-\rho_N^2(Y,\hat Y)\right],
\]
and therefore
\[
V^*(\phi_{\mathrm{id}})-\inf_\phi V^*(\phi)
 =D S_Y^2\left[R^2_{Y\sim\hat Y}-\rho_N^2(Y,\hat Y)\right].
\]
Moreover, strict improvement is possible, i.e. $\inf_\phi V^*(\phi)<V^*(\phi_{\mathrm{id}})$, if and only if $m$ is not affine on the finite support of $\hat Y$ (there do not exist constants $a,b$ such that $m(\hat Y_i)=a+b\hat Y_i$ for every $i$).
