# Reference Proof

## Proof obligations

The proof establishes: (1) conditional Gaussian regression and the empirical-moment strong laws; (2) probability-zero equality for every fixed shallow predictor, not merely failure of almost-sure equality; (3) the recurrence and fixed-depth readout limit, including vanishing residuals without bounded individual embeddings; (4) existence of the source-defined population-loss limit and its scalar expression; (5) strict convexity, coercivity, and global gradient-flow convergence; (6) convergence of the depth-dependent minimizers; and (7) almost-sure prediction convergence in the prescribed sequential limits. All obligations are closed below.

## 1. Regression and context limits

Put $Z=1+\|m\|^2$ and $\Lambda=I_d+mm^\top$. Conditional on $(m,\zeta)$, the token pairs, including the query, are independent centered Gaussian vectors with covariance
\[
\begin{pmatrix}\Lambda&\zeta m\\ \zeta m^\top&\zeta^2\end{pmatrix}.
\]
Direct multiplication gives $\Lambda^{-1}=I_d-mm^\top/Z$. Consequently, for $w=\zeta m/Z$ and $\varepsilon_i=y_i-w^\top x_i$, the residual has conditional variance $\zeta^2/Z$ and zero conditional covariance with $x_i$. Joint Gaussianity gives conditional independence. Across tokens the residuals are independent, and the entire residual sequence is independent of the entire covariate sequence conditional on $(m,\zeta)$. The same statements hold for the query residual. Thus $\mathbb E[y_q\mid m,\zeta,x_q]=w^\top x_q$.

The scalar strong law states that averages of iid integrable random variables converge almost surely to their expectation. Apply it conditionally on $(m,\zeta)$ to every coordinate of the following products, whose conditional moments are finite. Since $d$ is fixed, it yields
\[
S_L:=XX^\top/L\to\Lambda,\qquad Xy/L\to\zeta m,\qquad \|y\|^2/L\to\zeta^2,\qquad X\varepsilon/L\to0
\]
almost surely, also in the appropriate matrix norms. Integrating the conditional probability-one statement gives an unconditional probability-one event.

Absolute continuity of the law of $m$ implies $\mathbb P(m=0)=0$ and $\mathbb P(\|m\|=r)=0$ for every fixed $r$: each sphere has Lebesgue measure zero. In particular, $Z$ is atomless and $Z>1$ almost surely. Write $a=1+\underline m$ and $b=1+\overline m$, so $1\le a<b<\infty$ and $a\le Z\le b$ almost surely.

## 2. Shallow impossibility

Fix the two weight matrices. Write the last row of $W^{PV}$ as $(h^\top,v)$, and write the first $d$ columns of $W^{KQ}$ as $(A^\top,b_0)^\top$, meaning that their upper block is $A\in\mathbb R^{d\times d}$ and lower row is $b_0^\top$.

The exact prediction is
\[
\frac1L\sum_{i=1}^L(h^\top x_i+vy_i)(x_i^\top A+y_i b_0^\top)x_q
+\frac{(h^\top x_q)(x_q^\top A x_q)}L.
\]
The second term vanishes because the query is fixed as $L$ grows. The context strong laws give the limiting coefficient
\[
g(m,\zeta)=A^\top\Lambda h+\zeta\{b_0(h^\top m)+vA^\top m\}+\zeta^2vb_0.
\]
Let $B=h b_0^\top+vA$. Then
\[
g(m,\zeta)-w=A^\top\Lambda h+\zeta(B^\top m-m/Z)+\zeta^2vb_0.
\]
The event $\{m=0\}\cup\{Z^{-1}\in\sigma(B)\}$ is null: $Z^{-1}$ is atomless and a fixed finite-dimensional matrix has a finite spectrum. Outside this event, $B^\top m-m/Z\ne0$. Hence the displayed vector polynomial in $\zeta$ is not identically zero. At least one scalar component is a nonzero polynomial of degree at most two and has only finitely many roots. Independence of $m$ and $\zeta$, together with atomlessness of $\zeta$, gives
\[
\mathbb P(g(m,\zeta)=w)=0.
\]
Finally, condition on $(m,\zeta)$. If $g-w\ne0$, then $(g-w)^\top x_q$ is a centered Gaussian with strictly positive variance $(g-w)^\top\Lambda(g-w)$, and so has zero probability of being zero. Combining this fact with the almost-sure context limit proves the required probability-zero prediction equality.

