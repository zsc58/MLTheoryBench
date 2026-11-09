# Problem

## Setup

Let m and k be positive integers with k >= m+1, and let the label set be [k] = {1,...,k}. Let X be a topological input space equipped with a sigma-algebra F containing its open sets and a probability measure p_x. Define its support by

S = {x in X : p_x(U) > 0 for every open neighborhood U of x},

and assume S is measurable and p_x(S)=1.

Consider two softmax models with representation dimension m:

- measurable functions f, f': X -> R^m;
- centered unembeddings g, g': [k] -> R^m, meaning sum_y g(y) = sum_y g'(y) = 0;
- logits u_y(x) = f(x)^T g(y) and u'_y(x) = f'(x)^T g'(y);
- probabilities p(y|x) = exp(u_y(x)) / sum_{z=1}^k exp(u_z(x)) and p'(y|x) = exp(u'_y(x)) / sum_{z=1}^k exp(u'_z(x)).

Thus u(x) and u'(x) are centered k-dimensional logit vectors. Assume both models are in general position: span{f(x): x in S} = span{f'(x): x in S} = R^m, and every shifted-unembedding matrix below is invertible.

For a pivot i in [k] and J subset of [k]\{i} with |J|=m, define

L_{i,J} = [ g(j)-g(i) ]_{j in J},    L'_{i,J} = [ g'(j)-g'(i) ]_{j in J},

with the columns in increasing label order. Define A_{i,J} = L_{i,J}^{-T} L'_{i,J}^T, where L^{-T} denotes (L^{-1})^T. Define

d_logit^2 = E_{x~p_x} ||u(x)-u'(x)||_2^2,

and

d_rep^2 = average_{i in [k], J subset [k]\{i}, |J|=m} E_{x~p_x} ||f(x)-A_{i,J}f'(x)||_2^2,

where the average is uniform over all pivots and all such subsets. These expectations are nonnegative extended-real integrals, and d_logit and d_rep are their respective nonnegative square roots, possibly +infinity.

Finally, let sigma_min be the minimum over (i,J) of the smallest singular value of L_{i,J}, and sigma_max the maximum over (i,J) of the largest singular value of L_{i,J}.

## Task

Prove the integrated theorem: with C = sqrt(2m/(k-1)),

(C/sigma_max) d_logit <= d_rep <= (C/sigma_min) d_logit,

with inequalities interpreted in [0,+infinity].
