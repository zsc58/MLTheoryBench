# Reference Proof

## Proof Structure

1. Use input separability to isolate one processed tensor contribution per input channel.
2. Freeze those channelwise functions and rewrite the scalar-reweighted pre-activation as a tensor dot product with scalar coefficients.
3. Match the expression to the tensor-affine node definition, account for possible node-specific inputs, and derive the inheritance and scalar-per-channel training consequence.

## Complete Proof

Fix a node j. Input separability gives

q'_j(Z, theta_j) = sum_{k=1}^d q'_{jk}(Z_k, theta_{jk}) + b_j Gamma_{D_out},

where the kth summand depends only on Z_k and its parameter block. The scalar-reweighted node is

q_tilde_j(Z, theta_j, gamma_j) = sum_{k=1}^d gamma_{jk} q'_{jk}(Z_k, theta_{jk}) + b_j Gamma_{D_out},

with output f_tilde_j = sigma(q_tilde_j). Freeze every theta_{jk} and set

Z_tilde_{jk} = q'_{jk}(Z_k, theta_{jk}) in R^{D_out}.

Then

f_tilde_j = sigma(sum_{k=1}^d Z_tilde_{jk} gamma_{jk} + b_j Gamma_{D_out})
           = sigma(Z_tilde_j odot_t gamma_j + b_j Gamma_{D_out}),

by the definition of odot_t. This is exactly the tensor-affine node form, with channel inputs Z_tilde_{jk}, scalar weights gamma_{jk}, and bias b_j. Because the frozen functions may depend on j, these processed channel inputs need not be shared across nodes, so the representation can be inhomogeneous.

Therefore any property or training result for tensor-affine nodes whose hypotheses allow inhomogeneous inputs applies after this identification. In particular, freezing the channelwise functions leaves precisely one trainable scalar gamma_{jk} for each input-channel contribution. This proves both clauses of the integrated claim.
