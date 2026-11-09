# Reference Proof

## Proof Structure

1. Establish the Hilbert–Schmidt factorization and equality of the first two noise moments.
2. Expand at the common drift-shifted point to obtain a uniform cubic one-step weak error.
3. Differentiate the Gaussian transition in mean, derive the three correct linear derivative recurrences, and bound their sum without division.
4. Telescope the transition operators and sum the local errors over the finite horizon.

## Complete Proof

Write \(L_r=\|D^r b\|_\infty\) and \(S_r=\|D^r\sigma\|_\infty\), for \(r=1,2,3\). The range norm for derivatives of \(\sigma\) is the Hilbert–Schmidt norm. Throughout, \(0<\eta\le\bar\eta<\infty\).

### 1. Noise factorization and integrability

For \(h\in H\), duality gives
\[
\sigma(x)^*h=\langle V(x;\cdot),h\rangle\in U.
\]
If \((f_j)\) is an orthonormal basis of \(H\), Parseval and monotone convergence give
\[
\|\sigma(x)^*\|_{L_2(H,U)}^2
=\sum_j\mathbb E_\gamma|\langle V(x;\gamma),f_j\rangle|^2
=\mathbb E_\gamma\|V(x;\gamma)\|^2.
\]
Thus \(\sigma(x)\) is Hilbert–Schmidt. For \(h_1,h_2\in H\),
\[
\langle\sigma(x)\sigma(x)^*h_1,h_2\rangle
=\mathbb E_\gamma[\langle V(x;\gamma),h_1\rangle\langle V(x;\gamma),h_2\rangle]
=\langle Q(x)h_1,h_2\rangle.
\]
Consequently, for a standard cylindrical Gaussian \(\xi\), the variables \(Y=V(x;\gamma)\) and \(Z=\sigma(x)\xi\) are centered and have the same covariance.

Only radonified cylindrical variables are used. For a Hilbert–Schmidt \(S\), the finite Gaussian sums defining \(S\xi\) converge in \(L^2(H)\). Expanding fourth moments of finite sums using independent standard Gaussian coordinates gives
\[
\mathbb E\|S\xi\|^4
=(\operatorname{Tr}SS^*)^2+2\|SS^*\|_{L_2(H,H)}^2
\le3\|S\|_{L_2(U,H)}^4.
\]
The same bound applied to tails gives convergence in \(L^4\). Hence, with \(\kappa=3^{1/4}\),
\[
\|S\xi\|_{L^p(H)}\le\kappa\|S\|_{L_2(U,H)},\qquad 1\le p\le4.
\]
Higher finite Gaussian moments are also bounded by constants times the corresponding power of the Hilbert–Schmidt norm. For completeness, for \(p\ge2\), Minkowski applied to \(\sum_j|\langle S\xi,f_j\rangle|^2\) in \(L^{p/2}\) gives
\[
\|S\xi\|_{L^p(H)}^2
\le (\mathbb E|N|^p)^{2/p}\sum_j\|S^*f_j\|^2,
\]
where \(N\) is a real standard Gaussian. This also proves the required higher-moment convergence of Gaussian series.

These arguments do not require the entire space \(U\) to be separable. Alternatively, a common separable noise subspace suffices: continuity of \(\sigma\), a countable dense subset of \(H\), and a countable basis of \(H\) give a separable closed subspace \(U_0\subset U\) containing every range \(\sigma(x)^*H\). Indeed, take the closed span of \(\sigma(x_i)^*f_j\) and approximate arbitrary \(x,h\). Every \(\sigma(x)\) vanishes on \(U_0^\perp\); so do its derivatives. All Gaussian series may therefore be realized on one countable basis of \(U_0\).

The coefficient \(b\) need not be bounded. Boundedness of its first derivative gives
\[
\|b(x)\|\le\|b(0)\|+L_1\|x\|.
\]
The third-moment assumption bounds each noise's first moment by \(D^{1/3}\). Conditioning on each iteration's own past therefore shows inductively that both iterates have finite first moments. Since every \(g\in\mathcal G\) satisfies \(|g(x)|\le|g(0)|+\|Dg\|_\infty\|x\|\), all target expectations are finite. Independence between the two different noise sources is unnecessary; each recursion has its specified marginal Markov law.

