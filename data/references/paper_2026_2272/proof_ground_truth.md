# Reference Proof

## Proof Structure

Represent both dynamics by the geometric family. Derive their parameters from the normalized log-density equation, calculate the KL derivative at interior interpolation parameters, and integrate. Endpoint variances need not be finite, so a zero lower endpoint is handled by continuity and monotone convergence.

## Complete Proof

### 1. Normalization, integrability, and continuity

Put
\[
\ell=\log\frac{\mu_0}{\pi},\qquad
w_a=\mu_0e^{-a\ell}=\mu_0^{1-a}\pi^a,\qquad
Z(a)=\int w_a,\qquad
m(a)=\frac{\int \ell w_a}{Z(a)}.
\]
The quadratic log-ratio bound and the two finite second moments imply
\[
\int |\ell|(\mu_0+\pi)<\infty.
\]
For every \(a\in[0,1]\), weighted arithmetic-geometric mean gives
\[
0<w_a\le (1-a)\mu_0+a\pi\le\mu_0+\pi.
\]
Thus \(0<Z(a)\le1\). Dominated convergence shows that \(Z\) and \(\int\ell w_a\) are continuous on \([0,1]\). In particular, \(Z\) has a positive minimum there, and \(m\) is continuous. The same domination also shows that every \(\rho_a\) has a finite second moment.

Differentiating \(w_a\) once is justified by the integrable bound \(|\ell|(\mu_0+\pi)\), including one-sided differentiation at the endpoints. Hence
\[
Z'(a)=-Z(a)m(a),\qquad
\partial_a\rho_a=-\rho_a(\ell-m(a)),
\]
with the density derivative also valid in \(L^1\). All first moments appearing here are finite; no endpoint second moment of \(\ell\) is asserted.

The identity
\[
\log\frac{\rho_a}{\pi}=(1-a)\ell-\log Z(a)
\]
gives a finite KL divergence
\[
F(a):=D(\rho_a\|\pi)=(1-a)m(a)-\log Z(a).
\]
Consequently, \(F\) is continuous on \([0,1]\).

### 2. Identification of the two flows

