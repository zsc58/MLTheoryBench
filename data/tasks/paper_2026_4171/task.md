# Problem

## Setup

Let \(K,d\) be fixed positive integers. There are arms \(a\in\{1,\ldots,K\}\). The context \(X_t\) takes values in a measurable subset \(\mathcal X\subseteq\mathbb R^{d_X}\), and the potential outcomes \(Y_t(a)\) are real-valued. The tuples \((X_t,Y_t(1),\ldots,Y_t(K))\) are i.i.d. over time. The experiment proceeds sequentially: at time \(t\), a fresh tuple is independent of the recorded past, its context is observed, and an action is sampled from the measurable probability vector \(\pi_t(\cdot\mid X_t,H_{t-1})\). The observed outcome is \(Y_t=Y_t(A_t)\), and the realized propensity \(p_t=\pi_t(A_t\mid X_t,H_{t-1})\) is recorded. Here
\[
H_t=\sigma\{X_s,p_s,A_s,Y_s:1\le s\le t\},\qquad H_0\text{ is trivial}.
\]
Assume sequential unconfoundedness: conditional on \((H_{t-1},X_t)\), \(A_t\) is independent of all current potential outcomes. Write \(\pi_t(a)=\pi_t(a\mid X_t,H_{t-1})\).

Let \(g:\mathcal X\times\mathbb R\times\mathbb R^d\to\mathbb R^d\) be a known measurable score, twice differentiable with respect to its parameter. Vector norms below are Euclidean and matrix norms are operator norms. Write \(\nabla_\theta g\) for the Jacobian whose \((i,j)\) entry is \(\partial g^{(i)}/\partial\theta_j\). For each arm, the finite vector expectation
\[
m_a(\theta)=\mathbb E[g(X_t,Y_t(a);\theta)],\qquad\theta\in\mathbb R^d,
\]
has a zero \(\theta_a^*\). Assume well separation: for every \(\varepsilon>0\),
\[
\inf_{\|\theta-\theta_a^*\|_2>\varepsilon}\|m_a(\theta)\|_2>0.
\]

Let \(0<R_\theta<\infty\), and assume \(\|\theta_a^*\|_2<R_\theta\) for every arm. There are finite constants \(M_2,M_4,M'_2\) such that, for every arm,
\[
\left\|\mathbb E[g(X_t,Y_t(a);\theta_a^*)g(X_t,Y_t(a);\theta_a^*)^\top\mid X_t]\right\|_{\rm op}\le M_2\quad\text{almost surely},
\]
\[
\sup_{\|\theta\|_2\le R_\theta}\mathbb E\|g(X_t,Y_t(a);\theta)\|_2^2<\infty,
\qquad
\mathbb E\|g(X_t,Y_t(a);\theta_a^*)\|_2^4\le M_4.
\]
For each arm there are nonnegative measurable functions \(\phi_a,\Phi_a:\mathcal X\times\mathbb R\to[0,\infty)\) and a constant \(\varepsilon_a>0\) such that, for all \((x,y)\),
\[
\sup_{\|\theta\|_2\le R_\theta}\|\nabla_\theta g(x,y;\theta)\|_{\rm op}\le\phi_a(x,y),
\qquad
\mathbb E[\phi_a(X_t,Y_t(a))^2\mid X_t]\le M'_2\quad\text{almost surely},
\]
\[
\sup_{\substack{\|\theta-\theta_a^*\|_2\le\varepsilon_a\\1\le i\le d}}
\|\nabla_\theta^2 g^{(i)}(x,y;\theta)\|_{\rm op}\le\Phi_a(x,y),
\qquad
\mathbb E\Phi_a(X_t,Y_t(a))<\infty.
\]
Assume that
\[
J_a=\mathbb E[\nabla_\theta g(X_t,Y_t(a);\theta_a^*)]
\]
is nonsingular for every arm. Let \((\pi_{\min,t})_{t\ge1}\) be a deterministic sequence of positive numbers such that \(\pi_t(a)\ge\pi_{\min,t}\) almost surely for every arm and time.

For deterministic positive numbers \(r_{a,t}\), assume there is a deterministic measurable function \(\rho:\{1,\ldots,K\}\times\mathcal X\to[0,\infty)\) with \(\mathbb E\rho(a,X_t)<\infty\) such that
\[
\mathbb E\left|\frac{r_{a,t}}{\pi_t(a)}-\rho(a,X_t)\right|\longrightarrow0.
\]
Put
\[
S_{a,T}=\left(\sum_{t=1}^T r_{a,t}^{-1}\right)^{1/2},\qquad b_{a,T}=T/S_{a,T}.
\]
As \(T\to\infty\), assume, for every arm,
\[
S_{a,T}\to\infty,\qquad b_{a,T}\to\infty,\qquad
\frac{\sum_{t=1}^T\pi_{\min,t}^{-1}}{T^2}\to0,\qquad
\frac{\sum_{t=1}^T\pi_{\min,t}^{-3}}{S_{a,T}^4}\to0.
\]

Define
\[
G_{a,T}(\theta)=T^{-1}\sum_{t=1}^T\frac{{\bf1}\{A_t=a\}}{p_t}g(X_t,Y_t;\theta).
\]
An IPW-Z estimate sequence consists of \(H_T\)-measurable vectors \(\hat\theta_a=\hat\theta_{a,T}\) taking values in \(\{\theta:\|\theta\|_2\le R_\theta\}\) for every \(T\), and satisfying
\[
G_{a,T}(\hat\theta_a)=o_p(1/b_{a,T}).
\]
Define
\[
\bar I_a=\mathbb E[\rho(a,X_t)g(X_t,Y_t(a);\theta_a^*)g(X_t,Y_t(a);\theta_a^*)^\top],
\qquad \Sigma_a^*=J_a^{-1}\bar I_aJ_a^{-\top}.
\]
For variance estimation set
\[
\widehat J_{a,T}=T^{-1}\sum_{t=1}^T\frac{{\bf1}\{A_t=a\}}{p_t}\nabla_\theta g(X_t,Y_t;\hat\theta_a),
\]
\[
\widehat I_{a,T}=S_{a,T}^{-2}\sum_{t=1}^T\frac{{\bf1}\{A_t=a\}}{p_t^2}g(X_t,Y_t;\hat\theta_a)g(X_t,Y_t;\hat\theta_a)^\top.
\]
Let \(\widehat\Sigma_{a,T}=\widehat J_{a,T}^{-1}\widehat I_{a,T}\widehat J_{a,T}^{-\top}\) when \(\widehat J_{a,T}\) is invertible, and let \(\widehat\Sigma_{a,T}=0_{d\times d}\) otherwise.

## Task

Prove that bounded IPW-Z estimate sequences exist. For every arm, prove that every such sequence is consistent, \(\hat\theta_a\to_p\theta_a^*\), and
\[
b_{a,T}(\hat\theta_a-\theta_a^*)\Rightarrow N(0,\Sigma_a^*).
\]
Moreover, with \(\hat\theta=(\hat\theta_1^\top,\ldots,\hat\theta_K^\top)^\top\), \(\theta^*=((\theta_1^*)^\top,\ldots,(\theta_K^*)^\top)^\top\), and \(D_T=\operatorname{Diag}(b_{1,T}I_d,\ldots,b_{K,T}I_d)\), prove
\[
D_T(\hat\theta-\theta^*)\Rightarrow N\!\left(0,\operatorname{diag}(\Sigma_1^*,\ldots,\Sigma_K^*)\right),
\]
and \(\widehat\Sigma_{a,T}\to_p\Sigma_a^*\) for every arm.
