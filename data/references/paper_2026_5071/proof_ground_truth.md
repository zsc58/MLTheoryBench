# Reference Proof

## Proof Structure

1. Simultaneously diagonalize the matrices, use correctly scaled momentum, and determine the mean threshold with zero initial momentum.
2. Derive the weighted coordinatewise second-moment recursion from conditional Gaussian moments.
3. Restrict spectral analysis to positive-curvature coordinates and derive the local resolvent and adjoint obstruction.
4. Characterize the coupled spectral radius through a scalar resolvent equation, including steps outside the local contractive regime.
5. Prove full-state boundedness below the root and instability from an admissible deterministic initialization above it.
6. Identify the critical supremum and prove uniqueness and both bounds.

## Complete Proof

### 1. Coordinates and mean stability

Simultaneous orthogonal diagonalization gives
\[
P=U\Sigma U^\top,\qquad H=U\Lambda U^\top,
\]
where \(\Sigma=\operatorname{diag}(\sigma_i)\), \(\sigma_i>0\), and \(\Lambda=\operatorname{diag}(h_i)\), \(h_i\ge0\). Write
\[
\lambda_i=\widetilde\lambda_i=h_i/\sigma_i,\qquad
\delta=(1-\beta)\eta,\qquad
y_t=U^\top P^{1/2}x_t,\qquad q_t=\eta U^\top P^{-1/2}m_t.
\]
In particular, \(q_0=0\). Rotate the Gaussian directions by \(U^\top\), retaining the notation \(u_t\). They remain independent standard Gaussian vectors. With
\[
B_t=\Sigma^{-1/2}u_tu_t^\top\Sigma^{1/2},\qquad
\widetilde\Lambda=\operatorname{diag}(\lambda_i),
\]
the exact update is
\[
q_{t+1}=\beta q_t+\delta B_t\widetilde\Lambda y_t,
\qquad y_{t+1}=y_t-q_{t+1}.
\]
The factors in the definition of \(q_t\) are essential: it equals the source's step-size-scaled transformed momentum, not its unscaled transformed momentum.

The state at time \(t\) is measurable with respect to the preceding Gaussian directions, so the new direction is independent of it. All finite-time moments used below exist, since the state is a finite-degree polynomial in finitely many Gaussian coordinates. Since \(\mathbb E B_t=I\), coordinate \(i\) of the mean evolves by
\[
A_i=\begin{pmatrix}1-a_i&-\beta\\a_i&\beta\end{pmatrix},
\qquad a_i=\delta\lambda_i.
\]
Its characteristic polynomial is
\[
p_i(r)=r^2-(1+\beta-a_i)r+\beta.
\]
For \(0<a_i<2(1+\beta)\), its roots lie strictly inside the unit disk. Indeed, nonreal roots have modulus \(\sqrt\beta<1\). If the roots are real and \(\beta>0\), their product is \(\beta\); a root at least one would force \(p_i(1)\le0\), contrary to \(p_i(1)=a_i>0\), and a root at most minus one would force \(p_i(-1)\le0\), contrary to \(p_i(-1)=2(1+\beta)-a_i>0\). The case \(\beta=0\) has roots zero and \(1-a_i\). At \(a_i=0\) the roots are \(1,\beta\), and at \(a_i=2(1+\beta)\) they are \(-1,-\beta\); these boundary roots are distinct because \(\beta<1\). Thus the corresponding powers are bounded throughout the closed interval.

If \(a_i>2(1+\beta)\), then \(p_i(-1)<0\), so there is a root \(r_-<-1\). It is excited by a nonzero position initialization with zero momentum. For \(\beta>0\), otherwise the ratio of the first two positions, \(1-a_i\), would be the other root, but
\[
p_i(1-a_i)=\beta a_i>0.
\]
For \(\beta=0\), the position multiplier itself is \(1-a_i<-1\). Consequently some admissible deterministic initialization has unbounded mean whenever the top mode exceeds this interval. Since \(L>0\),
\[
\eta_{\rm mean}^*=\frac{2(1+\beta)}{(1-\beta)L}.
\]

### 2. Exact second-moment recursion