### 2. Local weak discrepancy

Fix \(x\) and put \(a=x+\eta b(x)\). Taylor's formula, or its bounded-third-derivative remainder estimate along the segment, gives
\[
f(a+\eta Y)=f(a)+\eta Df(a)Y+\frac{\eta^2}{2}D^2f(a)[Y,Y]+R_Y,
\qquad
|R_Y|\le\frac{\eta^3}{6}\|D^3f\|_\infty\|Y\|^3.
\]
The same formula holds with \(Z\). Centeredness cancels the linear expectations. Equality of covariance cancels the quadratic expectations: a bounded bilinear form on \(H\) has expectation determined by the covariance of a centered square-integrable variable, as follows by finite-dimensional projection and convergence in \(L^2(H)\).

Define
\[
(Pf)(x)=\mathbb E_\gamma f(x+\eta b(x)+\eta V(x;\gamma)),\qquad
(Af)(x)=\mathbb E f(x+\eta b(x)+\eta\sigma(x)\xi).
\]
It follows that
\[
\|(P-A)f\|_\infty\le\frac{D\eta^3}{6}\|D^3f\|_\infty,
\qquad f\in\mathcal G.
\]
The functions themselves need not be bounded; their difference in this display is bounded.

### 3. Mean differentiation and regularity propagation

Let \(\Phi_x=x+\eta b(x)+\eta\sigma(x)\xi\). The Gaussian moment bounds show that the map \(S\mapsto S\xi\) is bounded linear from \(L_2(U,H)\) to \(L^p(H)\) for every finite \(p\). Thus \(x\mapsto\Phi_x\) is three-times Frechet differentiable as an \(L^p(H)\)-valued map, with evaluations
\[
J_x[h]=h+\eta Db(x)h+\eta D\sigma(x)[h]\xi,
\]
\[
K_x[h_1,h_2]=\eta D^2b(x)[h_1,h_2]+\eta D^2\sigma(x)[h_1,h_2]\xi,
\]
\[
R_x[h_1,h_2,h_3]=\eta D^3b(x)[h_1,h_2,h_3]+\eta D^3\sigma(x)[h_1,h_2,h_3]\xi.
\]
No assertion of almost sure Frechet differentiability of a random map is needed.

Differentiating the scalar expectation gives
\[
D(Af)(x)h=\mathbb E\,Df(\Phi_x)J_x[h],
\]
\[
D^2(Af)(x)[h_1,h_2]
=\mathbb E\bigl(D^2f(\Phi_x)[J_x[h_1],J_x[h_2]]+Df(\Phi_x)K_x[h_1,h_2]\bigr),
\]
and
\[
\begin{aligned}
D^3(Af)(x)[h_1,h_2,h_3]=\mathbb E\bigl(&D^3f(\Phi_x)[J_x[h_1],J_x[h_2],J_x[h_3]]\\
&+D^2f(\Phi_x)[K_x[h_1,h_2],J_x[h_3]]\\
&+D^2f(\Phi_x)[K_x[h_1,h_3],J_x[h_2]]\\
&+D^2f(\Phi_x)[K_x[h_2,h_3],J_x[h_1]]\\
&+Df(\Phi_x)R_x[h_1,h_2,h_3]\bigr).
\end{aligned}
\]
Here is a justification of differentiation under expectation that also covers the stated class without assuming continuity of the highest derivative. The derivatives through order two of \(f\) are Lipschitz, because the next derivatives exist and are bounded. At each point, Frechet differentiability gives a remainder that is small uniformly over increment directions; boundedness of the next derivative bounds that remainder by a constant times the increment norm. In the difference quotients above, \(\Phi_{x+h}-\Phi_x\) is \(O(\|h\|)\) in every finite \(L^p\). Split according to whether the local Frechet remainder at \(\Phi_x\) is within a fixed tolerance and whether the random increment is within its corresponding radius. The probability of the exceptional set tends to zero, uniformly over directions, by first choosing a positive radius outside a set of small probability and then using the \(L^p\) increment bound. Hölder's inequality and the higher Gaussian moment bounds make the normalized products uniformly integrable. The expected remainders are therefore \(o(\|h\|)\), uniformly in the remaining unit directions. The \(L^p\) Frechet remainders of \(\Phi,J,K\) are handled in the same way. This establishes the displayed formulas as Frechet derivatives, including the third derivative.

