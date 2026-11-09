# Reference Proof

## Proof Structure

Reduce both matrix procedures to signed momentum on the first two diagonal coordinates. Exclude a countable union of hyperplanes containing every initialization that could reach a zero difference coordinate along a non-boundary gradient history. On its complement, prove that the momentum direction follows the signed difference direction, preserving the nonzero sum coordinate and hence a positive objective gap.

## Source-Local Correction

The source's momentum expansion at L000555 has a reversed time index. The recurrence gives
\[
\eta_t=(1-\beta)\sum_{j=0}^{t}\beta^{t-j}\operatorname{sign}(q_j),
\]
not the expression with \(\beta^j\operatorname{sign}(q_j)\). The corrected expansion gives exactly the same bound \(|\eta_t|\le1\) required by the subsequent argument. The proof below uses this corrected expansion and its recurrence. No theorem assumption or conclusion changes.

## Complete Proof

### 1. Objective, subgradients, and minimizers

Let
\[
P(W)=(W_{11},W_{22}),\qquad
J(v)=\operatorname{Diag}(v_1,v_2,0,\ldots,0),
\]
where the latter is an \(m\times n\) rectangular diagonal matrix. Thus \(J=P^*\) for the Euclidean and Frobenius inner products, and \(\|J(v)\|_F=\|v\|_2\).

Put
\[
h(w)=c|w_1+w_2|+|w_1-w_2|,
\qquad F=h\circ P.
\]
Because \(0<c\le1/2\), both functions are convex and continuous. Their nonnegative summands vanish simultaneously exactly when the two displayed coordinates vanish. Hence
\[
\min F=0,
\qquad
\operatorname*{argmin}F=\{W:W_{11}=W_{22}=0\}.
\]
All other matrix entries are unrestricted.

Define \(\operatorname{Sign}(x)=\{1\}\) for \(x>0\), \(\operatorname{Sign}(x)=\{-1\}\) for \(x<0\), and \(\operatorname{Sign}(0)=[-1,1]\). The scalar subgradient inequality for absolute value gives \(\partial|x|=\operatorname{Sign}(x)\). For the separable function \(k(p,q)=c|p|+|q|\), varying its coordinates separately in the subgradient inequality gives
\[
\partial k(p,q)=\{(ca,b):a\in\operatorname{Sign}(p),\ b\in\operatorname{Sign}(q)\}.
\]
We use the standard finite-dimensional linear-composition rule: if \(k\) is finite, convex, and continuous on its whole Euclidean space and \(A\) is linear, then
\[
\partial(k\circ A)(x)=A^*\partial k(Ax).
\]
Here these hypotheses hold for \(k\), for \(h\), and for the relevant linear maps. Applying the rule first to \(w\mapsto(w_1+w_2,w_1-w_2)\) and then to \(P\) yields
\[
\partial h(w)=\{ca(1,1)+b(1,-1):a\in\operatorname{Sign}(w_1+w_2),\ b\in\operatorname{Sign}(w_1-w_2)\},
\]
\[
\partial F(W)=J\bigl(\partial h(P(W))\bigr).
\]
Every displayed vector subgradient satisfies
\[
\|ca(1,1)+b(1,-1)\|_2^2=2c^2a^2+2b^2\le2(1+c^2).
\]
Consequently every matrix subgradient has Frobenius norm at most \(L=\sqrt{2(1+c^2)}\). For any matrices \(X,Y\), a subgradient \(H\in\partial F(Y)\) gives
\[
F(Y)-F(X)\le\langle H,Y-X\rangle\le L\|Y-X\|_F.
\]
Interchanging \(X\) and \(Y\) proves the required Lipschitz bound.

### 2. Matrix reduction and effective steps

Every \(G_t\) is supported on the first two diagonal entries. Since \(M_{-1}=0\), the same holds for every \(M_t\).

For a rectangular diagonal matrix \(D=\operatorname{Diag}(d)\), let \(I=\{i:d_i\ne0\}\). A rank-sized SVD uses the columns \(\operatorname{sign}(d_i)e_i^{(m)}\) and \(e_i^{(n)}\), for \(i\in I\), with singular values \(|d_i|\). Its polar factor is therefore
\[
\operatorname{polar}(D)=\sum_{i\in I}\operatorname{sign}(d_i)e_i^{(m)}(e_i^{(n)})^\top
=\operatorname{Diag}(\operatorname{sign}(d)),
\]
where \(\operatorname{sign}(0)=0\). For \(D=0\), this identity follows from the specified zero convention.

Write
\[
w_t=P(W_t),\qquad g_t=P(G_t),\qquad m_t=P(M_t).
\]
Then \(G_t=J(g_t)\), \(M_t=J(m_t)\), and both algorithms satisfy
\[
m_t=\beta m_{t-1}+(1-\beta)g_t,
\qquad
w_{t+1}=w_t-a_t\operatorname{sign}(m_t),
\qquad g_t\in\partial h(w_t).
\]
For Algorithm A,
\[
a_t=\Phi_t(J(g_0),\ldots,J(g_t)).
\]
For Algorithm B,
\[
a_t=\Phi_t(J(g_0),\ldots,J(g_t))\|J(m_t)\|_*.
\]
Thus each effective step is a finite function of the finite vector-gradient history. It is positive for Algorithm A and nonnegative for Algorithm B. Positivity for Algorithm B on the non-exceptional trajectories will follow below from the nonzero momentum coordinates; it is not assumed for arbitrary trajectories.

### 3. A fixed null exceptional set

