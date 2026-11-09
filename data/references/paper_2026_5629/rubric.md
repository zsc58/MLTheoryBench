# Scoring Guide

- **0:** No correct idea or relevant valid method.
- **1-2:** Nontrivial relevant ideas, but no complete correct proof step or useful conclusion.
- **3-7:** Some correct core steps or conclusions, but important steps are missing.
- **8-9:** Complete and essentially correct, with only readily repairable errors or omitted cases.
- **10:** Fully correct.

# Core Steps

- **2 points:** Shows the LayerNorm normalized vector has zero sum and rigorously deduces that its centered covariance annihilates \(\mathbf 1\), or gives an equivalent direct argument for the corresponding constant linear functional of the LayerNorm output.
- **3 points:** Correctly removes the bias, transports the kernel through \(D_\gamma\), and obtains \(C_{\mathrm{LN}}\gamma^{-1}=0\) and the normalized direction (**2 points**); proves \(C_{\mathrm{LN}}e_i=0\) for every zero scale coordinate (**1 point**). The zero-scale conclusion is a mandatory part of the task, including when all scale coordinates are zero.
- **3 points:** Rigorously establishes the RMSNorm obstruction. In the reference route, uses an admissible isotropic Gaussian input, proves that its radially normalized vector has covariance \(I_d\), and obtains \(D_\gamma^2\succ0\). Award equivalent credit for a valid alternative argument; neither a Gaussian witness nor a single positive-definite-output witness is mandatory if the required nonuniversality is otherwise established.
- **2 points:** Correctly concludes that for each fixed all-nonzero \(\gamma\), every proposed unit direction fails for at least one admissible input distribution, and thereby rules out a universal direction depending only on \(\gamma\).

# Evaluator Notes

Accept a complete valid alternative proof. Do not require the reference proof's incidental presentation choices. For example, a direct variance calculation may replace a covariance-matrix calculation.

All conclusions in the public task are required for full credit. Omitting the zero-scale case does not earn its allocated point; a brief, readily repairable omission is consistent with the 8-9 band.

Use centered covariance, not the uncentered second moment of a biased LayerNorm output. Do not require \(\mathbb EZ=0\); only its coordinate sum must vanish. No moment or positive-definiteness assumption on the LayerNorm input is available or necessary, because normalization bounds the output. Routine well-definedness may be implicit when the argument is otherwise valid.

The scale vectors may have negative coordinates. In the nonzero-scale parts, every coordinate must be nonzero, not merely the vector itself. Do not require the LayerNorm kernel to be one-dimensional, and do not accept the unsupported stronger assertion that RMSNorm output covariance is positive definite for every admissible positive-definite-covariance input.
