# Problem

## Setup

Let \(q\) be an odd prime, let \(\zeta=e^{2\pi i/q}\), and identify \(\mathbb Z_q\) with the field of residues modulo \(q\). Fix integers \(2\le d<q\) and \(m\ge1\).

For arbitrary coordinate maps \(\phi,\psi:\mathbb Z_q\to\mathbb C\), parameters \(U\in\mathbb C^{2\times m}\), and \(c\in\mathbb C^m\), define
\[
 F(x_1,x_2)=\sum_{j=1}^m c_j(U_{1j}x_1+U_{2j}x_2)^d
\]
and its output matrix \(M\in\mathbb C^{q\times q}\) by
\[
 M_{ab}=F(\phi(a),\psi(b)).
\]
For a function \(f:\mathbb Z_q^2\to\mathbb Z_q\), define its encoded target matrix by
\[
 K_f(a,b)=\zeta^{f(a,b)}.
\]
Call \(f\) representable if there exist \(\phi,\psi,U,c\) for which \(M=K_f\). Write \(\|\cdot\|_F\) for the Frobenius norm.

## Task

Prove the following theorem.

1. Every output matrix \(M\) has rank at most \(d+1\), regardless of \(m\) and of the coordinate maps. The bilinear target \(f_\times(a,b)=ab\) has rank \(q\), with all singular values equal to \(\sqrt q\). Consequently, if \(d<q-1\), it is not representable, and every network output satisfies
\[
 \frac{\|K_{f_\times}-M\|_F^2}{\|K_{f_\times}\|_F^2}
 \ge 1-\frac{d+1}{q}.
\]
Moreover, this value is the exact normalized residual of the best rank-at-most-\((d+1)\) approximation to \(K_{f_\times}\).

2. If \(m\ge d+1\), then suitable coordinate maps and parameters represent every linear phase
\[
 f(a,b)=ua+vb\qquad (u,v\in\mathbb Z_q)
\]
and each of
\[
 f(a,b)=a^2+b,\qquad f(a,b)=a+b^2,\qquad f(a,b)=a^2+b^2,
\]
where all expressions are evaluated modulo \(q\).
