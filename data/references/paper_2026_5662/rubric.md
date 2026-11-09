# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Uses the given definition \(g=a\otimes e\) and correctly expands \(\langle F_i,F_j\rangle_F\) into \(\mathbb E[(a^\top a')^2(e^\top e')^2]\) using independent task draws.
- **3 points:** Establishes that this expectation is the inner product of the joint product-kernel mean embeddings, handles the self terms, and obtains the normalized cosine identity under the stated nonzero-norm condition.
- **2 points:** Defines or otherwise validly analyzes the factored Rademacher feature and proves that its expected inner product is exactly the product kernel, without replacing the argument by an unsupported assertion of unbiasedness.
- **2 points:** Correctly derives the \(81/m\) variance bound from iid coordinates and the Rademacher fourth-moment inequality, and justifies the stated factored \(O(m(d+K))\) evaluation cost.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices.

The public task supplies \(g_t(a,e)=a\otimes e\) as a definition. Do not require a separate differentiation argument, a specified loss, or a head parameterization to earn full credit. The reference proof's parenthetical explanation of the affine-head interpretation is optional, not an additional proof obligation.
