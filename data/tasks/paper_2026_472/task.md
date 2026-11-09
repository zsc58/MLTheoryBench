# Problem

## Setup

Let \(D=\{1,\ldots,p\}\) be a finite feature index set and let \(X=(X_i)_{i\in D}\) have distribution \(P\) on a product measurable space. Let \(R\) be a measurable region with \(P(X\in R)>0\), and write
\[
Q=P(\,\cdot\mid X\in R)
\]
for the regional distribution. Let \(F\) be a measurable real-valued prediction function, and assume all expectations below are finite.

For \(S\subseteq D\), write \(-S=D\setminus S\), and let \(Q_{-S}\) be the \(X_{-S}\)-marginal of \(Q\). For every \(x_S\) under consideration, assume that a version of the conditional distribution satisfies
\[
Q_{-S\mid S=x_S}\ll Q_{-S},
\qquad
w_{x_S}=\frac{dQ_{-S\mid S=x_S}}{dQ_{-S}}.
\]
Define the conditional- and marginal-masking evaluations by
\[
 m_{\mathrm c}(x,S)=\mathbb E_{Q_{-S\mid S=x_S}}[F(x_S,X_{-S})],
 \qquad
 m_{\mathrm m}(x,S)=\mathbb E_{Q_{-S}}[F(x_S,X_{-S})].
\]
Define the density-ratio discrepancy
\[
\delta(x,S)=\mathbb E_{Q_{-S}}
\left[(w_{x_S}(X_{-S})-1)F(x_S,X_{-S})\right].
\]

Fix an input \(x^0\). The two local value functions are
\[
v_{\mathrm c}(S)=m_{\mathrm c}(x^0,S),
\qquad
v_{\mathrm m}(S)=m_{\mathrm m}(x^0,S).
\]

For a set function \(v:2^D\to\mathbb R\), choose the same attribution operator \(I\) for both value functions from one of the following three forms, for every \(i\in D\):
\[
\begin{aligned}
I_{\mathrm{pure}}(v)_i
  &=v(\{i\})-v(\varnothing),\\
I_{\mathrm{weighted}}(v)_i
  &=\sum_{S\subseteq D\setminus\{i\}}
    \frac{|S|!(p-|S|-1)!}{p!}
    \bigl(v(S\cup\{i\})-v(S)\bigr),\\
I_{\mathrm{full}}(v)_i
  &=v(D)-v(D\setminus\{i\}).
\end{aligned}
\]
Let
\[
\phi_{\mathrm c}=I(v_{\mathrm c}),
\qquad
\phi_{\mathrm m}=I(v_{\mathrm m}),
\qquad
d(S)=\delta(x^0,S).
\]

## Task

Prove the integrated regional-disagreement identity
\[
\boxed{\phi_{\mathrm c}-\phi_{\mathrm m}=I(d)}.
\]
