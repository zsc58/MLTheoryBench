# Reference Proof

## Proof Structure and Obligations

1. Derive the exact Gaussian covariance recursion and identify its positive trace-noise submap.
2. Prove positive-operator spectral domination, construct the trace-coupled eigenmode, and obtain the batch-dependent step-size cap.
3. Establish the deterministic stability restriction and root-gap bounds, distinguishing a coordinate-block radius from the global radius.
4. Eliminate the parameters uniformly, include noncontracting choices, and calculate the real crossover of the two terms.

All four obligations are closed below. The standard external ingredients are the Gaussian fourth-moment identity, finite-dimensional Perron--Frobenius for a proper cone, and the real quadratic Schur criterion. Their relevant statements and hypotheses are given where used. The finite-dimensional spectral-radius formula used in the source's domination proof is also stated explicitly.

## 1. Exact Covariance Recursion

Write
\[
 c=\gamma(1-\mu),\qquad
 A=M(G),\qquad
 \mathcal L(S)=ASA^\top.
\]
All matrices supplied as inputs to these operators are deterministic real symmetric matrices. Gaussian fourth moments are finite, so the operators are well-defined on the finite-dimensional space of symmetric \(2d\)-by-\(2d\) matrices.

For a centered Gaussian vector with covariance \(G\), the fourth-moment formula is
\[
 \mathbb E[x_a x_b x_c x_d]
 =G_{ab}G_{cd}+G_{ac}G_{bd}+G_{ad}G_{bc}.
\]
Consequently, for every deterministic symmetric \(U\),
\[
 \mathbb E[xx^\top Uxx^\top]
 =2GUG+\operatorname{tr}(GU)G.
\]
In the minibatch expansion, the \(m\) same-sample terms have this expectation, while the \(m(m-1)\) different-sample terms have expectation \(GUG\), by independence. Thus
\[
 \mathbb E[\bar XU\bar X]
 =\left(1+\frac1m\right)GUG
  +\frac1m\operatorname{tr}(GU)G,
\]
and, since \(\mathbb E\bar X=G\),
\[
 \mathbb E[(\bar X-G)U(\bar X-G)]
 =\frac1m\left(GUG+\operatorname{tr}(GU)G\right).
\]
Expanding \(M(\bar X)=A+\begin{psmallmatrix}-c(\bar X-G)&0\\0&0\end{psmallmatrix}\), the mixed terms vanish. Hence the exact operator is
\[
 \mathcal T(S)=\mathcal L(S)+
 \begin{pmatrix}
 \dfrac{c^2}{m}\left(GS_{11}G+\operatorname{tr}(GS_{11})G\right)&0\\
 0&0
 \end{pmatrix}. \tag{1}
\]
For \(S\succeq0\), its principal block \(S_{11}\) is PSD, so both noise summands are PSD. Define
\[
 D=\begin{pmatrix}G&0\\0&0\end{pmatrix},\qquad
 h(S)=\operatorname{tr}(GS_{11}),\qquad
 \alpha=\frac{c^2}{m},\qquad
 \mathcal T_0(S)=\mathcal L(S)+\alpha h(S)D.
\]
These are positive maps, and their order on PSD inputs satisfies
\[
 0\le\mathcal L\le\mathcal T_0\le\mathcal T. \tag{2}
\]
The trace-only map is used as a lower comparison map, not as an equality replacement for the exact stochastic operator.

## 2. Spectral Comparison and the Stochastic Cap

### Positive-map comparison

The standard finite-dimensional cone Perron--Frobenius theorem states that a linear map preserving a proper cone has a nonzero cone-valued eigenvector at its nonnegative spectral radius. Here the PSD cone in the real symmetric matrices is closed, convex, pointed, and has nonempty interior, and it generates the ambient space. Thus the theorem applies to each positive map used here; irreducibility is not required.

