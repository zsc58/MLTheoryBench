# Reference Proof

## Proof Structure

Use the two human-partition cells to produce the same observable pair with distinct conditional label laws. Then use injectivity of the Bayes combiner to transfer those differing laws to a positive-probability value of its output.

The theorem-critical obligations are:

1. Establish that the common observation occurs with positive probability in both grouping cells.
2. Derive the two different conditional label laws and show that the grouping changes the label law beyond the common observation.
3. Justify the transfer through injectivity with the stated measurable structure and conclude failure of generalized calibration.

## Complete Proof

Let \(W=(A,M)\), let \(w_0=(a',v)\), and write \(Q=g^*(W)\).

### 1. Positive probability of the shared observation

For each \(i=1,2\), the assumption \(\Pr(M=v,G=S_i)>0\) implies \(\Pr(G=S_i)>0\). Conditional independence of \(A\) and \((Y,M)\) given \(G\) therefore gives
\[
p_i:=\Pr(W=w_0,G=S_i)
=\Pr(A=a'\mid G=S_i)\Pr(M=v,G=S_i)>0.
\]
In particular, \(\Pr(W=w_0)>0\). Every point-conditioned probability used below has a positive-probability conditioning event.

### 2. Different conditional label laws

For every label \(a\in\mathcal Y\), conditional independence also gives
\[
\Pr(Y=a,W=w_0,G=S_i)
=\Pr(A=a'\mid G=S_i)\Pr(Y=a,M=v,G=S_i).
\]
Dividing by the positive expression for \(p_i\) yields
\[
\Pr(Y=a\mid W=w_0,G=S_i)
=\Pr(Y=a\mid M=v,G=S_i).
\]
Define
\[
b_i=\Pr(Y=a''\mid M=v,G=S_i),
\qquad
c=\Pr(Y=a''\mid W=w_0).
\]
The hypothesis says \(b_1\ne b_2\). If \(\Pr(Y\mid W,G)=\Pr(Y\mid W)\) almost surely, then on each positive-probability event \(\{W=w_0,G=S_i\}\), its \(a''\)-coordinate would give \(b_i=c\). This would imply \(b_1=b_2\), a contradiction. Thus the two conditional label distributions are not equal almost surely.

### 3. Transfer to the combiner output

Let \(T\) be the support of the law of \(W\) in \(\mathcal Y\times\Delta^{K-1}\). This space has a countable base: use singletons in the finite label set and intersections of the simplex with Euclidean balls having rational centers and positive rational radii. By the definition of support, every point outside \(T\) belongs to some open neighborhood with probability zero, and hence to a zero-probability member of this countable base. Consequently, \(T^c\) is the union of zero-probability members of a countable base, so
\[
\Pr(W\in T)=1.
\]
Also, \(w_0\in T\), since every neighborhood of \(w_0\) has probability at least \(\Pr(W=w_0)>0\).

Set \(q_0=g^*(w_0)\). Injectivity of \(g^*\) on \(T\) implies that, whenever \(W\in T\),
\[
Q=q_0\quad\Longleftrightarrow\quad W=w_0.
\]
Thus the measurable events \(\{Q=q_0\}\) and \(\{W=w_0\}\) agree up to a null set. Their intersections with each \(\{G=S_i\}\) also agree up to a null set. It follows that
\[
\Pr(Q=q_0,G=S_i)=p_i>0,
\]
\[
\Pr(Y=a''\mid Q=q_0,G=S_i)=b_i,
\qquad
\Pr(Y=a''\mid Q=q_0)=c.
\]
Because \(g^*(W)=\Pr(Y\mid W)\) almost surely and \(\Pr(W=w_0)>0\), the \(a''\)-coordinate of \(q_0\) equals \(c\).

Since \(b_1\ne b_2\), at least one of them differs from \(c\). On the corresponding positive-probability event \(\{Q=q_0,G=S_i\}\),
\[
\Pr(Y=a''\mid Q,G)=b_i\ne c=\Pr(Y=a''\mid Q)=Q_{a''}.
\]
Hence the required equalities for generalized calibration fail on a set of positive probability. Therefore \(g^*(A,M)\) is not generalized calibrated with respect to \(G\). \(\square\)

## Closure and Boundary Checks

All three critical obligations are derived explicitly. The proof requires no global measurable-inverse theorem or nonstandard external dependency. It does not assume that \(M\) is discrete, that \(G\) has finitely many values, or that every coordinate of a predictive distribution is positive. Only the witness events must have positive probability. Boundary points of the simplex are allowed. When \(K=1\), the unequal-label-probability hypothesis cannot hold, so the implication is vacuous. No distinction between \(a'\) and \(a''\) is required. The model- and human-calibration assumptions remain part of the source setup even though the conditional-independence and witness conditions suffice for the argument.
