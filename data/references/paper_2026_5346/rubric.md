# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Valid threshold processes.** Shows that, before a fixed threshold becomes safe, its stopped product is an adapted nonnegative supermartingale. The argument must use the unsafe conditional-mean inequality and verify nonnegativity of every factor; merely calling the product an e-process is insufficient. Predictability of the stopping/freezing decision follows from the conditional-mean definition of the frontier. Zero conditional action probability does not make a threshold unsafe.

- **3 points: Simultaneous certification and deployment safety.** Applies a time-uniform crossing bound to each stopped threshold process, sums the stated epoch-threshold budgets, and uses within-epoch frontier monotonicity plus the one-round deployment delay to conclude that every adaptively selected maximum certified threshold is safe on an event of probability at least 1-delta. This central transfer must address all epochs and thresholds, including epoch-initial abstention.

- **2 points: Drift-adjusted exponential supermartingale.** Constructs a valid exponential supermartingale for excess verifier losses accumulated on safe deployed rounds, under the original probability law. The proof must correctly verify the conditional drift inequality and the bounded-increment/Hoeffding step, including the random action clock. An action-conditioned mixture argument, or a valid equivalent construction, closes this obligation.

- **3 points: Time-uniform stitching and final risk bound.** Obtains a boundary uniform over all horizons by a valid dyadic stitching or equivalent argument, with the stated log(1/delta)+log log(eN_T+e) dependence. It must intersect the two probability events, identify the safe-round clock with N_T, divide by N_T when positive, and handle N_T=0, giving total probability at least 1-2delta. All positive clock values, including one, must be covered. Constants must be universal; the reference proof's particular constants are not required.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A concentration argument that is only fixed-time does not establish the target. Likewise, per-threshold validity alone earns no credit for the deployment-safety step unless the proof transfers it to the adaptively chosen maximum certified threshold.

The safe-round concentration process must be justified before intersecting with the global no-false-certificate event. Conditioning on that future event does not automatically preserve supermartingales. A predictable safe-step mask, stopping at the first unsafe deployment, or another correctly justified construction is acceptable.

The action indicator is generally not predictable. Do not accept the inequality E[exp(lambda M_t)|F_{t-1}]<=exp(lambda^2 A_t/8) merely because it appears in the source. The required bound is on the compensated one-step factor, obtained by conditioning on the action branch and averaging, or by a valid equivalent argument. For drift adjustment, subtract nu_j E[A_t|F_{t-1}] in the conditional mean. The length-one interval is an action-conditional interval; no upper restriction on the stated nonnegative drift budgets may be introduced.

Bets at the allowed upper endpoint may produce a zero factor; nonnegativity, not strict positivity, is sufficient. Neither persistent positive action probabilities nor positive safe-side margins are needed. A stronger valid square-root-only concentration bound proves the requested bound after adding the nonnegative linear term.

The reference proof explicitly repairs local source proof errors in theory_004 and theory_005. These corrections do not create new solver obligations beyond proving the public claim correctly. No specialized external dependency or unresolved GT step is designated as completed credit.
