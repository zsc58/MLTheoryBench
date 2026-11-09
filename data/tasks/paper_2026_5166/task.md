# Problem

## Setup

Let $a>0$, $r>0$, and $m\in\mathbb R$. For $x\in\mathbb R$, define

$$E(x)=-\tfrac12\log(a+e^x)-\frac{r}{2(a+e^x)}-\tfrac14(x-m)^2.$$

## Specification of the approximation

Define

$$C(x)=E(x)+\frac{r}{2(a+e^x)}.$$

For $\varepsilon>0$, let $E_\varepsilon$ be the displayed energy with $a$ replaced by $\varepsilon$ and with $r,m$ unchanged. Set

$$F(x)=\lim_{\varepsilon\downarrow0}E_\varepsilon(x),$$

and let $y$ be the unique real stationary point of $F$. Establishing that this limit and this point are well-defined is part of the task.

The two quadratic functions $Q_1,Q_2$, regarded up to additive constants, are specified by

$$Q_1'(m)=E'(m),\qquad Q_1''(x)=C''(m)\quad(x\in\mathbb R),$$

and

$$Q_2'(y)=E'(y),\qquad
Q_2''(x)=
\begin{cases}
E''(y),&E''(y)<0,\\
C''(y),&E''(y)\geq0
\end{cases}
\quad(x\in\mathbb R).$$

For $i=1,2$, let $G_i$ be the probability law whose density is proportional to $\exp(Q_i)$, provided its normalizing integral exists. Write $u_i$ for its mean and $p_i$ for its precision, meaning the reciprocal of its variance.

Form a probability mixture

$$M=(1-b)G_1+bG_2,$$

where the respective weights are proportional to $\exp(E(u_1))$ and $\exp(E(u_2))$. The requested approximation is the Gaussian having the first two moments of $M$.

## Task

Derive explicit expressions for the secondary expansion point $y$, both component means and precisions, the mixing weight, and the final Gaussian's mean $\bar u$, variance $\bar v$, and precision $\bar p$.

Prove that, for every $a>0$, $r>0$, and $m\in\mathbb R$, this entire construction is well-defined and the final precision is strictly positive. Prove that the final Gaussian has the first two moments of the constructed mixture and that the higher-energy component mean receives the greater mixture weight. The construction must retain both prescribed expansions, including when $E$ has two local maxima.
