# Reference Proof

## Proof Structure

1. Verify the sampling density, measurability, finite second moments, and the parameter-independent mean; identify the mean using the one-dimensional CDF formula.
2. Derive localization from the coupling definition of the infinity transport distance, including its endpoint, and handle zero distance.
3. Define the squared gap profile explicitly and prove its boundedness, monotonicity, and localization.
4. Differentiate the second moment with an integrable dominating function, apply integration by parts, and choose a threshold depending only on the normalized transport distance.
5. Transfer the conclusion to the variance of every independent sample mean.

## Complete Proof

Let \(\sigma\) denote uniform probability measure on the sphere, and put
\[
D_\theta(u,v)=\Delta^{(2)}(\theta,-R+2Ru,-R+2Rv),\qquad A=2(2R)^2.
\]
Write \(Z_k=A D_\theta(U,V)/f_k(U,V)\) for one summand. All density formulas and quotients can be evaluated off the diagonal \(u=v\); arbitrary values on that null set do not change any law or moment.

### 1. Sampling, moments, and mean

The change of variables \(s=v-u\) gives
\[
\int_T f_k(u,v)\,du\,dv
=k(k+1)\int_0^1s^{k-1}(1-s)\,ds=1.
\]
It also shows that the gap has density \(k(k+1)s^{k-1}(1-s)\) on \((0,1)\), the Beta\((k,2)\) density, including at \(k=1\).

Projected CDFs are jointly measurable in direction and threshold: for example,
\[
F_{\mu,\theta}(x)=\int\mathbf 1_{\{\langle\theta,z\rangle\le x\}}\,d\mu(z).
\]
Thus all integrands below are measurable. We have \(0\le D_\theta\le2\). Moreover, for \(0<s\le1\) and \(0<k\le1\),
\[
\frac1{f_k(u,v)}=\frac{s^{1-k}}{k(k+1)}\le\frac1{k(k+1)}.
\]
Consequently \(Z_k\) is bounded for each fixed \(k>0\), so its mean and variance are finite.

Cancellation of the sampling density gives the conditional expectation
\[
\mathbb E[Z_k\mid\theta]=A\int_TD_\theta(u,v)\,du\,dv.
\]
In particular, the unconditional mean
\[
m:=A\int_{\mathbb S^{d-1}}\int_TD_\theta(u,v)\,du\,dv\,d\sigma(\theta)
\]
is independent of \(k\).

For completeness, the audited standard one-dimensional CDF identity states that, for probability measures \(\alpha,\beta\) with finite second moments,
\[
W_2^2(\alpha,\beta)=2\int_{x\le y}\big[(F_\alpha(x)-F_\beta(y))_++(F_\beta(x)-F_\alpha(y))_+\big]\,dx\,dy,
\]
where \(W_2^2\) is the infimum of \(\int|x-y|^2\) over couplings. Our projected laws are supported in \([-R,R]\), hence have finite second moments. Their CDF integrand vanishes outside \(-R\le x\le y\le R\), apart from immaterial boundary sets. The substitution \(x=-R+2Ru\), \(y=-R+2Rv\) therefore identifies the conditional expectation above with \(W_2^2(\mu_\theta,\nu_\theta)\). Thus \(m\) is its uniform directional average, proving the stated estimator's unbiasedness interpretation. Only the independence of \(m\) from \(k\) is needed for the target.

The summands are independent and identically distributed for each \(k\), so
\[
\operatorname{Var}(\widehat S_{2,L,k}^2)=\frac1L\big(\mathbb E[Z_k^2]-m^2\big).
\]

### 2. Localization and zero distance

Put \(w=W_\infty(\mu,\nu)\). For every \(h>w\), the definition of the infimum supplies a coupling \((X,Y)\) with \(\|X-Y\|\le h\) almost surely. Since projection onto a unit vector is 1-Lipschitz, the projected coupling has displacement at most \(h\); this also proves the projection contraction for \(W_\infty\).

For every real \(x\), the event \(\langle\theta,X\rangle\le x\) implies \(\langle\theta,Y\rangle\le x+h\). Hence
\[
F_{\mu,\theta}(x)\le F_{\nu,\theta}(x+h),\qquad
F_{\nu,\theta}(x)\le F_{\mu,\theta}(x+h).
\]
Letting \(h\downarrow w\) and using CDF right continuity gives these inequalities with \(h=w\). Consequently, if \(y-x\ge w\), monotonicity of the CDFs yields
\[
F_{\mu,\theta}(x)\le F_{\nu,\theta}(y),\qquad
F_{\nu,\theta}(x)\le F_{\mu,\theta}(y),
\]
so \(\Delta^{(2)}(\theta,x,y)=0\). This proves localization, including equality at the gap threshold, without assuming that an optimal coupling is attained or invoking an unproved CDF characterization.

If \(w=0\), these inequalities show that the two projected CDFs agree for every direction. Their discrepancy is therefore zero whenever \(x\le y\), so every estimator is identically zero. Choose \(k_0=1/2\) in this case.

For the remainder, assume \(w>0\) and define
\[
\varepsilon=\frac{w}{2R}\in(0,e^{-1/2}).
\]
Localization gives \(D_\theta(u,v)=0\) whenever \(v-u\ge\varepsilon\).

### 3. The gap profile and second moment

