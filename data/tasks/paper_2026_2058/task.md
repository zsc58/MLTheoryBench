# Problem

## Setup

Let \(n,d\) be positive integers and let \(b\) be an integer with \(0\le b<n/2\). A fixed unknown honest set \(H\subseteq\{1,\ldots,n\}\) has size \(h=n-b\). The remaining workers may be Byzantine. Honest worker \(i\) has a differentiable objective \(f_i:\mathbb R^d\to\mathbb R\) of the form \(f_i(x)=\mathbb E[\ell(x,\xi_i)]\). Define
\[
f_H(x)=\frac1h\sum_{i\in H}f_i(x),\qquad
f_H^*=\inf_{x\in\mathbb R^d}f_H(x)>-\infty.
\]
Assume that \(\nabla f_H\) is \(L\)-Lipschitz for a finite \(L>0\). In the PL case, assume for a finite \(\mu>0\) that
\[
\|\nabla f_H(x)\|^2\ge2\mu(f_H(x)-f_H^*)\qquad(x\in\mathbb R^d).
\]
Finite constants \(G,B\ge0\) satisfy
\[
\frac1h\sum_{i\in H}\|\nabla f_i(x)-\nabla f_H(x)\|^2
\le G^2+B^2\|\nabla f_H(x)\|^2\qquad(x\in\mathbb R^d).
\]

Start from a deterministic \(x^0\) and \(m_i^0=0\) for honest workers. Let \(\mathcal F_{t-1}\) denote the history before the fresh oracle calls at round \(t\). Conditional on this history, the honest stochastic gradients are independent across workers and satisfy
\[
\mathbb E[g_i^t\mid\mathcal F_{t-1}]=\nabla f_i(x^{t-1}),\qquad
\mathbb E[\|g_i^t-\nabla f_i(x^{t-1})\|^2\mid\mathcal F_{t-1}]\le\sigma^2
\]
for a finite \(\sigma\ge0\). Byzantine messages may depend measurably on the history and current honest messages, but not on future oracle draws. Expectations below include all algorithmic randomness.

For a finite \(\kappa\ge0\), the server uses a measurable map \(A:(\mathbb R^d)^n\to\mathbb R^d\) satisfying, for every input collection and every subset \(S\) of size \(h\),
\[
\|A(v_1,\ldots,v_n)-\bar v_S\|^2
\le\frac\kappa h\sum_{i\in S}\|v_i-\bar v_S\|^2,
\qquad \bar v_S=\frac1h\sum_{i\in S}v_i.
\]
At each integer round \(t\ge1\), the server broadcasts \(x^{t-1}\). Honest workers form
\[
m_i^t=\beta_t m_i^{t-1}+(1-\beta_t)g_i^t,
\]
while Byzantine workers send arbitrary vectors. The server computes
\[
g^t=A(m_1^t,\ldots,m_n^t),\qquad x^t=x^{t-1}-\gamma_tg^t.
\]
Parameter schedules are deterministic. Setting \(\beta_t=0\) gives the no-momentum variant. All norms are Euclidean, all iteration horizons are positive integers, and \(\lfloor\cdot\rfloor\) is the ordinary floor function.

## Task

Prove the following integrated theorem.

### 1. Average-gradient upper bound

If \(\kappa B^2<1/56\), \(\gamma_t\equiv\gamma\) with \(0<\gamma L\le1/36\), and \(\beta_t=1-36\gamma L\), then for every integer \(T\ge1\),
\[
\frac1T\sum_{t=1}^T\mathbb E\|\nabla f_H(x^{t-1})\|^2
\le
\frac{9\Delta_0}{4(3/8-21\kappa B^2)\gamma T}
+\frac{(162L/h+756\kappa L)\gamma\sigma^2}{3/8-21\kappa B^2}
+\frac{21\kappa G^2}{3/8-21\kappa B^2},
\qquad \Delta_0=f_H(x^0)-f_H^*.
\]

### 2. PL last-iterate upper bound

