# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs a finite nonnegative, possibly non-probability base measure containing the range of any epsilon-LDP mechanism in Q_m. A density-envelope proof must justify the essential-envelope ratio without taking an uncountable union of exceptional null sets; countable representing families or a valid alternative suffice.
- **2 points:** Justifies projection existence under the stated assumptions, establishes pointwise and uniform WPM dominance, and proves WPM privacy from the common bounds. The converse common-set implication is the same privacy argument and need not be duplicated.
- **2 points:** Proves the Dirac reduction needed in the finite specialization by convex mixtures and a coupling, including the reverse inequality. An exact finite-mixture proof suffices; a general continuous-space reduction is not required by the public target.
- **3 points:** Derives the finite coordinate constraints and their exact feasibility domain, derives the displayed greedy formula for phi_i and justifies its optimality, and proves convexity of f(m)=max_i phi_i(m).
- **1 point:** Verifies continuity or lower semicontinuity sufficient for attainment on the nonempty compact domain, obtains m*, and proves both inequalities in the minimax equality and the stated value.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require incidental presentation choices. Merely naming projection, polytope, or knapsack methods without deriving the required inequalities earns no credit for those steps. Failure to justify convexity or minimax attainment is theorem-critical.

Do not require compactness of V: it is only a Borel subset of the compact input space. Projection existence can be proved by viewing Q_m in the ambient compact-space probability measures and using its domination inequalities to establish weak closedness. Any independently valid existence argument is acceptable.

Mechanisms and projection choices are not assumed measurable as functions of the input law. Consequently, a continuous-space argument integrating arbitrary Dirac projection choices must justify its kernel or avoid that integral. The finite Dirac argument has no such issue and fully satisfies the public task.

The finite formula and minimax claim include zero coordinates, tied costs, k_v=1, and both endpoints of the total-mass interval. A unified proof covering these cases is sufficient; separate case splits are not mandatory. The public regime has epsilon>0, so an epsilon=0 extension is not required.

The source's unrestricted threshold definition is privately repaired by restricting its minimum to the finite row-cost set. Solvers are not required to introduce any threshold: the public greedy formula is well-defined throughout D. Do not reward or require discussion of source labels or source repairs.

Convexity and compactness alone do not establish attainment without the needed semicontinuity. Continuity follows directly from the public finite minimum/positive-part expression, and a short explicit verification suffices. All listed obligations have a completed derivation in the reference proof; no private GT gap remains.
