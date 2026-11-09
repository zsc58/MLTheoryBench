# Problem

## Setup

Let $X_N=\{x_1,\ldots,x_N\}$ be a fixed finite corpus and let $g:X_N\to\{0,1\}$ be a fixed candidate generator. Its excluded pool is
\[
E=\{x_i:g(x_i)=0\},\qquad |E|=N_0\ge1.
\]
A labeling is a fixed vector $y=(y_1,\ldots,y_N)\in\{0,1\}^N$ of unknown noiseless relevance labels. Write $M_0(y)$ for the number of relevant items in $E$.

An audit may inspect corpus items from either $E$ or $X_N\setminus E$ one at a time, possibly repeating an inspection. Each inspection reveals that item's true label. The audit rule and the law of its internal random seed are fixed independently of the labeling. With the corpus and generator available, the next inspected index, stopping decision, and integer report $\widehat M_0$ are given by pre-specified measurable functions of the seed and the observed index-label history; they may not depend on unobserved labels. The audit terminates almost surely for every labeling. Let $T$ count the distinct items of $E$ inspected before termination; inspections outside $E$ do not contribute to $T$. Write $\Pr_y$ for probability over the audit's randomness under the fixed labeling $y$.

Fix an integer $1\le m\le N_0$ and parameters $0<\beta\le1/2$, $0<\delta<1/4$. Call an audit valid at level $\delta$ if, for every complete labeling $y$ with $M_0(y)\ge m$,
\[
\Pr_y(\widehat M_0\le m-1)\le\delta.
\]
Require also that, for every complete labeling $y$ with $M_0(y)=0$,
\[
\Pr_y(\widehat M_0\le m-1)\ge1-\beta.
\]

For any fixed complete zero-miss labeling $y^{(0)}$, write $\Pr_0$ and $\mathbb E_0$ for probability and expectation under that labeling. Let $C^*$ be the infimum of $\mathbb E_0[T]$ over all audits satisfying both requirements. The claims below are to hold for every choice of $y^{(0)}$, including every choice of its included-pool labels.

## Task

Prove the following integrated theorem: every valid audit with the stated zero-miss success satisfies
\[
\mathbb E_0[T]\ge (1-\beta-\delta)\frac{N_0}{m},
\]
and, with
\[
n_0=\left\lceil N_0\bigl(1-\delta^{1/m}\bigr)\right\rceil,
\]
there is a valid nonadaptive audit inspecting $n_0$ distinct excluded items and no included items whose report is at most $m-1$ whenever all inspected labels are zero. Consequently,
\[
(1-\beta-\delta)\frac{N_0}{m}\le C^*\le n_0
\le \bigl(1+\log(1/\delta)\bigr)\frac{N_0}{m},
\]
so $C^*=\Theta(N_0/m)$ with constants depending only on $\beta$ and $\delta$, not on the choice of complete zero-miss labeling.
