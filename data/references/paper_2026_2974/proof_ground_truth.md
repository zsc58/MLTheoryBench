# Reference Proof

## Proof Structure
Derive weighted gradient smoothness and finite-horizon integrability, introduce a deterministic predictable proxy, prove its one-step descent bound, telescope the normalized accumulator terms, and bound their terminal logarithms. Choose the offsets coordinatewise, handle zero-noise coordinates directly, close the two-case self-bounding inequality, and convert coordinate energies to the required average gradient norm.

## Complete Proof
Write
\[
a_{t,i}=\nabla_i f(x_t),\qquad \xi_{t,i}=z_{t,i}-a_{t,i},\qquad U_{t,i}=\sum_{s=1}^t a_{s,i}^2.
\]
All auxiliary offsets below are deterministic proof parameters, not algorithm inputs.

### 1. Smoothness and integrability
The stated smoothness condition implies
\[
\|\nabla f(x)-\nabla f(y)\|_{1/\ell}\le\|x-y\|_\ell.
\tag{1}
\]
Here is an elementary derivation. Set \(h(y)=f(\operatorname{diag}(\ell)^{-1/2}y)\). Its Taylor remainder has absolute value at most \(\|y-x\|_2^2/2\). Thus \(F(y)=h(y)+\|y\|_2^2/2\) has nonnegative Taylor remainder, so every tangent plane supports \(F\), and its Taylor remainder is at most \(\|y-x\|_2^2\). For fixed \(x,y\), put \(D=\nabla F(y)-\nabla F(x)\). The function \(\Phi(z)=F(z)-\langle\nabla F(x),z\rangle\) is minimized at \(x\). Its upper Taylor bound at \(y\), evaluated at \(y-D/2\), gives
\[
F(y)-F(x)-\langle\nabla F(x),y-x\rangle\ge\|D\|_2^2/4.
\]
Adding the reverse inequality yields \(\|D\|_2^2\le2\langle D,y-x\rangle\). Since \(D=\nabla h(y)-\nabla h(x)+(y-x)\), expansion gives \(\|\nabla h(y)-\nabla h(x)\|_2\le\|y-x\|_2\), which is (1) after changing coordinates.

The update satisfies \(|x_{t+1,i}-x_{t,i}|\le\eta\). Consequently, (1) gives the deterministic pathwise bound
\[
|a_{t,i}|\le |a_{1,i}|+\eta\sqrt{\ell_i\|\ell\|_1}(t-1).
\tag{2}
\]
The Taylor bound at the fixed point \(x_1\) also bounds \(|f(x_t)-f(x_1)|\) deterministically for every finite horizon. The noise assumption implies \(\mathbb E|\xi_{t,i}|^p\le s_i^p\); together with (2), this gives finite p-moments of \(z_{t,i}\). All objective expectations, coordinate energies, and first moments of square-root accumulators used below are finite. No second noise moment is needed.