Put
\[
a=L_1+\kappa S_1,\qquad d_2=L_2+\kappa S_2,\qquad d_3=L_3+\kappa S_3.
\]
Minkowski and the Gaussian moment bound imply
\[
\|J_x[h]\|_{L^3}\le(1+\eta a)\|h\|,
\]
\[
\|K_x[h_1,h_2]\|_{L^3}\le\eta d_2\|h_1\|\|h_2\|,
\quad
\|R_x[h_1,h_2,h_3]\|_{L^3}\le\eta d_3\prod_i\|h_i\|.
\]
The same bounds hold in \(L^1\) and \(L^2\). Applying Hölder to each term of the derivative formulas proves that \(A\) preserves \(\mathcal G\). With \(z_{r,m}=\|D^rA^mg\|_\infty\), it gives the linear recurrences
\[
z_{1,m+1}\le(1+\eta a)z_{1,m},
\]
\[
z_{2,m+1}\le(1+\eta a)^2z_{2,m}+\eta d_2z_{1,m},
\]
\[
z_{3,m+1}\le(1+\eta a)^3z_{3,m}
+3\eta d_2(1+\eta a)z_{2,m}+\eta d_3z_{1,m}.
\]
The factor 3 accounts for the three mixed terms.

Let \(Z_m=z_{1,m}+z_{2,m}+z_{3,m}\) and choose
\[
c=3a+3\bar\eta a^2+\bar\eta^2a^3+(4+3\bar\eta a)d_2+d_3.
\]
Expanding the powers and using \(\eta\le\bar\eta\) shows, coefficient by coefficient, that
\[
Z_{m+1}\le(1+c\eta)Z_m.
\]
Therefore, whenever \(m\eta\le T\),
\[
\|D^3A^mg\|_\infty\le Z_m
\le(1+c\eta)^mZ_0
\le e^{cT}\sum_{r=1}^3\|D^rg\|_\infty=:B.
\]
This proof uses no divisions and is valid when any or all of the coefficient derivative bounds vanish. The constant \(B\) depends only on the displayed derivative bounds, \(T\), and \(\bar\eta\), not on the initial state, \(\eta\), or \(m\).

### 4. Global comparison

For \(k\ge1\), the algebraic identity
\[
P^k-A^k=\sum_{j=0}^{k-1}P^j(P-A)A^{k-1-j}
\]
holds on the integrable functions used here. The propagated functions have bounded first derivatives and hence at most linear growth, so each composition is integrable. Moreover, each \((P-A)A^mg\) is bounded by the local estimate, and a Markov operator does not increase the supremum norm of a bounded function. Evaluating at the common initial state gives
\[
\begin{aligned}
|\mathbb E g(\phi_k)-\mathbb E g(\widetilde\phi_k)|
&\le\sum_{j=0}^{k-1}\frac{D\eta^3}{6}\|D^3A^{k-1-j}g\|_\infty\\
&\le\frac{kD\eta^3B}{6}
\le\frac{TD B}{6}\eta^2
\end{aligned}
\]
for \(k\le\lfloor T/\eta\rfloor\). Taking \(C_{g,b,\sigma,T,\bar\eta}=TB/6\) proves the claim. At \(k=0\) the discrepancy is zero; if \(\lfloor T/\eta\rfloor=0\), this is the only case. The argument also covers \(D=0\), constant test functions, and all zero-coefficient cases.
