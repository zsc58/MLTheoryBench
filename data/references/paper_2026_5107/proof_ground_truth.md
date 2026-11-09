# Reference Proof

## Proof Structure

Construct nested interior cells separated by transition regions. A recursive ReLU encoder supplies the cell label at each resolution, and two successive sine evaluations approximate all residual cell averages at that resolution. A cell-average translation estimate controls the residual on cell interiors, while a common small transition parameter controls every exceptional region. Finally, an explicit pipeline realizes all corrections in one shared network with exactly the allowed prefix timing and width.

## Complete Proof

Write \(D=[0,1]^d\), \(\mu(t)=\mu_{f,p}(t)\), and \(W=2dN+d+2\). For a measurable set \(Q\) with \(0<|Q|<\infty\) and \(g\in L^1(Q)\), write
\[
 A_Q(g)=|Q|^{-1}\int_Q g.
\]
All averages below have positive-volume domains, and all identities involving the target or residuals hold almost everywhere.

### 1. The cell-average estimate and the zero-modulus case

First let \(I=[0,s]\), where \(s>0\), and let \(g\in L^p(I)\). Jensen's inequality gives
\[
 \int_I|g(t)-A_I(g)|^p\,dt
 \leq \frac1s\int_I\int_I|g(t)-g(y)|^p\,dy\,dt
 =\frac1s\int_{-s}^s\int_{I\cap(I-h)}|g(t+h)-g(t)|^p\,dt\,dh.
 \tag{1}
\]
The equality follows by setting \(h=y-t\) and using Tonelli's theorem.

For a cube \(Q=a+[0,s]^d\subseteq D\), let \(P_i\) average a function over its \(i\)-th coordinate interval, leaving the other coordinates fixed. Jensen and Fubini show that each \(P_i\) is an \(L^p(Q)\) contraction. Moreover, \(P_1\cdots P_d f=A_Q(f)\), and
\[
 f-A_Q(f)=\sum_{i=1}^d P_1\cdots P_{i-1}(f-P_i f).
\]
Using \(|\sum_i z_i|^p\leq d^{p-1}\sum_i|z_i|^p\), contraction, and (1) on the coordinate slices gives
\[
 \|f-A_Q(f)\|_{L^p(Q)}^p
 \leq\frac{d^{p-1}}s\int_{-s}^s\sum_{i=1}^d
 \int_{Q\cap(Q-he_i)}|f(x+he_i)-f(x)|^p\,dx\,dh.
 \tag{2}
\]
Here \(e_i\) is the \(i\)-th standard coordinate vector. Fubini ensures that the slices belong to \(L^p\) almost everywhere, so every application of (1) is legitimate. This also covers \(d=1\) and \(p=1\).

The definition of the modulus and the triangle inequality imply
\[
 0\leq\mu(t)\leq2\|f\|_{L^p(D)},
 \qquad \mu\text{ is nondecreasing}.
 \tag{3}
\]
If \(\mu(t_0)=0\) for some \(t_0>0\), (2) implies that \(f\) is constant almost everywhere on every cube in \(D\) of positive side length at most \(t_0\). Cover \((0,1)^d\) by a countable family of such open cubes with rational endpoints. Their overlap graph is connected: otherwise the unions belonging to distinct graph components would disconnect \((0,1)^d\). Intersecting open cubes have positive-measure intersection, so their almost-everywhere constants agree. Countability then shows that \(f\) is constant almost everywhere on \(D\).

If \(f=c\) almost everywhere, choose all hidden maps to have width \(W\) and be zero, take \(C_0\equiv c\), and take \(C_j\equiv0\) for \(j\geq1\). Every readout equals \(c\). Henceforth assume that \(f\) is not almost everywhere constant. Then \(\mu(t)>0\) for every \(t>0\).

### 2. A common geometric parameter and the recursive encoder

