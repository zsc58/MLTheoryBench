# Problem

## Setup

Let \(f:\{0,1\}^n\to\mathbb{R}\) be a pseudo-Boolean objective with a simple undirected variable-interaction graph \(G\) on vertex set \([n]\): an edge joins two variables exactly when they are dependent in the objective. Let \(x^{(1)},x^{(2)}\in\{0,1\}^n\) be two parent solutions and define
\[
I=\{g\in[n]:x^{(1)}_g\ne x^{(2)}_g\}.
\]
Call the connected components of the induced graph \(H=G[I]\) the component masks.

Let \(D^*:[n]\times[n]\to[0,1]\) be a symmetric dependency matrix that is perfect for \(G\): there is a real threshold \(\theta\) such that \(D^*(g,h)>\theta\) for every edge of \(G\), and \(D^*(g,h)<\theta\) for every non-edge with distinct endpoints. Only entries with distinct variables are used.

The linkage-tree construction starts with one singleton node \(\{g\}\) for each \(g\in I\). For two distinct current clusters \(A,B\subseteq I\), its linkage strength is
\[
L(A,B)=\max_{g\in A,\,h\in B}D^*(g,h).
\]
While at least two current clusters remain, choose any pair with maximum linkage strength and replace those two clusters by their union. Assign the merged cluster its linkage strengths to the remaining clusters using the same formula. The linkage tree consists of all singleton and merged clusters produced. If \(I=\varnothing\), this collection is empty.

## Task

Prove that, for every such \(G\), perfect \(D^*\), and parent pair \(x^{(1)},x^{(2)}\), the linkage tree contains every component mask as one of its nodes, regardless of the choices among maximizing pairs.
