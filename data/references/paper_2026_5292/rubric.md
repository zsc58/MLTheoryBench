# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses the sequential one-action-per-round model, the history-based information restriction, regret, tail function, reservation policy, and threshold-price correspondence. Establishes or correctly justifies the strictly positive mean fresh-inspection gap needed for the converse. Does not introduce free initial observations or access to unrevealed values.
- **3 points:** Proves the reservation-policy upper bound R_T <= 1/p(y)+Ty, accounting for horizon truncation, and evaluates the threshold y_T proportional to T^(-1/(alpha+1)) using the lower tail bound to obtain O(T^(alpha/(alpha+1))).
- **3 points:** Proves the policy-uniform lower bound. The reference route justifies the adaptive inspection-regret and success-count expectations by pre-revelation conditioning, splits according to the expected inspection count, and uses the constant-probability missed-tail event before choosing y proportional to T^(-1/(alpha+1)). A complete valid alternative converse receives the same credit.
- **2 points:** Integrates the tail bounds to obtain lambda(y_T)=Theta(L/T), and proves the constant-epsilon extension under the stated throttled policy. This must account for calendar rounds and the charged first inspection, justify a bound such as R_T(y) <= 1/(epsilon p(y))+Ty, and derive the stated regret order and price Theta(L/(epsilon T)).

# Evaluator Notes

Accept any complete valid alternative proof under the stated sequential action/payoff and randomization models. Do not award credit for merely naming reservation search or a gating method.

The inspection count is generally dependent on the revealed values. A proof must justify the required expectations using nonanticipation, conditional expectation, or an equivalent valid argument; it must not assume that the stopped count and observed values are independent.

The expected number of override opportunities alone does not imply the required expected discovery time. Full credit for the throttled extension requires a valid waiting-time or equivalent calendar-regret argument under the specified independent coins. Merely replacing T by epsilon T in the unthrottled total-regret expression is insufficient.

The first-round inspection consumes a horizon round and receives its revealed value. It is not a free initialization. An equivalent analysis that incurs a bounded additional initialization term is acceptable if it proves the stated asymptotic claims.

The lower-bound constant must be uniform over admissible policies, including horizon-dependent ones. No matching epsilon-dependent lower bound is required. The tail assumption is local, so it is enough that the chosen thresholds lie in its range for sufficiently large T. Do not require continuity of the arm-value distribution or discovery before the horizon.

Do not require a proof of optimality for general costly search, a noisy-bandit regret theorem, or a guarantee under an annealed override schedule. Those are outside the public task.
