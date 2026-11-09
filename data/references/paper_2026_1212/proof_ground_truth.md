# Reference Proof

## Proof Structure

Count the order-respecting permutations whose predecessor set for a fixed feature is a specified admissible coalition.  The resulting bijection gives the coalition weight.  Then establish the recursion and the interleaving/product identities for the modular counts.

## Complete Proof

Let \(\mathcal L(A)\) denote the set of linear extensions of the order induced on \(A\), so \(L(A)=|\mathcal L(A)|\).  Fix \(i\in F\) and \(S\subseteq F\setminus\{i\}\).

In every linear extension, the set of elements preceding \(i\) is a down-set.  Moreover, adjoining \(i\) to that predecessor set is again a down-set.  Hence a non-admissible \(S\) cannot occur as \(\operatorname{Pre}_\pi(i)\).

Now suppose that \(S\) is admissible and put \(R=F\setminus(S\cup\{i\})\).  There is a bijection
\[
 \mathcal L(S)\times\mathcal L(R)
 \longrightarrow
 \{\pi\in\mathcal L(F):\operatorname{Pre}_\pi(i)=S\}
\]
given by concatenating an extension of \(S\), then \(i\), then an extension of \(R\).

This concatenation respects every order relation.  Indeed, a relation from \(R\) into \(S\) is impossible because \(S\) is a down-set; a relation from \(R\) into \(\{i\}\) is impossible because \(S\cup\{i\}\) is a down-set.  All remaining cross-block relations point in the displayed concatenation direction.  Conversely, an extension with predecessor set \(S\) restricts uniquely to extensions of \(S\) and \(R\).  Therefore
\[
 \bigl|\{\pi\in\mathcal L(F):\operatorname{Pre}_\pi(i)=S\}\bigr|
 =L(S)L(R).
\]
Since \(\pi\) is uniform on \(\mathcal L(F)\),
\[
 \Pr\{\operatorname{Pre}_\pi(i)=S\}
 =\frac{L(S)L(F\setminus(S\cup\{i\}))}{L(F)}
\]
for admissible \(S\), and it is zero otherwise.  Partitioning the expectation defining \(\phi_i\) by its predecessor set consequently yields
\[
 \phi_i=
 \sum_{\substack{S\subseteq F\setminus\{i\}:\\S,\,S\cup\{i\}\text{ are down-sets}}}
 \frac{L(S)L(F\setminus(S\cup\{i\}))}{L(F)}
 \bigl[v(S\cup\{i\})-v(S)\bigr].
\]
This is the asserted exact asymmetric coalition-weight formula.

It remains to verify the count rules.  For nonempty \(A\), the first element of a linear extension must be a minimal element of \(A\).  Removing that first element leaves an arbitrary linear extension of \(A\setminus\{a\}\), and this construction is reversible.  The classes indexed by the first element are disjoint, so
\[
 L(\varnothing)=1,\qquad
 L(A)=\sum_{a\in\operatorname{Min}(A)}L(A\setminus\{a\}).
\]
Thus the counts, and hence all the weights above, are recursively computable.

If \(A_1,\ldots,A_r\) have no order relations between distinct sets, first choose the \(|A_j|\) positions occupied by each set and then choose an internal extension in each set.  This gives
\[
 L\!\left(\bigsqcup_{j=1}^r A_j\right)
 =\binom{\sum_j|A_j|}{|A_1|,\ldots,|A_r|}\prod_{j=1}^rL(A_j).
\]
If instead every element of \(A_j\) precedes every element of \(A_k\) whenever \(j<k\), the blocks cannot interleave, whence
\[
 L(A_1\oplus\cdots\oplus A_r)=\prod_{j=1}^rL(A_j).
\]
A relation-free block of size \(m\) has \(m!\) extensions, while a completely ordered block has one.  Applying the two displayed composition rules repeatedly gives the stated one-, two-, and three-module ordered and partially interleaved cases.  Substitution of these exact counts into the already proved ratio completes the proof.
