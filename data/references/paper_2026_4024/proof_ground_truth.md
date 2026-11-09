# Reference Proof

## Audit status and obligation ledger

The public task is verified against the complete source contract. This reference reconstructs the projected-matrix calculation and repairs the local concentration-threshold and moment-counting errors. It is not a fully closed proof: the nonstandard eigenvalue-rigidity input stated in Section 5 remains an explicit external derivation obligation.

The theorem-critical obligations are:

1. Permutation normalization, existence of minimizers, and uniform commutator control — closed below.
2. Spectral projection and the total-mass identity — closed below.
3. Uniform projected-matrix entry bounds, including Gaussian representation, all monomial classes, and sufficient failure probabilities — closed below using the explicitly stated independent quadratic-form inequality.
4. The precise GOE rigidity statement in Section 5 — unresolved nonstandard dependency, theory_013. Its implication for separated eigenvalue gaps is closed below.
5. Uniform trace, Frobenius, and row-wise rounding deductions — closed conditional on obligation 4.

No unresolved obligation is a public assumption. The final theorem remains the target to prove.

## 1. Normalize and control the commutator

Both feasible sets are nonempty compact subsets of a finite-dimensional space, and the objective is continuous, so minimizers exist. Write Y=XP^T. Right multiplication by P^T preserves each feasible set and

\[
\|AX-XB\|_F=\|AY-Y(A+\sigma Z)\|_F,
\qquad \|X-P\|_F=\|Y-I\|_F.
\]

It suffices to analyze the normalized model. Rename Y as X. Every feasible X belongs to H_n, hence

\[
\|X\|_F^2\le \sum_{a,b}X_{ab}=n.
\]

The independent GOE operator-norm fact used here is that, for the stated variances, P(||Z||_2<=3) tends to one. The model satisfies exactly its symmetric Gaussian and variance hypotheses. Also ||Z||_F^2 has distribution (2/n) times a chi-square variable with n(n+1)/2 degrees of freedom; consequently ||Z||_F<=2sqrt(n) with probability tending to one. For every minimizer of either relaxation, comparison with I gives

\[
\|AX-X(A+\sigma Z)\|_F\le \sigma\|Z\|_F.
\]

Thus, on a common event,

\[
\|AX-XA\|_F
\le \sigma\|Z\|_F+\sigma\|XZ\|_F
\le 5\sigma\sqrt n. \tag{1}
\]

This event and inequality do not depend on a choice of minimizer or on sigma.

## 2. Spectral projection and total mass

Let A=sum_r lambda_r u_r u_r^T with increasing eigenvalues. Fix eta=kappa/(log n)^4, where kappa>0 will be a sufficiently small universal constant. All subsequent assertions concern sufficiently large n; in particular 0<eta<1 and the off-band index set is nonempty. Define

\[
Q_\eta(M)=\sum_{|r-s|<\eta n}\langle u_ru_s^T,M\rangle u_ru_s^T,
\qquad
g_\eta=\min_{|r-s|\ge\eta n}(\lambda_r-\lambda_s)^2.
\]

These are a Frobenius-orthogonal projection and a well-defined nonnegative minimum. Put D=X-I and let J be the all-ones matrix. Spectral expansion gives

\[
\|AX-XA\|_F^2
\ge g_\eta\|(\mathrm{Id}-Q_\eta)D\|_F^2.
\]

Since <J,D>=0, orthogonality and Cauchy-Schwarz imply

\[
\langle Q_\eta(J),I-X\rangle
=\langle(\mathrm{Id}-Q_\eta)J,D\rangle,
\qquad
\|AX-XA\|_F^2
\ge g_\eta n^{-2}\langle Q_\eta(J),I-X\rangle^2. \tag{2}
\]

Here ||J||_F=n. No positivity of the last inner product has yet been assumed.

## 3. Elementary probabilistic ingredients

Write L=log n and theta=sqrt(L/n). Constants in this section may depend on a fixed desired polynomial failure exponent c, but not on n or eta.

### Gaussian and Haar facts

The GOE density is proportional to exp(-n Tr(A^2)/4), so it is invariant under orthogonal conjugation. The spectrum is simple almost surely: the repeated-eigenvalue discriminant is a nonzero polynomial and its zero set has Lebesgue measure zero. Conditional on the ordered eigenvalues, orthogonal invariance, with independent random signs assigned to eigenvectors, gives a Haar orthogonal eigenvector matrix U independent of the eigenvalues. The projection Q_eta is unchanged by those signs. A fixed orthonormal two- or three-frame transformed by a Haar matrix has the same law as Gram-Schmidt applied to two or three independent standard Gaussian vectors; this follows from the orthogonal invariance of their joint Gaussian law.

