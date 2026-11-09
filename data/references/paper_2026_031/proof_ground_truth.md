# Reference Proof

## Proof Structure

Condition on the current parameter value. Integrating missing emissions and summing missing-position states gives a retained-state chain on the observed indices. Derive its forward filter and backward sampling conditionals, verify their normalization on sampled support, and count work over the retained positions. Add construction of the transition-power cache for the current transition matrix. Compare with a conventional pass over every latent position.

## Complete Proof

### 1. Marginalization

Fix one sequence and write its observed indices as 1 = t_1 < ... < t_K <= T. All probabilities and densities below condition on the current theta. The HMM has conditionally independent emissions. Integrating each missing observation therefore replaces its emission factor by one. Ignorable missingness permits using this observed-data likelihood without an additional missingness factor.

For a gap d = t_{k+1}-t_k and endpoint states i,j, summing the intervening latent states gives

sum over x_1,...,x_{d-1} of A_{i,x_1} A_{x_1,x_2} ... A_{x_{d-1},j} = (A^d)_{ij}.

For d=1 this is simply A_{ij}. The identity follows directly by repeated matrix multiplication. After the last retained time t_K, summing all remaining latent states gives one: successively sum the last transition's destination state and use that every row of A sums to one. Thus trailing missing positions introduce no additional factor. There are no leading missing positions because t_1=1.

Consequently,

p(z_o | theta) = pi_{z_{t_1}} product_{k=1}^{K-1} (A^(t_{k+1}-t_k))_{z_{t_k},z_{t_{k+1}}},

and

p(theta,y_o,z_o) = p(theta) p(z_o | theta) product_{k=1}^K b_{z_{t_k}}(y_{t_k}).

The retained latent states therefore form an inhomogeneous Markov chain. Conditional independence of the sequences given theta allows their latent-state updates to be performed separately at this fixed parameter value.

### 2. Forward filtering

Let alpha_{t_k}(j) be the joint mass or density of the retained observations through t_k and the event z_{t_k}=j, conditional on theta. For continuous observations this is a density in the observation coordinates, not the probability of observing an exact point.

At the first retained position,

alpha_{t_1}(j) = pi_j b_j(y_{t_1}).

Conditioning on the preceding retained state gives, for k>1,

alpha_{t_k}(j) = b_j(y_{t_k}) sum_{i=1}^m alpha_{t_{k-1}}(i) (A^(t_k-t_{k-1}))_{ij}.

The final normalizer is

L = sum_{j=1}^m alpha_{t_K}(j) = p(y_o | theta).

By the stipulated domain of the update, 0<L<infinity. Hence the last retained state can be sampled with probabilities alpha_{t_K}(j)/L.

### 3. Backward sampling and normalization

Suppose z_{t_{k+1}}=j and the later retained states have already been sampled. In the joint retained-chain factorization, the factors involving observations and states strictly after t_k depend on the earlier state z_{t_k}=i only through the fixed next state j. They therefore cancel when the conditional distribution over i is normalized. It follows that

P(z_{t_k}=i | z_{t_{k+1}},...,z_{t_K},y_o,theta)
= alpha_{t_k}(i) (A^(t_{k+1}-t_k))_{ij} / D_k(j),

where

D_k(j) = sum_{r=1}^m alpha_{t_k}(r) (A^(t_{k+1}-t_k))_{rj}.

The same expression gives the conditional given only z_{t_{k+1}}=j and y_o. This follows by summing over later states, whose likelihood factor again does not depend on i.

The denominator is positive for every j that can actually be sampled. At the terminal step, a sampled state has positive alpha_{t_K}. Inductively, the forward recursion implies that positive alpha_{t_{k+1}}(j) requires D_k(j)>0. A draw with positive backward weight has alpha_{t_k}(i)>0, maintaining this property at the next backward step. Zero-probability states need not be assigned a conditional by division by zero. All relevant quantities are finite under the finite emission evaluations and finite positive likelihood stipulated in the setup.

The backward chain rule now proves that these draws have exactly the collapsed conditional distribution of z_o given y_o and theta. Neither pass visits missing-position states.

### 4. Complexity

At a retained position, evaluating the m emissions and forming a forward vector takes O(m^2) arithmetic operations. A backward distribution, its normalization, and a categorical draw take O(m) operations. With fixed m, both are O(1). The already ordered observed-index input allows consecutive gaps to be obtained in O(1) work per retained position. Thus the two passes for sequence s cost O(K_s).

Since every K_s is at least one, per-sequence initialization and bookkeeping are absorbed by this bound. Summing gives

O(sum_s K_s) = O(n(1-p)T).

For the current A, the stipulated transition-power cache can be constructed within O(T^2) work. For example, computing each A^d separately with at most d-1 fixed-size matrix multiplications uses O(sum_{d=1}^T d)=O(T^2) work; storing all T matrices costs O(T). Cached lookup has the stipulated O(1) cost. Therefore the complete update, including this preprocessing, costs

O(n(1-p)T + T^2).

If n(1-p)/T tends to infinity, then T^2/[n(1-p)T] tends to zero, giving O(n(1-p)T). More generally, the same absorption is valid whenever T=O(n(1-p)). Constants in the operation count may depend on fixed m and the computational primitives, but not on the observation pattern, n, T, or p. A changed A requires a cache valid for that new A; it is not assumed reusable across distinct transition matrices.

### 5. Conventional comparison and boundary cases

A conventional forward-backward update performs a fixed-size forward calculation and backward calculation or draw at all T positions. Missing observations may be integrated by using emission factor one there, but these positions are still visited. Its total cost is therefore O(nT) under the same model. Parameter updates and subsequent reconstruction or imputation of missing positions are not included in either latent-update comparison.

The proof includes m=1, T=1, K_s=1, fully observed sequences, zero transition entries, and trailing missing blocks. When K_s=1, the transition product and backward loop are empty. Since the first observation is retained in every sequence, p<=1-1/T; an entirely unobserved sequence or p=1 is outside this stated contract.

## Sharper Preprocessing Is Also Valid

The O(T^2) preprocessing bound is not a lower bound or a requirement to use an inefficient implementation. Setting C_1=A and successively computing C_d=C_{d-1}A produces all powers in O(T) work for fixed m. This yields the stronger bound O(n(1-p)T+T), which implies the requested additive bound and its requested sufficient simplification regime. In particular, under this sharper construction, n much larger than T suffices to absorb preprocessing because sum_s K_s>=n. Such a proof is fully valid; it does not justify dropping T^2 from a calculation that uses only the looser preprocessing bound.
