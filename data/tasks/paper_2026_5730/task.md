# Problem

## Setup

Fix an integer \(d\ge 1\). Choose one of the following kernel families \((k_r)_{r>0}\), using the same family for every lengthscale and a fixed smoothness parameter \(s>1\) in the Matérn case:
\[
k_r(x,y)=\exp\!\left(-\frac{\|x-y\|^2}{2r^2}\right)
\]
or
\[
k_r(x,y)=\frac{2^{1-s}}{\Gamma(s)}
\left(\frac{\sqrt{2s}\,\|x-y\|}{r}\right)^s
K_s\!\left(\frac{\sqrt{2s}\,\|x-y\|}{r}\right).
\]
Here \(\Gamma\) is the Gamma function and \(K_s\) is the modified Bessel function of the second kind. The Matérn expression at \(x=y\) is defined by continuous extension, so that \(k_r(x,x)=1\). Let \(\mathcal H_r\) be the reproducing kernel Hilbert space associated with \(k_r\).

For probability measures \(P,Q\) on \(\mathbb R^d\), define their witness function and maximum mean discrepancy at lengthscale \(r\) by
\[
f_{r,P,Q}(z)=\int k_r(x,z)\,dP(x)-\int k_r(x,z)\,dQ(x),
\]
\[
\operatorname{MMD}_r(P,Q)
=\left\|\int k_r(x,\cdot)\,dP(x)-\int k_r(x,\cdot)\,dQ(x)\right\|_{\mathcal H_r}.
\]
For a vector field \(G\), write
\(\|G\|_{L_2^d(P)}^2=\int\|G(x)\|^2dP(x)\), and let \(T_\#P\) denote the pushforward of \(P\) by a measurable map \(T\). Let \(\mathcal P_2(\mathbb R^d)\) denote the Borel probability measures \(P\) on \(\mathbb R^d\) satisfying \(\int\|x\|^2dP(x)<\infty\).

Let \(P_0,Q\in\mathcal P_2(\mathbb R^d)\), and define recursively
\[
P_{t+1}=\bigl(\mathrm{Id}-\gamma_t\nabla f_{r_t,P_t,Q}\bigr)_\#P_t.
\]
Assume that, for some constant \(C>0\) independent of \(t\):

- \((\gamma_t)_{t\ge0}\) is nonincreasing, \(0<\gamma_t<1/(2C)\), \(\gamma_t\to0\), and \(\sum_{t=0}^\infty\gamma_t=\infty\);
- \((r_t)_{t\ge0}\) is nonincreasing and \(r_t\to r\) for some \(r>0\);
- for every \(t\),
\[
\left(\frac{r_t}{r}\right)^d
\bigl\|\nabla f_{r,P_t,Q}\bigr\|_{L_2^d(P_t)}^2
\ge C\operatorname{MMD}_r^2(P_t,Q).
\]

## Task

Prove that
\[
\operatorname{MMD}_r^2(P_t,Q)\longrightarrow0
\qquad\text{as }t\to\infty.
\]
