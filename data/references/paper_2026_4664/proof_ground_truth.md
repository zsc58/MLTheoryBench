# Reference Proof

## Proof Structure

Differentiate the pre-activation message with respect to a selected neighbor state distinct from the receiver state. The receiver state and all other state inputs are held fixed. Each score depends only on the receiver and its corresponding neighbor, so only the selected neighbor's score can vary. The product rule gives a direct derivative of that neighbor's message and derivatives of all attention coefficients. Softmax differentiation supplies the indirect competition term. Applying the elementwise activation derivative completes the block Jacobian formula.

## Complete Proof

Fix m, t, and n in N(m) with n != m. Abbreviate v_r = W_mr x_r, e_r = e_mr(t), alpha_r = alpha_mr(t), and

s = s_m(t) = sum_{r in N(m)} alpha_r v_r.

Let g_n = partial e_mn(t) / partial x_n, regarded as a row vector in R^{1 x d_c}. Since n != m, differentiation with respect to x_n holds the receiver state x_m fixed. For r != n, neither state input on which e_mr can depend varies. Therefore

partial e_r / partial x_n = delta_rn g_n.

This also covers a self-loop r=m: its score depends on x_m, which is fixed in the present off-diagonal derivative. There is one state vector x_m, not independent copies for its receiver and neighbor occurrences.

For the softmax calculation, set

Z = sum_{k in N(m)} exp(e_k).

Because n belongs to N(m), this neighborhood is nonempty. It is finite and all scores are real, so 0 < Z < infinity. Treating the logits as independent coordinates, the quotient rule gives

partial alpha_r / partial e_n
= [delta_rn exp(e_r) Z - exp(e_r) exp(e_n)] / Z^2
= alpha_r (delta_rn - alpha_n).

Applying the chain rule over all logits and using the preceding state derivatives yields

partial alpha_r / partial x_n
= sum_{k in N(m)} [partial alpha_r / partial e_k] [partial e_k / partial x_n]
= alpha_r (delta_rn - alpha_n) g_n.

Next differentiate s by the product rule. Each W_mr is fixed. The derivative of v_r with respect to x_n is W_mn when r=n and is zero otherwise. Thus

partial s / partial x_n
= alpha_n W_mn + sum_{r in N(m)} v_r [alpha_r (delta_rn - alpha_n) g_n].

Here v_r is a d_s-dimensional column vector and the expression in brackets is a 1 x d_c row vector. Their outer product is a d_s x d_c matrix, matching the dimensions of the direct term. Substituting v_r = W_mr x_r gives

partial s_m(t) / partial x_n
= alpha_mn(t) W_mn
  + sum_{r in N(m)} W_mr x_r alpha_mr(t) (delta_rn - alpha_mn(t)) partial e_mn(t) / partial x_n.

Finally, (tilde h_t^m)_s = sigma(s_m(t)) componentwise. Its activation derivative is the d_s x d_s matrix diag(sigma'(s_m(t))). The multivariate chain rule therefore gives

J_mn(t)
= diag(sigma'(s_m(t))) [partial s_m(t) / partial x_n].

Combining the last two displays proves exactly the claimed identity. The first summand comes from differentiating the selected message and is the direct attention-weighted influence. The summation comes from differentiating the attention weights and is the indirect softmax-competition influence. Both are multiplied by the activation derivative.

## Scope and Boundary Checks

The argument establishes only the asserted cross-client blocks n != m. It does not assume that the graph lacks self-loops. If N(m) contains a single distinct neighbor n and no other neighbor, alpha_mn=1 and the competition term vanishes, as the formula requires. If N(m) is empty or contains only m, there is no n in the asserted domain and the target is vacuous; the empty message sum has its usual value zero. Zero message matrices, score derivatives, or activation derivatives cause no difficulty. No inverse activation, rank condition, nonzero derivative, stochastic assumption, or stability result is used.
