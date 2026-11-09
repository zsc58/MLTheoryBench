# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Uses the two positive-probability conditions and conditional independence to establish that \(W=(a',v)\) occurs with positive probability in both grouping cells.
- **4 points:** Correctly derives that the conditional label laws given \(W=(a',v)\) and the two cells equal the respective laws given \(M=v\) and the cells, and uses their difference to prove \(\Pr(Y\mid W,G)\ne\Pr(Y\mid W)\) on a set of positive probability, or establishes the equivalent contradiction directly after passing to the output.
- **3 points:** Correctly uses injectivity on the support to transfer the differing conditional laws to \(Q=g^*(W)\), and concludes failure of generalized calibration. A positive-probability level-set argument or a valid measurable-recovery argument earns full credit.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

For the level-set argument, it suffices to establish that \(\{Q=g^*(a',v)\}\) and \(\{W=(a',v)\}\) agree modulo null sets. The finite-label/simplex state space gives a full-probability support, and the positive-mass input belongs to that support. A correct argument using equality of the conditioning sigma-algebras in this measurable setting is also acceptable; do not require a global inverse when the relevant level set suffices.

A proof that merely asserts that information is lost, names conditional independence, or invokes injectivity without establishing and transferring the differing conditional laws does not earn the associated core-step credit. The different cellwise probabilities need not both differ from the ungrouped probability: at least one must, which is sufficient.

The model- and human-calibration assumptions need not be used beyond verifying the intended setup. Do not require additional positivity of all class probabilities, discreteness of the model output, finitely many grouping cells, distinctness of \(a'\) and \(a''\), or independence of the human and model feature spaces. The one-label case has an impossible unequal-probability premise and requires no separate substantive argument.