Set
\[
 \eta=\tfrac12\mu(N^{-L})>0,
 \qquad M=2^{d+2}(d+1)N^{dL}\|f\|_{L^p(D)}.
\]
For \(0<\delta<(2N^L)^{-1}\), define, for \(0\leq r\leq L\),
\[
 I_{r,j}=[jN^{-r},(j+1)N^{-r}-\delta],
 \quad Q_{r,\beta}=\prod_{a=1}^d I_{r,\beta_a},
 \quad U_r=\bigcup_{\beta\in\{0,\ldots,N^r-1\}^d}Q_{r,\beta},
 \quad \Omega_r=D\setminus U_r.
\]
Each finer interval is contained in its corresponding coarser interval, since its left endpoint is no smaller and its right endpoint is no larger. Thus \(U_r\subseteq U_q\) for \(q\leq r\), and \(\Omega_q\subseteq\Omega_r\). The cells at a fixed level are disjoint, have side length \(s_r=N^{-r}-\delta>0\), and satisfy
\[
 |\Omega_r|=1-(1-N^r\delta)^d\leq dN^r\delta.
\]
By absolute continuity of the integral of \(|f|^p\), choose one \(\delta\) sufficiently small that, simultaneously for all \(0\leq r\leq L\),
\[
 \|f\|_{L^p(\Omega_r)}+(L+1)M|\Omega_r|^{1/p}\leq\eta.
 \tag{4}
\]
This choice precedes the decoder parameters. The bound \(M\) is independent of \(\delta\).

Let \(t_+=\max\{t,0\}\). The source's continuous step proxy has the explicit representation
\[
 h(t)=\frac1\delta\sum_{b=1}^{N-1}
 \bigl((t-b+\delta)_+-(t-b)_+\bigr).
 \tag{5}
\]
For \(N=1\), the empty sum is zero. For general \(N\), each summand is zero before \(b-\delta\), rises linearly to one on \([b-\delta,b]\), and equals one thereafter. Consequently \(h\geq0\) and
\[
 h(t)=j\quad\text{on }[j,j+1-\delta],\qquad 0\leq j<N.
\]
Define vector registers recursively by
\[
 y_0(x)=0,\qquad
 y_{r,a}(x)=y_{r-1,a}(x)+N^{-r}h\bigl(N^r(x_a-y_{r-1,a}(x))\bigr),
 \quad 1\leq a\leq d.
 \tag{6}
\]
All their coordinates are nonnegative on \(D\).

For \(x_a\in I_{1,j}\), the argument \(Nx_a\) belongs to \([j,j+1-N\delta]\subseteq[j,j+1-\delta]\), so \(y_{1,a}=j/N\). For the induction step, write \(j=mN+b\) and suppose \(x_a\in I_{r,j}\). Then \(x_a\in I_{r-1,m}\), so the preceding register equals \(m/N^{r-1}\), and
\[
 N^r(x_a-m/N^{r-1})\in[b,b+1-N^r\delta]
 \subseteq[b,b+1-\delta].
\]
Equation (6) therefore gives \(y_{r,a}=j/N^r\). It follows that
\[
 y_r(x)=\beta/N^r\quad\text{on }Q_{r,\beta}.
 \tag{7}
\]
For \(r\geq1\), define
\[
 \Lambda_r(y)=1+\sum_{a=1}^dN^{ar}y_a.
\]
On the cell \(Q_{r,\beta}\), this gives the integer
\[
 k=1+\sum_{a=1}^dN^{(a-1)r}\beta_a.
 \tag{8}
\]
These labels enumerate \(1,\ldots,N^{dr}\) bijectively. When \(N=1\), there is only one cell and its label is one.

### 3. Finite interpolation with two sine evaluations