### 2. One-step proxy descent
For deterministic offsets with \(c_i>0\) whenever \(s_i>0\), and \(c_i=0\) permitted when \(s_i=0\), define
\[
w_{t,i}=v_{t-1,i}+a_{t,i}^2+c_i^2,\qquad
r_{t,i}=\frac{z_{t,i}^2}{\rho^2+v_{t,i}},\qquad
q=\frac{2}{\bar p}\in(0,1].
\]
The proxy is \(\mathcal F_{t-1}\)-measurable and \(0\le r_{t,i}\le1\). Smoothness and the update give
\[
f(x_{t+1})\le f(x_t)-\eta\sum_i\frac{a_{t,i}z_{t,i}}{\rho+\sqrt{v_{t,i}}}
+\frac{\eta^2}{2}\sum_i\ell_i r_{t,i}.
\tag{3}
\]
For one coordinate with \(c_i>0\), abbreviate \(a=a_{t,i}\), \(b=z_{t,i}\), \(c=c_i\), \(A=\rho+\sqrt{w_{t,i}}\), and \(B=\rho+\sqrt{v_{t,i}}\). Rationalization gives
\[
ab(A^{-1}-B^{-1})
=\frac{((b+a)\xi_{t,i}-c^2)ab}{AB(\sqrt{w_{t,i}}+\sqrt{v_{t,i}})}.
\]
Using \(|b|+|a|\le\sqrt{v_{t,i}}+\sqrt{w_{t,i}}\) and \(c\le\sqrt{v_{t,i}}+\sqrt{w_{t,i}}\), its conditional expectation is bounded above by \(|a|(X+Y)/A\), where
\[
X=\mathbb E_{t-1}\frac{|\xi_{t,i}||b|}{B},\qquad
Y=c\mathbb E_{t-1}\frac{|b|}{B}.
\]
Applying \(|a|X\le a^2/4+X^2\) separately to \(X\) and \(Y\), conditional Holder's inequality and conditional Cauchy--Schwarz give
\[
\mathbb E_{t-1}[ab(A^{-1}-B^{-1})]
\le\frac{a^2}{2A}+\frac{X^2+Y^2}{A},
\]
\[
X^2\le s_i^2\left(\mathbb E_{t-1}\left(\frac{|b|}{B}\right)^{\bar p}\right)^{2/\bar p}
\le s_i^2(\mathbb E_{t-1}r_{t,i})^q,
\qquad Y^2\le c_i^2\mathbb E_{t-1}r_{t,i}.
\]
The second inequality for \(X\) follows from \(|b|/B\le\sqrt{r_{t,i}}\), \(r_{t,i}\le1\), and \(\bar p/2\ge1\). Since \(A\ge c_i\), the error is at most
\[
\frac{a_{t,i}^2}{2(\rho+\sqrt{w_{t,i}})}
+\frac{s_i^2}{c_i}(\mathbb E_{t-1}r_{t,i})^q
+c_i\mathbb E_{t-1}r_{t,i}.
\]
If \(s_i=c_i=0\), the moment assumption implies \(\xi_{t,i}=0\) almost surely. Then \(z_{t,i}=a_{t,i}\) and \(v_{t,i}=w_{t,i}\), so the denominator error is exactly zero. The same upper bound holds with the noise-error term defined to be zero, without evaluating \(0/0\).

Replace the descent denominator in (3) by the proxy denominator and use conditional unbiasedness. Taking expectations and applying concavity of \(x^q\) to \(\mathbb E_{t-1}r_{t,i}\) proves
\[
\frac\eta2\sum_i\mathbb E\frac{a_{t,i}^2}{\rho+\sqrt{w_{t,i}}}
\le\mathbb E[f(x_t)-f(x_{t+1})]
+\eta\sum_{i:s_i>0}\frac{s_i^2}{c_i}(\mathbb E r_{t,i})^q
+\eta\sum_i\left(c_i+\frac{\eta\ell_i}{2}\right)\mathbb E r_{t,i}.
\tag{4}
\]

### 3. Logarithmic telescoping and accumulator control
For \(0<r\le1\), concavity gives
\[
\sum_{t=1}^T(\mathbb E r_{t,i})^r
\le T^{1-r}\left(\mathbb E\sum_{t=1}^T r_{t,i}\right)^r.
\]
Pathwise, \(1-u^{-1}\le\log u\) gives
\[
\sum_{t=1}^T r_{t,i}
=\sum_{t=1}^T\left(1-\frac{\rho^2+v_{t-1,i}}{\rho^2+v_{t,i}}\right)
\le\log(1+v_{T,i}/\rho^2).
\]
Thus
\[
\sum_{t=1}^T(\mathbb E r_{t,i})^r
\le T^{1-r}\left(\mathbb E\log(1+v_{T,i}/\rho^2)\right)^r.
\tag{5}
\]
The optional endpoint \(r=0\) uses the constant-function convention \(x^0=1\), including at zero; the proof only needs \(r=q>0\) and \(r=1\).

