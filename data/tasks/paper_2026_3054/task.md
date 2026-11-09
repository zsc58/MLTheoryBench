# Problem

## Setup

Fix \(T>0\) and an integer \(d\geq1\). Let \(\mu\) be a Borel probability measure on \(\mathbb R^d\) with a Lebesgue density, and let
\[
d\bar X_t=-\bar X_t\,dt+\sqrt2\,dB_t,\qquad \bar X_0\sim\mu.
\]
Write \(p_t\) for its Lebesgue density at \(t>0\). Let \(\gamma^d=N(0,I_d)\), with Lebesgue density
\[
g_d(x)=(2\pi)^{-d/2}e^{-\|x\|^2/2},
\qquad \tilde p_t(x)=p_t(x)/g_d(x).
\]
Assume \(\mathrm{KL}(p_T(x)\,dx\|\gamma^d)<\infty\).

Fix a deterministic, jointly continuous, locally bounded map \(s^\theta:[0,T]\times\mathbb R^d\to\mathbb R^d\). The learned reverse process starts from \(\gamma^d\) and solves
\[
dX_r^\theta=\big[-X_r^\theta+s^\theta(T-r,X_r^\theta)\big]dr+\sqrt2\,dW_r,
\qquad X_0^\theta\sim\gamma^d.
\]
Assume it is nonexplosive and has continuous paths on \([0,T]\), and denote its terminal law by \(\mu_T^\theta\).

Let \(Y_r=\bar X_{T-r}\). Assume this time reversal is a weak solution, on \(0\leq r<T\), of
\[
dY_r=\big[-Y_r+2\nabla\log\tilde p_{T-r}(Y_r)\big]dr+\sqrt2\,d\widehat W_r,
\qquad Y_0\sim p_T(x)\,dx.
\]
Write \(q_r=p_{T-r}\) and \(h_r\) for the Lebesgue densities of \(Y_r\) and \(X_r^\theta\), respectively. Assume these densities are positive and belong to \(C^{1,2}([0,T)\times\mathbb R^d)\), and satisfy the Fokker--Planck equations
\[
\partial_r q_r=\Delta q_r-\nabla\cdot\big(q_r[-x+2\nabla\log\tilde p_{T-r}]\big),
\qquad
\partial_r h_r=\Delta h_r-\nabla\cdot\big(h_r[-x+s^\theta(T-r,x)]\big).
\]
For positive densities \(q,h\), define
\[
I(q\|h)=\int_{\mathbb R^d}\left\|\nabla\log\frac{q(x)}{h(x)}\right\|^2q(x)\,dx.
\]
Assume \(I(q_r\|h_r)<\infty\) for every \(0<r<T\).

For \(0<t\leq T\), define the score error by
\[
\varepsilon_t^\theta(x)^2=\big\|2\nabla\log\tilde p_t(x)-s^\theta(t,x)\big\|^2.
\]
Assume that the two scalar functions
\[
r\longmapsto\mathbb E\big[\varepsilon_{T-r}^\theta(Y_r)^2\big],
\qquad
r\longmapsto\mathbb E\left[\frac{\|s^\theta(T-r,Y_r)\|}{1+\|Y_r\|}\right]
\]
are finite on \((0,T)\) and integrable there. All expectations are with respect to the indicated diffusion laws; no training-sample randomness is included. Values of the score error at \(t=0\) are immaterial to the integrals below.

Assume the one-sided Lipschitz condition
\[
\langle s^\theta(t,x)-s^\theta(t,y),x-y\rangle\le M_t\|x-y\|^2
\]
for every \(x,y\in\mathbb R^d\). In the constant case it holds for \(t\in[0,T]\) with \(M_t\equiv M\in\mathbb R\). In the time-dependent case it holds for \(0<t\leq T\) with \(M_t=1+c/t\), where \(c>1\); no value of \(1+c/t\) is assigned at \(t=0\).

## Task

Prove that
\[
\mathrm{KL}(\mu\,\|\,\mu_T^\theta)\le K_T+\frac12\int_0^T\lambda_T(t)\,\mathbb E\!\left[\varepsilon_t^\theta(\bar X_t)^2\right]dt,
\qquad
K_T=\lambda_T(T)\,\mathrm{KL}(p_T(x)\,dx\|\gamma^d),
\]
where, for \(t\in[0,T]\), when \(M_t\equiv M\),
\[
\lambda_T(t)=\sqrt{\frac{M-e^{-2(M-1)(T-t)}}{M-e^{-2(M-1)T}}}\quad(M>1),
\]
\[
\lambda_T(t)=\sqrt{\frac{1+2(T-t)}{1+2T}}\quad(M=1),
\]
\[
\lambda_T(t)=\sqrt{\frac{e^{2(1-M)(T-t)}-M}{e^{2(1-M)T}-M}}
\le \exp\!\left(-\frac{(1-M)t}{2-M}\right)\quad(M<1).
\]
When \(M_t=1+c/t\) with \(c>1\), prove the same bound instead with
\[
\lambda_T(t)=\sqrt{1-\frac{2t^{2c+1}}{(2c+1)T^{2c}+2T^{2c+1}}},
\qquad 0\leq t\leq T.
\]
