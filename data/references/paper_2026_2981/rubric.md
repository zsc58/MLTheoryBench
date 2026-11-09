# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly formulates the least-squares capacity as the squared norm of the orthogonal projection onto the readout span, including the singular/readout-dependence case appropriately.
- **3 points:** Uses the complete tensor-product orthonormal basis and Parseval to express the sum over the complete input basis as the total input-only projection mass of an orthonormal basis of the readout span, establishing each contribution is at most one.
- **3 points:** Proves the characteristic strictness mechanism: genuine noise dependence gives a nonzero component in a noise basis direction orthogonal to the constant component, so at least one readout-basis vector has input-only mass strictly below one.
- **2 points:** Correctly concludes the strict bound, separately or implicitly handling \(\dim\mathcal S<K\) and \(\dim\mathcal S=K\), and states the integrated result for the total capacity.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.
