# Reference Proof

## Proof Structure

1. Derive the exact affine inventory perturbation and its maximum over the catalog.
2. Identify the signed-hull support function, verify that the score itself belongs to the certificate class, and establish minimality and the polar equality characterization.
3. Apply the conditional exchangeability argument to the block-specific scores, treating ties and the infinite-quantile case explicitly.
4. Use the assumed simultaneous component event to establish feasibility and regret against the realized-value optimum, including empty feasible sets and infinite component radii.

## Complete Proof

### 1. Operational characterization

Fix a nominal pair $(u_0,\lambda_0)$, with $u_0=(z_0,\tau_0,m_0)$. For each $\pi\in\Pi$, affineness gives a constant $c_\pi$ such that
\[
L(\pi;(z,\tau_0,m_0),\lambda_0)=c_\pi+\langle w_\pi,z\rangle.
\]
Consequently, for every $e\in\mathbb R^d$,
\[
L(\pi;(z_0+e,\tau_0,m_0),\lambda_0)-L(\pi;u_0,\lambda_0)=\langle w_\pi,e\rangle.
\]
Taking absolute values and the maximum over the nonempty finite catalog proves the operational identity. This calculation is pointwise in the nominal pair, so it also applies separately at each block's nominal pair. It does not require sensitivities to agree across blocks.

### 2. Support function and minimality

The set $W$ is a nonempty compact convex set, being the convex hull of finitely many vectors. A linear functional evaluated at any convex combination of its generators is no larger than its maximum over those generators. Conversely, every generator belongs to $W$. Hence
\[
\sigma_W(e)=\max_{\pi\in\Pi}\max\{\langle w_\pi,e\rangle,-\langle w_\pi,e\rangle\}=\Phi(e).
\]
The function $\Phi$ is finite and continuous, since it is the maximum of finitely many continuous linear functions. It is nonnegative, positively homogeneous for nonnegative scalars, and subadditive: the triangle inequality for each inner product gives
\[
\Phi(e+f)\le\Phi(e)+\Phi(f).
\]
By the operational identity, $\Phi$ therefore belongs to the stated class of valid certificates.

Let $B$ be any certificate in that class, and define
\[
K_B=\{v\in\mathbb R^d:\langle v,e\rangle\le B(e)\text{ for every }e\in\mathbb R^d\}.
\]
Operational validity and the affine identity imply
\[
|\langle w_\pi,e\rangle|\le B(e)
\quad\text{for every }\pi,e.
\]
Thus $B\ge0$, and both $w_\pi$ and $-w_\pi$ belong to $K_B$. The set $K_B$ is closed and convex as an intersection of closed halfspaces, and it is nonempty because it contains the signed generators, as well as zero. Convexity gives $W\subseteq K_B$.

We use the audited standard independent result recorded as theory_017: a proper lower-semicontinuous sublinear function on a finite-dimensional real vector space is the support function of the closed convex set of linear functionals it dominates. Support functions are monotone under inclusion and determine nonempty closed convex sets uniquely. Its hypotheses hold here: $B$ is finite, hence proper, lower-semicontinuous by assumption, and convex by sublinearity. Therefore
\[
B=\sigma_{K_B},\qquad \Phi=\sigma_W\le\sigma_{K_B}=B.
\]
Together with the admissibility of $\Phi$, this proves pointwise minimality. If $B=\Phi$ everywhere, then $\sigma_{K_B}=\sigma_W$, and uniqueness for nonempty closed convex sets yields $K_B=W$. Conversely, $K_B=W$ gives $B=\sigma_W=\Phi$.

No full-dimensionality or nonzero-sensitivity assumption was used. In particular, when every sensitivity vanishes, $W=\{0\}$ and $\Phi=0$, and the same proof applies.

### 3. Conformal calibration

Let $N=n+1$, and label the next-block score as $S_N=S_{\mathrm{next}}$. Conditional on $\mathcal H$, the $N$ scores are exchangeable by the public assumption. These are the scores formed with their respective block-specific nominal worlds and dual prices. We do not additionally condition on the realized list of those block-specific nominal outputs.

