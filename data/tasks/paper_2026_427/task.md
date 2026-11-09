# Problem

## Setup

Let `(X,Y)` be a test feature-response pair with `Y` real-valued. A split-conformal procedure uses a measurable real-valued score `s(x,y)` fitted on a separate training fold and `n >= 1` calibration observations `(X_i,Y_i)`, where n is fixed. Conditional on the training data and all randomness used to fit the score, the calibration observations and the test observation are exchangeable. The same fitted score is used for calibration and test observations.

For `u in (0,1)`, set `k_u=ceil((n+1)u)`. Let `Q_u` be the `k_u`-th smallest of the n calibration scores `s(X_i,Y_i)` when `k_u <= n`, and let `Q_u=+infinity` when `k_u=n+1`. Define the measurable prediction set

`B_u(x) = {y in R : s(x,y) <= Q_u}`.

Write `|A|` for the Lebesgue length of a measurable set A. Assume the random sets and fitted functions are measurable so that the membership events and lengths below are measurable.

Fix a target coverage `q in (0,1)`. For each deterministic `p in (q,1)`, let Z be a Bernoulli random variable with success probability p, independent of the training data, calibration data, test pair, and all randomness used to fit or construct the base prediction sets and point prediction. Define

`T_{p,q}(x) = B_{q/p}(x)` if `Z=1`, and `T_{p,q}(x) = {a(x)}` if `Z=0`,

where a is any measurable fitted real-valued point prediction. Thus the second branch has length zero.

Define the base average-length curve

`G(u) = E[|B_u(X)|]`, `u in (0,1)`,

where the expectation includes the training, fitting, calibration, and test-input randomness. Assume that G is differentiable at q in the ordinary real-valued sense and

`G(q)/q > G'(q)`.

For the conditional-coverage clause below, additionally suppose that the base procedure satisfies

`P(Y in B_u(X) | X) >= u` almost surely for every `u in (0,1)`.

## Task

Prove the following integrated claim. For every deterministic `p in (q,1)`, the randomized set has marginal coverage

`P(Y in T_{p,q}(X)) >= q`.

Under the additional conditional-coverage premise, it also satisfies

`P(Y in T_{p,q}(X) | X) >= q` almost surely.

Moreover, there exists a deterministic parameter `p in (q,1)` for which these coverage guarantees hold and

`E[|T_{p,q}(X)|] < E[|B_q(X)|] = G(q)`,

where the expectation on the left also includes the independent Bernoulli randomization.
