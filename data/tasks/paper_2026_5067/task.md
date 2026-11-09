# Problem

## Setup

Let n be a positive integer, let F:R^n -> R be differentiable, and fix x,x' in R^n. Define the straight path

gamma(alpha)=x'+alpha(x-x'),  alpha in [0,1].

All integrals below are Lebesgue integrals. Assume that, for every coordinate i=1,...,n, the function alpha -> partial_i F(gamma(alpha)) is measurable and

integral_0^1 |partial_i F(gamma(alpha))| d alpha < infinity.

Let p:[0,1] -> [0,infinity) be a measurable probability density, so that integral_0^1 p(s) d s=1, and define its cumulative distribution function by

G(alpha)=integral_0^alpha p(s) d s.

For a baseline y in R^n for which each function u -> partial_i F(y+u(x-y)) is measurable and absolutely integrable on [0,1], define integrated gradients by

IG_i(x;y)=(x_i-y_i) integral_0^1 partial_i F(y+u(x-y)) d u.

For a measurable nonnegative weight g on [0,1] satisfying

integral_0^1 g(alpha) d alpha < infinity

and, for every coordinate i,

integral_0^1 g(alpha)|partial_i F(gamma(alpha))| d alpha < infinity,

define path-weighted integrated gradients by

PWIG_i(x;x';g)=(x_i-x'_i) integral_0^1 g(alpha) partial_i F(gamma(alpha)) d alpha.

For s in [0,1], let b_s=x'+s(x-x'), and define path-sampled integrated gradients by

PSIG_i(x;x';p)=integral_0^1 IG_i(x;b_s) p(s) d s.

## Task

Prove that, for every coordinate i=1,...,n,

PSIG_i(x;x';p)=PWIG_i(x;x';G),

where G is the CDF of the sampling density p.
