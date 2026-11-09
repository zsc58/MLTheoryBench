# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses M-convex local optimality and symmetric exchange to justify uniqueness for distinct estimated coordinates and show that every mistaken recommendation supplies a feasible exchange pair with `hat w_t(i)<hat w_t(j)`. Accounts for the full update after every round. Establishes the required well-definedness without introducing a new boundedness assumption on the action sets.
- **3 points:** Distinguishes the exact centroid `c_t` from the coordinate-tie-broken estimate. Uses preservation of strict coordinate comparisons to obtain `c_t(i)<=c_t(j)` for an informative exchange, then applies the exact centroid theorem with the correct halfspace, including the equality case, to prove shrinkage by at most `1-1/e` on every mistake. Uses volume monotonicity on the other rounds.
- **3 points:** Establishes that the hidden coordinate ordering remains feasible, embeds its order simplex in every version space, computes its volume as `1/d!`, and obtains the exact mistake bound `log(d!)/[-log(1-1/e)]`. Uses `P_{T+1}` for mistakes through round `T`. The positive-volume argument also justifies centroid existence and coordinate tie-breaking.
- **2 points:** Converts the mistake bound to the stated exact regret bound using zero regret on correct rounds and the uniform per-round gap bound. Derives `O(B d log(d+1))` with a universal implied constant and handles `d=1` and `B=0` consistently.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The M-convex local-exchange optimality characterization and the standard centroid halfspace theorem may be invoked with their relevant statements and hypotheses. The strict-uniqueness consequence must be justified; symmetric exchange gives a short proof. Strict local inequalities at one point do not, by themselves, justify claiming that every later step along an arbitrary exchange path decreases the objective.

Do not apply the exact centroid halfspace theorem directly to a perturbed estimate. The source-compatible tie-breaking preserves strict comparisons of the exact centroid, which allows the exact argument without weakening the target constant.

The action sets are not separately assumed finite. Finiteness can be derived by fixing the observed true optimizer, using symmetric exchanges to move any other point toward it, and noting that each move increases the true objective by at least the minimum positive coordinate gap of `w*`. The bound on objective gaps then bounds the integer distance. Equivalent well-definedness arguments are acceptable.

The algorithm adds all feasible exchange arcs even on correct rounds. Such additions need only be shown not to increase volume; they need not satisfy the mistake-round shrinkage estimate.

A proof establishing only an unspecified constant-factor shrinkage does not establish the exact numerical bound requested, although it earns appropriate partial credit. There are no unresolved reference-proof obligations.
