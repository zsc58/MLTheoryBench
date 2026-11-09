# Reference Proof

## Contract and obligations

All distributions and information quantities below are conditional on the realized previous data and the fixed kernel parameters. There are \(n=t-1\) training coalitions. The calculation concerns one candidate and includes the preprocessing needed for that candidate; it does not include learning hyperparameters, evaluating the value function, or searching over all candidates. Complexity is an arithmetic-operation count, not a bit-complexity or numerical-stability guarantee.

The five obligations are: (1) establish nondegeneracy and the Gaussian information identity; (2) derive the scalar acquisition and its domain; (3) explicitly compute the projected kernel vector; (4) explicitly compute the projected kernel matrix, including the diagonal and the excluded-player updates; and (5) assemble the GP quantities within the claimed cost. Each is derived below.

## Step 001: nondegeneracy and Gaussian information

Put \(N=2^p\), \(K_0=K(Z,Z)\), and \(\beta_r=\exp(-\ell_r^{-2})\). Finite positive lengthscales imply \(0<\beta_r<1\). In a lexicographic coalition ordering, \(K_0\) is the tensor product of the matrices
\[
\begin{pmatrix}1&\beta_r\\\beta_r&1\end{pmatrix}.
\]
Each factor has eigenvalues \(1+\beta_r\) and \(1-\beta_r\), both positive. Tensor products of their eigenvectors give a basis with positive product eigenvalues. An arbitrary coalition ordering only permutes rows and columns, so \(K_0\) is positive definite.

Let \(E\in\mathbb R^{n\times N}\) select the training coordinates. Completing the square in the Gaussian prior density times the independent Gaussian observation likelihood gives posterior precision
\[
\Sigma^{-1}=K_0^{-1}+\sigma_\epsilon^{-2}E^\top E.
\]
This is positive definite, and its inverse is the covariance displayed in the problem. Thus \(\Sigma\) is positive definite; positive observation noise does not by itself suffice for an arbitrary singular prior, which is why the kernel check above is included.

The Shapley operator has full row rank. Indeed, for each player \(r\), consider the vector of coalition values \(g_r(S)=\mathbf 1[r\in S]\). Its marginal contribution for player \(j\) is \(\mathbf 1[j=r]\), independently of the preceding coalition. The weights sum to
\[
\sum_{m=0}^{p-1}\binom{p-1}{m}\frac{1}{p\binom{p-1}{m}}=1.
\]
Hence \(Ag_r\) is the \(r\)-th standard basis vector. In particular, \(M=A\Sigma A^\top\) is positive definite.

For a positive-definite \(q\)-dimensional Gaussian covariance \(C\), direct expectation of the log Gaussian density gives
\[
h(N(m,C))=\frac q2\log(2\pi)+\frac12\log\det C+\frac12\operatorname{tr}(C^{-1}C)
=\frac12\log\bigl((2\pi e)^q\det C\bigr).
\]
This explicitly establishes the standard-independent Gaussian entropy identity used here. The goal vector is Gaussian with covariance \(M\). Updating with the independent scalar observation gives
\[
\Sigma_y=(\Sigma^{-1}+\sigma_\epsilon^{-2}e_i e_i^\top)^{-1}
=\Sigma-\frac{\Sigma e_i e_i^\top\Sigma}{\sigma_\epsilon^2+e_i^\top\Sigma e_i}.
\]
The last equality is the rank-one inverse identity; all its inverses and its denominator exist by positive definiteness and positive noise. This conditional covariance is independent of the observed numerical value. It is positive definite, so \(M_y=A\Sigma_yA^\top\) is also positive definite. Consequently the entropy expectation is finite and
\[
\mathcal I_i=\frac12\bigl(\log\det M-\log\det M_y\bigr).
\]
Thus the relevant goal-oriented Gaussian information identity is derived, not left as an unaudited specialized citation.

## Step 002: scalar acquisition and logarithm domains

