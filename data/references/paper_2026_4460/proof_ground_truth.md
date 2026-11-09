# Reference Proof

## Proof Structure

Consistency makes every masked disagreement have empirical mean zero. For a fixed group, its disagreement patterns are controlled by the restrictions of H to that group. For varying groups, first partition by the group trace on the finite set of points, then use one representative group for each trace to bound the available hypothesis patterns. Apply the relative VC inequality and Sauer's lemma. The concentration events are separate for the fixed-group and simultaneous guarantees.

## Standard-Independent Results Used

For a nonempty measurable binary class F on a domain Z, an iid sample z_1,...,z_n from a probability distribution Q, n >= 1, and delta in (0,1), put
\[
Q_n f=\frac1n\sum_{i=1}^n f(z_i),\qquad
\alpha=\frac4n\log\frac{4S_Z(F,2n)}{\delta}.
\]
The relative VC inequality states that, with probability at least 1-delta, simultaneously for every f in F,
\[
Qf\le Q_n f+\sqrt{\alpha Qf}.
\]
This is the division-free form of the source's relative uniform-convergence inequality. For Qf>0 the forms are equivalent, and for Qf=0 the displayed inequality is automatic. The assumed measurability of the relevant class-indexed events permits the probability assertion. Since F is nonempty and binary, 1 <= S_Z(F,2n) <= 2^{2n}, so alpha is finite and nonnegative.

Sauer's lemma states that a binary class of finite VC dimension d has at most
\[
\sum_{j=0}^{\min(d,k)}\binom{k}{j}
\]
restriction patterns on k points. For infinite VC dimension the elementary bound 2^k supplies the same formula under the public convention. This includes k=0 for nonempty classes. Taking suprema over sets of at most m points gives the corresponding growth-function bound with m in place of k.

These results are the standard-independent dependencies theory_006 and theory_007. No paper-specific result is being assumed without proof.

## Complete Proof

Fix the objects and parameters in the setup. Write
\[
P_n f=\frac1n\sum_{i=1}^n f(x_i).
\]
For a group g and a concept c in C_{G,H}, define
\[
f_{g,c}(x)=\mathbf 1\{x\in g\}\mathbf 1\{c(x)\ne c^*(x)\}.
\]
These are measurable binary functions. Their population means are exactly the joint errors in the targets. Whenever c is consistent with S, every summand defining P_n f_{g,c} is zero, so P_n f_{g,c}=0.

If G is empty, both group-indexed assertions are vacuous, as is the conditional-error conclusion. Hence suppose G is nonempty. The existence of c* in C_{G,H} then implies that H is nonempty: apply the defining condition to any group, including an empty group if that is the only available group.

### Fixed group

Fix g in G before drawing the sample and let
\[
F_g=\{f_{g,c}:c\in C_{G,H}\}.
\]
This is a nonempty class, since c* belongs to C_{G,H}. Consider any finite A subset X with |A| <= 2n and put I=A intersect g. Every trace of a member of F_g is zero outside I. On I, the definition of C_{G,H} supplies an h in H whose values agree with c. The map from the h-labels on I to disagreement labels with the fixed c*-labels is a fixed bijective relabeling. Therefore
\[
|F_g|_A|\le |H|_I|\le S_g(H|_g,2n)
\le \binom{2n}{\le d_{g,H}}.
\]
Here |F_g|_A| denotes the number of distinct restrictions to A, and similarly for H. If I is empty there is exactly one masked trace, so the same inequality holds. The public growth-function convention also covers an empty domain g. The last inequality is Sauer's lemma for finite dimension and the binary-pattern bound for infinite dimension. Thus
\[
S_X(F_g,2n)\le\binom{2n}{\le d_{g,H}}.
\]

Apply the relative VC inequality to the fixed class F_g, the iid sample from P, and confidence parameter delta. All hypotheses have been checked: n is positive, delta lies in (0,1), F_g is nonempty and binary, and the measurability assumptions apply. On its probability-at-least-1-delta event, every consistent c satisfies, with t=P f_{g,c},
\[
t\le\sqrt{\alpha_g t},\qquad
\alpha_g=\frac4n\log\frac{4S_X(F_g,2n)}{\delta}.
\]
If t=0 the desired conclusion is immediate. If t>0, division by sqrt(t) and squaring give t <= alpha_g. Substituting the growth bound proves (a). The event is uniform in c but is asserted separately for each fixed g; no simultaneous fixed-group event is claimed.

### All groups simultaneously

Let
\[
F=\{f_{g,c}:g\in G,\ c\in C_{G,H}\}.
\]
Because G is nonempty, this is again a nonempty measurable binary class. Fix a finite A subset X with |A| <= 2n. Partition the pairs (g,c) by the mask I=A intersect g. There are at most S_X(G,2n) such masks.

For each realized mask I, choose one representative group g_I with A intersect g_I=I. For every pair (g,c) producing this mask, its masked disagreement on A is zero outside I. Its values on I come from some h in H, followed by fixed relabeling with c*. Crucially, I is also contained in g_I; consequently the entire union of possible patterns for this mask is bounded by the restrictions of H to I, regardless of which group produced the mask. Hence the number of patterns for this mask is at most
\[
S_{g_I}(H|_{g_I},2n)
\le\sup_{g\in G}S_g(H|_g,2n).
\]
If I is empty its contribution is one pattern, which also satisfies this bound. Summing over masks gives
\[
S_X(F,2n)
\le S_X(G,2n)\sup_{g\in G}S_g(H|_g,2n)
\le \binom{2n}{\le d_G}\binom{2n}{\le d_H^{\mathrm{sup}}}.
\]
The final step uses Sauer's lemma, monotonicity of the binomial sum in its dimension argument, and the elementary binary-pattern bound when a dimension is infinite.

Apply the relative VC inequality once to F with confidence delta. Its hypotheses hold for the same reasons as above. On the resulting single event, every g in G and every consistent c satisfy
\[
P f_{g,c}\le P_n f_{g,c}+\sqrt{\alpha P f_{g,c}}
=\sqrt{\alpha P f_{g,c}},
\qquad
\alpha=\frac4n\log\frac{4S_X(F,2n)}{\delta}.
\]
The same zero-or-positive case split yields P f_{g,c} <= alpha. Substituting the product growth bound proves (b), uniformly over both g and consistent c. This derivation also covers infinite dimensions under the binomial convention; alternatively, if either dimension is infinite, the right-hand side is greater than 1 and the conclusion is immediate.

Finally, for P(g)>0,
\[
\operatorname{err}_g(c)=\frac{P f_{g,c}}{P(g)}.
\]
Dividing the appropriate joint bound by P(g) gives its conditional-error counterpart without changing its probability event. No division is made for zero-mass groups. The events used for (a) and (b) each have probability at least 1-delta; their intersection is not asserted to have that same probability.

## Obligation Closure

The masked-disagreement representation and zero empirical error were derived from consistency and the concept-class definition. The fixed-group and varying-group growth bounds were derived explicitly, including the representative-group argument and empty traces. The two external inequalities were stated with the hypotheses verified at their applications. The final algebra, probability quantifiers, infinite dimensions, empty families, and conditional-error conversion were all handled. No unresolved private proof obligation remains.