If positive maps \(\mathcal P\le\mathcal Q\) act on this space, take \(W\succeq0\), \(W\ne0\), with \(\mathcal P(W)=\rho(\mathcal P)W\). Positivity and induction give
\[
 \mathcal Q^n(W)\succeq\rho(\mathcal P)^n W.
\]
The matrix spectral norm is monotone on PSD matrices. Therefore the induced operator norm satisfies \(\|\mathcal Q^n\|\ge\rho(\mathcal P)^n\). The finite-dimensional spectral-radius formula, valid for every linear map \(K\) and every induced norm,
\[
 \rho(K)=\lim_{n\to\infty}\|K^n\|^{1/n},
\]
then yields \(\rho(\mathcal P)\le\rho(\mathcal Q)\).

For the deterministic congruence map, \(\mathcal L^n(S)=A^nS(A^n)^\top\). Its induced norm on symmetric matrices equipped with the spectral norm is exactly \(\|A^n\|_2^2\): the upper bound follows by submultiplicativity, and equality follows by taking \(S=I\). Applying the same spectral-radius formula gives
\[
 \rho(\mathcal L)=\rho(A)^2.
\]
Thus (2) implies
\[
 \rho(A)^2=\rho(\mathcal L)
 \le\rho(\mathcal T_0)\le\rho(\mathcal T). \tag{3}
\]
This argument is on the full symmetric-matrix space and does not assume that every eigenmode is trace-observable.

For now suppose \(\rho(\mathcal T)<1\). Then \(\rho(A)<1\) and \(\rho(\mathcal T_0)<1\).

### Trace-mode construction

Rotate by the lifted orthogonal change of basis \(\operatorname{diag}(Q,Q)\), where \(Q\) diagonalizes \(G\), and then permute coordinates to group each pair \((e_i,e_{i,\mathrm{previous}})\). The deterministic matrix becomes block diagonal with
\[
 A_i=\begin{pmatrix}a_i&-\mu\\1&0\end{pmatrix},\qquad
 a_i=1+\mu-c\lambda_i.
\]
In this ordering, \(D\) has diagonal blocks \(\lambda_i E_{11}\), where \(E_{11}=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}\). Define \(\mathcal L_i(P)=A_iPA_i^\top\).

For every real \(s\ge1\), the resolvent exists and has the convergent positive expansion
\[
 (sI-\mathcal L)^{-1}
 =\sum_{k=0}^{\infty}s^{-k-1}\mathcal L^k,
\]
because \(\rho(\mathcal L)<1\). Set
\[
 W(s)=(sI-\mathcal L)^{-1}D,\qquad
 u_i(s)=\left[(sI-\mathcal L_i)^{-1}(E_{11})\right]_{11},
\]
\[
 F(s)=\alpha h(W(s))
 =\frac{c^2}{m}\sum_{i=1}^d\lambda_i^2u_i(s).
\]
The matrix \(W(s)\) is nonzero and PSD, and is block diagonal in the coordinate ordering just described. If \(F(s)=1\), then
\[
 \mathcal T_0(W(s))
 =\mathcal L(W(s))+\alpha h(W(s))D
 =sW(s)-D+D=sW(s).
\]
Thus a root of \(F(s)=1\) in this range is an actual eigenvalue of the positive comparison map on symmetric matrices. Conversely, if \(\mathcal T_0(V)=sV\) with \(s\ge1\) and \(V\ne0\), invertibility of \(sI-\mathcal L\) gives
\[
 V=\alpha h(V)W(s).
\]
Here \(h(V)\ne0\), since otherwise \(V=0\); applying \(h\) gives \(F(s)=1\).

The resolvent representation makes \(F\) continuous on \([1,\infty)\), with \(F(s)\to0\) as \(s\to\infty\). If \(F(1)>1\), the intermediate value theorem gives a root at some \(s>1\), contradicting (3) and strict stability. Hence
\[
 F(1)\le1. \tag{4}
\]
No diagonalizability assumption, assertion about real positive poles, or identification of the global leading eigenmode is needed.