Write
\[
v=A\Sigma e_i,\qquad d=\sigma_\epsilon^2+e_i^\top\Sigma e_i,\qquad q_i=v^\top M^{-1}v.
\]
Then \(M_y=M-vv^\top/d\). The determinant identity \(\det(M+ab^\top)=\det(M)(1+b^\top M^{-1}a)\) gives
\[
\det M_y=\det M\left(1-\frac{q_i}{d}\right).
\]
Moreover, the variance of \(e_i^\top\vartheta-v^\top M^{-1}\phi\), under the current posterior, is \(e_i^\top\Sigma e_i-q_i\), and is nonnegative. Thus
\[
q_i\ge0,\qquad d-q_i\ge\sigma_\epsilon^2>0.
\]
Both logarithms are therefore well defined, and
\[
\mathcal I_i=\frac12\{\log d-\log(d-q_i)\}.
\]
Since \(q_i=e_i^\top Qe_i\), this proves the requested expression. In fact, with natural logarithms the scaling is exactly \(1/2\) and no additive constant is needed. Constants introduced by the intermediate negative-log-determinant expression are independent of the candidate.

## Step 003: projected kernel vector in quadratic time

Define the finite weight sequence
\[
w(m)=\begin{cases}[p\binom{p-1}{m}]^{-1},&0\le m\le p-1,\\0,&\text{otherwise}.
\end{cases}
\]
It can be formed in \(O(p)\) arithmetic operations using the binomial recurrence starting at \(\binom{p-1}{0}=1\).

Fix any binary vector \(z\), including a training vector when needed later. Define the coordinate factors without applying the vector kernel to scalars:
\[
(\gamma_r,\delta_r)=\begin{cases}(1,\beta_r),&z_r=0,\\(\beta_r,1),&z_r=1.
\end{cases}
\]
Then
\[
k(1_S,z)=\prod_{r\notin S}\gamma_r\prod_{r\in S}\delta_r.
\]
Let
\[
P_z(u)=\prod_{r=1}^p(\gamma_r+\delta_r u)=\sum_{m=0}^p c_m u^m.
\]
Expanding by one choice per factor proves that \(c_m\) is the sum of kernel values over coalitions of size \(m\). Initialize \(c^{(0)}_0=1\), with other coefficients zero, and update
\[
c^{(r)}_m=\gamma_r c^{(r-1)}_m+\delta_r c^{(r-1)}_{m-1}.
\]
All out-of-range coefficients are zero. There are \(O(p^2)\) coefficient updates.

For player \(j\), let
\[
P_{z,-j}(u)=\frac{P_z(u)}{\gamma_j+\delta_j u}=\sum_{m=0}^{p-1} d^{(j)}_m u^m.
\]
Because \(\gamma_j>0\), its coefficients are recovered by
\[
d^{(j)}_0=c_0/\gamma_j,\qquad d^{(j)}_m=(c_m-\delta_jd^{(j)}_{m-1})/\gamma_j\quad(1\le m\le p-1).
\]
This takes \(O(p)\) per player. The generating polynomial for coalitions containing \(j\) is \(\delta_j uP_{z,-j}(u)\), not \(\delta_jP_{z,-j}(u)\). Thus their size-\(k\) sum is \(\delta_jd^{(j)}_{k-1}\); the size-\(k\) sum for coalitions excluding \(j\) is \(\gamma_jd^{(j)}_k\). This includes the empty and full coalition endpoints with zero extension.

Inserting these identities into the Shapley sum gives
\[
(AK(Z,z))_j=\sum_{m=0}^{p-1}w(m)(\delta_j-\gamma_j)d^{(j)}_m.
\]
Computing all quotients and assembling all weighted sums takes \(O(p^2)\), proving the projected-vector bound. This corrects the degree-shift omission in the previous reference proof; the source itself supplies the correct shift.

## Step 004: projected kernel matrix in quartic time

Write \(B_0=AK(Z,Z)A^\top\). Use formal variables \(u,v\), and put
\[
f_r(u,v)=1+\beta_r u+\beta_r v+uv.
\]
Its four monomials correspond respectively to player \(r\) lying in neither coalition, only the first, only the second, or both. Therefore the coefficient of \(u^a v^b\) in \(\prod_r f_r\) sums the kernel over all coalition pairs with sizes \((a,b)\).

