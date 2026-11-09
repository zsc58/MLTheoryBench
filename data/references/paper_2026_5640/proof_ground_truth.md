# Reference Proof

## Audited Contract and Obligations

The observations and kernel values are fixed. There is no distributional assumption or probabilistic convergence assertion. The source's algorithmic regime is \(1/n<\nu<1\), with \(\eta>0\); the public algorithm uses the permitted no-shrinking configuration and compares the two maximum violations. Its initialization is feasible, including when \(\nu n\) is an integer. The argument below in fact applies to any feasible initialization and any rule that always updates an eligible pair with violation greater than the fixed positive tolerance. This stronger fact is used only privately and does not change the public algorithm.

The theorem-critical obligations are: well-defined and feasible exact updates, quantitative descent, convergence of an infinite coefficient sequence, a common tail of saturated updates, eventual boundary-transfer forms, recurrent neighbors in the same family, and the finite-index contradiction. Each is established below. No specialized external convergence theorem is assumed.

## 1. Well-Defined Exact Updates

Let \(A_{km}=K(x_k,x_m)\) and \(B_{km}=K^*(x_k^*,x_m^*)\). These are fixed real symmetric positive-semidefinite matrices. Write
\[
 F(u,v)=\frac{u^TAu}{\nu n}+\frac{(u-v)^TB(u-v)}\eta,
 \qquad G=\frac{Au}{\nu n}+\frac{B(u-v)}\eta,
 \qquad H=\frac{B(u-v)}\eta.
\]
The feasible set is nonempty: the prescribed initializer satisfies both sums and all coordinate bounds. At every feasible point the sets \(\{i:u_i>0\}\), \(\{i:v_i>0\}\), and \(\{i:v_i<1\}\) are nonempty. Indeed, the first two assertions follow from the positive sum \(\nu n\), and the third from \(\nu n<n\). All score extrema are therefore defined and attained. A violating pair has distinct indices.

For \(d=e_i-e_j\), direct expansion gives
\[
 F(u+td,v)-F(u,v)=2t(G_i-G_j)+t^2(D_{ij}+D^*_{ij}), \tag{1}
\]
\[
 F(u,v+sd)-F(u,v)=-2s(H_i-H_j)+s^2D^*_{ij}. \tag{2}
\]
The feasible intervals are respectively
\[
 -u_i\le t\le u_j,
 \qquad \max(-v_i,v_j-1)\le s\le\min(1-v_i,v_j).
\]

We verify that the denominators used for violating pairs are positive without assuming positive definiteness. If \(M\) is positive semidefinite and \(d^TMd=0\), then for every vector \(w\) and real \(h\),
\[
 0\le(d+hw)^TM(d+hw)=2h\,d^TMw+h^2w^TMw.
\]
Considering sufficiently small positive and negative \(h\) shows \(d^TMw=0\) for every \(w\), hence \(Md=0\). If \(D_{ij}+D^*_{ij}=0\), their nonnegativity implies \(Ad=Bd=0\), so \(G_i-G_j=0\). If \(D^*_{ij}=0\), then \(Bd=0\), so \(H_i-H_j=0\). Neither is possible for the corresponding violating pair.

For an ordinary update put \(\Delta=G_i-G_j>\tau\) and \(c=D_{ij}+D^*_{ij}>0\). Minimizing (1) over its feasible interval gives
\[
 t=-a,\qquad a=\min(\Delta/c,u_i)>0.
\]
For an auxiliary update put \(\Delta=H_i-H_j>\tau\) and \(c=D^*_{ij}>0\). Minimizing (2) gives
\[
 s=a,\qquad a=\min(\Delta/c,1-v_i,v_j)>0.
\]
These are precisely the public updates. They preserve the sums and all coordinate bounds. Notice that the linear coefficient in (2) is negative; in either descent direction the objective change is \(-2\Delta a+ca^2\).

After either update the selected score difference equals \(\Delta-ca\). If the unconstrained minimizer is used, this difference is zero, including when that minimizer coincides with a constraint endpoint. Otherwise an ordinary update sets \(u_i=0\), and an auxiliary update sets \(v_i=1\) or \(v_j=0\). Thus the selected ordered pair is no longer eligible and violating, or its score difference is zero. In particular, an ordinary update ending with \(u_i>0\), or an auxiliary update ending with both \(v_i<1\) and \(v_j>0\), makes its selected score difference zero.

## 2. Descent and Convergence

