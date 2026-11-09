# Problem

## Setup

Let \(\mathcal X\subseteq\mathbb R^d\) and \(\mathcal Y\subseteq\mathbb R^q\). Let \((\Omega,\mathcal F,\pi)\) be a probability space, let \(\eta\sim\pi\), and let \(f,g:\mathcal X\times\Omega\to\mathcal Y\) be measurable maps that are differentiable in \(x\) for \(\pi\)-almost every noise realization. For each \(x\in\mathcal X\), let the conditional law of interest be represented as the law of \(g(x,\eta)\in\mathcal Y\). Let \(f(x,\eta)\in\mathcal Y\) be a differentiable approximate sampler driven by the same noise. Let \(G\) be a target probability distribution on \(\mathcal Y\). Write \(J_f=\partial_x f\) and \(J_g=\partial_x g\).

Let \(k\) be a characteristic positive-definite kernel with RKHS \(\mathcal H\) and a continuously differentiable feature map \(\Phi\). Assume that, for constants \(K,L,H>0\),
\[
0\le k(y,y')\le K,\qquad
\|D\Phi(y)\|_{\rm op}\le L,\qquad
\|\Phi(y)-\Phi(y')\|_{\mathcal H}\le L\|y-y'\|,
\]
and
\[
\|D\Phi(y)-D\Phi(y')\|_{\rm op}\le H\|y-y'\|.
\]
For a law \(Q\), write \(\mu_Q=\mathbb E_{Y\sim Q}\Phi(Y)\), so that
\(\operatorname{MMD}_k^2(Q,R)=\|\mu_Q-\mu_R\|_{\mathcal H}^2\).

Assume, uniformly in \(x\), that for constants \(\epsilon_o,\epsilon_J,C_f\ge0\),
\[
\mathbb E\|f(x,\eta)-g(x,\eta)\|^2\le\epsilon_o^2,
\qquad
\mathbb E\|J_f(x,\eta)-J_g(x,\eta)\|_F^2\le\epsilon_J^2,
\]
and
\[
\mathbb E\|J_f(x,\eta)\|_F^2\le C_f^2,
\qquad
\mathbb E\|J_g(x,\eta)\|_F^2\le C_f^2.
\]
Assume that, for every \(x\), differentiation in \(x\) may be interchanged with the expectations defining \(\mathbb E_\eta\Phi(f(x,\eta))\), \(\mathbb E_\eta\Phi(g(x,\eta))\), and \(\mathbb E\widehat L_f(x)\).

Define
\[
L(x)=\operatorname{MMD}_k^2(\mathcal L(g(x,\eta)),G),
\qquad
L_f(x)=\operatorname{MMD}_k^2(\mathcal L(f(x,\eta)),G).
\]
For \(N,M\ge2\), draw \(\eta_1,\ldots,\eta_N\) independently with common law \(\pi\), and draw \(T_1,\ldots,T_M\) independently with common law \(G\), independently of \(\eta_1,\ldots,\eta_N\). Set \(Y_i=f(x,\eta_i)\), and define the unbiased estimator
\[
\widehat L_f(x)=\frac{1}{N(N-1)}\sum_{i\ne j}k(Y_i,Y_j)
-\frac{2}{NM}\sum_{i=1}^N\sum_{r=1}^M k(Y_i,T_r)
+\frac{1}{M(M-1)}\sum_{r\ne s}k(T_r,T_s).
\]
Its gradient is obtained by differentiating through the samples \(Y_i\). All expectations involving \(\widehat L_f\) or its gradient are over these independent samples.

## Task

Prove that there is a universal constant \(c\) such that, for every \(x\in\mathcal X\),
\[
\left\|\mathbb E\nabla_x\widehat L_f(x)-\nabla_xL(x)\right\|
\le 8L\sqrt K\,\epsilon_J+
\bigl(2L^2C_f+8HC_f\sqrt K\bigr)\epsilon_o,
\]
and
\[
\mathbb E\left\|\nabla_x\widehat L_f(x)-\mathbb E\nabla_x\widehat L_f(x)\right\|^2
\le C_V\left(\frac1N+\frac1M\right),
\qquad C_V\le cL^2KC_f^2.
]
