# Problem

## Setup

Let $n\ge 1$ be an integer, let $x_1,\ldots,x_n\in\mathbb R^d$ be fixed design points, and let the parameter satisfy $\theta\in\mathbb R^p$, where $d$ and $p$ are finite dimensions. Let $f^*:\mathbb R^d\to\mathbb R$ be fixed. Observe
\[
Y_i=f^*(x_i)+\xi_i,\qquad i=1,\ldots,n,
\]
where the noises are independent. For a fixed $\alpha>0$, each noise law has a density proportional to $e^{-V_i(z)}$ on a nonempty open interval $I_i\subseteq\mathbb R$, possibly unbounded, and zero outside that interval. The potential $V_i$ is twice differentiable on $I_i$ and satisfies $V_i''(z)\ge\alpha$ there. Values of the density at interval endpoints are immaterial.

Let $f(x;\theta)$ be real-valued and differentiable in $\theta$, and write $f_i(\theta)=f(x_i;\theta)$. Fix $\lambda\ge0$. For every $y\in\mathbb R^n$, define
\[
\widehat L_y(\theta)=\frac1{2n}\sum_{i=1}^n(f_i(\theta)-y_i)^2,\qquad
\widehat L_{\lambda,y}(\theta)=\widehat L_y(\theta)+\frac\lambda2\|\theta\|^2,
\]
and write $\widehat L=\widehat L_Y$.

Fix a single $C^1$ map $y\mapsto\theta_y$ from $\mathbb R^n$ to $\mathbb R^p$. For every $y\in\mathbb R^n$, assume that each $f_i$ is twice differentiable at $\theta_y$, that $\theta_y$ is a local minimizer of $\widehat L_{\lambda,y}$, and that
\[
\nabla_\theta\widehat L_{\lambda,y}(\theta_y)=0,\qquad
H_y:=\nabla_\theta^2\widehat L_{\lambda,y}(\theta_y)\succ0.
\]
For each $j=1,\ldots,n$, define the prediction map $h_j(y)=f_j(\theta_y)$. Assume that $h_j$ is locally Lipschitz and that
\[
\mathbb E[h_j(Y)^2]<\infty,\qquad
\mathbb E\!\left[\sum_{k=1}^n\bigl(\partial_{y_k}h_j(Y)\bigr)^2\right]<\infty.
\]

At the fitted parameter, put $g_i=\nabla_\theta f_i(\theta_Y)$ and define
\[
G_Y=\frac1n\sum_{i=1}^n g_i g_i^\top,\qquad
\Delta_Y=\frac1n\sum_{i=1}^n(f_i(\theta_Y)-Y_i)\nabla_\theta^2f_i(\theta_Y),\qquad
H_Y=G_Y+\Delta_Y+\lambda I_p,
\]
\[
d_{\rm eff}(\theta_Y;\lambda)=\operatorname{tr}\!\left((H_Y^{-1}G_Y)^2\right),
\]
where $I_p$ is the identity matrix on $\mathbb R^p$.

For each $i$, let $Y_i'$ have the same law as $Y_i$ and be independent of the entire training vector $Y$. Define
\[
Y^{(i)}=(Y_1,\ldots,Y_{i-1},Y_i',Y_{i+1},\ldots,Y_n),
\]
and use the same fixed selection map to obtain $\theta_{Y^{(i)}}$. For deterministic $\theta$, define
\[
L(\theta)=\frac1{2n}\sum_{i=1}^n\mathbb E_{Y_i'}[(f_i(\theta)-Y_i')^2].
\]

## Task

Prove the following integrated claim. The selected ridge-regularized nondegenerate local-minimizer predictor obeys
\[
\frac1n\sum_{i=1}^n\mathbb E\!\left[(f_i(\theta_Y)-f_i(\theta_{Y^{(i)}}))^2\right]
\le \frac4{\alpha n}\,\mathbb E\left[d_{\rm eff}(\theta_Y;\lambda)\right],
\]
and consequently
\[
\mathbb E[L(\theta_Y)-\widehat L(\theta_Y)]
\le \sqrt{\frac{8\,\mathbb E\widehat L(\theta_Y)\,\mathbb E d_{\rm eff}(\theta_Y;\lambda)}{\alpha n}}
+\frac{2\,\mathbb E d_{\rm eff}(\theta_Y;\lambda)}{\alpha n}.
\]
In particular, for every $\eta>0$,
\[
\mathbb E[L(\theta_Y)-\widehat L(\theta_Y)]
\le \eta\,\mathbb E\widehat L(\theta_Y)+\left(2+\frac2\eta\right)\frac{\mathbb E d_{\rm eff}(\theta_Y;\lambda)}{\alpha n}.
\]