Let \(z^k=(u^k,v^k)\) be the coefficient vector before iteration \(k\), whenever that iteration occurs. Since \(a\le\Delta/c\), (1)-(2) imply
\[
 F(z^k)-F(z^{k+1})=2\Delta a-ca^2\ge\Delta a>\tau a
 =\frac{\tau}{\sqrt2}\|z^{k+1}-z^k\|_2. \tag{3}
\]
The last equality holds because exactly two distinct coordinates change, by opposite amounts of magnitude \(a\).

If the algorithm stops, the desired termination assertion already holds. For the rest of the proof suppose, for contradiction, that it has infinitely many iterations. The feasible set is closed and bounded in \(\mathbb R^{2n}\): \(0\le u_i\le\nu n\), \(0\le v_i\le1\), and the equality constraints are closed. It is therefore compact. The continuous objective is bounded below, so its strictly decreasing values have a finite limit \(F_\infty\).

For integers \(h\ge1\), summing (3) and using the triangle inequality gives
\[
 \|z^{k+h}-z^k\|_2
 \le\sum_{j=k}^{k+h-1}\|z^{j+1}-z^j\|_2
 <\frac{\sqrt2}{\tau}\{F(z^k)-F(z^{k+h})\}.
\]
For \(h=0\) the endpoint distance is zero. Consequently, for every integer \(h\ge0\),
\[
 \|z^{k+h}-z^k\|_2
 \le\frac{\sqrt2}{\tau}\{F(z^k)-F(z^{k+h})\}
 \le\frac{\sqrt2}{\tau}\{F(z^k)-F_\infty\}. \tag{4}
\]
The last bound tends to zero independently of \(h\). Thus \(z^k\) is Cauchy and converges to a feasible vector \(\bar z=(\bar u,\bar v)\). In particular, the step magnitudes tend to zero. Since the score maps are linear in the coefficients, \(G^k\to\bar G\) and \(H^k\to\bar H\).

## 3. Recurrent Pairs and a Common Saturated Tail

Call an ordered pair recurrent in a specified family if it is selected in that family infinitely often. There are finitely many family-labeled ordered pairs. Hence at least one is recurrent, and after a finite number of iterations every selected pair is recurrent: take a time beyond the last occurrence of every nonrecurrent pair.

At occurrences of a recurrent ordinary pair \((p,q)\), \(G_p^k-G_q^k>\tau\). Passing to the limit along these occurrences yields
\[
 \bar G_p-\bar G_q\ge\tau>0. \tag{5}
\]
Similarly, a recurrent auxiliary pair satisfies
\[
 \bar H_p-\bar H_q\ge\tau>0. \tag{6}
\]
The limiting gap need not be strictly greater than \(\tau\); its positivity is what is needed.

If infinitely many occurrences of a recurrent ordinary pair ended with \(u_p^{k+1}>0\), Section 1 would give \(G_p^{k+1}=G_q^{k+1}\) along that subsequence, contradicting (5). Therefore all sufficiently late occurrences of that pair set \(u_p^{k+1}=0\). Likewise, all sufficiently late occurrences of a recurrent auxiliary pair set \(v_p^{k+1}=1\) or \(v_q^{k+1}=0\); otherwise their post-update score differences would vanish along a subsequence, contradicting (6).

Because there are finitely many recurrent pairs, one common iteration index suffices for all these assertions. Beyond that index, every ordinary update empties its first coordinate and every auxiliary update reaches at least one of its two relevant endpoints. Increase this index if necessary so that every step magnitude is also less than \(1\), using convergence from Section 2.

## 4. The Missing Boundary-Counting Argument

Define the integer counts
\[
 N_u(k)=\#\{i:u_i^k>0\},\qquad
 N_v(k)=\#\{i:0<v_i^k<1\}.
\]
On the common tail just established, an ordinary update has \(a=u_p^k\). If \(u_q^k>0\), it decreases \(N_u\) by one. If \(u_q^k=0\), it replaces one positive coordinate by another and leaves \(N_u\) unchanged. Auxiliary updates do not change \(u\). Thus \(N_u\) is eventually nonincreasing and, being an integer between zero and \(n\), eventually constant. Thereafter every ordinary update has the form
\[
 (u_p,0)\longmapsto(0,u_p),\qquad u_p>0. \tag{7}
\]

For the auxiliary count, consider all eligible starting configurations of a saturated update:

