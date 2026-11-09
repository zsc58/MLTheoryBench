# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **4 points:** Constructs the fixed-target restricted Shapley game, derives its Mobius coefficients from those of the masked game, and correctly obtains the directed off-diagonal coefficient \(m_U/(|U|(|U|-1))\), or establishes the corresponding result by a valid alternative argument.
- **2 points:** Establishes the singleton Shapley identity and derives, or otherwise validly proves from the definition, the Mobius coefficient \(1/\binom{|U|}{2}\) for the symmetric pair quantity.
- **2 points:** Correctly compares the two coefficient formulas and proves the two Shapley-based diagonal and pair identities, including both directions in the pair sum.
- **1 point:** Proves \(\operatorname{IG}_i(\{i\})=f(\{i\};x)-f(\varnothing;x)\) by a valid one-dimensional fundamental-theorem argument under the stated path assumptions, thereby establishing the path-based singleton identity.
- **1 point:** Correctly identifies the path-based directional quantity with the integrated-gradient meta quantity and obtains the symmetrized pair identity.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. A bare assertion that the restricted metagame or symmetric pair quantity has the required Mobius coefficients does not earn the corresponding derivation credit. Failure to establish the Shapley coefficient comparison leaves the Shapley pair conclusion unsupported.

The public definition of \(\mathcal P_i\) is the endpoint difference \(f(\{i\};x)-f(\varnothing;x)\), not \(\operatorname{IG}_i(\{i\})\). Treating their equality as a definition does not establish the singleton obligation. A correct invocation of the standard one-dimensional fundamental theorem, with its applicability evident from the stated assumptions, is sufficient; a proof of that standard calculus theorem is not required. The hypotheses here give ordinary derivatives at every point of the singleton segment and an integrable derivative, not merely almost-everywhere differentiability.

Do not require \(f(b)=0\), nonzero coordinate displacements, continuous derivatives, or additional positivity assumptions. Arguments must cover \(d=2\) and zero displacements, but a separate case discussion is unnecessary when the argument already covers them without division by a displacement or an invalid denominator.
