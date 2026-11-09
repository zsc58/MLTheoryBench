# Reference Proof

## Proof Structure

Establish the arithmetic domain of the displayed expression, including the permitted infinite-risk case. Bound the ranking loss by the normalized shifted surrogate. Integrate against the common conditional label distribution, decompose conditional regret, and average using the definitions of the minimizability gaps.

## Complete Proof

Fix an admissible \(h\in\mathcal H\). In particular, \(\mathcal H\) is nonempty. Write
\[
 k=\Phi(-\gamma),\qquad \ell_\gamma=\ell_{\Phi_\gamma},
\]
and abbreviate the corresponding risks and conditional risks by \(R_0,R_\gamma,c_0,c_\gamma\). We have \(0<k<\infty\), since \(\Phi\) is finite-valued and the denominator is assumed positive.

### 1. Definedness and the infinite-risk case

The ranking loss lies in \([0,1]\). Hence \(R_0(h)\), \(R_0^*(\mathcal H)\), and
\[
 b_0=\mathbb E_P[c_0^*(\mathcal H;S)]
\]
are finite. For the surrogate, set
\[
 r_\gamma=R_\gamma^*(\mathcal H),\qquad
 b_\gamma=\mathbb E_P[c_\gamma^*(\mathcal H;S)].
\]
The losses are measurable: score differences are measurable, and a finite monotone real function is Borel measurable because its strict superlevel sets are intervals. The assumed measurability of the conditional infima makes their nonnegative expectations well-defined.

For every \(g\in\mathcal H\), the definition of the pointwise infimum gives
\[
 0\le c_\gamma^*(\mathcal H;S)\le c_\gamma(g;S).
\]
Integrating and using the defining integral property of conditional expectation yields
\[
 0\le b_\gamma\le R_\gamma(g).
\]
Taking the infimum of these numerical upper bounds gives \(b_\gamma\le r_\gamma\); this does not exchange an expectation and an infimum or require an attained optimum.

Admissibility forces \(r_\gamma<\infty\). Indeed, if \(r_\gamma=\infty\), then \(R_\gamma(h)=\infty\), so the displayed difference \(R_\gamma(h)-r_\gamma\) would be undefined. Consequently \(b_\gamma<\infty\), \(M_{\ell_\gamma}(\mathcal H)=r_\gamma-b_\gamma\) is finite, and \(A_\gamma(\mathcal H)=b_\gamma/k-b_0\) is finite.

If \(R_\gamma(h)=\infty\), the right-hand side of the requested inequality is \(+\infty\), while its left-hand side is finite. The claim follows immediately in this case. It remains to prove the result when \(R_\gamma(h)<\infty\). All population-risk subtractions used below are then between finite quantities.

### 2. Pointwise domination

For any scorer \(g\in\mathcal H\), let \(u=w d_g(x,y,y')\). Under the specified binary sign convention,
\[
 \ell_0(g;x,y,y',w)\le\mathbf 1\{u\le0\}.
\]
This need not be equality: when \(d_g=0\) and \(w=1\), the ranking loss is zero but the indicator is one.

If \(u\le0\), then \(u-\gamma\le-\gamma\), so monotonicity gives
\[
 \Phi(u-\gamma)\ge\Phi(-\gamma)=k.
\]
If \(u>0\), the indicator is zero and the surrogate is nonnegative. Thus, for every tuple and every \(g\),
\[
 \ell_0(g;x,y,y',w)
 \le\mathbf 1\{u\le0\}
 \le\frac{\Phi(u-\gamma)}{k}
 =\frac{\ell_\gamma(g;x,y,y',w)}{k}.
\tag{1}
\]

### 3. Conditional comparison and regret decomposition

Conditional risk is integration over the two labels against the same fixed conditional distribution for every scorer. Its weights are nonnegative, so integrating (1) gives
\[
 c_0(g;s)\le\frac{c_\gamma(g;s)}{k}
\tag{2}
\]
for \(P_S\)-almost every \(s\), with the common-law versions making this comparison simultaneous across \(g\). Since scores and \(\Phi\) are finite-valued and there are only two labels, these conditional risks are finite wherever that conditional law is defined. Their infima are nonnegative and finite because \(\mathcal H\) is nonempty.

Taking pointwise infima in (2) gives
\[
 c_0^*(\mathcal H;s)\le\frac{c_\gamma^*(\mathcal H;s)}{k}.
\]
In particular, the measurable function
\[
 a(s)=\frac{c_\gamma^*(\mathcal H;s)}{k}-c_0^*(\mathcal H;s)
\]
is nonnegative, and its expectation is exactly \(A_\gamma(\mathcal H)\).

Apply (2) to the fixed \(h\), subtract \(c_0^*(\mathcal H;s)\), and add and subtract \(c_\gamma^*(\mathcal H;s)/k\). This gives
\[
 c_0(h;s)-c_0^*(\mathcal H;s)
 \le
 \frac{c_\gamma(h;s)-c_\gamma^*(\mathcal H;s)}{k}
 +a(s).
\tag{3}
\]

### 4. Averaging and the gap identities

For either \(\ell=\ell_0\) or \(\ell=\ell_\gamma\), the conditional regret is nonnegative. In the finite-risk case under consideration, both its constituent conditional risks are integrable. By the defining integral property of conditional expectation and the definition of \(M_\ell\),
\[
 \begin{aligned}
 \mathbb E_P[c_\ell(h;S)-c_\ell^*(\mathcal H;S)]
 &=R_\ell(h)-\mathbb E_P[c_\ell^*(\mathcal H;S)]\\
 &=R_\ell(h)-R_\ell^*(\mathcal H)+M_\ell(\mathcal H).
 \end{aligned}
\tag{4}
\]
Take expectations in (3), use \(\mathbb E_P[a(S)]=A_\gamma(\mathcal H)\), and substitute (4). The result is
\[
 R_{\ell_0}(h)-R_{\ell_0}^*(\mathcal H)+M_{\ell_0}(\mathcal H)
 \le
 \frac{R_{\ell_{\Phi_\gamma}}(h)-R_{\ell_{\Phi_\gamma}}^*(\mathcal H)+M_{\ell_{\Phi_\gamma}}(\mathcal H)}{\Phi(-\gamma)}
 +A_\gamma(\mathcal H).
\]
Together with the infinite-risk case, this proves the claim for every admissible \(h\). If \(\mathcal H\) is empty, there is no such \(h\), so the universal assertion is vacuous.

## Obligation Closure

The proof explicitly checks the positive finite normalization, the source-consistent treatment of ties, pointwise domination, common-law conditioning, pointwise-infimum comparison without attainment, identification of the approximation term, admissible extended-real arithmetic, and the risk-gap conversion. No specialized external result or unresolved paper-specific dependency is used.
