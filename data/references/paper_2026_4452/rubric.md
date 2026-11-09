# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly relates restriction densities to conditional expectations on \(\sigma(X)\) and \(\sigma(Y)\), including a Radon–Nikodym/test-event justification. Distinguishes coordinate densities from their pullbacks to \(\Omega\).
- **3 points:** Derives both factor/conditional-expectation equations from an existing joint density with the specified factors, using the nonnegative measurable-multiplier property. The argument must remain valid when an individual factor is not integrable and a conditional expectation is infinite on a zero-factor set.
- **3 points:** From the coupled equations, proves \(a(X)b(Y)\) has total mass one and constructs the corresponding probability measure absolutely continuous with respect to \(P\), without assuming normalization or individual-factor integrability in advance.
- **2 points:** Verifies that the constructed measure has feature and label marginals \(\mu\) and \(\nu\) on their respective measurable coordinate spaces, completing the equivalence and converse existence claim.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices. The central conditional-expectation factorization and the converse normalization/marginal verification must be substantively established; merely naming these methods is insufficient.

The public task concerns the fixed factors \(a,b\), not the existence of an unrelated factorization. It imposes neither strict positivity nor separate integrability of the factors. Nonnegative conditional expectations may be extended-valued, and \(0\cdot\infty=0\). A solver may invoke the standard nonnegative conditional-expectation multiplier rule without reproducing its proof, provided it is used in its applicable nonnegative form. Do not demand an additional integrability assumption or penalize a valid proof for not establishing one.

Marginal verification may use coordinate events \(H\in\mathcal H\), \(G\in\mathcal G\), or an explicitly defined pullback measure on \(\sigma(X)\) or \(\sigma(Y)\). Expressions such as \(\mu(D)\) for an arbitrary \(D\in\sigma(X)\subseteq\mathcal F\) are not literally well-typed unless that pullback interpretation has been supplied. Treat an isolated, unambiguous notation slip as readily repairable; a missing marginal argument remains a substantive omission.
