# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Correctly marginalizes missing observations and missing latent states, obtaining the retained observed-index Markov chain with transition entry (A^d)_{ij} across a gap d. The argument must be valid for trailing missing positions and a single retained observation; a concise appeal to stochastic row sums and empty products suffices.
- **3 points:** Justifies forward filtering and backward sampling on the retained chain, including normalization and why the resulting draws have the collapsed conditional posterior. Explicit formulas or an equivalent complete factorization argument are acceptable. Conditional probabilities need only be defined on sampled support; strict positivity of every transition or emission is not required. For continuous observations, interpret observation likelihoods as densities.
- **3 points:** Counts retained-position work as O(sum_s K_s)=O(n(1-p)T) for fixed state cardinality, accounts for construction of a cache valid for the current A within O(T^2), and obtains the requested additive bound and its stated sufficient domination regime. A justified sharper preprocessing bound earns full credit when it implies the requested conclusions.
- **1 point:** Correctly contrasts the result with O(nT) for conventional full-length forward-backward updates under the same computational model.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. Require an explanation of why marginalization permits the observed-position filtering and sampling calculation, not merely the name of an algorithm. Do not require the reference proof's exact formulas or presentation when an equivalent argument closes these obligations.

The computational input already consists of the retained observations and ordered indices. Do not charge each latent update for a fresh scan of a full missingness mask, sorting, parameter estimation, or reconstruction of missing-position states. Conversely, do not assume that powers of A remain valid after A changes.

Treat unjustified omission of preprocessing as an important complexity error. When only the O(T^2) preprocessing bound is used, n much larger than T alone does not justify absorbing that displayed term uniformly in p; the comparison must involve n(1-p).

However, O(T^2) is only an upper bound. Computing powers successively by C_1=A and C_d=C_{d-1}A takes O(T) work for fixed m. A solver establishing this obtains O(n(1-p)T+T), which implies the requested result. Under this sharper construction, n much larger than T also suffices for absorption because K_s>=1 and hence sum_s K_s>=n. Do not penalize this valid reasoning or insist that a sharper proof retain an unnecessary T^2 term.

Read all runtime conclusions as upper bounds for the specified latent update, not as lower bounds, exact speedup ratios, or bounds for a complete Gibbs iteration including arbitrary parameter-update procedures.
