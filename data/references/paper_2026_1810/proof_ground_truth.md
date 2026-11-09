# Reference Proof

## Proof Structure

Prove an equivalence between a fixed set of positions being exactly the support positions and those positions forming a fully supporting input whose decision is confirmed by all remaining observations. Use exchangeability and independent integration to obtain support-induced finite measures and their normalization identities at every sample size. Form the finite moment relaxation, derive its full pointwise dual constraints, and verify the supplied multipliers, including all boundary faces and indices outside the target-size rectangle.

## Complete Proof

Write \(Q=[0,1]^m\). Lists and their sublists below are indexed by observation positions, so repeated observations cause no ambiguity. For a tuple of lists \(D\), write \(\operatorname{supp}(D)\) for its support sublists.

### 1. Exact support-event equivalence

Fix a size vector \(n\in\mathbb N_0^m\), an index \(k\le n\), and deterministic choices of \(k_i\) positions in each component of an i.i.d. input \(D\). Let \(A\) be the tuple of selected sublists and let \(B=D\setminus A\) be the remaining sublists. Outside the non-degeneracy null set for \(D\), we claim
\[
\operatorname{supp}(D)=A
\quad\Longleftrightarrow\quad
\operatorname{supp}(A)=A\ \text{ and }\ M(A)\in Z_i(\delta)\text{ for every occurrence }\delta\in B_i.
\tag{1}
\]

For the forward implication, non-degeneracy gives \(M(A)=M(D)=z\). Batch responsiveness then implies that every observation in \(B\) confirms \(z\); otherwise appending the entire batch \(B\) to \(A\) would change the decision. If an occurrence \(a\in A\) were not supporting for \(A\), then \(M(A\setminus a)=z\). Appending the confirming batch \(B\) would give \(M(D\setminus a)=z\), contradicting that \(a\) is supporting for \(D\). Thus every occurrence of \(A\) supports \(A\).

Conversely, suppose the right-hand side holds and put \(z=M(A)\). Stability gives \(M(D)=z\). It also gives \(M(D\setminus b)=z\) for each occurrence \(b\in B\), so \(T=\operatorname{supp}(D)\subseteq A\). Non-degeneracy gives \(M(T)=z\). Because appending \(D\setminus T\) to \(T\) leaves its decision unchanged, batch responsiveness implies that every observation in \(D\setminus T\) confirms \(z\). If some occurrence \(a\in A\setminus T\) existed, stability applied to \(T\) and the batch \((A\setminus a)\setminus T\) would give \(M(A\setminus a)=z=M(A)\). This contradicts \(\operatorname{supp}(A)=A\). Hence \(T=A\), proving (1). Empty batches and empty component lists are included in this argument.

### 2. Support-induced measures and decomposition

For every \(k\in\mathbb N_0^m\), let \(X_k\) be an independent input of size \(k\), and define the finite nonnegative Borel measure
\[
\mu_k(C)=\mathbb E\left[
\mathbf1_{\{\operatorname{supp}(X_k)=X_k\}}
\mathbf1_{\{V(M(X_k))\in C\}}
\right],\qquad C\subseteq Q\text{ Borel}.
\tag{2}
\]
Its mass is at most one. For \(k=0\), the input is the deterministic empty tuple and the fully-supporting condition is vacuous.

