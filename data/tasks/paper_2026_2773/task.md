# Problem

## Setup

Let r>=1 be a fixed integer and n>=r. Let (X_i,Y_i)_{i=1}^n be iid copies of (X,Y), with Y taking values in a measurable space \(\mathcal Y\). Let \(\mu:\mathcal X\to\mathcal Y\) be a fixed measurable prediction function and put \(\hat Y_i=\mu(X_i)\). Let \(h:\mathcal Y^r\to\mathbb R\) be measurable and symmetric, with

\[
E[h(Y_1,\ldots,Y_r)^2]<\infty,
\qquad E[h(\hat Y_1,\ldots,\hat Y_r)^2]<\infty.
\]

Define

\[
\theta^*=E[h(Y_1,\ldots,Y_r)],\qquad
\mathcal C_{n,r}=\{(i_1,\ldots,i_r):1\le i_1<\cdots<i_r\le n\},
\]
\[
U_n=\binom nr^{-1}\sum_{I\in\mathcal C_{n,r}}h(Y_I).
\]

Here \(Y_I=(Y_{i_1},\ldots,Y_{i_r})\), and the same tuple convention is used for predicted labels. Define the population functions

\[
h_1(y)=E[h(y,Y_2,\ldots,Y_r)],\qquad
h_1^\mu(\hat y)=E[h(\hat y,\hat Y_2,\ldots,\hat Y_r)].
\]

For r=1 these are both the function h. Assume

\[
\operatorname{Var}(h_1(Y))>0,
\qquad \operatorname{Var}(h_1^\mu(\mu(X)))>0.
\]

Let a and b be supplied fixed measurable real-valued functions on \(\mathcal Y\), used to form the sampling score

\[
V(x)=E[|a(Y)-b(\mu(X))|\mid X=x].
\]

Assume V has a measurable version with \(0<E[V(X)]<\infty\). No equality between a,b and the population functions h_1,h_1^mu is assumed. Fix \(\rho\in(0,1]\) and \(\tau\in[0,1]\\), independent of n, and define the fixed target rule

\[
\pi_\tau^*(x)=\rho\left(\tau\frac{V(x)}{E[V(X)]}+1-\tau\right).
\]

Assume this rule takes values in [0,1].

Initially only the inference covariates X_1,...,X_n are observed. The learned probabilities \(q_i=\hat\pi_\tau(X_i)\in[0,1]\) are measurable functions of these covariates and auxiliary training information, chosen before the labeling randomization below. They do not use the unqueried inference labels. The prediction function and the supplied score-building functions remain fixed in this inference experiment. Conditional on the full inference data and the auxiliary training information, the labeling indicators \(\xi_i=\xi_i(\hat\pi_\tau)\) are independent Bernoulli(q_i) variables. Thus labeling uses fresh randomness, not randomness already used to fit the probabilities.

Assume there is a constant \(\pi_{\min}>0\), independent of n, such that

\[
\pi_\tau^*(X)\ge\pi_{\min}\quad\text{almost surely},
\qquad
P\left(\min_{1\le i\le n}q_i\ge\pi_{\min}/2\right)\longrightarrow1,
\]
\[
\max_{1\le i\le n}|q_i-\pi_\tau^*(X_i)|=O_p(n^{-1/2}).
\]

For any vector of sampling probabilities \(q=(q_1,\ldots,q_n)\) with its associated Bernoulli indicators \(\xi_i(q)\), define the unnormalized estimator, when all q_i>0, by

\[
\Delta_h(I)=h(Y_I)-h(\hat Y_I),
\]
\[
U_{\rm AIPW}^{q}
=\binom nr^{-1}\sum_{I\in\mathcal C_{n,r}}
\left[h(\hat Y_I)+\Delta_h(I)\prod_{i\in I}\frac{\xi_i(q)}{q_i}\right].
\]

The superscript \(\hat\pi_\tau\) means the learned probabilities q_i and their indicators specified above. Put \(h_{1i}=h_1(Y_i)\) and \(\hat h_{1i}=h_1^\mu(\hat Y_i)\). These are population projection evaluations. Define, using the learned probabilities and indicators,

\[
\hat m_1=\frac1n\sum_{i=1}^n\frac{\xi_i}{q_i}h_{1i},
\qquad
\hat m_2=\frac1n\sum_{i=1}^n\frac{\xi_i}{q_i}h_{1i}^2,
\]
\[
\widehat{\operatorname{Var}}_1=r^2(\hat m_2-\hat m_1^2),
\qquad
\widehat{\operatorname{Var}}_2
=\frac{r^2}{n}\sum_{i=1}^n\frac{\xi_i}{q_i}
(h_{1i}-\hat h_{1i})^2\left(\frac1{q_i}-1\right).
\]

For a finite-sample convention, if any learned q_i equals zero, set \(U_{\rm AIPW}^{\hat\pi_\tau},\hat m_1,\hat m_2,\widehat{\operatorname{Var}}_1,\widehat{\operatorname{Var}}_2\) all equal to zero on that event. Otherwise use the displayed formulas. Set

\[
\hat\sigma=\sqrt{\max\{0,\widehat{\operatorname{Var}}_1+\widehat{\operatorname{Var}}_2\}}.
\]

To define the target variance, let \((X,Y)\) have the population law and, conditional on (X,Y), let \(\xi^*\) be Bernoulli\((\pi_\tau^*(X))\). Put

\[
\sigma_*^2=r^2\operatorname{Var}\left(
h_1^\mu(\mu(X))+
\frac{\xi^*}{\pi_\tau^*(X)}[h_1(Y)-h_1^\mu(\mu(X))]
\right).
\]

## Task

Prove that, as n tends to infinity,

\[
\sqrt n\left(U_{\rm AIPW}^{\hat\pi_\tau}-\theta^*\right)
\Rightarrow N(0,\sigma_*^2),
\qquad
\widehat{\operatorname{Var}}_1+\widehat{\operatorname{Var}}_2
\xrightarrow{p}\sigma_*^2.
\]

For every fixed \(\alpha\in(0,1)\), also prove

\[
P(\theta^*\in C_{n,\alpha})\longrightarrow1-\alpha,
\]

where \(z_{1-\alpha/2}\) is the \((1-\alpha/2)\)-quantile of the standard normal distribution and

\[
C_{n,\alpha}=
\left[
U_{\rm AIPW}^{\hat\pi_\tau}-z_{1-\alpha/2}\frac{\hat\sigma}{\sqrt n},
U_{\rm AIPW}^{\hat\pi_\tau}+z_{1-\alpha/2}\frac{\hat\sigma}{\sqrt n}
\right].
\]