For completeness, the exchangeability rank result recorded as theory_015 can be derived as follows. Adjoin independent identically distributed continuous auxiliary variables $U_1,\ldots,U_N$, independent of the scores and $\mathcal H$, and order the pairs $(S_i,U_i)$ lexicographically. There are almost surely no tied pairs. Conditional exchangeability and permutation symmetry imply that the rank $R_N$ of the last pair is uniform on $\{1,\ldots,N\}$: for each rank, exactly one pair occupies it, and every index has the same conditional probability of doing so.

Suppose first that $r\le n$. If $S_N$ were larger than the $r$th calibration order statistic, at least $r$ calibration scores would be strictly smaller than $S_N$, forcing $R_N>r$. Therefore
\[
\{R_N\le r\}\subseteq\{S_N\le\hat q\}.
\]
It follows that, almost surely,
\[
\Pr(S_N\le\hat q\mid\mathcal H)\ge\frac{r}{N}\ge1-\alpha.
\]
If $r=N$, the prescribed radius is $+\infty$, and the event has probability one because the scores are finite. Taking expectations of these conditional bounds proves the asserted unconditional coverage. The auxiliary variables are only a proof device; the actual procedure uses the unrandomized order statistic, and ties require no continuity assumption on the score distribution.

### 4. Robust feasibility and regret

Let $E$ be the public simultaneous component event. Its probability lower bound is assumed directly. The component scores and their radii are defined by their own calibration recipe; the proof does not derive their joint event from the combined Lagrangian score, nor does it impose an additional independence or concentration assumption.

Work on $E$. If $\mathcal F$ is empty, there is no robust-selector policy output and no policy-comparison assertion to prove. Otherwise any output $\hat\pi\in\mathcal F$ satisfies, for each $j\in\mathcal J$,
\[
g_j(\hat\pi;u_*)\le\hat g_j(\hat\pi)+\Delta_{g,j}(\hat\pi)\le0.
\]
This proves realized feasibility. If $\mathcal J$ is empty, feasibility is vacuous, while the separately quantified value part of $E$ remains available.

Since $\mathcal F$ is a nonempty finite set and all realized values are real, a realized-value maximizer $\pi_*^{\mathrm{rob}}$ exists. This is a comparison policy, not information made available to the selector.

Write
\[
D=\sup_{\pi\in\Pi}\Delta_V(\pi)\in[0,+\infty].
\]
If $D=+\infty$, the desired regret inequality holds immediately: its left side is the difference of two real numbers and its right side is $+\infty$. In particular, no cancellation of infinite robust objectives is needed.

Now suppose $D<\infty$, and define, for this proof,
\[
R(\pi)=\hat V(\pi)-\Delta_V(\pi).
\]
All these quantities are real. Approximate optimization gives
\[
R(\hat\pi)\ge R(\pi)-\varepsilon_{\mathrm{opt}}\quad\text{for every }\pi\in\mathcal F.
\]
On $E$, the value inequalities hold simultaneously for every catalog policy. For any $\pi\in\mathcal F$, including the realized-value maximizer, they give
\[
\begin{aligned}
V(\pi;u_*)-V(\hat\pi;u_*)
&\le \hat V(\pi)+\Delta_V(\pi)-R(\hat\pi)\\
&\le \hat V(\pi)+\Delta_V(\pi)-R(\pi)+\varepsilon_{\mathrm{opt}}\\
&=2\Delta_V(\pi)+\varepsilon_{\mathrm{opt}}\\
&\le2D+\varepsilon_{\mathrm{opt}}.
\end{aligned}
\]
Taking $\pi=\pi_*^{\mathrm{rob}}$ proves the requested comparison. The proof does not require that this comparator maximize the robust objective.

These implications hold pointwise on the same event $E$, whose probability is at least $1-\alpha-\alpha_\tau-\alpha_m$. This is an unconditional common-event guarantee, not a claim about coverage conditional on the selector producing an output.

## Obligation Closure

The affine identity, support calculation, admissibility of the score, and robust comparisons are derived explicitly. Polar representation and support-function uniqueness use theory_017 with their hypotheses checked. The exchangeability rank guarantee in theory_015 is also derived explicitly, including ties and the infinite-quantile convention. The joint component event is a stated hypothesis, not an unproved theorem. No nonstandard dependency or unresolved proof obligation remains.