Put \(N_i=(\sum_{t=1}^T\xi_{t,i}^2)^{1/2}\) and \(m_i=\mathbb E\sqrt{U_{T,i}}\). Since \(p\le2\),
\[
N_i\le\left(\sum_{t=1}^T|\xi_{t,i}|^p\right)^{1/p},\qquad
\mathbb E N_i\le\left(\sum_{t=1}^T\mathbb E|\xi_{t,i}|^p\right)^{1/p}\le s_iT^{1/p}.
\]
Also \(z_{t,i}^2\le2\xi_{t,i}^2+2a_{t,i}^2\), so
\[
\mathbb E\sqrt{v_{T,i}}\le\sqrt2 s_iT^{1/p}+\sqrt2 m_i.
\tag{6}
\]
Jensen's inequality for the logarithm now yields
\[
\mathbb E\log(1+v_{T,i}/\rho^2)
\le2\log\left(1+\frac{\mathbb E\sqrt{v_{T,i}}}{\rho}\right)
\le D_i,
\qquad
D_i:=2\log\left(1+\frac{\sqrt2s_iT^{1/p}+\sqrt2m_i}{\rho}\right).
\tag{7}
\]
From (2), the inequalities \((a+b)^2\le2a^2+2b^2\) and \(\sum_{t=1}^T(t-1)^2\le T^3\) give
\[
\sqrt{2U_{T,i}}
\le2|a_{1,i}|\sqrt T+2\eta\sqrt{\ell_i\|\ell\|_1}T^{3/2}.
\]
Substitution in (7) proves
\[
\mathbb E\log(1+v_{T,i}/\rho^2)\le D_i\le2\log K_T.
\tag{8}
\]

### 4. Deterministic offset selection
Let
\[
\beta=\frac12-\frac1{\bar p}=\frac1p-\frac12\ge0,
\qquad \alpha=\frac1{\bar p}+\frac12\in(0,1],
\qquad L=\log K_T,
\]
\[
S=\|s\|_1,\qquad H=\Delta/\eta+\eta\|\ell\|_1 L.
\]
Choose
\[
c_i=\begin{cases}s_iT^\beta/D_i^\beta,&s_i>0,\\0,&s_i=0.\end{cases}
\tag{9}
\]
When \(s_i>0\), (7) gives \(D_i>0\), so this is finite and positive. When \(s_i=0\), no power of a possibly zero \(D_i\) is evaluated. Each \(D_i\) is defined using an unconditional expectation, so each offset is deterministic. At \(p=2\), positive-noise coordinates simply have \(c_i=s_i\).

Define
\[
Q_i=\mathbb E\sum_{t=1}^T\frac{a_{t,i}^2}{\rho+\sqrt{w_{t,i}}},\qquad Q=\sum_iQ_i.
\]
Sum (4), use \(f(x_{T+1})\ge f_*\), and apply (5) and (8):
\[
\frac\eta2 Q
\le\Delta+\eta\sum_{i:s_i>0}\left(\frac{s_i^2}{c_i}T^{1-q}D_i^q+c_iD_i\right)
+\eta^2\|\ell\|_1L.
\]
The two offset terms are equal under (9), and each equals \(s_iT^\beta D_i^\alpha\). Since \(D_i\le2L\) and \(\alpha\le1\),
\[
Q\le2H+4\sum_i s_iT^\beta D_i^\alpha
\le2H+8ST^\beta L^\alpha.
\tag{10}
\]
The coefficient replacement here is an inequality, not an equality: \(2^{1/\bar p+3/2}\le4\). This implements the explicit local correction to source line 323.

