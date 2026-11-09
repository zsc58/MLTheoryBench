# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Calibration reduction (2 points):** Correctly convert the two conditional error penalties into unconditional expectations involving \(1-S\) and \(S\), using the positive class probabilities and the fact that the policy depends only on the score.
2. **Pointwise objective and value (3 points):** Derive the three costs \(1\), \(a(1-s)\), and \(bs\); establish the lower bound for every admissible policy; and justify attainment by a measurable deterministic minimizing policy. Obtain \(\mathbb E[\min\{1,a(1-S),bS\}]\). A fixed-priority tie rule or the explicit measurable threshold construction is sufficient.
3. **Threshold characterization (3 points):** For positive weights in the regime where verification is jointly minimizing somewhere, establish the ordered reject, verify, and accept regions and valid boundary choices. Include coincident thresholds, at which all three costs tie. The condition \(1/b\le1-1/a\) already places both thresholds inside \((0,1)\), so no separate clipping operation is required.
4. **Complementary and degenerate cases (2 points):** When \(1/b>1-1/a\), derive the acceptance/rejection crossing and verify that the chosen acceptance or rejection cost is below one, including at the crossing. Correctly handle either or both weights being zero with endpoint-degenerate thresholds and suitable boundary actions.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or explicit threshold formulas if another argument establishes all claims.

The score distribution may have atoms, including at zero, one, or a threshold. Boundary actions therefore cannot be dismissed as changes on probability-zero events. Arbitrary tie handling means a choice among minimizing actions, not permission to select a more costly action. In particular, a collapsed threshold does not force strong verification.

Measurability is automatic for an explicitly constructed threshold policy with finitely many boundary choices. Do not require a separate general selection theorem. Conversely, continuity of the costs alone does not imply that every arbitrary selection from a continuum of ties is measurable.

Do not require a characterization of every optimal policy, a Pareto-frontier theorem, treatment of zero class probabilities excluded by the setup, or any sequential-algorithm guarantee.
