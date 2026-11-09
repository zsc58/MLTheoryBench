# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points — Operational memory:** Uses the equal legality decision required of a memory-passive reduction for the witness configurations. Shows that either accepting both or rejecting both violates faithfulness. Recognizes that different passive experience encodings are allowed and that using protected memory to distinguish legality retains the gate.
- **3 points — Comparison domain:** Uses an undefined protected comparison and the defined truth value supplied by total scalar comparison. Covers ties or otherwise makes clear that equality remains a comparison. Explains that suppressing answers outside D retains the partial domain. Preserving only comparisons already defined is not enough.
- **3 points — Finite penalty:** Fixes an arbitrary finite lambda > 0 for the specified utility q, chooses the jointly available legal/violating witnesses, uses legality to obtain K=1 for the legal witness, and derives the strict score advantage q(k,c')-q(k,c)-lambda > 0. Connects this to failure of scalar-only hard rejection, with filtering or projection identified as boundary retention.
- **1 point — Combination and scope:** Combines the alternatives and correctly states the reconstruction qualification. Does not say that a faithful reconstruction itself loses semantics or claim impossibility of every fixed-state or statically constrained representation.

# Evaluator Notes

Accept any complete valid alternative proof under the corrected definitions. Award points for established mathematical obligations, not merely for naming a method or repeating the conclusion.

Condition 3 concerns a fixed supplied utility and quantifies over finite penalty weights. Do not require, infer, or reward the inconsistent assertion that every real-valued proxy has arbitrarily large violating advantage. Hardness alone does not establish condition 3.

A successful proof need not show that a global maximum exists, that all maximizing updates violate protection, or that the violating witness outranks every legal candidate. The target is preservation of the hard boundary under the expressly defined scalar-only semantics, not an optimizer-existence theorem.

For the comparison branch, an undefined query differs from a defined false query. Ties and noninjective encodings do not preserve undefinedness. A masked scalar comparator can be faithful only by retaining the mask/domain as operational data.

No proof of stability, statistical capacity, factorization, morphism properties, or quantitative guarantee transport is required. No credit should depend on proving unrelated source results. An argument limited to one obstruction earns the points for that obstruction, but a complete proof of the disjunctive statement must address all three possible alternatives.