The standard measure fact used here is the pushforward integration identity: if \(\nu\) is a finite measure and \(T\) is measurable, then \(T_\#\nu(C)=\nu(T^{-1}(C))\) and \(\int f\,d(T_\#\nu)=\int f\circ T\,d\nu\) for nonnegative measurable \(f\). Here \(\nu\) is the product probability restricted to the measurable fully-supporting event and \(T=V\circ M\). All its hypotheses follow from the public measurability conditions. This standard fact does not supply the normalization identities proved below.

For Borel sets \(C(k)\subseteq Q\), partition the event \(V(M(D))\in C(s_n^\star)\) by its exact support positions. There are \(\binom nk\) position choices of count \(k\), and permutation invariance and i.i.d. sampling make their probabilities equal. For each fixed choice, (1) identifies the event with the selected input being fully supporting, having its risk vector in \(C(k)\), and all other observations confirming its decision. Integrating first over the independent observations outside those fixed positions gives
\[
\prod_{i=1}^m(1-V_i(M(A)))^{n_i-k_i}.
\]
This is integration before selecting the random support set, not an assertion that observations remain independent conditional on being nonsupport samples. Applying (2) yields
\[
\mathbb P^{|n|}\{V(M(D))\in C(s_n^\star)\}
=\sum_{k\le n}\binom nk\int_{C(k)}(1-v)^{n-k}\,d\mu_k(v).
\tag{3}
\]
All exponents in (3) are nonnegative, with \(0^0=1\).

Taking every \(C(k)=Q\) and replacing \(n\) by any \(h\in\mathbb N_0^m\) gives the normalization identities
\[
\sum_{k\le h}\binom hk\int_Q(1-v)^{h-k}\,d\mu_k(v)=1.
\tag{4}
\]
They use the same measures \(\mu_k\) at every size, because (2) depends only on the input size \(k\) and the single fixed decision scheme. No additional deletion-consistency identities are needed.

Equation (3) also resolves the region boundary convention. For fixed \(k\le N\), choosing only the \(k\)-th set nonempty gives
\[
\mathbb P^{|N|}\{s_N^\star=k,\ (1-V(z_N^\star))^{N-k}=0\}=0.
\tag{5}
\]
Indeed the corresponding integrand in (3) is identically zero. Thus excluding those faces from \(R(k)\) does not alter the observed-support confidence event except on a null set. This reasoning does not exclude a coordinate \(v_i=1\) when \(k_i=N_i\).

### 3. Finite moment relaxation and its full dual

For \(k\le H\), define the bounded measurable functions
\[
c_k(v)=
\begin{cases}
\binom Nk(1-v)^{N-k}\mathbf1_{R(k)}(v),&k\le N,\\
0,&k\not\le N.
\end{cases}
\]
The second case is a separate definition; no negative power or undefined region is evaluated there.

Minimize \(\sum_{k\le H}\int_Q c_k\,d\nu_k\) over finite nonnegative Borel measures \(\nu_k\), \(k\le H\), subject to
\[
\sum_{k\le h}\binom hk\int_Q(1-v)^{h-k}\,d\nu_k(v)=1,
\qquad 0\le h\le H.
\tag{6}
\]
The actual measures \(\mu_k\) are feasible by (4), and their objective equals the desired probability by (3). Hence this program's infimum is a lower bound on that probability. It is the finite truncation of the analogous program containing all identities (4).

For initially unrestricted real equality multipliers \(a_h\), set
\[
B_k^a(v)=\sum_{k\le h\le H}a_h\binom hk(1-v)^{h-k}.
\]
Expanding the Lagrangian gives
\[
L(\nu,a)=\sum_{h\le H}a_h+
\sum_{k\le H}\int_Q(c_k-B_k^a)\,d\nu_k.
\tag{7}
\]
Its infimum over the nonnegative-measure cone is \(\sum_h a_h\) if \(B_k^a(v)\le c_k(v)\) for every \(k\le H\) and \(v\in Q\): all integrals are nonnegative and zero measures attain that infimum. If one pointwise inequality fails, arbitrarily large point masses at that point make the infimum \(-\infty\). Thus the full dual constraints are
\[
B_k^a(v)\le c_k(v),\qquad k\le H,\ v\in Q.
\tag{8}
\]
No strong-duality or attainment assertion is required. In particular, integrating (8) against the actual measures and using (4) proves weak duality directly:
\[
\sum_h a_h
=\sum_{k\le H}\int_Q B_k^a\,d\mu_k
\le\sum_{k\le H}\int_Q c_k\,d\mu_k
=\mathbb P^{|N|}\{V(z_N^\star)\in R(s_N^\star)\}.
\tag{9}
\]
The sign restrictions in the problem are sufficient additional restrictions for constructing a feasible point of this full dual; they are not inherent restrictions on the equality multipliers in (7).

### 4. Verification of the collective certificate

Take \(a_h=\lambda_h\). For \(k\le N\) and \(w_k(v)=(1-v)^{N-k}>0\), write
\[
g_k(v)=\sum_{k\le h\le H}\lambda_h
\frac{\binom hk}{\binom Nk}(1-v)^{h-N}.
\]
This is well-defined on the stated domain. Its \(h=N\) term equals \(\lambda_N\); all other terms are nonpositive. Consequently
\[
g_k(v)\le\lambda_N\le1.
\]
Where \(g_k(v)\ge0\), the definition of \(R(k)\) gives its indicator equal to one. Where \(g_k(v)<0\), that indicator is zero. Therefore \(g_k(v)\le\mathbf1_{R(k)}(v)\) throughout \(w_k>0\). Multiplication by \(\binom Nk w_k(v)>0\) proves (8) there.

If \(k\le N\) and \(w_k(v)=0\), the \(h=N\) term of \(B_k^\lambda(v)\) is zero. Every other term is nonpositive and involves only nonnegative powers. Thus \(B_k^\lambda(v)\le0=c_k(v)\), proving (8) on these faces as well.

Finally, if \(k\le H\) but \(k\not\le N\), then \(h=N\) cannot occur in the sum defining \(B_k^\lambda\). Every summand is nonpositive, so again \(B_k^\lambda(v)\le0=c_k(v)\).

All full dual constraints hold. Equation (9) and the prescribed sum now give
\[
\mathbb P^{|N|}\{V(z_N^\star)\in R(s_N^\star)\}
\ge\sum_{0\le h\le H}\lambda_h=1-\beta.
\]
The proof includes zero support counts, partially empty inputs, \(H=N\), \(k=N\), zero multipliers, and risk vectors on the closed-cube boundary. No Cartesian-product decomposition of the regions is used.

## Obligation Closure

The support-event equivalence is proved in Section 1; the measure construction, sampling integration, and normalization are proved in Section 2; the finite relaxation and full weak-duality inequality are proved in Section 3; every multiplier constraint and boundary case is checked in Section 4. The only invoked measure-theoretic background is the stated pushforward integration identity and integration under a product probability law. No specialized external theorem or unresolved proof obligation remains.
