# Reference Proof

## Proof Structure

The five obligations are: establish admissible projection existence; verify an invertible witness; prove generic existence while simultaneously enforcing admissibility; derive the interventional variance system; and establish unique recovery, including the nonnegative least-squares domain. The genericity argument uses one witness-compatible minor chart and one nonzero polynomial in the entries of the measurement matrix. It does not project a joint polynomial zero set or assume that a witness belongs to every chart.

## Complete Proof

### step_001: Admissible projections exist

Write the columns of the known matrix as $a_1,\ldots,a_d$. For each $i$, let $A_{-i}$ denote the matrix obtained by deleting column $i$. Since $A$ has full column rank, $a_i$ is not in the span of the other columns. If every vector in the orthogonal complement of that span were orthogonal to $a_i$, taking orthogonal complements would place $a_i$ in that span, a contradiction. Hence there is a vector $t$ such that
\[
A_{-i}^Tt=0,\qquad a_i^Tt\ne0.
\]
This argument includes $d=1$, when the span of the other columns is $\{0\}$.

### step_002: An invertible witness

Let $e_1,\ldots,e_p$ be the standard coordinate vectors of $\mathbb R^p$ and set
\[
A_0=\begin{bmatrix}I_d\\0_{(p-d)\times d}\end{bmatrix}.
\]
Define fixed target indices and witness vectors by
\[
i_r=r,\quad c_r=e_r\quad(1\le r\le d),
\]
and
\[
i_{d+s}=1,\quad c_{d+s}=e_1+e_{d+s}\quad(1\le s\le p-d).
\]
Every $c_r$ is admissible for target $i_r$ at $A_0$, with $a_{0,i_r}^Tc_r=1$. Their squared-coordinate matrix is
\[
C_2=\begin{bmatrix}I_d&0\\E&I_{p-d}\end{bmatrix},
\]
where $E$ has ones in its first column and zeros elsewhere. Thus $\det C_2=1$. When $p=d$, the lower blocks are absent and $C_2=I_d$.

### step_003: Genericity and simultaneous admissibility

For a positive integer $m$, write $[m]=\{1,\ldots,m\}$. Fix, for every $i\in[d]$,
\[
J_i=[d]\setminus\{i\},\qquad K_i=[p]\setminus J_i,
\]
with all index sets ordered increasingly. Define
\[
M_i(A)=(A_{-i})_{J_i,:},\qquad R_i(A)=(A_{-i})_{K_i,:},\qquad m_i(A)=\det M_i(A),
\]
and
\[
\Delta(A)=\prod_{i=1}^d m_i(A).
\]
The matrix $M_i$ has size $(d-1)\times(d-1)$, the matrix $R_i$ has size $(p-d+1)\times(d-1)$, and $|K_i|=p-d+1$. For $d=1$, use the determinant convention $\det(0\times0)=1$; the equations involving the empty coordinate set $J_i$ impose no conditions.

At $A_0$, every $M_i$ is the identity of size $d-1$, so $\Delta(A_0)=1$. On the fixed chart $\Delta(A)\ne0$, retain the witness free coordinates
\[
u_r=(c_r)_{K_{i_r}}\in\mathbb R^{p-d+1}
\]
and define $t_r(A)$ in the original measurement-coordinate order by
\[
(t_r)_{K_{i_r}}=u_r,\qquad
(t_r)_{J_{i_r}}=-\big(M_{i_r}(A)^T\big)^{-1}R_{i_r}(A)^Tu_r.
\]
Consequently,
\[
A_{-i_r}^Tt_r=M_{i_r}^T(t_r)_{J_{i_r}}+R_{i_r}^T(t_r)_{K_{i_r}}=0.
\]
Also $t_r(A_0)=c_r$.

The inverse-adjugate formula shows that every coordinate of $t_r$ is a polynomial in the entries of $A$ divided by $m_{i_r}(A)$. Therefore
\[
w_r(A)=\Delta(A)t_r(A)
\]
on this chart extends to a polynomial vector on all of $\mathbb R^{p\times d}$. More explicitly, its free-coordinate block is $\Delta u_r$, while, when $d>1$, its other block is
\[
(w_r)_{J_{i_r}}=-\left(\prod_{j\ne i_r}m_j(A)\right)\operatorname{adj}(M_{i_r}(A)^T)R_{i_r}(A)^Tu_r.
\]
For $d=1$, that second block is empty and $w_r=u_r$ in the original coordinates.

