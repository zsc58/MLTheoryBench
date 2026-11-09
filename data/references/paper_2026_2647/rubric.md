# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct relative to the public assumptions.

# Core Steps

- **2 points:** Establishes continuity of the conditioning map, including control of denominator changes using the uniform marginal lower bound and continuity in the query variable.
- **3 points:** Constructs the constant-function query embedding, proves the lifted input set is compact, and defines the corresponding continuous lifted map.
- **3 points:** Uses continuous extension to the ambient function space and correctly invokes the compact-set approximation property stated in the public setup to obtain uniform error on the compact lifted set.
- **2 points:** Realizes the embedding with a valid vector-to-function layer and composes it with the approximating neural operator to obtain the stated augmented operator and final uniform bound.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the extension or architecture-specific approximation step as theorem-critical unless an alternative proof supplies those steps. The public approximation property may be invoked as an assumption in a solver proof; awarding credit for that invocation does not independently verify the nonstandard external theorem cited by the source. The private reference proof retains that unresolved external obligation.
