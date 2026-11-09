# Reference Proof

## Proof Structure

First verify that the expected performance trajectory is finite at every time using initial integrability and the pathwise chain rule. Then identify its derivative using integrability and Fubini's theorem. Next dominate its squared derivative by the expected Jacobian-velocity energy. The one-dimensional Wirtinger-Poincare inequality then gives the general volatility bound. Finally, decompose the velocity into its subspace and residual components and bound the resulting Jacobian energy.

## Complete Proof

Set
\[
H_t=\nabla G(X_t)^\top \dot X_t.
\]
Assumption (B) states that, on almost every sample path, for every \(0\le s<t\le T\),
\[
G(X_t)-G(X_s)=\int_s^t H_u\,du,
\]
and that \(\mathbb E\int_0^T |H_u|\,du<\infty\). In particular, for every \(t\in[0,T]\),
\[
|G(X_t)|\le |G(X_0)|+\int_0^T|H_u|\,du
\]
almost surely. Initial integrability therefore gives
\[
\mathbb E|G(X_t)|
\le \mathbb E|G(X_0)|+\mathbb E\int_0^T|H_u|\,du<\infty.
\]
Thus every \(R(t)\) is a finite real number, and subtraction of expectations is legitimate. Taking expectations in the pathwise identity and applying Fubini's theorem gives
\[
R(t)-R(s)=\int_s^t \mathbb E[H_u]\,du.
\]
Moreover, \(\int_0^T|\mathbb E[H_u]|\,du\le\mathbb E\int_0^T|H_u|\,du<\infty\). Consequently, \(R\) is absolutely continuous and
\[
R'(t)=\mathbb E[H_t]
\]
for almost every \(t\).

By assumption (C),
\[
|H_t|\le \gamma\|J(X_t)\dot X_t\|
\]
almost surely for almost every \(t\). Moreover, the right-hand side has finite integrated second moment. Tonelli's theorem gives
\[
\int_0^T\mathbb E|H_t|^2dt
\le\gamma^2\int_0^T\mathbb E\|J(X_t)\dot X_t\|^2dt<\infty.
\]
Thus, for almost every \(t\), Jensen's inequality and (C) yield
\[
|R'(t)|^2
 =|\mathbb E[H_t]|^2
 \le \mathbb E[|H_t|^2]
 \le \gamma^2\mathbb E\|J(X_t)\dot X_t\|^2.
\]
After integration,
\[
\int_0^T |R'(t)|^2dt
\le \gamma^2\int_0^T\mathbb E\|J(X_t)\dot X_t\|^2dt<\infty.
\]
Absolute continuity on the compact interval implies that \(R\) is bounded and belongs to \(L^2(0,T)\). Hence \(R\in H^1(0,T)\). Let
\[
\overline R=\frac1T\int_0^T R(t)\,dt.
\]
The standard one-dimensional mean-zero Wirtinger-Poincare inequality states that, for every \(q\in H^1(0,T)\) with \(\int_0^Tq(t)dt=0\),
\[
\int_0^T q(t)^2dt\le\frac{T^2}{\pi^2}\int_0^T|q'(t)|^2dt.
\]
The function \(q=R-\overline R\) satisfies both hypotheses, so
\[
\int_0^T (R(t)-\overline R)^2dt
\le \frac{T^2}{\pi^2}\int_0^T |R'(t)|^2dt.
\]
Since \(U\) is uniform on \([0,T]\),
\[
\operatorname{Var}(R(U))
=\frac1T\int_0^T(R(t)-\overline R)^2dt.
\]
Combining the preceding estimates proves
\[
\operatorname{Var}(R(U))
\le \frac{\gamma^2T}{\pi^2}
\int_0^T\mathbb E\|J(X_t)\dot X_t\|^2dt.
\]

Now suppose \(\dot X_t=Sb_t+\varepsilon_t\). At almost every time on almost every sample path,
\[
\begin{aligned}
\|J(X_t)\dot X_t\|^2
&=\|J(X_t)Sb_t+J(X_t)\varepsilon_t\|^2\\
&\le 2\|J(X_t)Sb_t\|^2
   +2\|J(X_t)\varepsilon_t\|^2\\
&\le 2\|J(X_t)S\|_F^2\|b_t\|^2
   +2\|J(X_t)\varepsilon_t\|^2.
\end{aligned}
\]
The first inequality is the squared-sum bound, and the second follows from the matrix-vector Frobenius-norm inequality. Taking expectations and integrating nonnegative quantities over time gives
\[
\int_0^T\mathbb E\|J(X_t)\dot X_t\|^2dt
\le 2(E_S+E_\varepsilon).
\]
Substitution into the general bound proves
\[
\operatorname{Var}(R(U))
\le \frac{2\gamma^2T}{\pi^2}(E_S+E_\varepsilon),
\]
as required. These integrations and comparisons are valid in the extended-real sense; if either structured energy is infinite, the conclusion is immediate because the general bound already gives finite volatility. The orthogonality condition \(S^\top\varepsilon_t=0\) specifies the stated subspace-residual decomposition, although the upper-bound estimate itself only needs the displayed decomposition. In particular, the decomposition and orthogonality give \(b_t=S^\top\dot X_t\) and \(\varepsilon_t=(I-SS^\top)\dot X_t\) almost everywhere, so measurable versions can be used throughout. No division by either energy or by a component of the velocity occurs, and zero-energy cases require no exception.