- If \(0<v_p<1\) and \(0<v_q<1\), at least one selected coordinate becomes a boundary coordinate. Thus \(N_v\) decreases by one or two.
- If \(v_p=0\) and \(0<v_q<1\), saturation forces \(a=v_q\), and the update is \((0,v_q)\mapsto(v_q,0)\). The count \(N_v\) is unchanged.
- If \(0<v_p<1\) and \(v_q=1\), saturation forces \(a=1-v_p\), and the update is \((v_p,1)\mapsto(1,v_p)\). Again \(N_v\) is unchanged.
- If \((v_p,v_q)=(0,1)\), saturation requires \(a=1\), giving \((1,0)\). This cannot occur on the chosen tail because its step magnitude is \(1\).

Ordinary updates leave \(v\) unchanged. Hence \(N_v\) is eventually nonincreasing and eventually constant. This excludes the both-interior starting case on a further common tail. Every remaining auxiliary update is therefore one of
\[
 (0,b)\longmapsto(b,0),\quad 0<b<1,
 \qquad
 (b,1)\longmapsto(1,b),\quad 0<b<1. \tag{8}
\]
This uses the number of interior coordinates, not the number of at-bound coordinates.

For a recurrent ordinary pair, (7) and convergence of both the pre-update and post-update vectors imply \((\bar u_p,\bar u_q)=(0,0)\). If the first auxiliary pattern in (8) occurs infinitely often for a fixed pair, convergence implies \((\bar v_p,\bar v_q)=(0,0)\). If the second occurs infinitely often, it implies \((\bar v_p,\bar v_q)=(1,1)\). Both patterns cannot occur infinitely often for the same pair because the full sequence has a unique limit. Thus each recurrent auxiliary pair eventually has one fixed pattern, with the corresponding limiting corner.

## 5. Recurrent Neighbors and Strict Score Ordering

A pair and its reverse cannot both be recurrent in the same family. For the ordinary family this would give both \(\bar G_p-\bar G_q\ge\tau\) and \(\bar G_q-\bar G_p\ge\tau\), an impossibility. The auxiliary argument uses \(\bar H\) in the same way.

Consider consecutive sufficiently late occurrences of a recurrent ordinary pair \((p,q)\). Immediately after the first occurrence, (7) gives \(u_p=0\) and \(u_q>0\). Before the next occurrence, it gives \(u_p>0\) and \(u_q=0\). Between them, some ordinary update must increase coordinate \(p\); it must be a pair \((r,p)\), because an ordinary update decreases its first coordinate and increases its second. Some ordinary update must also decrease coordinate \(q\); it must be a pair \((q,s)\). Auxiliary updates cannot effect either change. There are infinitely many disjoint intervals between consecutive occurrences and only finitely many possible partners. Consequently some \((r,p)\) and some \((q,s)\) are recurrent ordinary pairs. Self-pairs cannot be selected, and exclusion of the reverse pair gives \(r\ne q\) and \(s\ne p\). Applying (5) to the three pairs yields
\[
 \bar G_r>\bar G_p>\bar G_q>\bar G_s. \tag{9}
\]

For a recurrent auxiliary pair, either pattern in (8) requires coordinate \(p\) to decrease and coordinate \(q\) to increase between consecutive late occurrences. In the lower-corner pattern, \(p\) must return from a positive value to zero and \(q\) from zero to a positive value. In the upper-corner pattern, \(p\) must return from one to a value below one and \(q\) from a value below one to one. Only auxiliary updates change these coordinates. An auxiliary update decreases its second coordinate and increases its first, so the required pairs are respectively \((r,p)\) and \((q,s)\). The same finite-partner argument makes such pairs recurrent, and the reverse pair is again excluded. Thus
\[
 \bar H_r>\bar H_p>\bar H_q>\bar H_s. \tag{10}
\]
Each neighbor satisfies the same already-proved tail properties. For auxiliary neighbors, the shared coordinate's limit also forces the same limiting corner as the original pair.

## 6. Finite Termination

Starting from a recurrent pair, repeatedly apply the predecessor construction in Section 5 within its family. At each extension the limiting score strictly increases. Therefore no index can repeat. After sufficiently many extensions this gives more than \(n\) distinct indices, contradicting the size of the data set. Equivalently, extending at both ends gives the source's indefinitely lengthening strict score chain.

The assumed infinite run is impossible. The algorithm therefore stops after finitely many iterations. Feasibility has been preserved at every step, and the stopping rule says exactly that neither maximum score gap exceeds \(\tau\). The output is consequently \(\tau\)-approximate in the public definition.

## Private Source-Repair Notes

The strict telescoping estimate is applied only to nonempty iteration intervals; the zero-length case is equality. The auxiliary counting passage is repaired by counting interior coordinates, specifying the both-interior case, and treating the corner swap separately. These are local corrections to the supplied source argument, not additional public assumptions. Every listed proof obligation is closed.
