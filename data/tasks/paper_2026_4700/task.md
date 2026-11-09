# Problem

## Setup

Let \(X\) be a discrete instance set, let \(k\geq 1\) be an integer, and let \(Y=\{z_1,\ldots,z_k\}\) be a finite set of distinct labels with utility function \(\operatorname{Val}:Y\to\mathbb R\) satisfying \(\operatorname{Val}(z_1)<\cdots<\operatorname{Val}(z_k)\). Let \(\varnothing\ne H\subseteq Y^X\). Fix an unweighted directed graph \(G=(X,E)\) containing every self-loop, and define \(\Delta(x)=\{v\in X:(x,v)\in E\}\). The class \(H\), graph \(G\), and utility ordering are known to the learner. Movement along an edge has zero cost.

An unknown target \(h^*\in H\) is fixed throughout a play. In each round, the environment presents an instance \(x\), after which the learner implements an arbitrary classifier \(g:X\to Y\), not necessarily in \(H\). If \(\max_{u\in\Delta(x)}\operatorname{Val}(g(u))=\operatorname{Val}(g(x))\), the agent stays at \(v=x\). Otherwise, the agent chooses a maximizer \(v\in\Delta(x)\), with ties allowed to be resolved adversarially. The true label is \(y=h^*(v)\), and the loss is \(\mathbf 1[g(v)\ne y]\). The learner observes whether it made a mistake and, on a mistaken round, also receives \((v,y)\). On a correct round its feedback is just the correctness indicator. Its classifier choices may depend on the known setup, its preceding observations and choices, and the current presented instance, but not on the unknown target or unrevealed outcomes. Presented instances may be chosen adaptively, before the corresponding classifier is implemented.

For a deterministic learner \(A\), let \(M(A;H,G)\) be the supremum of its total mistakes over all finite legal plays, including the empty play, all fixed choices of \(h^*\in H\), all presented-instance sequences, and all permitted best-response tie choices. This supremum takes values in \(\mathbb N_0\cup\{\infty\}\). Define the optimal worst-case mistake bound by
\[
M^*(H,G)=\inf_{A\text{ deterministic}}M(A;H,G).
\]

An improvement tree has finite height, but need not have finitely many nodes. Each internal node is labeled by an instance \(x\), and its outgoing edges consist of:

- two edges labeled \((x,a)\) and \((x,b)\), where \(a,b\in Y\) and \(a\ne b\);
- for each \(v\in\Delta(x)\setminus\{x\}\), either one edge labeled \((v,z_1)\), or two edges labeled \((v,a_v)\) and \((v,b_v)\), where \(a_v,b_v\in Y\setminus\{z_1\}\) and \(a_v\ne b_v\).

A branch with edge labels \((u_1,y_1),\ldots,(u_m,y_m)\) is realized by a hypothesis \(h\) if \(h(u_i)=y_i\) for every \(i\). A tree is shattered by \(V\subseteq H\) if every root-to-leaf branch is realized by some \(h\in V\); the realizing hypothesis may differ between branches. The tree consisting of a single leaf is allowed and has depth zero. The depth of a tree is the minimum number of edges on a root-to-leaf branch. For nonempty \(V\), define \(\operatorname{IDim}(V)\) as the supremum of the depths of improvement trees shattered by \(V\), with value \(\infty\) when these finite depths are unbounded. Set \(\operatorname{IDim}(\varnothing)=-1\).

The dimension-based learner maintains a version space \(V\), initially \(H\), consisting of the hypotheses agreeing with all revealed pairs. Write \(V_{u,y}=\{h\in V:h(u)=y\}\). At a presented instance \(x\), put \(D=\operatorname{IDim}(V)\), allowing \(D=\infty\), and use the following priority rule. In each of the first three cases, assign \(z_1\) to every point not otherwise assigned a label.

1. If some \(u\in\Delta(x)\) satisfies \(\max_{y\in Y}\operatorname{IDim}(V_{u,y})<D\), choose such a \(u\) and assign \(z_k\) at \(u\).
2. Otherwise, if \(y\mapsto\operatorname{IDim}(V_{x,y})\) has a unique maximizing label \(a\), assign \(a\) at \(x\).
3. Otherwise, if some \(u\in\Delta(x)\setminus\{x\}\) has a unique maximizing label \(a\ne z_1\) for \(y\mapsto\operatorname{IDim}(V_{u,y})\), choose such a pair \((u,a)\) and assign \(a\) at \(u\).
4. If none of these conditions holds, use any classifier.

All selections, including the fallback classifier, use fixed deterministic rules based only on the learner's permitted information. After a mistake with revealed pair \((v,y)\), replace \(V\) by \(V_{v,y}\). After a correct round, leave \(V\) unchanged.

## Task

Prove that
\[
M^*(H,G)=\operatorname{IDim}(H),
\]
and that the dimension-based learner attains this value. The equality is in the extended nonnegative integers: in the infinite-dimensional case every deterministic learner has an unbounded worst-case mistake bound, and the stated arbitrary fallback has this optimal unbounded value.