We prove the interpolation statement needed below. Given \(K\geq1\), prescribed real values \(z_1,\ldots,z_K\), and \(\varepsilon>0\), put \(u=\max_k|z_k|\). There are real \(v,w\) such that
\[
 |u\sin(v\sin(kw))-z_k|<\varepsilon\quad(1\leq k\leq K).
 \tag{9}
\]
If \(u=0\), choose \(v=w=0\). Otherwise set \(\xi_k=\arcsin(z_k/u)\). For every nonzero integer vector \(c=(c_0,\ldots,c_K)\), consider
\[
 F_c(t)=2\pi c_0+\sum_{k=1}^Kc_k\sin(kt).
\]
This trigonometric polynomial is not identically zero: integration over a period would first give \(c_0=0\), and multiplication by each \(\sin(kt)\), followed by integration, would give every remaining coefficient zero. A nonzero trigonometric polynomial has finitely many zeros in a period; this also follows by expressing it as a Laurent polynomial in \(e^{it}\) and clearing negative powers. The union of the zero sets over the countably many vectors \(c\) is countable. Choose \(w\in[0,2\pi)\) outside that union. Then
\[
 1,\frac{\sin w}{2\pi},\ldots,\frac{\sin Kw}{2\pi}
\]
are rationally independent.

Use the following standard independent form of Kronecker's approximation theorem: if \(1,\alpha_1,\ldots,\alpha_K\) are rationally independent, then for every \(\beta\in\mathbb R^K\) and \(\tau>0\), there exist \(n\in\mathbb Z\) and \(q\in\mathbb Z^K\) with \(|n\alpha_k-\beta_k-q_k|<\tau\) for all \(k\). Its hypotheses hold here with \(\alpha_k=\sin(kw)/(2\pi)\), \(\beta_k=\xi_k/(2\pi)\), and \(\tau=\varepsilon/(2\pi u)\). Taking \(v=n\) and using periodicity and the Lipschitz bound for sine proves (9).

Only the amplitude \(u\) will be bounded uniformly below. No bound on the magnitudes of \(v,w\) is needed or asserted.

### 4. Residual corrections and the simultaneous error estimates

Define \(f_0=f\) and, successively,
\[
 \Phi_r=\sum_{q=0}^r\Gamma_q,\qquad f_{r+1}=f-\Phi_r.
\]
At level zero, let \(z_{0,1}=A_{Q_{0,0}}(f)\) and \(u_0=|z_{0,1}|\). Since \(\delta<1/2\),
\[
 u_0\leq |Q_{0,0}|^{-1}\|f\|_{L^1(D)}
 \leq 2^d\|f\|_{L^p(D)}\leq M.
\]
Apply (9) with tolerance \(\eta\) to choose \(v_0,w_0\), and set
\[
 \Gamma_0(x)=u_0\sin(v_0\sin w_0).
\]
Thus \(|\Gamma_0|\leq M\) and \(|\Gamma_0-A_{Q_{0,0}}(f)|<\eta\).

For \(r\geq1\), assume the corrections through level \(r-1\) have been constructed and that their partial sum is constant on each level-\((r-1)\) cell and satisfies the desired error estimate. Equation (3) then gives
\[
 \|f_r\|_{L^p(D)}\leq(2d+1)\mu(N^{-(r-1)})
 \leq(4d+2)\|f\|_{L^p(D)}.
\]
Enumerate the level-\(r\) cells by (8), and let \(z_{r,k}=A_{Q_{r,\beta}}(f_r)\) on the cell with label \(k\). Because \(\delta<(2N^L)^{-1}\), every such cell has volume at least \((2N^L)^{-d}\). Therefore
\[
 |z_{r,k}|
 \leq2^dN^{dL}\|f_r\|_{L^1(D)}
 \leq2^dN^{dL}(4d+2)\|f\|_{L^p(D)}\leq M.
 \tag{10}
\]
Use (9) with tolerance \(\eta\), put \(u_r=\max_k|z_{r,k}|\), and define
\[
 \Gamma_r(x)=u_r\sin\bigl(v_r\sin(w_r\Lambda_r(y_r(x)))\bigr).
 \tag{11}
\]
This is a continuous function bounded in absolute value by \(M\), is constant on each level-\(r\) cell, and differs there from the residual average by less than \(\eta\). Every earlier correction is also constant on that cell by nesting. Hence \(\Phi_r\) is constant on it, and cancellation of the preceding constant readout inside the average gives
\[
 |f_{r+1}(x)|\leq |f(x)-A_Q(f)|+\eta
 \quad\text{for almost every }x\in Q.
 \tag{12}
\]
The same estimate holds at level zero by its construction.

