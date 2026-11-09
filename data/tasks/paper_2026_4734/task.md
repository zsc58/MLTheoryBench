# Problem

## Setup

Let `X=(X_1,\ldots,X_L)` have a distribution `p_data` on a finite product alphabet, with integer `L\ge2`, and write `[L]=\{1,\ldots,L\}`. For `A\subseteq[L]`, write `X_A` for the subvector. Entropies and KL divergences use natural logarithms, with `0\log0=0` and KL allowed to equal `+\infty`. Define
`TC(p_{X_A\mid X_{A^c}})=\sum_{i\in A}H(X_i\mid X_{A^c})-H(X_A\mid X_{A^c})`,
where conditional entropies average over the data distribution of the conditioning context, and
`TC(p_data)=\sum_{i=1}^L H(X_i)-H(X)`.

Fix conditional probability mass functions `\hat p_i(\cdot\mid x_C)` for every `C\subseteq[L]\setminus\{i\}` and every context value `x_C`. The true conditional marginals are those of `p_data`; choose any probability-mass-function versions at contexts having zero data probability.

A reverse unmasking state consists of a masked set `I` and the generated values `y_{I^c}` on its complement. When a batch `B\subseteq I` is revealed, the learned sampler draws its coordinates independently according to `\hat p_i(\cdot\mid y_{I^c})`; the ideal sampler uses the true marginals `p(X_i\mid X_{I^c}=y_{I^c})`. After revealing `B`, recurse on `I\setminus B`. Both samplers start with `I=[L]` and no revealed values. Let `Y_{out}^S` be the learned output for a fixed complete schedule `S`, and let `Y_{out}` be the mixture obtained by first sampling `S` and then running the learned sampler. Schedule randomization is independent of the data sample and token-draw randomness.

For integers `1\le K\le |I|\le L`, define the recursive schedule `\pi_{tc}(K,I)` as follows. If `K=1`, reveal all indices in `I`. If `K\ge2`, let `L'=|I|`, sample `ell\in\{1,\ldots,L'-K+1\}` with probability `w^{tc}_ell(K,L')/\Psi_{tc}(K,L')`, choose `B` uniformly among the `ell`-subsets of `I`, reveal `B`, and recurse with `\pi_{tc}(K-1,I\setminus B)`. Each schedule choice uses only the preceding index sets and fresh schedule randomness, not token values.

The scalar quantities are defined for integers `1\le K\le L'\le L`. Set `f_{tc}(1,1)=0` and `f_{tc}(1,L')=1` for `L'\ge2`. For `2\le K\le L'`, set
`w^{tc}_1(K,L')=1`,
`w^{tc}_ell(K,L')=\prod_{i=1}^{ell-1}\frac{(L'-i)f_{tc}(K-1,L'-i)}{1+(L'-i-2)f_{tc}(K-1,L'-i-1)}`
for `2\le ell\le L'-K+1`,
`\Psi_{tc}(K,L')=\sum_{ell=1}^{L'-K+1}w^{tc}_ell(K,L')`, and
`f_{tc}(K,L')=1-\frac{1+(L'-2)f_{tc}(K-1,L'-1)}{\Psi_{tc}(K,L')}`.
Let `H_n=\sum_{j=1}^n1/j` for `n\ge1`.

For `\pi=\pi_{tc}(K,[L])`, write its complete schedule as `S=(B_1,\ldots,B_K)` and put `U_{k-1}=\bigcup_{j<k}B_j`. Define
`epsilon_pred(\pi)=\mathbb E_{S\sim\pi}\mathbb E_{X\sim p_data}\sum_{k=1}^K\sum_{i\in B_k}KL(p(X_i\mid X_{U_{k-1}})\,\|\,\hat p_i(\cdot\mid X_{U_{k-1}}))`.
Here each conditional KL is evaluated at the context value supplied by the data sample `X`, independently of `S`. This quantity is zero for an exact conditional-marginal predictor.

## Task

For every integer `2\le K\le L`, prove the integrated bound
`KL(p_data\|p_{Y_{out}})\le \mathbb E_{S\sim\pi_{tc}(K,[L])}KL(p_data\|p_{Y_{out}^S})`
`\le \frac{H_{L-K+1}-1}{K+H_{L-K+1}-2}\,TC(p_data)+epsilon_pred(\pi_{tc}(K,[L]))`.