This argument does not equate coefficients merely because equality holds at one realized scalar value; it treats the conditional root event explicitly.

## 3. Recurrence and readout

For arbitrary fixed scalars $(\alpha,\beta)$, let $M_L=I_d+\beta S_L$. Induction in positive integer depth gives
\[
F_T=\alpha\sum_{k=0}^{T-1}M_L^kX.
\]
Since $S_L$ and $M_L$ commute and are symmetric,
\[
XF_T^\top/L=\alpha S_L\sum_{k=0}^{T-1}M_L^k
=\frac\alpha\beta(M_L^T-I_d)\quad(\beta\ne0).
\]
When $\beta=0$, the undivided polynomial expression gives $F_T=\alpha T X$.

For $\beta=-\alpha$, define the matrix polynomial
\[
P_T(S)=\alpha\sum_{k=0}^{T-1}(I_d-\alpha S)^k.
\]
For every real $\alpha$, including zero,
\[
F_T=P_T(S_L)X,\qquad S_LP_T(S_L)=I_d-(I_d-\alpha S_L)^T.
\]
Using $y=X^\top w+\varepsilon$, the readout therefore equals
\[
\widehat y_{L,T,\alpha,-\alpha}
=w^\top[I_d-(I_d-\alpha S_L)^T]x_q
+(X\varepsilon/L)^\top P_T(S_L)x_q.
\]
At fixed $T$ and $\alpha$, polynomial continuity and the strong laws show that the second term tends to zero and that
\[
\widehat y_{L,T,\alpha,-\alpha}\longrightarrow
w^\top Q_T(\alpha)x_q,\qquad Q_T(\alpha)=I_d-(I_d-\alpha\Lambda)^T
\]
almost surely. No bound on $\sup_i\|f_i\|$ is needed.

For completeness, the source's bounded-embedding residual assertion can also be justified without an iid assumption on the products. Conditional on the entire covariate sequence and $(m,\zeta)$, a residual average with X-measurable coefficients bounded by a finite constant $C$ is Gaussian with coordinate variance at most $(\zeta^2/Z)C^2/L$. Its fixed-threshold tail probabilities are summable in $L$. The elementary Borel-Cantelli implication then gives almost-sure convergence. This auxiliary boundedness argument is not used for the polynomial embeddings above.

## 4. Population-loss limit and scalar objective

We first verify the order of limit and expectation in the public definition. Fix $T$ and $\alpha$. Let $u=(u_1,\ldots,u_L)^\top$ and $c_L=Xu/L$. Since $y=\zeta u$,
\[
\widehat y_{L,T,\alpha,-\alpha}-y_q
=\zeta R_L,\qquad R_L=c_L^\top P_T(S_L)x_q-u_q.
\]
The variable $\zeta$ is independent of all variables in $R_L$ and has second moment one. Thus the finite-context population loss is $\mathbb E[R_L^2]$.

Here is a uniform-integrability justification requiring no fourth moment of $\zeta$. Put
\[
H_L=1+\frac1L\sum_{i=1}^L(u_i^2+\|\mu_i\|^2),\qquad G_q=|u_q|+\|\mu_q\|.
\]
Boundedness of $m$, Cauchy-Schwarz, and the polynomial degree of $P_T$ give constants depending only on $d,\overline m,T,\alpha$ such that
\[
\|S_L\|\le C H_L,\quad \|c_L\|\le C H_L,\quad
\|P_T(S_L)\|\le C H_L^{T-1},\quad |R_L|\le C H_L^T G_q.
\]
All Gaussian moments are finite. For every fixed integer $k\ge1$, Jensen's inequality bounds $\sup_L\mathbb E[H_L^k]$ by a finite constant. The query Gaussians are independent of the context Gaussians. Consequently $\sup_L\mathbb E[|R_L|^4]<\infty$. The almost-sure convergence $S_L\to\Lambda$ and $c_L\to m$ gives $R_L\to R=m^\top P_T(\Lambda)x_q-u_q$ almost surely. The fourth-moment bound makes $R_L^2$ uniformly integrable, so $\mathbb E[R_L^2]\to\mathbb E[R^2]$. This follows, for example, by truncating the squares and bounding their tails by the fourth-moment bound. Thus the source-defined loss limit exists and equals the expected squared error of the limiting predictor.

