# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Constructs a valid source coupling and justifies its cost as the source Wasserstein distance. The cell-mean coupling may be proved optimal using ordered cells and threshold indicators; another valid optimal coupling is acceptable.
- **2 points:** Propagates original-versus-input-quantized expected errors through nodewise Lipschitz inequalities under a common graph coupling, and expands the homogeneous DAG recurrence into the source-to-terminal path sum.
- **4 points:** Controls recursive compression by a valid support-diameter envelope and a justified scalar quantization estimate; propagates actual coupled errors and unrolls the inhomogeneous recurrence so that source-to-terminal paths carry their length and Lipschitz product. Within these four points, allocate one point to the scalar estimate, one to the diameter envelope and local cost, one to the valid joint-coupling recurrence, and one to path expansion and multiplicity.
- **2 points:** Applies the Wasserstein triangle inequality and obtains the stated terminal bound, with both error contributions, correct constants and quantifiers, and coverage of depth zero, singleton supports, zero Lipschitz constants, and terminal compression.

# Evaluator Notes

Accept any complete valid alternative proof under the stated assumptions. A stronger compression constant earns full credit when it implies the displayed inequality. Do not require the particular scalar potential or topological presentation in the reference proof.

The quantization estimate must be justified by a valid derivation or a precisely stated applicable result; an unexplained invocation of a specialized quantization method is not itself a completed proof step. The assertion that splitting at a mean halves the mass-weighted child support diameters is false and must not be accepted as its proof.

Intermediate variables sharing ancestors can be dependent. Separate optimal couplings of parent marginals need not form the required joint coupling. A proof that substitutes marginal Wasserstein distances for expected errors without addressing this issue has a major gap. Using expected errors throughout a common recursively defined coupling resolves it.

Compression cannot enlarge the diameter of its own precompression support hull. It does not follow that the compressed graph's support diameter is bounded by the corresponding uncompressed graph's support diameter after nonlinear operations. The diameter-envelope argument or a valid alternative is required.

Backward-neighborhood boundaries can contain multiple vertices on one path and can omit intended insertion positions. Neither boundary-sum monotonicity nor an exact boundary-sum/path-length identity may be assumed on an arbitrary DAG. Direct path expansion or another valid counting argument is required.

Do not penalize a solver for avoiding intermediate claims in the original source that are false. The public task asks only for the terminal bound. Missing theorem-critical diameter control, joint-coupling justification, scalar quantization control, or path-length accounting is a major gap; a merely unstated routine boundary case is evaluated according to whether the actual argument already covers it.