### 5. Two-case self-bounding closure
Put \(B_i=\rho+\sqrt{v_{T,i}+U_{T,i}+c_i^2}\). Because \(w_{t,i}\le v_{T,i}+U_{T,i}+c_i^2\), Cauchy--Schwarz gives
\[
m_i=\mathbb E\sqrt{(U_{T,i}/B_i)B_i}
\le\sqrt{Q_i\mathbb E B_i}.
\]
The inequality \(z_{t,i}^2+a_{t,i}^2\le2\xi_{t,i}^2+3a_{t,i}^2\), followed by the bound on \(\mathbb E N_i\), implies
\[
\mathbb E B_i\le\rho+c_i+\sqrt2s_iT^{1/p}+\sqrt3m_i.
\tag{11}
\]
If \(D_i\ge1\), (9) gives \(c_i\le s_iT^\beta\le s_iT^{1/p}\), also valid when \(s_i=0\). Therefore
\[
m_i\le\sqrt{Q_i\big(\rho+(1+\sqrt2)s_iT^{1/p}+\sqrt3m_i\big)}.
\]
If \(D_i<1\), its definition instead gives
\[
m_i+s_iT^{1/p}<\frac{\sqrt e-1}{\sqrt2}\rho.
\]
Writing \(a_0=(\sqrt e-1)/\sqrt2\), both cases imply
\[
m_i\le\sqrt{Q_i\big(\rho+(1+\sqrt2)s_iT^{1/p}+\sqrt3m_i\big)}+a_0\rho.
\]
Set \(M=\sum_i m_i\), \(R=d\rho\), \(N=ST^{1/p}\), \(k=1+\sqrt2\), and \(h=\sqrt3\). Cauchy--Schwarz over coordinates yields
\[
M\le\sqrt{Q(R+kN+hM)}+a_0R.
\]
To close it explicitly, split the square root and use
\[
\sqrt{QR}\le(Q+R)/2,\qquad
\sqrt{hQM}\le M/2+hQ/2.
\]
It follows that
\[
M\le(1+h)Q+(1+2a_0)R+2\sqrt{kQN}
\le C\big(R+Q+\sqrt{QN}\big)
\tag{12}
\]
for a numerical constant \(C\). Substituting (10) and using \(\sqrt{x+y}\le\sqrt x+\sqrt y\) gives
\[
M\le C'\left[
R+H+ST^\beta L^\alpha
+\sqrt{HS}\,T^{1/(2p)}
+ST^{\beta/2+1/(2p)}L^{\alpha/2}
\right].
\tag{13}
\]
This argument includes zero noise, zero initial gap, \(p=2\), \(T=1\), and coordinates with \(D_i=0\).

### 6. Final normalization and exponents
Pathwise Cauchy--Schwarz gives
\[
\sum_{t=1}^T\|\nabla f(x_t)\|_1
\le\sqrt T\sum_i\sqrt{U_{T,i}}.
\]
Thus the expected average is at most \(M/\sqrt T\), not \(M/(T\sqrt T)\). Dividing (13) by \(\sqrt T\), and using
\[
\beta-\tfrac12=-\frac{p-1}{p},\qquad
\frac1{2p}-\frac12=-\frac{p-1}{2p},\qquad
\frac\beta2+\frac1{2p}-\frac12=-\frac{3p-4}{4p},
\]
proves
\[
\mathbb E\left[\frac1T\sum_{t=1}^T\|\nabla f(x_t)\|_1\right]
\le C_p\left(
\frac{d\rho+\Delta/\eta+\eta\|\ell\|_1\log K_T}{\sqrt T}
+\frac{\|s\|_1\log^{1/\bar p+1/2}(K_T)}{T^{(p-1)/p}}
+\frac{\sqrt{(\Delta/\eta+\eta\|\ell\|_1\log K_T)\|s\|_1}}{T^{(p-1)/(2p)}}
+\frac{\|s\|_1\log^{1/(2\bar p)+1/4}(K_T)}{T^{(3p-4)/(4p)}}
\right).
\]
The constants above may even be chosen numerical; in particular, they satisfy the requested dependence only on \(p\). The final exponent is positive for the frozen range \(p>4/3\).

## Proof-Obligation Audit
All theorem-critical obligations are closed by the explicit derivations above: weighted gradient smoothness and integrability in Section 1; predictable proxy descent and the zero-noise case in Section 2; telescoping and heavy-tail accumulator-log control in Section 3; deterministic coordinatewise balancing in Section 4; both logarithm cases and self-bounding closure in Section 5; and normalization and all four exponents in Section 6. There is no unresolved specialized or external theorem dependency.
