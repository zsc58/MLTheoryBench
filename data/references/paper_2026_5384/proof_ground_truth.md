# Reference Proof

## Proof Structure

First derive an exact variance identity for one importance-weighted summand. Its second moment is controlled by a purely combinatorial factor. Reorganize that factor by the two cardinalities $r=|S\cap T|$ and $q=|T\setminus S|$, simplify a ratio of binomial coefficients using rising factorials, and analyze the boundary and interior values of $r$. Finally, use a nonzero constant value function to attain the resulting upper rates.

## Complete Proof

Put $d=n-s$ and let

$$
Y(T)=v(T)(-1)^{s-|S\cap T|}\frac{w_{|T\setminus S|}}{Q(T)},
$$

so that $\widehat I_S=m^{-1}\sum_{i=1}^m Y(T_i)$. Every $T\subseteq N$ is uniquely $U\cup L$ with $U\subseteq N\setminus S$ and $L\subseteq S$. Therefore

$$
\mathbb E Y
 =\sum_{U\subseteq N\setminus S}w_{|U|}
   \sum_{L\subseteq S}(-1)^{s-|L|}v(U\cup L)
 =I_S(v).
$$

Squaring removes the sign, while one factor of $Q(T)$ cancels when taking expectation. Independence consequently gives the exact identity

$$
\operatorname{Var}(\widehat I_S)
 =\frac1m\left(
 \sum_{T\subseteq N}v(T)^2\frac{w_{|T\setminus S|}^2}{Q(T)}
 -I_S(v)^2\right).
$$

Hence, with

$$
\Gamma_S:=\sum_{T\subseteq N}\frac{w_{|T\setminus S|}^2}{Q(T)},
$$

we have

$$
\operatorname{Var}(\widehat I_S)
 \leq \frac{\|v\|_\infty^2}{m}\Gamma_S. \tag{1}
$$

It remains to determine $\Gamma_S$. Group coalitions according to
$r=|S\cap T|$ and $q=|T\setminus S|$. There are
$\binom{s}{r}\binom{d}{q}$ such coalitions, and the definitions of $Q$ and $w_q$ yield

$$
\Gamma_S
 =\frac{n+1}{(d+1)^2}
 \sum_{r=0}^s\binom{s}{r}
 \sum_{q=0}^d\frac{\binom{n}{q+r}}{\binom{d}{q}}.
$$

For the rising factorial $(x)_k=x(x+1)\cdots(x+k-1)$, direct cancellation of factorials gives

$$
\frac{\binom{n}{q+r}}{\binom{d}{q}}
 =\frac{(d+1)_s}{(q+1)_r(d-q+1)_{s-r}}.
$$

Thus

$$
\Gamma_S=A_{n,s}\sum_{r=0}^s\binom{s}{r}
 \sum_{q=0}^d
 \frac1{(q+1)_r(d-q+1)_{s-r}}, \tag{2}
$$

where

$$
A_{n,s}=\frac{(n+1)(d+1)_s}{(d+1)^2}.
$$

If $s=1$, then $A_{n,1}=(n+1)/n$, and the terms $r=0,1$ in (2) are respectively

$$
\sum_{q=0}^{n-1}\frac1{n-q}=H_n,
\qquad
\sum_{q=0}^{n-1}\frac1{q+1}=H_n.
$$

Therefore $\Gamma_S=2(n+1)H_n/n=\Theta(\log n)$.

Now fix $s\geq2$. Then $A_{n,s}=\Theta_s(n^{s-1})$. For either boundary value $r=0$ or $r=s$, the corresponding inner sum is

$$
\sum_{j=1}^{d+1}\frac1{(j)_s}.
$$

It is bounded below by $1/(1)_s>0$ and above, uniformly in $d$, by the convergent series $\sum_{j\geq1}j^{-s}$. Thus each boundary sum is $\Theta_s(1)$. For $1\leq r\leq s-1$,

$$
(q+1)_r\geq q+1,
\qquad
(d-q+1)_{s-r}\geq d-q+1,
$$

and hence the inner sum is at most

$$
\sum_{q=0}^d\frac1{(q+1)(d-q+1)}
 =\frac{2H_{d+1}}{d+2}
 =O\left(\frac{\log n}{n}\right).
$$

There are only finitely many $r$, with their number depending on fixed $s$. The two positive boundary sums therefore show that the entire double sum in (2) is both $O_s(1)$ and $\Omega_s(1)$. Consequently

$$
\Gamma_S=\Theta_s(n^{s-1})
\qquad(s\geq2). \tag{3}
$$

Combining (1) with the singleton calculation and (3) proves the asserted upper bounds.

For matching lower bounds, take any nonzero constant $c$ and set $v(T)=c$ for every $T\subseteq N$. Since $S$ is nonempty,

$$
\Delta_Sv(U)=c\sum_{L\subseteq S}(-1)^{s-|L|}=0,
$$

so $I_S(v)=0$, while $v(T)^2=\|v\|_\infty^2$ for every coalition. The exact variance identity becomes

$$
\operatorname{Var}(\widehat I_S)
 =\frac{\|v\|_\infty^2}{m}\Gamma_S.
$$

The established estimates for $\Gamma_S$ give the claimed matching $\Theta(\|v\|_\infty^2\log n/m)$ rate for $s=1$ and $\Theta_s(\|v\|_\infty^2n^{s-1}/m)$ rate for every fixed $s\geq2$.