Let \(\chi_r\) equal \(A_Q(f)\) on each level-\(r\) cell. Apply (2) on the cells and sum. For fixed coordinate \(i\) and displacement \(h\), the sets \(Q\cap(Q-he_i)\) from distinct cells are disjoint, and their union lies in \(E_{he_i}\). Since \(|h|\leq s_r<N^{-r}\),
\[
 \begin{aligned}
 \|f-\chi_r\|_{L^p(U_r)}^p
 &\leq\frac{d^{p-1}}{s_r}\int_{-s_r}^{s_r}
 \sum_{i=1}^d\mu(N^{-r})^p\,dh\\
 &=2d^p\mu(N^{-r})^p.
 \end{aligned}
 \tag{13}
\]
Equations (12) and (13), together with \(|U_r|\leq1\), imply
\[
 \|f_{r+1}\|_{L^p(U_r)}\leq2^{1/p}d\mu(N^{-r})+\eta.
\]
On the complementary region, the already established amplitude bounds and (4) give
\[
 \|f_{r+1}\|_{L^p(\Omega_r)}
 \leq\|f\|_{L^p(\Omega_r)}+(r+1)M|\Omega_r|^{1/p}\leq\eta.
\]
Consequently
\[
 \begin{aligned}
 \|f-\Phi_r\|_{L^p(D)}
 &\leq2^{1/p}d\mu(N^{-r})+2\eta\\
 &\leq(2d+1)\mu(N^{-r}),
 \end{aligned}
 \tag{14}
\]
since \(2\eta=\mu(N^{-L})\leq\mu(N^{-r})\) and \(2^{1/p}\leq2\). Applying this argument first to level zero and then successively to the other levels closes the induction used in (10). Thus all corrections exist, all amplitude bounds hold, and (14) holds simultaneously for every level. No smallness of the decoder frequencies is used in choosing \(\delta\).

### 5. Explicit shared-network realization and timing

We now realize the particular functions just constructed, rather than merely counting the channels in separate modules.

Let \(q=2dN\). For \(r\geq1\), define an affine map \(E_r:\mathbb R^{2d}\to\mathbb R^q\) by concatenating, for each coordinate \(a\), the entries
\[
 x_a,\quad y_a,\quad
 \bigl(N^r(x_a-y_a)-b+\delta,\ N^r(x_a-y_a)-b\bigr)_{b=1}^{N-1}.
\]
There are \(2N\) entries per coordinate, including when \(N=1\). Let \(\mathcal R\) denote coordinatewise ReLU on these \(q\) entries. Formula (5) gives a linear readout \(D_r:\mathbb R^q\to\mathbb R^{2d}\): from the coordinate block \((X_a,Y_a,(P_{a,b},T_{a,b})_b)\), output
\[
 X_a,\qquad Y_a+\frac{N^{-r}}\delta\sum_{b=1}^{N-1}(P_{a,b}-T_{a,b}).
\]
For nonnegative \(x,y\), copying through ReLU leaves \(x,y\) unchanged, and therefore
\[
 D_r\mathcal R E_r(x,y)
 =\bigl(x,\ y+N^{-r}h(N^r(x-y))\bigr),
 \tag{15}
\]
with the last expression interpreted coordinatewise.

