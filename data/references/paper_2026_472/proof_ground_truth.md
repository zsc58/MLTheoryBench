# Reference Proof

## Proof Structure

First use the Radon–Nikodym derivative to express each conditionally masked evaluation as a weighted marginally masked evaluation. Subtracting the unweighted marginal evaluation gives the discrepancy set function. Finally, use the linearity of the selected attribution operator to propagate this equality to the attribution vectors.

## Complete Proof

Fix a coalition \(S\subseteq D\) and a value \(x_S\) under consideration. Absolute continuity and the defining property of the Radon–Nikodym derivative give
\[
\begin{aligned}
m_{\mathrm c}(x,S)
&=\int F(x_S,z_{-S})\,Q_{-S\mid S=x_S}(dz_{-S})\\
&=\int F(x_S,z_{-S})w_{x_S}(z_{-S})\,Q_{-S}(dz_{-S}).
\end{aligned}
\]
All integrals are well defined by the assumptions. Since
\[
m_{\mathrm m}(x,S)=\int F(x_S,z_{-S})\,Q_{-S}(dz_{-S}),
\]
subtraction yields
\[
\begin{aligned}
m_{\mathrm c}(x,S)-m_{\mathrm m}(x,S)
&=\int \bigl(w_{x_S}(z_{-S})-1\bigr)F(x_S,z_{-S})\,Q_{-S}(dz_{-S})\\
&=\delta(x,S).
\end{aligned}
\]
Evaluating this identity at the fixed input \(x^0\), for every \(S\subseteq D\), gives
\[
v_{\mathrm c}(S)-v_{\mathrm m}(S)=\delta(x^0,S)=d(S).
\]
Thus \(v_{\mathrm c}-v_{\mathrm m}=d\) as set functions.

It remains to pass this equality through \(I\). Each allowed operator is linear in its set-function argument. Indeed, the pure-effect and full-effect formulas are differences of two evaluations, while the weighted marginal-effect formula is a finite weighted sum of such differences. Consequently,
\[
I(v_{\mathrm c})-I(v_{\mathrm m})=I(v_{\mathrm c}-v_{\mathrm m}).
\]
Using \(v_{\mathrm c}-v_{\mathrm m}=d\) and the definitions of the attribution vectors, we conclude
\[
\phi_{\mathrm c}-\phi_{\mathrm m}=I(d),
\]
as required.
