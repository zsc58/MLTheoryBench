# Problem

## Setup

Fix integers `d,m >= 1`, an exponent `p in [1,infinity]`, a confidence level `delta in (0,1)`, a total budget `T>0`, a known range `M>0`, and known source costs `d_a>0` for `a in {1,...,m}`.

For each coordinate-source pair `(i,a)`, there is a fixed unknown distribution supported on `[0,M]`, with mean `theta_i` and variance `v_{i,a}^2>0`; write `v_{i,a}` for its positive standard deviation. The pair has a sequence `(X_{i,a}^{(r)})_{r>=1}` of independent draws from this distribution, and the sequences for all pairs are jointly independent. Querying `(i,a)` costs `d_a` and reveals its next previously unobserved draw. The means and variances are not given to the estimator.

Let

`Lambda = {lambda in [0,infinity)^(d m): sum_{i,a} lambda_{i,a}=1}`.

For `lambda in Lambda` and finite `p`, define

`A_p(lambda) = [sum_i (sum_a lambda_{i,a}/(d_a v_{i,a}^2))^(-p/2)]^(2/p)`.

For `p=infinity`, define

`A_infinity(lambda) = max_i (sum_a lambda_{i,a}/(d_a v_{i,a}^2))^(-1)`.

These are extended-real-valued objectives: if the inner sum is zero for any coordinate, set the corresponding reciprocal power, and hence the objective, equal to `+infinity`. Let

`Gamma_p = min_{lambda in Lambda} A_p(lambda)`.

Consider the following two-stage estimator. Put

`D = d sum_a d_a`, `L = log(4dm/delta)`.

Define the real exploration prescription

- if `p>=2`, including `p=infinity`,
  `N = (2T)^(1/3) (M^2 L)^(2/3)`;
- if `1<=p<2`,
  `N = 2^(p/(2p+2)) M^((3p+2)/(2p+2)) L^((3p+2)/(4p+4)) T^((p+2)/(4p+4))`.

Set `n_0=max{2,ceil(N)}` and assume `T >= 2n_0D`.

First query every pair exactly `n_0` times and compute

`hat v_{i,a}^2 = [2n_0(n_0-1)]^(-1) sum_{1<=r != s<=n_0}(X_{i,a}^{(r)}-X_{i,a}^{(s)})^2`,

where `hat v_{i,a}` denotes the nonnegative square root. Set

`eta = M sqrt(2L/(n_0-1))`, `bar v_{i,a}=hat v_{i,a}+eta`,

and `T'=T-n_0D`.

For each coordinate choose

`hat a(i) in argmin_a d_a bar v_{i,a}^2`,

using a fixed deterministic tie-breaking rule chosen before observing the data. Put `alpha=p/(p+2)` for finite `p`, and `alpha=1` for `p=infinity`, and define

`hat lambda_i = [d_{hat a(i)}bar v_{i,hat a(i)}^2]^alpha / sum_l [d_{hat a(l)}bar v_{l,hat a(l)}^2]^alpha`.

Use the following integer-rounded second-stage allocation:

`D_hat=sum_i d_{hat a(i)}`,

`n_i = 1 + floor((T'-D_hat)hat lambda_i/d_{hat a(i)})`.

The selected sources and all second-stage counts are determined from the first-stage observations before any second-stage observation is revealed. Query each selected pair `(i,hat a(i))` an additional `n_i` times and return

`hat theta_i = (1/n_i) sum_{r=1}^{n_i} X_{i,hat a(i)}^{(n_0+r)}`.

The exploration observations are not reused in these means.

## Task

Prove that the estimator is well defined, spends at most `T` almost surely, and, with probability at least `1-delta`, satisfies

- for `p>=2`, including `p=infinity`,

  `||hat theta-theta||_p <= sqrt(2Gamma_p log(4d/delta)/T) + O(M^(1/3)Gamma_p log(4dm/delta)^(2/3)/T^(2/3));`

- for `1<=p<2`,

  `||hat theta-theta||_p <= sqrt(2Gamma_p log(4d/delta)/T) + O(M^(p/(2p+2))Gamma_p log(4dm/delta)^((3p+2)/(4p+4))/T^((3p+2)/(4p+4))).`

The big-O constants may depend on `p`, the source-cost vector, the cost-variance array `(d_a v_{i,a}^2)_{i,a}`, `D`, and the fixed rounding convention, but not on `T` or `delta`. The bounds must hold uniformly over the choices of `T` and `delta` satisfying the displayed budget assumption.