Conditional on $(m,\zeta)$, that error is
\[
-w^\top(I_d-\alpha\Lambda)^T x_q-\varepsilon_q.
\]
Its cross term has mean zero. Since $\Lambda m=Zm$,
\[
\mathbb E[(w^\top(I_d-\alpha\Lambda)^T x_q)^2\mid m,\zeta]
=\zeta^2\frac{Z-1}{Z}(1-\alpha Z)^{2T}.
\]
The residual variance is $\zeta^2/Z$. Independence and $\mathbb E[\zeta^2]=1$ therefore yield
\[
\ell_T(\alpha)=\mathbb E\left[\frac1Z+\frac{Z-1}{Z}(1-\alpha Z)^{2T}\right].
\]

An exact finite-context check also identifies the local algebra correction needed in the source. With $M_L=I_d-\alpha S_L$ and $P=P_T(S_L)$, conditioning on $(m,\zeta,X)$ gives
\[
\mathbb E[(\widehat y-y_q)^2\mid m,\zeta,X]
=w^\top M_L^T\Lambda M_L^T w+\frac{\zeta^2}{Z}
+\frac{\zeta^2}{ZL}\operatorname{tr}(\Lambda P S_L P).
\]
Here $M_L^T$ denotes the depth power, not a transpose. There is no need, and generally no permission, to commute $S_L$ with $\Lambda$. The preceding moment bounds justify the limit of this expression as well.

## 5. Minimization and gradient flow

Write $W=(Z-1)/Z$. Almost surely $W>0$. For every such $Z$, the function $\alpha\mapsto W(1-\alpha Z)^{2T}$ is strictly convex. Integrating its strict convexity inequality gives strict convexity of $\ell_T$. Its leading coefficient as a polynomial of degree $2T$ is $\mathbb E[WZ^{2T}]>0$, so it is coercive. All coefficients are finite because $Z$ is bounded.

Differentiation gives
\[
\ell_T'(\alpha)=-2T\mathbb E[(Z-1)(1-\alpha Z)^{2T-1}].
\]
This is strictly negative for $\alpha\le0$ and strictly positive for $\alpha\ge1$, because $Z>1$ almost surely. Continuity, coercivity, and strict convexity imply a unique critical point and global minimizer $\alpha_T^*\in(0,1)$.

For fixed $T$, the polynomial vector field $-\ell_T'$ is locally Lipschitz. The local solution of the scalar ODE is unique. Along it,
\[
\frac{d}{ds}\ell_T(\alpha_s)=-\ell_T'(\alpha_s)^2.
\]
The trajectory stays in the compact sublevel set determined by its initialization. A solution of a locally Lipschitz ODE that stays in such a compact set extends for all $s\ge0$: the vector field is bounded and Lipschitz on a neighborhood of that set, preventing a finite-time escape and allowing continuation.

Set $h(s)=\ell_T'(\alpha_s)^2$. The dissipation identity gives $\int_0^\infty h(s)\,ds<\infty$. Moreover,
\[
h'(s)=-2\ell_T'(\alpha_s)^2\ell_T''(\alpha_s),
\]
which is bounded on the compact sublevel set. Thus $h$ is uniformly continuous. The relevant form of Barbalat's lemma says that a nonnegative, uniformly continuous, integrable function on $[0,\infty)$ tends to zero. To see it directly, if values stayed above a fixed positive threshold at arbitrarily large times, uniform continuity would give disjoint intervals of a fixed positive length with a fixed positive lower bound, contradicting integrability. Hence $\ell_T'(\alpha_s)\to0$.

Every accumulation point of the compact trajectory is therefore the unique zero $\alpha_T^*$. If the trajectory did not converge to it, a sequence staying a positive distance away would have a different accumulation point. This contradiction proves convergence from every real initialization.

## 6. Depth limit of the minimizers

Define
\[
f_T(\alpha)=\left(\mathbb E[W|1-\alpha Z|^{2T}]\right)^{1/(2T)},\qquad
\phi(\alpha)=\operatorname*{ess\,sup}|1-\alpha Z|.
\]
The essential endpoints $a,b$ and continuity of $z\mapsto|1-\alpha z|$ imply
\[
\phi(\alpha)=\max\{|1-\alpha a|,|1-\alpha b|\}.
\]
For the upper bound, use $a\le Z\le b$ and convexity in $z$. For the reverse inequality, every neighborhood of either essential endpoint has positive probability. This does not require the support to fill the interval.

