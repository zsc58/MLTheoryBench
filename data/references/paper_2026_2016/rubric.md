# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Correctly normalizes the intensity, verifies that the latent law is atomless on a standard Borel space, constructs the measure-preserving Borel isomorphism, defines the bilinear digraphon, and proves equality of conditional and Poissonized graph laws. The comparison must use the same ordered-pair convention, including self-loops, and retain all sampled vertices.
- **4 points:** Proves the sectional-BV obstruction. Selects basis vectors from both appropriate full-measure sets, explains why such bases exist, and inverts the corresponding systems to obtain BV latent coordinates or BV representatives. Derives the contradiction between the absolutely continuous joint latent law in dimension 2d>=2 and the Lebesgue-null image of a BV map. A valid standard rectifiability result may replace the elementary covering argument, provided its hypotheses and the pushforward contradiction are correctly stated.
- **1 point:** Establishes almost twin-freeness by using equality of both rows and columns, the two marginal span conditions, and injectivity of the representing isomorphism outside a single null set.
- **3 points:** Applies the assumed directed lifting property, verifies that the composed latent map preserves the required measure, and handles the product-almost-everywhere pullback identity correctly. In particular, if the proof uses pointwise BV sections, it must use Fubini and finite basis selection to produce BV representatives of the latent coordinates, or provide an equivalent valid argument. It then concludes that every weakly equivalent digraphon fails sectional BV.

# Evaluator Notes

Accept any complete valid alternative proof. Do not require the reference proof's incidental presentation choices or its order of steps. The Fubini refinement may be incorporated into the local obstruction or supplied only at the final transfer step; do not double-count it.

The directed lifting property is an explicit assumption. Do not require the solver to prove it or to supply a specialized external citation. The atomless standard Borel probability-space isomorphism theorem is permissible standard background when correctly applied.

Treat omission of a valid basis-extraction justification, the absolute-continuity contradiction, or the lifting application as a theorem-critical gap. Merely naming graphon theory or rectifiability without explaining the relevant conclusion and verifying its hypotheses is insufficient.

Pointwise scalar BV is not invariant under arbitrary null modifications. A proof must not simply assert that product-almost-everywhere equality transfers the stated sectional-BV property to the exact latent pullback. This is a locally repairable issue when the surrounding Fubini-and-inversion argument is otherwise present, but full credit requires the representative issue to be closed.

Do not require uniform bounds on the variations of all sections: the theorem assumes only finite variation for almost every individual section. No product-intensity assumption, bounded-density assumption, or limiting regime is needed. The case d=1 is covered because the joint latent dimension is 2, and N=0 is included in the Poissonized graph law.

Almost-everywhere equality of kernels alone need not preserve self-loop laws. The initial graph-law comparison is justified by the exact constructed pullback; the final lifting identity is used only for the regularity contradiction.
