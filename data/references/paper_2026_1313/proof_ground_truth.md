# Reference Proof

## Proof Structure

Write the base density as a probability measure \(P\), factor the mixture as a likelihood ratio depending only on \(F\), and identify that likelihood ratio with the Radon--Nikodym derivative of the induced law of \(F\). Then prove directly, by conditional Jensen's inequality, that no other density with that same induced law can have smaller KL divergence from \(P\).

## Complete Proof

Let
\[
P(dx)=\pi(x)\,d\mu(x),\qquad Q(dx)=p_q(x)\,d\mu(x),
\]
and write \(P_F=F_\#P\) and \(\nu=F_\#Q\). Define the nonnegative measurable function
\[
G(t)=\int_\Lambda q(\lambda)
\frac{\exp\{\sum_{i=1}^m\lambda_i t_i\}}{Z(\lambda)}\,d\rho(\lambda),
\qquad t\in\mathbb R^m.
\]
The integrand is jointly measurable and nonnegative. Tonelli's theorem and the definition of the conditional density give, for \(\mu\)-almost every \(x\),
\[
\begin{aligned}
p_q(x)
&=\int_\Lambda q(\lambda)
\frac{\pi(x)\exp\{\sum_i\lambda_i f_i(x)\}}{Z(\lambda)}\,d\rho(\lambda)\\
&=\pi(x)G(F(x)).
\end{aligned}
\]
Since \(Q\) is normalized,
\[
1=\int_{\mathcal X}G(F(x))\,dP(x)=\int_{\mathbb R^m}G(t)\,dP_F(t).
\]
Thus \(G\) is finite \(P_F\)-almost everywhere. Replacing it by \(0\) on its measurable infinite-value set, if necessary, gives a finite nonnegative measurable function \(g\) with
\[
p_q(x)=\pi(x)g(F(x))\quad\text{for \(\mu\)-almost every }x.
\]

For every Borel set \(B\subseteq\mathbb R^m\), this factorization gives
\[
\begin{aligned}
\nu(B)
&=Q(F^{-1}(B))\\
&=\int_{F^{-1}(B)}g(F(x))\,dP(x)\\
&=\int_B g(t)\,dP_F(t).
\end{aligned}
\]
Hence \(\nu\ll P_F\) and
\[
\frac{d\nu}{dP_F}=g\qquad P_F\text{-almost everywhere}.
\]

It remains to prove the maximum-relative-entropy assertion. Let \(R\) be any probability measure having a \(\mu\)-density \(r\) and satisfying \(F_\#R=\nu\). If \(R\not\ll P\), then \(D_{\mathrm{KL}}(R\|P)=+\infty\), so it cannot improve on \(Q\). Suppose instead that \(R\ll P\), and set \(u=dR/dP\). Let
\[
a=\mathbb E_P[u\mid\sigma(F)].
\]
Because \(F_\#R=\nu\), the defining property of conditional expectation and the preceding Radon--Nikodym identity imply
\[
a(x)=g(F(x))\qquad P\text{-almost everywhere}.
\]
The function \(s\mapsto s\log s\), with \(0\log 0=0\), is convex. Conditional Jensen's inequality therefore yields
\[
\begin{aligned}
D_{\mathrm{KL}}(R\|P)
&=\int u\log u\,dP\\
&\geq \int a\log a\,dP\\
&=\int g(F(x))\log g(F(x))\,dP(x)\\
&=\int g(t)\log g(t)\,dP_F(t).
\end{aligned}
\]
On the other hand, \(dQ/dP=g(F)\), so
\[
D_{\mathrm{KL}}(Q\|P)
=\int g(t)\log g(t)\,dP_F(t).
\]
Consequently,
\[
D_{\mathrm{KL}}(R\|P)\geq D_{\mathrm{KL}}(Q\|P)
\]
for every normalized \(\mu\)-density \(r\) whose pushforward law under \(F\) is \(\nu=F_\#Q\). This remains valid when the common lower bound is \(+\infty\). Thus \(p_q\) minimizes KL divergence to \(\pi\), equivalently maximizes relative entropy to \(\pi\), subject to fixing the complete marginal law \(F_\#p_q\).