For fixed $\alpha$,
\[
f_T(\alpha)\le\mathbb E[W]^{1/(2T)}\phi(\alpha),
\]
so $\limsup_T f_T(\alpha)\le\phi(\alpha)$.

For the needed moving-parameter lower bound, let $\alpha_T\to\alpha$. Since $a<b$, $\phi(\alpha)>0$. Fix $0<\eta<\phi(\alpha)$ and set
\[
A=\{|1-\alpha Z|>\phi(\alpha)-\eta/2\}.
\]
This event has positive probability, and $c=\mathbb E[W\mathbf1_A]>0$ because $W>0$ almost surely. For all sufficiently large $T$, $b|\alpha_T-\alpha|<\eta/2$, and hence on $A$,
\[
|1-\alpha_T Z|\ge\phi(\alpha)-\eta>0.
\]
Consequently
\[
f_T(\alpha_T)\ge c^{1/(2T)}(\phi(\alpha)-\eta).
\]
Taking the lower limit and then $\eta\downarrow0$ proves $\liminf_T f_T(\alpha_T)\ge\phi(\alpha)$. This also handles $a=1$, where $W$ is not bounded away from zero.

Let $\alpha_*=2/(a+b)$ and $\rho=(b-a)/(a+b)$. At $\alpha_*$ the two endpoint magnitudes equal $\rho$. If $\alpha<\alpha_*$, then $\phi(\alpha)\ge1-\alpha a>\rho$; if $\alpha>\alpha_*$, then $\phi(\alpha)\ge\alpha b-1>\rho$. Thus $\alpha_*$ is the unique global minimizer of $\phi$.

The minimizers $\alpha_T^*$ lie in $(0,1)$ and also minimize $f_T$. For any convergent subsequence $\alpha_{T_k}^*\to\bar\alpha$, the lower bound and optimality give
\[
\phi(\bar\alpha)\le\liminf_k f_{T_k}(\alpha_{T_k}^*)
\le\limsup_k f_{T_k}(\alpha_{T_k}^*)
\le\limsup_k f_{T_k}(\alpha_*)\le\phi(\alpha_*).
\]
Uniqueness implies $\bar\alpha=\alpha_*$. Compactness then proves convergence of the entire sequence, namely
\[
\alpha_T^*\to\frac{2}{a+b}=\frac{2}{2+\underline m+\overline m}.
\]

## 7. Trained prediction in sequential limits

The limit $\alpha_*$ lies strictly inside $(0,2/b)$. Choose a compact interval $K$ containing it in its interior and contained in $(0,2/b)$. For all sufficiently large $T$, $\alpha_T^*\in K$. Every eigenvalue of $\Lambda$ lies in $[1,b]$, and
\[
q:=\max_{\gamma\in K,\lambda\in[1,b]}|1-\gamma\lambda|<1.
\]
Thus, uniformly over all admissible prompts,
\[
\|(I_d-\alpha_T^*\Lambda)^T\|\le q^T\to0.
\]
The fixed-depth readout limit from Section 3 holds on a probability-one event for every positive integer depth; take a countable intersection if necessary. On this event,
\[
\lim_{L\to\infty}\widehat y_{L,T,\alpha_T^*,-\alpha_T^*}
=w^\top[I_d-(I_d-\alpha_T^*\Lambda)^T]x_q.
\]
Since $w$ and the fixed query are finite almost surely, the uniform contraction gives
\[
\lim_{T\to\infty}\lim_{L\to\infty}\widehat y_{L,T,\alpha_T^*,-\alpha_T^*}
=w^\top x_q=y_q^{\mathrm{Bayes}}\quad\text{almost surely}.
\]

## Source-repair accounting

The conditional polynomial-root argument repairs the event-level coefficient comparison in theory_004. The conditional Gaussian-tail argument and the architecture-specific factorization repair the residual application in theory_010. The exact conditional finite-context variance and the moment argument repair theory_012. The positive-base weighted-event estimate and uniform contraction repair theory_014. These corrections preserve the selected source claims and leave no unresolved reference-proof obligation.
