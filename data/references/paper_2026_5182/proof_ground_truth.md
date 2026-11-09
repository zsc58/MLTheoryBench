# Reference Proof

## Proof Structure

Compare the surrogate with a minimum-cardinality exact solution, use the residual-separation condition to eliminate all lower-cardinality binary vectors, and then force equality for any surrogate minimizer.

## Complete Proof

The set \(\mathcal B\) is finite and nonempty, and \(\mathcal E\) is a nonempty subset of it. Consequently, the minimum defining \(K\) is attained, \(K\in\{0,\ldots,n\}\), and \(Q_\tau\) attains a minimum on \(\mathcal B\). For every integer \(k\) with \(0\le k<K\), the binary vectors of cardinality \(k\) form a nonempty finite set, so \(r_k\) is also well-defined and attained.

Let \(z^\star\in\mathcal E\) satisfy \(\|z^\star\|_0=K\). Since \(Az^\star+b=0\),
\[
Q_\tau(z^\star)=\tau^2K.
\]
Hence the minimum value of \(Q_\tau\) on \(\mathcal B\) is at most \(\tau^2K\).

Fix any \(z\in\mathcal B\). If \(\|z\|_0=k<K\), then by the definition of \(r_k\),
\[
Q_\tau(z)=\|Az+b\|_2^2+\tau^2k
\ge r_k^2+\tau^2k
>\tau^2(K-k)+\tau^2k
=\tau^2K.
\]
Thus no binary vector with fewer than \(K\) nonzero entries can minimize \(Q_\tau\). When \(K=0\), there are no such vectors or residual indices, and every binary vector already has cardinality at least \(K\).

Now let \(\widehat z\) be any minimizer of \(Q_\tau\) over \(\mathcal B\). The preceding paragraph gives \(\|\widehat z\|_0\ge K\), while comparison with \(z^\star\) gives
\[
Q_\tau(\widehat z)\le \tau^2K.
\]
On the other hand,
\[
Q_\tau(\widehat z)
=\|A\widehat z+b\|_2^2+\tau^2\|\widehat z\|_0
\ge \tau^2\|\widehat z\|_0
\ge \tau^2K.
\]
All these inequalities are therefore equalities. Since \(\tau>0\), equality gives \(\|\widehat z\|_0=K\), and equality in the residual inequality gives \(\|A\widehat z+b\|_2^2=0\). Hence \(\widehat z\in\mathcal E\) and has the minimum possible number of flips, as required. This argument includes \(K=0\).
