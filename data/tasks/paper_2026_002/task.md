# Problem

## Setup

Fix \(T>0\). Let \((X_t)_{t\in[0,T]}\) be an \(\mathbb R^d\)-valued random process. Let \(F:\mathbb R^d\to\mathbb R\) be a frozen scalar predictor, with row Jacobian
\[
J(x)=\nabla F(x)^\top,
\]
and let \(G:\mathbb R^d\to\mathbb R\) be a scalar performance field. Assume
\[
\mathbb E|G(X_0)|<\infty.
\]
Define the deterministic trajectory
\[
R(t)=\mathbb E[G(X_t)].
\]
For \(U\sim\operatorname{Unif}[0,T]\), define its temporal volatility as
\[
\operatorname{Var}(R(U))
=\mathbb E[(R(U)-\mathbb E[R(U)])^2].
\]

Assume:

- **(A)** Almost surely, \(t\mapsto X_t\) is absolutely continuous, and
  \[
  \mathbb E\int_0^T\|\dot X_t\|^2dt<\infty.
  \]
- **(B)** The field \(G\) is weakly differentiable; almost surely, \(t\mapsto G(X_t)\) is absolutely continuous and, for every \(0\le s<t\le T\),
  \[
  G(X_t)-G(X_s)=\int_s^t\nabla G(X_u)^\top\dot X_u\,du.
  \]
  Moreover,
  \[
  \mathbb E\int_0^T|\nabla G(X_t)^\top\dot X_t|dt<\infty.
  \]
- **(C)** The measurable field \(J\) is well defined at \(X_t\) almost surely for almost every \(t\),
  \[
  \mathbb E\int_0^T\|J(X_t)\dot X_t\|^2dt<\infty,
  \]
  and there is a constant \(\gamma>0\) such that, almost surely for almost every \(t\),
  \[
  |\nabla G(X_t)^\top\dot X_t|
  \le \gamma\|J(X_t)\dot X_t\|.
  \]

For the structured-drift clause below, additionally suppose that, almost surely for almost every \(t\),
\[
\dot X_t=Sb_t+\varepsilon_t,
\]
where \(S\in\mathbb R^{d\times k}\), \(S^\top S=I_k\), \(b_t\in\mathbb R^k\), \(\varepsilon_t\in\mathbb R^d\), and \(S^\top\varepsilon_t=0\). Define
\[
E_S=\int_0^T\mathbb E[\|J(X_t)S\|_F^2\|b_t\|^2]dt,
\qquad
E_\varepsilon=\int_0^T\mathbb E\|J(X_t)\varepsilon_t\|^2dt.
\]
These quantities may take the value \(+\infty\).

## Task

Prove the following integrated theorem:

1. The trajectory \(R\) is absolutely continuous and satisfies
   \[
   \operatorname{Var}(R(U))
   \le \frac{\gamma^2T}{\pi^2}
   \int_0^T\mathbb E\|J(X_t)\dot X_t\|^2dt.
   \]
2. Under the additional structured-drift decomposition,
   \[
   \operatorname{Var}(R(U))
   \le \frac{2\gamma^2T}{\pi^2}(E_S+E_\varepsilon).
   \]
