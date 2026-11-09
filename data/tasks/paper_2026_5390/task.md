# Problem

## Setup

Let \(m,n\) be positive integers and let \(f:\mathbb R^{m\times n}\to\mathbb R\) be differentiable. Let \(W_\star\) be a global minimizer such that \(f(W_\star)=f_\star\) and \(\nabla f(W_\star)=0\). Set \(r=\min\{m,n\}\). Fix finite constants \(L>0\), \(D>0\), and \(\sigma\ge0\), deterministic parameters \(0\le\beta,\mu<1\) and \(\eta>0\), an integer batch size \(B\ge1\), and a fixed deterministic initial matrix \(X_0=Z_0\).

The notation \(\nabla f(A;\xi)\) denotes the matrix-valued stochastic-gradient oracle evaluated at \(A\) with sample \(\xi\); assume this oracle is jointly measurable. For \(t\ge0\), define
\[
Y_t=\beta X_t+(1-\beta)Z_t,
\qquad
G_t=\frac1B\sum_{i=1}^B\nabla f(Y_t;\xi_{t,i}),
\]
\[
M_0=G_0,\qquad M_t=\mu M_{t-1}+(1-\mu)G_t\quad(t\ge1),
\]
\[
P_t=\operatorname{polar}(M_t),\qquad
Z_{t+1}=Z_t-\eta P_t,\qquad
X_{t+1}=\frac{t}{t+1}X_t+\frac1{t+1}Z_{t+1}.
\]
If \(M=U\Sigma V^\top\) is the compact SVD retaining exactly the positive singular values, define \(\operatorname{polar}(M)=UV^\top\); set \(\operatorname{polar}(0)=0\). Norms \(\|\cdot\|_F\) and \(\|\cdot\|_*\) denote the Frobenius and nuclear norms.

All batches are defined on a common probability space. Let
\[
\mathcal F_t=\sigma(\xi_{s,i}:0\le s<t,\ 1\le i\le B)
\]
be the history before the batch at time \(t\). In particular, \(X_t,Z_t,Y_t\) and, for \(t\ge1\), \(M_{t-1}\) are \(\mathcal F_t\)-measurable. Assume, almost surely for every \(t\ge0\),
\[
\mathbb E[G_t\mid\mathcal F_t]=\nabla f(Y_t),
\qquad
\mathbb E[\|G_t-\nabla f(Y_t)\|_F^2\mid\mathcal F_t]\le\frac{\sigma^2}{B}.
\]
Assume that \(f\) is Frobenius-smooth:
\[
\|\nabla f(A)-\nabla f(C)\|_F\le L\|A-C\|_F
\quad\text{for all }A,C\in\mathbb R^{m\times n}.
\]
Assume also that
\[
\|W_\star\|_F\le D/2,
\qquad \|Z_t\|_F\le D/2\quad\text{almost surely for all }t\ge0.
\]
Define \(\Delta=f(Y_0)-f_\star\).

## Task

Prove that, for every integer \(T\ge1\),
\[
\begin{aligned}
 \frac1T\sum_{t=0}^{T-1}\mathbb E\|\nabla f(Y_t)\|_*
 \le{}& \frac{\Delta+2LD^2(\log(eT)+\pi^2/6)}{(1-\beta)T\eta}
 +\frac{Lr\eta}{2(1-\beta)}
 +\frac{2\mu Lr\eta}{(1-\beta)(1-\mu)}\\
 &+\frac{2\sqrt rLD\log(eT)}{(1-\beta)T}
 \left(1+\frac{2\mu}{1-\mu}\right)
 +\frac{2\sqrt r\sigma}{(1-\beta)\sqrt B}
 \sqrt{\frac{1-\mu}{1+\mu}}\\
 &+\frac{2\sqrt r\sigma}{(1-\beta)(1-\mu)T\sqrt B}.
\end{aligned}
\]

For the rate assertions, keep \(f,W_\star,X_0,m,n,L,D,\sigma,B\) and \(\beta\) fixed as \(T\) varies. Each horizon uses a separate run, with parameters \(\mu_T,\eta_T\) constant throughout that run and chosen independently of the realized batches. The assertions concern runs satisfying the preceding oracle and bounded-iterate assumptions with these same constants for all horizons.

Deduce that, for fixed \(\beta\in[0,1)\), there are such horizon-dependent choices \(\mu_T\in[0,1)\) and \(\eta_T>0\) for which the left-hand side is \(O((\log T/T)^{1/4})\) when \(\sigma>0\), and \(O(\sqrt{\log T/T})\) when \(\sigma=0\). Show further that when \(\beta=0\), the corresponding rates improve to \(O(T^{-1/4})\) and \(O(T^{-1/2})\), respectively. The constants in these asymptotic bounds may depend on the fixed problem data and constants, but not on \(T\).
