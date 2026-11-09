# Reference Proof

## Proof Structure

First verify well-definedness and the analytic operations from the explicit finite target-score second moment. Derive the two conditional score representations and hence the common conditional mean of every matrix-weighted estimator. Then remove this common mean from the optimization by the conditional variance identity. Under the joint law of the endpoint variable and the Gaussian variable, compute the required second moments. Finally solve the resulting matrix normal equation and use positive definiteness to prove unique global optimality.

## Complete Proof

Write \(b=1-a\), and set
\[
z=z(x,y):=\frac{x-\sqrt a\,y}{\sqrt b},
\qquad k_x(y):=b^{-d/2}q(z(x,y)).
\]
The density of \(X\) is
\[
m(x)=\int_{\mathbb R^d}k_x(y)p(y)\,dy,
\]
and \(r_x(y)=k_x(y)p(y)/m(x)\). The Gaussian kernel is strictly positive and bounded, so \(0<m(x)<\infty\) for every \(x\). A change of variables in the Gaussian integral shows \(\int m(x)\,dx=1\), and the displayed conditional density integrates to one. The joint density of \((X,Y)\) is \(m(x)r_x(y)=k_x(y)p(y)\).

### Analytic justification and moment finiteness

The explicit assumption and Cauchy–Schwarz give
\[
\int\|\nabla p(y)\|\,dy
=\int\|S_p(y)\|p(y)\,dy
\leq\left(\int\|S_p(y)\|^2p(y)\,dy\right)^{1/2}<\infty.
\]
Choose smooth cutoffs \(\chi_R\) equal to one on the ball of radius \(R\), supported on the ball of radius \(2R\), with \(0\leq\chi_R\leq1\) and \(\|\nabla\chi_R\|\leq C/R\). Such cutoffs are obtained by rescaling one fixed smooth cutoff.

Compactly supported integration by parts gives
\[
\int\chi_R\nabla p=-\int p\nabla\chi_R.
\]
The left side converges to \(\int\nabla p\) by integrability, and the right side has norm at most \(C/R\). Consequently,
\[
\mathbb E[S_p(Y)]=\int\nabla p(y)\,dy=0.
\]
The Gaussian score is \(S_q(z)=-z/\sigma^2\), so it also has mean zero and has second-moment matrix \(F_q=\sigma^{-2}I_d\).

Both \(k_x(y)\) and its first derivatives in \(x\) and \(y\) are bounded uniformly in \((x,y)\), with bounds depending on the fixed parameters. Differentiation under the integral defining \(m\) is therefore justified by domination by a constant times \(p\). It also gives continuity of the derivative. For fixed \(x\), compactly supported integration by parts gives
\[
\int\chi_R p\nabla_y k_x
=-\int\chi_R k_x\nabla p-\int p k_x\nabla\chi_R.
\]
The last term tends to zero, bounded in norm by \((C/R)\|k_x\|_\infty\). The other terms converge absolutely because \(\nabla_y k_x\) and \(k_x\) are bounded, \(p\) is integrable, and \(\nabla p\) is integrable. Hence
\[
\int p(y)\nabla_y k_x(y)\,dy
=-\int k_x(y)\nabla p(y)\,dy.
\]
This establishes exactly the integration-by-parts operation needed below, without a separate boundary assumption.

For every fixed \(x\),
\[
\mathbb E_{r_x}\|T(Y)\|^2
\leq\frac{\|k_x\|_\infty}{a\,m(x)}
\int\|S_p(y)\|^2p(y)\,dy<\infty.
\]
Also \(k_x(y)\|D_x(y)\|^2\) is bounded in \(y\), since it is a fixed constant times \(q(z)\|z\|^2\). Thus \(D_x(Y)\), and consequently \(G_x^A(Y)\), have finite conditional second moments for every \(x\).

Under the joint generative experiment,
\[
D_X(Y)=\frac1{\sqrt b}S_q(Z),\qquad
T(Y)=\frac1{\sqrt a}S_p(Y).
\]
Both are square-integrable. Every fixed matrix combination is therefore jointly square-integrable, so \(J(A)\) is finite.

### Conditional score representations

