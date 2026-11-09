# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Score-error reduction and density-ratio transfer (3 points).** Represent the log-ratio error as the time integral of the score error, apply Cauchy--Schwarz and Tonelli, change measure from the terminal law to the intermediate density, and derive the factor \(e^L\) from the uniform time-Lipschitz condition. An equivalent direct comparison of the densities is acceptable.
2. **Integration-by-parts decomposition (3 points).** Derive the cross-term identity with both endpoint contributions and the model-score time derivative, obtaining the fitting-loss/surrogate decomposition with the stated full normalization. Justify the signed integration using the explicit admissibility assumptions and the bounded marginal score, or an equivalent valid argument. Do not merely assume the desired decomposition or invoke an unspecified score-matching theorem.
3. **Variance identification (2 points).** Show that normalization implies the marginal time score has zero mean for almost every time and identify the integrated second moment with \(V\). Justify the interchange using the Lipschitz domination, or integrate density increments over arbitrary time intervals and use Fubini. Pointwise differentiability at every time is not required.
4. **Final combination and interpretation (2 points).** Establish both displayed conclusions. Explain that, with \(L\) held fixed, reducing the sum of the surrogate and variance terms reduces the displayed upper bound. In path comparisons, the same chosen Lipschitz bound must be used. Do not infer that variance reduction controls a varying \(L\), necessarily decreases the actual error, or guarantees simultaneous separate minimizers of the two terms.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Treat omission of the endpoint terms, density-ratio transfer, or zero-mean variance step as theorem-critical gaps when no alternative argument supplies the missing conclusion.

The model assumptions make the needed square and derivative integrals finite. A concise verification of the relevant Fubini or differentiation hypotheses is sufficient; an exhaustive restatement of standard integration theorems is not required. Distinguish a readily supplied domination detail from an actually invalid interchange.

The theorem includes \(L=0\). A proof that uses \(p_1/p_t\le e^L\) directly already covers it and need not make a separate case split. A proof using a formula with division by \(L\) must give its continuous interpretation at zero or handle that case separately.

The surrogate need not be nonnegative; the established identity makes its sum with \(V\) nonnegative. Do not require a claim of nonnegativity of the surrogate itself.

The public surrogate has the full normalization. A solver may introduce a half-normalized surrogate internally, but must include the corresponding factor of two when returning to the public identity. No proof of conditional-score objective equivalence, model realizability, or a closed-form path-variance formula is required.
