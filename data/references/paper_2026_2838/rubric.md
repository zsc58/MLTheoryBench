# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **3 points:** Derive a target-independent weak certificate from learnability and establish polynomial depth. In the reference route, establish logarithmic confidence amplification, justify simultaneous one-sided validity for transcript-and-sample survivors using the conditional-distribution comparison, and perform a second union bound to fix one random seed and sample stream that works for every target containing S. Compile sample observations into actual queries so the final guarantee concerns all transcript-inducing concepts, not merely concepts containing S. Explain polynomial class-size control or an equally valid complexity argument.
- **3 points:** Recursively upgrade weak certificates to full compression. Prove constant-factor shrinkage and realizability of the remaining set, and explain why any concept inducing the entire transcript contains both the already certified points and the recursively certified remainder. Bound all tree paths, including nonrealizable branches, and show O(log(|S|+1)) rounds and polynomial depth.
- **3 points:** Construct the converse learner by taking the intersection over all concepts inducing the realized labeled transcript. Prove one-sidedness and containment of all sampled points. Count closures using labeled query locations and answers, including length-zero transcripts, rather than counting entire strategy trees. Derive the finite-class zero-empirical-error generalization bound, with a polynomial example/query budget uniform over epsilon,delta in (0,1).
- **1 point:** Establish the necessary polynomial complexity control. For the reference VC route, justify the hard prior, uniform posterior after conditioning on the ordered sample, at most 2^M response strings even for queries outside the shattered set, the per-string success count, and the resulting contradiction. Accept a valid alternative sufficient to close the polynomial-depth argument; the exact numerical VC constant is not itself part of the public target.

# Evaluator Notes

Accept any complete valid alternative proof. General residual error boosting is reconstructed in the GT to audit the selected support, but is not a mandatory additional solver obligation: confidence amplification at fixed error is sufficient for the characterization.

The transcript version space must not be silently restricted to hypotheses containing S; doing so makes the compression condition vacuous. A successful run for one target does not establish a tree that succeeds for every target containing S. Naming boosting, uniform success, compression, or VC counting without deriving the needed consequences is insufficient.

Uniform success controls false-negative error under D conditioned on each surviving concept's support. Its one-sided guarantee holds for every surviving nonempty concept; coverage of the whole input sample is obtained separately using the generating target and the uniform distribution on that sample.

Outputs are allowed outside H_d. Do not impose properness, polynomial running time, advance knowledge of D, or target-dependent choices of the compression tree. The converse counting class is fixed independently of the realized sample even though the selected strategy depends on that sample.

Allow harmless padding and positive constant floors in complexity bounds. Empty samples have depth-zero certificates; empty classes have no realizable samples or compatible learning pairs; singleton classes admit zero-query certification. A zero-call weak learner need not imply zero-query compression if an empty concept remains in the class. The supporting source estimate has been normalized accordingly. Treat isolated omissions of straightforward degenerate cases as minor when the rest of the proof is complete, but do not accept a division by zero, logarithm of zero, or unbounded branch as a completed argument.

All listed GT obligations are explicitly closed. There is no unresolved specialized dependency or private-proof quality warning.
