# Problem

## Setup

Fix an integer horizon \(T\ge2\). On each round \(t\), a learner, possibly randomized and history-dependent, chooses and announces a probability distribution \(\mu_t\) on \([0,1]\), using information from previous rounds and its internal randomness. After observing \(\mu_t\) and the previous history, an adaptive adversary chooses and reveals a convex 1-Lipschitz loss function \(\ell_t:[0,1]\to\mathbb R\). Then \(X_t\sim\mu_t\) is sampled using fresh randomness, and the learner incurs \(\ell_t(X_t)\). In particular, conditional on the information available before this draw, including the revealed loss, the law of \(X_t\) is \(\mu_t\). All strategy choices and dependence on history are measurable.

For a Borel-measurable mapping \(s:[0,1]\to[0,1]\), let
\[
R_T(s)=\sum_{t=1}^T\bigl(\ell_t(X_t)-\ell_t(s(X_t))\bigr),
\qquad \mathrm{SR}_T=\sup_s R_T(s).
\]
Additive constants in losses are immaterial.

## Task

Prove that there are a universal constant \(C\) and a randomized online algorithm taking \(T\) and a confidence parameter \(\delta\in(0,1/T]\) as inputs before the first round, running in time polynomial in \(T\) and in the cost of evaluating the revealed losses, such that for every adaptive adversary in this game,
\[
\Pr\!\left[\mathrm{SR}_T\le C\sqrt{(T\log T)\log(1/\delta)}\right]\ge1-\delta.
\]
The algorithm may depend on the supplied confidence parameter. By running it with \(\delta=1/T\), deduce the existence of a strategy satisfying
\[
\mathbb E[\mathrm{SR}_T]=O(\sqrt T\,\log T).
\]
