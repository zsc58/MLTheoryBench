# Reference Proof

## Proof Structure

Construct independent standard-normal variables and the monotone one-dimensional optimal transports to the component laws. Their shared-noise coupling gives the non-strict weighted contrast bound. If equality holds, uniqueness of the one-dimensional optimal coupling makes the mixture a nondecreasing function of the Gaussian projection. Justify this functional identity everywhere, then differentiate it to force every active component transport to be affine with a common slope. Two active affine transports would make two components Gaussian, contradicting the hypothesis. Finally sum the row bounds for an orthogonal matrix and characterize equality.

## Standard Transport Fact and Its Hypotheses

For probability laws \(\mu,\nu\) on \(\mathbb R\) with finite second moments, when \(\mu\) is absolutely continuous, the unique optimal quadratic coupling is induced by the nondecreasing map \(F_\nu^{-1}\circ F_\mu\), defined \(\mu\)-almost everywhere. In particular, if \(Y\) is standard normal, every optimal coupling of \(X\) and \(Y\) satisfies \(X=h(Y)\) almost surely, where \(h=F_{\mathcal L(X)}^{-1}\circ\Phi\) and \(\Phi\) is the standard normal CDF. This is the standard one-dimensional monotone optimal-coupling result. All its uses below have an absolutely continuous Gaussian input and finite-second-moment output.

## Complete Proof

Write \(F_j\) and \(f_j\) for the CDF and density of \(S_j\), and write \(\phi\) for the standard normal density. Since \(f_j\) is smooth and strictly positive on \(\mathbb R\), \(F_j\) is a smooth strictly increasing bijection from \(\mathbb R\) onto \((0,1)\). Define
\[
T_j=F_j^{-1}\circ\Phi.
\]
The inverse function theorem shows that \(T_j\) is smooth and
\[
T_j'(t)=\frac{\phi(t)}{f_j(T_j(t))}>0.
\]
Thus the differentiability and local absolute continuity needed below follow directly from the stated source assumptions.

Let \(N_1,\ldots,N_d\) be independent standard normal variables. The variables \(T_j(N_j)\) are independent and have the component laws of \(S\). By the standard transport fact,
\[
\mathbb E[(T_j(N_j)-N_j)^2]=C(S_j).
\]
These expectations are finite because both variables have finite second moments.

Fix any unit vector \(u\in\mathbb R^d\), and put
\[
X=\sum_j u_jT_j(N_j),\qquad Y=\sum_j u_jN_j.
\]
Then \(X\) has the law of \(\sum_j u_jS_j\), and \(Y\) is standard normal. Both have finite second moments. The differences \(D_j=T_j(N_j)-N_j\) are independent, centered, and square integrable. Consequently,
\[
\mathbb E[(X-Y)^2]
=\sum_j u_j^2\mathbb E[D_j^2]
=\sum_j u_j^2 C(S_j).
\]
Since this is the cost of an admissible coupling,
\[
C\!\left(\sum_j u_jS_j\right)
\leq\sum_j u_j^2C(S_j). \tag{1}
\]

Suppose now that \(u\) has at least two nonzero coordinates and equality holds in (1). The constructed coupling is then optimal. By the standard transport fact,
\[
X=h(Y)\quad\text{almost surely},\qquad
h=F_{\mathcal L(X)}^{-1}\circ\Phi.
\]
We justify differentiating this relation without assuming any smoothness of the mixture density.

Choose an active index \(j\), meaning \(u_j\ne0\), and write \(X=u_jT_j(N_j)+R\), where \(R\) is independent of \(N_j\). Conditional on any value of \(R\), the first term has an atomless distribution assigning positive probability to every nonempty open interval. Hence \(X\) has no atoms and also assigns positive probability to every nonempty open interval. Its CDF is therefore continuous and strictly increasing from \(0\) to \(1\), so its inverse on \((0,1)\) is continuous. In particular, \(h\) is continuous and finite on \(\mathbb R\).

Define the smooth function
\[
F(n)=\sum_j u_jT_j(n_j),\qquad n\in\mathbb R^d.
\]
The identity \(F(N)=h(u\cdot N)\) holds almost surely. Both sides are continuous functions of \(n\), and the joint Gaussian law of \(N\) gives positive probability to every nonempty open set. Their difference must therefore vanish everywhere:
\[
F(n)=h(u\cdot n)\qquad\text{for all }n\in\mathbb R^d.
\]
Because \(\|u\|_2=1\), substitution of \(n=tu\) gives \(h(t)=F(tu)\). Thus \(h\) is smooth as well. Differentiating the everywhere identity now gives
\[
u_jT_j'(n_j)=u_jh'(u\cdot n).
\]
For every active index \(j\),
\[
T_j'(n_j)=h'(u\cdot n).
\]
Choose two distinct active indices \(j,k\). For all independently chosen values of \(n_j,n_k\), these identities imply
\[
T_j'(n_j)=T_k'(n_k).
\]
Fixing one coordinate and varying the other shows that both derivatives are a common constant \(c\). Comparison with any other active index gives the same constant for every active transport. Since each transport is continuously differentiable,
\[
T_j(t)=ct+a_j\qquad\text{for every active }j.
\]
Centering gives \(a_j=0\); positivity of \(T_j'\) gives \(c>0\); and the unit variance of \(T_j(N_j)\) gives \(c^2=1\), hence \(c=1\). Every active source is therefore standard Gaussian. There are at least two active sources, contradicting the assumption that at most one component is Gaussian. Equality in (1) is impossible for a proper mixture. This proves part 1, including arbitrary signs of the active weights.

Now let \(Q\in O(d)\). Each row is a unit vector, so (1) yields
\[
\sum_i C\!\left(\sum_jQ_{ij}S_j\right)
\leq\sum_i\sum_jQ_{ij}^2C(S_j)
=\sum_jC(S_j),
\]
where the last equality uses \(\sum_iQ_{ij}^2=1\) for every column.

All row deficits are nonnegative and finite. If equality holds in the summed bound, each row deficit is zero. Part 1 therefore excludes any row containing two or more nonzero entries. Each unit row must have exactly one nonzero entry, equal to \(1\) or \(-1\). Orthogonality forces these entries to occupy distinct columns, so \(Q\) is a signed permutation matrix.

Conversely, reflection of both variables in any coupling preserves its squared cost and leaves the standard normal marginal unchanged. Applying reflection twice shows \(C(-U)=C(U)\) for every finite-second-moment \(U\). A signed permutation produces the variables \(\pm S_j\) in some order and therefore attains equality in the summed bound. This proves part 2.

## Proof-Obligation Closure

The monotone transport construction and optimal-coupling uniqueness use the stated standard result with Gaussian inputs and finite second moments. Component-map smoothness, continuity and regularity of the equality representation, the constant-slope conclusion, the Gaussian contradiction, the orthogonal sum, and the equality characterization are explicitly established above. No specialized regularity theorem or unresolved paper-specific dependency is required.