For a standard Gaussian G, E exp(tG^2)=(1-2t)^(-1/2) for t<1/2. For independent standard Gaussians G,H, E exp(tGH)=(1-t^2)^(-1/2) for |t|<1. Chernoff's argument gives, with failure O(n^{-c}), coordinate maxima O(sqrt L), Gaussian squared norms n+O(sqrt(nL)), and inner products of independent Gaussian vectors O(sqrt(nL)). We also use the conditional Gaussian tail

\[
\Pr(|T|>\sqrt{2tv}\mid\mathcal F)\le 2e^{-t}
\]

when T conditional on F is centered Gaussian with variance v. These statements apply to the independent Gaussian vectors used below.

### Moment estimate, with the local counting repair

For iid centered real variables U_a with E|U_a|^(2k)<=r_k and a fixed positive integer k, expand E(sum_a U_a)^(2k). A tuple with a singleton index has zero expectation. At most C_k n^k remaining tuples exist, and Holder bounds the absolute expectation of every product by r_k. Therefore

\[
\mathbb E\left|\sum_a U_a\right|^{2k}\le C_k r_k n^k,
\qquad
\Pr\left(\left|\sum_aU_a\right|>n^{2/3}\right)
\le C_k r_k n^{-k/3}. \tag{3}
\]

We count absolute expectations of original tuples, not a signed sum over overlapping supports. Gaussian monomials of fixed degree have all fixed moments, so k can be chosen large enough to obtain any fixed polynomial failure exponent. Applying (3) after subtracting the mean also bounds sums of noncentered monomials by their means plus O(n^(2/3)).

### Independent quadratic-form inequality

The standard independent result used here is the following form of the quadratic-form concentration inequality displayed in the source. For independent centered variables xi_a with uniformly bounded sub-exponential norms, and deterministic symmetric zero-diagonal M,

\[
\Pr(|\xi^TM\xi|\ge t)
\le 2\exp\left[-c_0\min\left\{
\frac{t^2}{\|M\|_F^2},\sqrt{\frac{t}{\|M\|_{\rm op}}}
\right\}\right]. \tag{4}
\]

The constant depends only on the common sub-exponential bound. We apply (4) only to xi_a=X_aY_a, for independent standard Gaussian vectors X,Y. These variables are independent across a, centered, and have a uniformly bounded sub-exponential norm, as follows from the product moment-generating function above.

Set M_ab=1_{a!=b, |a-b|<eta n}. Its maximum degree is at most 2eta n, so

\[
\|M\|_F^2\le2\eta n^2,
\qquad \|M\|_{\rm op}\le2\eta n.
\]

For any fixed c, taking

\[
R_n=K_c n\big(\sqrt{\eta L}+\eta L^2\big) \tag{5}
\]

makes both exponents in (4) at least a sufficiently large multiple of L. Consequently |xi^TMxi|<=R_n with failure O(n^{-c}). This is the necessary local correction to the source's threshold n eta L^2: at eta=kappa/L^4 that smaller threshold does not make the first exponent grow like L.

## 4. Uniform entry bounds for W=Q_eta(J)

We prove

\[
\max_a|W_{aa}-1|=o(1),
\qquad \max_{a\ne b}|W_{ab}|\le\tfrac12 \tag{6}
\]

with probability tending to one. Each calculation below is for a fixed entry with failure O(n^{-c}) for arbitrarily large fixed c. The Gaussian representations need only reproduce each entry's marginal distribution; they need not be coupled across different entries.

### Six banded-sum estimates

For independent standard Gaussian vectors X,Y,Z, write S for summation over a!=b and |a-b|<eta n. The following bounds hold simultaneously with failure O(n^{-c}), also after permuting X,Y,Z or exchanging a,b:

\[
\begin{array}{c|c}
\text{sum}&\text{absolute-value bound}\\ \hline
S(X_aX_bY_aZ_b)&C_c n\sqrt\eta L^2\\
S(X_a^2Y_bZ_b)&C_c\eta n^{3/2}L^2\\
S(X_aY_aX_bY_b)&R_n\\
S(X_a^2X_bY_b)&C_c\eta n^{3/2}L^2\\
S(X_a^2Y_b^2)&C_c\eta n^2\\
S(X_a^2X_b^2)&C_c\eta n^2.
\end{array} \tag{7}
\]