Differentiating the convolution with respect to \(x\) and dividing by \(m(x)\) gives
\[
\nabla\log m(x)
=\mathbb E_{r_x}\left[\frac1{\sqrt b}S_q(z(x,Y))\right].
\]
Since \(S_q(z)=-z/\sigma^2\),
\[
\frac1{\sqrt b}S_q(z(x,y))
=\frac{\sqrt a\,y-x}{\sigma^2b}=D_x(y),
\]
so
\[
\mathbb E_{r_x}[D_x(Y)]=\nabla\log m(x). \tag{1}
\]

For the second representation, observe that
\[
\nabla_x k_x(y)=-\frac1{\sqrt a}\nabla_y k_x(y).
\]
The integration by parts justified above therefore yields
\[
\begin{aligned}
\nabla m(x)
&=-\frac1{\sqrt a}\int p(y)\nabla_y k_x(y)\,dy\\
&=\frac1{\sqrt a}\int k_x(y)\nabla p(y)\,dy.
\end{aligned}
\]
After division by \(m(x)\),
\[
\mathbb E_{r_x}[T(Y)]
=\mathbb E_{r_x}\left[\frac{S_p(Y)}{\sqrt a}\right]
=\nabla\log m(x). \tag{2}
\]
It follows from (1)-(2) that, for every matrix \(A\),
\[
\mathbb E_{r_x}[G_x^A(Y)]=\nabla\log m(x). \tag{3}
\]
Moreover, conditional Jensen applied to (1) gives
\[
\mathbb E\|\nabla\log m(X)\|^2
\leq\mathbb E\|D_X(Y)\|^2
=\frac{d}{b\sigma^2}<\infty.
\]

### Reduction to endpoint moments

Let expectations without a subscript now be taken under the joint experiment
\[
Y\sim p,\qquad Z\sim q\text{ independently},\qquad
X=\sqrt b\,Z+\sqrt a\,Y.
\]
By (3), square integrability, and the conditional variance formula,
\[
J(A)=\mathbb E\|G_X^A(Y)\|^2
-\mathbb E\|\nabla\log m(X)\|^2. \tag{4}
\]
Both terms are finite. The second term is independent of \(A\), so it remains to minimize the first.

Define
\[
D:=D_X(Y)=\frac1{\sqrt b}S_q(Z),
\qquad T:=T(Y)=\frac1{\sqrt a}S_p(Y),
\qquad Q:=D-T.
\]
The zero score means proved above and independence of \(Y\) and \(Z\) make both cross moments between \(D\) and \(T\) vanish. All entries of these moments are integrable by square integrability. Hence
\[
\mathbb E[TT^\top]=a^{-1}F_p,
\qquad
\mathbb E[DD^\top]=b^{-1}F_q,
\qquad
\mathbb E[TD^\top]=0. \tag{5}
\]
In particular,
\[
\mathbb E[TQ^\top]=-a^{-1}F_p,
\qquad
M:=\mathbb E[QQ^\top]=b^{-1}F_q+a^{-1}F_p. \tag{6}
\]
Because \(F_q=\sigma^{-2}I_d\) and \(F_p\) is positive semidefinite,
\[
M\succeq\frac1{b\sigma^2}I_d\succ0. \tag{7}
\]
Thus \(M\) is invertible; no separate nonsingularity assumption on \(F_p\) is needed.

### Matrix optimization and uniqueness

Since \(G_X^A(Y)=T+AQ\), the function \(\mathbb E\|T+AQ\|^2\) is a finite quadratic polynomial in the entries of \(A\). Its gradient gives the matrix normal equation
\[
0=2\bigl(\mathbb E[TQ^\top]+A\mathbb E[QQ^\top]\bigr)
=2(-a^{-1}F_p+AM).
\]
Its unique solution is
\[
A^*=a^{-1}F_pM^{-1}
=a^{-1}F_p\left(b^{-1}F_q+a^{-1}F_p\right)^{-1}. \tag{8}
\]
The order of these matrix factors follows directly from the normal equation and does not require a commutativity assumption.

For completeness, let \(B=A-A^*\). Equation (8) implies
\(\mathbb E[(T+A^*Q)Q^\top]=0\). Expanding the square therefore gives
\[
\mathbb E\|T+AQ\|^2-
\mathbb E\|T+A^*Q\|^2
=\operatorname{tr}(BMB^\top). \tag{9}
\]
By (7), this quantity is nonnegative and equals zero only when \(B=0\). Combining (4) and (9) proves that \(A^*\) is the unique global minimizer of \(J\).
