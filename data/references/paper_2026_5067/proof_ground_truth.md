# Reference Proof

## Proof Structure

For each sampled baseline, reparameterize its integrated-gradient path as a tail segment of the original path. Verify that the sampled attribution is measurable and integrable. Apply Fubini's theorem to the resulting absolutely integrable function on the triangular integration region, identify the inner density integral with the sampling CDF, and recognize the path-weighted attribution.

## Complete Proof

Fix a coordinate i. Write d_i=x_i-x'_i and h_i(alpha)=partial_i F(gamma(alpha)). The public assumptions give a measurable h_i with integral_0^1 |h_i(alpha)| d alpha < infinity. Since p is a probability density, its CDF G is measurable and satisfies 0 <= G(alpha) <= 1. Consequently G is an integrable nonnegative weight and

integral_0^1 G(alpha)|h_i(alpha)| d alpha <= integral_0^1 |h_i(alpha)| d alpha < infinity.

This holds for every coordinate, so PWIG(x;x';G) is within the stated definition domain.

For s<1, x-b_s=(1-s)(x-x'), and

b_s+u(x-b_s)=x'+[s+u(1-s)](x-x')=gamma(s+u(1-s)).

The affine change of variables alpha=s+u(1-s) gives

integral_0^1 |partial_i F(b_s+u(x-b_s))| du
= (1/(1-s)) integral_s^1 |h_i(alpha)| d alpha < infinity.

Thus the integrated-gradient expression at b_s is defined. Applying the same substitution to the signed integral gives

IG_i(x;b_s)=(1-s)d_i integral_0^1 h_i(s+u(1-s)) du
=d_i integral_s^1 h_i(alpha) d alpha.

At s=1, b_s=x. The integrand in the IG definition is the finite constant partial_i F(x), and its prefactor is zero. Thus IG_i(x;b_1)=0, agreeing with the tail-integral formula at s=1. The formula therefore holds for every s in [0,1]. Since h_i is integrable, its tail integral is continuous as a function of s. In particular, s -> IG_i(x;b_s) is measurable. Moreover,

|IG_i(x;b_s)| <= |d_i| integral_0^1 |h_i(alpha)| d alpha,

so its integral against the probability density p is absolutely finite. Hence PSIG is defined.

The function

K_i(s,alpha)=p(s) 1_{s<=alpha} h_i(alpha)

is measurable on [0,1]^2. Tonelli's theorem for nonnegative measurable functions yields

integral_0^1 integral_0^1 |K_i(s,alpha)| d alpha d s
= integral_0^1 |h_i(alpha)| [integral_0^alpha p(s) d s] d alpha
= integral_0^1 G(alpha)|h_i(alpha)| d alpha
<= integral_0^1 |h_i(alpha)| d alpha < infinity.

Fubini's theorem states that an absolutely integrable measurable function on a product measure space has equal iterated integrals in either order. Applying it to K_i gives

PSIG_i(x;x';p)
= d_i integral_0^1 p(s) [integral_s^1 h_i(alpha) d alpha] d s
= d_i integral_0^1 [integral_0^alpha p(s) d s] h_i(alpha) d alpha
= d_i integral_0^1 G(alpha) h_i(alpha) d alpha
= PWIG_i(x;x';G).

No step divides by d_i or assumes distinct endpoints, so zero coordinate displacements and x=x' are included. Since i was arbitrary, the claimed equality holds for every coordinate.
