# Problem

## Setup

Let \(n\) be a positive integer, let \([n]=\{1,\ldots,n\}\), and let \(\Omega=\{-1,1\}^n\) with uniform probability measure. For \(S\subseteq[n]\), define the Walsh character \(\chi_S(x)=\prod_{i\in S}x_i\), with \(\chi_\emptyset=1\). For a function \(f:\Omega\to\mathbb R\), write its Walsh expansion as \(f(x)=\sum_{S\subseteq[n]}\theta_S\chi_S(x)\), and set \(\|f\|_\infty=\max_{x\in\Omega}|f(x)|\). For an integer \(1\leq s\leq n\), let
\[
\mathcal S_{n,s}=\left\{f:\Omega\to\mathbb R:\|f\|_\infty\leq1,\;|\{S:\theta_S\ne0\}|\leq s\right\}.
\]

Fix \(\sigma>0\). A learner may use internal randomness independent of the noises. At time \(t\), it chooses \(X_t\in\Omega\) measurably as a function of that randomness and the preceding query-response pairs \((X_1,Y_1),\ldots,(X_{t-1},Y_{t-1})\), and then receives
\[
Y_t=f(X_t)+\xi_t.
\]
The noises are independent across time, independent of the learner's internal randomness, and centered. In this problem, the condition that they are \(\sigma\)-subgaussian means
\[
\Pr(|\xi_t|\geq u)\leq2\exp\!\left(-\frac{u^2}{2\sigma^2}\right)
\quad\text{for every }u>0\text{ and every }t.
\]
They need not be identically distributed. After \(m\) queries the learner outputs a measurable function \(\widehat f:\Omega\to\mathbb R\) based on its internal randomness and all \(m\) query-response pairs; the output is not required to belong to \(\mathcal S_{n,s}\).

With dependence on \(\sigma\) suppressed in the notation, define \(m^*(\mathcal S_{n,s},\epsilon,\delta)\) as the least nonnegative integer \(m\) for which some such learner satisfies, uniformly over \(f\in\mathcal S_{n,s}\) and all allowed noise laws,
\[
\Pr\bigl(\|\widehat f-f\|_\infty>\epsilon\bigr)\leq\delta.
\]
The probability includes both the observation noise and the learner's randomness.

## Task

Prove that there are universal constants \(c,C,\epsilon_0>0\) such that, for every integer \(n\geq1\), every integer \(1\leq s\leq n\), \(0<\epsilon\leq\epsilon_0\), \(0<\delta\leq1/4\), and every \(\sigma>0\),
\[
 c\,\frac{\sigma^2}{\epsilon^2}\left(ns^2+s\log\frac1\delta\right)
 \leq m^*(\mathcal S_{n,s},\epsilon,\delta)
 \leq C\,\frac{\sigma^2+1}{\epsilon^2}\left(ns^2+s\log\frac1\delta\right).
\]
In particular, when \(\sigma\) is bounded below by a positive universal constant, the minimax complexity is \(\Theta\!\left((\sigma^2/\epsilon^2)(ns^2+s\log(1/\delta))\right)\).
