# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly obtains the Gaussian conditional predictors or an equivalent justified formula for the Gaussian velocity. A score-based derivation is acceptable but not required. Essential conditional-expectation identities must be justified rather than invoked as an unspecified specialized result.
- **3 points:** Proves both directions of the global zero-velocity characterization, including the conclusion that the constant variance equals one by the endpoint conditions. A pointwise-in-time assertion without the global argument is insufficient.
- **3 points:** Proves the displayed normalized-schedule velocity identity. Accept either a derived conditional-velocity transformation or direct computation of both Gaussian velocities. Correctly handles the schedule coefficients and denominators; merely naming a conversion theorem is insufficient.
- **2 points:** Correctly evaluates the initial endpoint and proves b^L(0,z)=z+bar b(0,z)=E[X] for every z, using the endpoint definition or a justified continuous extension.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental score notation, auxiliary diffusion quantity, general space/time transformation, or separate verification of background well-posedness when a direct proof establishes all requested claims. In the present Gaussian setting E[X]=0, and explicitly establishing this value is acceptable.

The public definitions use spatially continuous conditional-expectation versions. An almost-everywhere computation extends pointwise by continuity and full support; do not demand excessive measure-theoretic detail when this interpretation is clear.

Do not require a non-Gaussian theorem or a claim about approximate learned velocities. The exact linear conditional velocity in the public setup is the relevant object.

The source's duplicated dot-u subscript has an existing local repair and should not be penalized when the mathematically correct expression is used. If a solution uses epsilon*/(alpha c) at t=1, it must cancel the removable factor or use its continuous extension, rather than substitute into 0/0. None of these private source details is a required proof route.
