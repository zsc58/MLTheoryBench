# Reference Proof

## Proof Obligations

1. Establish the scalar score-error equation, including times on the target level set, and solve it for every nonnegative time.
2. Use continuity to identify every omega-limit point, without assuming that such a point exists.
3. Under the eventual gradient lower bound, derive an integrable velocity bound, prove convergence in the Euclidean output space, and establish boundary membership, uniqueness of the limit of the given trajectory, and the stated distance estimate.

## Complete Proof

The calibration index satisfies \(1\le k\le n\), so the real-valued calibration scores define a finite threshold \(\tau_\alpha\). Throughout the proof the input, score, and threshold are fixed.

Let
\[
\varepsilon(t)=S(x,y(t))-\tau_\alpha.
\]
On every compact time interval, the trajectory is absolutely continuous and the score is continuously differentiable. The chain rule for a continuously differentiable function composed with an absolutely continuous curve therefore shows that \(\varepsilon\) is absolutely continuous on that interval and
\[
\varepsilon'(t)=\nabla_yS(x,y(t))^\top y'(t)
\]
for almost every \(t\).

At times where the ODE holds and \(\varepsilon(t)\ne0\), the nonvanishing gradient assumption and the prescribed velocity give
\[
\varepsilon'(t)
=-\lambda\varepsilon(t)
\frac{\|\nabla_yS(x,y(t))\|_2^2}{\|\nabla_yS(x,y(t))\|_2^2}
=-\lambda\varepsilon(t).
\]
At times where the ODE holds and \(\varepsilon(t)=0\), the velocity is zero, so the same equality holds without dividing by the gradient norm. Consequently
\[
\varepsilon'(t)=-\lambda\varepsilon(t)
\]
almost everywhere on every compact time interval. The locally absolutely continuous function \(e^{\lambda t}\varepsilon(t)\) has derivative zero almost everywhere and hence is constant. Thus, for every \(t\ge0\),
\[
\varepsilon(t)=\varepsilon(0)e^{-\lambda t}.
\]
Since \(\lambda>0\), this proves \(S(x,y(t))\to\tau_\alpha\). In particular, if \(\varepsilon(0)=0\), then the trajectory stays on the level set; its velocity is zero almost everywhere, and local absolute continuity makes it constant.

If \(z\) is an omega-limit point, choose \(t_j\to\infty\) with \(y(t_j)\to z\). Continuity of \(S(x,\cdot)\) gives
\[
S(x,z)=\lim_{j\to\infty}S(x,y(t_j))=\tau_\alpha.
\]
Therefore \(z\in B_\alpha(x)\). This argument does not assert existence of an omega-limit point without the additional hypothesis.

Now assume there are \(T\in[0,\infty)\) and \(m>0\) such that
\[
\|\nabla_yS(x,y(t))\|_2\ge m\qquad(t\ge T).
\]
For almost every \(t\ge T\), the velocity formula, including its zero value on the level set, yields
\[
\|y'(t)\|_2
=\lambda\frac{|\varepsilon(t)|}{\|\nabla_yS(x,y(t))\|_2}
\le\frac{\lambda}{m}|\varepsilon(0)|e^{-\lambda t}.
\]
The right-hand side is integrable on \([T,\infty)\). For any \(u>t\ge T\), absolute continuity on \([t,u]\) gives
\[
\begin{aligned}
\|y(u)-y(t)\|_2
&\le\int_t^u\|y'(s)\|_2\,ds\\
&\le\frac{|\varepsilon(0)|}{m}\bigl(e^{-\lambda t}-e^{-\lambda u}\bigr)\\
&\le\frac{|\varepsilon(0)|}{m}e^{-\lambda t}.
\end{aligned}
\]
This bound tends to zero as \(t\to\infty\), uniformly in \(u>t\). Hence the trajectory is Cauchy at infinity. To make the convergence step explicit, the sequence \(y(T+j)\) is Cauchy in the complete space \(\mathbb R^d\), so it converges to some \(y_\infty\). The same Cauchy bound then shows that the whole trajectory converges to \(y_\infty\).

The point \(y_\infty\) is an omega-limit point, so \(y_\infty\in B_\alpha(x)\). Letting \(u\to\infty\) in the preceding estimate gives, for every \(t\ge T\),
\[
\|y(t)-y_\infty\|_2
\le\frac{|S(x,y_0)-\tau_\alpha|}{m}e^{-\lambda t}.
\]
A trajectory cannot converge to two distinct points in \(\mathbb R^d\), so its limit is unique. This does not assert that the level set has only one point or that different trajectories have the same limit.

## Dependency Closure

The only independent background used is the continuously differentiable/absolutely continuous chain rule, the fundamental theorem for absolutely continuous functions, elementary exponential integration, and completeness of Euclidean space, as indexed by theory_009. Their hypotheses are verified above. The velocity is part of the public definition, so no additional optimization or flow-existence theorem is needed. All theorem-critical obligations are closed.
