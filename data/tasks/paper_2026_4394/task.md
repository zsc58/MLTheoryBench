# Problem

## Setup

Let X be a nonempty finite domain, let H be a nonempty class of functions from X to {0,1}, and let h* belong to H. The class H is known to the learner. For a distribution D on X and a classifier h, define

err_{D,h*}(h) = Pr_{x~D}[h(x) != h*(x)],

where the test point is independent of the training experiment. The VC dimension of H is the largest cardinality of a subset of X on which H realizes every binary labeling.

An empirical risk minimizer (ERM) takes a finite ordered labeled sample consistent with some member of H and returns a member of H agreeing with every sample label. The uniformly random consistent ERM chooses uniformly from the nonempty set of consistent members of H, using fresh randomness on each call.

For each input length N>=1, a majority voter specifies a positive finite number K=K(N) of finite index lists L_1,...,L_K with entries in {1,...,N}. The number and lists depend only on N, not on the observed examples, their labels, or ERM outputs. Repeated indices are permitted. Given an ordered labeled input and a supplied ERM, the voter applies that ERM once to each ordered subsample selected by a list and predicts by pointwise majority of the returned hypotheses. Ties may be resolved by any fixed convention. The voter has subsample size at least t at input length N if every list contains at least t distinct indices.

A monotone adaptive adversary knows H, D, and h*, observes n independent clean points from D, and appends exactly m examples, possibly randomly and depending on the clean points. Every clean and appended example is labeled by h*. The concatenated list is then permuted by an independent uniformly random permutation, and only the resulting ordered labeled sample is given to the learner.

## Task

Prove the following integrated theorem. There are universal constants c>1 and a>0 such that, for every integer d>=1 and every integer n>=cd, both statements hold:

1. There exist a finite domain X, a distribution D, a target h*, a binary class H with VC dimension exactly d, and an ERM E such that the following holds for every integer t with 1<=t<=n for which m=2n/t is integral: for every majority voter having subsample size at least t at input length n+m and using E as its base learner, there is a monotone adaptive adversary appending m examples for which the voter's output h satisfies

   E[err_{D,h*}(h)] >= a d log(n/d)/n.

2. There exist a finite domain X, a distribution D, a target h*, and a binary class H with VC dimension at most d+2 such that the following holds for every integer t with 1<=t<=n for which m=2n/t is integral: for every majority voter having subsample size at least t at input length n+m and using the uniformly random consistent ERM, there is a monotone adaptive adversary appending m examples for which the voter's output h satisfies

   E[err_{D,h*}(h)] >= a d log(n/d)/n.

Here log is the natural logarithm. The expectations include the clean sample, adversary and permutation randomness, and, in the second statement, the ERM's internal randomness. The witnesses X, H, D, h*, and E where applicable are chosen before t and the voter.
