# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **Step 1 (2 points):** Correctly uses the conditioned distributions, classifier-output probabilities, subgroup events, and positivity conditions needed for the conditional probabilities.
- **Step 2 (3 points):** Derives the exact identity for every positive-mass subgroup by conditional-probability expansion, common-denominator algebra, and the decomposition into the two classifier outputs, including the factor \(1/(p_1p_0)\).
- **Step 3 (2 points):** Uses the positive subgroup-independent factor to establish equality of the maximizing subgroup sets over the same full class \(\mathcal S_A\). Accounts for null subgroups: they have zero probability under both conditioned distributions and zero defined disparity, including when the maximum value is zero.
- **Step 4 (2 points):** Identifies the SD supremum with \(\mathsf M\), justifies restricting its value to the nonempty positive-mass subgroup class, and obtains the stated supremum formula.
- **Step 5 (1 point):** Correctly derives the maximum-discrepancy bound from the uniform \(\gamma\)-weighted-parity condition for \(\gamma\in[0,1]\).

# Evaluator Notes

Accept any complete valid alternative proof; do not require the reference proof's presentation choices. The definition of probability conditioned on an event is sufficient; explicitly invoking Bayes' rule is not required. Equality of maximizing sets must use the same domain for both objectives. A proof that handles only positive-mass groups must also account for null groups before asserting equality over all of \(\mathcal S_A\). Showing that null groups do not change the supremum value alone does not establish that they can be omitted from the maximizing set when the maximum is zero. No separate proof of existence of a maximizing subgroup is required. The empty conjunction supplies a positive-mass subgroup, so the positive-mass class is nonempty.
