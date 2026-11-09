# Problem

## Setup

Let $N$ be a finite set with $|N|=n$, let $S\subseteq N$ be nonempty, and write $s=|S|$. Assume $n\geq\max\{2,s\}$. A value function is any map $v:2^N\to\mathbb R$, with

$$
\|v\|_\infty=\max_{T\subseteq N}|v(T)|.
$$

For $U\subseteq N\setminus S$, define

$$
\Delta_Sv(U)=\sum_{L\subseteq S}(-1)^{s-|L|}v(U\cup L).
$$

Define weights

$$
w_q=\frac{1}{(n-s+1)\binom{n-s}{q}},
\qquad 0\leq q\leq n-s,
$$

and the corresponding interaction

$$
I_S(v)=\sum_{U\subseteq N\setminus S}w_{|U|}\Delta_Sv(U).
$$

Let $T_1,\ldots,T_m$ be independent coalitions sampled from the size-uniform law

$$
Q(T)=\frac{1}{(n+1)\binom{n}{|T|}},
\qquad T\subseteq N,
$$

where $m\geq1$. Consider the importance-sampling estimator

$$
\widehat I_S=\frac{1}{m}\sum_{i=1}^m
v(T_i)(-1)^{s-|S\cap T_i|}
\frac{w_{|T_i\setminus S|}}{Q(T_i)}.
$$

All variances below are with respect to the sampled coalitions.

## Task

Prove that the following worst-case variance rates are sharp as $n\to\infty$:

- If $s=1$, then every $v$ satisfies
  $$
  \operatorname{Var}(\widehat I_S)
  =O\left(\frac{\|v\|_\infty^2\log n}{m}\right),
  $$
  and for every $n$ there is a nonzero $v$ for which the matching lower bound
  $$
  \operatorname{Var}(\widehat I_S)
  =\Omega\left(\frac{\|v\|_\infty^2\log n}{m}\right)
  $$
  holds.

- For every fixed $s\geq2$, every $v$ satisfies
  $$
  \operatorname{Var}(\widehat I_S)
  =O_s\left(\frac{\|v\|_\infty^2 n^{s-1}}{m}\right),
  $$
  and for every sufficiently large $n$ there is a nonzero $v$ for which the matching lower bound
  $$
  \operatorname{Var}(\widehat I_S)
  =\Omega_s\left(\frac{\|v\|_\infty^2 n^{s-1}}{m}\right)
  $$
  holds. Constants may depend on the fixed order $s$, but not on $n$, $m$, $S$, or $v$.