Here is a derivation of every row. For the first, condition on X. For each b, T_b=X_b sum_a M_ab X_aY_a is Gaussian with variance X_b^2 sum_a M_ab X_a^2. On the coordinate-max event this variance is O(eta n L^2). Conditional Gaussian tails and a union bound give max_b T_b^2=O(eta n L^3). Conditional on X,Y, sum_b T_b Z_b is Gaussian with variance O(eta n^2 L^3); one more Gaussian tail gives the first row.

For the second and fourth rows, condition respectively on X,Y and on X. The sums are Gaussian in Z and Y, respectively. Their coefficient vectors have squared norms at most C eta^2 n^3 L^3 on the coordinate-max event. The Gaussian tail supplies the extra sqrt L and gives the stated bounds.

The third row is exactly (4)-(5) with xi_a=X_aY_a, whose hypotheses were checked above.

For the final two rows, eta n grows faster than L. Chernoff's inequality for Gaussian squares, followed by a union bound over b, gives max_b sum_a M_ab X_a^2<=C eta n with failure O(n^{-c}). Also ||X||^2 and ||Y||^2 are O(n). Hence S(X_a^2Y_b^2)<=C eta n||Y||^2 and S(X_a^2X_b^2)<=C eta n||X||^2. This also avoids incorrect uniform band-degree asymptotics at the boundaries.

### Off-diagonal entries

Fix i!=j, let V=U^T and let e be the all-ones vector. The triple Ve_i, Ve_j, (Ve-Ve_i-Ve_j)/sqrt(n-2) is a Haar orthonormal three-frame. Construct it from independent standard Gaussian X,Y,Z by

