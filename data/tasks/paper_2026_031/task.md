# Problem

## Setup

Let n, T, and m be positive integers, with m fixed with respect to n and T. Consider n sequences of a finite-state hidden Markov model with common length T and latent state space {1,...,m}. Conditional on their shared Bayesian parameter vector theta, the sequences are independent. For sequence s, write z_s,1:T for its latent states and y_s,1:T for its observations. Conditional on theta, the latent chain has initial distribution pi and row-stochastic transition matrix A, and the observations are conditionally independent given the latent states, with emission probabilities or densities b_j(·) in state j. Writing y and z for all sequences, the Bayesian joint factorization is

p(theta,y,z) = p(theta) p(z | theta) p(y | z,theta).

Missingness is ignorable: the observation pattern may be omitted from the likelihood used for inference on theta and the latent states. Let O_s be the observed time indices and M_s={1,...,T}\O_s the missing indices. Assume

O_s = {1 = t_s,1 < ... < t_s,K_s <= T}.

Define the aggregate missing rate

p = (sum_s |M_s|)/(nT), so that sum_s K_s = n(1-p)T.

Consider a latent-state update at a fixed current value of theta. Emission evaluations at the supplied observed values are finite, and the observed-data likelihood p(y_s,O_s | theta) is finite and strictly positive for each sequence; thus the latent-state conditional distributions being sampled are defined. Here y_s,O_s denotes the observations of sequence s at the indices in O_s.

The collapsed sampler integrates the missing observations and analytically sums the latent states at indices in M_s before performing a forward-backward latent-state update on the retained observed indices O_s. The update is supplied with the retained observation values and their already ordered time indices. Its cost does not include locating these entries in a full-length data representation, updating theta, or subsequently reconstructing missing observations or missing-position latent states.

In the computational model, arithmetic, emission evaluation, access to a supplied index or observation, a categorical draw on the fixed state space, and access to a previously cached powered transition each cost O(1). For the current A, the matrices A^1,...,A^T may be precomputed and stored within O(T^2) work. Because A changes during Gibbs updates, preprocessing for the corresponding current A is included in the update cost. The complexity constants may depend on fixed m and the stipulated computational primitives, but not on n, T, p, or the locations of the missing entries.

## Task

Prove that the collapsed sampler's latent-state forward-backward update over the n sequences, including the stated transition-power preprocessing, has total cost O(n(1-p)T + T^2), and hence cost O(n(1-p)T) whenever n(1-p)/T tends to infinity.

Show that a conventional forward-backward update over every latent position has cost O(nT) under the same fixed-state computational model, so the collapsed update scales with the observed fraction rather than the full sequence length, apart from the stated transition-power preprocessing cost.
