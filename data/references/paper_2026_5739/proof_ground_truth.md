# Reference Proof

## Proof Structure

Write the shrinkage parameter as `epsilon = 1 - lambda` and the displacement from the barycenter as `delta = p - u`. Expand each logarithm in the CLR definition around the barycenter coordinate `a = 1/K`, average these expansions, and use `sum_i delta_i = 0` to cancel the averaged linear term. Subtracting the average from each coordinate leaves the stated linear term and a quadratic-order remainder.

## Complete Proof

Fix `p` in the interior simplex and set

`a = 1/K`, `epsilon = 1 - lambda`, and `delta_i = p_i - a`.

Then `sum_i delta_i = 0` and

`S_lambda(p) = u + epsilon (p-u)`,

so its `i`-th coordinate is `a + epsilon delta_i`. Since `p` is fixed and has strictly positive coordinates, these coordinates are positive for all sufficiently small nonnegative `epsilon` (indeed, they are convex combinations of `p_i` and `a`).

For each coordinate, apply Taylor's theorem to `f(x) = log x` at `a`. For sufficiently small `epsilon`, the points `a + epsilon delta_i` lie in a compact positive interval around `a`, so the third derivative is bounded there. Consequently,

`log(a + epsilon delta_i) = log a + K epsilon delta_i - (K^2/2) epsilon^2 delta_i^2 + R_i(epsilon)`,

where `|R_i(epsilon)| <= C epsilon^3` for a constant `C` depending only on the fixed `p` and `K` (enlarging `C` to cover the finitely many coordinates).

Let

`m(epsilon) = (1/K) sum_j log(a + epsilon delta_j)`.

Averaging the expansion and using `sum_j delta_j = 0` gives

`m(epsilon) = log a - (K^2/2) epsilon^2 (1/K) sum_j delta_j^2 + O(epsilon^3)`.

By the definition of the centered log-ratio map,

`[Psi(S_lambda(p))]_i = log(a + epsilon delta_i) - m(epsilon)`.

Therefore

`[Psi(S_lambda(p))]_i = K epsilon delta_i - (K^2/2) epsilon^2 (delta_i^2 - (1/K) sum_j delta_j^2) + O(epsilon^3)`.

The displayed quadratic and cubic terms are `O(epsilon^2)` for fixed `p`, so, componentwise,

`[Psi(S_lambda(p))]_i = K epsilon (p_i-a) + O(epsilon^2)`.

Substituting `epsilon = 1-lambda` and `a = 1/K`, for every coordinate `i` we obtain

`[Psi(S_lambda(p))]_i = K(1-lambda)(p_i-1/K) + O((1-lambda)^2)`.

Since there are finitely many coordinates, this is equivalently the vector statement

`Psi(S_lambda(p)) = K(1-lambda)(p-u) + O((1-lambda)^2)`

in any fixed norm, as `lambda` approaches `1` from below.