For membership indicators \(\eta,\zeta\in\{0,1\}\), define the restricted factors
\[
s_r^0=1+\beta_r v,\quad s_r^1=u(\beta_r+v),\qquad
 t_r^0=1+\beta_r u,\quad t_r^1=v(\beta_r+u).
\]
For distinct players \(r,s\), let
\[
H_{rs}=\prod_{q\notin\{r,s\}}f_q,\qquad F_{rs}^{\eta\zeta}=H_{rs}s_r^\eta t_s^\zeta.
\]
The coefficient of \(u^a v^b\) in this polynomial is precisely the kernel sum for coalition pairs of sizes \((a,b)\) with \(\mathbf 1[r\in S]=\eta\) and \(\mathbf 1[s\in T]=\zeta\).

For coincident players, let \(H_r=\prod_{q\ne r}f_q\) and use the single restricted factor
\[
d_r^{00}=1,\quad d_r^{10}=\beta_r u,\quad d_r^{01}=\beta_r v,\quad d_r^{11}=uv,
\qquad F_{rr}^{\eta\zeta}=H_r d_r^{\eta\zeta}.
\]
This explicitly covers the diagonal rather than treating it as a distinct-player formula.

Define \(a_\eta(m)=(2\eta-1)w(m-\eta)\). The coefficient of a coalition \(S\) in Shapley row \(r\) is \(a_{\mathbf 1[r\in S]}(|S|)\). Hence, for both cases,
\[
(B_0)_{rs}=\sum_{\eta,\zeta\in\{0,1\}}\sum_{a,b=0}^p
 a_\eta(a)a_\zeta(b)[u^av^b]F_{rs}^{\eta\zeta}.
\]
This is exactly the four membership cases with their signs and size weights.

Expand the restricted local product as \(\sum_{h,k}\lambda_{hk}u^hv^k\). It has at most four monomials for each off-diagonal membership case and one for each diagonal case. A monomial contributes
\[
\lambda_{hk}\sum_{a,b=0}^{p-1}W_{\eta,h}(a)[u^av^b]H\,W_{\zeta,k}(b),
\qquad W_{\eta,h}(a)=a_\eta(a+h),
\]
where \(H=H_{rs}\) or \(H_r\). All weight arrays are extended by zero outside \(0,\ldots,p-1\). For the monomials that actually occur, \(h-\eta\) and \(k-\zeta\) belong to \(\{0,1\}\); consequently the needed arrays belong to the fixed collection \(w(a),-w(a),w(a+1),-w(a+1)\). There are at most sixteen bilinear contributions per off-diagonal entry and four per diagonal entry. The coefficient table of \(H_{rs}\), of degrees at most \(p-2\), is zero-padded to the same \(p\)-by-\(p\) index range as \(H_r\). In particular, this construction never forms a reciprocal of an out-of-range binomial coefficient.

It remains to compute these bilinear forms at the asserted cost. Fix the excluded player \(r\). For \(j=1,\ldots,p\), define
\[
\Pi_j(u,v)=\prod_{q<j,\ q\ne r}f_q(u,v),
\]
and for \(j=0,\ldots,p\), define
\[
\Lambda_j(u,v)=\prod_{q>j,\ q\ne r}f_q(u,v).
\]
For \(j\ne r\), \(H_{rj}=\Pi_j\Lambda_j\), while \(H_r=\Lambda_0\) and \(\Pi_1=1\).

For each of the finitely many left and right weight arrays \(W,V\), set, for \(0\le a,b\le p-1\),
\[
L_j^W(a,b)=\sum_{h=0}^{p-1-a}W(h+a)[u^hv^b]\Pi_j,
\]
\[
R_j^V(a,b)=\sum_{k=0}^{p-1-b}V(b+k)[u^av^k]\Lambda_j.
\]
Expanding the coefficient convolution of \(\Pi_j\Lambda_j\) and regrouping its finite sums yields
\[
\sum_{c,d=0}^{p-1}W(c)[u^cv^d]H_{rj}\,V(d)
=\sum_{a,b=0}^{p-1}L_j^W(a,b)R_j^V(a,b)\qquad(j\ne r).
\]
Indeed, the prefix contributes exponents \((h,b)\), the suffix contributes \((a,k)\), and the two weights are \(W(h+a)\) and \(V(b+k)\). Zero extension implements exactly the range restrictions. For the diagonal the same argument, using \(\Pi_1=1\) and \(H_r=\Lambda_0\), gives
\[
\sum_{c,d=0}^{p-1}W(c)[u^cv^d]H_r\,V(d)
=\sum_{a,b=0}^{p-1}L_1^W(a,b)R_0^V(a,b).
\]

