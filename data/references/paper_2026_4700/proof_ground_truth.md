# Reference Proof

## Proof Structure and Obligations

1. Establish the elementary dimension facts needed for restriction and finite-depth witnesses, while preserving a nonempty version space.
2. Derive the lower bound by following a shattered improvement tree, and verify that the resulting finite transcript is compatible with one target fixed throughout the play.
3. Prove the trichotomy for nonempty finite-dimensional version spaces by grafting restriction trees.
4. Analyze all three prediction cases under the strict-improvement response rule and prove dimension decrease after every mistake.
5. Count mistakes, include the boundary cases, and distinguish an unbounded uniform mistake bound from the existence of one infinitely mistaken play.

All obligations below are derived directly from the definitions and the selected source arguments. No external theorem or specialized unproved dependency is used.

## Elementary Facts and Domain

A single-leaf tree is shattered by every nonempty class. Thus a nonempty class has dimension in \(\mathbb N_0\cup\{\infty\}\), whereas the empty class has dimension \(-1\) by convention. If \(W\subseteq V\), every tree shattered by \(W\) is also shattered by \(V\), so
\[
\operatorname{IDim}(W)\leq\operatorname{IDim}(V).
\]
In particular, every label restriction has dimension at most that of its parent class.

A finite dimension \(D\geq0\) is attained: the available depths form a nonempty set of nonnegative integers, and a finite supremum of such a set is its maximum. If a shattered tree has minimum branch length at least \(d\), truncate it at level \(d\). Every node before level \(d\) retains all its outgoing edges. Every branch of the truncated tree extends to a branch of the original finite-height tree, so it remains realizable. The result is a shattered tree all of whose branches have length \(d\). This argument permits infinitely many children at a node and does not assume a bounded graph degree.

On a realizable play, the fixed target \(h^*\) belongs to the initial version space and to every update \(V_{v,y}\), since \(y=h^*(v)\). Correct rounds do not change the maintained version space. Consequently every encountered version space is nonempty, and its dimension is never \(-1\). Empty label restrictions are nevertheless allowed in the maxima and comparisons used by the learner.

## Lower Bound

Fix a deterministic learner \(A\) and a positive integer \(d\) for which \(H\) shatters an improvement tree of depth at least \(d\). Truncate the tree to height exactly \(d\). Present its root instance \(x\), and let \(g\) be the classifier implemented by \(A\).

Choose a permitted best response. Such a response exists because \(x\in\Delta(x)\) and the image of \(\Delta(x)\) under \(g\) lies in the nonempty finite ordered label set.

If the response is to stay at \(x\), the tree has two edges at \(x\) with distinct label components. At least one label differs from \(g(x)\); supply that label and follow its edge.

If the response moves to \(v\ne x\), strict improvement gives \(g(v)\ne z_1\). If the tree has the single edge \((v,z_1)\), supply \(z_1\) and follow it. Otherwise it has two edges at \(v\) with distinct nonminimal labels, at least one of which differs from \(g(v)\). Supply such a label and follow that edge.

In either case a mistake occurs, and its final-feature/label pair is precisely the selected edge label. Repeat from the child reached. This forces a mistake at every one of the \(d\) levels. Every full branch of the tree has a realizing hypothesis, so the completed selected branch has a witness \(h^*\in H\) agreeing with all \(d\) supplied labels.

This argument is compatible with a target fixed throughout the play, not merely with changing targets at each step. For the fixed deterministic learner, simulate the finite construction to obtain its transcript and choose a realizing hypothesis for that completed branch. Now fix that hypothesis before replaying the transcript. Inductively, the learner receives the same presented instance and preceding feedback, hence implements the same classifier; the same best response remains permitted, and the supplied true label equals the fixed hypothesis's value. Thus the simulated transcript is an actual legal play for one fixed target. The target may depend on \(A\) and on \(d\), as permitted by the definition of the worst-case bound.

If \(\operatorname{IDim}(H)=D<\infty\) and \(D>0\), take \(d=D\). When \(D=0\), nonnegativity of mistakes already gives the lower bound. If \(\operatorname{IDim}(H)=\infty\), a witness exists for every finite \(d\), so \(M(A;H,G)=\infty\) for every deterministic learner. This does not assert that a single target and infinite play must force infinitely many mistakes.

## Finite-Dimensional Trichotomy

Let \(V\ne\varnothing\) and \(D=\operatorname{IDim}(V)<\infty\). Fix a presented instance \(x\). Suppose none of the first three conditions in the learner's rule holds.

Failure of the first condition, together with monotonicity, gives
\[
\max_{y\in Y}\operatorname{IDim}(V_{u,y})=D
\qquad\text{for every }u\in\Delta(x).
\]
The maxima exist because \(Y\) is finite. Failure of the second condition supplies two distinct labels at \(x\) whose restrictions both have dimension \(D\).

