# Reference Proof

## Proof Structure and Obligations

The four obligations are: obtain a uniform per-step classifier bound from the stated finite divergence; sum it under the stated schedule; prove soundness of the open ball using the reference-centered trajectory bound; and establish divergent verifier utility under the uniform conditional coverage assumption. The classifier observes only the feature map, whereas the verifier acts on the proposed parameter. Both rates are computed using the same conditional parameter laws.

## Complete Proof

### 1. Per-step classifier bound

Let \(f=dP^+/dP^-\), which exists by absolute continuity. Set
\[
\alpha=\alpha_0,\qquad
\alpha'=\frac{\alpha}{\alpha-1},\qquad
\beta=\frac{\alpha-1}{\alpha}.
\]
Thus \(1/\alpha+1/\alpha'=1\). The divergence assumption gives
\[
\int f^\alpha\,dP^-
=\exp\bigl((\alpha-1)D_\alpha(P^+\Vert P^-)\bigr)<\infty.
\]
The acceptance event \(A_n\) is measurable, and its indicator belongs to \(L^{\alpha'}(P^-)\), since \(P^-\) is a probability measure.

Hölder's inequality states that for conjugate exponents \(a,b>1\), \(u\in L^a\), and \(v\in L^b\), one has \(\int |uv|\le(\int |u|^a)^{1/a}(\int |v|^b)^{1/b}\). Applying it to \(f\) and \(\mathbf1_{A_n}\), with the verified exponents and integrability conditions, gives
\[
\begin{aligned}
\operatorname{TPR}_n
&=\int f\mathbf1_{A_n}\,dP^-\\
&\le \left(\int f^\alpha\,dP^-\right)^{1/\alpha}
       \left(\int\mathbf1_{A_n}^{\alpha'}\,dP^-\right)^{1/\alpha'}\\
&=C\delta_n^\beta,
\end{aligned}
\]
where
\[
C=\exp\bigl(\beta D_\alpha(P^+\Vert P^-)\bigr)<\infty.
\]
Stationarity makes \(C\) independent of \(n\). This also covers \(\delta_n=0\); no division by \(\delta_n\) is used. Choosing \(\alpha=\alpha_0\) avoids any need for an additional divergence-monotonicity argument.

### 2. Classifier impossibility

The assumption \(\alpha>p/(p-1)\) implies
\[
p\beta=p\left(1-\frac1\alpha\right)>1.
\]
Consequently,
\[
\operatorname{TPR}_n\le Cc^\beta n^{-p\beta}.
\]
For every real \(s>1\), monotonicity of \(x^{-s}\) gives
\[
\sum_{n=1}^\infty n^{-s}
\le 1+\int_1^\infty x^{-s}\,dx
=1+\frac1{s-1}<\infty.
\]
Using \(s=p\beta\) yields
\[
\sum_{n=1}^\infty\operatorname{TPR}_n
\le Cc^\beta\left(1+\frac1{p\beta-1}\right)<\infty.
\]
Likewise, \(\sum_n\delta_n\le c(1+1/(p-1))<\infty\). The required divergent utility condition therefore fails for every classifier sequence in the stated regime.

### 3. Verifier soundness and zero false acceptance

Put \(r=m/L\), \(B=B(\theta_0,r)\), and \(h=\mathbf1_B\). The radius is positive and finite, and \(B\) is open and hence Borel, so this is a measurable verifier.

If \(\theta\in B\), the assumed reference-centered bound gives
\[
\rho(F(\theta),F(\theta_0))
\le L\|\theta-\theta_0\|_2<m.
\]
For every \(u\in U\), the triangle inequality and margin assumption imply
\[
\rho(F(\theta),u)
\ge \rho(F(\theta_0),u)-\rho(F(\theta),F(\theta_0))
\ge m-L\|\theta-\theta_0\|_2>0.
\]
It follows that \(F(\theta)\notin U\). If \(U\) is empty, this conclusion holds immediately as well. The oracle-certification implication now gives \(S(\theta)=\mathrm{safe}\). Thus \(B\subseteq E_+\), proving soundness. Because \(Q_n^-\) is the proposal law conditional on \(E_-\),
\[
\delta_n^{\mathrm{ver}}
=Q_n^-(B)
=\frac{\mu_n(B\cap E_-)}{\mu_n(E_-)}=0
\]
for every \(n\). No all-pairs Lipschitz bound or closedness of \(U\) is needed.

### 4. Verifier utility

For every \(n\), the stated conditional coverage assumption gives
\[
\operatorname{TPR}_n^{\mathrm{ver}}=Q_n^+(B)\ge q.
\]
Hence for every positive integer \(N\),
\[
\sum_{n=1}^N\operatorname{TPR}_n^{\mathrm{ver}}\ge Nq,
\]
which tends to infinity. Together with zero false acceptance, this establishes the verifier conclusion.

## Private Source-Contract and Normalization Note

The source's fixed Gaussian mutation example supplies positive coverage, but its displayed ball probability is an unconditional acceptance probability. For a fixed proposal law \(\mu\), write \(s=\mu(E_+)\). After ball soundness has been proved, \(B\subseteq E_+\), and therefore
\[
Q^+(B)=\frac{\mu(B)}{s}\ge\mu(B)>0.
\]
For the source's nondegenerate Gaussian centered at \(\theta_0\), positivity follows directly from its everywhere-positive density and the positive Lebesgue volume of the nonempty open ball. The fixed proposal law makes this positive lower bound independent of the step. The public task retains the more general, already stated uniform conditional lower bound \(q\), so no Gaussian calculation is required of a solution. Positivity separately at each step, without uniformity or another divergent-sum condition, would not suffice.

All conclusions concern the numerical series of conditional rates. Neither temporal independence nor a sample-path assertion about infinitely many accepted improvements or never encountering an unsafe acceptance is invoked.
