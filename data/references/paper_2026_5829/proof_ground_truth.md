# Reference Proof

## Proof Structure

Fix an arbitrary complete zero-miss labeling. Couple its audit run with runs in which a uniformly chosen set of excluded items is made relevant, keeping all included-pool labels unchanged. This gives the lower bound even for audits that inspect both pools, repeat inspections, and stop adaptively. A uniform without-replacement zero-count audit gives the upper bound.

## Complete Proof

Fix an audit satisfying the two requirements and any complete labeling $y^{(0)}$ with $M_0(y^{(0)})=0$. Probabilities and expectations with subscript $0$ refer to this fixed labeling. Use a common internal random seed $R$ to couple runs under different labelings. This is possible because both the seed law and the measurable history-based audit rule are fixed independently of the labeling.

Let $G$ be the event that the audit reports $\widehat M_0\le m-1$ under $y^{(0)}$. Then $\Pr_0(G)\ge1-\beta$. Let $A_0(R)$ be the set of distinct excluded items inspected in that run, and put $T_0=|A_0(R)|$. Included-pool inspections and repeated inspections do not increase this count.

Independently of $R$, choose a uniformly random $m$-subset $S\subseteq E$. Define $y^{(S)}$ by changing the labels of exactly the items in $S$ from zero to one and leaving every other label, including every included-pool label, unchanged.

For a fixed seed, if $S\cap A_0(R)=\varnothing$, the two runs have identical trajectories. Indeed, their initial histories agree. Whenever their histories agree, the common rule makes the same stopping decision or chooses the same next index. An included item has the same label in both labelings, and an excluded item inspected along the zero-miss trajectory lies outside $S$ and also has the same label. This induction applies to repeated inspections as well. At the almost surely finite termination time of the zero-miss run, both runs stop and give the same report. Null exceptional seeds can be discarded simultaneously for the finitely many planted labelings.

Consequently,
\[
\Pr_{0,S}\bigl(\widehat M_0(R;y^{(S)})\le m-1\bigr)
\ge \Pr_0(G)-\Pr_{0,S}\bigl(G\cap\{S\cap A_0\ne\varnothing\}\bigr).
\]
Conditionally on $A_0$, each of its items belongs to $S$ with probability $m/N_0$. The union bound therefore gives
\[
\Pr_S(S\cap A_0\ne\varnothing\mid A_0)
\le \frac{m|A_0|}{N_0}=\frac{mT_0}{N_0}.
\]
Dropping $G$ from the intersection and averaging yields
\[
\Pr_{0,S}\bigl(\widehat M_0(R;y^{(S)})\le m-1\bigr)
\ge 1-\beta-\frac{m}{N_0}\mathbb E_0[T_0].
\]
For every fixed $S$, the complete labeling $y^{(S)}$ has $M_0=m$. Validity bounds its probability of reporting at most $m-1$ by $\delta$. Averaging this bound over $S$ and rearranging proves
\[
\mathbb E_0[T]\ge(1-\beta-\delta)\frac{N_0}{m}.
\]
The labeling $y^{(0)}$ was arbitrary, so the bound holds for every complete zero-miss labeling.

For achievability, let
\[
n_0=\left\lceil N_0(1-\delta^{1/m})\right\rceil.
\]
Since $0<\delta^{1/m}<1$ and $N_0$ is a positive integer, $1\le n_0\le N_0$. Choose $n_0$ distinct excluded items uniformly without replacement, independently of the labels, and inspect them. Report $m-1$ if all inspected labels are zero, and report $N_0$ otherwise. This is a nonadaptive, terminating audit in the allowed class, and its cost is exactly $n_0$.

For any labeling with $M_0\ge m$, fix a set $S_*$ of $m$ relevant excluded items. Observing only zeros requires that the sample avoid $S_*$. If $n_0>N_0-m$, avoidance is impossible. Otherwise its probability is
\[
\frac{\binom{N_0-m}{n_0}}{\binom{N_0}{n_0}}
=\frac{\binom{N_0-n_0}{m}}{\binom{N_0}{m}}
=\prod_{j=0}^{m-1}\frac{N_0-n_0-j}{N_0-j}
\le\left(1-\frac{n_0}{N_0}\right)^m.
\]
Each factor is nonnegative and equals $1-n_0/(N_0-j)\le1-n_0/N_0$. In the impossible-avoidance case the same upper bound holds because the probability is zero. By the definition of $n_0$,
\[
\left(1-\frac{n_0}{N_0}\right)^m\le\delta.
\]
Since $N_0>m-1$, the event of reporting at most $m-1$ is exactly the zero-count event. Thus the audit is valid for every complete labeling with $M_0\ge m$. For every complete zero-miss labeling, all inspected labels are zero, so success has probability one, regardless of included-pool labels.

It follows that the admissible audit class is nonempty and, for every fixed $y^{(0)}$, its infimum zero-miss expected cost satisfies
\[
(1-\beta-\delta)\frac{N_0}{m}\le C^*\le n_0.
\]
Finally, put $a=\log(1/\delta)/m>0$. The elementary inequality $1-e^{-a}\le a$ and the ceiling bound give
\[
n_0\le N_0(1-e^{-a})+1
\le\frac{N_0}{m}\log(1/\delta)+1
\le\bigl(1+\log(1/\delta)\bigr)\frac{N_0}{m},
\]
where the last inequality uses $m\le N_0$. Since $1-\beta-\delta>1/4$, the lower constant is positive. This proves the full displayed bounds and $C^*=\Theta(N_0/m)$, with constants depending only on $\beta,\delta$, uniformly over the choice of complete zero-miss labeling.
