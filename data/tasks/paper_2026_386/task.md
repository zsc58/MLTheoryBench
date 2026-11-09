# Problem

## Setup

Let $\mathcal T=(\mathcal V,\mathcal E)$ be a finite rooted tree of depth $D\ge 1$, with every leaf at depth $D$. Let $S_t$ be its set of depth-$t$ vertices. Give every edge $e$ a positive weight $\omega_e$, and let $d_{\mathcal T}(u,v)$ be the sum of the edge weights on the unique path between $u$ and $v$.

Fix parameters

$$
b>1,\qquad 0<\varepsilon<\frac{\log b}{4},\qquad
q=\left\lfloor\frac D2\right\rfloor,
$$

and suppose that every edge satisfies $\omega_e\ge\rho$ for some $\rho>0$. For every vertex $v\in\mathcal V$, define

$$
S_D(v)=\{x\in S_D:\ v\text{ lies on the path from the root to }x\}.
$$

Assume

$$
\exp((\log b-\varepsilon)t)\le |S_t|
\le \exp((\log b+\varepsilon)t)
\quad\text{for }t\in\{q,D\},
$$

and

$$
\max_{w\in S_q}|S_D(w)|
\le \exp\left(\frac{(\log b+\varepsilon)D}{2}\right).
$$

Let $p\ge1$ be an integer, let $A>0$, and let $F:\mathcal V\to\mathbb R^p$ satisfy

$$
F(S_D)\subseteq B_2(0,A).
$$

For a real-valued function $r$ on a metric space $(X,d)$, write

$$
\operatorname{Lip}_d(r)=
\sup_{x\ne y}\frac{|r(x)-r(y)|}{d(x,y)}.
$$

Write $\operatorname{Lip}_2$ when the domain is Euclidean.

## Task

Prove that there is a universal constant $c>0$ for which the following holds. There exist a vertex $a$ of depth at most $q$, two distinct children $a_+,a_-$ of $a$, leaves $x_+\in S_D(a_+)$ and $x_-\in S_D(a_-)$, and a function $f:\mathcal V\to[-1,1]$ such that

$$
f(x)=
\begin{cases}
1,&x\in S_D(a_+),\\
-1,&x\in S_D(a_-),\\
0,&x\in S_D\setminus(S_D(a_+)\cup S_D(a_-)),
\end{cases}
$$

$$
\operatorname{Lip}_{d_{\mathcal T}}(f)
\le \frac{2}{\rho D},
$$

and every function $\psi:\mathbb R^p\to[-1,1]$ satisfying

$$
|\psi(F(x_+))-f(x_+)|
+|\psi(F(x_-))-f(x_-)|\le1
$$

obeys

$$
\operatorname{Lip}_2(\psi)
\ge \frac{c}{A}
\exp\left(\frac{(\log b-4\varepsilon)D}{2p}\right).
$$
