# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly uses sound coordinatewise feature bounds to place the adversarial feature in each bounding interval and proves that the convex-combination intervals are nested as alpha increases, or supplies an equivalent soundness-based argument supporting monotonicity.
- **3 points:** Derives both endpoint identities and the two-sided bounds. If using scalar interval maximization, correctly justifies that the maximum squared distance is attained at an endpoint; a valid direct argument receives equivalent credit.
- **2 points:** Establishes continuity and monotone nondecrease of the parameterized loss on the full interval [0,1].
- **3 points:** For an affine classification head, uses the correctly typed map zeta(a,y)=g(a)_y 1^K-g(a), decomposes its weights into signed positive/nonpositive parts, and algebraically proves the same-alpha mixed logit representation, or gives an equivalent valid algebraic proof.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, interval notation, or ordering of arguments; assign equivalent credit for the corresponding mathematical obligations.

The adversarial input, maps, teacher feature, and bounds are fixed as alpha varies. Monotonicity means nondecrease, not strict increase. Arguments must remain valid when feature intervals are singletons, when epsilon=0, and at alpha=0 and alpha=1; no separate case discussion is necessary if the proof already covers them.

The notation z_f(u,y) takes an input u in R^d. Do not require or endorse the incorrect composition z_f(g(a),y). The feature-space expression is zeta(a,y)=g(a)_y 1^K-g(a).

The reference proof also verifies the stated soundness of the affine lower logit bound. This verification is a setup consistency check, not an additional scored target. Do not require a proof of a hidden-layer bound-generation algorithm, the standalone worst-case feature-loss upper-bound theorem, or any assertion about classification-loss expressivity.
