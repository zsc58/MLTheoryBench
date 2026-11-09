# Problem

## Setup

Fix a predictor, a training sample, and a disjoint calibration sample \((X_i,Y_i)_{i=1}^n\), where \(n\ge1\), with exchangeable regression pairs. Let the output space be \(\mathbb R^d\) for a finite positive integer \(d\). Let \(S(x,y)\) be a real-valued, positively oriented score, continuously differentiable in \(y\). Define the calibration scores \(S_i=S(X_i,Y_i)\).

Fix an input \(x\) and choose \(\alpha\in(0,1)\) such that
\[
k=\lceil(1-\alpha)(n+1)\rceil
\quad\text{satisfies}\quad 1\le k\le n.
\]
Let \(\tau_\alpha\) be the \(k\)-th order statistic of \(S_1,\ldots,S_n\), and define
\[
C_\alpha(x)=\{y\in\mathbb R^d:S(x,y)\le\tau_\alpha\},\qquad
B_\alpha(x)=\{y\in\mathbb R^d:S(x,y)=\tau_\alpha\}.
\]
Assume the conformal sets are nonempty. Fix \(\lambda>0\). Let \(y:[0,\infty)\to\mathbb R^d\) be a trajectory that exists for every \(t\ge0\), is absolutely continuous on every compact time interval, and follows the minimum-norm score-controlling flow: for almost every \(t\ge0\),
\[
y'(t)=
\begin{cases}
-\lambda\,\dfrac{(S(x,y(t))-\tau_\alpha)\nabla_yS(x,y(t))}{\|\nabla_yS(x,y(t))\|_2^2},&S(x,y(t))\ne\tau_\alpha,\\[6pt]
0,&S(x,y(t))=\tau_\alpha.
\end{cases}
\]
Assume \(\nabla_yS(x,y(t))\ne0\) whenever \(S(x,y(t))\ne\tau_\alpha\). Write \(y_0=y(0)\).

## Task

Prove that, with \(\varepsilon(t)=S(x,y(t))-\tau_\alpha\),
\[
\varepsilon(t)=\varepsilon(0)e^{-\lambda t}\quad(t\ge0),
\qquad S(x,y(t))\to\tau_\alpha,
\]
and every omega-limit point of \(y(t)\) belongs to \(B_\alpha(x)\). Moreover, if there exist \(T\in[0,\infty)\) and \(m>0\) such that
\[
\|\nabla_yS(x,y(t))\|_2\ge m\quad\text{for all }t\ge T,
\]
then \(y(t)\) converges to a unique point \(y_\infty\in B_\alpha(x)\) and, for all \(t\ge T\),
\[
\|y(t)-y_\infty\|_2
\le\frac{|S(x,y_0)-\tau_\alpha|}{m}e^{-\lambda t}.
\]
