# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Nearest-neighbor control and positive local separation (2 points).** Establishes sufficiently strong concentration for actual neighbor prefixes and obtains positive local separation almost everywhere by differentiation. Fixed-query bounds followed by integration suffice. Handles atoms and distance ties, or supplies an equally valid argument for the stated convention. Does not claim all-query concentration with a dimension-free fixed-query threshold.
2. **Adaptive elimination mechanism (3 points).** Relates a local separated neighborhood and an integer iteration index to the threshold and cap. Proves that at least one pointwise bag maximizer survives until every nonmaximizer is removed. Handles ties among optimal labels and subsequent iterations. Uses alignment only on a full-measure set to conclude membership in the Bayes-optimal set, not equality to a predetermined Bayes selector.
3. **Almost-sure Bayes consistency (3 points).** Converts the almost-everywhere query guarantee to a valid risk statement, including empty high-advantage regions and the null alignment-exception set; derives the vanishing low-advantage contribution or an equivalent conclusion; verifies the schedules and applies Borel-Cantelli on the common training probability space. Respects the cap 1<=T_n<=n and the universal lower-bound scope of c1.
4. **Indistinguishability converse (2 points).** Gives an actual pair with identical observable laws, incompatible Bayes-optimal decisions on a positive-mass set, and one aligned distribution. Checks the bag law and alignment. Proves impossibility using excess risk or an equivalent quantitative argument. Different selected Bayes rules alone are insufficient if their optimal sets overlap. Concludes impossibility for the full PLL class and any class containing the constructed pair.

# Evaluator Notes

Accept any correct alternative proof. Do not require the reference proof's presentation choices, salience notation, advantage formulation, particular constants, or particular indistinguishable pair.

The fixed task does not require proving the source's stronger claim about every strictly broader scenario class. Do not award a completed converse step for merely citing a general swapping construction without checking ties, observable-law preservation, and incompatible optimal decisions.

It is enough to retain one optimal label. A claim that every optimal label survives is unnecessary and generally unjustified. The risk target allows different predictions among tied Bayes-optimal labels.

Alignment is assumed almost everywhere. A fixed-query bag-optimality guarantee can be converted to true-posterior optimality only where alignment holds. Integration needs only the resulting almost-everywhere bound. Changing a conditional-probability version on a null set does not refute the public risk theorem. An isolated pointwise-for-almost-everywhere overstatement, when the integrated argument is otherwise correct and immediately repairable, is a minor quantifier error rather than a failure of the consistency target.

Do not accept a proof that ignores distance ties by assuming atom-free data; that assumption is absent. Do not accept arbitrary early stopping before the cap unless a singleton remains. A sufficiently large fixed universal threshold constant is essential to the stated guarantee.

The replacement reference proof closes all obligations of the frozen target; there is no unresolved GT step.
