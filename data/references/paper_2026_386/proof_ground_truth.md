# Reference Proof

## Proof Structure

1. Use an absolute-base Euclidean covering bound and the regular-growth inequalities to find leaves from distinct depth-$q$ subtrees whose representations are exponentially close.
2. Separate the two branches below their lowest common ancestor and verify that the resulting three-valued leaf function is intrinsically $2/(\rho D)$-Lipschitz.
3. Extend the leaf function to the whole tree without increasing its Lipschitz constant or leaving $[-1,1]$.
4. Convert accurate approximation at the two colliding leaves into an exponential lower bound on the Euclidean Lipschitz constant, handling coincident images without division by zero.
5. Verify the boundary cases and independence of the final constant from all parameters.

## Complete Proof

Set

$$
\alpha=\log b-4\varepsilon>0,
\qquad
\delta=6A\exp\left(-\frac{\alpha D}{2p}\right).
$$

### 1. A close pair from different depth-$q$ subtrees

The sets $S_D(w)$, for $w\in S_q$, partition $S_D$. Let

$$
M=\max_{w\in S_q}|S_D(w)|,
$$

and let $N_q$ denote the number of nonempty sets in this partition. The leaf lower bound ensures that $S_D$ is nonempty, so $M>0$. Consequently,

$$
N_q\ge \frac{|S_D|}{M}
\ge \exp\left(\frac{(\log b-3\varepsilon)D}{2}\right)>1.
$$

Thus at least two depth-$q$ subtrees contain leaves. In particular, the assumptions cannot hold when $D=1$: then $q=0$ and there is only one depth-zero subtree. Every admissible instance therefore has $q\ge1$; the original parameter range need not be changed.

If $\delta>2A$, choose leaves $x_+,x_-$ from any two distinct nonempty depth-$q$ subtrees. Since both images lie in $B_2(0,A)$,

$$
\|F(x_+)-F(x_-)\|_2\le 2A<\delta.
$$

Suppose instead that $\delta\le2A$. We claim that $B_2(0,A)$ can be covered by at most $(6A/\delta)^p$ sets of Euclidean diameter at most $\delta$.

Take a maximal collection of points in the ball whose pairwise distances are greater than $\delta/2$. The open radius-$\delta/4$ balls about these points are disjoint and lie in the radius-$(A+\delta/4)$ ball. Comparison of Euclidean volumes bounds the size of every such collection by

$$
\left(1+\frac{4A}{\delta}\right)^p.
$$

This also ensures that a greedy separated collection terminates after finitely many additions. By maximality, the closed radius-$\delta/2$ balls about its points cover $B_2(0,A)$ and each has diameter at most $\delta$. Since $\delta\le2A$,

$$
\left(1+\frac{4A}{\delta}\right)^p
\le \left(\frac{6A}{\delta}\right)^p.
$$

Assign each leaf to one covering set containing its image. These are assignments of leaves, not counts of distinct image points; no injectivity of $F$ is assumed. If some assigned set receives leaves from two distinct depth-$q$ subtrees, those leaves form the desired pair. Otherwise each assigned set receives at most $M$ leaves, and hence

$$
|S_D|
\le \left(\frac{6A}{\delta}\right)^p M
\le \exp\left(\frac{(\log b-4\varepsilon)D}{2}
                 +\frac{(\log b+\varepsilon)D}{2}\right)
=\exp\left((\log b-\tfrac32\varepsilon)D\right).
$$

This contradicts $|S_D|\ge\exp((\log b-\varepsilon)D)$ because $\varepsilon D>0$. Thus in all cases there are leaves $x_+,x_-$ from distinct depth-$q$ subtrees such that

$$
\|F(x_+)-F(x_-)\|_2\le
6A\exp\left(-\frac{(\log b-4\varepsilon)D}{2p}\right).
\tag{1}
$$

### 2. The intrinsically smooth branch cut

Let $a$ be the lowest common ancestor of $x_+,x_-$, and let $a_+,a_-$ be the distinct children of $a$ leading respectively to them. Because the leaves have distinct depth-$q$ ancestors,

$$
\operatorname{depth}(a)<q,
$$

