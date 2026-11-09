# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Support-count exchangeability and reduction (3 points).** Proves, outside the non-degeneracy null set, that a deterministic selection of positions is exactly the full support list if and only if the selected input is fully supporting and all remaining observations confirm its decision. Both directions must be justified using batch consistency and non-degeneracy. Uses within-dataset exchangeability to obtain the product binomial coefficient, then integrates observations outside fixed positions to obtain the factors \(\prod_i(1-v_i)^{n_i-k_i}\). Do not accept an unsupported assertion that nonsupport observations are independent after conditioning on the selected support set.
2. **Measure construction and normalization (2 points).** Defines the finite subprobability measure \(\mu_k(C)=\mathbb P^{|k|}\{\operatorname{supp}(X_k)=X_k,\ V(M(X_k))\in C\}\), or an equivalent generalized distribution function, and derives
   \[
   \sum_{k\le h}\binom hk\int_{[0,1]^m}(1-v)^{h-k}\,d\mu_k(v)=1
   \]
   for the sizes needed through \(H\). Uses the same measures across sizes and accounts for zero coordinates. These are consequences of the support decomposition, not standard distribution-function identities that may simply be cited.
3. **Full weak-duality lower bound (3 points).** Derives the finite moment relaxation with measures indexed by all \(k\le H\), or gives its equivalent direct weighted-integral proof. The full pointwise requirement is \(\sum_{h\ge k}\lambda_h\binom hk(1-v)^{h-k}\le c_k(v)\), where \(c_k\) is the target integrand for \(k\le N\) and zero otherwise. Shows that integration and normalization give a lower bound \(\sum_h\lambda_h\). The multipliers of the equality constraints are initially unrestricted; the supplied sign conditions are sufficient restrictions used to verify feasibility. Strong duality and existence of optimizers are unnecessary.
4. **Collective superlevel certificate and boundaries (2 points).** On \((1-v)^{N-k}>0\), proves directly that the normalized expression is at most \(\lambda_N\le1\) and is negative outside its nonnegative-superlevel set. Verifies the unnormalized inequalities also on the zero-factor faces and for \(k\not\le N\), using the multiplier signs. Concludes the probability bound from \(\sum_h\lambda_h=1-\beta\), without assuming a Cartesian-product region. Handles \(0^0=1\), zero support counts, and \(k=N\) consistently.

# Evaluator Notes

Accept a complete valid alternative proof. In particular, directly integrating a verified pointwise certificate against the explicitly constructed support measures earns full credit for the moment-to-dual step; writing an optimization problem is not mandatory. Do not require the reference proof's incidental presentation choices.

Treat omission of the support decomposition or of the normalization-to-certificate argument as theorem-critical. Merely naming exchangeability, a moment problem, generalized distribution functions, or duality without deriving its role earns no credit for that step. Do not require nonexistent additional deletion-consistency identities.

The public region excludes points with \((1-v)^{N-k}=0\). A proof may instead use a different measurable convention on those faces if it proves that, at the observed support count, they have probability zero. It must not silently divide by a zero factor, discard all coordinates with risk one, or assume that the risk law has no boundary mass.

An isolated missing routine boundary check may warrant 8-9 if the complete argument already supplies its immediate repair. An unsupported moment representation, omission of necessary sizes through \(H\), or failure to establish a full certificate is not merely a presentation issue. A failure in an upstream construction propagates only when the final certificate is consequently unsupported.