Treat both flows at once by taking \(\eta_t=\lambda_t\) for the tempered flow and \(\eta_t=1\) for the standard flow. Their target is \(q_t=\rho_{\eta_t}\). Define
\[
a(t)=\int_0^t e^{-(t-s)}\eta_s\,ds.
\]
Then \(a(0)=0\), \(a'=\eta-a\) almost everywhere, and
\[
0\le a(t)\le1-e^{-t}<1
\]
for every finite \(t>0\).

To identify any positive normalized solution \(\nu_t\), set
\[
h_t(x)=\log\frac{\nu_t(x)}{\mu_0(x)},\qquad
c_t=\int\nu_t\log\frac{q_t}{\nu_t}.
\]
The specified solution interpretation makes \(c_t\) locally integrable. Since
\[
\log q_t=\log\mu_0-\eta_t\ell-\log Z(\eta_t),
\]
the normalized flow equation becomes
\[
\partial_t h_t+h_t=-\eta_t\ell-\log Z(\eta_t)-c_t.
\]
The integrating factor \(e^t\) yields
\[
h_t(x)=-a(t)\ell(x)+k(t),\qquad
k(t)=-\int_0^t e^{-(t-s)}\bigl(\log Z(\eta_s)+c_s\bigr)\,ds.
\]
Here \(k(t)\) is independent of \(x\). Normalization forces \(e^{k(t)}=Z(a(t))^{-1}\). Thus any such solution equals \(\rho_{a(t)}\).

Conversely, \(\rho_{a(t)}\) is a solution. Indeed,
\[
\partial_t\rho_{a(t)}=-a'(t)\rho_{a(t)}(\ell-m(a(t))),
\]
while centering
\[
\log\frac{q_t}{\rho_{a(t)}}
=(a(t)-\eta_t)\ell+\log Z(a(t))-\log Z(\eta_t)
\]
gives \((a(t)-\eta_t)(\ell-m(a(t)))\). The two sides of the flow equation therefore agree. The previously established uniform bounds on \(Z^{-1}\) and \(\int|\ell|\rho_a\) verify the required local time integrability. The formula for the log-density verifies local absolute continuity in time. This also proves existence and uniqueness in the stated class.

It follows that
\[
\mu_t^{\mathrm{T-FR}}=\rho_{\alpha_T(t)},\qquad
\alpha_T(t)=\int_0^t e^{-(t-s)}\lambda_s\,ds,
\]
and
\[
\mu_t^{\mathrm{FR}}=\rho_{\alpha_S(t)},\qquad
\alpha_S(t)=1-e^{-t}.
\]
No cancellation of \(\ell-m(a)\) was used, so the argument also covers \(\mu_0=\pi\).

### 3. Interior KL derivative

Fix \(0<\delta<1/2\). For \(a\in[\delta,1-\delta]\), split according to the sign of \(\ell\). On \(\{\ell\ge0\}\),
\[
|\ell|^2w_a=\ell^2\mu_0e^{-a\ell}\le C_\delta\mu_0.
\]
On \(\{\ell<0\}\), write \(w_a=\pi e^{(1-a)\ell}\) to obtain
\[
|\ell|^2w_a\le C_\delta\pi.
\]
The constants are finite because \(r^2e^{-\delta r}\) is bounded for \(r\ge0\). These integrable bounds justify differentiation of \(\int\ell w_a\) and continuity of the relevant second moments throughout the interior. The quotient rule gives
\[
m'(a)=-\frac{\int\ell^2w_a}{Z(a)}+m(a)^2
=-\operatorname{Var}_{\rho_a}(\ell),\qquad 0<a<1.
\]
Using the formula for \(F\) and \((\log Z)'=-m\),
\[
F'(a)=-m(a)+(1-a)m'(a)+m(a)
=-(1-a)\operatorname{Var}_{\rho_a}(\ell).
\]
This is an interior derivative identity; the variance at \(a=0\) or \(a=1\) can be infinite.

### 4. Parameter ordering and endpoint integration

The schedule range implies
\[
0\le\alpha_T(t)\le\int_0^t e^{-(t-s)}\,ds=\alpha_S(t)<1
\]
for finite \(t>0\). Monotonicity of the schedule is part of the source contract, but the displayed ordering uses only its range.

For \(0<a<b<1\), the interior derivative calculation and the fundamental theorem of calculus yield
\[
F(b)-F(a)=-\int_a^b(1-u)\operatorname{Var}_{\rho_u}(\ell)\,du.
\]
If \(a=0<b<1\), apply this equality with lower endpoint \(\varepsilon\in(0,b)\). Continuity gives \(F(\varepsilon)\to F(0)\), and monotone convergence for the nonnegative integrand gives
\[
F(b)-F(0)=-\int_0^b(1-u)\operatorname{Var}_{\rho_u}(\ell)\,du.
\]
The integral is finite because the KL difference is finite. The value, possibly infinite, of the variance at the single endpoint zero does not affect the Lebesgue integral. Equal endpoints give zero by definition.

Taking \(a=\alpha_T(t)\) and \(b=\alpha_S(t)\) proves, for every finite \(t\ge0\),
\[
D(\mu_t^{\mathrm{FR}}\|\pi)-D(\mu_t^{\mathrm{T-FR}}\|\pi)
=-\int_{\alpha_T(t)}^{\alpha_S(t)}(1-u)\operatorname{Var}_{\rho_u}\!\left(\log\frac{\mu_0}{\pi}\right)\,du\le0.
\]
At \(t=0\), both flows equal \(\mu_0\) and the integration interval is empty. A schedule that remains zero for a time interval is covered by the zero-endpoint argument. If \(\mu_0=\pi\), all densities coincide and every gap is zero. This establishes the exact comparison and the no-speedup conclusion.

## Source Repair Note

The integrated normalized log-density equation retains the term \(-\int_0^t e^{s-t}\log Z(\eta_s)\,ds\). The source omits this spatially constant term in its intermediate equality at L000886. Restoring it does not alter the final proportional-density representation. This source-local repair is recorded under theory_005.
