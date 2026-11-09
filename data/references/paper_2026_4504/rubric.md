# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Uses the uniform confidence assumption to establish greedy copying of every \(a_N\) and the bound \(\operatorname{ppl}_T(a_N)\le-\log(1-g)\).
- **3 points:** Constructs a one-bit-flipped input for every sufficiently large \(N\), applies the assumed continuity at common histories, and proves that its greedy output remains \(a_N\), hence is an incorrect copy.
- **4 points:** Derives quantitative log-probability bounds using continuity and the uniform positive probability floor, isolates the flipped-coordinate term, averages the discrepancy, and chooses both the continuity tolerance and length threshold so the discrepancy is below the prescribed tolerance.
- **1 point:** States the required quantifiers and combines the discrepancy estimate with the baseline to obtain \(\operatorname{ppl}_T(c_N)<-\log(1-g)+\varepsilon\) for every \(N\) beyond one threshold.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions; the listed construction and induction are a reference route rather than mandatory syntax. An alternative must justify incorrect copying and the required log-perplexity bound with the stated quantifiers.

The model probabilities are raw probabilities on the three-symbol vocabulary. Greedy selection is restricted to the two bits; do not require their probabilities to sum to one or silently renormalize them.

Continuity is an explicit public hypothesis. Solvers need not prove the externally cited architectural continuity theorem. They must apply the stated uniformity correctly rather than compare distributions at different histories without justification.

Probability closeness does not itself give the same numerical bound on logarithms. A valid proof must supply an appropriate logarithmic estimate, such as \(|\log u-\log v|\le |u-v|/\lambda\) for \(u,v\ge\lambda\). Holding the continuity tolerance at a fixed confidence margin and merely increasing length does not make the unchanged-coordinate contribution arbitrarily small.

If a proof invokes a strict-margin intermediate lemma, its chosen margin must be strictly smaller than \(1/2-g\). Choosing half that positive quantity suffices. No change to the stated range \(0\le g<1/2\) is necessary.