\[
v=X/\alpha,
\quad v'=(Y-rv)/\beta,
\quad v''=(Z-sv-tv')/\gamma,
\]

where alpha=||X||, r=<v,Y>, beta=||Y-rv||, s=<v,Z>, t=<v',Z>, and gamma=||Z-sv-tv'||. The Gaussian estimates give

\[
\alpha,\beta,\gamma=\sqrt n(1+O(\theta)),
\qquad r,s,t=O(\sqrt L).
\]

Thus v+v'+sqrt(n-2)v''=aX+bY+dZ with a,b=O(theta), d=1+O(theta), while r/alpha=O(theta). Symmetry of the band gives the representation

\[
\alpha\beta W_{ij}
\overset{d}{=}
\sum_{|a-b|<\eta n}
X_a\big(Y_b-(r/\alpha)X_b\big)
(a_0X_a+b_0Y_a+d_0Z_a)
(a_0X_b+b_0Y_b+d_0Z_b), \tag{8}
\]

where a_0,b_0=O(theta) and d_0=1+O(theta). The subscripts distinguish coefficients from summation indices. The coefficients are random: we bound their magnitudes on the normalization event and do not condition on them to assert independence.

In the a=b terms, the leading sum is sum_a X_aY_aZ_a^2, a centered iid sum. Every other term is a fixed degree-four Gaussian monomial with a coefficient O(theta) or smaller. By (3), their total contribution after division by alpha beta is O(n^(-1/3)+theta)=o(1). In particular, noncentered terms are retained rather than incorrectly declared centered.

For a!=b, expanding (8) gives the six classes in (7) with respective largest coefficient orders

\[
1,\quad \theta,\quad \theta,\quad \theta^2,\quad \theta^2,\quad \theta^3.
\]

Terms related by vector or index exchange have the same bounds; terms of a listed class with smaller coefficients are harmless. After division by alpha beta, comparable to n, the total is bounded by a constant times

\[
\sqrt\eta L^2
+\eta L^{5/2}
+\theta(\sqrt{\eta L}+\eta L^2)
+\frac{\eta L^3}{\sqrt n}
+\eta L
+\frac{\eta L^{3/2}}{\sqrt n}.
\]

At eta=kappa/L^4 this is C_c sqrt(kappa)+o(1).

### Diagonal entries

Fix i. Use two independent Gaussian vectors X,Y to represent Ve_i=X/alpha and

\[
Ve=X/\alpha+\sqrt{n-1}(Y-rX/\alpha)/\beta.
\]

Write Ve=aX+bY, where a=O(theta), b=1+O(theta). Then

\[
\alpha^2W_{ii}\overset{d}{=}
\sum_{|a-b|<\eta n}X_aX_b
(a_0X_a+b_0Y_a)(a_0X_b+b_0Y_b). \tag{9}
\]

The same-index part consists of b_0^2 sum X_a^2Y_a^2, 2a_0b_0 sum X_a^3Y_a, and a_0^2 sum X_a^4. Equation (3), centering where necessary, gives respectively n+O(n^(2/3)), O(n^(2/3)), and 3n+O(n^(2/3)) for the three unweighted sums. Since alpha^2=n(1+O(theta)), their normalized total is 1+o(1).

For a!=b, the three classes are the third, fourth, and sixth rows of (7), with coefficient orders 1, theta, and theta^2. Their normalized total is at most

\[
C_c\big(\sqrt{\eta L}+\eta L^2+\eta L^{5/2}+\eta L\big)=o(1). \tag{10}
\]

This verifies the diagonal conclusion with the corrected quadratic-form threshold.

Finally choose, for example, c>4 throughout. A union bound over n diagonal and n(n-1) off-diagonal entries has failure o(1). Then choose the fixed universal kappa sufficiently small that C_c sqrt(kappa)<1/2 with a fixed margin. Equations (8)-(10) prove (6).

## 5. Separated eigenvalues: the remaining nonstandard input

The exact external rigidity assertion stated in the source is:

> For this GOE normalization, there exists a universal C_0 such that, with probability tending to one,
> \[
> \max_{1\le j\le n}|\lambda_j-\nu_j|
> \le r_n:=n^{-2/3}(\log n)^{C_0\log\log n},
> \]
> where nu_j is the semicircle quantile in [-2,2] satisfying integral_{-2}^{nu_j} rho_sc(x) dx=j/n and rho_sc(x)=(1/(2pi))sqrt((4-x^2)_+).

This is theory_013, retained as a nonstandard dependency. The supplied source cites it without deriving it. It is the sole unresolved derivation obligation in this reference; the following argument proves its implication, not the rigidity assertion itself.

Since rho_sc<=1/pi, every integer pair i<j satisfies nu_j-nu_i>=pi(j-i)/n. On the stated rigidity event, for j-i>=eta n,

\[
\lambda_j-\lambda_i\ge\pi\eta-2r_n.
\]

The exact error is n^(-2/3+o(1)), and

\[
\frac{r_n}{\eta}
=\kappa^{-1}n^{-2/3}(\log n)^{C_0\log\log n+4}\longrightarrow0.
\]

Thus g_eta>=(pi eta/2)^2 for all sufficiently large n. This uses actual integer pairs and requires no fractional-index eigenvalue notation.

## 6. Trace separation, recovery, and rounding

On the entrywise event (6), let E be an extreme point of either feasible polytope. For B_n, the extreme points are permutation matrices. For H_n, an extreme point cannot have two fractional entries because they could be perturbed in opposite directions; it cannot have exactly one fractional entry because the total sum is the integer n. Hence each extreme point is a zero-one matrix with exactly n ones.

Let m=n-Tr(E). There are m missing diagonal ones and m off-diagonal ones, so for all sufficiently large n,

\[
\langle W,I-E\rangle
\ge(1-o(1))m-\tfrac12m\ge m/3.
\]

Convex decomposition and linearity give, simultaneously for every X in either feasible set,

\[
\langle W,I-X\rangle\ge(n-\operatorname{Tr}X)/3. \tag{11}
\]

Combine (1), (2), (11), and the separated-gap estimate from Section 5. For every minimizer,

\[
n-\operatorname{Tr}X
\le C\sigma n^{3/2}/\eta
\le C'\sigma n^{3/2}(\log n)^4.
\]

Since X belongs to H_n,

\[
\|X-I\|_F^2
=\|X\|_F^2+n-2\operatorname{Tr}X
\le2(n-\operatorname{Tr}X).
\]

Undoing the normalization proves the requested bound with a universal constant, conditional only on the unresolved input in Section 5. The assumed deterministic noise sequence makes its right-hand side o(n). No division by sigma occurred, so sigma=0 gives exact equality X=P on the same event. The estimates hold simultaneously for both feasible sets and all minimizers, without any measurable choice of a particular optimizer.

For rounding, let p(i) be the unique column with P_{i,p(i)}=1. If a row is rounded to j!=p(i), then X_{ij}>=X_{i,p(i)}. If X_{i,p(i)}<=1/2, its planted coordinate contributes at least 1/4 to the squared row error; otherwise the coordinate j contributes more than 1/4. Thus every tie-breaking choice has at most 4||X-P||_F^2 incorrectly rounded rows, which is o(n).

## Remaining GT obligation

Provide a derivation of the precise nonstandard GOE rigidity assertion in Section 5, or another independently justified derivation of g_eta>=c eta^2 at eta=kappa/(log n)^4. Its citation alone is not recorded as completed proof. All other steps and the local source repairs are explicit above.
