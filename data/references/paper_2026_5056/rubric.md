# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **2 points:** Uses the nonempty pseudo-cube definition and the correct DS-dimension contract, and obtains the quantity \(\sum_{i=0}^{d}\binom ni(k-\ell)^i\ell^{n-i}\), by counting the allowed monomials or an equivalent valid argument.
2. **4 points:** For the reference approach, formulates an induction applicable to dimension at most a fixed bound, identifies a point with fewer than \(\ell\) neighbors in some coordinate, interpolates on the projection of the current class before deleting that point, multiplies by the coordinate polynomial vanishing on its neighbor values, and verifies the exponent restrictions. A valid alternative proof earns the corresponding credit for its own main argument establishing the bound.
3. **2 points:** For the reference approach, uses the successive-removal evaluation matrix to establish independence and spanning, thereby completing the induction and proving the cardinality bound. With rows indexed by removal polynomials and columns by removed points, the guaranteed zeros are at \(a<b\); a consistently transposed convention is equally acceptable. A valid alternative proof earns the corresponding credit for completing its cardinality argument.
4. **2 points:** Gives an extremal class of the stated size and proves that its DS dimension is exactly \(d\). Covers the admissible boundary cases: \(d=0\), \(d=n\), \(n=0\), and \(\ell=k\), where only \(d=0\) is admissible. The empty class must not invalidate the upper-bound argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its polynomial method. In particular, an alternative proof need not introduce monomials, interpolation, or a removal order.

For a proof that does rely on the reference induction, an unjustified interpolation step, failure to preserve the dimension or exponent restrictions, or failure to close the spanning induction is a theorem-critical gap. Failure to establish the extremal class's exact dimension is likewise a substantive gap in the tightness claim. Distinguish these gaps from readily repairable indexing slips or routine boundary-case omissions.

The source definition requires a nonempty pseudo-cube. Do not accept arguments that permit the empty set to witness shattering. Do not demand existence of positive-dimensional classes when \(\ell=k\), and use \(0^0=1\) in the displayed count. The source's reversed triangular index at L000112 is a documented local typo, not a condition a correct answer must reproduce.
