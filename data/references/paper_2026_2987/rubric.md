# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Prove the general conditional backward-increment identity. A time-reversal proof must state an applicable standard theorem or derive the necessary reversed martingale statement, use the reversed path law rather than only matching one-time marginals, and verify its hypotheses. In the reference route, local coefficient regularity, compact-cylinder density integrability, and the weak Fokker-Planck equation justify the local reversed martingale problem. Separately, conditional disintegration and the task's envelope justify the coordinate martingale's zero conditional mean and the drift-average limit. Correctly expand div(pa)/p as div a+a grad log p. Obtain the inverse expression only where a is invertible.
2. **3 points:** Correctly establish the squared-Bessel conditional representation needed for the explicit score. In the reference route, state the transition density with its parameter domain, use Markov bridge factorization, and express the bridge first moment as the ratio of the correctly defined product integral and its negative derivative. Account for initial state zero by the kernel's continuous limit.
3. **3 points:** Derive the explicit Bessel-ratio term rather than assume it. In the reference route, apply the product integral and derivative recurrence to obtain the exact bridge mean or a justified equivalent asymptotic. Justify posterior averaging and the epsilon limit; a pointwise O(epsilon^2) with no expectation control is not sufficient. Recognize that posterior moments can be justified from the kernel, without imposing an unconditional finite prior mean. Use the continuous value zero of the score integrand at initial state zero.
4. **2 points:** Substitute a=4x, b=2(nu+1), and div a=4, or complete an equivalent valid calculation, to obtain the explicit squared-Bessel marginal score with the correct coefficients, conditioning, domain x>0, and statewise almost-everywhere qualification at each interior time.

# Evaluator Notes

Accept any complete valid alternative proof. The four allocations describe mathematical accomplishments, not mandatory presentation choices. In particular, a proof that differentiates the transition-density mixture and rigorously justifies differentiation and posterior conditioning can receive full credit for the explicit-score component without a bridge computation.

Naming the special-function identities without evaluating the bridge mean is insufficient for a proof using the bridge route. Likewise, assuming the explicit marginal score is theorem-critical. However, the absence of a bridge asymptotic is not a defect when a complete alternative derivation supplies the same conclusion.

For the general identity, naming time reversal without establishing applicability is not a completed theorem-critical step. Finite conditional suprema at individual conditioning states do not imply unconditional integrability. A valid local time-reversal theorem can instead be verified using compact-cylinder conditions supplied by the public smoothness assumptions; the conditional envelope then serves the separate coordinate-integrability and limit argument. Do not demand global moment assumptions solely because a solver chooses a theorem stated with stronger global hypotheses.

Do not require the private contextual scaled extension: it is not a public target. Do not demand global ellipticity, a density for p_data, a finite unconditional prior mean, or exclusion of an atom at initial state zero. Distinguish a small omitted boundary clarification from an argument that fails for a permitted initial law. Reserve a score of 10 for a proof that closes all applicable theorem-applicability, conditioning, limiting, and well-definedness obligations.
