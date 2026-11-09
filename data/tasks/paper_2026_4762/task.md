# Problem

## Setup

Let d be a positive integer and let D>=0 be a known finite bound. Let \(\mathcal P\) be a fixed measurable partition of \(\mathbb R^d\) into convex cells. The partition may be unknown. Each observed cell is supplied by a finite-bit description supporting polynomial-time cell membership and oracle operations; the learner is not given the unobserved Gaussian point or a description of the rest of the partition.

An unknown vector \(\mu^\star\in\mathbb R^d\) satisfies \(\|\mu^\star\|_2\le D\). Independent samples \(X_i\sim N(\mu^\star,I_d)\) are observed only through the unique cells \(C_i\in\mathcal P\) containing them. The cell observation map is measurable. Write \(Q_\mu\) for its pushforward distribution when the Gaussian mean is \(\mu\), and write \(\operatorname{TV}(P,Q)=\sup_A|P(A)-Q(A)|\), where the supremum is over measurable events in the observation space.

The partition is **\(\alpha\)-information-preserving** with respect to \(\mu^\star\) if, for every \(\mu\in\mathbb R^d\),
\[
\operatorname{TV}(Q_{\mu^\star},Q_\mu)\ge \alpha\,\operatorname{TV}\!\left(N(\mu^\star,I_d),N(\mu,I_d)\right),
\]
where \(0<\alpha\le1\). Assume this property holds.

For a supplied observed-cell description \(C\), a candidate mean \(\mu\), and a radius \(R>0\), assume access to an efficient sampler for \(N(\mu,I_d)\) conditioned on \(C\cap B_\infty(0,R)\), where \(B_\infty(0,R)=\{x:\|x\|_\infty\le R\}\). Whenever the conditioning set has positive Gaussian mass, the sampler returns a draw from that conditional law. For adaptive queries this distributional guarantee holds conditionally on the query and previous history, using fresh randomness. No distributional guarantee is imposed when the normalizing mass is zero. Every call terminates in polynomial time in its input bit complexity, as do the cell operations.

The notation \(\widetilde O\) suppresses polylogarithmic factors in the displayed parameters. Logarithmic factors in sample bounds are understood to be at least one, and sample counts are rounded up to integers.

## Task

Prove that for every \(\epsilon,\delta\in(0,1)\), there is a randomized algorithm which, from coarse observations and the parameters \((\epsilon,\delta,\alpha,D)\), outputs \(\widehat\mu\) satisfying
\[
\|\widehat\mu-\mu^\star\|_2\le\epsilon
\]
with probability at least \(1-\delta\), using
\[
 m=\widetilde O\!\left(\frac{dD^2\log(1/\delta)}{\alpha^4}+\frac{d\log(1/\delta)}{\alpha^4\epsilon^2}\right)
\]
samples, and running in time polynomial in \(m\) and the cell bit complexity.