Define, for \(0\le s\le1\),
\[
H(s)=\int_{\mathbb S^{d-1}}\int_0^{1-s}D_\theta(u,u+s)^2\,du\,d\sigma(\theta).
\]
Then \(0\le H(s)\le4\), \(H(1)=0\), and \(H(s)=0\) for \(s\ge\varepsilon\).

For fixed \(\theta,u\), increasing \(s\) increases only the second CDF argument in each positive-part expression defining \(D_\theta(u,u+s)\). Both expressions are nonincreasing in \(s\). Squaring preserves this ordering because they are summed into a nonnegative quantity. Thus for \(s_1\le s_2\),
\[
\int_0^{1-s_2}D_\theta(u,u+s_2)^2\,du
\le\int_0^{1-s_2}D_\theta(u,u+s_1)^2\,du
\le\int_0^{1-s_1}D_\theta(u,u+s_1)^2\,du.
\]
Averaging over directions proves that \(H\) is nonincreasing. CDF right continuity and dominated convergence, also accounting for the moving integration endpoint, show that \(H\) is right continuous. In particular, it has bounded variation, and its Stieltjes derivative \(dH\) is a finite negative measure with support contained in \([0,\varepsilon]\).

Squaring the summand and cancelling one factor of its sampling density gives
\[
\begin{aligned}
\Phi(k):=\mathbb E[Z_k^2]
&=A^2\int_{\mathbb S^{d-1}}\int_T\frac{D_\theta(u,v)^2}{f_k(u,v)}\,du\,dv\,d\sigma(\theta)\\
&=C\int_0^1K_k(s)H(s)\,ds,
\end{aligned}
\]
where
\[
C=A^2=4(2R)^4,\qquad K_k(s)=\frac{s^{1-k}}{k(k+1)}.
\]
These identities follow by the same gap change of variables and Tonelli's theorem.

### 4. Differentiation and the sign argument

Fix \(a>0\). Uniformly over \(k\in[a,1]\),
\[
\left|\partial_k K_k(s)\right|
=K_k(s)\left| -\log s-\frac1k-\frac1{k+1}\right|
\le C_a(1+|\log s|),\qquad 0<s<1,
\]
for a finite constant \(C_a\). The right side is integrable and \(H\) is bounded. Dominated convergence therefore justifies differentiation for \(0<k<1\), the left derivative at \(1\), and continuity on each \([a,1]\). Set
\[
q_k(s)=\partial_kK_k(s)
=K_k(s)\left(-\log s-\frac1k-\frac1{k+1}\right).
\]
An antiderivative with respect to \(s\), with value zero at the origin, is
\[
G_k(s)=\frac{s^{2-k}}{k(k+1)(2-k)}
\left(-\log s+\frac1{2-k}-\frac1k-\frac1{k+1}\right),\qquad G_k(0)=0.
\]
Direct differentiation gives \(\partial_sG_k=q_k\). Define
\[
r_k=\exp\left(\frac1{2-k}-\frac1k-\frac1{k+1}\right).
\]
The bracket in \(G_k(s)\) is \(\log(r_k/s)\), so \(G_k(s)\ge0\) for \(0\le s\le r_k\). Furthermore,
\[
\frac{d}{dk}\log r_k
=\frac1{(2-k)^2}+\frac1{k^2}+\frac1{(k+1)^2}>0,
\]
\(r_k\to0\) as \(k\downarrow0\), and \(r_1=e^{-1/2}\). There is therefore a unique \(k_0\in(0,1)\) with \(r_{k_0}=\varepsilon\). It depends only on \(\varepsilon=w/(2R)\), and \(r_k\ge\varepsilon\) for every \(k\in[k_0,1]\).

Since \(G_k\) is absolutely continuous with integrable derivative and \(H\) has bounded variation, integration by parts gives
\[
\begin{aligned}
\Phi'(k)
&=C\int_0^1q_k(s)H(s)\,ds\\
&=C[G_k(s)H(s)]_0^1-C\int_{(0,1)}G_k(s)\,dH(s)\\
&=-C\int_{(0,1)}G_k(s)\,dH(s)\ge0
\end{aligned}
\]
for \(k\in(k_0,1)\). The boundary terms vanish because \(G_k(0)=0\), \(H\) is bounded, and \(H(1)=0\). The last sign follows because \(dH\le0\), its support is contained in \([0,\varepsilon]\), and \(G_k\ge0\) there. The same sign holds for the appropriate endpoint derivatives, but continuity alone suffices to extend monotonicity to the closed interval \([k_0,1]\).

### 5. Variance conclusion

The identity
\[
\operatorname{Var}(\widehat S_{2,L,k}^2)=\frac{\Phi(k)-m^2}{L}
\]
now proves the desired monotonicity for every positive integer \(L\). The chosen threshold depends only on \(R\) and \(w\), not on the dimension, other features of the measures, or \(L\).

## Source Audit Note

The source's antiderivative uses the opposite sign and a different positive normalization from the one above. At L000372-L000373, its displayed antiderivative differentiates to \(s^{1-k}(1/k+1/(k+1)+\log s)\), not to the unweighted expression named in the prose. This local correction is recorded under theory_008. The existing zero-distance repair under theory_010 is retained. All theorem-critical obligations are closed.