Consider a proper neighbor \(u\in\Delta(x)\setminus\{x\}\). If \(z_1\) attains its maximum, then \(\operatorname{IDim}(V_{u,z_1})=D\). Otherwise all maximizing labels are nonminimal. There cannot be a unique such label, because that would satisfy the third condition. Hence two distinct nonminimal labels have restriction dimension \(D\).

Build a new root labeled \(x\). Give it the two indicated \(x\)-edges. At each proper neighbor, use the single \(z_1\)-edge when available, and otherwise the two indicated nonminimal-label edges. For each selected edge \((u,y)\), its restriction has finite dimension \(D\), so choose a shattered tree of depth \(D\) and truncate it to height \(D\). Attach that tree below the edge.

The resulting tree has the required outgoing-edge structure and every branch has length \(D+1\). A branch beginning with \((u,y)\) is realized by a hypothesis in \(V_{u,y}\) that realizes its remaining subtree branch; this hypothesis also realizes the first edge. Hence the whole tree is shattered by \(V\), contradicting \(\operatorname{IDim}(V)=D\).

At least one of the first three conditions therefore holds at every nonempty finite-dimensional state. The fallback in the total definition is never used at such a state. The grafting argument also applies to \(D=0\), when the attached trees are single leaves.

## Movement and Dimension Decrease

First handle the one-label case. If \(k=1\), every classifier and target assigns \(z_1\) everywhere. No mistake is possible, and no improvement tree can have an internal node because that would require two distinct labels at that node. Thus every nonempty class has dimension zero. At any presented instance, the first condition fails because \(V_{u,z_1}=V\), and the second condition has its unique label \(z_1\). The learner is well defined and correct.

Now suppose \(k\geq2\), and consider any nonempty version space with finite dimension \(D\).

In the first case, the learner assigns \(z_k\) at the selected \(u\) and \(z_1\) elsewhere. If \(u=x\), no strict improvement is possible and the agent stays at \(u\). If \(u\ne x\), \(u\) is the unique utility-maximizing destination, and its utility is strictly greater than that at \(x\), so the agent moves to \(u\). For every possible revealed label \(y\),
\[
\operatorname{IDim}(V_{u,y})
\leq\max_{b\in Y}\operatorname{IDim}(V_{u,b})<D.
\]
In particular this holds after any mistake.

In the second case, the learner assigns the unique dimension-maximizing label \(a\) at \(x\) and \(z_1\) elsewhere. No point has strictly greater utility than \(x\), including when \(a=z_1\), so the agent stays at \(x\). If a mistake occurs, its true label \(y\ne a\) is not the unique maximizer. Therefore
\[
\operatorname{IDim}(V_{x,y})
<\operatorname{IDim}(V_{x,a})\leq D.
\]

In the third case, the selected proper neighbor \(u\) receives \(a\ne z_1\), and every other point receives \(z_1\). Strict utility ordering makes \(u\) the unique best response. If the revealed label \(y\ne a\) is erroneous, uniqueness of the maximizing label gives
\[
\operatorname{IDim}(V_{u,y})
<\operatorname{IDim}(V_{u,a})\leq D.
\]

These analyses use only the mistake feedback provided in the public task. After a mistake, the update is exactly the restriction just analyzed; after a correct round, the maintained version space is unchanged. Thus every mistake strictly decreases its finite integer dimension, and no intervening correct round increases it.

## Counting and Optimality

Suppose initially \(D_0=\operatorname{IDim}(H)<\infty\). All subsequent version spaces are nonempty subsets of \(H\), so their dimensions remain finite and nonnegative. After \(m\) mistakes, the preceding analysis gives dimension at most \(D_0-m\). Hence \(m\leq D_0\) on every finite play. In particular, when \(D_0=0\), a mistake would require a negative dimension for a nonempty updated class and is impossible. This proves the upper bound without using any observations on correct rounds.

If \(X\) is empty, there are no positive-length legal plays or internal-node trees; the empty play and single-leaf tree give mistake bound and dimension zero, respectively. This is also consistent with the argument above.

The lower bound applies to the dimension-based learner as well as to every other deterministic learner. Consequently its worst-case bound is exactly \(D_0\), and the optimal deterministic bound equals \(D_0\).

If \(\operatorname{IDim}(H)=\infty\), the prediction tests are still defined using dimensions in \(\{-1\}\cup\mathbb N_0\cup\{\infty\}\). The deterministic fallback provides a classifier whenever all three tests fail. Realizability keeps the version space nonempty, and if a later state has finite dimension the finite-state argument applies there. Independently of those subsequent possibilities, the lower bound already proves an unbounded worst-case number of mistakes for every deterministic learner, including this totalized learner. Therefore the optimal value and the learner's worst-case value are both \(\infty\).

Combining the finite and infinite cases proves the requested exact characterization. The previously recorded source repair is retained: the trichotomy is used only at nonempty finite-dimensional states, while infinite-dimensional states are totalized without claiming an infinite-dimensional trichotomy.
