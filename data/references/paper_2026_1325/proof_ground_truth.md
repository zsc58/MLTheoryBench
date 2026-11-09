# Reference Proof

## Proof Structure

Let \(A=I-W\) and \(A_q=I-W_q=A-\Delta W\). Bound the strong-monotonicity margin and norm of \(A_q\), verify that the locally Lipschitz full-domain monotone map \(G\) is maximal monotone and hence has a firmly nonexpansive resolvent, and apply the standard forward-backward contraction estimate to the quantized inclusion. Finally differentiate the equilibrium equation at a parameter point where the displayed derivatives exist. The chain rule determines a compatible Clarke generalized-Jacobian selection for the backward inclusion; its positive-semidefinite symmetric part gives the same contraction certificate columnwise.

## Complete Proof

Let

\[
A=I-W,\qquad A_q=I-W_q=A-\Delta W,
\]

and define

\[
m_q:=\lambda_{\min}(\operatorname{sym}(A_q)),\qquad L_q:=\|A_q\|_2.
\]

Since \(F\) is \(m\)-strongly monotone, for every \(d\in\mathbb R^n\),

\[
\langle Ad,d\rangle\ge m\|d\|_2^2.
\]

Therefore

\[
\begin{aligned}
\langle A_qd,d\rangle
&=\langle Ad,d\rangle-\langle\Delta Wd,d\rangle\\
&\ge (m-\|\Delta W\|_2)\|d\|_2^2\\
&\ge (m-\epsilon)\|d\|_2^2.
\end{aligned}
\]

Thus

\[
m_q\ge m-\epsilon.
\]

If \(\epsilon<m\), then \(m_q\ge m-\epsilon>0\). Also, strong monotonicity and Cauchy--Schwarz imply \(m\le L\), so \(\epsilon<m\) gives \(\epsilon<L\). The triangle and reverse-triangle inequalities yield

\[
L-\epsilon\le L-\|\Delta W\|_2\le L_q\le L+\|\Delta W\|_2\le L+\epsilon.
\]

Because \(L-\epsilon>0\), this is precisely

\[
|L-\epsilon|\le L_q\le L+\epsilon.
\]

We next verify the resolvent property needed below. Since \(G\) is locally Lipschitz, it is continuous. To prove maximality, suppose that \((u,v)\) is monotonically related to the graph of \(G\), so

\[
\langle u-z,v-G(z)\rangle\ge0\qquad\text{for every }z\in\mathbb R^n.
\]

For any \(h\in\mathbb R^n\) and \(t>0\), apply this inequality first with \(z=u+th\) and then with \(z=u-th\). After division by \(t\) and letting \(t\downarrow0\), continuity gives

\[
\langle h,v-G(u)\rangle\le0
\quad\text{and}\quad
\langle h,v-G(u)\rangle\ge0.
\]

Thus \(v=G(u)\), proving that \(G\) is maximal monotone. The standard resolvent theorem for maximal monotone operators now gives that \(J_{\alpha G}\) is everywhere defined and single-valued. Moreover, if \(a=J_{\alpha G}(s)\) and \(b=J_{\alpha G}(t)\), then

\[
s-a\in\alpha G(a),\qquad t-b\in\alpha G(b).
\]

Monotonicity of \(G\) yields

\[
\langle a-b,(s-a)-(t-b)\rangle\ge0,
\]

or equivalently

\[
\|a-b\|_2^2\le\langle a-b,s-t\rangle.
\]

Hence \(J_{\alpha G}\) is firmly nonexpansive.

The quantized equilibrium equation is

\[
0\in F_q(z)+G(z),
\]

which is equivalent, by the resolvent relation, to \(z=\Phi_q(z)\). By the definitions of \(m_q\) and \(L_q\), \(F_q\) is \(m_q\)-strongly monotone and \(L_q\)-Lipschitz. Therefore, for all \(z,y\), firm nonexpansiveness gives

\[
\begin{aligned}
\|\Phi_q(z)-\Phi_q(y)\|_2^2
&\le \|(z-y)-\alpha(F_q(z)-F_q(y))\|_2^2\\
&\le \bigl(1-2\alpha m_q+\alpha^2L_q^2\bigr)\|z-y\|_2^2.
\end{aligned}
\]

Hence, if

\[
0<\alpha<\frac{2m_q}{L_q^2},
\]

then

\[
\rho:=\sqrt{1-2\alpha m_q+\alpha^2L_q^2}<1,
\]

so \(\Phi_q\) is a contraction with modulus \(\rho\). Its unique fixed point is the unique solution \(z_q^*\) of the quantized equilibrium inclusion, and the forward iteration converges to \(z_q^*\) linearly with rate at most \(\rho\).

Now work at a parameter point at which \(W_q(\theta)\) and \(z_q^*(\theta)\) are differentiable. Let \(p=D_\theta z_q^*\) and

\[
r=(D_\theta W_q)z_q^*+(D_\theta U)x+D_\theta b.
\]

Let \(G_b\in\partial_CG(z_q^*)\) be a Clarke generalized-Jacobian matrix selected compatibly with the columnwise chain rule, namely

\[
D_\theta\bigl[G(z_q^*(\theta))\bigr]=G_bp.
\]

Differentiating

\[
(I-W_q)z_q^*-(Ux+b)+G(z_q^*)=0
\]

columnwise gives

\[
0=(I-W_q)p-r+G_bp.
\]

Thus \(p\) is a solution of the stated backward inclusion. On the matrix space equipped with the Frobenius norm, the affine map

\[
P\longmapsto (I-W_q)P-r
\]

is \(m_q\)-strongly monotone and \(L_q\)-Lipschitz, columnwise. Because \(\operatorname{sym}(G_b)\succeq0\), the linear map \(P\mapsto G_bP\) is monotone. It is continuous and full-domain, so the same maximality argument above applies; consequently, its resolvent is everywhere defined, acts columnwise, and is firmly nonexpansive. Applying the same forward-backward estimate therefore gives

\[
\|\Psi_{q,b}(P)-\Psi_{q,b}(Q)\|_F\le\rho\|P-Q\|_F.
\]

Consequently \(\Psi_{q,b}\) has a unique fixed point, that fixed point is \(p\), and \(P_{k+1}=\Psi_{q,b}(P_k)\) converges linearly to \(p\) with the same stepsize condition and contraction modulus \(\rho\).
