# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly rewrites Chernoff Information using the density ratio as \(\sup_{u\in[0,1]}-\log\mathbb E_{P_0}[r^u]\), including the endpoint/continuity justification.
- **2 points:** Establishes fixed-\(u\) convergence of the empirical powered average, using independent training, consistency, bounded convergence, and sampling error control. The argument must justify convergence of the random integral over \(P_0\), for example by bounded convergence in training mean, integration over \(P_0\), and Markov's inequality; conditional variance control then handles the evaluation sample.
- **4 points:** Derives uniform convergence over \([0,1]\) via a valid equicontinuity/Lipschitz (or equivalent uniform-convergence) argument and handles the logarithm using a positive lower bound.
- **2 points:** Transfers uniform objective convergence to convergence in probability of the optimized Chernoff Information value by bounding the difference of suprema.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Do not award the uniform-convergence points for merely naming an empirical-process theorem without verifying its hypotheses.

Convergence in probability is sufficient throughout. Do not require almost-sure consistency of the trained estimator or its integrated estimation error, since neither is assumed. A direct appeal to almost-sure dominated convergence needs an appropriate justification and cannot follow merely from pointwise convergence in probability.

The case \(P_0=P_1\) is included. Strict convexity, uniqueness of the maximizing exponent, and convergence of a chosen optimizer are not required. Do not assume that the clipped estimate satisfies \(\mathbb E_{P_0}r_n=1\); only the true density ratio has this normalization. Routine measurability can be justified by continuity in the exponent and restriction of suprema to a countable dense subset, and need not be a separate scored step.