### Evaluating the resolvent

Solve \((I-\mathcal L_i)P=qE_{11}\) with \(P=\begin{psmallmatrix}u&v\\v&w\end{psmallmatrix}\). The lower-right and off-diagonal equations give
\[
 w=u,\qquad v=\frac{a_i u}{1+\mu}.
\]
The upper-left equation consequently gives
\[
 u=\frac{1+\mu}
 {(1-\mu)c\lambda_i\,[2(1+\mu)-c\lambda_i]}q.
\]
For \(q=1\), the positive resolvent series gives \(u_i(1)>0\), so the displayed denominator is positive. Substitution in (4) yields
\[
 1\ge F(1)
 =\frac{\gamma(1+\mu)}{m}
 \sum_i\frac{\lambda_i}
 {2(1+\mu)-\gamma(1-\mu)\lambda_i}
 \ge\frac{\gamma\operatorname{tr}(G)}{2m}.
\]
Therefore
\[
 \gamma\le\frac{2m}{\operatorname{tr}(G)}. \tag{5}
\]

### Weak-stability convention in the supporting source lemma

The final target needs (5) only when \(\rho(\mathcal T)<1\). The source also states the cap under \(\rho(\mathcal T)\le1\); that endpoint has a routine completion. Under this weaker hypothesis, (3) gives \(\rho(A)\le1\). A coordinate block can have a unit-modulus root only at \(-1\): nonreal unit roots would have product \(1\), contrary to \(\mu<1\), and the characteristic polynomial at \(+1\) equals \(c\lambda_i>0\). A root \(-1\) requires \(a_i=-(1+\mu)\), with other root \(-\mu\). The two-root recurrence then gives
\[
 (A_i^k)_{11}=(-1)^k\frac{1-\mu^{k+1}}{1-\mu},
 \qquad |(A_i^k)_{11}|\ge1.
\]
For \(s>1\), its resolvent therefore satisfies
\[
 u_i(s)=\sum_{k=0}^{\infty}s^{-k-1}|(A_i^k)_{11}|^2
 \ge\frac1{s-1}.
\]
Consequently \(F(s)\to\infty\) as \(s\downarrow1\), while \(F(s)\to0\) as \(s\to\infty\). The same eigenmatrix construction would give an eigenvalue greater than one, contradicting weak stability. Thus even under \(\rho(\mathcal T)\le1\), the deterministic map is strictly stable. The preceding argument gives \(F(1)\le1\) and (5), without discarding the source lemma's boundary.

## 3. Deterministic Stability and the Root Gap

For a real polynomial \(r^2+pr+q\), the quadratic Schur criterion places both roots in the open unit disk exactly when
\[
 |q|<1,\qquad 1+p+q>0,\qquad 1-p+q>0.
\]
The additional condition \(1-q>0\) in the source's formulation is redundant with \(|q|<1\). Here \(p=-a_i\), \(q=\mu\), with real coefficients and \(0\le\mu<1\). The two remaining inequalities become
\[
 c\lambda_i>0,\qquad 2(1+\mu)-c\lambda_i>0.
\]
Thus strict deterministic stability is equivalent to
\[
 0<\gamma<\frac{2(1+\mu)}{(1-\mu)\lambda_1}. \tag{6}
\]
In particular, every strictly contracting stochastic choice satisfies (6).

Let \(R=\rho(A)\). From (3),
\[
 1-\rho(\mathcal T)\le1-R^2.
\]
Each coordinate block has root product \(\mu\), so \(R^2\ge\mu\) and
\[
 1-R^2\le1-\mu. \tag{7}
\]
To obtain the other bound, use the block for \(\lambda_d\), and put \(t=\gamma\lambda_d\), \(\delta=1-\mu\). Its root sum is \(a_d=1+\mu-\delta t\).

