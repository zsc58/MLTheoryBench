# Reference Proof

## Proof Structure

Represent every joint model classification by a case, with one assigned class for each model. Independence factors the probability of each case into per-model probabilities. The event of consistent correct classification is the disjoint union of the cases satisfying the actual score and margin inequalities for the ideal correct class. In each such product, replace factors corresponding to models assigned their own true class by the stated per-model lower bound, then sum over the qualifying cases.

## Complete Proof

Fix the subregion and suppress its symbol in the notation. For an assignment t=(z_1,...,z_N) in {1,...,K}^N, let N_k^t={n:z_n=k} and let E_t be the event that Y_n=z_n for every n. The events E_t are pairwise disjoint and exhaustive. By independence,

Pr(E_t) = product over k=1,...,K of product over n in N_k^t of p_n^k.

Let B_k={n:k_n^T=k}. For the ideal classifier, the ideal assignment is z_n=k_n^T and the ideal score for class k is |B_k|. By assumption, the ideal assignment satisfies the consistency inequalities for the unique class k*.

For the actual probabilities, let A(k) be the set of assignments satisfying C_k^t >= v and C_k^t-C_j^t >= r for every j != k. Since r>0, no assignment can satisfy the margin inequalities for two different classes: if classes k and j both satisfied them, then both C_k^t-C_j^t >= r and C_j^t-C_k^t >= r would hold, which is impossible. Therefore the event of consistent correct classification as k* is exactly the disjoint union of E_t over t in A(k*).

The stated per-model guarantee gives p_n^{k_n^T} >= q, where q=(1-alpha)^4. If n is in N_k^t intersect B_k, then k_n^T=k and the corresponding factor p_n^k is at least q. All other factors are left unchanged. Hence, for every t,

Pr(E_t) >= product over k=1,...,K of [ q raised to |N_k^t intersect B_k| times product over n in N_k^t\B_k of p_n^k ].

Summing these inequalities over the disjoint assignments in A(k*) gives

Pr(consistent correct classification as k*) >= sum over t in A(k*) of product over k=1,...,K of [ q raised to |N_k^t intersect B_k| times product over n in N_k^t\B_k of p_n^k ].

Substituting q=(1-alpha)^4 proves the stated inequality. Empty products equal 1.

## GT Quality Note

The derivation above is complete conditional on the explicit per-model guarantee in the public task. The guarantee itself is a specialized nonstandard external dependency identified in theory_008. It is not independently derived or audited here, so the private ground truth retains the unresolved obligation to verify that guarantee under its complete external hypotheses. This limitation does not make the public conditional task undefined or invalid.
