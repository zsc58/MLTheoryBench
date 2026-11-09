# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Establishes joint Borel measurability of the empirical ghost-gap map from the stated evaluator and target assumptions, including the prescribed zero value for empty samples, and correctly concludes that its threshold witness set is Borel for every nonnegative sample size and every real threshold.
- **3 points:** Correctly identifies the bad event as the witness-set projection, verifies the hypotheses of the analytic projection result, and uses analytic universal measurability to obtain completion-measurability for every finite Borel measure on the paired sample space. In particular, establishes the event-completion property for every stated product probability measure and every positive threshold. The argument must allow an empty parameter space.
- **2 points:** Gives a valid jointly Borel parametrization of \(\mathcal C_A\), including the zero function, and validly applies the first conclusion to obtain its event-completion property. Analytic non-Borel \(A\) is necessarily nonempty, so a parametrization with range \(A\) has a nonempty parameter space.
- **2 points:** For \(m=1\) and \(c\equiv0\), derives the bad-event/superlevel set exactly as \(P_A=\{(x,y):y\in A,\ x\ne y\}\), proves it non-Borel by a section argument or another valid argument, and correctly concludes failure of the supremum-Borel property.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The analytic bridge is required for every real threshold, while the definition of event completion requires only positive thresholds. Preserve this distinction. The positive bridge concerns Borel measurable targets; the supremum-Borel property quantifies over all targets, and one Borel target suffices to refute it.

The standard results that Borel projections are analytic, analytic sets are measurable in every finite Borel completion, and analytic subsets of \(\mathbb R\) admit standard-Borel parametrizations may be invoked without reproving them. Their applicable hypotheses must be checked. No paper-specific theorem or specialized unproved method is needed.

Zero-length samples and empty parameter spaces may be covered uniformly; separate case paragraphs are not required when the proof already handles them. A proof that divides by the sample size without covering the zero-length case has an omitted boundary case. Do not introduce a nonemptiness assumption on the parameter space.

The reference proof's final implication from the supremum-Borel property to event completion explains the strict comparison. A separate discussion of that implication is not required for full credit when both numbered public claims are completely proved.
