# Problem

## Setup

Let $d\ge1$ be an integer, let $\mathsf Z\subseteq\mathbb R^d$ be equipped with its Borel sigma-algebra $\mathcal A$, and let $P$ be a probability law on $(\mathsf Z,\mathcal A)$. Let $m\ge1$ be an integer. A possibly random measurable score $s:\mathsf Z\to\mathbb R$ is fitted using only a fitting sample of i.i.d. observations from $P$, independent of a held-out sample $Y_1,\ldots,Y_m\stackrel{\mathrm{i.i.d.}}{\sim}P$. Assume that score evaluation is jointly measurable in the fitting data and its argument $z$. Define

$$
U_j=s(Y_j),\qquad
G_m(t)=\frac1m\sum_{j=1}^m\mathbf 1\{U_j\le t\}.
$$

Fix $\delta\in(0,1)$ and $\gamma\in[0,1)$, and set

$$
r_m=\sqrt{\frac{\log(2/\delta)}{2m}},
\qquad L_m(t)=\max\{G_m(t)-r_m,0\}.
$$

Assume $\gamma\ge r_m$, and define

$$
\tau=\inf\{t\in\mathbb R:L_m(t)\ge1-\gamma\},
\qquad B=\{z\in\mathsf Z:s(z)\le\tau\}.
$$

Assume that the selected set $B$ is bounded.

For a probability law $Q$ and a measurable set $B$ with $Q(B)>0$, write

$$
Q_B(A)=\frac{Q(A\cap B)}{Q(B)},\qquad A\in\mathcal A.
$$

For probability laws $Q$ and $G$ on $(\mathsf Z,\mathcal A)$, define the directional distortion

$$
d_-(Q,G)=\sup_{A\in\mathcal A:G(A)>0}\frac{G(A)-Q(A)}{G(A)}.
$$

Let

$$
E=\{P(B)\ge1-\gamma\}.
$$

Let $C$ be a probability law on $(\mathsf Z,\mathcal A)$, possibly depending on the fitting and held-out data. When data-dependent, $C$ is a probability kernel: for each $A\in\mathcal A$, $C(A)$ is a measurable function of those data. Assume that, on $E$, $C(B)>0$ and

$$
e_c=d_-(P_B,C_B)<1.
$$

Let the deployment law be

$$
D=(1-\alpha)P+\alpha R,
$$

where $R$ is a probability law on $(\mathsf Z,\mathcal A)$ and $\alpha\in[0,1)$. On $E$, define

$$
\rho=\frac{R(B)}{D(B)},
\qquad
e_{\mathrm{eff}}=e_c+\alpha\rho-\alpha e_c\rho.
$$

Finally, let $\{\ell_a:\mathsf Z\to[0,\infty):a\in\mathcal I\}$ be any family of nonnegative real-valued measurable losses. Assume that for some $p\in(1,\infty)$, with $q=p/(p-1)$,

$$
M_p(a)=\left(\mathbb E_D[\ell_a^p]\right)^{1/p}<\infty
\quad\text{for every }a\in\mathcal I.
$$

Nonnegative extended-real expressions use the convention $0\cdot(+\infty)=0$: a term with coefficient zero is omitted. In particular, the supremum in the conclusion is allowed to be $+\infty$.

## Task

Prove that $\Pr(E)\ge1-\delta$ and that, on $E$, simultaneously for every $a\in\mathcal I$,

$$
\mathbb E_D\ell_a
\le
(1-e_{\mathrm{eff}})\mathbb E_{C_B}\ell_a
+e_{\mathrm{eff}}\sup_{z\in B}\ell_a(z)
+M_p(a)\left[(1-\alpha)\gamma+\alpha\bigl(1-R(B)\bigr)\right]^{1/q}.
$$

Thus the bulk-mass guarantee and the displayed risk certificate hold together with probability at least $1-\delta$ over the data used to construct $B$.
