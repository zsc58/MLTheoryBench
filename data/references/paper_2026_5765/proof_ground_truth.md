# Reference Proof

## Proof Structure

First differentiate the log-exponential loss along the line segment between two representations. The resulting softmax-weighted perturbation is controlled by a tunable power mean over the negative samples. Next specialize the exponent and use the parameter Lipschitz condition to control the empirical loss pseudometric. Finally handle the zero-metric case and combine a uniform loss-diameter bound, Euclidean covering numbers, and Dudley's entropy integral.

## Complete Proof

### Continuity inequality

Write $\delta=f-g$ and $f_t=g+t\delta$ for $0\le t\le1$. Since $f$ and $g$ take values in the unit sphere, $\|f_t(u)\|_2\le1$ for every $u$. In this proof extend the defining finite-sum formula for $\ell_\gamma(h;z)$ to bounded measurable $\mathbb R^d$-valued maps $h$, so it is defined along this segment even though intermediate maps need not be sphere-valued.

For a fixed tuple $z=(x,x^+,x_1^-,\ldots,x_m^-)$, define

$$H(h)=\log\left(\frac1m\sum_{j=1}^m\exp\left(\frac{\langle h(x),h(x_j^-)-h(x^+)\rangle}{\gamma}\right)\right).$$

Then $\ell_\gamma(h;z)=Q(H(h))$, where $Q(u)=\log(m^{-1}+e^u)$ and $0<Q'(u)\le1$. Set

$$p_j(t)=\frac{\exp(\langle f_t(x),f_t(x_j^-)\rangle/\gamma)}{\sum_{s=1}^m\exp(\langle f_t(x),f_t(x_s^-)\rangle/\gamma)}.$$

Direct differentiation gives

$$\frac{d}{dt}H(f_t)=\frac1\gamma\left[\left\langle\delta(x),\sum_jp_j(t)f_t(x_j^-)-f_t(x^+)\right\rangle+\left\langle f_t(x),\sum_jp_j(t)\delta(x_j^-)-\delta(x^+)\right\rangle\right].$$

All differentiation is justified by finite sums of smooth functions with strictly positive arguments of the logarithms. Using $\|f_t(\cdot)\|_2\le1$, $\sum_jp_j(t)=1$, and $Q'\le1$ yields

$$\left|\frac{d}{dt}\ell_\gamma(f_t;z)\right|\le\frac1\gamma\left(2\|\delta(x)\|_2+\|\delta(x^+)\|_2+\sum_jp_j(t)\|\delta(x_j^-)\|_2\right).$$

Every inner product in the definition of $p_j(t)$ belongs to $[-1,1]$, so

$$p_j(t)\le\frac{e^{2/\gamma}}m.$$

For every $\beta\ge1$ and nonnegative $u_j$, Jensen's inequality gives

$$\sum_jp_j(t)u_j\le\left(\sum_jp_j(t)u_j^\beta\right)^{1/\beta}\le e^{2/(\beta\gamma)}\left(\frac1m\sum_ju_j^\beta\right)^{1/\beta}.$$

Apply this with $u_j=\|\delta(x_j^-)\|_2$ and integrate over $t\in[0,1]$. Enlarging the anchor coefficient from $2$ to $4$ and the negative coefficient from $1$ to $3$ proves

$$|\ell_\gamma(f;z)-\ell_\gamma(g;z)|\le\frac4\gamma\|\delta(x)\|_2+\frac1\gamma\|\delta(x^+)\|_2+\frac3\gamma e^{2/(\beta\gamma)}\left(\frac1m\sum_j\|\delta(x_j^-)\|_2^\beta\right)^{1/\beta}.$$

### Empirical metric estimate

Fix any realized sample. Define

$$\rho_n(f,g)=\left(\frac1n\sum_{i=1}^n|\ell_\gamma(f;z_i)-\ell_\gamma(g;z_i)|^2\right)^{1/2}.$$

