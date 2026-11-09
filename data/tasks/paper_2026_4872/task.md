# Problem

## Setup

Fix an integer \(d\ge1\), a symmetric positive-definite matrix \(\Sigma\in\mathbb R^{d\times d}\), distinct vectors \(\mu_o,\mu_n\in\mathbb R^d\), and \(\alpha\in(0,1)\). Let
\[
p_o=\mathcal N(\mu_o,\Sigma),\qquad p_n=\mathcal N(\mu_n,\Sigma),\qquad p_\alpha=\alpha p_o+(1-\alpha)p_n,
\]
where the same symbols denote the associated Lebesgue densities. For \(\beta\in(0,1)\) and \(m_o,m_n\in\mathbb R^d\), define
\[
q_{\beta,m_o,m_n}=\beta q_o(\cdot;m_o)+(1-\beta)q_n(\cdot;m_n),\qquad
q_o(\cdot;m_o)=\mathcal N(m_o,\Sigma),\quad q_n(\cdot;m_n)=\mathcal N(m_n,\Sigma).
\]
In reverse-KL formulas, write \(q=q_{\beta,m_o,m_n}\), \(q_o=q_o(\cdot;m_o)\), and \(q_n=q_n(\cdot;m_n)\). All integrals below are over \(\mathbb R^d\) with respect to Lebesgue measure, and
\[
\operatorname{KL}(f\Vert g)=\int f(x)\log\frac{f(x)}{g(x)}\,dx.
\]
Unsubscripted vector norms are Euclidean, \(\|A\|_{op}=\sup_{\|v\|=1}\|Av\|\), and
\[
\|v\|_{\Sigma^{-1}}=(v^\top\Sigma^{-1}v)^{1/2},\qquad \sigma(\phi)=(1+e^{-\phi})^{-1}.
\]

For forward-KL weight optimization, extend the fixed-component mixture to \(\beta\in[0,1]\) by
\[
q_\beta=\beta p_o+(1-\beta)p_n,\qquad L_F(\beta)=\operatorname{KL}(p_n\Vert q_\beta).
\]
An optimum at \(\beta^*=0\) represents old-mass forgetting. Define
\[
L_R(\beta,m_o,m_n)=\operatorname{KL}(q_{\beta,m_o,m_n}\Vert p_\alpha).
\]
At \(m_o=\mu_o\), an \(\varepsilon\)-bound on old-component drift is an inequality \(\|\nabla_{m_o}L_R\|\le\varepsilon\). Such a bound is vanishing in a specified parameter limit when the nonnegative, parameter-dependent \(\varepsilon\) tends to zero. All parameter derivatives hold the target parameters and covariance fixed, and an old-mean derivative evaluated at \(m_o=\mu_o\) is taken before substituting that equality.

## Task

Prove the following integrated theorem.

First, \(L_F\) is strictly increasing on \([0,1]\), has unique minimizer \(\beta^*=0\), and, for every finite initial logit \(\phi(0)\in\mathbb R\), the gradient flow
\[
\dot\phi(t)=-\partial_\phi L_F(\sigma(\phi(t))),\qquad \beta(t)=\sigma(\phi(t)),
\]
is defined for all \(t\ge0\) and satisfies \(\beta(t)\downarrow0\) as \(t\to\infty\). For \(0<\beta<1\), with \(\beta=\sigma(\phi)\) and \(r_o(x)=\beta p_o(x)/q_\beta(x)\), prove
\[
\partial_\phi\log q_\beta(x)=r_o(x)-\beta,
\qquad
\mathbb E_{p_n}r_o\le\frac12\sqrt{\frac{\beta}{1-\beta}}\exp\!\left(-\frac{\|\mu_o-\mu_n\|_{\Sigma^{-1}}^2}{8}\right).
\]

Second, prove that \((\beta,m_o,m_n)=(\alpha,\mu_o,\mu_n)\) is a global minimizer of \(L_R\), derive
\[
\partial_\beta L_R=\int(q_o-q_n)\log(q/p_\alpha)\,dx,
\qquad
\nabla_{m_n}L_R=(1-\beta)\int q_n\Sigma^{-1}(x-m_n)\log(q/p_\alpha)\,dx,
\]
and show that both derivatives vanish at the matching point.

Finally, evaluate at \(m_o=\mu_o\), with \(m_n\) arbitrary. In this part define
\[
r_o(x)=\frac{\beta p_o(x)}{q_{\beta,\mu_o,m_n}(x)},\qquad
s_o(x)=\frac{\alpha p_o(x)}{p_\alpha(x)},\qquad
\varepsilon_q=\mathbb E_{p_o}(1-r_o),\quad
\varepsilon_p=\mathbb E_{p_o}(1-s_o).
\]
Prove
\[
\nabla_{m_o}L_R(\beta,\mu_o,m_n)
=\beta\Sigma^{-1}\big[\varepsilon_q(m_n-\mu_o)-\varepsilon_p(\mu_n-\mu_o)\big]
\]
and deduce
\[
\|\nabla_{m_o}L_R(\beta,\mu_o,m_n)\|
\le\beta\|\Sigma^{-1}\|_{op}\big(\varepsilon_q\|m_n-\mu_o\|+\varepsilon_p\|\mu_n-\mu_o\|\big).
\]
Establish the explicit overlap estimates
\[
\varepsilon_q\le\frac12\sqrt{\frac{1-\beta}{\beta}}\exp\!\left(-\frac{\|m_n-\mu_o\|_{\Sigma^{-1}}^2}{8}\right),\qquad
\varepsilon_p\le\frac12\sqrt{\frac{1-\alpha}{\alpha}}\exp\!\left(-\frac{\|\mu_n-\mu_o\|_{\Sigma^{-1}}^2}{8}\right).
\]
These estimates are required throughout the stated parameter domain. Their exponential-decay interpretation holds with \(d,\Sigma,\alpha,\beta\) fixed, in the respective learner and target separations displayed above. The separation limit for vanishing old-component drift sends both \(\|m_n-\mu_o\|_{\Sigma^{-1}}\) and \(\|\mu_n-\mu_o\|_{\Sigma^{-1}}\) to infinity.