The initial tables are explicit:
\[
L_1^W(a,b)=W(a)\mathbf 1[b=0],\qquad R_p^V(a,b)=V(b)\mathbf 1[a=0].
\]
All table entries with out-of-range indices are zero. When \(j-1\ne r\), multiplying the prefix by \(f_{j-1}\) and reindexing the contraction gives
\[
L_j^W(a,b)=L_{j-1}^W(a,b)+\beta_{j-1}L_{j-1}^W(a+1,b)
+\beta_{j-1}L_{j-1}^W(a,b-1)+L_{j-1}^W(a+1,b-1).
\]
When \(j-1=r\), the correct update is instead
\[
L_j^W=L_{j-1}^W.
\]
Likewise, for \(j=p-1,\ldots,0\), when \(j+1\ne r\),
\[
R_j^V(a,b)=R_{j+1}^V(a,b)+\beta_{j+1}R_{j+1}^V(a-1,b)
+\beta_{j+1}R_{j+1}^V(a,b+1)+R_{j+1}^V(a-1,b+1),
\]
and when \(j+1=r\),
\[
R_j^V=R_{j+1}^V.
\]
These equations follow directly from the four monomials of \(f_q\), with the copy cases forced by exclusion of \(r\). They preserve the displayed definitions of the contracted tables by induction, including their boundary entries.

For each fixed \(r\), build and store the backward tables for all right weights and sweep the forward tables for all left weights. There are \(O(p)\) stages, a constant number of \(p\)-by-\(p\) tables per stage, and constant work per table entry. This costs \(O(p^3)\). At each player \(j\ne r\), the bounded number of contractions needed for \((B_0)_{rj}\) costs \(O(p^2)\); their total is another \(O(p^3)\). The diagonal contractions cost \(O(p^2)\). Repeating for all \(p\) excluded players gives \(O(p^4)\) time. Empty products are initialized as 1, so the \(p=2\) off-diagonal boundary is covered. There is no admissible integer \(t\) when \(p=1\), although the single-player formulas themselves are also well defined.

Source-local repair: the source's general recurrences at L001377–L001411 omit the two copy cases, despite excluding the fixed player in their polynomial definitions at L001305–L001322. The copy cases are the unique local correction of that omission; they require no new assumption or algorithmic mechanism and do not change the operation count. The previous reference proof's unspecified reference to prefix/suffix recurrences is replaced here by the complete construction.

## Step 005: GP assembly and total cost

Let
\[
C=K(X,X)+\sigma_\epsilon^2I_n,\quad B=AK(Z,X),\quad b=AK(Z,z_i),\quad k_i=K(X,z_i).
\]
The projected-vector algorithm applies to every training column as well as to the unobserved candidate; its derivation only requires a binary input vector. Therefore \(B\) and \(b\) cost \(O(np^2+p^2)\). The matrix \(B_0\) costs \(O(p^4)\) by Step 004.

Forming the training kernel costs \(O(n^2p)\), including the coordinatewise products, and forming \(k_i\) costs \(O(np)\). A Cholesky factorization of \(C\) costs \(O(n^3)\). The same factor is reused in
\[
d=\sigma_\epsilon^2+1-k_i^\top C^{-1}k_i,
\]
\[
v=b-BC^{-1}k_i,
\qquad M=B_0-BC^{-1}B^\top.
\]
These are the GP posterior covariance identities from the problem after projection; \(k(z_i,z_i)=1\). The single right-hand-side solve costs \(O(n^2)\), the matrix-vector product costs \(O(np)\), the solve with \(p\) right-hand sides costs \(O(n^2p)\), and the resulting matrix product costs \(O(np^2)\). Factoring the positive-definite \(M\), solving against \(v\), and taking the dot product for \(q_i=v^\top M^{-1}v\) costs \(O(p^3+p^2)\).

The total is bounded by
\[
O(p^4+n^3+n^2p+np^2+p^3+n^2+np+p^2).
\]
Since \(n=t-1<t\) and \(p<t\), this is \(O(p^4+t^3)\). All preprocessing used in this calculation is included; no exponential matrix is materialized and no unprovided covariance oracle is assumed. Finally evaluate \(\log d-\log(d-q_i)\), or half of it for the exact information gain. All five obligations are closed.
