# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Joint surrogate construction and tight majorization (3 points).** For CP and Tucker and every beta regime in [0,2), explicitly construct a frozen-reference joint surrogate from the model summands. Prove global majorization, equality at the reference, and first-order consistency. Handle beta=0 explicitly or with a justified limit. Jensen is applied in the prediction argument of the divergence. Merely naming Jensen/MM or invoking an unspecified source split earns little credit.
2. **Exact block updates and descent (2 points).** Derive the scalar ratio subproblems and explicit contraction coefficients for CP factors, Tucker factors, and the Tucker core. Derive the unique multiplicative candidates and the epsilon clipping. The actual scalar summand contains the active positive reference multiplier; an explicitly normalized scalar objective is acceptable if this multiplier is restored when computing surrogate decreases. Show that one cyclic sweep decreases the frozen surrogate and hence the outer objective. Correctly use the assumed containment in C; do not claim that entrywise clipping preserves arbitrary convex block constraints.
3. **Uniform decrease and relative error (3 points).** Establish uniform positive scalar curvature on the bounded positive domain and apply the constrained minimizer gap only to feasible comparison points. Account for the reference multiplier and the ratio-to-parameter conversion to obtain a k-independent sufficient-decrease constant. Use exact feasible block optimality, product normal cones, first-order consistency, uniform Lipschitz bounds, and the one-sweep block structure to construct a limiting-subgradient residual bounded by the outer step. Constants may depend on the fixed data and dimensions, but not on k.
4. **KL convergence (2 points).** Establish objective convergence, square summability and vanishing increments, critical cluster points with the required objective-value continuity, and finite length. A correctly stated standard KL descent theorem with every relevant hypothesis checked is sufficient; alternatively give the uniformized-KL telescoping argument. Deduce convergence of the whole sequence to a feasible critical point. Include the eventually stationary case.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices, its particular conservative constants, or its notation. The curvature argument remains a private proof obligation, not an additional public assumption.

The update constraint is entrywise Z>=epsilon. Membership of the generated outer sequence in the specified compact block-product set C is a hypothesis. Intermediate mixed-block states then lie in C. A lower-constrained minimizer that lies in C_b is also a minimizer over C_b. No proof that an arbitrary C is invariant is required, and adding a projection or normalization generally changes the specified iteration.

Award credit for correctly handled beta boundary cases and for propagating only justified dependencies. Omitting the active reference multiplier solely in a normalized scalar minimization is harmless if the normalization is stated; omitting it from an asserted equality for the joint surrogate or its quantitative decrease is an error. A wrong numerical decrease constant can be locally repairable, while an unsupported existence of any uniform positive constant is a major gap. Theorem-critical omissions in surrogate construction, Tucker contractions, feasible optimality, or KL estimates are major gaps.
