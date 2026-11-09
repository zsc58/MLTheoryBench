# Problem

## Setup

Let \(d\ge1\) be an integer and let \(\mathcal P\subset\mathbb R^d\) be a finite nonempty pool satisfying \(\|z\|_2\le1\). Let \(\pi:\mathcal P\to[0,1]\) be a fixed weight function, and put
\[
\mathcal P_+=\{z\in\mathcal P:\pi(z)>0\}.
\]

Fix \(a_0,b_0>0\). The variance \(\sigma^2\) is a latent random variable with density
\[
p_{\sigma^2}(r)=\frac{b_0^{a_0}}{\Gamma(a_0)}r^{-a_0-1}\exp(-b_0/r),\qquad r>0,
\]
where \(\Gamma\) is the Euler gamma function. Conditional on \(\sigma^2\), the parameter has prior
\[
\theta\mid\sigma^2\sim\mathcal N(0,\sigma^2 I_d).
\]
A positive-weight query at \(z_s\) reveals
\[
Y_s=z_s^\top\theta+\sqrt{\frac{\sigma^2}{\pi(z_s)}}E_s,
\]
where the \(E_s\) are independent standard normal variables, independent of \((\theta,\sigma^2)\) and of any auxiliary randomization used for query selection. Each query is chosen using only previously observed history and such independent auxiliary randomization. A zero-weight step reveals no response and leaves the posterior unchanged.

Write \(\mathcal D_{t-1}\) for the observed query history before stage \(t\), including the chosen candidates and all responses actually revealed. Define
\[
S_{t-1}=\sum_{s<t}\pi(z_s)z_sz_s^\top,
\qquad
V_{t-1}=(I_d+S_{t-1})^{-1}.
\]
The conditional parameter posterior covariance is \(\sigma^2V_{t-1}\).

For \(z\in\mathcal P_+\), define the acquisition by the expected reduction in marginal parameter differential entropy:
\[
A_t(z)=H(\theta\mid\mathcal D_{t-1})-
\mathbb E_{Y\mid\mathcal D_{t-1},z}
\bigl[H(\theta\mid\mathcal D_{t-1},(z,Y))\bigr].
\]
Here each posterior law of \(\theta\) integrates out the latent variance, and the expectation uses the posterior predictive law specified by the model. For \(z\notin\mathcal P_+\), set \(A_t(z)=0\), consistently with revealing no response. All logarithms are natural.

## Task

Prove the following integrated theorem.

For every stage and observed history with \(\mathcal P_+\ne\varnothing\), there is a finite real number \(c_t\), independent of the candidate \(z\in\mathcal P_+\), such that
\[
A_t(z)=c_t+\frac12\log\!\left(1+\pi(z)z^\top V_{t-1}z\right),
\qquad z\in\mathcal P_+.
\]
Moreover, the exact maximizing sets satisfy
\[
\arg\max_{z\in\mathcal P}A_t(z)
=
\arg\max_{z\in\mathcal P_+}\pi(z)z^\top V_{t-1}z.
\]
If \(\mathcal P_+=\varnothing\), every candidate has acquisition zero and every candidate maximizes it.

For every integer \(t\ge0\) and every sequence \(z_1,\ldots,z_t\in\mathcal P\), including any sequence produced by greedy acquisition, write \(\pi_s=\pi(z_s)\), set \(V_0=I_d\), and define
\[
V_s=\left(I_d+\sum_{j=1}^s\pi_jz_jz_j^\top\right)^{-1}.
\]
Prove
\[
V_s^{-1}=V_{s-1}^{-1}+\pi_s z_sz_s^\top
\quad(1\le s\le t),
\qquad
\sum_{s=1}^t\pi_s z_s^\top V_{s-1}z_s
\le 2d\log\!\left(1+\frac td\right).
\]
Empty sums are zero. In particular, the displayed cumulative weighted score is \(O(d\log t)\) for fixed \(d\) as \(t\to\infty\).
