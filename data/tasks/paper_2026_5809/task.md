# Problem

## Setup

Consider right-censored observations \((X,T,\Delta)\), where \(X\) takes values in a measurable space \(\mathcal X\), \(T>0\), and \(\Delta\in\{0,1\}\), with \(\Delta=1\) denoting an observed event. An ordered pair \((1,2)\) is comparable when \(T_1<T_2\) and \(\Delta_1=1\). Assume that this event has positive probability, and let \(Q\) denote the conditional distribution of the ordered pair given this event. A measurable scalar risk score \(s:\mathcal X\to\mathbb R\) assigns larger values to greater risk. Define the population concordance index, with ties split equally, by
\[
C(s)=Q\big(s(X_1)>s(X_2)\big)+\tfrac12Q\big(s(X_1)=s(X_2)\big).
\]
Let the comparable-pair score gap be \(G=s(X_1)-s(X_2)\). Assume that \(G\) has a Lebesgue density \(p\) under \(Q\) and that for some fixed \(\varepsilon>0\) and \(0\le B<\infty\),
\[
p(z)\le B\qquad\text{for all }|z|\le\varepsilon.
\]
For temperature \(\tau>0\), define \(\sigma(u)=1/(1+e^{-u})\) and the population sigmoid concordance loss
\[
L_\tau(s)=\mathbb E_Q\left[\sigma\!\left(-\frac{s(X_1)-s(X_2)}{\tau}\right)\right].
\]

## Task

Prove that, as \(\tau\downarrow0\),
\[
\left|L_\tau(s)-(1-C(s))\right|\le 2B\tau+e^{-\varepsilon/\tau}=2B\tau+o(\tau).
\]
The bound must hold uniformly over any class of scores for which the same \(B\) and \(\varepsilon\) satisfy the density condition. Consequently, if two scores \(s_a,s_b\) both satisfy this density condition with the same \(B\) and \(\varepsilon\), and satisfy
\[
C(s_a)-C(s_b)>2\big(2B\tau+e^{-\varepsilon/\tau}\big),
\]
then \(L_\tau(s_a)<L_\tau(s_b)\).
