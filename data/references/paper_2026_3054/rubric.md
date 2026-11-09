# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **(2 points)** Correctly identify the forward and reverse laws, initialization and terminal distributions, Gaussian-relative density normalization, and score-error expectation under the true forward law. Use the stated regularity and integrability hypotheses without assuming entropy continuity at an endpoint.
2. **(3 points)** Derive the relative-entropy flow from the two Fokker-Planck equations, obtaining the negative relative Fisher-information term and the exact Young-inequality coefficient. With alpha=1/2 and the learned marginal's LSI, obtain D'<=-D/C+e/2.
3. **(3 points)** Establish the Gaussian LSI normalization and the propagated constant C(r)=exp(2 integral_0^r L)+2 integral_0^r exp(2 integral_s^r L)ds, with L(r)=M_{T-r}-1. Supply a valid propagation derivation or a precisely stated applicable independent result. Integrate the entropy inequality, justify initialization and terminal limits, and obtain the weighted bound with its initialization term. In the singular case, apply propagation on intervals ending strictly before T and pass to the endpoint; do not apply a closed-interval integrability theorem directly to c/(T-r).
4. **(2 points)** Evaluate the weights for M>1, M=1, M<1, and M_t=1+c/t with c>1. Prove the stated M<1 exponential upper bound, cover zero and negative M without invalid divisions, and use L(r)=c/(T-r) in the time-dependent computation.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

A citation to the source's own propagation claim, or an unspecified specialized propagation theorem, does not by itself close the central propagation obligation. A correctly stated independent theorem is acceptable when its hypotheses and normalization are checked.

Do not accept the Lebesgue score in place of the Gaussian-relative score while retaining the drift -x+s^theta. These describe different diffusions. Do not substitute learned-process expectations for the true forward-process expectations.

Weak convergence alone does not justify an upper limit for initialization entropy. The bounded-test-function comparison in the reference proof is one acceptable endpoint argument; a valid alternative entropy comparison is equally acceptable. Joint lower semicontinuity suffices at the terminal endpoint.

The reference proof derives all theorem-critical obligations. There is no unresolved ground-truth exception and no rubric step that is merely presumed complete because the paper cites it.
