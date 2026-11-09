# Problem

## Setup

Fix an integer `C >= 1`. Let `h in R^C` be a vector of variable-indexed states, and let `M in R^{C x C}` define the linear inter-variable coupling `h -> M h`. For each permutation `pi` of `{1,...,C}`, let `P_pi` be its permutation matrix, acting by `(P_pi h)_c = h_{pi^{-1}(c)}`. The coupling is permutation-equivariant if

`M P_pi = P_pi M` for every permutation `pi`.

Let `I_C` denote the identity matrix and let `1 in R^C` denote the all-ones vector.

## Task

Prove that the coupling is permutation-equivariant if and only if there exist scalars `alpha,beta in R` such that

`M = alpha I_C + beta 11^T`.

Equivalently, for every state vector `h` and coordinate `c`,

`(M h)_c = alpha h_c + beta sum_{j=1}^C h_j`,

so every equivariant linear coupling consists exactly of a local self-coupling term and a global pooled interaction.