Define the nonnegative feature vectors
\[
 S_r(x)=\mathcal R E_r(x,y_{r-1}(x)),\qquad 1\leq r\leq L.
\]
Then \(D_rS_r(x)=(x,y_r(x))\), and
\[
 S_{r+1}(x)=\mathcal R E_{r+1}D_rS_r(x).
 \tag{16}
\]
Thus one activation block advances the encoder features by one level. In particular, the update uses only an affine map followed by ReLU; no additional nonlinear operation is hidden in its readout.

Use hidden dimension \(W=q+d+2\). Order each state as two sine coordinates, the \(q\) encoder-feature coordinates, and \(d\) zero padding coordinates. Write the two sine coordinates after block \(i\) as \(a_i,b_i\).

The initial affine map \(B_{-1}:\mathbb R^d\to\mathbb R^W\) has first two outputs \(w_0,0\), encoder outputs \(E_1(x,0)\), and zero padding. Its activated state is therefore
\[
 (a_{-1},b_{-1},S_1,0_d)=(\sin w_0,0,S_1,0_d).
\]
For each \(i=0,\ldots,L\), define \(B_i:\mathbb R^W\to\mathbb R^W\) using the following affine preactivations:

- Its second sine preactivation is \(v_i a_{i-1}\).
- If \(i<L\), its first sine preactivation is \(w_{i+1}\Lambda_{i+1}(y_{i+1})\). The preceding state's encoder features are \(S_{i+1}\), so \(y_{i+1}\) is obtained by the linear readout \(D_{i+1}\). If \(i=L\), set the first preactivation to zero.
- If \(i+2\leq L\), its encoder preactivations are \(E_{i+2}D_{i+1}S_{i+1}\). Otherwise copy the preceding encoder-feature vector. All copied features are nonnegative, so ReLU preserves them.
- Its padding preactivations are zero.

Every listed preactivation is affine in the preceding state. After block \(i\), the encoder features are \(S_{\min\{i+2,L\}}\). Induction also gives
\[
 a_i=\sin\bigl(w_{i+1}\Lambda_{i+1}(y_{i+1})\bigr)
 \quad(0\leq i<L),
\]
and
\[
 b_0=\sin(v_0\sin w_0),\qquad
 b_i=\sin\bigl(v_i\sin(w_i\Lambda_i(y_i))\bigr)
 \quad(1\leq i\leq L).
\]
The formulas remain valid for \(L=1\): the initial block computes \(S_1\), and both subsequent blocks simply retain those features. They also remain valid for \(N=1\), where there are no hinge pairs and every localization register is zero.

Let \(C_j:\mathbb R^W\to\mathbb R\) extract the second sine coordinate multiplied by \(u_j\). Then on \(D\),
\[
 C_j\circ(\sigma\circ B_j)\circ\cdots\circ(\sigma\circ B_{-1})=\Gamma_j.
\]
All maps have input and output dimensions at most \(W\). The encoder uses \(2dN\) ReLU channels, the padding uses \(d\), and the two sine channels give total width \(2dN+d+2\). There are exactly the blocks indexed by \(-1,0,\ldots,L\); the inner and outer evaluations for correction \(j\) occur in blocks \(j-1\) and \(j\), respectively. The output sum is external to the hidden state, so no hidden accumulator is required.

Taking \(G_\ell=\sum_{j=0}^\ell\Gamma_j=\Phi_\ell\), equation (14) proves the required estimate for every prefix. All constructed network functions are continuous and bounded on the compact domain, so the residual norms are well defined.

## Obligation Closure

The cell-average domain and estimate, zero-modulus case, common transition parameter, recursive encoder, finite interpolation, amplitude-controlled residual induction, and exact shared-network width and timing have all been established above. Kronecker's theorem is used only in its stated standard independent form, with its hypotheses verified. The ReLU realization is derived explicitly from (5), rather than left to an unspecified external realization claim. There are no unresolved proof obligations.
