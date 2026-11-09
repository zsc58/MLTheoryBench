# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points: Both non-strict inclusions.** Correctly embeds every ordered fixed activation pair into the constant-mixture class, including the factor swap when needed, and realizes arbitrary constant coefficients by bias-only bounded gates with a valid common rescaling.
- **3 points: First strict separation.** Constructs a width-one constant-mixture witness and proves that fixed-pair derivative jumps along its separating hyperplane agree almost everywhere with functions in the appropriate finite ridge-profile classes. Correctly excludes the witness profile in all cases: no nonsmooth factor, exactly one nonsmooth factor, and two nonsmooth factors. Connects equality of jump profiles almost everywhere to the required non-membership, for example using continuity of the profile representatives.
- **2 points: Structural restriction for constant mixtures.** Constructs the width-one input-adaptive witness and proves that the normal-derivative jump of any width-\(m\) constant-mixture representation agrees almost everywhere with a function in a class of at most \(2m\) shared-affine dictionary ridges. Correctly groups all activation-pair contributions while preserving the shared affine arguments.
- **3 points: Finite-dictionary exclusion and conclusion.** Proves that \(R(t)\tanh t\) is outside every finite dictionary-ridge class using the local analytic-versus-degree-two-polynomial decomposition, then derives the second strict containment and handles all \(d\ge2\) by restriction and extension. The analytic argument must apply to arbitrary real affine offsets and use an identity principle across zero, or an independently valid replacement argument.

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. Merely naming a jump argument or analyticity argument does not earn the corresponding full credit: the relevant profile restriction or non-membership must be derived. If a profile restriction is not established by one route but is independently proved by another valid argument, award downstream credit normally. A missing treatment of dimensions \(d>2\) is a minor omission only when the two-dimensional proof is otherwise complete and the restriction argument is immediate.

The profile restrictions are almost-everywhere statements, or equivalently statements about agreement away from finitely many intersection coordinates with continuous ridge-profile representatives. Do not require the actual jump to equal its continuous representative at every exceptional coordinate. Equality almost everywhere between continuous profiles suffices for equality everywhere. A solver may use this convention without introducing separate notation for representatives, provided the argument is mathematically sound. Constant affine arguments, identically zero factors, coincident singular lines, and zero coefficients are allowed by the task; no nondegeneracy assumption may be imposed to exclude them. Routine treatment of these cases may be implicit when the proof already covers them.
