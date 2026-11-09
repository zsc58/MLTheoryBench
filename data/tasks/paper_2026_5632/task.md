# Problem

## Setup

Let d be a finite nonnegative integer and let X be a subset of [0,1]^d, equipped with its trace Borel sigma-algebra. Let P be an arbitrary probability distribution on X x [0,1], using the product sigma-algebra. Let G be a finite nonempty family of measurable functions g:X->[0,1], fixed before sampling. All logarithms are natural.

A deterministic grid predictor is a measurable function f:X->V, where V is a finite nonempty subset of [0,1]. Define its expected calibration error with respect to G by

Cal_P(f;G) = max_{g in G} sum_{v in V} | E_{(X,Y)~P}[g(X) 1{f(X)=v} (v-Y)] |.

The learner is given d, the accuracy parameter, and the group family, and receives independent identically distributed samples from the unknown distribution P. It has no access to P other than these samples. It may use randomization during training. Its output includes a finite grid V chosen by the learner and a deterministic predictor f:X->V: after the sample and training randomness are fixed, every query x has one fixed prediction f(x).

For the computational claims, G is supplied as an indexed family with evaluation access to g(x). Running time counts group evaluations, real arithmetic and comparisons, evaluations of exp, log, and square root, random-access storage operations, and independent uniform-real draws during training as unit-cost operations. The implicit representation may store real numbers.

## Task

Prove that there is a universal constant C and a learning algorithm such that, for every X, P, and G as above and every epsilon in (0,1/10), it uses at most

C ((1/epsilon + log(|G|+1)) log((1/epsilon + log(|G|+2))/epsilon)) / epsilon^2

independent samples and, with probability at least 2/3 over the sample and training randomness, outputs a deterministic grid predictor f satisfying

Cal_P(f;G) <= epsilon.

If n is the number of samples used, the predictor has an implicit representation constructible in time polynomial in n, |G|, d, and 1/epsilon, and can be evaluated on a query in time polynomial in |G|, d, 1/epsilon, and log(n+1), in the computational model specified above. In particular, for every fixed kappa >= 0, if |G| <= epsilon^{-kappa}, the sample complexity is tilde-O(epsilon^{-3}), where tilde-O suppresses polylogarithmic factors in 1/epsilon and |G| and constants may depend on kappa.
