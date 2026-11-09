# Problem

## Setup

Fix integers \(d,M\geq1\), data \((x^m,y^m)_{m=1}^M\in(\mathbb R^d\times\mathbb R)^M\), and constants \(C_x,C_y>0\) such that \(\|x^m\|_2\leq C_x\) and \(|y^m|\leq C_y\). Assume that every \(x^m\) is nonzero and that no two inputs are collinear: for \(m\ne n\),
\[
\operatorname{span}(x^m)\cap\operatorname{span}(x^n)=\{0\}.
\]

Let \(\beta\in(1/2,1)\). Let \(\sigma:\mathbb R\to\mathbb R\) be bounded and Lipschitz, non-polynomial, with bounded Lipschitz derivative \(\sigma'\) and bounded second derivative \(\sigma''\). Let \(\mu_0\) be a law on \((c,w,\eta)\in\mathbb R\times\mathbb R^d\times\mathbb R\) such that \(c\) is independent of \((w,\eta)\), has mean zero and compact support, and the \((w,\eta)\)-marginal assigns positive mass to every measurable set of positive Lebesgue measure.

For parameters \(\theta=(c^i,w^i,\eta^i)_{i=1}^N\), define
\[
f_\theta^N(u)=N^{-\beta}\sum_{i=1}^N c^i\sigma(w^i\cdot u+\eta^i),
\qquad
L^N(\theta)=\frac1{2M}\|y-f_\theta^N(x)\|_2^2,
\]
where \(y=(y^m)_{m=1}^M\) and \(f_\theta^N(x)=(f_\theta^N(x^m))_{m=1}^M\).

Define the deterministic \(M\times M\) matrix
\[
B_{mn}=\frac1M\int\!\left[\sigma(w\cdot x^m+\eta)\sigma(w\cdot x^n+\eta)
+c^2\sigma'(w\cdot x^m+\eta)\sigma'(w\cdot x^n+\eta)(x^m\cdot x^n+1)\right]d\mu_0.
\]
Fix \(\gamma>0\), set \(Q=B(\gamma I_M+B)^{-1}\), and fix a step size satisfying
\[
0<\alpha<\frac{2}{\lambda_{\max}(Q)+\lambda_{\min}(Q)}.
\]
Also fix a finite integer \(K\geq0\) and \(R>C_y\).

For each integer \(N\geq1\), draw \(\theta_0^i=(c_0^i,w_0^i,\eta_0^i)\) independently from \(\mu_0\), and put \(\gamma^N=\gamma/N^{2\beta-1}\). Starting at \(\theta_0\), attempt the following updates for \(k=0,\ldots,K-1\): solve
\[
(\gamma^N I_{N(d+2)}+\nabla^2L^N(\theta_k))z_k^N=-\nabla L^N(\theta_k)
\]
and set \(\theta_{k+1}=\theta_k+\alpha z_k^N\). If a system does not have a unique solution, declare the procedure unsuccessful and stop. For \(K=0\), the procedure is successful without performing an update.

## Task

Prove that there exist positive constants \(C_0=C_0(\sigma,\mu_0)\), \(C_\gamma\), and \(C\), independent of \(N\) and \(\delta\), with the following property. The constants \(C_\gamma\) and \(C\) may depend on the fixed parameters \(\alpha,\gamma,\sigma,\mu_0,d,M,(x^m,y^m)_{m=1}^M,C_x,C_y,R,K\).

For every \(\delta\in(0,1/2]\) and every integer \(N\geq1\) satisfying
\[
N^{2\beta-1}\geq\frac{C_0}{(R-C_y)^2\delta},
\qquad
\gamma\geq\frac{C_\gamma}{N^{1-\beta}},
\]
with probability at least \(1-2\delta\), the procedure is successful and its final output satisfies
\[
\|f_{\theta_K}^N(x)-y\|_2
\leq \frac{C\sqrt M}{\delta}
\left(N^{-(\beta-1/2)}+N^{-(1-\beta)}+\frac{\log M}{\sqrt N}\right)
+(1-\alpha\lambda_{\min}(Q))^K\|y\|_2.
\]