Choose $\beta=\max\{1,2/\gamma\}$, so $e^{2/(\beta\gamma)}\le e$. Writing $\Delta_\theta=\|\theta-\theta'\|_2$, the parameter Lipschitz assumption and the continuity inequality imply

$$|\ell_\gamma(f_\theta;z_i)-\ell_\gamma(f_{\theta'};z_i)|\le\frac{L_0\Delta_\theta}{\gamma}\left[4\|x_i\|_2+\|x_i^+\|_2+3e\left(\frac1m\sum_j\|x_{ij}^-\|_2^\beta\right)^{1/\beta}\right].$$

Minkowski's inequality separates the three terms after taking the empirical root mean square. Put $p=2/(1\wedge\gamma)$. Then

$$\left[\frac1n\sum_i\left(\frac1m\sum_j\|x_{ij}^-\|_2^\beta\right)^{2/\beta}\right]^{1/2}\le\left(\frac1{nm}\sum_{i,j}\|x_{ij}^-\|_2^p\right)^{1/p}.$$

Indeed, if $\gamma<1$, then $p=\beta>2$, and concavity of $s\mapsto s^{2/\beta}$ gives the inequality by averaging over $i$. If $\gamma\ge1$, then $p=2\ge\beta$, and the power-mean inequality within each row gives

$$\left(\frac1m\sum_j\|x_{ij}^-\|_2^\beta\right)^{2/\beta}\le\frac1m\sum_j\|x_{ij}^-\|_2^2.$$

Averaging over $i$ proves the other case, including $\gamma=1$. Since $4\le4e$, $1\le4e$, and $3e\le4e$, we obtain

$$\rho_n(f_\theta,f_{\theta'})\le L\|\theta-\theta'\|_2,\qquad L=\frac{4e}{\gamma}B_\gamma L_0.$$

All empirical moments here are finite because the sample contains finitely many finite-dimensional vectors and $\gamma>0$.

### Loss diameter and the zero case

Each score in the loss lies in $[-2/\gamma,2/\gamma]$. Consequently,

$$\log(m^{-1}+e^{-2/\gamma})\le\ell_\gamma(f;z)\le\log(m^{-1}+e^{2/\gamma}).$$

The ratio of the arguments at the two endpoints is at most $e^{4/\gamma}$, so their difference is at most $4/\gamma$. Thus the $\rho_n$-diameter of the class is at most $4/\gamma$. The metric estimate and the radius-$r$ parameter ball also give diameter at most $2Lr$.

If $L=0$, all members of the class have exactly the same loss vector on the realized sample. Choosing any $f_*\in\mathcal F$ therefore gives

$$\mathfrak R_n=\mathbb E_\sigma\frac1n\sum_i\sigma_i\ell_\gamma(f_*;z_i)=0.$$

Here $a=erB_\gamma L_0=0$, so the asserted bound holds with equality. Henceforth suppose $L>0$, and thus $a>0$.

### Covering numbers and the entropy inequality

Let

$$T=\{(\ell_\gamma(f_\theta;z_1),\ldots,\ell_\gamma(f_\theta;z_n)):\theta\in\Theta\}\subset\mathbb R^n,$$

and equip it with $d_n(v,w)=(n^{-1}\sum_i(v_i-w_i)^2)^{1/2}$. The metric estimate makes the map from the compact parameter ball to $T$ Lipschitz, so $T$ is nonempty and compact. Its diameter $\Delta_T$ satisfies

$$\Delta_T\le\min\{2rL,4/\gamma\}.$$

Write $N(\varepsilon,T,d_n)$ for the minimum number of radius-$\varepsilon$ balls, centered in $T$, covering $T$. An $\varepsilon/L$-cover of the parameter ball induces an $\varepsilon$-cover of $T$. The standard volumetric estimate for a radius-$r$ Euclidean ball in $\mathbb R^q$ gives

$$N(\varepsilon,T,d_n)\le\left(1+\frac{2rL}{\varepsilon}\right)^q,\qquad\varepsilon>0.$$

We use the following standard independent form of Dudley's entropy inequality. For a nonempty compact $T\subset\mathbb R^n$, independent Rademacher signs, and the normalized Euclidean metric just defined,

$$\mathbb E_\sigma\sup_{v\in T}\frac1n\sum_i\sigma_i v_i\le\frac{12}{\sqrt n}\int_0^{\Delta_T}\sqrt{\log N(\varepsilon,T,d_n)}\,d\varepsilon.$$

The expected supremum is unchanged by subtracting any fixed vector $v_*\in T$. In particular, this inequality does not require $0\in T$. The increment normalization is verified directly: for $X_v=n^{-1}\sum_i\sigma_i v_i$,

$$\mathbb E_\sigma e^{\lambda(X_v-X_w)}=\prod_i\cosh\left(\frac{\lambda(v_i-w_i)}n\right)\le\exp\left(\frac{\lambda^2d_n(v,w)^2}{2n}\right).$$

Compactness supplies total boundedness and separability, and the sample paths are continuous linear functions of $v$. Thus the hypotheses of the entropy inequality hold. The covering estimate makes its improper integral finite. All suprema are also finite and measurable; the signs have a finite sample space.

If $\Delta_T=0$, the expected supremum is zero and the result follows. Otherwise monotonicity of covering numbers implies

$$\int_0^{\Delta_T}\sqrt{\log N(\varepsilon,T,d_n)}\,d\varepsilon\le2\int_0^{\Delta_T/2}\sqrt{\log N(\varepsilon,T,d_n)}\,d\varepsilon.$$

Since $\Delta_T/2\le\min\{rL,2/\gamma\}\le D$, where $D=\min\{rL,4/\gamma\}$, we may enlarge the endpoint and use the covering estimate to obtain

$$\mathfrak R_n\le24\sqrt{\frac qn}\int_0^D\sqrt{\log\left(1+\frac{2rL}{\varepsilon}\right)}\,d\varepsilon.$$

This explains why the endpoint $rL$ is valid despite the pairwise parameter-ball diameter being $2r$, not $r$.

### The two integral bounds

Set $a=erB_\gamma L_0$, so $rL=4a/\gamma$. Because the integrand is nonnegative and $D$ is no greater than either $rL$ or $4/\gamma$, integrating up to either endpoint gives a valid upper bound.

First substitute $\varepsilon=rLu$ and apply Cauchy-Schwarz:

$$\int_0^{rL}\sqrt{\log(1+2rL/\varepsilon)}\,d\varepsilon\le rL\sqrt{\int_0^1\log(1+2/u)\,du}\le rL\sqrt{\log3+1}.$$

The last inequality follows from $1+2/u\le3/u$ for $0<u\le1$ and $\int_0^1-\log u\,du=1$.

Second substitute $\varepsilon=(4/\gamma)u$:

$$\int_0^{4/\gamma}\sqrt{\log(1+2rL/\varepsilon)}\,d\varepsilon\le\frac4\gamma\sqrt{\int_0^1\log(1+2a/u)\,du}\le\frac4\gamma\sqrt{\log(1+2a)+1}.$$

For example, direct integration gives

$$\int_0^1\log(1+2a/u)\,du=\log(1+2a)+2a\log\left(1+\frac1{2a}\right)\le\log(1+2a)+1,$$

using $\log(1+t)\le t$. This calculation is used only for $a>0$; the zero case was already proved separately.

Multiplying each integral bound by $24\sqrt{q/n}$ and taking the smaller result proves

$$\mathfrak R_n\le\frac{96}{\gamma}\sqrt{\frac qn}\min\left\{a\sqrt{\log3+1},\sqrt{\log(1+2a)+1}\right\}.$$

Both asserted clauses follow. No population distribution, sampling assumption, or population moment condition was used.