In the PL case assume \(\kappa B^2<1/56\), and define
\[
\alpha_4=\mu(3/8-21\kappa B^2),\qquad
\alpha_5=(162L/h+756\kappa L)\sigma^2,\qquad
\alpha_6=21\kappa G^2.
\]
For an integer \(T\ge1\), choose
\[
s_0>\max\{2,72L/\alpha_4\},\qquad
\gamma_0=\frac2{\alpha_4s_0}<\min\{1/\alpha_4,1/(36L)\},
\]
and set
\[
\gamma_t=\begin{cases}
\gamma_0,&t<\lfloor T/2\rfloor,\\
\displaystyle\frac2{\alpha_4(s_0+t-\lfloor T/2\rfloor)},&t\ge\lfloor T/2\rfloor,
\end{cases}
\qquad \beta_t=1-36\gamma_tL.
\]
Then
\[
\begin{aligned}
\mathbb E[f_H(x^{T-1})-f_H^*]\le{}&
\frac{2(s_0-1)^2\Delta_0}{T^2}
 e^{-\alpha_4\gamma_0(\lfloor T/2\rfloor-1)}\\
&+\frac{2(\alpha_5\gamma_0+\alpha_6)(s_0-1)^2}{\alpha_4T^2}
+\frac{4\alpha_5}{\alpha_4^2T}+\frac{\alpha_6}{\alpha_4}.
\end{aligned}
\]

### 3. Matching heterogeneity lower bounds

For every finite \(G,B,\kappa\ge0\) with \(\kappa B^2<1\), every \(\mu>0\), and a prescribed initial point \(x^0\in\mathbb R\), there exist one-dimensional two-worker quadratic objectives, with both workers honest, and valid \(\kappa\)-robust aggregators for the two variants, satisfying the setup with exact gradients and \(L=\mu\), such that
\[
\|\nabla f_H(x^{T-1})\|^2\ge c\frac{\kappa G^2}{1-\kappa B^2},\qquad
f_H(x^{T-1})-f_H^*\ge c\frac{\kappa G^2}{\mu(1-\kappa B^2)}
\]
for a universal constant \(c>0\). The instances and aggregators must be fixed independently of \(T\) and of the subsequent choice of schedule parameters. For each fixed choice of the parameters in any of the following families, the inequalities must hold for all sufficiently large integer \(T\):

- **No momentum:** Set \(\beta_t=0\). Choose a fixed \(\delta\in(0,1/4)\) such that
  \(\kappa B^2<(1-4\delta)/(1+2\delta)\). One may use either a fixed constant stepsize \(0<\gamma\le\delta/\mu\), or the horizon-dependent constant stepsize \(\gamma_t=\gamma_0/\sqrt T\) with fixed \(0<\gamma_0\le\delta/\mu\). The required two-phase family is defined by
  \[
  a_N=2\mu\bigl(1/2-2\delta-\kappa B^2(1/2+\delta)\bigr)>0,
  \quad s_N>\max\{2,2\mu/(\delta a_N)\},\quad
  \gamma_0=2/(a_Ns_N),
  \]
  with \(\gamma_t=\gamma_0\) for \(t<\lfloor T/2\rfloor\) and \(\gamma_t=2/[a_N(s_N+t-\lfloor T/2\rfloor)]\) thereafter.

- **Local momentum:** Use either a fixed constant stepsize \(0<\gamma\mu\le1/36\), or \(\gamma_t=\gamma_0/\sqrt T\) with fixed \(0<\gamma_0\mu\le1/36\), and set \(\beta_t=1-36\gamma_t\mu\). These constant and horizon-dependent choices are included throughout \(\kappa B^2<1\). When \(\kappa B^2<1/56\), the lower bounds are also required for the two-phase schedule in item 2 with \(L=\mu\) and fixed \(s_0\).

The constant \(c\) must be independent of \(G,B,\kappa,\mu\), the initialization, the schedule parameters, and the horizon. The threshold for sufficiently large \(T\) may depend on the fixed instance and schedule parameters.
