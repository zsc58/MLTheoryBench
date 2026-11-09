# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

1. **Observed transport construction (2 points).** Use the class-wide shared factorization and injectivity on the specified union of pushed ν-dominated probability laws to obtain equality of the pushed concept laws for every observed attribute. Use common positive support at the anchor, or an equivalent valid common-mixture argument, to align the embedding-image carriers. Construct a single t∈Aut_ν(C), interpreted modulo null sets, and justify both k'λ=k(T_tλ) for every ν-dominated probability law λ and μ_a=T_tμ'_a for every observed a. Do not assume that the original embeddings are automorphisms of C or that their images agree everywhere.

2. **Exact extrapolation criterion (3 points).** Establish injectivity of k on ν-dominated probability laws from the stated factorization. Use the pushforward density identity with r=d(T_{t^{-1}}ν)/dν, with the correct orientation, and the already-established anchor identity. Prove both directions between feature equality, concept-law transport, and the transported potential identity for each test attribute. This part must not rely on the additional affine-representation assumption. A valid equivalent measure-theoretic argument need not introduce r explicitly.

3. **Affine-hull extension and normalization (3 points).** Under the additional fixed representation, use a finite affine expansion with coefficients summing to one to transfer observed centered-potential identities to an arbitrary test attribute. Justify composition with the transition on product-almost-everywhere identities and obtain an attribute-dependent almost-everywhere additive constant. Eliminate the constant using anchor transport and probability normalization. No nonnegativity of affine coefficients or full-rank assumption is required.

4. **Integrated conclusion (2 points).** State and justify the exact equivalence on A_test and the sufficient affine-hull condition for extrapolated feature agreement, using the same transition. Preserve the order 'for every attribute, almost everywhere in the concept variable'; no common null set over an uncountable attribute family is required. Keep the additional representation hypothesis confined to the sufficient-condition result.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. In particular, using the single observed anchor instead of an observed mixture is valid under the common positive-support hypothesis. The source's weaker mixture condition, when used, has one probability measure π that works for all indexing kernels; the public task does not require a separate mixture assumption.

Treat an unjustified identification of embedding images, failure to establish a common transition, failure to prove a direction of the exact criterion, or omission of the normalization argument as theorem-critical gaps. The shared channel is assumed injective only on the stated pushed-law set, not on every probability measure on the intermediate space. An everywhere-defined bijection of C is not required. Ordinary almost-everywhere reasoning may be concise, but it must be valid for σ-finite ν and for attribute-dependent exceptional sets. No integrability of log densities is assumed or needed.
