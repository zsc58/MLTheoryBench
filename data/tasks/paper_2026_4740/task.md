# Problem

## Setup

Let \(K\subseteq[0,1]^d\) be convex, down-closed (if \(0\le u\le v\in K\), then \(u\in K\)), contain \(0\), and have bounded diameter. Let \(f:[0,1]^d\to\mathbb R_{\ge0}\) be differentiable and continuous, non-monotone, and DR-submodular: whenever \(u\le v\) coordinatewise in the cube, \(\nabla f(u)\ge\nabla f(v)\) coordinatewise. Assume \(\nabla f\) is bounded and Lipschitz on K. For \(\alpha\in(0,1]\), call the restriction of f to K \(\alpha\)-linearizable if there are maps \(h:K\to K\) and \(g_f:K\to\mathbb R^d\), and a constant \(\beta>0\), such that for every \(x,y\in K\),
\[
\alpha f(y)-f(h(x))\le\beta\langle g_f(x),y-x\rangle.
\]

## Task

Prove that f is 1/e-linearizable on K. More precisely, with
\[
h(x)=1-e^{-x}
\]
(coordinatewise),
\[
F(x)=\int_0^1\frac{e^{z-1}}{(1-e^{-1})z}\bigl(f(1-e^{-zx})-f(0)\bigr)\,dz,
\]
and \(g_f(x)=\nabla F(x)\), show that for all \(x,y\in K\),
\[
\frac1e f(y)-f(h(x))\le (1-e^{-1})\langle g_f(x),y-x\rangle.
\]
