# Problem

## Setup

Treatments are randomized uniformly: `t ~ Unif[0,1]`. Outcomes are noiseless, `y=f^*(t)`. Fix a peak location `t_0 in [1/2,1)` and a peak scale `y_max>0`, and define

`f^*(t) = (y_max/t_0)t` for `0<=t<=t_0`,

`f^*(t) = y_max(1-t)/(1-t_0)` for `t_0<t<=1`.

The evaluator uses the restricted linear family `f_beta(t)=beta t` and, in the infinite-data limit, chooses the population least-squares coefficient

`beta = argmin_{b in R} E[(b t-f^*(t))^2]`,

where the expectation is over the uniform treatment `t`. It then selects `hat t in argmax_{t in [0,1]} f_beta(t)`. Define the reported optimism and historical-distribution mean squared error by

`O = f_beta(hat t)-f^*(hat t)`,

`MSE = E[(f_beta(t)-f^*(t))^2]`.

## Task

Prove that for every `B>0` and every `eta>0`, there exist `y_max>0` and `t_0 in [1/2,1)` such that the population evaluator satisfies

`O >= B` and `MSE <= eta`.

Thus arbitrarily accurate historical-distribution prediction can coexist with arbitrarily large spurious policy improvement under randomized treatment and an infinite-data, deterministic evaluator.