If the roots are nonreal, their moduli equal \(\sqrt\mu\). This gives \(R^2\ge\mu\), not necessarily equality for the global radius. The discriminant condition implies
\[
 \delta t>(1-\sqrt\mu)^2.
\]
Only this implication is needed; the reverse implication alone would not characterize nonreal roots. It follows that
\[
 1-R^2\le1-\mu
 <(1+\sqrt\mu)^2t\le4t.
\]

If the roots are real and \(a_d\ge0\), including a zero discriminant, their nonnegative product and sum imply \(0\le r_-\le r_+<1\). Moreover \(r_-\le\sqrt\mu\), and evaluation of the characteristic polynomial at one gives
\[
 (1-r_+)(1-r_-)=\delta t.
\]
Therefore
\[
 1-r_+=\frac{\delta t}{1-r_-}
 \le\frac{\delta t}{1-\sqrt\mu}
 =(1+\sqrt\mu)t\le2t.
\]
Since \(R\ge r_+\),
\[
 1-R^2\le1-r_+^2\le2(1-r_+)\le4t.
\]
This includes \(\mu=0\) and the repeated zero root.

If the roots are real and \(a_d<0\), then
\[
 t>\frac{1+\mu}{1-\mu}\ge1,
\]
so \(1-R^2\le1\le4t\). These cases exhaust the possibilities, and hence
\[
 1-\rho(\mathcal T)
 \le\min\{4\gamma\lambda_d,\,1-\mu\}. \tag{8}
\]

## 4. Uniform Parameter Elimination and the Crossover

Combining (5) and (8) gives
\[
 1-\rho(\mathcal T)
 \le\frac{8m\lambda_d}{\operatorname{tr}(G)}. \tag{9}
\]
Combining (6) and (8), and writing \(q=\lambda_d/\lambda_1\), gives
\[
 1-\rho(\mathcal T)
 \le\min\left\{\frac{8(1+\mu)q}{\delta},\delta\right\}
 \le\sqrt{8(1+\mu)q}
 \le4\sqrt q. \tag{10}
\]
The middle inequality is simply \(\min\{x,y\}\le\sqrt{xy}\) for positive \(x,y\). It is uniform over the entire parameter range and does not assume the existence of a crossing inside \([0,1)\). In particular it covers \(d=1\) and \(\lambda_d=\lambda_1\).

Equations (9)--(10) imply
\[
 1-\rho(\mathcal T)
 \le\min\left\{\frac{8m\lambda_d}{\operatorname{tr}(G)},\,4\sqrt{\frac{\lambda_d}{\lambda_1}}\right\}
 \le8\min\left\{\frac{m\lambda_d}{\operatorname{tr}(G)},\,\sqrt{\frac{\lambda_d}{\lambda_1}}\right\}.
\]
We proved this for \(\rho(\mathcal T)<1\). If \(\rho(\mathcal T)\ge1\), the required lower bound on \(\rho(\mathcal T)\) is immediate. Thus it holds for every admissible parameter pair. Taking the infimum over \(\gamma>0\), \(\mu\in[0,1)\), without assuming that the infimum is attained, proves
\[
 s_\star(G,m)\ge
 1-8\min\left\{\frac{m\lambda_d}{\operatorname{tr}(G)},\sqrt{\frac{\lambda_d}{\lambda_1}}\right\}.
\]
Finally, equating the two expressions gives their positive real crossover
\[
 \frac{m\lambda_d}{\operatorname{tr}(G)}
 =\sqrt{\frac{\lambda_d}{\lambda_1}}
 \quad\Longleftrightarrow\quad
 m=\frac{\operatorname{tr}(G)}{\sqrt{\lambda_1\lambda_d}}
 =\frac{\operatorname{tr}(G)\sqrt\kappa}{\lambda_1}.
\]
This is an algebraic crossover of the two bound terms. It does not assert that the crossover is always an integer, that an optimizer is attained, or that the lower bound establishes an achievable runtime. An admissible integer minibatch has exact equality of the terms precisely when it equals this real crossover.