Fix one algorithm and the complete collection \((\Phi_t)\). Define the finite set
\[
\mathcal G=\{c\epsilon(1,1)+\delta(1,-1):\epsilon,\delta\in\{-1,1\}\}.
\]
For any finite string \((h_0,\ldots,h_t)\in\mathcal G^{t+1}\), compute its auxiliary momentum by
\[
\mu_{-1}=0,\qquad \mu_s=\beta\mu_{s-1}+(1-\beta)h_s.
\]
Define
\[
a_s(h_0,\ldots,h_s)=
\begin{cases}
\Phi_s(J(h_0),\ldots,J(h_s)),&\text{Algorithm A},\\
\Phi_s(J(h_0),\ldots,J(h_s))\|J(\mu_s)\|_*,&\text{Algorithm B}.
\end{cases}
\]
These quantities are defined even for strings not realized by an actual trajectory. Put
\[
\mathcal E=\left\{2\sum_{s=0}^{T-1}\sigma_s a_s(h_0,\ldots,h_s):
T\ge0,\ \sigma_s\in\{-1,1\},\ (h_0,\ldots,h_{T-1})\in\mathcal G^T\right\}.
\]
At \(T=0\), the sum is empty and equals zero. For each fixed \(T\), only finitely many values occur, so \(\mathcal E\) is countable and \(0\in\mathcal E\).

Define
\[
N=\{W:W_{11}+W_{22}=0\}\ \cup\ \bigcup_{x\in\mathcal E}\{W:W_{11}-W_{22}=x\}.
\]
Every set in this countable union is an affine hyperplane of Lebesgue measure zero. Explicitly, in a bounded box \([-R,R]^{mn}\), the slab \(|W_{11}\pm W_{22}-x|<\varepsilon\) containing the respective hyperplane has volume at most \(2\varepsilon(2R)^{mn-1}\); letting \(\varepsilon\) decrease to zero and then taking a countable union of boxes proves the assertion. Thus \(N\) is a measurable null set. This argument does not require the functions \(\Phi_t\) themselves to be measurable.

### 4. Induction, momentum dominance, and nonconvergence

Take \(W_0\notin N\), and set
\[
p_t=w_{t,1}+w_{t,2},\qquad q_t=w_{t,1}-w_{t,2}.
\]
Then \(p_0\ne0\) and \(q_0\notin\mathcal E\), so \(q_0\ne0\). We prove inductively that
\[
p_t=p_0,\qquad
q_t=q_0-2\sum_{s=0}^{t-1}a_s\operatorname{sign}(q_s),\qquad q_t\ne0.
\]
The assertions hold at \(t=0\). Suppose they hold through time \(t\). For every \(0\le s\le t\), the subgradient is unique and equals
\[
g_s=c\operatorname{sign}(p_0)(1,1)+s_s(1,-1),
\qquad s_s=\operatorname{sign}(q_s)\in\{-1,1\}.
\]
In particular, these actual gradients belong to \(\mathcal G\).

Write
\[
m_s=\alpha_s(1,1)+\eta_s(1,-1).
\]
The recurrences, initialized by \(\alpha_{-1}=\eta_{-1}=0\), give
\[
\alpha_s=\beta\alpha_{s-1}+(1-\beta)c\operatorname{sign}(p_0),
\qquad
\eta_s=\beta\eta_{s-1}+(1-\beta)s_s.
\]
Hence
\[
\alpha_s=c(1-\beta^{s+1})\operatorname{sign}(p_0),\qquad |\alpha_s|\le c.
\]
The corrected unrolling of the second recurrence is
\[
\eta_s=(1-\beta)\sum_{j=0}^{s}\beta^{s-j}s_j,
\]
so
\[
|\eta_s|\le(1-\beta)\sum_{j=0}^{s}\beta^{s-j}=1-\beta^{s+1}\le1.
\]
Exponent-zero weights in these finite polynomial sums equal one, also when \(\beta=0\). In particular \(|\eta_{t-1}|\le1\), including the initial case \(\eta_{-1}=0\). Therefore
\[
s_t\eta_t=(1-\beta)+\beta s_t\eta_{t-1}
\ge1-\beta-\beta|\eta_{t-1}|
\ge1-2\beta=2c>c\ge|\alpha_t|.
\]
It follows that \(\operatorname{sign}(\eta_t)=s_t\) and \(|\eta_t|>|\alpha_t|\), whence
\[
\operatorname{sign}(m_t)
=\operatorname{sign}(\alpha_t+\eta_t,\alpha_t-\eta_t)
=s_t(1,-1).
\]
Both momentum coordinates are nonzero. Thus \(\|J(m_t)\|_*>0\), establishing positivity of the effective step for Algorithm B along this trajectory as well.

The update now yields
\[
p_{t+1}=p_t=p_0,
\qquad
q_{t+1}=q_t-2a_ts_t
=q_0-2\sum_{s=0}^{t}a_s\operatorname{sign}(q_s).
\]
If \(q_{t+1}=0\), the actual finite gradient string lies in \(\mathcal G^{t+1}\), its effective steps agree with those used in defining \(\mathcal E\), and the last identity implies \(q_0\in\mathcal E\). This contradicts the initialization choice. Hence \(q_{t+1}\ne0\), completing the induction.

Finally,
\[
F(W_t)=c|p_t|+|q_t|\ge c|p_0|>0
\qquad\text{for every }t\ge0.
\]
Since \(F\) is continuous and every minimizer has value zero, no such iterate sequence can converge to a minimizer. All subgradients encountered outside \(N\) were forced by uniqueness, so the conclusion covers every permissible subgradient selection. The construction applies separately to either fixed algorithm and every fixed collection \((\Phi_t)\), with precisely the quantifier order in the task.