Define the following polynomials in the $pd$ real entries of $A$:
\[
H(A)=\det\big((w_{r,k}(A)^2)_{r,k=1}^p\big),\qquad
L_r(A)=a_{i_r}^Tw_r(A),
\]
\[
F(A)=\Delta(A)H(A)\prod_{r=1}^p L_r(A).
\]
At the witness, $w_r(A_0)=c_r$, $H(A_0)=1$, and $L_r(A_0)=1$ for every $r$. Hence $F(A_0)=1$, so $F$ is not the zero polynomial.

We use the standard independent polynomial-zero-set lemma stated in the source: the zero set of a nonzero real polynomial on $\mathbb R^n$ has Lebesgue measure zero. Its hypotheses hold here with $n=pd\ge1$ and the nonzero polynomial $F$. Thus
\[
Z(F)=\{A\in\mathbb R^{p\times d}:F(A)=0\}
\]
is a Lebesgue-null set.

For any full-column-rank $A\notin Z(F)$, all factors in $F(A)$ are nonzero. In particular, the chart is valid, all $t_r(A)$ are defined, and
\[
a_{i_r}^Tt_r(A)=\frac{L_r(A)}{\Delta(A)}\ne0.
\]
Combined with the previously proved orthogonality, this establishes admissibility of every selected vector. Finally, because every squared-coordinate row is scaled by $\Delta(A)^2$ when passing from $t_r$ to $w_r$,
\[
\det T_2(A)=\frac{H(A)}{\Delta(A)^{2p}}\ne0.
\]
Thus the exceptional set in the theorem is contained in $Z(F)$. The vectors and targets are selected using $A$ alone, not unknown latent laws or noise parameters. This argument covers $d=1$ and $p=d$ with the empty-block conventions already given. A union over all minor charts is unnecessary: the factor $\Delta$ already accounts for the complement of the single witness-compatible chart.

### step_004: The interventional variance equations

Let $A$ and the selected vectors be as above. Under the chosen regime $\operatorname{do}(i_r)$, orthogonality gives the exact random-variable identity
\[
t_r^TY=(a_{i_r}^Tt_r)X_{i_r}+t_r^T\varepsilon.
\]
The targeted variable has finite known variance $v_{i_r}$. The measurement noise is independent of it in that regime and has the same diagonal covariance in every regime. Therefore the displayed projection has finite variance and
\[
\operatorname{Var}(t_r^TY\mid\operatorname{do}(i_r))
=(a_{i_r}^Tt_r)^2v_{i_r}+\sum_{k=1}^p t_{r,k}^2\sigma_k^2.
\]
No second-moment assumption on the other latent coordinates is needed: their contributions vanish in the preceding random-variable identity. It also does not matter whether the selected intervention targets additional coordinates.

With $q=(q_1,\ldots,q_p)^T$ and $\sigma^2=(\sigma_1^2,\ldots,\sigma_p^2)^T$, the defining subtractions give
\[
q=T_2\sigma^2.
\]
Both $q$ and $T_2$ are known from the selected projections, known measurement matrix, targeted variances, and population projected variances.

### step_005: Identification and least squares

Since $T_2$ is invertible,
\[
\sigma^2=T_2^{-1}q
\]
is the unique solution. Every measurement-noise variance vector compatible with the supplied population quantities must satisfy the same linear system and hence equal this vector.

For any $s\in\mathbb R^p$,
\[
\|T_2s-q\|_2^2=\|T_2(s-\sigma^2)\|_2^2.
\]
This objective is zero at $s=\sigma^2$ and strictly positive for $s\ne\sigma^2$. Thus $\sigma^2$ is the unique unconstrained least-squares minimizer. It belongs to $[0,\infty)^p$, so it is also the unique minimizer on the source's nonnegative variance domain. Zero targeted or measurement-noise variances do not affect this argument.

All five theorem-critical obligations are closed. The only external result used is the explicitly stated standard independent polynomial-zero-set lemma, with its hypotheses verified above.
