# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Establishes the testing minimization basis correctly. A derivative proof derives the activity stationarity equations, including the free-output condition, with correct next-layer ranges and normalization. A direct proof instead constructs the feedforward activity tuple and establishes that it attains the nonnegative energy's lower bound of zero. Either route is eligible for all points.
- **3 points:** Proves exact testing equivalence in both directions and establishes attainment. Accept backward induction from the output stationarity equation together with the zero-energy converse, or the direct argument that every minimizer must have all residuals zero because the minimum is zero. Identifies the minimizing tuple with the feedforward recurrence. No separate hidden-layer induction is needed when L=1.
- **3 points:** Gives a valid node partition and index correspondence, specifies the consecutive-layer block-sparse weight family with every other weight fixed at zero, and proves the graph energy equals the layered energy plus the clamped-input constant. The mapping must include the first layer and allow unequal widths.
- **2 points:** Transfers training/testing activity argmin sets and permitted-weight argmin sets under the corresponding domains and clamps, and explains structural inclusion in the larger graph class. The argument must not rely on unproved attainment of general training or unrestricted-graph minima.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require derivatives, backward induction, or the reference proof's particular indexing if a correct zero-energy argument and a correct graph construction establish all conclusions.

For the defined energy, the full derivative carries a factor of 2. Writing the correctly scaled stationarity equations without labeling them as full derivatives is entirely valid. A missing common factor of 2 in a derivative label is a readily repairable normalization error, not a failure of the zero-gradient argument. The next-layer summation index ranges over n_{ell+1}, not n_ell.

The weight comparison is optimization over the permitted consecutive-layer blocks, with all other graph entries held at zero. Permitted entries need not be nonzero. Unrestricted optimization over every graph weight is not the stated specialization.

Activities are optimized with weights fixed; weights are optimized with activities fixed. Argmin means the set of global minimizers, possibly empty. Equality of these sets does not assert existence in every training or general-graph problem. For L=1, the hidden-activity tuple is empty and its domain is a singleton.

The final inclusion is structural and concerns feedforward computations during testing. Do not require or credit an unsupported claim that arbitrary extra connections preserve those computations, that a particular iterative optimizer converges, or that predictive-coding training equals backpropagation.
