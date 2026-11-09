# Reference Proof

## Proof Structure

1. Establish the Gamma-liminf inequality using convex-combination domination by the nearest squared distance and continuity of the finite minimum.
2. Establish the recovery (limsup) inequality by proving concentration of the softmax weights on the nearest-centroid set.
3. Apply the two inequalities to obtain Gamma-convergence.
4. Use compactness, continuity, and the minimizing-sequence inequalities to show that every accumulation point of soft minimizers minimizes the hard objective.

## Complete Proof

For each fixed sigma > 0, the functions r_ij(sigma; mu) and L_sigma(mu) are continuous on K, since the denominator in r_ij is strictly positive. Hence L_sigma attains a minimum on the compact set K. The function J is continuous because it is a finite sum of minima of finitely many continuous functions.

Let sigma_m tend to zero and mu_m tend to mu in K. For every i, the quantity sum_j r_ij(sigma_m; mu_m) ||x_i - (mu_m)_j||^2 is a convex combination of the numbers ||x_i - (mu_m)_j||^2. It is therefore at least min_j ||x_i - (mu_m)_j||^2. Summing over i and using continuity of each finite minimum gives

liminf_m L_{sigma_m}(mu_m) >= J(mu).

For the recovery inequality, fix mu in K and use the constant sequence mu_m = mu. For a fixed datum i, write a_j = ||x_i - mu_j||^2 and a_* = min_j a_j. The corresponding weighted average is

(sum_j exp(-(a_j-a_*)/(2 sigma_m^2)) a_j) / (sum_l exp(-(a_l-a_*)/(2 sigma_m^2))).

Indices with a_j > a_* have exponentially vanishing relative weight, while indices with a_j = a_* retain total limiting weight one. Since all indices attaining the minimum have value a_*, this weighted average converges to a_*. Summing over the finitely many data points yields L_{sigma_m}(mu_m) -> J(mu), and hence limsup_m L_{sigma_m}(mu_m) <= J(mu). Thus L_sigma Gamma-converges to J on K as sigma tends to zero.

Now let mu_m minimize L_{sigma_m} on K. By compactness, every subsequence has a further subsequence, still indexed by m, converging to some bar_mu in K. For any nu in K, the minimizing property gives L_{sigma_m}(mu_m) <= L_{sigma_m}(nu). The liminf inequality at mu_m and the recovery inequality for the constant sequence nu imply

J(bar_mu) <= liminf_m L_{sigma_m}(mu_m) <= limsup_m L_{sigma_m}(nu) = J(nu).

Since nu was arbitrary, bar_mu minimizes J on K. Therefore every accumulation point of soft minimizers is a minimizer of the hard K-Means distortion.