and in particular $\operatorname{depth}(a)\le q$.

Define $f_D:S_D\to[-1,1]$ by

$$
f_D(x)=
\begin{cases}
1,&x\in S_D(a_+),\\
-1,&x\in S_D(a_-),\\
0,&\text{otherwise}.
\end{cases}
$$

If two leaves have different labels, at least one lies in a selected child-subtree and the other lies outside that same child-subtree. Their lowest common ancestor therefore has depth at most $\operatorname{depth}(a)\le q$. Their path contains at least

$$
2(D-q)\ge D
$$

edges. Since every edge has weight at least $\rho$, their intrinsic distance is at least $\rho D$. This applies in particular to $x_+,x_-$. Every label difference is at most $2$, so

$$
|f_D(x)-f_D(y)|\le \frac{2}{\rho D}d_{\mathcal T}(x,y)
$$

for all leaves $x,y$; the inequality is immediate when their labels agree.

### 3. Extension to all vertices

Let $L=2/(\rho D)$ and define

$$
\widetilde f(v)=\min_{x\in S_D}
\bigl(f_D(x)+L d_{\mathcal T}(v,x)\bigr).
$$

The minimum is finite because $S_D$ is finite and nonempty. For vertices $u,v$, the triangle inequality gives, for every leaf $x$,

$$
f_D(x)+L d_{\mathcal T}(u,x)
\le f_D(x)+L d_{\mathcal T}(v,x)+L d_{\mathcal T}(u,v).
$$

Taking minima and then interchanging $u,v$ yields

$$
|\widetilde f(u)-\widetilde f(v)|
\le L d_{\mathcal T}(u,v).
$$

For a leaf $v$, the leaf Lipschitz inequality gives

$$
f_D(v)\le f_D(x)+L d_{\mathcal T}(v,x)
\quad\text{for every }x\in S_D.
$$

Thus $\widetilde f(v)\ge f_D(v)$, while choosing $x=v$ gives the reverse inequality. Hence $\widetilde f=f_D$ on $S_D$.

Finally set

$$
f(v)=\max\{-1,\min\{1,\widetilde f(v)\}\}.
$$

The clipping map satisfies $|\operatorname{clip}(s)-\operatorname{clip}(t)|\le|s-t|$ for real $s,t$. It fixes every value in $[-1,1]$, including all the prescribed leaf values. Therefore $f:\mathcal V\to[-1,1]$ has the required leaf labels and intrinsic Lipschitz constant at most $L$.

### 4. The Euclidean lower bound

If $F(x_+)=F(x_-)=z$, then every function $\psi$ satisfies

$$
|\psi(z)-1|+|\psi(z)+1|\ge2.
$$

There is consequently no $\psi$ satisfying the required approximation condition, and the universally quantified implication in the conclusion holds vacuously for this pair.

Otherwise, let $\psi:\mathbb R^p\to[-1,1]$ satisfy that condition, and denote its two errors by $e_+$ and $e_-$. Since $f(x_+)=1$ and $f(x_-)=-1$, the triangle inequality gives

$$
|\psi(F(x_+))-\psi(F(x_-))|
\ge 2-e_+-e_-
\ge1.
$$

The represented points are now distinct, so the definition of the Euclidean Lipschitz constant and (1) imply

$$
\operatorname{Lip}_2(\psi)
\ge \frac{1}{\|F(x_+)-F(x_-)\|_2}
\ge \frac{1}{6A}
\exp\left(\frac{(\log b-4\varepsilon)D}{2p}\right).
$$

This also covers functions whose Lipschitz constant is infinite.

### 5. Constants and proof closure

The choices of the pair, branches, and function depend only on the given tree, parameters, and representation, not on $\psi$. The numerical constant $c=1/6$ is independent of all of them. The proof covers both possible ranges of $\delta$, the impossible $D=1$ boundary, arbitrary positive edge weights bounded below by $\rho$, and noninjective representations. The nonempty partition, absolute-base cover, multiplicity-sensitive counting, intrinsic separation, range-preserving extension, and conditional Euclidean lower bound have all been derived explicitly. No probabilistic typicality result or unproved specialized external result is used.