For a standard Gaussian vector, independence of its coordinates and the one-dimensional second and fourth moments give
\[
\mathbb E[u_pu_iu_ju_q]
=\delta_{pi}\delta_{jq}+\delta_{pj}\delta_{iq}+\delta_{pq}\delta_{ij}.
\]
Expanding entries therefore gives
\[
\mathbb E[uu^\top Auu^\top]=A+A^\top+\operatorname{Tr}(A)I.
\]
Conjugating this identity by \(\Sigma^{-1/2}\), with the middle matrix \(\Sigma^{1/2}A\Sigma^{1/2}\), yields
\[
\mathbb E[B_tAB_t^\top]
=A+A^\top+\operatorname{Tr}(\Sigma A)\Sigma^{-1}.
\]

Define the conditionally centered innovation
\[
\xi_t=(B_t-I)\widetilde\Lambda y_t.
\]
It has conditional mean zero. Applying the preceding identity to the conditional rank-one matrix \(\widetilde\Lambda y_ty_t^\top\widetilde\Lambda\) gives
\[
\mathbb E[\xi_{i,t}^2\mid y_t,q_t]
=\lambda_i^2y_{i,t}^2+\sigma_i^{-1}\sum_j\sigma_j\lambda_j^2y_{j,t}^2.
\]
Set
\[
W_{i,t}=\mathbb E\left[\binom{y_{i,t}}{q_{i,t}}
\binom{y_{i,t}}{q_{i,t}}^\top\right],
\qquad Q=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
The state innovation is \(\delta\xi_{i,t}(-1,1)^\top\). Its cross terms with the previous state vanish conditionally. Hence
\[
W_{i,t+1}=M_i(W_{i,t})+
\delta^2\sigma_i^{-1}\ell(W_t)Q,\tag{1}
\]
where
\[
M_i(X)=A_iXA_i^\top+a_i^2X_{11}Q,
\qquad
\ell(W)=\sum_j\sigma_j\lambda_j^2(W_j)_{11}.
\]
This closes on diagonal coordinate blocks even if cross-coordinate covariances are nonzero. Furthermore,
\[
\mathbb E\|x_t\|^2=\sum_i\sigma_i^{-1}(W_{i,t})_{11}.
\]
All weights are fixed and strictly positive.

Let \(J=\{i:\lambda_i>0\}\) and \(Z=\{i:\lambda_i=0\}\). The nonempty subsystem indexed by \(J\) is autonomous in (1). All local inverse and strict spectral arguments below concern this subsystem only.

### 3. Local maps and the adjoint obstruction

We use the following audited standard finite-dimensional cone result: a linear operator preserving a closed, convex, pointed cone with nonempty interior has a nonzero cone eigenvector at its spectral radius. The cone of positive-semidefinite symmetric matrices and its finite products satisfy these hypotheses; the PSD cone is self-dual under the trace pairing. All maps used here preserve these cones by their displayed formulas, and their adjoints preserve the dual cones.

Fix \(a>0\), write
\[
A=\begin{pmatrix}1-a&-\beta\\a&\beta\end{pmatrix},
\qquad M(X)=AXA^\top+a^2X_{11}Q.
\]
First prove the scaled obstruction: if \(c>0\) and \(\rho(cM)\ge1\), no \(W\succeq0\) can satisfy
\[
(I-cM)W\succeq\alpha Q\qquad(\alpha>0).\tag{2}
\]
The cone result applied to \((cM)^*\) supplies \(V\succeq0\), \(V\ne0\), with \((cM)^*V=\rho(cM)V\). We claim \(\langle V,Q\rangle>0\). Otherwise, positivity implies \(V=k ee^\top\), where \(e=(1,1)^\top\) and \(k>0\). Since \(A^\top e=(1,0)^\top\), the adjoint formula gives
\[
(cM)^*V=ck\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
which cannot equal \(\rho(cM)k ee^\top\). Pairing (2) with \(V\) now gives
\[
0<\alpha\langle V,Q\rangle
\le(1-\rho(cM))\langle V,W\rangle\le0,
\]
a contradiction.

We next derive, rather than merely cite, the local contractivity criterion and resolvent. Put \(k=1-\beta^2\). Write \(Y=\begin{psmallmatrix}r&s\\s&t\end{psmallmatrix}\). The equation \((I-M)Y=Q\) implies
\[
2s+t=0,\qquad (1-\beta)s+t=ar,
\qquad (1-\beta^2)t=2a^2r+2a\beta s+1.
\]
The first two identities follow by adding all entries and by adding entries \((1,2)\) and \((2,2)\), respectively; the last is the \((2,2)\) equation. Solving gives
\[
r=\frac{1+\beta}{2a(k-a)},\qquad
s=-\frac1{2(k-a)},\qquad t=\frac1{k-a}.\tag{3}
\]
When \(0<a<k\), this matrix is positive definite, because \(r>0\) and
\[
\det Y=\frac{2(1+\beta)-a}{4a(k-a)^2}>0.
\]
Direct substitution verifies \((I-M)Y=Q\). If \(\rho(M)\ge1\), this contradicts (2) with \(c=\alpha=1\). Hence \(\rho(M)<1\).

Conversely, if \(\rho(M)<1\), its Neumann series gives a PSD solution \(Y=(I-M)^{-1}Q\). The same three equations imply
\[
2a(k-a)Y_{11}=1+\beta>0.
\]
Since \(a>0\) and \(Y_{11}\ge0\), necessarily \(a<k\). Therefore
\[
\rho(M_i)<1\quad\Longleftrightarrow\quad0<a_i<1-\beta^2,\tag{4}
\]
and in that regime the inverse is PSD-preserving and
\[
\big((I-M_i)^{-1}Q\big)_{11}
=\frac{1+\beta}{2a_i(1-\beta^2-a_i)}.\tag{5}
\]
No claim of invertibility at \(a_i=0\) is made.

### 4. Coupled spectral characterization

On the active subsystem define
\[
D=\operatorname{diag}(M_i)_{i\in J},\qquad
b_i=\sigma_i^{-1}Q,\qquad
T_JW=DW+\delta^2\ell(W)b.
\]
The product PSD cone is proper and is preserved by \(T_J\). Also
\[
T_Jb\succeq c_0b,\qquad c_0=\delta^2\sum_{i\in J}\lambda_i^2>0.
\]
Iteration and finite-dimensional spectral growth imply \(\rho(T_J)\ge c_0>0\). Let \(r=\rho(T_J)\), and let \(W^*\ne0\) be its PSD Perron eigenvector.

Its total first diagonal mass is positive. Otherwise \(W_i^*=t_i e_2e_2^\top\) with \(t_i\ge0\), and the eigenvector equation reads
\[
rW_i^*=\beta^2t_iQ.
\]
The first diagonal entry gives \(\beta^2t_i=0\); the second then gives \(rt_i=0\). Since \(r>0\), all blocks vanish, a contradiction. This argument includes \(\beta=0\). Because all \(\lambda_i>0\) on \(J\), it follows that \(\ell(W^*)>0\).

For every active block,
\[
(I-r^{-1}M_i)W_i^*
=\frac{\delta^2\ell(W^*)}{r\sigma_i}Q.
\]
The scaled obstruction proves \(\rho(M_i)<r\). Thus \(r>\rho(D)\), the resolvent exists, and cancellation of \(\ell(W^*)>0\) gives
\[
1=F(r),\qquad
F(s)=\delta^2\ell((sI-D)^{-1}b)
=\delta^2\sum_{i\in J}\lambda_i^2
\big((sI-M_i)^{-1}Q\big)_{11},\quad s>\rho(D).\tag{6}
\]
On this positive interval,
\[
F(s)=\delta^2\sum_{n=0}^{\infty}s^{-n-1}\ell(D^nb).
\]
Every coefficient is nonnegative, and its zeroth coefficient is strictly positive. Consequently \(F\) is continuous and strictly decreasing.

If \(\eta L<(1+\beta)\), then all active local maps are contractive by (4). Using (5),
\[
F(1)=\delta^2\sum_{i\in J}\lambda_i^2
\frac{1+\beta}{2\delta\lambda_i(1-\beta^2-\delta\lambda_i)}
=\sum_i\frac{\eta\lambda_i}{2(1-\eta\lambda_i/(1+\beta))}
=:S(\eta).\tag{7}
\]
The terms with \(i\in Z\) are zero. Comparing \(F(r)=1\) with \(F(1)\) shows
\[
r<1,\ r=1,\ r>1
\quad\text{according as}\quad S(\eta)<1,\ S(\eta)=1,\ S(\eta)>1.
\]
If instead \(\eta L\ge1+\beta\), (4) gives \(\rho(D)\ge1\), whereas the scaled obstruction already proved \(r>\rho(D)\). Thus \(r>1\) throughout this entire remaining step-size regime. This supplies the necessary strict-instability conclusion outside the resolvent domain at one.

### 5. Relating the operator to the stated initialization experiment

Suppose \(r<1\). Finite-dimensional matrix powers, for example by Jordan form, give constants \(C<\infty\) and \(\theta\in(0,1)\) such that the active covariance blocks have norm at most \(C\theta^t\) times their initial norm. Hence
\[
\sum_{t=0}^{\infty}\ell(W_t)<\infty.
\]
For each \(i\in Z\), (1) becomes
\[
W_{i,t+1}=A_0W_{i,t}A_0^\top+
\delta^2\sigma_i^{-1}\ell(W_t)Q,
\qquad A_0=\begin{pmatrix}1&-\beta\\0&\beta\end{pmatrix}.
\]
Its powers are
\[
A_0^t=\begin{pmatrix}
1&-\beta(1-\beta^t)/(1-\beta)\\0&\beta^t
\end{pmatrix},
\]
and are uniformly bounded. Unrolling the recursion gives
\[
W_{i,t}=A_0^tW_{i,0}(A_0^\top)^t+
\delta^2\sigma_i^{-1}\sum_{j=0}^{t-1}
\ell(W_j)A_0^{t-1-j}Q(A_0^\top)^{t-1-j}.
\]
The summable forcing and bounded powers make this uniformly bounded. Thus all position second moments are bounded for every allowed deterministic initialization.

Now suppose \(r>1\). We must exhibit instability with \(m_0=0\); an arbitrary mixture of full position-momentum states is not an admissible substitute. Choose a deterministic \(y_0\) with at least one nonzero active coordinate, and set \(q_0=0\). Then \(\ell(W_0)>0\), and positivity of (1) gives, on \(J\),
\[
W_1\succeq c_1 b,\qquad
W_2\succeq c_1 T_Jb,\qquad c_1=\delta^2\ell(W_0)>0.
\]
For \(v=(1,-1)^\top\), \(Q=vv^\top\), and
\[
A_iv=(1-a_i+\beta,a_i-\beta)^\top,\qquad
\det[v,A_iv]=1.
\]
Moreover,
\[
(T_Jb)_i
=\sigma_i^{-1}\left[A_iQA_i^\top+
\delta^2\left(\lambda_i^2+\sum_{j\in J}\lambda_j^2\right)Q\right].
\]
The two rank-one directions are independent and the coefficient of \(Q\) is positive, so every active block is positive definite. Since there are finitely many blocks, some \(\varepsilon>0\) satisfies
\[
W_2\succeq\varepsilon W^*.
\]
Positivity and the Perron equation then imply
\[
W_{t,J}\succeq\varepsilon r^{t-2}W^*,\qquad t\ge2.
\]
The Perron eigenvector has positive position mass and the weights \(\sigma_i^{-1}\) are positive. Therefore \(\mathbb E\|x_t\|^2\) is unbounded for this deterministic zero-momentum initialization. The use of two iterations is essential to the repaired domination argument: rank-one \(b\) itself need not dominate \(W^*\).

### 6. Critical supremum, uniqueness, and bounds

On \((0,(1+\beta)/L)\), the function \(S\) in (7) is continuous and strictly increasing, because the spectrum has at least one positive eigenvalue. It extends to \(S(0)=0\) and tends to infinity at the right endpoint. Thus there is a unique \(\eta_c\) in that interval with \(S(\eta_c)=1\).

The preceding arguments prove stability for every \(0<\eta<\eta_c\) and failure for every \(\eta>\eta_c\), including all steps outside the interval. Hence the supremum in the problem is exactly \(\eta_{\rm ms}^*=\eta_c\). No assertion about boundedness at equality is needed.

At this root,
\[
1=S(\eta_c)\ge\frac{\eta_c\tau}{2},
\]
which proves \(\eta_c\le2/\tau\). Also,
\[
1=S(\eta_c)
\le\frac{\eta_c\tau}{2(1-\eta_cL/(1+\beta))}.
\]
The denominator is positive, and rearrangement gives
\[
\eta_c\ge\frac{2}{\tau+2L/(1+\beta)}.
\]
This proves all requested claims.

## Obligation Closure

The proof explicitly derives the normalized dynamics, conditional Gaussian covariance closure, local contractivity and inverse formula, scaled adjoint obstruction, coupled spectral comparisons, nullspace boundedness, and instability from a deterministic zero-momentum initialization. It also proves mean-mode excitation, uniqueness, the supremum characterization, and both bounds. The only specialized external result used without proof is the stated finite-dimensional cone Perron theorem; its hypotheses are verified for each application. No unresolved proof obligation remains.
